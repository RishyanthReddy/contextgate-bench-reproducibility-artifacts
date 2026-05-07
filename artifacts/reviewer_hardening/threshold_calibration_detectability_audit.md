# CP-Q8.6E Threshold Calibration And Detectability Audit

> Reviewer-facing note for threshold choices, stress-test behavior, and
> positive-control detectability in ContextGate-Bench.
>
> Status: CP-Q8.6E.

---

## Purpose

This audit explains why the strict ContextGate thresholds are used and how the
existing CP-Q7 and CP-Q3 artifacts support them. It is not a formal prospective
power analysis for every possible ligand-receptor or spatial biology mechanism.
It is a benchmark calibration and detectability audit: it asks whether the
current benchmark detects injected context signal, rejects null/confounded
signal, and remains conservative when threshold values move.

Source artifacts:

- `results/reports/cp_q7_robustness_stress/threshold_sensitivity.csv`
- `results/reports/cp_q7_robustness_stress/positive_control_ablation.csv`
- `results/reports/cp_q3_positive_null_control_ladder/positive_control_ladder.csv`
- `results/reports/cp_q6_benchmark_matrix/benchmark_metric_matrix.csv`
- `results/reports/cp_q5_contextgate_decisions/contextgate_decisions.csv`

Generated supplement tables:

- `manuscript/tables/supp_table_s18_threshold_calibration_summary.*`
- `manuscript/tables/supp_table_s19_detectability_min_effect.*`
- `manuscript/tables/supp_table_s20_real_vs_detectability_audit.*`
- `manuscript/tables/supp_table_s26_threshold_operating_points.*`
- `manuscript/tables/supp_table_s26_threshold_axis_sensitivity.*`
- `manuscript/tables/supp_table_s33a_threshold_grid_detail.*`
- `manuscript/tables/supp_table_s33b_stress_family_accounting.*`
- `manuscript/tables/supp_table_s33c_claim_survival_reconciliation.*`

---

## Threshold Calibration Summary

The CP-Q7 stress table tests six threshold families:

| Gate family | Observed value | Tested thresholds | Result |
|---|---:|---|---|
| FDR/q-value | 0.343 | 0.01, 0.05, 0.10 | Fails all tested FDR thresholds. |
| Effect size | 0.157 | 0.02, 0.05, 0.10 | Passes effect-size screens alone. |
| False-context rate | 0.000 | 0.00, 0.05, 0.10 | Passes false-context safety. |
| No-harm rate | 1.000 | 0.80, 0.90, 0.95 | Passes no-harm safety. |
| Held-out replication | 0.599 | 0.50, 0.60, 0.70 | Passes lenient threshold, fails stricter thresholds. |
| Minimum row count | 188 | 3, 10, 30 | Passes benchmark row-count floor. |

The interpretation is intentionally conservative. The effect-size screen is not
the binding gate; FDR and replication are. This means the negative strict
real-data route is not caused by a single arbitrary effect-size cutoff. The
benchmark can see nonzero effects, but the current real-data effects do not
survive the full evidence contract required for `context_allowed`.

CP-Q8.8H expands this into a denominator reconciliation:

- seven row-generating stress families contribute the 127 CP-Q7 stress rows;
- those rows contain 122 passes, 5 explicit downgrades, and 0 failures without
  downgrade;
- the claim-survival audit is a separate six-claim table, with 5 surviving
  claims and 1 downgraded strong biological context-benefit claim;
- combined reviewer-facing accounting is therefore 133 row/claim entries,
  127 pass/survive outcomes, and 6 total downgrades.

There is no seventh downgrade in the registered CP-Q7 artifacts. The corrected
manuscript wording reports the registered 5 + 1 accounting and points to
Supplementary Tables S33B--S33C.

---

## Detectability Summary

The CP-Q3 positive/null ladder shows that ContextGate detects injected
true-neighbor signal down to an effective signal strength of 0.5501 in the
registered ladder. For ContextGate:

- positive rows: 36;
- recovered positive rows: 36;
- smallest recovered injected strength: 0.55;
- smallest recovered effective strength: 0.5501;
- mean positive sensitivity: 0.8633;
- null/confounded rows: 36;
- mean null/confounded specificity: 0.9433;
- maximum null/confounded false-context rate: 0.000;
- missing-panel abstention: 1.000;
- confounded-signal abstention: 1.000.

This answers the "model too weak or wiring broken" concern in bounded form. The
benchmark detects injected context signal and refuses missing-panel/confounded
controls. Therefore, the absence of strict real-data `context_allowed` decisions
should be interpreted as an evidence-routing result, not as failure to detect
any signal at all.

---

## Real-Data Versus Detectable Signal

The real-data full-benchmark ContextGate rows pass safety checks but not the
strict biological-evidence checks:

| Calibration item | Observed value | Reference threshold | Result |
|---|---:|---:|---|
| FDR/q-value gate | 0.343 | 0.05 | Fail |
| Effect-size screen | 0.157 | 0.05 | Pass alone |
| False-context safety | 0.000 | 0.05 | Pass |
| No-harm safety | 1.000 | 0.95 | Pass |
| Held-out replication | 0.599 | 0.60 | Borderline/fail under stricter gate |
| Residual delta direction | -0.063 | 0.00 | Fail |
| Injected positive-control detectability | 0.5501 | 0.5501 | Pass |
| Strict context-allowed route count | 0 | 1 | Fail |

The important conclusion is not "spatial biology is absent." The correct
conclusion is narrower: under the registered benchmark schema, real-data
neighbor context did not clear the combined FDR, residual, replication,
wrong-context, and route-count requirements, even though the same pipeline
detects injected neighbor signal and avoids false context use.

---

## Reviewer-Safe Claim Boundary

CP-Q8.6E supports three manuscript claims:

1. The strict thresholds are not arbitrary prose rules; they are backed by
   explicit CP-Q7 stress rows.
2. The benchmark has positive-control sensitivity and null/confounded-control
   specificity, so negative real-data gates are not a trivial implementation
   failure.
3. The current data support a conservative evidence-routing claim, not a
   universal claim that spatial context can never help and not a claim that
   biology lacks communication.

CP-Q8.6E does not support:

- a formal prospective power calculation for every dataset and pathway;
- a claim that all high-capacity future models would fail;
- a claim that targeted-panel data prove absence of biological communication;
- a claim that the effect-size screen alone justifies context use.
