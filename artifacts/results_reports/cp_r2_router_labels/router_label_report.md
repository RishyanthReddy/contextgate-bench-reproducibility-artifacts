# CP-R2 Router Labels and Split Hygiene

CP-R2 converts the CP-R1 context utility atlas into route labels while
blocking outcome-derived biological rows from training. The result is a
router target package, not a biological proof package.

## Summary

- Router label rows: 23
- Training-eligible rows: 6
- Evaluation-only rows: 13
- Held-out biological outcome rows: 13
- Training-eligible held-out outcome rows: 0
- Training leakage violations: 0
- Split hygiene passed: True

## Route Labels

- `abstain_uncertain`: 11
- `expression_only`: 11
- `full_context`: 1

## Training Route Labels

- `abstain_uncertain`: 5
- `full_context`: 1

## Class Balance Rows

- `all_route_label` / `abstain_uncertain`: 11 (0.478)
- `all_route_label` / `expression_only`: 11 (0.478)
- `all_route_label` / `full_context`: 1 (0.043)
- `deterministic_split` / `heldout_evaluation`: 13 (0.565)
- `deterministic_split` / `train_metadata`: 2 (0.087)
- `deterministic_split` / `train_synthetic`: 1 (0.043)
- `deterministic_split` / `validation_caution`: 4 (0.174)
- `deterministic_split` / `validation_metadata`: 3 (0.130)
- `heldout_evaluation_route_label` / `abstain_uncertain`: 2 (0.154)
- `heldout_evaluation_route_label` / `expression_only`: 11 (0.846)
- `label_family` / `biological_context_negative`: 11 (0.478)
- `label_family` / `exploratory_localized`: 2 (0.087)
- `label_family` / `synthetic_positive_control`: 1 (0.043)
- `label_family` / `uncertain_or_metadata`: 9 (0.391)
- `label_usage` / `evaluation_only`: 13 (0.565)
- `label_usage` / `train_allowed`: 6 (0.261)
- `label_usage` / `validation_only`: 4 (0.174)
- `training_route_label` / `abstain_uncertain`: 5 (0.833)
- `training_route_label` / `full_context`: 1 (0.167)

## Claim Boundary

Negative biological rows remain available for held-out evaluation and
baseline comparison, but they are not training labels. Positive-control
rows can train route mechanics only and cannot be cited as biological
context utility. `compressed_context` remains an allowed route label but
is intentionally unassigned until CP-R5 supplies compression-specific
evidence.
