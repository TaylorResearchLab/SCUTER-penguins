# SCUTER Penguins

Reproducible SCUTER-governed analysis of Palmer Penguins morphometrics.

## Scientific question

Among Palmer penguins, what is the relationship between flipper length and body mass, and how does that relationship change when species is taken into account?

## Governance and status

This project follows the user-supplied SCUTER v0.2.1-dev instructions. Deanne Taylor is the User and retains scientific direction, adjudication, acceptance, merge, and release authority. Agent A is OpenAI GPT-5.6 Sol for Work Unit 1. Claude is designated as Agent B for subsequent review.

**Current state: pre-analysis.** No target association has been estimated or accepted. Work Unit 1 is limited to project setup, prior-art review, dataset provenance/preservation, and a proposed first-analysis specification.

Durable scientific record: https://app.notion.com/p/3d829187800880ae9cd0fb1c531f8eea

## Preserved public input

The intended input is `inst/extdata/penguins.csv` from `allisonhorst/palmerpenguins`, pinned to:

- upstream commit: `8957207b78d6ccd1b4654a9dd9c9041b657478ab`
- upstream Git blob SHA: `25b46d384bf81f8399188500ea54917bb49d8890`
- source path: `inst/extdata/penguins.csv`
- immutable source URL: `https://raw.githubusercontent.com/allisonhorst/palmerpenguins/8957207b78d6ccd1b4654a9dd9c9041b657478ab/inst/extdata/penguins.csv`

An exact copy retrieved from that pinned URL on 2026-09-11 is attached to the Notion Project Overview. Before any model is fit, analysis code will verify the input identity and record the analytic exclusions.

## Repository layout

- `docs/project_overview.md`: bounded scope, authority, current state, and acceptance criteria
- `docs/prior_art.md`: search strategy, source dispositions, and provenance review
- `docs/analysis_plan.md`: proposed first analysis, without results
- `data/README.md`: input provenance and preservation record
- `analysis/`: executable scientific code once the analysis work unit is authorized
- `results/`: generated outputs, not manually edited

The Manubot repository is separate and will not receive scientific conclusions until supporting analyses are completed, independently reviewed as appropriate, and accepted by the User.
