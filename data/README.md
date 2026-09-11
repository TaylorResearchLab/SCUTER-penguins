# Data Provenance and Preservation

## Preserved analysis input

File: `data/penguins.csv`

This file is an exact copy of:

- repository: `allisonhorst/palmerpenguins`
- commit: `8957207b78d6ccd1b4654a9dd9c9041b657478ab`
- source path: `inst/extdata/penguins.csv`
- Git blob SHA: `25b46d384bf81f8399188500ea54917bb49d8890`
- retrieval/preservation date: 2026-09-11

After committing the project copy, the GitHub connector re-read `data/penguins.csv` and returned the same Git blob SHA, verifying byte-level identity under Git's blob-hash definition.

The source file has 344 data rows and eight columns: `species`, `island`, `bill_length_mm`, `bill_depth_mm`, `flipper_length_mm`, `body_mass_g`, `sex`, and `year`. Source inspection identifies two rows with missing flipper length and body mass; the executable analysis must independently reproduce and record all primary exclusions before model fitting.

## Public-source lineage

The simplified data are distributed by the `palmerpenguins` package and derive from Palmer Station Antarctica LTER/Kristen Gorman measurements. Official package documentation identifies three upstream Environmental Data Initiative datasets:

- Adélie, version 5: DOI `10.6073/pasta/98b16d7d563f265cb52372c8ca99e60f`
- Gentoo, version 5: DOI `10.6073/pasta/7fca67fb28d56ee2ffa3d9370ebda689`
- Chinstrap, version 6: DOI `10.6073/pasta/c14dfcfada8ea13a17536e73eb6fbe9e`

Associated primary publication:

Gorman KB, Williams TD, Fraser WR (2014). *Ecological Sexual Dimorphism and Environmental Variability within a Community of Antarctic Penguins (Genus Pygoscelis).* PLOS ONE 9(3): e90081. DOI `10.1371/journal.pone.0090081`.

Package archive:

Horst AM, Hill AP, Gorman KB (2020). `palmerpenguins` v0.1.0. DOI `10.5281/zenodo.3960218`.

Reference-validation status is maintained in the Notion Citation Ledger. The EDI records remain Provisional because direct DOI resolution returned HTTP 403 in Agent A's environment and requires an independent authoritative-record check.
