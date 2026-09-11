# Project Overview

## Scientific question

Among Palmer penguins, what is the relationship between flipper length and body mass, and how does that relationship change when species is taken into account?

## Authority and participants

- User: Deanne Taylor. Retains scientific direction, adjudication, acceptance, merge, and release authority.
- Agent A: OpenAI GPT-5.6 Sol, lead for Work Unit 1.
- Agent B: Claude, designated by the User for subsequent independent inspection/review.
- Session ID: `SCUTER-penguins-A1-WU1-2026-09-11`.
- Exposure status: this is a new project; Agent A did not import scientific conclusions, analyses, or project decisions from prior chats or other projects. Agent A has read the full User-supplied SCUTER v0.2.1-dev Skill, including the complete protocol and record/review guidance.

## Governing protocol

User-supplied SCUTER v0.2.1-dev. Work Unit 1 uses a custom prior-art coverage declaration bounded to: dataset provenance; prior analyses of the flipper-length/body-mass variable pair; species differences relevant to interpretation; and biological assumptions about the two measurements. No novelty claim is permitted from this work unit.

Under SCUTER `PRIOR-ART-LINEAGE` item 7, Agent A's initial searches are preliminary exploration for propositions Agent A introduced. They do not independently establish lineage for those statements. Agent B must perform or independently establish the required lineage search/review before release.

## Current state

Pre-analysis. No target relationship has been estimated, interpreted, or accepted. The bounded first analysis plan remains Proposed until the User accepts or revises it.

## Preserved dataset

The exact project input is committed at `data/penguins.csv` and is byte-identical at the Git-blob level to the upstream file:

- upstream repository: `allisonhorst/palmerpenguins`
- upstream commit: `8957207b78d6ccd1b4654a9dd9c9041b657478ab`
- upstream path: `inst/extdata/penguins.csv`
- upstream/project Git blob SHA: `25b46d384bf81f8399188500ea54917bb49d8890`
- project preservation commit: `ecadb53f77ebcecd8f07822c32a985e9ecfd739a`
- retrieval/preservation date: 2026-09-11

An additional exact copy is attached to the Notion Project Overview. The raw GitHub URL is the CSV file itself; a browser renders it as plain text.

## Primary missing-data rule

The bounded primary analysis will use complete cases for `species`, `flipper_length_mm`, and `body_mass_g` only. Neither morphometric measurement will be imputed. Missing values in `sex`, `island`, or other non-primary variables will not cause exclusion from the primary models. The executable analysis must emit the exact exclusion count and row identities before fitting models.

## User-gated scope

Sex is biologically relevant based on provisional prior-art framing but is not part of the primary question. A sex-adjusted sensitivity analysis is deferred unless the User expands the work unit. Island and year are likewise deferred.

## Repository state

The project repository contains the exact input, provenance record, proposed analysis plan, and committed but unexecuted analysis script. Current pre-analysis setup head after adding runtime requirements was `e95f95cd3a2f461e30a49ed81508839228d8fabf`; subsequent documentation-only synchronization commits do not change the scientific analysis code.

The companion Manubot repository is `TaylorResearchLab/SCUTER-penguins-manubot`. It is configured as a functional pre-results Manubot repository at setup commit `3e9e2185ec9fbadbe5ad241fd58cdc926b0da0aa`. Its Abstract, Introduction, Methods, Results, and Discussion are intentionally free of scientific conclusions pending analysis, review, and User acceptance.

Agent-initiated GitHub writes are performed through the User-authenticated integration and are recorded in the Collaboration Log because GitHub commit metadata may not distinguish them from manual User actions. Future scientific result changes should use a reviewable branch/PR pathway where feasible; branch-protection state has not been independently verified by this connector.

## Release rule

Agent A cannot accept its own scientific conclusions. All proposed references remain Provisional until second-participant identity/claim checks and User disposition are recorded. Prior-art lineage requirements must also be satisfied by the appropriate different participant. Results require review routing under SCUTER and User acceptance before release or before conclusions are written into the Manubot manuscript.
