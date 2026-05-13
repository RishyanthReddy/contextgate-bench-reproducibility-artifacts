# H6.5B Single Mature-Adapter Claim-Eligibility Probe

- Selected adapter: `liana_communication_adapter`
- Claim-eligible adapter rows: `0`
- Native output produced: `False`
- Mature adapter confirmed positive: `False`

## Claim Conclusion

H6.5B attempted the preferred LIANA+/COMMOT communication-adapter path for the H5D/H6.5A NSCLC CD274 task, but no native mature-adapter output was produced. H7 must not claim mature-adapter confirmation.

## Adapter Evidence

| phase | adapter_probe_id | adapter_id | adapter_family | primary_tool | backup_tool | dataset_id | expectation_id | task_id | parent_route | parent_context_allowed | parent_section_count | parent_median_residual_utility_delta | parent_bootstrap_ci_low | parent_bootstrap_ci_high | parent_replication_gate_passed | parent_wrong_context_gate_passed | primary_dependency_available | backup_dependency_available | scanpy_available | anndata_available | native_output_produced | contract_status | route_candidate | claim_eligible | include_in_claims | skip_reason | environment_fingerprint | evidence_pointer |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| H6.5B | h6_5b_liana_gse311609_nsclc_cd274 | liana_communication_adapter | communication_or_ligand_receptor | LIANA+ | COMMOT | gse311609_xenium_lung_breast_validation | h1_pos_gse311609_nsclc_cd274_checkpoint | residual_pathway_module_prediction | context_allowed | True | 10 | 0.018195432125342248 | 0.008247445348216116 | 0.021845731894313134 | True | True | False | False | True | True | False | blocked_missing_native_dependency | abstain_uncertain | False | False | LIANA+ and COMMOT are not installed in the execution runtime, so no native communication-score table was produced. | python=3.13.1;pandas=2.2.3;anndata=True;commot=False;liana=False;scanpy=True | manuscript/reviewer_hardening/h6_5a_nsclc_cd274_section_expansion/nsclc_cd274_replication_summary.csv |

## Feasibility

| adapter_id | primary_tool | backup_tool | selected_expectation_id | dependency_probe | contract_status | claim_eligible | primary_blocker | next_action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| liana_communication_adapter | LIANA+ | COMMOT | h1_pos_gse311609_nsclc_cd274_checkpoint | anndata=True;commot=False;liana=False;scanpy=True | blocked_missing_native_dependency | False | LIANA+ and COMMOT are not installed in the execution runtime, so no native communication-score table was produced. | Install/freeze the native adapter runner and define a transparent output-to-residual-utility mapping before using this adapter in manuscript claims. |

## Claim Audit

| claim_id | claim_status | safe_claim_text | unsafe_claim_text | evidence_pointer | skip_reason | does_not_modify_original_cp_q |
| --- | --- | --- | --- | --- | --- | --- |
| h6_5b_single_mature_adapter_probe | adapter_infeasible | H6.5B attempted the preferred LIANA+/COMMOT communication-adapter path for the H5D/H6.5A NSCLC CD274 task, but no native mature-adapter output was produced. H7 must not claim mature-adapter confirmation. | A mature SOTA communication adapter independently confirmed the NSCLC CD274 context_allowed route. | manuscript/reviewer_hardening/h6_5b_single_adapter_probe/single_adapter_evidence.csv | LIANA+ and COMMOT are not installed in the execution runtime, so no native communication-score table was produced. | True |
