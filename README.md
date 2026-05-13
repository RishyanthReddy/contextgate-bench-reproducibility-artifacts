# ContextGate-Bench Reproducibility Artifacts

This public repository provides reviewer-accessible artifacts for the ContextGate-Bench manuscript.
It contains reproducibility tables, figure exports, hardened-evidence audit
artifacts, and generation scripts. The manuscript source and compiled paper PDF
are intentionally not published here before journal submission clearance.

Included contents:

- `artifacts/results_reports/`: registered CP-Q and CP-R result tables, schemas, summaries, and reports.
- `artifacts/manuscript_tables/`: generated manuscript and supplementary table fragments plus the table manifest.
- `artifacts/reviewer_hardening/`: decision contract, method cards, threshold audits, rerun ledgers, and reviewer-hardening ledgers.
- `artifacts/scripts/`: table and publication figure generation scripts.
- `artifacts/figures_singles/`: generated PDF/PNG figure exports and publication figure manifest.
- `artifacts/h7_overleaf_figures_singles/`: H7 Overleaf-ready refreshed data figures and figure-action manifest. Figure 1 and the graphical abstract are intentionally excluded because they are author-supplied draw.io assets.
- `artifacts/supplementary/`: journal-facing supplementary-file index, combined Excel workbook `Supplementary_Tables_S1_to_S39.xlsx`, and additive hardening workbook `Supplementary_Tables_S40_to_S44_Hardening.xlsx`.
- `artifacts/manuscript/`: reviewer-remediation plans only. The full manuscript source and PDF are intentionally withheld from this public repository pending author and submission clearance.

The main decision contract is `artifacts/reviewer_hardening/contextgate_decision_contract.md`. The threshold calibration audit is `artifacts/reviewer_hardening/threshold_calibration_detectability_audit.md`.

Additive hardening artifacts are provided under:

- `artifacts/reviewer_hardening/h5d_gse311609_marker_replay/`: bounded marker-derived GSE311609 replay with one NSCLC CD274 `context_allowed` route and one breast CXCL12/CXCR4 abstention.
- `artifacts/reviewer_hardening/h6_expanded_synthetic_ladder/`: expanded synthetic ladder spanning additional neighbor mechanisms.
- `artifacts/reviewer_hardening/h6_5a_nsclc_cd274_section_expansion/`: 10 selected lung-section expansion for the NSCLC CD274 route.
- `artifacts/reviewer_hardening/h6_5b_single_adapter_probe/`: LIANA+/COMMOT adapter feasibility probe documenting zero claim-eligible native adapter rows because the required native packages were unavailable.
- `artifacts/reviewer_hardening/pre_h7_hardening_results_verification.md`: consolidated hardening metrics and claim-boundary checklist.

The original review snapshot remains pinned by the tag `review-snapshot-2026-05-07`. The hardened pre-H7 artifact snapshot is intended to be pinned by the tag `hardened-pre-h7-evidence-complete-2026-05-13` after this README update is pushed. No archival DOI is claimed in this repository snapshot unless or until a separate archival deposit is minted; this public GitHub repository supplies the externally timestamped review-access artifact package.

Note: generated table fragments remain available under `artifacts/manuscript_tables/` as reproducibility artifacts, but the full manuscript `.tex` source and compiled paper PDF are not published here to avoid premature redistribution of manuscript text.
