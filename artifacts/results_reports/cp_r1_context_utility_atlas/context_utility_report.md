# CP-R1 Context Utility Atlas

This registry-backed atlas converts previous CellPack evidence into a
conservative routing target. Strict biological context is counted only
when a strict gate passed; positive controls and localized leads remain
non-proof evidence.

## Summary

- Selected artifacts: 781
- Runs: 23
- Datasets: 6
- Strict positive runs: 0
- Positive-control runs: 1
- Localized exploratory runs: 2
- Negative-context runs: 11

## Evidence Classes

- `borderline_preflight`: 4
- `coverage_only`: 4
- `insufficient_evidence`: 1
- `localized_exploratory`: 2
- `negative_context`: 11
- `positive_control_only`: 1

## Dataset Summary

- `cosmx_6k_bcc_yerly_2024`: runs=4, max CUS=0.10, strict=0, localized=0, negative=2
- `cosmx_nsclc_ffpe_v1`: runs=2, max CUS=0.10, strict=0, localized=0, negative=0
- `gse277782_cosmx_pdac_metastasis`: runs=6, max CUS=0.35, strict=0, localized=1, negative=1
- `gse310352_cosmx_pdac_1k`: runs=3, max CUS=0.35, strict=0, localized=1, negative=2
- `xenium_breast_biomarkers_v1`: runs=3, max CUS=0.00, strict=0, localized=0, negative=3
- `xenium_breast_v1`: runs=5, max CUS=0.70, strict=0, localized=0, negative=3

## Claim Boundary

CP-R1 does not reopen the old always-context claim. It prepares CP-R2
router labels by separating strict positives, positive controls,
localized exploratory leads, and negative-context runs.

Confidence/FDR metadata is preserved from registered commands when it
exists. Registry-only rows without underlying interval tables are marked
`registry_metadata_only` and must not be treated as interval-level proof.

No strict biological context-positive run is present in this atlas.
That is expected after the CP-6L pivot and is exactly why the router
must learn abstention and expression-only behavior before compression.
