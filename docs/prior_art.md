# Prior Art and Dataset Provenance

Search date: 2026-09-11

Status: pre-analysis. This record frames the scientific question but does not substitute for analysis of the exact preserved project dataset.

## Coverage declaration

Custom Work Unit 1 coverage, as bounded by the User's assignment:

1. source and provenance of the Palmer Penguins data;
2. prior work relevant to flipper length, body mass, and their biological interpretation;
3. species differences relevant to morphometrics;
4. prior use of the exact flipper-length/body-mass variable pairing and species-aware modeling.

No novelty claim is permitted from this work unit. The full proposition-level search record is maintained in the Notion Prior-Art Search Record database.

## Search resources and strategy

Resources searched included PLOS ONE, PubMed, Zenodo, the official `allisonhorst/palmerpenguins` repository and package website, direct DOI resolution for the upstream Environmental Data Initiative records, Cornell INFO 2950 teaching materials, and general scholarly web search. Search terms included the Gorman et al. paper title; the package DOI; each upstream EDI DOI/hash; combinations of `Palmer Penguins`, `flipper length`, `body mass`, `species`, and `regression`; and terms linking penguin flipper length to structural size and body mass to body condition.

## Dataset lineage

The public simplified `penguins` dataset is distributed by the `palmerpenguins` package. Official package documentation attributes the measurements to Palmer Station Antarctica LTER and Kristen Gorman and identifies three species-specific Environmental Data Initiative datasets from 2007-2009. The associated primary paper is Gorman, Williams, and Fraser (2014).

The project input is not a floating package download. It is `inst/extdata/penguins.csv` pinned to upstream commit `8957207b78d6ccd1b4654a9dd9c9041b657478ab`. The committed project copy has Git blob SHA `25b46d384bf81f8399188500ea54917bb49d8890`, identical to the upstream blob.

### Upstream source records

- Adélie: PAL-LTER/Gorman 2020, version 5, DOI `10.6073/pasta/98b16d7d563f265cb52372c8ca99e60f`.
- Gentoo: PAL-LTER/Gorman 2020, version 5, DOI `10.6073/pasta/7fca67fb28d56ee2ffa3d9370ebda689`.
- Chinstrap: PAL-LTER/Gorman 2020, version 6, DOI `10.6073/pasta/c14dfcfada8ea13a17536e73eb6fbe9e`.

Direct DOI resolution for these three EDI records returned HTTP 403 in Agent A's web environment. Their identities are therefore recorded as Provisional and require an independent authoritative-record check before reference validation is complete.

## Primary biological prior art

### Gorman, Williams & Fraser 2014

Gorman KB, Williams TD, Fraser WR. *Ecological Sexual Dimorphism and Environmental Variability within a Community of Antarctic Penguins (Genus Pygoscelis).* PLOS ONE 9(3):e90081. DOI `10.1371/journal.pone.0090081`.

Agent A verified the publisher record. Adults were sampled at study nests at the one-egg stage. Right flipper length was measured with a ruler and body mass with Pesola spring scales. The paper documents interspecific differences in morphometric/sexual-size patterns and explicitly cautions that body mass is plastic across the annual cycle. These are established prior findings. They do not establish the pooled or species-adjusted flipper-length/body-mass relationship in the exact project analysis.

### Viblanc et al. 2012

Viblanc VA et al. *Body girth as an alternative to body mass for establishing condition indexes in field studies: a validation in the king penguin.* Physiological and Biochemical Zoology 85(5):533-542. DOI `10.1086/667540`; PMID `22902382`.

Agent A verified the PubMed record and abstract. The study supports a distinction between structural-size information from measures including flipper/bill length and the use of body mass in body-condition/energetic-state analyses. It is used here only to constrain interpretation, not to assume the direction or strength of the Palmer Penguins association.

## Exact-question prior art

The official palmerpenguins examples already visualize body mass against flipper length with species encoded. Cornell INFO 2950 materials explicitly use the same response-predictor pair for regression and use the Palmer Penguins data to teach multiple-predictor and interaction models. These are relevant prior analytic uses but not primary biological evidence.

Disposition: the project will not claim novelty for pairing these variables, plotting them by species, or fitting regression models. Numerical results from teaching examples will not be imported into this project and will not substitute for analysis of `data/penguins.csv`.

## Provisional reference status

Under SCUTER, every proposed reference remains Provisional until independent bibliographic/claim correspondence review and User disposition. The Notion Citation Ledger records this status. Gorman 2014, Viblanc 2012, and the Zenodo package record received Agent A identity/claim checks. The three EDI dataset records still require direct or independent authoritative-record verification.
