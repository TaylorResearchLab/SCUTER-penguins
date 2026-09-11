# Bounded First Analysis Plan

Status: proposed, not yet executed.

## Scientific question

Among Palmer penguins, what is the relationship between flipper length and body mass, and how does that relationship change when species is taken into account?

The analysis will not presuppose the sign, magnitude, statistical significance, or biological interpretation of any association.

## Primary analytic set

Use the exact committed `data/penguins.csv`. Include observations with non-missing values for `species`, `flipper_length_mm`, and `body_mass_g`. Do not impute. Use this same complete-case set for all three primary models so changes across models cannot be attributed to changing observations.

Before model fitting, record:

- Git blob identity of the input;
- row and column counts;
- species labels/counts;
- relevant missingness;
- included/excluded row identities and reasons;
- runtime software versions.

## Model sequence

### Model 1: pooled relationship

Ordinary least squares:

`body_mass_g ~ flipper_length_mm`

Report the slope scaled as grams of body mass per 10 mm of flipper length, 95% confidence interval, R², residual diagnostics, and a scatterplot with the fitted pooled line. Pearson correlation may be reported as a descriptive supplement, not as the sole analysis.

### Model 2: species-adjusted common-slope relationship

Ordinary least squares:

`body_mass_g ~ flipper_length_mm + species`

Use a centered/scaled flipper-length term for interpretable numeric scaling while preserving the slope. Species is a categorical fixed effect. The flipper coefficient represents a common within-species slope under the parallel-slopes assumption.

Report the adjusted flipper slope per 10 mm, 95% confidence interval, R², species coefficients with the reference species and centering convention stated, and the absolute and percentage change in the flipper slope relative to Model 1.

### Model 3: species-specific slopes

Ordinary least squares:

`body_mass_g ~ flipper_length_mm * species`

Report species-specific slopes per 10 mm with 95% confidence intervals. Compare Model 3 with Model 2 using a nested-model partial F test, AIC, R², and effect estimates. Statistical significance will not be used as the sole definition of scientific importance.

## How species impact will be characterized

No single arbitrary threshold will automatically decide whether species is "material." The project will quantify three pre-specified dimensions and the User will adjudicate interpretation:

1. **Magnitude shift:** absolute and percentage change between the pooled flipper coefficient and the species-adjusted common slope, including confidence intervals where feasible.
2. **Explanatory contribution:** change in model R²/AIC when species is added, interpreted descriptively rather than as proof of mechanism.
3. **Slope heterogeneity:** species-specific slopes and their uncertainty, plus the Model 2 versus Model 3 comparison.

A reversal of coefficient sign, major attenuation/amplification relative to its uncertainty, or clearly different species-specific slopes would be explicitly flagged as interpretation-changing. Absence of such behavior will also be reported rather than assumed.

## Diagnostics and sensitivity

For each primary model, inspect residual-versus-fitted and Q-Q plots. Assess leverage and Cook's distance. Record influential observations rather than silently removing them.

Evaluate heteroskedasticity. HC3 robust standard errors will be generated as a sensitivity result and emphasized if ordinary OLS variance assumptions appear inadequate. Primary coefficient point estimates will not be changed solely because robust covariance is used.

No observation will be removed as an outlier without a separately documented, scientifically justified User decision.

## Biological interpretation boundary

The primary analysis is descriptive/associational. It is not a causal analysis of body mass, a validated body-condition model, or a pure structural-allometry analysis. Published work indicates body mass is seasonally plastic and that sex is morphometrically important in these penguins. Sex is therefore an important possible secondary/sensitivity variable but is outside this bounded primary analysis unless the User expands scope. Island and year are also deferred.

## Required outputs

- `results/input_qc.json`
- `results/model_coefficients.csv`
- `results/model_fit.csv`
- `results/species_slopes.csv`
- `results/model_comparison.csv`
- `results/influence.csv`
- diagnostic figures and raw-data/model figures under `results/figures/`
- `results/runtime_environment.json`
- a concise machine-readable/run summary linking the input blob and code commit

## Acceptance criteria before Agent B review

Work Unit 1 analysis is ready for Agent B review only if all of the following are true:

- the input file passes identity verification against blob SHA `25b46d384bf81f8399188500ea54917bb49d8890`;
- analytic inclusion/exclusion is explicit and reproducible;
- Models 1-3 use the same primary complete-case set;
- effect sizes and 95% confidence intervals are reported, not p-values alone;
- the change from pooled to species-adjusted relationship is quantified;
- species-specific slope heterogeneity is evaluated;
- diagnostic and influence outputs are preserved;
- assumptions and limitations are recorded;
- executable scientific code and outputs are committed to the project repository;
- the Collaboration Log records the exact run command, code commit, output commit, and review assignment;
- Agent A does not self-approve the scientific conclusion.

User acceptance is required before any scientific conclusion is written into the Manubot manuscript or released as a project conclusion.
