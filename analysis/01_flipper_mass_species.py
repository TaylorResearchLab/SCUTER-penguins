#!/usr/bin/env python3
"""SCUTER Work Unit 1: flipper length, body mass, and species.

This script is committed before execution so that the User and Agent B can inspect
exactly what will be run. It performs no automatic data acquisition. It uses only
the exact input committed at data/penguins.csv and aborts if the Git blob identity
does not match the registered upstream blob.
"""

from __future__ import annotations

import hashlib
import json
import platform
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy
from scipy import stats
import statsmodels
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.diagnostic import het_breuschpagan

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "penguins.csv"
RESULTS_DIR = ROOT / "results"
FIGURES_DIR = RESULTS_DIR / "figures"

EXPECTED_GIT_BLOB_SHA = "25b46d384bf81f8399188500ea54917bb49d8890"
EXPECTED_COLUMNS = [
    "species",
    "island",
    "bill_length_mm",
    "bill_depth_mm",
    "flipper_length_mm",
    "body_mass_g",
    "sex",
    "year",
]
PRIMARY_COLUMNS = ["species", "flipper_length_mm", "body_mass_g"]


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    header = f"blob {len(data)}\0".encode("utf-8")
    return hashlib.sha1(header + data).hexdigest()


def git_head() -> str | None:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
        ).strip()
    except Exception:
        return None


def json_dump(obj: dict, path: Path) -> None:
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def tidy_result(result, model_name: str, covariance: str) -> pd.DataFrame:
    names = list(result.model.exog_names)
    params = pd.Series(np.asarray(result.params), index=names)
    bse = pd.Series(np.asarray(result.bse), index=names)
    pvalues = pd.Series(np.asarray(result.pvalues), index=names)
    conf = np.asarray(result.conf_int(alpha=0.05))
    return pd.DataFrame(
        {
            "model": model_name,
            "covariance": covariance,
            "term": names,
            "estimate": params.values,
            "std_error": bse.values,
            "ci_low": conf[:, 0],
            "ci_high": conf[:, 1],
            "p_value": pvalues.values,
        }
    )


def linear_combination(result, weights: np.ndarray) -> dict:
    test = result.t_test(weights)
    ci = np.asarray(test.conf_int(alpha=0.05)).reshape(-1, 2)[0]
    return {
        "estimate": float(np.asarray(test.effect).reshape(-1)[0]),
        "std_error": float(np.asarray(test.sd).reshape(-1)[0]),
        "ci_low": float(ci[0]),
        "ci_high": float(ci[1]),
        "p_value": float(np.asarray(test.pvalue).reshape(-1)[0]),
    }


def species_slope_table(model, robust_result, species_levels: list[str]) -> pd.DataFrame:
    names = list(model.model.exog_names)
    base_term = "flipper_10mm_centered"
    base_idx = names.index(base_term)
    rows = []

    for covariance, result in [("OLS", model), ("HC3", robust_result)]:
        for species in species_levels:
            weights = np.zeros(len(names), dtype=float)
            weights[base_idx] = 1.0
            if species != species_levels[0]:
                candidates = [
                    i
                    for i, name in enumerate(names)
                    if base_term in name and f"[T.{species}]" in name
                ]
                if len(candidates) != 1:
                    raise RuntimeError(
                        f"Could not resolve one interaction term for species={species}: {candidates}"
                    )
                weights[candidates[0]] = 1.0
            row = linear_combination(result, weights)
            row.update({"covariance": covariance, "species": species})
            rows.append(row)

    return pd.DataFrame(rows)


def save_residual_diagnostics(model, model_name: str) -> None:
    fitted = np.asarray(model.fittedvalues)
    resid = np.asarray(model.resid)

    plt.figure(figsize=(7, 5))
    plt.scatter(fitted, resid, alpha=0.65)
    plt.axhline(0, linewidth=1)
    plt.xlabel("Fitted body mass (g)")
    plt.ylabel("Residual (g)")
    plt.title(f"Residuals vs fitted: {model_name}")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / f"{model_name}_residuals_vs_fitted.png", dpi=300)
    plt.close()

    fig = sm.qqplot(resid, line="45", fit=True)
    plt.title(f"Normal Q-Q: {model_name}")
    plt.tight_layout()
    fig.savefig(FIGURES_DIR / f"{model_name}_qq.png", dpi=300)
    plt.close(fig)


def main() -> None:
    RESULTS_DIR.mkdir(exist_ok=True)
    FIGURES_DIR.mkdir(exist_ok=True)

    observed_blob = git_blob_sha(DATA_PATH)
    if observed_blob != EXPECTED_GIT_BLOB_SHA:
        raise RuntimeError(
            f"Input identity failure: expected {EXPECTED_GIT_BLOB_SHA}, observed {observed_blob}"
        )

    df = pd.read_csv(DATA_PATH, na_values=["NA"])
    if list(df.columns) != EXPECTED_COLUMNS:
        raise RuntimeError(f"Unexpected columns: {list(df.columns)}")

    df = df.copy()
    df["source_csv_line"] = df.index + 2

    missing_primary = df[PRIMARY_COLUMNS].isna()
    keep_mask = ~missing_primary.any(axis=1)
    excluded = df.loc[~keep_mask, ["source_csv_line"] + PRIMARY_COLUMNS].copy()
    analytic = df.loc[keep_mask].copy()

    species_levels = sorted(analytic["species"].astype(str).unique().tolist())
    analytic["species"] = pd.Categorical(
        analytic["species"], categories=species_levels, ordered=False
    )

    qc = {
        "input_path": str(DATA_PATH.relative_to(ROOT)),
        "git_blob_sha": observed_blob,
        "raw_rows": int(len(df)),
        "columns": list(df.columns[:-1]),
        "primary_complete_case_rows": int(len(analytic)),
        "excluded_primary_rows": int((~keep_mask).sum()),
        "excluded_source_csv_lines": excluded["source_csv_line"].astype(int).tolist(),
        "missing_counts_primary": {
            col: int(df[col].isna().sum()) for col in PRIMARY_COLUMNS
        },
        "species_levels": species_levels,
        "species_counts_primary": {
            str(k): int(v)
            for k, v in analytic["species"].value_counts(sort=False).items()
        },
        "missing_data_rule": (
            "Complete cases for species, flipper_length_mm, and body_mass_g only; "
            "no imputation; missing sex/island/year does not exclude primary observations."
        ),
    }
    json_dump(qc, RESULTS_DIR / "input_qc.json")
    excluded.to_csv(RESULTS_DIR / "excluded_primary_rows.csv", index=False)

    analytic["flipper_10mm"] = analytic["flipper_length_mm"] / 10.0
    flipper_center = float(analytic["flipper_10mm"].mean())
    analytic["flipper_10mm_centered"] = analytic["flipper_10mm"] - flipper_center

    formulas = {
        "pooled": "body_mass_g ~ flipper_10mm",
        "species_adjusted": "body_mass_g ~ flipper_10mm_centered + C(species)",
        "species_interaction": "body_mass_g ~ flipper_10mm_centered * C(species)",
    }

    models = {
        name: smf.ols(formula, data=analytic).fit()
        for name, formula in formulas.items()
    }
    robust = {
        name: model.get_robustcov_results(cov_type="HC3")
        for name, model in models.items()
    }

    coef_tables = []
    for name, model in models.items():
        coef_tables.append(tidy_result(model, name, "OLS"))
        coef_tables.append(tidy_result(robust[name], name, "HC3"))
    pd.concat(coef_tables, ignore_index=True).to_csv(
        RESULTS_DIR / "model_coefficients.csv", index=False
    )

    fit_rows = []
    for name, model in models.items():
        lm_stat, lm_p, f_stat, f_p = het_breuschpagan(model.resid, model.model.exog)
        fit_rows.append(
            {
                "model": name,
                "formula": formulas[name],
                "n": int(model.nobs),
                "r_squared": float(model.rsquared),
                "adj_r_squared": float(model.rsquared_adj),
                "aic": float(model.aic),
                "bic": float(model.bic),
                "breusch_pagan_lm": float(lm_stat),
                "breusch_pagan_lm_p": float(lm_p),
                "breusch_pagan_f": float(f_stat),
                "breusch_pagan_f_p": float(f_p),
            }
        )
    pd.DataFrame(fit_rows).to_csv(RESULTS_DIR / "model_fit.csv", index=False)

    pooled_slope = float(models["pooled"].params["flipper_10mm"])
    adjusted_slope = float(
        models["species_adjusted"].params["flipper_10mm_centered"]
    )
    slope_delta = adjusted_slope - pooled_slope
    slope_pct_change = (
        100.0 * slope_delta / abs(pooled_slope) if pooled_slope != 0 else np.nan
    )

    slope_comparison = pd.DataFrame(
        [
            {
                "pooled_slope_g_per_10mm": pooled_slope,
                "species_adjusted_slope_g_per_10mm": adjusted_slope,
                "absolute_change_g_per_10mm": slope_delta,
                "percent_change_relative_to_abs_pooled": slope_pct_change,
                "flipper_center_10mm_units": flipper_center,
            }
        ]
    )
    slope_comparison.to_csv(RESULTS_DIR / "slope_comparison.csv", index=False)

    interaction_model = models["species_interaction"]
    interaction_robust = robust["species_interaction"]
    species_slopes = species_slope_table(
        interaction_model, interaction_robust, species_levels
    )
    species_slopes.to_csv(RESULTS_DIR / "species_slopes.csv", index=False)

    comparison = anova_lm(models["species_adjusted"], interaction_model)
    comparison = comparison.reset_index().rename(columns={"index": "model_row"})
    comparison["species_adjusted_aic"] = models["species_adjusted"].aic
    comparison["species_interaction_aic"] = interaction_model.aic
    comparison["species_adjusted_r2"] = models["species_adjusted"].rsquared
    comparison["species_interaction_r2"] = interaction_model.rsquared
    comparison.to_csv(RESULTS_DIR / "model_comparison.csv", index=False)

    influence_frame = interaction_model.get_influence().summary_frame().copy()
    influence_frame.insert(0, "source_csv_line", analytic["source_csv_line"].to_numpy())
    influence_frame.insert(1, "species", analytic["species"].astype(str).to_numpy())
    influence_frame.insert(
        2, "flipper_length_mm", analytic["flipper_length_mm"].to_numpy()
    )
    influence_frame.insert(3, "body_mass_g", analytic["body_mass_g"].to_numpy())
    influence_frame = influence_frame.sort_values("cooks_d", ascending=False)
    influence_frame.to_csv(RESULTS_DIR / "influence.csv", index=False)

    pearson_r, pearson_p = stats.pearsonr(
        analytic["flipper_length_mm"], analytic["body_mass_g"]
    )

    plt.figure(figsize=(7, 5))
    plt.scatter(
        analytic["flipper_length_mm"], analytic["body_mass_g"], alpha=0.65
    )
    x_grid = np.linspace(
        analytic["flipper_length_mm"].min(),
        analytic["flipper_length_mm"].max(),
        200,
    )
    pooled_grid = pd.DataFrame({"flipper_10mm": x_grid / 10.0})
    plt.plot(x_grid, models["pooled"].predict(pooled_grid))
    plt.xlabel("Flipper length (mm)")
    plt.ylabel("Body mass (g)")
    plt.title("Pooled flipper length and body mass")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "pooled_relationship.png", dpi=300)
    plt.close()

    plt.figure(figsize=(7, 5))
    for species in species_levels:
        d = analytic.loc[analytic["species"] == species]
        plt.scatter(d["flipper_length_mm"], d["body_mass_g"], alpha=0.65, label=species)
        x_species = np.linspace(
            d["flipper_length_mm"].min(), d["flipper_length_mm"].max(), 100
        )
        pred = pd.DataFrame(
            {
                "flipper_10mm_centered": x_species / 10.0 - flipper_center,
                "species": pd.Categorical(
                    [species] * len(x_species), categories=species_levels
                ),
            }
        )
        plt.plot(x_species, interaction_model.predict(pred))
    plt.xlabel("Flipper length (mm)")
    plt.ylabel("Body mass (g)")
    plt.title("Flipper length and body mass by species")
    plt.legend(title="Species")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "species_relationships.png", dpi=300)
    plt.close()

    for name, model in models.items():
        save_residual_diagnostics(model, name)

    environment = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "python": platform.python_version(),
        "platform": platform.platform(),
        "numpy": np.__version__,
        "pandas": pd.__version__,
        "scipy": scipy.__version__,
        "statsmodels": statsmodels.__version__,
        "matplotlib": matplotlib.__version__,
    }
    json_dump(environment, RESULTS_DIR / "runtime_environment.json")

    run_manifest = {
        "status": "completed",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "command": "python analysis/01_flipper_mass_species.py",
        "git_head_at_run": git_head(),
        "input_git_blob_sha": observed_blob,
        "formulas": formulas,
        "primary_complete_case_n": int(len(analytic)),
        "pooled_pearson_r": float(pearson_r),
        "pooled_pearson_p": float(pearson_p),
        "results_directory": "results",
        "interpretation_status": (
            "UNREVIEWED. Script execution does not constitute scientific acceptance."
        ),
    }
    json_dump(run_manifest, RESULTS_DIR / "run_manifest.json")

    print("Analysis completed. Results are unreviewed and require SCUTER review/User acceptance.")
    print(f"Input Git blob: {observed_blob}")
    print(f"Primary complete-case N: {len(analytic)}")
    print(f"Results: {RESULTS_DIR}")


if __name__ == "__main__":
    main()
