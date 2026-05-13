# Pre-H7 Hardening Results Verification Packet

Created: 2026-05-13

Purpose: collect the new results and discoveries from the submission-evidence
hardening workflow before H7 manuscript drafting. This file is meant for human
verification of the metrics, route counts, claim limits, Modal runs, and artifact
locations before any manuscript text is rewritten.

## Bottom Line

The hardening phase changed the evidentiary story in a controlled way:

1. The original CP-Q benchmark result is preserved:
   - Original CP-Q5 route decisions: 100.
   - Original CP-Q5 `context_allowed` decisions: 0.
   - Original CP-Q5 route counts:
     - `expression_only`: 23.
     - `abstain_uncertain`: 40.
     - `positive_control_only`: 37.
   - H5E decision: no full scratch rerun is required.

2. A new additive real-data hardening result exists:
   - H5D evaluated 2 bounded GSE311609 marker-derived tasks.
   - H5D produced 1 real-data `context_allowed` route.
   - Plain-language check: H5D produced 1 real-data context_allowed route.
   - The positive route is:
     `h1_pos_gse311609_nsclc_cd274_checkpoint`.
   - The second route, breast CXCL12/CXCR4 boundary, remained
     `abstain_uncertain`.

3. A new additive expanded synthetic ladder exists:
   - H6 added 11 expanded rungs across 8 signal families.
   - H6 produced 132 synthetic cases and 1,320 method rows.
   - ContextGate positive synthetic recovery rate: 1.0.
   - ContextGate negative/confounded false-context rate: 0.0.
   - H6 does not modify the original CP-Q3 denominator.

4. The main claim boundary for H7 is:
   - Original CP-Q matrix: zero real-data `context_allowed`.
   - Additive H5D bounded marker replay: one real-data marker-derived
     `context_allowed`.
   - Additive H6.5A bounded section expansion: the same NSCLC CD274 route
     remains `context_allowed` across 10 selected lung sections.
   - Additive H6 ladder: expanded synthetic machinery evidence only.
   - Additive H6.5B adapter probe: one LIANA+/COMMOT claim-eligibility attempt
     was blocked by missing native adapter dependencies; H7 must not claim
     mature-adapter confirmation.

## Files To Review First

| Item | File |
|---|---|
| H5D real-data marker replay summary | `manuscript/reviewer_hardening/h5d_gse311609_marker_replay/gse311609_marker_replay_summary.json` |
| H5D route decisions | `manuscript/reviewer_hardening/h5d_gse311609_marker_replay/gse311609_marker_replay_route_decisions.csv` |
| H5D residual utilities | `manuscript/reviewer_hardening/h5d_gse311609_marker_replay/gse311609_marker_replay_residual_utility.csv` |
| H5D replication summary | `manuscript/reviewer_hardening/h5d_gse311609_marker_replay/gse311609_marker_replay_replication_summary.csv` |
| H5E rerun decision | `manuscript/reviewer_hardening/h5e_result_reconciliation_audit/contextgate_h5e_reconciliation_summary.json` |
| H5E claim update map | `manuscript/reviewer_hardening/h5e_result_reconciliation_audit/contextgate_h5e_claim_update_map.csv` |
| H6 expanded ladder summary | `manuscript/reviewer_hardening/h6_expanded_synthetic_ladder/expanded_ladder_summary.json` |
| H6 scale sensitivity | `manuscript/reviewer_hardening/h6_expanded_synthetic_ladder/expanded_ladder_scale_sensitivity.csv` |
| H6 claim audit | `manuscript/reviewer_hardening/h6_expanded_synthetic_ladder/expanded_ladder_claim_audit.csv` |
| H6.5A NSCLC expansion summary | `manuscript/reviewer_hardening/h6_5a_nsclc_cd274_section_expansion/nsclc_cd274_section_expansion_summary.json` |
| H6.5A section residual utility | `manuscript/reviewer_hardening/h6_5a_nsclc_cd274_section_expansion/nsclc_cd274_section_residual_utility.csv` |
| H6.5A claim audit | `manuscript/reviewer_hardening/h6_5a_nsclc_cd274_section_expansion/nsclc_cd274_claim_audit.csv` |
| H6.5B adapter probe summary | `manuscript/reviewer_hardening/h6_5b_single_adapter_probe/single_adapter_probe_summary.json` |
| H6.5B adapter evidence | `manuscript/reviewer_hardening/h6_5b_single_adapter_probe/single_adapter_evidence.csv` |
| Master hardening ledger | `manuscript/reviewer_hardening/submission_evidence_hardening_ledger.md` |

## Workflow Status

| Phase | Linear | Status | Main Outcome |
|---|---:|---|---|
| H0 | RIS-53 | Done | Current V1 package frozen as fallback snapshot. |
| H1 | RIS-54 | Done | 17 pre-registered route expectations frozen. |
| H2 | RIS-55 | Done | GSE311609 preflight allowed bounded Modal probing only, not full replay. |
| H3 | RIS-56 | Done | Spatial inference layer added and tested. |
| H4 | RIS-57 | Done | Initial validation replay produced 0 real-data `context_allowed`. |
| H5 | RIS-58 | Done | Mature adapter contracts added; no claim-eligible native SOTA rows. |
| H5A | RIS-62 | Done | Real-positive feasibility found no immediate replay-ready candidates. |
| H5B | RIS-63 | Done | GSE311609 loader cleared but labels/panel remained blocking. |
| H5C | RIS-64 | Done | Marker-label reconstruction cleared 2 bounded GSE311609 tasks. |
| H5D | RIS-65 | Done | One bounded real-data marker-derived `context_allowed` route observed. |
| H5E | RIS-66 | Done | No full scratch CP-Q rerun required. |
| H6 | RIS-59 | Done | Expanded synthetic ladder passed and stayed additive. |
| Pre-H7 verification | RIS-67 | Done | This metrics packet was created for human review before drafting. |
| H6.5A | RIS-68 | Done | NSCLC CD274 expansion to 10 lung sections preserved `context_allowed`. |
| H6.5B | RIS-69 | Done | Single LIANA+/COMMOT adapter probe was infeasible; no adapter-confirmed claim. |
| H6.5C | RIS-70 | Done | Hardened pre-H7 evidence snapshot created; science expansion stops here. |
| H7 | RIS-60 | Next | Rebuild manuscript artifacts and claim audit. |

## H0: Freeze Current V1

Result:

- Git tag: `v1-current-complete`.
- Tag commit: `4eeb6e23637ad0dc083904a4d3bb9e0dbda8b969`.
- Public artifact commit frozen at:
  `1c9ae9a51106f3163d9127d61ee55d1c35ac3a36`.
- Snapshot archive:
  `manuscript/snapshots/v1-current-complete-2026-05-13.zip`.
- Snapshot SHA256:
  `23900B3201837C74A40FA9A9C338F7D53FFFD136000105CE808B0A6654C8F9D0`.

Interpretation:

- We can fall back to the conservative V1 manuscript package if the hardening
  changes become too complex.

## H1: Pre-Registered Route Expectations

Artifact:

- `data/manifests/contextgate_route_expectations.yaml`.

Metrics:

- Total expectations: 17.
- Registry hash:
  `sha256:d67f17408c744b89cc2326a80e91e79fd1612fbb369b1bff502c9df0f901943d`.

Expectation families:

| Family | Count |
|---|---:|
| `expected_context_positive` | 4 |
| `expected_expression_only` | 3 |
| `expected_abstain_or_panel_blocked` | 3 |
| `strict_null_or_confounded_control` | 3 |
| `wrong_context_control` | 3 |
| `synthetic_positive_control` | 1 |

Expected routes:

| Expected route | Count |
|---|---:|
| `expression_only` | 7 |
| `abstain_uncertain` | 5 |
| `context_allowed` | 4 |
| `positive_control_only` | 1 |

Interpretation:

- The later H5D positive result is not post-hoc in the broad workflow sense:
  the positive GSE311609 task came from the pre-registered expectation set.
- H7 should cite the exact expectation ID when discussing the positive route.

## H2: GSE311609 Validation-Scale Preflight

Artifact:

- `manuscript/reviewer_hardening/h2_validation_preflight/gse311609_preflight_summary.json`.

Key metrics:

| Metric | Value |
|---|---:|
| Dataset | `gse311609_xenium_lung_breast_validation` |
| Reported sample count | 41 |
| Reported section count | 41 |
| Reported donor count | 27 |
| Raw bundle | `GSE311609_RAW.tar` |
| Raw bundle size | 159.9 GB |
| H1 GSE311609 expectations | 4 |
| H1 context-positive GSE311609 expectations | 3 |
| Full replay allowed | false |
| Bounded Modal preflight allowed | true |
| Decision | `go_bounded_modal_preflight_only` |

Modal:

- URL: `https://modal.com/apps/rishyanthreddy101/main/ap-A0yxPUvQvy5RdMPI6FgHBk`.
- Full raw bundle downloaded: false.

Interpretation:

- H2 did not clear a full 41-section replay.
- H2 justified bounded Modal probing only.
- H7 wording must distinguish the full validation-scale cohort from the bounded
  H5D marker replay.

## H3: Spatially Aware Inference Layer

Artifact:

- `manuscript/reviewer_hardening/h3_spatial_inference/contextgate_spatial_inference_summary.json`.

Key metrics:

| Metric | Value |
|---|---:|
| Rows | 3 |
| Spatial pass count | 1 |
| Spatial fail count | 1 |
| Downgrade count | 1 |
| Skip count | 0 |
| Schema passed | true |

Modal:

- URL: `https://modal.com/apps/rishyanthreddy101/main/ap-ct68PotjaINgODlRbP6Cv3`.
- Data mode: synthetic smoke only.
- Full raw bundle downloaded: false.

Interpretation:

- H3 adds the route-contract behavior needed for spatially aware downgrades.
- It does not by itself prove or disprove any real biological task.

## H4: Initial Validation Replay

Artifact:

- `manuscript/reviewer_hardening/h4_validation_replay/contextgate_validation_replay_summary.json`.

Key metrics:

| Metric | Value |
|---|---:|
| Expectations | 17 |
| Jobs | 17 |
| Real-data `context_allowed` count | 0 |
| Wrong-context controls | 12 |
| Wrong-context controls can create context | false |
| GSE311609 blocked before full replay | 4 |
| Deferred to H6 | 2 |
| Schema passed | true |

Route counts:

| Route | Count |
|---|---:|
| `abstain_uncertain` | 10 |
| `expression_only` | 3 |
| `rejected_or_access_blocked` | 4 |

Status counts:

| Status | Count |
|---|---:|
| `blocked_before_full_replay` | 4 |
| `blocked_by_panel_or_preflight` | 2 |
| `completed_from_registered_artifacts` | 4 |
| `completed_from_registered_dataset_proxy` | 3 |
| `deferred_to_h6_expanded_ladder` | 2 |
| `no_direct_task_replay_available` | 1 |
| `no_registered_evidence` | 1 |

Modal:

- Smoke URL: `https://modal.com/apps/rishyanthreddy101/main/ap-oCQLNm84Y6LrWkEDlwxKCw`.
- Core URL: `https://modal.com/apps/rishyanthreddy101/main/ap-RXugkS4Np6DT6ODYJYTGP2`.
- Full raw bundle downloaded: false.

Interpretation:

- H4 was still conservative: no real-data allowed route.
- H4 is now superseded in one narrow way by H5D, not by a full matrix rerun.

## H5: Mature Adapter Replay Contracts

Artifact:

- `manuscript/reviewer_hardening/h5_mature_adapter_replay/contextgate_sota_adapter_replay_summary.json`.

Key metrics:

| Metric | Value |
|---|---:|
| Adapter families represented | 3 |
| Adapter evidence rows | 3 |
| Adapter method-prediction rows | 3 |
| Passing adapter smoke rows | 3 |
| Valid native SOTA evidence rows | 0 |
| Claim-eligible adapter rows | 0 |
| Explicit infeasibility rows | 3 |
| Raw data downloaded | false |
| Schema passed | true |

Route-candidate counts:

| Route | Count |
|---|---:|
| `abstain_uncertain` | 2 |
| `rejected_or_access_blocked` | 1 |

Modal:

- BANKSY smoke:
  `https://modal.com/apps/rishyanthreddy101/main/ap-GFtlJlCC2pcCUy17eEXtYO`.
- LIANA smoke:
  `https://modal.com/apps/rishyanthreddy101/main/ap-FDcdT81XZPFMMO6QCHs6mq`.
- Neighbor-expression smoke:
  `https://modal.com/apps/rishyanthreddy101/main/ap-ufJ8xy5emVUOVQqau3T2db`.
- Combined core:
  `https://modal.com/apps/rishyanthreddy101/main/ap-2uz4BKZhuHZFeTUFtyIJ5a`.

Interpretation:

- H5 answers the comparator criticism structurally: mature adapters now have
  contracts.
- H5 does not claim mature SOTA tools independently found real context utility.
- H7 should say adapter coverage was added, but no native SOTA evidence row is
  claim eligible yet.

## H5A: Real-Data Positive Feasibility Sprint

Artifact:

- `manuscript/reviewer_hardening/h5a_real_positive_feasibility/contextgate_real_positive_feasibility_summary.json`.

Key metrics:

| Metric | Value |
|---|---:|
| Candidate count | 30 |
| Dataset count | 7 |
| Immediate replay-ready candidates | 0 |
| Current-decision real `context_allowed` count | 0 |
| Blocked GSE311609 candidates | 4 |
| Near-miss candidates | 3 |
| Raw data downloaded | false |
| Decision | `go_clear_gse311609_first` |

Interpretation:

- This phase stopped us from pretending a real-data positive route was already
  available.
- The best path was GSE311609 clearance, which led to H5B-H5D.

## H5B: GSE311609 Clearance Sprint

Artifact:

- `manuscript/reviewer_hardening/h5b_gse311609_clearance/gse311609_clearance_summary.json`.

Key metrics:

| Metric | Value |
|---|---:|
| Archive file count | 246 |
| Sample count | 41 |
| Complete sample bundles | 41 |
| Matrix H5 files | 41 |
| Cell metadata files | 41 |
| Lung samples | 22 |
| Breast samples | 19 |
| Inferred unique patients/donors | 27 |
| Bounded probe sample count | 2 |
| Bounded probe downloaded bytes | 24,912,896 |
| Full raw bundle downloaded | false |
| Loader required passed | true |
| Metadata required passed | false |
| Panel required passed | false |
| Clearance decision | `blocked_keep_gse311609_as_future_work` |

Blocked reasons:

- `cell_state_or_region_labels_missing`.
- `panel_h1_pos_gse311609_nsclc_tgfb_stroma`.

Modal:

- URL: `https://modal.com/apps/rishyanthreddy101/main/ap-lFXXSE3WEK8TQ7HBxZOEDx`.

Interpretation:

- GSE311609 was not cleanly cleared for full positive replay.
- The loader/file structure was usable, but labels and one panel path blocked
  full claim eligibility.
- This forced the marker-label reconstruction path in H5C.

## H5C: GSE311609 Marker-Label Reconstruction Feasibility

Artifact:

- `manuscript/reviewer_hardening/h5c_gse311609_marker_feasibility/gse311609_marker_feasibility_summary.json`.

Key metrics:

| Metric | Value |
|---|---:|
| Marker rules frozen | 9 |
| Passing marker rules | 8 |
| Failed marker rules | 1 |
| Marker probe sample count | 2 |
| Bounded probe downloaded bytes | 22,211,584 |
| Full raw bundle downloaded | false |
| Eligible context-positive expectations | 2 |
| Blocked context-positive expectations | 1 |
| Decision | `go_bounded_marker_positive_replay` |

Eligible H5D tasks:

- `h1_pos_gse311609_nsclc_cd274_checkpoint`.
- `h1_pos_gse311609_breast_cxcl12_cxcr4_boundary`.

Blocked task:

- `h1_pos_gse311609_nsclc_tgfb_stroma`.

Modal:

- URL: `https://modal.com/apps/rishyanthreddy101/main/ap-SM6xFjBmpygBgLnu3Jowin`.

Interpretation:

- H5C does not itself prove a real-data positive route.
- It gives H5D two pre-specified, bounded, marker-derived tasks to replay.

## H5D: Bounded GSE311609 Marker-Positive Replay

Artifacts:

- `manuscript/reviewer_hardening/h5d_gse311609_marker_replay/gse311609_marker_replay_summary.json`.
- `manuscript/reviewer_hardening/h5d_gse311609_marker_replay/gse311609_marker_replay_route_decisions.csv`.
- `manuscript/reviewer_hardening/h5d_gse311609_marker_replay/gse311609_marker_replay_residual_utility.csv`.
- `manuscript/reviewer_hardening/h5d_gse311609_marker_replay/gse311609_marker_replay_replication_summary.csv`.
- `manuscript/reviewer_hardening/h5d_gse311609_marker_replay/gse311609_marker_replay_wrong_context_controls.csv`.

Summary metrics:

| Metric | Value |
|---|---:|
| Tier | `core` |
| Tasks evaluated | 2 |
| Sections evaluated | 6 |
| Effect-gate sections | 4 |
| Bounded replay downloaded bytes | 102,267,392 |
| Full raw bundle downloaded | false |
| Route count: `context_allowed` | 1 |
| Route count: `abstain_uncertain` | 1 |
| Decision | `real_context_allowed_observed` |

Modal:

- Smoke URL:
  `https://modal.com/apps/rishyanthreddy101/main/ap-5TMEIfno9gfKSb2vPA2zQh`.
- Core URL:
  `https://modal.com/apps/rishyanthreddy101/main/ap-KfjWifPvF4SKfDiyKHC8Ju`.

### H5D Route Decisions

| Expectation ID | Task | Expected | Observed | Status | Failure reason |
|---|---|---|---|---|---|
| `h1_pos_gse311609_nsclc_cd274_checkpoint` | residual pathway/module prediction | `context_allowed` | `context_allowed` | `claim_eligible_context_allowed` | none |
| `h1_pos_gse311609_breast_cxcl12_cxcr4_boundary` | residual receptor prediction | `context_allowed` | `abstain_uncertain` | `evaluated_not_context_allowed` | `held_out_replication_not_passed` |

### H5D Positive Route: NSCLC CD274 Checkpoint

Expectation:

- `h1_pos_gse311609_nsclc_cd274_checkpoint`.
- Dataset: `gse311609_xenium_lung_breast_validation`.
- Target genes used for residuals: `CD274;CXCL9;CXCL10`.
- Final observed route: `context_allowed`.

Section-level evidence:

| Section | Sample | Receiver cells sampled | Context cell fraction | Expression-only R2 | True-context R2 | Wrong-context R2 | Delta vs expression | Delta vs wrong | q value |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| L1 | GSM9509134 | 5,000 | 0.055355 | 0.002633 | 0.031268 | 0.003542 | 0.028635 | 0.027726 | 0.023438 |
| L3 | GSM9509135 | 5,000 | 0.150697 | 0.110229 | 0.119159 | 0.110344 | 0.008930 | 0.008815 | 0.023438 |
| L5 | GSM9509136 | 5,000 | 0.161079 | 0.026327 | 0.061335 | 0.026439 | 0.035008 | 0.034895 | 0.023438 |

Replication summary:

| Metric | Value |
|---|---:|
| Sections | 3 |
| Evaluated sections | 3 |
| Effect-gate sections | 3 |
| Median residual utility delta | 0.027726 |
| Mean residual utility delta | 0.023812 |
| Minimum q value | 0.023438 |
| Bootstrap CI low | 0.008815 |
| Bootstrap CI high | 0.032505 |
| Replication gate passed | true |
| Wrong-context gate passed | true |
| Expression-baseline gate passed | true |
| Spatial gate passed | true |
| Route ready | true |

Wrong-context controls:

- Each NSCLC section had two wrong-context controls:
  `label_shuffled_context` and `coordinate_shuffled_context`.
- True context beat wrong context in all 6 NSCLC wrong-control comparisons.

Interpretation:

- This is the key new positive real-data result.
- It exercises ContextGate's allow side under a bounded, marker-derived,
  pre-registered GSE311609 contract.

### H5D Abstained Route: Breast CXCL12/CXCR4 Boundary

Expectation:

- `h1_pos_gse311609_breast_cxcl12_cxcr4_boundary`.
- Dataset: `gse311609_xenium_lung_breast_validation`.
- Target gene used for residuals: `CXCR4`.
- Final observed route: `abstain_uncertain`.
- Blocking gate: `held_out_replication_not_passed`.

Section-level evidence:

| Section | Sample | Receiver cells sampled | Context cell fraction | Expression-only R2 | True-context R2 | Wrong-context R2 | Delta vs expression | Delta vs wrong | q value | Effect gate |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| B17 | GSM9509156 | 5,000 | 0.701437 | 0.093788 | 0.094303 | 0.094052 | 0.000516 | 0.000251 | 0.171875 | false |
| B16 | GSM9509157 | 4,900 | 0.727448 | 0.054274 | 0.083288 | 0.054680 | 0.029014 | 0.028608 | 0.023438 | true |
| B15 | GSM9509158 | 5,000 | 0.684408 | 0.024263 | 0.025261 | 0.024685 | 0.000998 | 0.000576 | 0.093750 | false |

Replication summary:

| Metric | Value |
|---|---:|
| Sections | 3 |
| Evaluated sections | 3 |
| Effect-gate sections | 1 |
| Median residual utility delta | 0.000576 |
| Mean residual utility delta | 0.009812 |
| Minimum q value | 0.023438 |
| Bootstrap CI low | 0.000251 |
| Bootstrap CI high | 0.028608 |
| Replication gate passed | false |
| Wrong-context gate passed | true |
| Expression-baseline gate passed | true |
| Spatial gate passed | true |
| Route ready | false |

Interpretation:

- The breast task had one positive section but failed held-out replication.
- The correct route is abstention, not a weak positive.

### H5D Claim Limit

Allowed wording:

- "A bounded, marker-derived GSE311609 replay produced one pre-registered
  real-data `context_allowed` route for an NSCLC checkpoint task."

Not allowed:

- "The full GSE311609 cohort validates ContextGate."
- "All real-data tasks now show context utility."
- "Marker-derived labels are equivalent to expert annotations."
- "The original CP-Q5 denominator should be changed from 100 to 102."

## H5E: Result Reconciliation and Rerun Decision Audit

Artifact:

- `manuscript/reviewer_hardening/h5e_result_reconciliation_audit/contextgate_h5e_reconciliation_summary.json`.

Key metrics:

| Metric | Value |
|---|---:|
| Rerun decision | `targeted_reconciliation_no_full_scratch_rerun` |
| Full scratch rerun required | false |
| Old CP-Q gate or matrix code changed | false |
| Original CP-Q5 decision rows | 100 |
| Original CP-Q5 `context_allowed` | 0 |
| H5D task count | 2 |
| H5D `context_allowed` count | 1 |
| High-priority claim updates required | 6 |

Original CP-Q5 route counts:

| Route | Count |
|---|---:|
| `expression_only` | 23 |
| `abstain_uncertain` | 40 |
| `positive_control_only` | 37 |

H5D additive route counts:

| Route | Count |
|---|---:|
| `context_allowed` | 1 |
| `abstain_uncertain` | 1 |

H7 implications:

- Do not rewrite all Results from scratch.
- Preserve original CP-Q result sections.
- Add a bounded H5D marker-replay subsection.
- Revise absolute zero-real-data wording.
- Do not regenerate old CP-Q figures just because H5D exists.
- Add or patch H5D-specific table/figure material.

## H6: Expanded Synthetic Ladder

Artifacts:

- `manuscript/reviewer_hardening/h6_expanded_synthetic_ladder/expanded_ladder_summary.json`.
- `manuscript/reviewer_hardening/h6_expanded_synthetic_ladder/expanded_ladder_scale_sensitivity.csv`.
- `manuscript/reviewer_hardening/h6_expanded_synthetic_ladder/expanded_ladder_recovery.csv`.
- `manuscript/reviewer_hardening/h6_expanded_synthetic_ladder/expanded_ladder_failure_modes.csv`.
- `manuscript/reviewer_hardening/h6_expanded_synthetic_ladder/expanded_ladder_claim_audit.csv`.

Summary metrics:

| Metric | Value |
|---|---:|
| Signal families | 8 |
| Rungs | 11 |
| Dataset backbones | 2 |
| Splits | 2 |
| Seeds | 3 |
| Methods | 10 |
| Synthetic cases | 132 |
| Method rows | 1,320 |
| Required signal families present | true |
| ContextGate positive recovery rate | 1.0 |
| ContextGate negative false-context rate | 0.0 |
| ContextGate confounded trap passed | true |
| Schema passed | true |
| Ladder gate passed | true |
| Original CP-Q3 modified | false |

Modal:

- URL: `https://modal.com/apps/rishyanthreddy101/main/ap-KRe149qcI30qiKTp4h9WFv`.
- Data mode: synthetic only.
- Full raw bundle downloaded: false.

H6 rung-level ContextGate scale sensitivity:

| Signal family | Rung | Graph | k | Radius um | Route | Recovery | Sensitivity | Specificity | False-context |
|---|---|---|---:|---:|---|---:|---:|---:|---:|
| `confounded_trap` | `fov_confounded_positive_trap` | confounded | 5 | NA | `abstain_uncertain` | 1.0 | 0.000000 | 0.93 | 0.0 |
| `distance_decay` | `distance_decay_short_range_signal` | distance_decay | 8 | 160 | `positive_control_only` | 1.0 | 0.920799 | 0.00 | 0.0 |
| `k_sensitivity` | `k10_linear_diluted_signal` | knn | 10 | NA | `positive_control_only` | 1.0 | 0.890318 | 0.00 | 0.0 |
| `k_sensitivity` | `k3_linear_contact_signal` | knn | 3 | NA | `positive_control_only` | 1.0 | 0.878676 | 0.00 | 0.0 |
| `k_sensitivity` | `k5_linear_reference_signal` | knn | 5 | NA | `positive_control_only` | 1.0 | 0.915378 | 0.00 | 0.0 |
| `null_control` | `null_no_context_scale_control` | none | NA | NA | `expression_only` | 1.0 | 0.000000 | 0.98 | 0.0 |
| `radius_sensitivity` | `radius120_paracrine_signal` | radius | NA | 120 | `positive_control_only` | 1.0 | 0.899806 | 0.00 | 0.0 |
| `radius_sensitivity` | `radius40_contact_signal` | radius | NA | 40 | `positive_control_only` | 1.0 | 0.872253 | 0.00 | 0.0 |
| `rare_niche` | `rare_niche_local_strong_signal` | knn | 5 | NA | `positive_control_only` | 1.0 | 0.869618 | 0.00 | 0.0 |
| `receiver_state_conditioned` | `receiver_state_specific_signal` | knn | 5 | NA | `positive_control_only` | 1.0 | 0.906060 | 0.00 | 0.0 |
| `threshold_gated` | `threshold_gated_sender_signal` | knn | 5 | NA | `positive_control_only` | 1.0 | 0.885441 | 0.00 | 0.0 |

Interpretation:

- H6 answers the synthetic-ladder criticism: sensitivity is no longer limited
  to a linear k=5 mean-neighbor construction.
- H6 remains synthetic machinery evidence only.
- H6 does not prove real biological communication.

## H6.5A: Bounded NSCLC CD274 Section Expansion

Artifacts:

- `manuscript/reviewer_hardening/h6_5a_nsclc_cd274_section_expansion/nsclc_cd274_section_expansion_summary.json`.
- `manuscript/reviewer_hardening/h6_5a_nsclc_cd274_section_expansion/nsclc_cd274_attempted_sections.csv`.
- `manuscript/reviewer_hardening/h6_5a_nsclc_cd274_section_expansion/nsclc_cd274_section_residual_utility.csv`.
- `manuscript/reviewer_hardening/h6_5a_nsclc_cd274_section_expansion/nsclc_cd274_wrong_context_controls.csv`.
- `manuscript/reviewer_hardening/h6_5a_nsclc_cd274_section_expansion/nsclc_cd274_replication_summary.csv`.
- `manuscript/reviewer_hardening/h6_5a_nsclc_cd274_section_expansion/nsclc_cd274_route_decisions.csv`.
- `manuscript/reviewer_hardening/h6_5a_nsclc_cd274_section_expansion/nsclc_cd274_claim_audit.csv`.

Summary metrics:

| Metric | Value |
|---|---:|
| Selected lung sections | 10 |
| Attempted lung sections | 10 |
| Original H5D core lung sections | 3 |
| Additional attempted lung sections | 7 |
| Evaluated lung sections | 10 |
| Additional evaluated lung sections | 7 |
| Effect-gate section count | 10 |
| Context-allowed count | 1 |
| Median residual utility delta | 0.018195432125342248 |
| Bootstrap CI low | 0.008247445348216116 |
| Bootstrap CI high | 0.021845731894313134 |
| Replication gate passed | true |
| Wrong-context gate passed | true |
| Spatial gate passed | true |
| Bounded bytes downloaded | 172,341,248 |
| Full raw bundle downloaded | false |
| Original CP-Q modified | false |

Decision:

- `expanded_sections_support_context_allowed`.

Safe H7 claim:

- H6.5A strengthens the H5D additive result by showing that the same
  marker-derived NSCLC CD274 checkpoint route remains `context_allowed` across
  10 selected GSE311609 lung sections.

Unsafe H7 claim:

- Do not say full GSE311609 validation is complete.
- Do not say all 41 sections were replayed.
- Do not merge the H6.5A sections into the original CP-Q route count.

Modal:

- Smoke URL:
  `https://modal.com/apps/rishyanthreddy101/main/ap-OPQqO5JJvFyJdwxt9Z9cKp`.
- Smoke used 6 sections, 31 permutations, and 3,000 max receiver cells.
- The local 10-section core artifact is the claim artifact.

## H6.5B: Single Mature-Adapter Claim-Eligibility Probe

Artifacts:

- `manuscript/reviewer_hardening/h6_5b_single_adapter_probe/single_adapter_probe_summary.json`.
- `manuscript/reviewer_hardening/h6_5b_single_adapter_probe/single_adapter_evidence.csv`.
- `manuscript/reviewer_hardening/h6_5b_single_adapter_probe/single_adapter_feasibility_audit.csv`.
- `manuscript/reviewer_hardening/h6_5b_single_adapter_probe/single_adapter_claim_audit.csv`.
- `manuscript/reviewer_hardening/h6_5b_single_adapter_probe/single_adapter_probe_report.md`.

Summary metrics:

| Metric | Value |
|---|---:|
| Adapter attempts | 1 |
| Selected adapter | `liana_communication_adapter` |
| Selected expectation | `h1_pos_gse311609_nsclc_cd274_checkpoint` |
| Parent H6.5A context-allowed count | 1 |
| Claim-eligible adapter count | 0 |
| Mature adapter confirmed positive | false |
| Native output produced | false |
| Contract status | `blocked_missing_native_dependency` |
| `scanpy` available | true |
| `anndata` available | true |
| `liana` available | false |
| `commot` available | false |
| Modal required | false |
| Original CP-Q modified | false |

Decision:

- The preferred LIANA+/COMMOT communication-adapter path was attempted as a
  claim-eligibility probe, but no native mature-adapter output was produced
  because the native dependencies are absent in the execution runtime.

Safe H7 claim:

- H6.5B does not provide mature-adapter confirmation. It provides a documented
  infeasibility row showing that adapter-confirmed wording is not currently
  justified.

Unsafe H7 claim:

- Do not say LIANA+, COMMOT, or mature SOTA adapters independently confirmed
  the NSCLC CD274 route.

## New Discoveries

### Discovery 1: ContextGate Is No Longer Only A Never-Context Router

Before H5D:

- Original CP-Q real-data matrix had 0 `context_allowed` routes.
- H4 hardening replay also had 0 real-data `context_allowed` routes.

After H5D:

- One pre-registered bounded GSE311609 marker-derived task reached
  `context_allowed`.
- The task is NSCLC checkpoint related:
  `h1_pos_gse311609_nsclc_cd274_checkpoint`.

After H6.5A:

- The same route remained `context_allowed` when expanded to 10 selected lung
  sections under the same marker-derived contract.

What this means:

- The manuscript can now say ContextGate exercised both sides of the router in
  the hardening evidence package:
  - reject/abstain unsupported context;
  - allow one bounded real-data marker-derived context task, strengthened by a
    10-section NSCLC expansion.

What this does not mean:

- It does not mean the original CP-Q result was wrong.
- It does not mean full GSE311609 validation is complete.
- It does not mean all real-data settings support context.
- It does not mean mature external adapters confirmed the positive route.

### Discovery 2: GSE311609 Became Partially Usable Through Marker Reconstruction

Before H5C:

- H5B found GSE311609 blocked by missing cell-state/tissue-region labels.

After H5C:

- Marker rules cleared 2 bounded tasks:
  - NSCLC CD274 checkpoint.
  - Breast CXCL12/CXCR4 boundary.

After H5D:

- NSCLC task passed.
- Breast task abstained due replication failure.

What this means:

- Marker-derived replay is a viable bridge for bounded validation.

What this does not mean:

- Marker-derived labels are not a replacement for full expert annotation or
  full-cohort validation.

### Discovery 3: The Breast Boundary Signal Was Not Replication-Stable

The breast CXCL12/CXCR4 task had one section pass the effect gate:

- B16 q value: 0.023438.

But two sections failed:

- B17 q value: 0.171875.
- B15 q value: 0.093750.

What this means:

- ContextGate correctly abstained despite one positive section.
- This is a useful demonstration of replication discipline.

### Discovery 4: Expanded Synthetic Sensitivity Is Broader Than V1

H6 now covers:

- k=3, k=5, k=10;
- radius 40 um and 120 um;
- distance-decay weighting;
- threshold gating;
- receiver-state conditioning;
- rare niche signal;
- null no-context control;
- confounded FOV/sample trap.

What this means:

- The synthetic ladder is no longer only a matched linear k=5 operator check.

What this does not mean:

- It remains synthetic evidence and cannot be treated as real TME communication
  discovery.

### Discovery 5: Mature Adapter Work Is Still Contract-Level, Not Evidence-Level

H5 added adapter contract coverage:

- BANKSY/Graph representation style.
- LIANA/communication style.
- Neighbor-expression style.

But:

- Claim-eligible native SOTA evidence rows: 0.
- H6.5B attempted the preferred LIANA+/COMMOT path for the NSCLC CD274 task and
  still produced 0 claim-eligible adapter rows because native dependencies were
  missing.

What this means:

- H7 can say mature adapter contracts were added.
- H7 should not claim mature SOTA methods independently confirmed the H5D/H6.5A
  route.

## What H7 Must Update

High-priority H7 changes from H5E:

1. Abstract:
   - Keep the original 100 CP-Q route decisions as the original registered
     matrix.
   - Add a separate sentence for H5D:
     2 bounded GSE311609 marker-derived routes, including 1 `context_allowed`.
   - If space allows, update the H5D sentence to note that H6.5A expanded the
     NSCLC CD274 support to 10 selected lung sections.

2. Results:
   - Scope the old "no real-data setting routed to context_allowed" wording to
     the original CP-Q matrix.
   - Add the H5D bounded marker-replay result and exact task ID.
   - Add the H6.5A 10-section NSCLC expansion result as bounded additive
     evidence.
   - Add the H6.5B adapter-infeasibility result to prevent mature-adapter
     overclaiming.

3. Table 3:
   - Split real-data context utility into:
     - original CP-Q matrix: no;
     - additive H5D bounded marker-derived replay: yes, for NSCLC checkpoint
       only;
      - additive H6.5A expansion: yes, same NSCLC checkpoint task across 10
        selected lung sections;
      - mature adapter confirmation: no, LIANA+/COMMOT probe blocked by missing
        native dependencies.

4. Route figures/captions:
   - Either label old route-decision figure as original CP-Q only or add an H5D
     inset/table.

5. GSE311609 wording:
   - Full 41-section validation remains deferred.
   - Bounded H5D 6-section marker-derived replay has been executed.
   - Bounded H6.5A 10-lung-section NSCLC CD274 expansion has been executed.

6. Positive-control/synthetic section:
   - Add H6 expanded ladder as synthetic machinery hardening.
   - Do not merge H6 rows into CP-Q3 original ladder counts.

## Recommended Manuscript Claim Language

Safe H7 claim:

> In the original registered CP-Q matrix, no real-data route reached
> `context_allowed`. In the additive hardening replay, however, a bounded
> marker-derived GSE311609 NSCLC checkpoint task
> (`h1_pos_gse311609_nsclc_cd274_checkpoint`) passed the residual utility,
> wrong-context, replication, and spatial/bootstrap gates; a subsequent bounded
> H6.5A expansion preserved this route across 10 selected lung sections, while
> a breast CXCL12/CXCR4 task abstained because held-out replication failed.

Safe H6.5B claim:

> A targeted LIANA+/COMMOT communication-adapter claim-eligibility probe was
> attempted for the same NSCLC CD274 task, but no native mature-adapter output
> was produced because the required adapter dependencies were absent; therefore
> the positive route should not be described as mature-adapter confirmed.

Safe H6 claim:

> Expanded synthetic controls broadened the machinery check beyond the original
> linear k=5 mean-neighbor ladder, covering k/radius sensitivity,
> distance-decay, threshold-gated, receiver-state-conditioned, rare-niche, null,
> and confounded-trap rungs. These rows support synthetic sensitivity and
> specificity only; they do not constitute real biological context evidence.

Unsafe wording to avoid:

- "The full GSE311609 cohort validates ContextGate."
- "ContextGate found spatial communication broadly in real data."
- "The 100 route decisions should be updated to 102."
- "The H6.5A 10-section expansion is a full GSE311609 replay."
- "Synthetic ladder recovery proves real ligand-receptor biology."
- "Mature SOTA adapters confirmed the positive route."

## Verification Checklist Before H7

Review these items manually before drafting:

- [ ] Confirm H5D route table has exactly 2 rows.
- [ ] Confirm only `h1_pos_gse311609_nsclc_cd274_checkpoint` is
  `context_allowed`.
- [ ] Confirm breast CXCL12/CXCR4 route is `abstain_uncertain`.
- [ ] Confirm NSCLC sections L1, L3, L5 all pass the effect gate.
- [ ] Confirm NSCLC bootstrap CI is entirely above zero:
  `[0.008815, 0.032505]`.
- [ ] Confirm true context beats wrong context in all H5D wrong-control rows.
- [ ] Confirm H5E says `full_scratch_rerun_required = false`.
- [ ] Confirm original CP-Q5 counts remain 100 total and 0 `context_allowed`.
- [ ] Confirm H6 says `does_not_modify_original_cp_q3 = true`.
- [ ] Confirm H6 expanded ladder gate passed.
- [ ] Confirm H6 is described as synthetic machinery evidence only.
- [ ] Confirm H6.5A has 10 attempted/evaluated lung sections.
- [ ] Confirm H6.5A has 10 effect-gate-passing sections.
- [ ] Confirm H6.5A bootstrap CI is entirely above zero:
  `[0.008247, 0.021846]`.
- [ ] Confirm H6.5A full raw bundle downloaded is false.
- [ ] Confirm H6.5B has 0 claim-eligible adapter rows.
- [ ] Confirm H6.5B `liana` and `commot` dependency status are false.
- [ ] Confirm H7 does not claim mature-adapter confirmation.

## Validation Commands Already Run

H5E:

```powershell
python scripts/build_contextgate_h5d_reconciliation_audit.py --overwrite
python -m ruff check scripts/build_contextgate_h5d_reconciliation_audit.py
python -m compileall -q scripts/build_contextgate_h5d_reconciliation_audit.py
```

H6:

```powershell
python scripts/build_contextgate_expanded_ladder.py --overwrite
python -m pytest tests/unit/test_contextgate_expanded_ladder.py tests/integration/test_artifact_contracts.py -q
python -m ruff check src/cellpack/expanded_ladder.py scripts/build_contextgate_expanded_ladder.py scripts/pipeline_modal_expanded_ladder.py tests/unit/test_contextgate_expanded_ladder.py tests/integration/test_artifact_contracts.py
python -m compileall -q src/cellpack/expanded_ladder.py scripts/build_contextgate_expanded_ladder.py scripts/pipeline_modal_expanded_ladder.py
```

H6 Modal smoke:

```powershell
$env:PYTHONIOENCODING='utf-8'
python -m modal run scripts/pipeline_modal_expanded_ladder.py::expanded_ladder --tier smoke --overwrite
```

H6.5A:

```powershell
python scripts/build_h6_5a_nsclc_cd274_section_expansion.py --run-bounded-replay --max-lung-sections 10 --permutations 63 --bootstrap-iterations 399 --max-receiver-cells 5000 --overwrite
python -m pytest tests/unit/test_nsclc_cd274_section_expansion.py tests/integration/test_artifact_contracts.py -q
python -m compileall -q src/cellpack/nsclc_cd274_section_expansion.py scripts/build_h6_5a_nsclc_cd274_section_expansion.py scripts/pipeline_modal_h6_5a_nsclc_cd274_section_expansion.py tests/unit/test_nsclc_cd274_section_expansion.py
```

H6.5A Modal smoke:

```powershell
$env:PYTHONIOENCODING='utf-8'
python -m modal run scripts/pipeline_modal_h6_5a_nsclc_cd274_section_expansion.py::nsclc_cd274_section_expansion --max-lung-sections 6 --permutations 31 --max-receiver-cells 3000
```

H6.5B:

```powershell
python scripts/build_h6_5b_single_adapter_probe.py --overwrite
python -m pytest tests/unit/test_single_adapter_probe.py tests/unit/test_nsclc_cd274_section_expansion.py tests/integration/test_artifact_contracts.py -q
python -m compileall -q src/cellpack/single_adapter_probe.py scripts/build_h6_5b_single_adapter_probe.py tests/unit/test_single_adapter_probe.py
```

## Current Next Step

Proceed to H7 only after reviewing this file and the hardened evidence snapshot.
H7 should rebuild manuscript artifacts and claim language from the exact
separation:

- original CP-Q matrix;
- additive H5D bounded marker-derived real-data replay;
- additive H6 expanded synthetic ladder.
- additive H6.5A 10-section NSCLC CD274 expansion;
- additive H6.5B adapter-infeasibility result.

## H6.5C Hardened Evidence Freeze

Snapshot directory:

- `manuscript/snapshots/hardened-pre-h7-evidence-complete-2026-05-13/`

Snapshot archive:

- `manuscript/snapshots/hardened-pre-h7-evidence-complete-2026-05-13.zip`

Archive SHA256:

- `EAF5FDD310A86ADF93D2DB2531B1BFBF420A2936E5488810349D9B6AB78B0B18`

Snapshot manifest:

- `manuscript/snapshots/hardened-pre-h7-evidence-complete-2026-05-13/snapshot_manifest.json`

Claim-boundary note:

- `manuscript/snapshots/hardened-pre-h7-evidence-complete-2026-05-13/snapshot_claim_boundary.md`

Freeze note:

- Evidence expansion stops here.
- No git tag was created because the frozen evidence includes generated and
  currently uncommitted artifacts; the archive plus manifest is the
  authoritative pre-H7 freeze.
- Linear H6.5C issue `RIS-70` is synced and marked Done.
