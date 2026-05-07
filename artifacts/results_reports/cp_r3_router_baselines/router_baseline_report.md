# CP-R3 Router Baselines and Calibration

CP-R3 evaluates non-neural router baselines against the split-safe CP-R2
route labels. This is a baseline and claim-boundary artifact, not a
learned-router training run.

## Summary

- Router label rows: 23
- Baselines: 6
- Best non-oracle baseline: `spatial_statistics_heuristic`
- Best non-oracle oracle gap: 0.000
- Spatial heuristic oracle gap: 0.000
- Always-context false-positive context rate: 1.000
- Learned router target justified: False
- Recommendation: `block_cp_r4_until_unit_level_labels_or_new_signal`

## All-Label Metrics

- `oracle_upper_bound`: accuracy=1.000, utility=1.000, oracle_gap=0.000, mean_regret=0.000
- `spatial_statistics_heuristic`: accuracy=1.000, utility=1.000, oracle_gap=0.000, mean_regret=0.000
- `lr_pathway_heuristic`: accuracy=0.696, utility=0.870, oracle_gap=0.130, mean_regret=0.130
- `always_expression`: accuracy=0.478, utility=0.813, oracle_gap=0.187, mean_regret=0.187
- `random_router`: accuracy=0.174, utility=0.398, oracle_gap=0.602, mean_regret=0.602
- `always_full_context`: accuracy=0.043, utility=0.139, oracle_gap=0.861, mean_regret=0.861

## Calibration

- `oracle_upper_bound`: brier=0.000, ECE=0.000, AUROC=1.000, AUPRC=1.000
- `spatial_statistics_heuristic`: brier=0.106, ECE=0.272, AUROC=1.000, AUPRC=1.000
- `lr_pathway_heuristic`: brier=0.477, ECE=0.074, AUROC=0.614, AUPRC=0.056
- `always_expression`: brier=1.043, ECE=0.522, AUROC=0.500, AUPRC=0.043
- `random_router`: brier=0.810, ECE=0.226, AUROC=0.705, AUPRC=0.071
- `always_full_context`: brier=1.913, ECE=0.957, AUROC=0.500, AUPRC=0.043

## No-Harm Audit

- `always_expression`: expression rows=11, false-positive context rate=0.000, context overuse rate=0.000, positive-control context recall=0.000
- `always_full_context`: expression rows=11, false-positive context rate=1.000, context overuse rate=1.000, positive-control context recall=1.000
- `lr_pathway_heuristic`: expression rows=11, false-positive context rate=0.000, context overuse rate=0.000, positive-control context recall=0.000
- `oracle_upper_bound`: expression rows=11, false-positive context rate=0.000, context overuse rate=0.000, positive-control context recall=1.000
- `random_router`: expression rows=11, false-positive context rate=0.727, context overuse rate=0.591, positive-control context recall=1.000
- `spatial_statistics_heuristic`: expression rows=11, false-positive context rate=0.000, context overuse rate=0.000, positive-control context recall=1.000

## Claim Boundary

The current CP-R2 labels are run-level labels derived from CP-R1 evidence.
If a simple score heuristic has a tiny oracle gap, CP-R4 should not train
a learned router on these labels alone. The next valid learned-router
target would need finer unit/stratum labels, more train-eligible positive
context examples, or a new signal source that simple heuristics cannot
already reproduce.
