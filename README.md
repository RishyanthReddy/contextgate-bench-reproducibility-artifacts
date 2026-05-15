# ContextGate-Bench Reproducibility Artifacts

This repository provides reviewer-accessible artifacts for the ContextGate-Bench
manuscript. ContextGate-Bench is a benchmark and decision framework for auditing
when spatial neighbor context should be used in imaging-based spatial
transcriptomic prediction workflows.

The repository contains the tables, schemas, validation outputs, figure exports,
and scripts needed to trace the manuscript claims. The manuscript source and
compiled PDF are not distributed here before journal-submission clearance.

## Contents

- `artifacts/results_reports/`: registered result tables, schemas, summaries,
  and route-decision reports.
- `artifacts/manuscript_tables/`: manuscript and supplementary table fragments
  plus the table manifest.
- Reviewer evidence records: decision contract, method cards, threshold audits,
  validation ledgers, and claim-boundary records.
- `artifacts/scripts/`: scripts used to rebuild manuscript tables and data
  figures from registered artifacts.
- `artifacts/figures_singles/`: PDF/PNG figure exports and the figure manifest.
- `artifacts/supplementary/`: supplementary-file index, Supplementary File 2
  (`Supplementary_Tables_S1_to_S39.xlsx`), and Supplementary File 3
  with additive validation tables.
- `artifacts/manuscript/`: manuscript-remediation plans and review ledgers only;
  this directory does not contain the full submitted manuscript.

## Reproduce Main Tables And Figures

The primary table and figure builders are included under `artifacts/scripts/`.
From the repository root, run:

```bash
python artifacts/scripts/build_contextgate_manuscript_tables.py
python artifacts/scripts/build_contextgate_publication_figures.py
```

The supplementary workbooks are provided directly in `artifacts/supplementary/`.
The figure manifest is available at
`artifacts/figures_singles/publication_figure_manifest.json`, and the table
manifest is available at
`artifacts/manuscript_tables/manuscript_table_manifest.json`.

## Evidence Map

The main decision contract and calibration audit are included with the reviewer
evidence records in the artifact tree.

Additive validation records include the bounded marker-derived GSE311609 replay,
expanded synthetic ladder, 10 selected lung-section NSCLC CD274 expansion, and
LIANA+/COMMOT adapter feasibility probe. Manuscript labels and source locations
are listed in `artifacts/supplementary/README.md`.

## Data Access

This repository contains derived benchmark artifacts and validation outputs.
Public spatial transcriptomics datasets should be accessed from their original
public repositories or from the cached data locations described by the dataset
manifests and supplementary tables. Datasets rejected for access or schema
reasons are retained in the rejected registry and are not used for manuscript
claims.

## Known Limitations

- The primary executed benchmark covers targeted-panel, imaging-based CosMx and
  Xenium datasets.
- The GSE311609 evidence is bounded marker-derived validation, not full
  41-section validation.
- The LIANA+/COMMOT adapter probe produced no claim-eligible native adapter
  output; mature-adapter confirmation is not claimed.
- Synthetic ladders validate evaluator behavior and detectability under
  registered controls; they do not prove real communication biology in every
  dataset.

## Versioned Snapshots

The original review snapshot and additive validation evidence snapshot are
pinned as repository tags.

No archival DOI is claimed for this repository snapshot. The public GitHub tags
provide timestamped validation records for review access.
