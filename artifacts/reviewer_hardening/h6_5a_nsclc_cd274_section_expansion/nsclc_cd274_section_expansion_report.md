# H6.5A NSCLC CD274 Section-Expansion Probe

- Decision: `expanded_sections_support_context_allowed`
- Attempted lung sections: `10`
- Evaluated lung sections: `10`
- Context-allowed count: `1`
- Full raw bundle downloaded: `False`

## Claim Limit

H6.5A strengthens the H5D additive result by testing additional lung sections under the same marker-derived contract (n=10). Claims must remain bounded to the selected NSCLC CD274 sections and must not be described as full GSE311609 validation.

## Route Decision

| marker_replay_route_id | expectation_id | dataset_id | task_id | expected_route | observed_route | route_match | replay_status | failure_reason | pre_registered_expectation_match | evidence_pointer | claim_implication | config_alpha |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| a59b4ab4deb8 | h1_pos_gse311609_nsclc_cd274_checkpoint | gse311609_xenium_lung_breast_validation | residual_pathway_module_prediction | context_allowed | context_allowed | True | claim_eligible_context_allowed |  | True | manuscript/reviewer_hardening/h5d_gse311609_marker_replay/gse311609_marker_replay_replication_summary.csv | A pre-registered marker-derived GSE311609 task exercised the ContextGate allow side under the bounded H5D contract. | 0.05 |

## Replication Summary

| expectation_id | dataset_id | task_id | expected_route | section_count | evaluated_section_count | effect_gate_section_count | median_residual_utility_delta | mean_residual_utility_delta | min_effect_q_value | bootstrap_ci_low | bootstrap_ci_high | replication_gate_passed | wrong_context_gate_passed | expression_baseline_gate_passed | spatial_gate_passed | route_ready | blocking_gates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| h1_pos_gse311609_nsclc_cd274_checkpoint | gse311609_xenium_lung_breast_validation | residual_pathway_module_prediction | context_allowed | 10 | 10 | 10 | 0.018195432125342248 | 0.015564176314541479 | 0.01953125 | 0.008247445348216116 | 0.021845731894313134 | True | True | True | True | True |  |

## Claim Audit

| claim_id | claim_status | safe_claim_text | unsafe_claim_text | evidence_pointer | does_not_modify_original_cp_q |
| --- | --- | --- | --- | --- | --- |
| h6_5a_nsclc_cd274_section_expansion | allowed_with_scope | H6.5A strengthens the H5D additive result by testing additional lung sections under the same marker-derived contract (n=10). Claims must remain bounded to the selected NSCLC CD274 sections and must not be described as full GSE311609 validation. | Full GSE311609 validates ContextGate, or all mature lung sections confirm the CD274 checkpoint route. | manuscript/reviewer_hardening/h6_5a_nsclc_cd274_section_expansion/nsclc_cd274_replication_summary.csv | True |
