# CP-R3B Unit/Stratum-Level Target Mining

CP-R3B mines fine-grained Modal-held residual artifacts to test whether
the learned-router target can be rescued below the run level.

## Decision

- CP-R4 decision: `keep_cp_r4_downgraded_to_heuristic`
- CP-R4 reopened: False
- Learned router training allowed: False

## Summary

- Sources requested: 4
- Sources loaded: 4
- Stratum comparisons: 25628
- Stratum labels: 6407
- Train full-context strata: 3
- Train expression-only strata: 2470
- Train abstention strata: 1789
- Replicated train-positive strata: 0

## Gate Criteria

- PASS `trainable_context_positive_strata`: observed=3, required=2. Train split needs multiple biological context-positive strata.
- PASS `trainable_expression_negative_strata`: observed=2470, required=2. Train split needs expression-only negatives mined before held-out use.
- PASS `trainable_abstention_strata`: observed=1789, required=2. Router target needs uncertain strata for abstention calibration.
- FAIL `replicated_context_positive_strata`: observed=0, required=1. At least one train-positive stratum should recur in validation/test.

## Trainable Label Balance

- `expression_only`: 2470 (0.580)
- `compressed_context`: 0 (0.000)
- `full_context`: 3 (0.001)
- `abstain_uncertain`: 1789 (0.420)

## Source Status

- `cosmx_nsclc_cp6f_s8000`: status=`loaded`, residual_rows=1080000, unit_rows=8000
- `gse277782_cp6g_s9000`: status=`loaded`, residual_rows=1134000, unit_rows=8400
- `gse310352_cp6j_s30000`: status=`loaded`, residual_rows=4050000, unit_rows=30000
- `cosmx_bcc_cp6l_s20000`: status=`loaded`, residual_rows=2700000, unit_rows=20000

## Claim Boundary

Only train-split labels can train a future router. Validation and test
labels are replication evidence only. If the decision stays downgraded,
the project should stop trying learned routing on the current target.
