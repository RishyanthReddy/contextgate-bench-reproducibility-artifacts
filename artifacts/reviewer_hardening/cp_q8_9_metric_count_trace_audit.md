# CP-Q8.9 Metric and Count Trace Audit

Date: 2026-05-07

Purpose: resolve the numeric-source questions raised by CP-Q8.9A before
manuscript prose, table, or figure edits.

## Trace Summary

| Review issue | Question | Source of truth | Trace result | Action required |
|---|---|---|---|---|
| C1 | Why does Section 4.2 report always-context false-context exposure 0.4783 and spatial-statistics 0.000 while Figure 2 shows 0.62 and 0.06? | `results/reports/cp_q2_method_comparison/method_metrics.csv`; `results/reports/cp_q6_benchmark_matrix/aggregate_metrics.csv`; `manuscript/tables/supp_table_s24_stratified_false_context.csv` | Values are from different tiers. CP-Q2 method-comparison rows give always-context all-row false-context flag mean 0.4782608695652174 and spatial-stats 0.0. CP-Q6 q1/full-tier aggregate rows give always-context 0.6226271970397781 and spatial-stats 0.06468085106382979. | Patch Section 4.2 and Figure 2 caption/header to label CP-Q2 versus CP-Q6 scopes explicitly. No rerun. |
| C2 | Should positive-control-only decisions be 36 or 37? | `results/reports/cp_q5_contextgate_decisions/contextgate_decision_summary.json`; `contextgate_route_summary.csv`; `contextgate_decisions.csv`; `manuscript/tables/supp_table_s30a_route_aggregation_trace.csv` | The global CP-Q5 route count is 37. S30A decomposes this as 36 from CP-Q3 positive/null ladder plus 1 from CP-R1 `run_context_utility`. The extra row is `cus_007`, dataset `xenium_breast_v1`, target `cp3lr_mu128_mg128_k5_steps12`, `uses_synthetic_context=True`, `uses_real_context=False`, reason `Only synthetic/injected context evidence is positive.` | Keep global count 37, but add main-text decomposition: CP-Q3 contributes 36 positive-control-only rows and CP-R1 contributes one synthetic-mechanics-only positive-control row. No rerun. |
| C4 | How can sensitivity score be 0.8633 while binary recovery is 36/36? | `results/reports/cp_q3_positive_null_control_ladder/method_summary.csv`; `positive_control_ladder.csv`; `scripts/build_contextgate_manuscript_tables.py::build_detectability_min_effect` | The 0.8633333333333335 value is the mean continuous `sensitivity` score across 36 expected-positive rows. The 36/36 value is binary route/gate recovery (`gate_passed=True`) across those rows. They are different quantities but Section 4.3 currently names them too similarly. | CP-Q8.9C must define continuous score and binary recovery separately and use Wilson interval only for binary recovery. No rerun. |
| C5 | Why does Section 4.2 report ContextGate regret 0.0261 while Figure 2/S17 show 0.34? | `results/reports/cp_q2_method_comparison/method_metrics.csv`; `manuscript/tables/supp_table_s17_q6_regret_distribution.csv`; `results/reports/cp_q6_benchmark_matrix/aggregate_metrics.csv` | CP-Q2 route-comparison subset: ContextGate mean regret 0.02608695652173913 over 23 rows. CP-Q6 full benchmark: ContextGate mean regret 0.3429540839015384 over 188 rows. | Patch Section 4.2 to cite both values and explain subset difference. No rerun. |
| C8 | Is spatial-statistics zero regret independently earned? | `results/reports/cp_q2_method_comparison/method_metrics.csv`; `data/manifests/contextgate_benchmark_manifest.yaml`; current manuscript Sections 3.4/4.2 | CP-Q2 method table reports spatial-statistics mean utility 1.0 and regret 0.0 over 23 rows. The manifest registers the method family, but the manuscript does not show threshold timestamp independence or independent oracle-label freezing. | CP-Q8.9B should frame zero regret as empirical in-sample oracle alignment/threshold-policy behavior unless a stronger registry pointer is added. No rerun. |
| E1 | Why do figures show different method subsets? | Figure captions and Table S29 | Current plan already maps this to caption/tier eligibility language. | CP-Q8.9H patch. No rerun. |

## Detailed Evidence Notes

### C1 False-Context Values

CP-Q2 `method_metrics.csv`:

- `always_true_neighbor_mean`: `false_positive_context_rate =
  0.4782608695652174`.
- `spatial_statistics_heuristic`: `false_positive_context_rate = 0.0`.
- `contextgate_transparent_router`: `false_positive_context_rate = 0.0`.

CP-Q6 `aggregate_metrics.csv`, q1/full benchmark rows:

- `always_true_neighbor_mean`: `false_positive_context_rate =
  0.6226271970397781`.
- `spatial_statistics_heuristic`: `false_positive_context_rate =
  0.06468085106382979`.
- `contextgate_transparent_router`: `false_positive_context_rate = 0.0`.

Interpretation: this is a labeling/context problem, not a numeric artifact
failure.

### C2 Positive-Control-Only Count

CP-Q5 summary:

- total decisions: 100;
- expression-only: 23;
- abstain: 40;
- positive-control-only: 37;
- context-allowed: 0.

S30A source decomposition:

- CP-Q3 positive/null-control ladder: 72 rows; 12 expression-only, 24 abstain,
  36 positive-control-only.
- CP-R1 context-utility route rows: 23 rows; 11 expression-only, 11 abstain,
  1 positive-control-only.
- rejected/access-blocked rows: 5 rows; 5 abstain.

The CP-R1 positive-control-only row is `cus_007`, derived from positive-control
context signal metadata, and is not a real biological `context_allowed` row.

Interpretation: the global count of 37 is artifact-registered, but the main
text must show the 36+1 decomposition because Section 4.3 discusses only CP-Q3.

### C4 Sensitivity Score Versus Binary Recovery

`method_summary.csv` for `contextgate_transparent_router`:

- positive rows: 36;
- negative rows: 36;
- mean positive sensitivity score: 0.8633333333333335;
- mean negative specificity score: 0.9433333333333331;
- false-positive context rate on negative rows: 0.0;
- gate pass rate: 1.0.

`positive_control_ladder.csv` for ContextGate groups into 36 expected-positive
rows and 36 expected-negative rows; all expected-positive rows have
`gate_passed=True`, and all expected-negative rows pass the non-context
response rule.

Interpretation: Section 4.3 must stop implying the continuous score is the same
quantity as the binary route-recovery proportion.

### C5 Regret Scope

CP-Q2 route-comparison method table:

- ContextGate mean regret: 0.02608695652173913 over 23 rows.

CP-Q6/S17 full benchmark:

- ContextGate full benchmark mean regret: 0.3429540839015384 over 188 rows.

Interpretation: both are valid, but Section 4.2 should not report only the
favorable CP-Q2 subset value without immediate full-tier context.

## Modal Decision

CP-Q8.9A is local artifact tracing only. No Modal rerun is required because all
major numeric questions reconciled to existing registered artifacts.
