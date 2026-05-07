# CP-Q8.6C ContextGate Decision Contract

> Formal reviewer-facing contract for reconstructing ContextGate decisions from
> benchmark artifacts.
>
> Status: CP-Q8.6C.

---

## 1) Purpose

This contract defines how ContextGate turns registered benchmark evidence into
one of four route labels:

- `expression_only`
- `context_allowed`
- `abstain_uncertain`
- `positive_control_only`

It also defines the context-use indicator `c_{im}`, route precedence,
tie-breaking, skipped-job handling, leakage flags, and downgrade reasons.

This document is intended to let a reviewer reconstruct every ContextGate
decision from:

- `contextgate_decisions.parquet`
- `contextgate_rule_table.parquet`
- `failure_taxonomy.parquet`
- `method_predictions.parquet`
- `positive_control_ladder.parquet`
- `job_status.parquet`
- `benchmark_metric_matrix.parquet`

Primary implementation:

- `src/cellpack/contextgate.py`
- `src/cellpack/failure_taxonomy.py`
- `src/cellpack/method_comparison.py`
- `src/cellpack/benchmark_matrix.py`

---

## 2) Symbols

| Symbol | Meaning |
|---|---|
| `i` | Benchmark instance, row, task-target, or synthetic-control case. |
| `m` | Method family or method ID. |
| `r_{im}` | Route predicted or selected for instance `i` by method `m`. |
| `r_i^*` | Oracle/evidence route assigned by the registered benchmark evidence. |
| `u(r_i^*, r_{im})` | Utility lookup comparing predicted route with oracle route. |
| `R_{im}` | Oracle regret, `u(r_i^*, r_i^*) - u(r_i^*, r_{im})`. |
| `c_{im}^{real}` | Real-context-use indicator. |
| `c_{im}^{synthetic}` | Synthetic-context-use indicator for positive-control-only cases. |
| `\ell_i` | Leakage-audit pass indicator (`1` = passed, `0` = failed). |
| `d_i` | Downgrade reason code or failure class. |
| `q_i` | FDR-adjusted p-value or q-value proxy when available. |

---

## 3) Route Label Domain

The allowed ContextGate route labels are:

| Route | Meaning | Biological Claim Allowed? |
|---|---|---|
| `expression_only` | Use center/expression-only evidence; real context is not justified. | No real context-benefit claim. |
| `context_allowed` | Real spatial context passed the strict replicated evidence gate. | Yes, but only for the registered row/target. |
| `abstain_uncertain` | Evidence is missing, underpowered, confounded, unreplicated, or otherwise insufficient. | No positive claim. |
| `positive_control_only` | Synthetic/injected context signal was detected. | Mechanics-only claim; no real biology claim. |

`skip` is not a ContextGate route label. It is a benchmark job status used when
a job cannot be evaluated because required data, labels, controls, metadata, or
upstream evidence are unavailable. Skipped jobs can appear in CP-Q6 job-status
and skip-reason tables, but they are not counted as `context_allowed`.

---

## 4) Context-Use Indicator `c_{im}`

For method-comparison rows, define the real-context indicator as:

`c_{im}^{real} = 1[r_{im} in {context_allowed, full_context, compressed_context}]`

and:

`c_{im}^{real} = 0` otherwise.

For ContextGate decision rows:

- `c_{im}^{real} = 1` only if `route_label = context_allowed`;
- `c_{im}^{real} = 0` for `expression_only`, `abstain_uncertain`, and
  `positive_control_only`.

For synthetic positive controls, define:

`c_{im}^{synthetic} = 1[route_label = positive_control_only]`

This separates a mechanics check from a real biological context claim.

The false-context indicator is:

`f_{im} = 1[c_{im}^{real} = 1 and r_i^* = expression_only]`

The no-harm indicator is:

`h_{im} = 1 - f_{im}`

Aggregate false-context rate for method `m` is:

`FCR_m = mean_i(f_{im})`

ContextGate passes the false-context safety gate only when:

`FCR_ContextGate <= 0.05`

and ContextGate does not have a higher false-context rate than the selected
context-using comparator.

---

## 5) Real-Data Route Precedence

For registered real-data context-utility rows, ContextGate evaluates route
precedence in this order.

### Priority 1: Strict Real Context

Return `context_allowed` only if all conditions hold:

- `evidence_class = strict_positive`
- `residual_signal_gate_passed = true`
- `strict_conditioned_gate_passed = true`
- `heldout_gate_passed = true`
- `fdr_controlled = true`

The reason code is `strict_replicated_context_signal`.

If any of these gates is false or missing, the row cannot be
`context_allowed`.

### Priority 2: Positive-Control-Only Evidence

Return `positive_control_only` if:

- `evidence_class = positive_control_only`; or
- `positive_control_gate_passed = true`

This route is mechanics-only. It does not allow a real-data context-benefit
claim.

### Priority 3: Negative or Expression-Absorbed Evidence

Return `expression_only` if:

- `evidence_class = negative_context`; or
- upstream `route_recommendation = expression_only`

The reason code is selected from the failure taxonomy. Typical reasons include:

- `negative_context_evidence`
- `expression_absorbs_neighbor_signal`
- `panel_or_target_coverage_gap`

### Priority 4: Abstention

Return `abstain_uncertain` for all remaining real-data cases, including:

- borderline preflight evidence;
- localized but unreplicated evidence;
- underpowered evidence;
- missing panel or target evidence;
- FOV/sample artifacts;
- access or schema blockers;
- incomplete upstream artifacts.

---

## 6) Synthetic-Control Route Precedence

For CP-Q3 positive/null-control rows, the router first restricts to
`method_id = contextgate_transparent_router`, then applies this precedence.

### Priority 1: Detected Injected Signal

Return `positive_control_only` if:

- `expected_context_positive = true`
- `gate_passed = true`
- `observed_route = positive_control_only`

This verifies sensitivity to injected true-neighbor signal.

### Priority 2: Missing-Panel Dropout

Return `abstain_uncertain` if:

- `missing_panel_dropout = true`

This checks that the router does not invent a context claim when the target is
not observable.

### Priority 3: FOV/Sample Confounding

Return `abstain_uncertain` if:

- `fov_or_sample_confounded = true`

This checks that confounded synthetic structure is not treated as real spatial
neighbor evidence.

### Priority 4: Null Rejection

Return `expression_only` if:

- `expected_context_positive = false`
- `observed_route = expression_only`

### Priority 5: Synthetic Abstention Fallback

Return `abstain_uncertain` for all other synthetic rows.

---

## 7) Access and Schema Blockers

Rows with failure class `access_or_schema_blocker` route to
`abstain_uncertain`.

Required gate booleans are set to false except `leakage_audit_passed`, which is
true when the row is explicitly represented as an access/schema blocker rather
than silently included as evidence.

These rows support rejected-dataset ledgers, not biological claims.

---

## 8) Tie-Breaking

Tie-breaking is deterministic and conservative.

1. `context_allowed` has highest priority but requires every strict real-data
   gate to pass.
2. `positive_control_only` outranks `expression_only` only for synthetic or
   explicitly positive-control evidence.
3. `expression_only` outranks `abstain_uncertain` when evidence is explicitly
   negative or the upstream route recommendation is expression-only.
4. `abstain_uncertain` is the default for missing, conflicting, underpowered,
   unreplicated, confounded, or incomplete evidence.
5. Duplicate decision rows with the same `source_table`, `benchmark_row_id`,
   `dataset_id`, and `task_id` keep the first generated row. Generation order is
   real-data context rows, synthetic-control rows, then access/schema blocker
   rows. The output is sorted only after duplicates are removed.

This means a row cannot become `context_allowed` through tie-breaking. It must
pass the strict gate.

---

## 9) Leakage-Audit Gate `\ell_i`

The leakage-audit gate is defined as a leakage-audit pass indicator:

`\ell_i = 1` when a row passes the registered evidence-isolation audit, and
`\ell_i = 0` when a direct leakage or evidence-isolation failure is detected.

In current artifacts, this is the `leakage_audit_passed` column in
`contextgate_decisions.csv`. It is deliberately narrower than the whole failure
taxonomy. FOV/sample artifacts, unreplicated held-out evidence, panel failures,
and synthetic confounds are represented through `wrong_context_gate_passed`,
`heldout_replication_passed`, `failure_class`, and `reason_code`, then surfaced
as downgrade gate failures. This prevents the leakage gate from becoming an
opaque catch-all.

Operationally:

| Condition | `\ell_i` | Other Gate Effect |
|---|---:|---|
| Direct evidence-isolation or train/test leakage failure | 0 | Blocks `context_allowed`. |
| FOV/sample artifact failure class present | 1 in current artifacts | Exposed by wrong-context, held-out, and downgrade gates. |
| Wrong-context specificity below threshold in synthetic controls | 1 in current artifacts | Exposed by wrong-context and downgrade gates. |
| Held-out replication missing for real-data signal | 1 in current artifacts | Exposed by held-out replication and downgrade gates. |
| Access/schema blocker row recorded explicitly | 1 in current artifacts | Evidence remains unusable through residual, FDR, held-out, and downgrade gates. |
| Standard clean row with passed leakage audit | 1 | Other gates decide route. |

For run-context decisions, `wrong_context_gate_passed = false` when access or
artifact evidence prevents a clean wrong-context separation. For synthetic
decisions, wrong-context and null specificity are represented by the synthetic
ladder metrics rather than by `leakage_audit_passed`.

---

## 10) Downgrade Reason `d_i`

The downgrade reason `d_i` is derived from `failure_class` and `reason_code`.

Failure class priority in the current reason mapper is:

1. `access_or_schema_blocker`
2. `panel_lacks_downstream_genes`
3. `fov_or_sample_artifact`
4. `labels_not_replicated`
5. `insufficient_power`
6. `expression_absorbs_signal`
7. explicit upstream `route_recommendation = expression_only`
8. default uncertain abstention

The failure taxonomy also includes `lr_without_downstream_response`, which is
recorded in the taxonomy and downgrade audit. When this class appears without a
more specific route reason, it supports a ligand-receptor/pathway claim
downgrade rather than a context-allowed route.

Downgrade mapping:

| Failure Class | Claim Downgrade |
|---|---|
| `panel_lacks_downstream_genes` | `downgrade_pathway_or_lr_panel_claim` |
| `labels_not_replicated` | `no_heldout_generalization_claim` |
| `expression_absorbs_signal` | `prefer_expression_only_baseline` |
| `fov_or_sample_artifact` | `no_spatial_neighbor_claim_without_controls` |
| `lr_without_downstream_response` | `no_downstream_lr_response_claim` |
| `insufficient_power` | `abstain_until_more_power_or_replicates` |
| `access_or_schema_blocker` | `rejected_dataset_ledger_only` |

---

## 11) Threshold Dependence

Current threshold parameters:

| Threshold | Value | Used For |
|---|---:|---|
| `false_positive_context_threshold` | 0.05 | Maximum acceptable ContextGate false-context rate. |
| `positive_control_route_recovery_threshold` | 0.95 | Minimum route recovery for injected positive controls in no-harm analysis. |
| `positive_control_sensitivity_threshold` | 0.65 | Synthetic signal sensitivity gate. |
| `synthetic_specificity_threshold` | 0.80 | Null/confounded specificity gate. |

Method-comparison helper thresholds:

| Threshold | Value | Used For |
|---|---:|---|
| `expression_score_threshold` | 0.01 | Spatial-statistics and LR/pathway low-score route. |
| `full_context_score_threshold` | 0.65 | Spatial-statistics and packed-context high-score route. |
| `lr_pair_threshold` | 4 | Minimum measured LR pair coverage. |
| `module_target_threshold` | 4 | Minimum measured pathway/module target coverage. |

CP-Q8.6E calibrates these thresholds. Until then, CP-Q8.6C records the current
implementation contract.

---

## 12) Reconstruction Pseudocode

For real-data rows:

```text
if strict_positive and residual and conditioned and heldout and fdr:
    route = context_allowed
elif evidence_class == positive_control_only or positive_control_gate_passed:
    route = positive_control_only
elif evidence_class == negative_context or route_recommendation == expression_only:
    route = expression_only
else:
    route = abstain_uncertain
```

For synthetic-control rows:

```text
if expected_context_positive and gate_passed and observed_route == positive_control_only:
    route = positive_control_only
elif missing_panel_dropout:
    route = abstain_uncertain
elif fov_or_sample_confounded:
    route = abstain_uncertain
elif not expected_context_positive and observed_route == expression_only:
    route = expression_only
else:
    route = abstain_uncertain
```

For access/schema blockers:

```text
route = abstain_uncertain
reason_code = access_or_schema_blocker
```

---

## 13) Required Decision Columns

Every ContextGate decision table must include:

- `benchmark_row_id`
- `dataset_id`
- `task_id`
- `target_id`
- `route_label`
- `reason_code`
- `residual_gate_passed`
- `wrong_context_gate_passed`
- `fdr_effect_gate_passed`
- `heldout_replication_passed`
- `leakage_audit_passed`
- `evidence_pointer`
- `artifact_registry_ids`

The implementation also writes:

- `contextgate_decision_id`
- `source_table`
- `reason_detail`
- `failure_class`
- `failure_taxonomy_ids`
- `claim_level`
- `split_id`
- `seed`
- `control_level`
- `confidence`
- `uses_real_context`
- `uses_synthetic_context`

---

## 14) Review-Safe Interpretation

ContextGate decisions should be interpreted as evidence routing, not biological
truth.

- `context_allowed`: real spatial context is justified for that registered
  row under the current evidence contract.
- `positive_control_only`: the benchmark detected synthetic context signal, so
  the machinery is sensitive, but no real biological claim is allowed.
- `expression_only`: the expression-only baseline is preferred under the
  current evidence row.
- `abstain_uncertain`: evidence is insufficient, confounded, inaccessible,
  underpowered, or not replicated.
- skipped jobs: benchmark scope or feasibility limitation, not a route.

This contract prevents strict negative or abstention outcomes from being
misread as proof that biology lacks spatial communication.
