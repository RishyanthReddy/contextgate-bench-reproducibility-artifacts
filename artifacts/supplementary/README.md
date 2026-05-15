# ContextGate-Bench Supplementary Files

This directory contains supplementary files for the ContextGate-Bench submission package.

## Supplementary File 2: Supplementary Tables S1-S39

- File: `Supplementary_Tables_S1_to_S39.xlsx`
- Contents: one Excel workbook with an Index sheet and worksheets named `Table S1` through `Table S39`.
- Source: generated CSV tables from `artifacts/manuscript_tables/`.
- Notes: generated split tables are merged into the corresponding numbered worksheet:
  - `Table S25`: gate-failure summary and decomposition.
  - `Table S26`: threshold operating points and axis sensitivity.
  - `Table S30`: route aggregation trace and dataset-task performance disaggregation.
  - `Table S33`: threshold grid detail, stress-family accounting, and claim-survival reconciliation.

## Supplementary Note/File Map

Use these manuscript labels instead of repository-style file paths:

| Manuscript label | Repository source |
|---|---|
| Supplementary Note 1: External Review Gap Analysis | `artifacts/reviewer_hardening/cp_q8_6_gap_ledger.md` |
| Supplementary File 1: Methodological Parameter Cards | `artifacts/reviewer_hardening/method_cards/` |
| Supplementary Note 2: Formal ContextGate Route Contract | `artifacts/reviewer_hardening/contextgate_decision_contract.md` |
| Supplementary Note 3: Threshold Calibration and Detectability Audit | `artifacts/reviewer_hardening/threshold_calibration_detectability_audit.md` |
| Supplementary Note 4: Leakage, Downgrade, and Residualization Audit | `artifacts/reviewer_hardening/leakage_downgrade_residualization_audit.md` |
| Supplementary Note 5: SOTA Method Feasibility Ledger | `artifacts/reviewer_hardening/sota_feasibility_ledger.md` and `.csv` |
| Supplementary Note 6: Literature Concordance and Claim Boundary Audit | `artifacts/reviewer_hardening/paper_wizard_literature_concordance_audit.md` and `.csv` |
| Supplementary Note 7: Rerun Decision Log | `artifacts/reviewer_hardening/modal_rerun_decision_log.md` and `.csv`; `artifacts/reviewer_hardening/cp_q8_7_modal_rerun_decision_log.md` and `.csv` |
| Supplementary File 2: Supplementary Tables S1-S39 | `artifacts/supplementary/Supplementary_Tables_S1_to_S39.xlsx` |
