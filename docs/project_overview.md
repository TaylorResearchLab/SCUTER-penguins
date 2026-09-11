# Project Overview

## Scientific question

Among Palmer penguins, what is the relationship between flipper length and body mass, and how does that relationship change when species is taken into account?

## Authority and participants

- User: Deanne Taylor. Retains scientific direction, adjudication, acceptance, merge, and release authority.
- Agent A: OpenAI GPT-5.6 Sol, lead for Work Unit 1.
- Agent B: Claude, designated by the User for subsequent independent inspection/review.
- Session ID: `SCUTER-penguins-A1-WU1-2026-09-11`.
- Exposure status: this is a new project; Agent A did not import scientific conclusions, analyses, or project decisions from prior chats or other projects.

## Governing protocol

User-supplied SCUTER v0.2.1-dev. Work Unit 1 uses a custom prior-art coverage declaration bounded to: dataset provenance; prior analyses of the flipper-length/body-mass variable pair; species differences relevant to interpretation; and biological assumptions about the two measurements. No novelty claim is permitted from this work unit.

## Current state

Pre-analysis. No target relationship has been estimated, interpreted, or accepted.

## Preserved dataset

The exact project input is committed at `data/penguins.csv` and is byte-identical at the Git-blob level to the upstream file:

- upstream repository: `allisonhorst/palmerpenguins`
- upstream commit: `8957207b78d6ccd1b4654a9dd9c9041b657478ab`
- upstream path: `inst/extdata/penguins.csv`
- upstream/project Git blob SHA: `25b46d384bf81f8399188500ea54917bb49d8890`
- project preservation commit: `ecadb53f77ebcecd8f07822c32a985e9ecfd739a`
- retrieval/preservation date: 2026-09-11

An additional exact copy is attached to the Notion Project Overview.

## Primary missing-data rule

The bounded primary analysis will use complete cases for `species`, `flipper_length_mm`, and `body_mass_g` only. Neither morphometric measurement will be imputed. Missing values in `sex`, `island`, or other non-primary variables will not cause exclusion from the primary models. The executable analysis must emit the exact exclusion count and row identities before fitting models.

## User-gated scope

Sex is biologically relevant based on prior art but is not part of the primary question. A sex-adjusted sensitivity analysis is deferred unless the User expands the work unit. Island and year are likewise deferred.

## Release rule

Agent A cannot accept its own scientific conclusions. Results require review routing under SCUTER and User acceptance before release or before conclusions are written into the Manubot manuscript.
