# H5D GSE311609 Marker-Positive Replay

- Dataset: `gse311609_xenium_lung_breast_validation`
- Decision: `real_context_allowed_observed`
- Context-allowed count: `1`
- Full raw bundle downloaded: `False`

## Claim Limit

H5D supplies bounded real-data marker-derived context_allowed evidence. Manuscript claims must state the marker-derived label contract, bounded section set, and remaining need for broader replay.

## Route Decisions

| marker_replay_route_id | expectation_id | dataset_id | task_id | expected_route | observed_route | route_match | replay_status | failure_reason | pre_registered_expectation_match | evidence_pointer | claim_implication | config_alpha |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| a59b4ab4deb8 | h1_pos_gse311609_nsclc_cd274_checkpoint | gse311609_xenium_lung_breast_validation | residual_pathway_module_prediction | context_allowed | context_allowed | True | claim_eligible_context_allowed |  | True | manuscript/reviewer_hardening/h5d_gse311609_marker_replay/gse311609_marker_replay_replication_summary.csv | A pre-registered marker-derived GSE311609 task exercised the ContextGate allow side under the bounded H5D contract. | 0.05 |
| 526da7c1a7d6 | h1_pos_gse311609_breast_cxcl12_cxcr4_boundary | gse311609_xenium_lung_breast_validation | residual_receptor_prediction | context_allowed | abstain_uncertain | False | evaluated_not_context_allowed | wrong_context_not_separated;held_out_replication_not_passed;spatial_block_bootstrap_not_passed | True | manuscript/reviewer_hardening/h5d_gse311609_marker_replay/gse311609_marker_replay_replication_summary.csv | The bounded marker-derived GSE311609 replay did not exercise the allow side; keep the manuscript claim conservative for this task. | 0.05 |

## Replication Summary

| expectation_id | dataset_id | task_id | expected_route | section_count | evaluated_section_count | effect_gate_section_count | median_residual_utility_delta | mean_residual_utility_delta | min_effect_q_value | bootstrap_ci_low | bootstrap_ci_high | replication_gate_passed | wrong_context_gate_passed | expression_baseline_gate_passed | spatial_gate_passed | route_ready | blocking_gates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| h1_pos_gse311609_nsclc_cd274_checkpoint | gse311609_xenium_lung_breast_validation | residual_pathway_module_prediction | context_allowed | 3 | 3 | 3 | 0.027725605955001398 | 0.023811919221390476 | 0.0234375 | 0.0088147491124686 | 0.03250547038280142 | True | True | True | True | True |  |
| h1_pos_gse311609_breast_cxcl12_cxcr4_boundary | gse311609_xenium_lung_breast_validation | residual_receptor_prediction | context_allowed | 3 | 3 | 1 | 0.0003658203726587539 | 0.009240950122840652 | 0.0234375 | -0.0007258506678068377 | 0.028628716183902836 | False | False | True | False | False | wrong_context_not_separated;held_out_replication_not_passed;spatial_block_bootstrap_not_passed |
