# Submission Evidence Hardening Ledger

This ledger records the task-by-task evidence trail for the submission
hardening phase. It is intentionally separate from the manuscript prose so the
paper can stay clean while the project retains a reviewer-ready audit trail.

## Linear Map

- Project: ContextGate submission evidence hardening
- Project URL: https://linear.app/rishyanth/project/contextgate-submission-evidence-hardening-4e3e7ec0b8f6
- H0 freeze issue: RIS-53
- H1 expectation registry issue: RIS-54
- H2 validation-scale preflight issue: RIS-55
- H3 spatial inference issue: RIS-56
- H4 validation replay issue: RIS-57
- H5 mature adapter replay issue: RIS-58
- H6 synthetic ladder expansion issue: RIS-59
- H6.5A bounded NSCLC CD274 section-expansion issue: RIS-68
- H6.5B single mature-adapter claim-eligibility issue: RIS-69
- H6.5C hardened pre-H7 evidence freeze issue: RIS-70
- H7 manuscript artifact rebuild issue: RIS-60
- H8 release QA issue: RIS-61

## H0 - Freeze Current Complete Package

Status: Completed on 2026-05-13.

Purpose: preserve the current complete submission package before evidence
hardening begins, so the project can fall back to the existing manuscript,
figures, tables, supplement, references, and public artifact bundle if the
extension work becomes noisy or infeasible.

### Git Anchors

- Root repository commit: `4eeb6e23637ad0dc083904a4d3bb9e0dbda8b969`
- Root repository tag: `v1-current-complete`
- Tag commit: `4eeb6e23637ad0dc083904a4d3bb9e0dbda8b969`
- Public artifact repository commit: `1c9ae9a51106f3163d9127d61ee55d1c35ac3a36`

### Snapshot Artifacts

- Snapshot directory: `manuscript/snapshots/v1-current-complete-2026-05-13/`
- Snapshot archive: `manuscript/snapshots/v1-current-complete-2026-05-13.zip`
- Snapshot manifest: `manuscript/snapshots/v1-current-complete-2026-05-13/snapshot_manifest.md`
- File-level checksum manifest: `manuscript/snapshots/v1-current-complete-2026-05-13/snapshot_file_manifest.csv`
- Archive SHA256: `23900B3201837C74A40FA9A9C338F7D53FFFD136000105CE808B0A6654C8F9D0`
- Archive size: 14,115,818 bytes
- Snapshot file count: 709

### Frozen Scope

- Root manuscript PDFs, including the review-analysis PDF.
- Overleaf final text exports.
- Manuscript TeX source and CP-Q8.10 PDF render.
- Figure singles and manuscript table artifacts.
- Submission supplement workbook and supporting files.
- Complete bibliography and metadata audit.
- Public artifact repository README and artifact bundle.
- Data manifests where present.
- Master plan, TODO, and hardening plan tracking files.

### Verification

- Confirmed the `v1-current-complete` tag resolves to the current root commit.
- Confirmed the public artifact repository is clean at the recorded commit.
- Generated a file-level SHA256 manifest for the snapshot contents.
- Generated a compressed archive and recorded its SHA256 digest.
- Verified the current CP-Q8.10 PDF begins with a valid `%PDF` header.
- Verified the supplementary workbook opens as an `.xlsx` archive containing
  `xl/workbook.xml`.
- No Modal run was required for H0 because this task freezes artifacts rather
  than executing benchmark jobs.

## H1 - Pre-Registered Route Expectation Registry

Status: Completed on 2026-05-13.

Purpose: freeze a compact route-expectation set before validation replay,
spatially aware inference, mature adapter experiments, or expanded ladder runs.
This protects the hardening phase from post-hoc positive-result hunting.

### Registry Artifacts

- Registry manifest: `data/manifests/contextgate_route_expectations.yaml`
- Validation helper: `src/cellpack/route_expectations.py`
- Unit tests: `tests/unit/test_contextgate_route_expectations.py`
- Reviewer-facing table: `manuscript/reviewer_hardening/contextgate_route_expectation_registry.md`
- Artifact registry entry: `contextgate_route_expectations/h1_registry`
- Registry hash: `sha256:d67f17408c744b89cc2326a80e91e79fd1612fbb369b1bff502c9df0f901943d`

### Registry Scope

- 17 total expectations.
- 4 expected real-data context-positive candidates.
- 3 expected expression-only controls.
- 3 expected abstain or panel-blocked cases.
- 3 strict null, confounded, or panel-blocked control rows.
- 3 wrong-context control rows.
- 1 synthetic positive-control extension row.

### Guardrails

- Missing panel targets force `abstain_uncertain`, not `context_allowed`.
- `context_allowed` expectations require held-out replication and wrong-context
  controls at the registry level.
- GSE311609 positive candidates remain preflight-gated until H2 confirms panel
  coverage, labels, coordinates, and donor/section metadata.
- Synthetic positive controls can validate machinery but cannot support a real
  biological context claim.

### Verification

- `pytest tests/unit/test_contextgate_route_expectations.py`: 5 passed.
- `pytest tests/unit/test_contextgate_benchmark_manifest.py tests/unit/test_contextgate_route_expectations.py`: 8 passed.
- `python -m ruff check src/cellpack/route_expectations.py tests/unit/test_contextgate_route_expectations.py`: passed.
- No Modal run was required for H1 because this task freezes expectations and
  validates manifest joins; real data execution starts in H2/H4.

## H2 - Validation-Scale Dataset Preflight

Status: Completed on 2026-05-13.

Purpose: preflight the frozen validation-scale GSE311609 Xenium cohort against
the H1 route expectations before any expensive replay, avoiding accidental
treatment of failed conversion work as biological evidence.

### Preflight Artifacts

- Preflight builder: `src/cellpack/validation_scale_preflight.py`
- Local artifact script: `scripts/build_validation_scale_preflight.py`
- Bounded Modal smoke script: `scripts/pipeline_modal_gse311609_preflight.py`
- Artifact directory: `manuscript/reviewer_hardening/h2_validation_preflight/`
- Summary JSON: `gse311609_preflight_summary.json`
- Loader compatibility CSV: `gse311609_loader_compatibility.csv`
- Panel coverage CSV: `gse311609_panel_coverage.csv`
- Split feasibility CSV: `gse311609_split_feasibility.csv`
- Modal snapshot plan CSV: `gse311609_modal_snapshot_plan.csv`
- Reviewer report: `gse311609_validation_preflight.md`
- Summary SHA256: `bb3569b2255d6298feefeb66425ee4dc02077cd463b61a06cfe9fa4cca7c7c35`

### Decision

Decision: `go_bounded_modal_preflight_only`.

Full validation replay is not allowed yet. GSE311609 has the desired scale
signal (41 sections/samples, 27 reported donors), but the current contract still
requires Modal extraction of unit metadata, coordinates, expression matrix,
panel-specific gene metadata, donor/section labels, and analysis-level labels.
The three H1 GSE311609 context-positive expectations remain blocked until
panel coverage is verified.

### Modal Smoke

- Command: `python -m modal run scripts/pipeline_modal_gse311609_preflight.py::gse311609_preflight --max-units 1000`
- Run URL: `https://modal.com/apps/rishyanthreddy101/main/ap-A0yxPUvQvy5RdMPI6FgHBk`
- Result: passed.
- `modal_smoke_passed`: true.
- `schema_passed`: true.
- `raw_bundle_downloaded`: false.

### Verification

- `pytest tests/unit/test_gse311609_loader_contract.py tests/integration/test_artifact_contracts.py`: 7 passed.
- `python -m ruff check src/cellpack/validation_scale_preflight.py scripts/build_validation_scale_preflight.py scripts/pipeline_modal_gse311609_preflight.py tests/unit/test_gse311609_loader_contract.py tests/integration/test_artifact_contracts.py`: passed.
- Local artifact generation completed with `python scripts/build_validation_scale_preflight.py --overwrite`.
- H2 summary registered in `data/manifests/artifact_registry.yaml`.

## H3 - Spatially Aware Inference Layer

Status: Completed on 2026-05-13.

Purpose: add a block-level inference overlay so ContextGate can distinguish
nominal cell-level evidence from donor/sample/section/FOV-aware evidence. The
overlay is additive by default and does not change route labels unless a future
replay explicitly requires spatial inference.

### Artifacts

- Schema: `data/manifests/contextgate_spatial_inference_schema.yaml`
- Engine: `src/cellpack/spatial_inference.py`
- Local smoke builder: `scripts/build_contextgate_spatial_inference_smoke.py`
- Bounded Modal smoke: `scripts/pipeline_modal_contextgate_spatial_inference.py`
- Artifact directory: `manuscript/reviewer_hardening/h3_spatial_inference/`
- Spatial inference CSV: `contextgate_spatial_inference.csv`
- Nominal-vs-spatial summary CSV: `contextgate_nominal_vs_spatial_summary.csv`
- Decision overlay CSV: `contextgate_spatial_decision_overlay.csv`
- Summary JSON: `contextgate_spatial_inference_summary.json`
- Reviewer report: `contextgate_spatial_inference_report.md`
- Summary SHA256: `3a7208ccbc4b349d4ee0462bf5fa764013108c16149572ec895104543b6cf2bb`

### Implemented Evidence Fields

- `spatial_test_type`
- `block_unit`
- `n_blocks`
- `block_permutation_p`
- `block_permutation_q`
- `bootstrap_unit`
- `bootstrap_ci_low`
- `bootstrap_ci_high`
- `effective_sample_size_estimate`
- `spatial_inference_status`

### Modal Smoke

- Command: `python -m modal run scripts/pipeline_modal_contextgate_spatial_inference.py::contextgate_spatial_inference_smoke --max-rows 100`
- Run URL: `https://modal.com/apps/rishyanthreddy101/main/ap-ct68PotjaINgODlRbP6Cv3`
- Result: passed.
- `modal_smoke_passed`: true.
- `schema_passed`: true.
- `raw_data_downloaded`: false.

### Verification

- `pytest tests/unit/test_spatial_inference_block_permutation.py tests/unit/test_spatial_inference_bootstrap.py tests/integration/test_artifact_contracts.py`: 10 passed.
- `python -m ruff check src/cellpack/spatial_inference.py scripts/build_contextgate_spatial_inference_smoke.py scripts/pipeline_modal_contextgate_spatial_inference.py tests/unit/test_spatial_inference_block_permutation.py tests/unit/test_spatial_inference_bootstrap.py tests/integration/test_artifact_contracts.py`: passed.
- H3 artifact summary registered in `data/manifests/artifact_registry.yaml`.

### Readiness Review Before H4

- Re-read the hardening plan, TODO tracker, and ledger before opening H4.
- Confirmed H2's GSE311609 decision remains `go_bounded_modal_preflight_only`;
  full validation replay is blocked until H4 extracts and verifies loader,
  panel, donor/section metadata, and label-join contracts.
- Fixed an H3 overlay edge case so an unmatched decision row is treated as
  `not_evaluated` and downgraded when spatial inference is explicitly required
  for `context_allowed`.
- Added an integration test for the missing-spatial-match downgrade path.
- Re-ran the H0-H3/H4-entry gate:
  `python -m pytest tests/unit/test_contextgate_benchmark_manifest.py tests/unit/test_contextgate_route_expectations.py tests/unit/test_gse311609_loader_contract.py tests/unit/test_contextgate_decisions.py tests/unit/test_spatial_inference_block_permutation.py tests/unit/test_spatial_inference_bootstrap.py tests/integration/test_artifact_contracts.py`
  passed with 28 tests.
- Re-ran targeted `ruff` on the H1-H3 source/scripts/tests: passed.
- Re-ran `git diff --check` on H1-H3 touched files: no whitespace errors;
  Git reported only LF-to-CRLF working-tree warnings.

## H4 - Validation Replay Through ContextGate

Status: Completed on 2026-05-13.

Purpose: run the H1 pre-registered expectation set through the available
H2/H3 evidence contracts and registered CP-Q2/CP-Q5 artifacts without allowing
uncleared validation-scale rows to become context-positive evidence.

### Artifacts

- Schema: `data/manifests/contextgate_validation_replay_schema.yaml`
- Engine: `src/cellpack/validation_replay.py`
- Local builder: `scripts/build_contextgate_validation_replay.py`
- Bounded Modal replay: `scripts/pipeline_modal_validation_replay.py`
- Artifact directory: `manuscript/reviewer_hardening/h4_validation_replay/`
- Job manifest: `contextgate_validation_job_manifest.csv`
- Evidence table: `contextgate_validation_evidence.csv`
- Wrong-context controls: `contextgate_validation_wrong_context_controls.csv`
- Expression baseline table: `contextgate_validation_expression_baseline.csv`
- Spatial overlay: `contextgate_validation_spatial_overlay.csv`
- Final route table: `contextgate_validation_route_decisions.csv`
- Summary JSON: `contextgate_validation_replay_summary.json`
- Reviewer report: `contextgate_validation_replay_report.md`
- Summary SHA256:
  `bfe03349472e65585938069c601eef5a3e5c99eb47a3cc697f87cd9c894dbfd0`

### Route Outcome

- Expectation rows: 17.
- Final route counts: `abstain_uncertain` = 10, `expression_only` = 3,
  `rejected_or_access_blocked` = 4.
- Real-data `context_allowed` rows: 0.
- Wrong-context control rows: 12.
- Wrong-context controls cannot create context: true.
- GSE311609 rows remain `rejected_or_access_blocked` because H2 did not clear
  full validation replay.
- H6-deferred rows: 2 expanded-ladder expectations that require future
  distance-decay or confounded positive-control execution.

### Modal Replay

- Smoke command:
  `python -m modal run scripts/pipeline_modal_validation_replay.py::validation_replay --tier smoke --overwrite`
- Smoke run URL:
  `https://modal.com/apps/rishyanthreddy101/main/ap-oCQLNm84Y6LrWkEDlwxKCw`
- Core command:
  `python -m modal run scripts/pipeline_modal_validation_replay.py::validation_replay --tier core --overwrite`
- Core run URL:
  `https://modal.com/apps/rishyanthreddy101/main/ap-RXugkS4Np6DT6ODYJYTGP2`
- Result: smoke and core passed.
- `schema_passed`: true.
- `raw_data_downloaded`: false.
- Full replay remains blocked until loader, panel, donor/section metadata, and
  label-join contracts clear.

### Verification

- `python -m pytest tests/unit/test_contextgate_benchmark_manifest.py tests/unit/test_contextgate_route_expectations.py tests/unit/test_gse311609_loader_contract.py tests/unit/test_contextgate_decisions.py tests/unit/test_spatial_inference_block_permutation.py tests/unit/test_spatial_inference_bootstrap.py tests/unit/test_contextgate_validation_replay.py tests/integration/test_artifact_contracts.py`:
  33 passed.
- `python -m pytest tests/integration/test_pipeline_spine.py tests/integration/test_artifact_contracts.py`:
  7 passed.
- Targeted `ruff` on H1-H4 source/scripts/tests: passed.
- YAML parse of H1/H4/registry manifests: passed.
- `git diff --check` on H4 touched files: no whitespace errors; Git reported
  only LF-to-CRLF working-tree warnings.
- H4 artifact summary registered in `data/manifests/artifact_registry.yaml`.

## H5 - Mature External Adapter Replay Contracts

Status: Completed on 2026-05-13.

Purpose: add a bounded, honest replay layer for mature external method families
without treating unadapted native outputs as ContextGate evidence. H5 records
whether each adapter can emit the shared contract fields required for
true-context score, expression-only comparison, wrong-context control,
replication status, spatial status, and route implications.

### Artifacts

- Adapter registry: `data/manifests/contextgate_sota_adapter_registry.yaml`
- Adapter schema: `data/manifests/contextgate_sota_adapter_schema.yaml`
- Engine: `src/cellpack/sota_adapters.py`
- Local builder: `scripts/build_contextgate_sota_adapters.py`
- Bounded Modal replay: `scripts/pipeline_modal_sota_adapters.py`
- Artifact directory: `manuscript/reviewer_hardening/h5_mature_adapter_replay/`
- Adapter evidence CSV: `contextgate_sota_adapter_evidence.csv`
- Adapter method-prediction CSV/Parquet:
  `contextgate_sota_adapter_method_predictions.*`
- Adapter feasibility ledger: `contextgate_sota_adapter_feasibility_ledger.csv`
- Adapter comparison table: `contextgate_sota_adapter_comparison.csv`
- Parameter cards:
  `parameter_cards/banksy_feature_adapter.md`,
  `parameter_cards/liana_communication_adapter.md`,
  `parameter_cards/neighbor_expression_adapter.md`
- Summary JSON: `contextgate_sota_adapter_replay_summary.json`
- Reviewer report: `contextgate_sota_adapter_replay_report.md`
- Summary SHA256:
  `669b8c8f8773bab053b808cfebef623e0d9081ab49f39029f3b86f8a89150f4d`

### Adapter Outcome

- Adapter families represented: 3.
- Passing contract-smoke rows: 3.
- Valid native SOTA evidence rows: 0.
- Claim-eligible adapter rows: 0.
- Route candidates: `abstain_uncertain` = 2,
  `rejected_or_access_blocked` = 1.
- Contract status counts: `adapter_contract_required` = 2,
  `blocked_by_parent_preflight` = 1.
- BANKSY/GraphST-style representation remains blocked until a frozen
  feature-to-CP-Q-head adapter exists.
- LIANA+/COMMOT-style communication remains blocked by the GSE311609 parent
  preflight and the need for a label-rich CCC-to-residual-utility adapter.
- CellNeighborEX/NICHES-style neighbor expression remains blocked until a
  cell-state-specific neighbor-effect adapter is frozen.

### Modal Replay

- BANKSY smoke URL:
  `https://modal.com/apps/rishyanthreddy101/main/ap-GFtlJlCC2pcCUy17eEXtYO`
- LIANA smoke URL:
  `https://modal.com/apps/rishyanthreddy101/main/ap-FDcdT81XZPFMMO6QCHs6mq`
- Neighbor-expression smoke URL:
  `https://modal.com/apps/rishyanthreddy101/main/ap-ufJ8xy5emVUOVQqau3T2db`
- Combined core URL:
  `https://modal.com/apps/rishyanthreddy101/main/ap-2uz4BKZhuHZFeTUFtyIJ5a`
- Result: all smoke/core contract runs passed.
- `schema_passed`: true.
- `raw_data_downloaded`: false.

### Verification

- `python -m pytest tests/unit/test_contextgate_adapter_contract.py tests/integration/test_artifact_contracts.py`:
  12 passed.
- H1-H5 broad gate:
  `python -m pytest tests/unit/test_contextgate_benchmark_manifest.py tests/unit/test_contextgate_route_expectations.py tests/unit/test_gse311609_loader_contract.py tests/unit/test_contextgate_decisions.py tests/unit/test_spatial_inference_block_permutation.py tests/unit/test_spatial_inference_bootstrap.py tests/unit/test_contextgate_validation_replay.py tests/unit/test_contextgate_adapter_contract.py tests/integration/test_pipeline_spine.py tests/integration/test_artifact_contracts.py`
  passed with 40 tests.
- Targeted `ruff` on H1-H5 source/scripts/tests: passed.
- YAML parse of H5 registry/schema and artifact registry: passed.
- H5 summary registered in `data/manifests/artifact_registry.yaml`.

## H5A - Real-Data Positive Evidence Feasibility Sprint

Status: Completed on 2026-05-13.

Purpose: stop the hardening sequence before synthetic-only H6 and determine
whether any existing real-data artifact is actually close to a claim-eligible
`context_allowed` route. This is a go/no-go audit, not another optimistic
expansion task.

### Artifacts

- Schema: `data/manifests/contextgate_real_positive_feasibility_schema.yaml`
- Engine: `src/cellpack/real_positive_feasibility.py`
- Local builder: `scripts/build_contextgate_real_positive_feasibility.py`
- Artifact directory:
  `manuscript/reviewer_hardening/h5a_real_positive_feasibility/`
- Candidate table: `contextgate_real_positive_candidate_table.csv`
- Gate-gap table: `contextgate_real_positive_gate_gaps.csv`
- Dataset-readiness table: `contextgate_real_positive_dataset_readiness.csv`
- Expectation-runnability table:
  `contextgate_real_positive_expectation_runnability.csv`
- Summary JSON: `contextgate_real_positive_feasibility_summary.json`
- Reviewer report: `contextgate_real_positive_feasibility_report.md`
- Summary SHA256:
  `f5fd11bc314c7b3aad7117375f58b240275ef099fc78dce78e255952f39ec41f`

### Feasibility Outcome

- Candidates audited: 30.
- Immediate replay-ready real-data `context_allowed` candidates: 0.
- Current ContextGate real-data `context_allowed` decisions: 0.
- Blocked GSE311609 candidates: 4.
- Near-miss/localized candidates: 3.
- Go/no-go decision: `go_clear_gse311609_first`.
- H6 recommendation: proceed only as synthetic robustness; do not treat H6 as
  solving the missing real-data positive evidence gap.

### Interpretation

The strongest current-artifact lead is a localized exploratory PDAC row
(`gse310352_cosmx_pdac_1k`, `cus_020`), but it is not pre-registered as a
context-positive expectation and fails the residual, wrong-context, replication,
and spatial evidence requirements. The only high-value pre-registered route to
a real positive is still GSE311609 clearance, because the current GSE rows are
blocked before full replay.

### Modal Policy

No H5A Modal run was performed. H5A is intentionally an artifact-only audit.
Modal replay should resume only if a later task clears a runnable real-positive
candidate.

### Verification

- `python scripts/build_contextgate_real_positive_feasibility.py --overwrite`:
  passed.
- `python -m pytest tests/unit/test_real_positive_feasibility.py tests/integration/test_artifact_contracts.py`:
  12 passed.
- H1-H5A broad gate:
  `python -m pytest tests/unit/test_contextgate_benchmark_manifest.py tests/unit/test_contextgate_route_expectations.py tests/unit/test_gse311609_loader_contract.py tests/unit/test_contextgate_decisions.py tests/unit/test_spatial_inference_block_permutation.py tests/unit/test_spatial_inference_bootstrap.py tests/unit/test_contextgate_validation_replay.py tests/unit/test_contextgate_adapter_contract.py tests/unit/test_real_positive_feasibility.py tests/integration/test_pipeline_spine.py tests/integration/test_artifact_contracts.py`
  passed with 45 tests.
- Targeted `ruff` on H1-H5A source/scripts/tests: passed.
- YAML parse of H5A schema and artifact registry: passed.
- H5A summary registered in `data/manifests/artifact_registry.yaml`.

## Pre-H5B Next Task (Closed)

The next scientific decision is whether to clear GSE311609 before H6 or to
submit the manuscript as a conservative benchmark. H6 can still improve
synthetic robustness, but H5A shows it will not fix the missing real-data
positive route. This decision was closed by H5B below.

## H5B - GSE311609 Clearance Sprint

Status: Completed on 2026-05-13.

Purpose: test whether the blocked GSE311609 validation cohort can become a
bounded real-data positive replay target before H6 synthetic-only work
continues.

### Artifacts

- Schema: `data/manifests/contextgate_gse311609_clearance_schema.yaml`
- Engine: `src/cellpack/gse311609_clearance.py`
- Local builder: `scripts/build_gse311609_clearance.py`
- Modal bounded probe: `scripts/pipeline_modal_gse311609_clearance.py`
- Artifact directory:
  `manuscript/reviewer_hardening/h5b_gse311609_clearance/`
- Summary JSON: `gse311609_clearance_summary.json`
- File/sample inventories:
  `gse311609_file_inventory.csv`, `gse311609_sample_inventory.csv`
- Contract tables:
  `gse311609_loader_contract.csv`,
  `gse311609_metadata_join_clearance.csv`,
  `gse311609_panel_coverage_clearance.csv`
- Modal/fallback tables:
  `gse311609_modal_probe_plan.csv`,
  `gse311609_fallback_decision.csv`
- GEO filelist snapshot: `gse311609_filelist_snapshot.txt`
- Bounded raw probe summary: `gse311609_bounded_raw_probe.json`
- Reviewer report: `gse311609_clearance_report.md`
- Summary SHA256:
  `7c7f3f27acc8d753765378f1d9dac19e1f7c0af6924ef078a0ba9f22e5c7692e`

### Clearance Outcome

- Clearance decision: `blocked_keep_gse311609_as_future_work`.
- GEO archive members parsed: 246.
- Samples parsed: 41 total, 22 lung, 19 breast.
- Inferred patient/donor labels: 27.
- Complete sample bundles: 41/41.
- Bounded raw range probe downloaded: 24,912,896 bytes.
- Full raw bundle downloaded: false.
- Loader required contract: passed.
- Metadata required contract: failed because bounded cell metadata exposes no
  cell-state or tissue-region label columns.
- Panel required contract: failed because the NSCLC TGF-beta/stromal H1 module
  is partial in the representative Prime 5K probe (`COL1A1` and `ACTA2`
  absent).
- CD274/PDCD1 NSCLC and CXCL12/CXCR4 breast expectations remain panel-plausible
  but not claim-eligible until label strategy clears.

### Modal Replay

- Modal bounded probe URL:
  `https://modal.com/apps/rishyanthreddy101/main/ap-lFXXSE3WEK8TQ7HBxZOEDx`
- Result: passed.
- `schema_passed`: true.
- `raw_data_download_mode`: `bounded_byte_range`.
- `full_raw_bundle_downloaded`: false.

### Verification

- `python scripts/build_gse311609_clearance.py --run-bounded-probe --overwrite`:
  passed.
- Focused H5B test gate:
  `python -m pytest tests/unit/test_gse311609_clearance.py tests/integration/test_artifact_contracts.py`
  passed with 14 tests.
- H1-H5B broad gate:
  `python -m pytest tests/unit/test_contextgate_benchmark_manifest.py tests/unit/test_contextgate_route_expectations.py tests/unit/test_gse311609_loader_contract.py tests/unit/test_contextgate_decisions.py tests/unit/test_spatial_inference_block_permutation.py tests/unit/test_spatial_inference_bootstrap.py tests/unit/test_contextgate_validation_replay.py tests/unit/test_contextgate_adapter_contract.py tests/unit/test_real_positive_feasibility.py tests/unit/test_gse311609_clearance.py tests/integration/test_pipeline_spine.py tests/integration/test_artifact_contracts.py`
  passed with 51 tests.
- Targeted `ruff` on H5B source/scripts/tests: passed.
- YAML parse of H5B schema and artifact registry: passed.

## Pre-H5C Next Task (Closed)

Do not proceed directly to real positive replay. The next real-data decision
task should be marker-label reconstruction for GSE311609 or fallback
validation-dataset preflight. H6 can follow later as synthetic robustness, but
H5B confirms it does not solve the missing real-data positive route. This
decision was closed by H5C below.

## H5C - GSE311609 Marker-Label Reconstruction Feasibility

Status: Completed on 2026-05-13.

Purpose: test whether GSE311609 can be rescued for bounded real-data positive
replay by freezing transparent marker-derived label rules before replay.

### Artifacts

- Schema: `data/manifests/contextgate_gse311609_marker_feasibility_schema.yaml`
- Engine: `src/cellpack/gse311609_marker_feasibility.py`
- Local builder: `scripts/build_gse311609_marker_feasibility.py`
- Modal bounded probe:
  `scripts/pipeline_modal_gse311609_marker_feasibility.py`
- Artifact directory:
  `manuscript/reviewer_hardening/h5c_gse311609_marker_feasibility/`
- Summary JSON: `gse311609_marker_feasibility_summary.json`
- Marker rules: `gse311609_marker_rule_registry.csv`
- Marker expression probe: `gse311609_marker_expression_probe.csv`
- Rule feasibility: `gse311609_marker_rule_feasibility.csv`
- Expectation mapping: `gse311609_expectation_marker_mapping.csv`
- Replay contract: `gse311609_marker_replay_contract.csv`
- Marker probe JSON: `gse311609_marker_probe_summary.json`
- Reviewer report: `gse311609_marker_feasibility_report.md`
- Summary SHA256:
  `d9f69d1bba36d5e204f3271729353c9f3ae1587367a35fc099f69c90c085cd34`

### Marker Feasibility Outcome

- Decision: `go_bounded_marker_positive_replay`.
- Marker rules frozen: 9.
- Bounded marker probe samples: 2.
- Bounded raw range probe downloaded: 22,211,584 bytes.
- Full raw bundle downloaded: false.
- Passing marker rules: 8/9.
- Failed marker rules: 1/9 (`lung_tgfb_stromal_strict`).
- Eligible H1 context-positive expectations:
  - `h1_pos_gse311609_nsclc_cd274_checkpoint`
  - `h1_pos_gse311609_breast_cxcl12_cxcr4_boundary`
- Blocked H1 context-positive expectation:
  - `h1_pos_gse311609_nsclc_tgfb_stroma`

### Modal Replay

- Modal bounded marker probe URL:
  `https://modal.com/apps/rishyanthreddy101/main/ap-SM6xFjBmpygBgLnu3Jowin`
- Result: passed.
- `schema_passed`: true.
- `raw_data_download_mode`: `bounded_byte_range`.
- `full_raw_bundle_downloaded`: false.

### Verification

- `python scripts/build_gse311609_marker_feasibility.py --run-bounded-probe --overwrite`:
  passed.
- Focused H5C test gate:
  `python -m pytest tests/unit/test_gse311609_marker_feasibility.py tests/integration/test_artifact_contracts.py`
  passed with 14 tests.
- Targeted `ruff` on H5C source/scripts/tests: passed.

### Claim Limit

H5C is not a real-data positive route result. It clears two pre-registered
tasks for bounded H5D replay only. H5D must still evaluate residual utility,
wrong-context controls, held-out replication, and spatially aware inference
before the manuscript can claim any real-data `context_allowed` route.

## H5D - Bounded GSE311609 Marker-Positive Replay

Status: Completed on 2026-05-13.

Purpose: run the two H5C-cleared GSE311609 expectations through marker-derived
receiver/context labels, expression-only residual baselines, wrong-context
controls, held-out section replication, block bootstrap evidence, and final
ContextGate routing.

### Artifacts

- Schema: `data/manifests/contextgate_gse311609_marker_replay_schema.yaml`
- Engine: `src/cellpack/gse311609_marker_replay.py`
- Local builder: `scripts/build_gse311609_marker_replay.py`
- Modal bounded replay:
  `scripts/pipeline_modal_gse311609_marker_replay.py`
- Artifact directory:
  `manuscript/reviewer_hardening/h5d_gse311609_marker_replay/`
- Summary JSON: `gse311609_marker_replay_summary.json`
- Sample manifest: `gse311609_marker_replay_sample_manifest.csv`
- Marker-label summary: `gse311609_marker_replay_label_summary.csv`
- Residual utility table: `gse311609_marker_replay_residual_utility.csv`
- Wrong-context controls:
  `gse311609_marker_replay_wrong_context_controls.csv`
- Spatial/bootstrap overlay:
  `gse311609_marker_replay_spatial_overlay.csv`
- Replication summary: `gse311609_marker_replay_replication_summary.csv`
- Route decisions: `gse311609_marker_replay_route_decisions.csv`
- Replay probe JSON: `gse311609_marker_replay_probe_summary.json`
- Reviewer report: `gse311609_marker_replay_report.md`
- Summary SHA256:
  `fa3952fd53babf5a2e35a17e94797c8cbcaa9fbb03727546580b5739f29e444e`
- Route-decision SHA256:
  `5f7f501eea312444f6a4244c65b4127ebb323b64b152e49a428c2d755b183474`

### Replay Outcome

- Decision: `real_context_allowed_observed`.
- Bounded replay tier: `core`.
- Raw download mode: `bounded_byte_range`.
- Bounded bytes downloaded: 102,267,392.
- Full raw bundle downloaded: false.
- Tasks evaluated: 2.
- Sections evaluated: 6.
- Effect-gate sections: 4/6.
- Final routes:
  - `h1_pos_gse311609_nsclc_cd274_checkpoint`:
    `context_allowed`.
  - `h1_pos_gse311609_breast_cxcl12_cxcr4_boundary`:
    `abstain_uncertain` because wrong-context separation, held-out
    replication, and spatial/bootstrap gates did not pass.

### Positive Route Details

The NSCLC checkpoint task passed on three bounded Prime 5K lung sections:

- L1: residual utility delta `0.0277256060`, q `0.0234375`.
- L3: residual utility delta `0.0088147491`, q `0.0234375`.
- L5: residual utility delta `0.0348954026`, q `0.0234375`.

Replication summary:

- Section count: 3.
- Effect-gate section count: 3.
- Median residual utility delta: `0.0277256060`.
- Bootstrap CI: `[0.0088147491, 0.0325054704]`.
- Replication gate: passed.
- Wrong-context gate: passed.
- Expression-baseline gate: passed.
- Spatial/bootstrap gate: passed.

### Abstained Route Details

The breast CXCR4 task had positive but inconsistent section evidence:

- B17: q `0.171875`, effect gate failed.
- B16: residual utility delta `0.0286080268`, q `0.0234375`, effect gate
  passed.
- B15: q `0.09375`, effect gate failed.

Final route: `abstain_uncertain` with blockers
`wrong_context_not_separated`, `held_out_replication_not_passed`, and
`spatial_block_bootstrap_not_passed`.

### Modal Replay

- Modal smoke URL:
  `https://modal.com/apps/rishyanthreddy101/main/ap-5TMEIfno9gfKSb2vPA2zQh`
- Modal core URL:
  `https://modal.com/apps/rishyanthreddy101/main/ap-KfjWifPvF4SKfDiyKHC8Ju`
- Result: passed.
- `schema_passed`: true.
- `raw_data_download_mode`: `bounded_byte_range`.
- `full_raw_bundle_downloaded`: false.

### Verification

- Local core replay:
  `python scripts/build_gse311609_marker_replay.py --run-bounded-replay --tier core --permutations 63 --bootstrap-iterations 399 --max-receiver-cells 5000 --overwrite`
  passed.
- Focused H5D test gate:
  `python -m pytest tests/unit/test_gse311609_marker_replay.py tests/integration/test_artifact_contracts.py -q`
  passed with 15 tests.
- Targeted `ruff` on H5D source/scripts/tests: passed.
- `git diff --check` for H5D files: passed, with only the existing
  LF-to-CRLF warning for `tests/integration/test_artifact_contracts.py`.

### Claim Limit

H5D supplies one bounded real-data marker-derived `context_allowed` route. The
manuscript may use this to say ContextGate exercised its allow side under a
pre-registered marker-label contract, but it must state the bounded section set,
the marker-derived labels, and the remaining need for broader validation-scale
replay.

## H5E - Result Reconciliation and Rerun Decision Audit

Status: Completed on 2026-05-13.

Purpose: answer whether H5D changes require a full from-scratch rerun of all
original CP-Q results, figures, and tables, or a targeted H7 reconciliation.

### Artifacts

- Builder: `scripts/build_contextgate_h5d_reconciliation_audit.py`
- Artifact directory:
  `manuscript/reviewer_hardening/h5e_result_reconciliation_audit/`
- Summary JSON: `contextgate_h5e_reconciliation_summary.json`
- Code-scope audit: `contextgate_h5e_code_scope_audit.csv`
- Gate-scope comparison: `contextgate_h5e_gate_scope_comparison.csv`
- Claim-update map: `contextgate_h5e_claim_update_map.csv`
- Figure/table impact map: `contextgate_h5e_figure_table_impact.csv`
- Manuscript claim hits: `contextgate_h5e_manuscript_claim_hits.csv`
- Reviewer report: `contextgate_h5e_reconciliation_report.md`
- Summary SHA256:
  `4E7921B0EB16344CE22FCEA5334FDC7F1F11E9BB3743598FE41B39510414B205`

### Rerun Decision

- Decision: `targeted_reconciliation_no_full_scratch_rerun`.
- Full scratch rerun required: false.
- Original CP-Q gate or matrix code changed: false.
- Original CP-Q5 denominator: 100 route decisions.
- Original CP-Q5 `context_allowed` count: 0.
- Original CP-Q5 route counts:
  - `expression_only`: 23.
  - `abstain_uncertain`: 40.
  - `positive_control_only`: 37.
- H5D additive route rows: 2.
- H5D additive `context_allowed` count: 1.
- H5D positive route:
  `h1_pos_gse311609_nsclc_cd274_checkpoint`.

### H7 Required Updates

- Keep the 100-decision CP-Q route denominator unchanged.
- Add a separate H5D bounded marker-replay result sentence/subsection.
- Revise absolute zero-real-data wording in the Abstract, Results,
  Discussion/Limitations, route captions, and Table 3.
- Split Table 3's real-data context-utility row into original CP-Q evidence
  versus additive H5D evidence.
- Clarify that full 41-section GSE311609 validation remains deferred while a
  bounded 6-section marker-derived replay has been executed.
- Do not inject H5D into Figure 2 or other CP-Q6 aggregate figures unless H7
  creates an explicitly separate hardening figure/inset.

### Verification

- `python scripts/build_contextgate_h5d_reconciliation_audit.py --overwrite`:
  passed.
- `python -m ruff check scripts/build_contextgate_h5d_reconciliation_audit.py`:
  passed.
- `python -m compileall -q scripts/build_contextgate_h5d_reconciliation_audit.py`:
  passed.
- H5E summary assertion check: passed.
- `git diff --check -- scripts/build_contextgate_h5d_reconciliation_audit.py manuscript/reviewer_hardening/h5e_result_reconciliation_audit`:
  passed.

### Claim Limit

H5E does not create new biological evidence. It prevents over-rewriting by
separating the original CP-Q benchmark result from the additive H5D hardening
result. The manuscript should now say the original registered CP-Q matrix had
zero real-data `context_allowed` routes, while the bounded H5D marker-derived
GSE311609 replay supplied one pre-registered real-data `context_allowed` route.

## H6 - Expanded Synthetic Ladder and Scale Sensitivity

Status: Completed on 2026-05-13.

Purpose: broaden the synthetic positive/null ladder beyond the original linear
k=5 mean-neighbor construction while preserving the original CP-Q3 denominator
and claim boundary.

### Artifacts

- Schema: `data/manifests/contextgate_expanded_ladder_schema.yaml`
- Engine: `src/cellpack/expanded_ladder.py`
- Local builder: `scripts/build_contextgate_expanded_ladder.py`
- Modal smoke: `scripts/pipeline_modal_expanded_ladder.py`
- Artifact directory:
  `manuscript/reviewer_hardening/h6_expanded_synthetic_ladder/`
- Cases: `expanded_ladder_cases.csv`
- Method rows: `expanded_ladder_results.csv`
- Recovery table: `expanded_ladder_recovery.csv`
- Failure-mode table: `expanded_ladder_failure_modes.csv`
- Scale-sensitivity table: `expanded_ladder_scale_sensitivity.csv`
- Claim audit: `expanded_ladder_claim_audit.csv`
- Reviewer report: `expanded_ladder_report.md`
- Summary JSON: `expanded_ladder_summary.json`
- Summary SHA256:
  `0199E0B626CD64E807CD6B2C7F5367DB9332AA2D6CA487FEC179D4D3358F6A07`

### Expanded Ladder Outcome

- Rung count: 11.
- Signal-family count: 8.
- Synthetic cases: 132.
- Method rows: 1,320.
- Required signal families present: true.
- ContextGate positive recovery rate: `1.0`.
- ContextGate negative false-context rate: `0.0`.
- ContextGate confounded trap passed: true.
- Original CP-Q3 denominator modified: false.
- Claim scope: `expanded_synthetic_machinery_check_only`.

The expanded rung families cover:

- k sensitivity: k=3, k=5, k=10.
- Radius sensitivity: 40 um contact and 120 um paracrine-like radii.
- Distance-decay weighting.
- Threshold-gated sender activation.
- Receiver-state-conditioned signal.
- Rare but locally strong niche signal.
- Null no-context control.
- FOV/sample-confounded positive trap.

### Modal Smoke

- Modal smoke URL:
  `https://modal.com/apps/rishyanthreddy101/main/ap-KRe149qcI30qiKTp4h9WFv`
- Result: passed.
- Tier: `smoke`.
- Raw data download mode: none, synthetic only.
- Full raw bundle downloaded: false.
- Modal output path:
  `/cellpack/runs/h6_expanded_ladder/contextgate_h6_expanded_ladder_modal_smoke`

Note: the first Modal invocation failed only because the Windows console used a
non-UTF-8 encoding and could not print the Modal CLI checkmark. Rerunning with
`PYTHONIOENCODING=utf-8` passed.

### Verification

- `python scripts/build_contextgate_expanded_ladder.py --overwrite`: passed.
- `python -m pytest tests/unit/test_contextgate_expanded_ladder.py tests/integration/test_artifact_contracts.py -q`:
  passed with 18 tests.
- Targeted `ruff` on H6 source/scripts/tests: passed.
- `python -m compileall -q src/cellpack/expanded_ladder.py scripts/build_contextgate_expanded_ladder.py scripts/pipeline_modal_expanded_ladder.py`:
  passed.
- YAML parse for `data/manifests/artifact_registry.yaml` and
  `data/manifests/contextgate_expanded_ladder_schema.yaml`: passed.

### Claim Limit

H6 is synthetic machinery evidence only. It supports the statement that the
benchmark now tests scale, nonlinear, prevalence, and confounding failure modes
beyond the original matched linear k=5 ladder. It does not add real biological
context evidence and does not change the original CP-Q3 or CP-Q5 denominators.

## Pre-H7 Hardening Results Verification Packet

Status: Completed on 2026-05-13.

Purpose: provide a human-readable metrics digest before H7 manuscript drafting,
so the H0-H6 results can be reviewed before claim language changes.

Artifact:

- `manuscript/reviewer_hardening/pre_h7_hardening_results_verification.md`
- SHA256:
  `53C5DC42B81D7DA9674B48D7D84A0FA89C0940CCFBCC2FFE5F36B7A010958FB2`

Contents:

- Original CP-Q5 route-count preservation from H5E.
- H5D GSE311609 route decisions and section-level residual utility details.
- H5D wrong-context, replication, and bootstrap evidence.
- H6 expanded synthetic ladder metrics and rung-level scale-sensitivity table.
- H6.5A 10-section NSCLC CD274 expansion metrics and claim boundary.
- H6.5B LIANA+/COMMOT adapter infeasibility and no-confirmation boundary.
- Modal links and validation commands for H0-H6 hardening.
- Safe and unsafe H7 manuscript claim wording.
- Manual verification checklist before drafting.

## H6.5A - Bounded NSCLC CD274 Section-Expansion Probe

Status: Completed on 2026-05-13.

Linear issue: RIS-68.

Purpose: test whether the H5D NSCLC CD274 checkpoint `context_allowed` route
can be strengthened by adding more GSE311609 lung sections while preserving the
same marker-derived evidence contract.

Strict scope:

- Use only lung/NSCLC GSE311609 sections that satisfy the existing H5C/H5D
  marker-derived CD274 checkpoint contract.
- Keep bounded byte-range access; do not download the full 159.9 GB raw bundle.
- Preserve the original CP-Q route counts and treat H6.5A as additive hardening
  evidence.
- Reuse H5D-style expression baseline, true-neighbor, wrong-neighbor,
  residual-utility, q/effect, replication, bootstrap, and route-decision fields.

Stop rules:

- No new marker biology or label assumptions.
- No gate or threshold relaxation.
- No full GSE311609 replay claim.
- Emit blocked/infeasible rows if additional sections cannot be mapped cleanly.

Expected artifacts:

- `manuscript/reviewer_hardening/h6_5a_nsclc_cd274_section_expansion/`
- Attempted-section inventory.
- Section-level residual utility table.
- Route-decision table.
- Replication/bootstrap summary.
- Claim-audit table.

Result:

- Decision: `expanded_sections_support_context_allowed`.
- Selected/attempted lung sections: 10.
- Evaluated lung sections: 10.
- Additional evaluated sections beyond H5D core: 7.
- Effect-gate-passing sections: 10.
- Context-allowed route count: 1.
- Median residual utility delta: 0.018195432125342248.
- Bootstrap CI: [0.008247445348216116, 0.021845731894313134].
- Replication, wrong-context, and spatial gates: passed.
- Bounded bytes downloaded: 172,341,248.
- Full raw bundle downloaded: false.
- Original CP-Q denominator changed: false.

Modal:

- Smoke URL:
  `https://modal.com/apps/rishyanthreddy101/main/ap-OPQqO5JJvFyJdwxt9Z9cKp`.
- Smoke was used as execution-environment validation with 6 sections, 31
  permutations, and 3,000 receiver cells; the local 10-section core artifact is
  the claim artifact.

## H6.5B - Single Mature-Adapter Claim-Eligibility Probe

Status: Completed on 2026-05-13.

Linear issue: RIS-69.

Purpose: run one mature-adapter attempt on the H5D NSCLC CD274 checkpoint task
and decide whether it can contribute a claim-eligible row under the shared
ContextGate adapter contract.

Preferred adapter order:

1. Communication/LR-style adapter if the CD274 checkpoint task maps cleanly.
2. Neighbor-expression adapter if communication mapping is too indirect.
3. Spatial representation adapter only if it can emit contract fields without
   opaque interpretation.

Strict scope:

- Do not run all adapters everywhere.
- Do not claim SOTA confirmation unless the row is contract-valid, traceable,
  and wrong-context controlled.
- Treat infeasibility as a valid outcome.
- Keep the result additive and separate from original CP-Q denominators.

Expected artifacts:

- `manuscript/reviewer_hardening/h6_5b_single_adapter_probe/`
- Adapter evidence table.
- Adapter feasibility/claim-audit table.
- Summary JSON.
- H7-safe language note.

Result:

- Selected adapter: `liana_communication_adapter`.
- Parent H6.5A `context_allowed` count: 1.
- Adapter attempts: 1.
- Claim-eligible adapter rows: 0.
- Mature adapter confirmed positive: false.
- Native output produced: false.
- Contract status: `blocked_missing_native_dependency`.
- Runtime dependency status:
  - `scanpy`: true.
  - `anndata`: true.
  - `liana`: false.
  - `commot`: false.
- Modal required: false; not run because the native dependency path was blocked.
- Original CP-Q denominator changed: false.

Claim conclusion:

H6.5B documents that the preferred LIANA+/COMMOT communication-adapter path was
attempted for the NSCLC CD274 task, but no native mature-adapter output was
produced. H7 must not claim mature-adapter confirmation.

## H6.5C - Hardened Pre-H7 Evidence Freeze

Status: Completed locally on 2026-05-13.

Linear issue: RIS-70.

Purpose: stop evidence expansion and freeze the hardened pre-H7 evidence package
before manuscript drafting.

Snapshot:

- Directory:
  `manuscript/snapshots/hardened-pre-h7-evidence-complete-2026-05-13/`
- Archive:
  `manuscript/snapshots/hardened-pre-h7-evidence-complete-2026-05-13.zip`
- Archive SHA256:
  `EAF5FDD310A86ADF93D2DB2531B1BFBF420A2936E5488810349D9B6AB78B0B18`
- Manifest:
  `manuscript/snapshots/hardened-pre-h7-evidence-complete-2026-05-13/snapshot_manifest.json`
- Manifest SHA256:
  `504994135799142642AEAE69AB453640BD970C2142F8F7B31FA9F03B025976C3`
- Claim-boundary note:
  `manuscript/snapshots/hardened-pre-h7-evidence-complete-2026-05-13/snapshot_claim_boundary.md`
- Claim-boundary SHA256:
  `3EFAFFEC3E3E8E231417DC4C7252112FE0809C8CA856B6B9E340126FFC13A5BD`

Included evidence layers:

- H5D bounded marker replay.
- H6 expanded synthetic ladder.
- H6.5A 10-section NSCLC CD274 expansion.
- H6.5B single mature-adapter infeasibility probe.
- Refreshed pre-H7 verification packet.
- Route-decision tables, claim audits, summaries, registry pointers, code,
  scripts, and focused tests needed to audit those results.

Frozen claim boundary:

The original CP-Q matrix remains 100 decisions with 0 real-data
`context_allowed`. Additive hardening evidence includes a bounded marker-derived
GSE311609 NSCLC CD274 `context_allowed` route, preserved across 10 selected lung
sections. Mature-adapter confirmation is not available because the LIANA+/COMMOT
probe produced no native output.

Unsafe claims frozen out:

- Full GSE311609 validation is complete.
- All 41 sections were replayed.
- H5D/H6.5A rows update the original 100 CP-Q route decisions.
- Mature SOTA adapters confirmed the positive route.
- Synthetic ladder recovery proves real ligand-receptor biology.

## Next Task

Proceed to H7 manuscript artifact rebuild and claim audit after reviewing the
hardened pre-H7 evidence snapshot and refreshed verification packet. H7 must
integrate H5D, H6, H6.5A, and H6.5B without merging additive hardening
denominators into the original CP-Q route counts.
