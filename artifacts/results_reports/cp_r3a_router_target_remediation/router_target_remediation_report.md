# CP-R3A Router Target Remediation and CP-R4 Gate

CP-R3A decides whether the next step may honestly train a learned
CellPack-Router, or whether the current evidence should be released as a
heuristic routing benchmark until finer labels exist.

## Decision

- CP-R4 decision: `downgrade_to_heuristic_router_release`
- CP-R4 reopened: False
- Learned router training allowed: False
- Heuristic router release allowed: True

## Gate Criteria

- FAIL `nontrivial_baseline_gap`: observed=0.0, required=0.05. A learned router is only justified if simple CP-R1 score thresholds leave meaningful oracle gap.
- FAIL `trainable_biological_context_positive`: observed=0.0, required=2.0. Positive-control rows can test mechanics but cannot support a biological learned-router claim.
- FAIL `trainable_context_positive_any`: observed=1.0, required=2.0. The training target needs enough context-positive examples to avoid a one-row synthetic route.
- FAIL `trainable_expression_negative`: observed=0.0, required=2.0. Expression-only negatives are held out biological outcomes in CP-R2, so they cannot train the learned route directly.
- PASS `trainable_abstention`: observed=5.0, required=2.0. Abstention examples are needed for calibrated uncertainty.
- FAIL `usable_fine_grained_artifact`: observed=0.0, required=1.0. Existing per-unit or per-stratum artifacts must be local and split-safe before they can remediate CP-R4 labels.
- PASS `independent_features_available`: observed=10.0, required=1.0. The router can use coverage/metadata features, but not the label-derived CP-R1 score or gate outcomes.

## Artifact Availability

- Candidate artifacts audited: 918
- Local candidates: 0
- Modal-only candidates: 918
- Fine-grained candidates: 530
- CP-R4 train-usable candidates: 0

- `modal_only_not_local`: 918

## Trainable Label Balance

- `expression_only`: 0 (0.000)
- `compressed_context`: 0 (0.000)
- `full_context`: 1 (0.167)
- `abstain_uncertain`: 5 (0.833)

## Feature Leakage Boundary

- Training-allowed independent features: 10
- Blocked label/outcome-derived features: 11

- `artifact_count`: training_allowed=True, risk=`low`
- `available_module_target_count`: training_allowed=True, risk=`low`
- `available_pair_count`: training_allowed=True, risk=`low`
- `cell_type_count`: training_allowed=True, risk=`low`
- `fov_id_count`: training_allowed=True, risk=`low`
- `gene_count`: training_allowed=True, risk=`low`
- `pathway_count`: training_allowed=True, risk=`low`
- `row_or_unit_count`: training_allowed=True, risk=`low`
- `sample_id_count`: training_allowed=True, risk=`low`
- `split_metadata_status`: training_allowed=True, risk=`low`
- `bio_gate_replay_passed`: training_allowed=False, risk=`blocked_high`
- `context_utility_score`: training_allowed=False, risk=`blocked_high`
- `evidence_class`: training_allowed=False, risk=`blocked_high`
- `label_family`: training_allowed=False, risk=`blocked_high`
- `label_usage`: training_allowed=False, risk=`blocked_high`
- `proof_gate_passed`: training_allowed=False, risk=`blocked_high`
- `raw_receptor_signal_gate_passed`: training_allowed=False, risk=`blocked_high`
- `residual_module_gate_passed`: training_allowed=False, risk=`blocked_high`
- `route_label`: training_allowed=False, risk=`blocked_high`
- `strict_conditioned_gate_passed`: training_allowed=False, risk=`blocked_high`
- `training_route_label`: training_allowed=False, risk=`blocked_high`

## Claim Boundary

The current run-level target should not be used for a learned CP-R4
router: the spatial-statistics score heuristic has zero oracle gap. Failed criteria: `nontrivial_baseline_gap`, `trainable_biological_context_positive`, `trainable_context_positive_any`, `trainable_expression_negative`, `usable_fine_grained_artifact`.
The defensible next path is a heuristic-router release or a future
data task that creates split-safe unit/stratum labels before training.
