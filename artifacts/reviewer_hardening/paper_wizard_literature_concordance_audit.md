# Paper-Wizard Literature-Concordance Mini-Audit

Task: CP-Q8.7G

Purpose: address the route-ground-truth independence concern without
overclaiming. This audit does not create independent biological ground truth
for real-data routes. It records whether selected published expectations are
compatible with the ContextGate-Bench decision boundary.

## Scope

- Inputs: current manuscript, CP-Q5 route decisions, Supplementary Tables
  S24-S26, CP-Q8.6 related-work expansion, and existing bibliography entries.
- Output interpretation: concordant, downgraded, or abstained.
- Boundary: these rows are literature-anchored sanity checks, not expert
  adjudication, not wet-lab validation, and not a substitute for future
  pre-registered real-data route labels.

## Audit Rows

| Anchor | Published expectation | ContextGate-Bench observation | Concordance call | Claim boundary |
|---|---|---|---|---|
| Janesick et al. 2023 Xenium breast TME mapping | High-resolution Xenium can recover breast tumor, immune, stromal, and tissue-architecture signals in targeted panels. | Xenium breast rows were eligible for cell-level benchmark contracts, but no real-data setting was routed to `context_allowed` under strict residual, wrong-context, held-out, leakage, and downgrade gates. | Downgraded, not contradicted. | Spatial architecture can be biologically visible while still failing to show incremental predictive residual utility over expression-only and controls for the tested tasks. |
| Ren et al. 2025 subcellular spatial platform benchmarking | Platform, panel, segmentation, and sample/FOV effects can change what signal is observable and reproducible across high-throughput subcellular spatial transcriptomics assays. | Failure taxonomy and S25 decomposition expose panel observability, insufficient power, held-out replication, and unresolved downgrade failures; S26 shows zero `context_allowed` routes across tested operating points. | Concordant with caution. | The benchmark diagnoses observability and reproducibility limits; it does not infer that tumor communication is absent. |
| Fischer et al. 2022, NICHES 2022, and CellNeighborEX 2022 | Neighbor-dependent expression and ligand-receptor/pathway proxies can be biologically meaningful and should be tested with explicit spatial context. | Positive-control ladders are recovered, wrong-context controls are rejected, and real-data rows are routed to expression-only or abstain when residual context evidence is insufficient. | Concordant with conditional-use framing. | ContextGate-Bench supports testing neighbor context rather than assuming it; it is compatible with future context-positive discoveries that pass the same gates. |

## Manuscript Wording Supported By This Audit

Recommended safe wording:

- "Under the pre-specified ContextGate gates, no real-data setting was routed
  to `context_allowed`."
- "This is a benchmark-defined claim boundary, not proof that tumor
  neighborhoods lack biology."
- "ContextGate preserves zero registered false-context use while retaining
  positive-control sensitivity, distinguishing it from expression-only
  policies that never test context and always-context policies that fail
  null/wrong-context safety checks."

Avoid:

- "No real-data spatial biology exists."
- "ContextGate proves spatial context is useless."
- "ContextGate uniquely reduces false context use" without noting the
  expression-only comparator and positive-control sensitivity distinction.

## Artifact Pointers

- `results/reports/cp_q5_contextgate/contextgate_decisions.csv`
- `manuscript/tables/supp_table_s24_stratified_false_context.*`
- `manuscript/tables/supp_table_s25_gate_failure_decomposition.*`
- `manuscript/tables/supp_table_s25_gate_failure_summary.*`
- `manuscript/tables/supp_table_s26_threshold_operating_points.*`
- `manuscript/tables/supp_table_s26_threshold_axis_sensitivity.*`
- `manuscript/reviewer_hardening/paper_wizard_metric_consistency_audit.md`
- `manuscript/reviewer_hardening/contextgate_decision_contract.md`
- `manuscript/reviewer_hardening/leakage_downgrade_residualization_audit.md`

## Decision

CP-Q8.7G partially resolves Paper-Wizard D1 by making the manuscript honest
about route-label provenance. Real-data routing remains ContextGate-defined,
not independently adjudicated. The final manuscript should state this
explicitly and treat a future expert-curated route set as an extension rather
than as evidence already present in the current release.
