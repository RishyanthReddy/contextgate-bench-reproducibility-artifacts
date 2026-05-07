# CP-Q8.6A Reviewer Gap Ledger and Claim Boundary

> Status: active reviewer-hardening ledger for ContextGate-Bench.
>
> Purpose: map every external-review criticism to a concrete action,
> artifact, scope boundary, validation check, or future-work statement before
> final release polish.

---

## 1) Claim Boundary Lock

The manuscript should not claim that spatial context is never useful, that all
large spatial foundation models would fail, or that current negative real-data
results disprove biological communication.

The reviewer-safe claim is:

> ContextGate-Bench evaluates whether a specific dataset, task, split, method,
> and control setting contains enough reproducible residual evidence to justify
> using spatial neighbor context. In the registered public benchmark artifacts
> tested here, strict context-allowed gates usually downgrade real-data context
> claims, while positive controls verify that the benchmark can detect injected
> spatial signal. The framework is model-agnostic and can admit larger future
> context models when they satisfy the same evidence contract.

The manuscript must preserve this boundary in the abstract, contribution list,
Results, Discussion, Limitations, and Data/Code statements.

---

## 2) Gap Severity Definitions

| Severity | Meaning | Required Handling |
|---|---|---|
| Must-fix | Likely to be raised by a computational-biology reviewer and fixable before submission. | Address in manuscript and/or supplement before release polish. |
| Scope-controlled | Legitimate criticism but too broad to fully solve without changing the paper. | Add explicit boundary, feasibility ledger, or limited replay decision. |
| Optional | Improves polish but does not block the benchmark/resource claim. | Add if low-cost or defer with a reason. |
| Rejected | Not appropriate, unverifiable, or outside the manuscript scope. | Record reason and do not force into text. |

---

## 3) Review Criticism Mapping

| ID | Review Criticism | Severity | Affected Sections | Required Action | Artifact / Output | Modal Needed? | Acceptance Criterion |
|---|---|---|---|---|---|---|---|
| G01 | Graph-style aggregation is insufficiently specified for replication. | Must-fix | Methods 3.4, Appendix | Add method card with graph construction, node features, aggregation rule, hyperparameters, splits, normalization, and outputs. | `method_cards/graph_style_context_aggregation.md` | No unless implementation changes. | A reviewer can reimplement the baseline without reading source code. |
| G02 | Ligand-receptor/pathway heuristics are insufficiently specified. | Must-fix | Methods 3.3-3.4, Appendix | Define sender/receiver features, LR pair filtering, pathway target construction, score normalization, control comparison, and skip rules. | `method_cards/lr_pathway_heuristics.md` | No unless table rows are regenerated. | Heuristic scores can be recomputed from expression, graph, and LR/pathway inputs. |
| G03 | Tiny packed-context transformer is intentionally small and weakens conclusions about high-capacity models. | Scope-controlled | Methods 3.4, Results 4.3, Discussion, Limitations | State that the tiny model is a bounded capacity/smoke baseline, not a SOTA model; use positive controls as capacity sanity checks; add SOTA feasibility ledger. | `method_cards/tiny_packed_context_transformer.md`; `sota_feasibility_ledger.md` | Optional only after feasibility gate. | Manuscript no longer implies all strong models would fail. |
| G04 | No head-to-head comparison with recent high-capacity spatial context models. | Scope-controlled | Related Work, Discussion, Limitations | Add literature positioning and optional feasibility decision for one bounded replay. | `contextgate_related_work_expansion.csv`; `sota_feasibility_ledger.md` | Maybe. | Each named SOTA family is either cited, scoped, rejected, or selected for replay. |
| G05 | Statistical gates lack justification and calibration. | Must-fix | Methods 3.6, Results 4.6, Appendix | Add threshold-rationale table using CP-Q7 stress outputs and positive/null control ladder. | threshold calibration supplementary table | Only if CP-Q7 rows are insufficient. | Threshold choices are tied to false-context avoidance, no-harm, and positive/null sensitivity. |
| G06 | No formal power or minimum-detectable-effect analysis. | Must-fix with careful wording | Methods 3.6, Results 4.3/4.6, Limitations | Add a detectability audit from injected signal strengths and observed real-data effects; call it a benchmark calibration, not a full prospective power analysis. | minimum-detectable-effect supplementary table | Maybe, only if ladder needs more rows. | Real-data effect sizes are contextualized against detectable injected effects. |
| G07 | `c_{im}` context-use/favors-context indicator is not fully formalized. | Must-fix | Methods 3.6, Appendix | Define `c_{im}`, route precedence, tie-breaking, threshold dependence, skipped jobs, and positive-control-only handling. | `contextgate_decision_contract.md` | No unless router code changes. | Every route can be reconstructed from metric and decision tables. |
| G08 | Results are too top-line and need per-dataset/per-task utility, FCR, sensitivity, specificity, and regret. | Must-fix | Results 4.1-4.6, Supplement | Generate expanded quantitative tables from CP-Q2/Q3/Q5/Q6/Q7 artifacts. | `supp_table_s10_*` onward | Maybe if missing metrics require refresh. | Main text cites richer summaries and supplement exposes row-level aggregates. |
| G09 | Leakage audit mechanics `\ell_i` are not documented with examples or thresholds. | Must-fix | Methods 3.2/3.6, Appendix | Add leakage examples for random-cell split, same-FOV leakage, synthetic-control leakage, and held-out outcome leakage. | leakage/downgrade examples table | No unless table generation changes. | `\ell_i` is defined by concrete conditions, not prose intuition. |
| G10 | Downgrade reasons `d_i` are not documented with examples. | Must-fix | Methods 3.6, Results 4.4-4.6, Appendix | Add reason-code examples for panel observability, wrong-context erasure, non-replication, skip/infeasible, positive-control-only. | leakage/downgrade examples table | No unless table generation changes. | Each major downgrade class has an example row and threshold/criterion. |
| G11 | Residualization for LR/pathway tasks may be misspecified. | Must-fix | Methods 3.3, Discussion, Limitations | Document expression-only baseline capacity, feature selection, residual target definition, fairness rationale, collider/misspecification risks. | `residualization_audit.md` | No unless residual metrics are changed. | Manuscript admits residualization limits while explaining why it is the fair context test. |
| G12 | Supplementary artifacts are referenced but not visible. | Must-fix | Results, Data/Code, Supplement | Add table inventory and explicit pointers for rejected dataset ledger, failure taxonomy, reason-code ablations, robustness outcomes, and claim audit. | updated supplement/table manifest references | No unless files are missing. | Every "supplementary" claim maps to an existing output path. |
| G13 | Related work omits SpaFormer-like, HEIST-like, dynamic communication, and benchmark resources. | Must-fix | Related Work, Discussion, Limitations | Expand related work with verified peer-reviewed/core and preprint/future-work separation. | `contextgate_related_work_expansion.csv` | No. | The manuscript positions ContextGate-Bench against recent context-heavy methods and benchmarks. |
| G14 | Some named methods may be unverifiable or only adjacent to this task. | Must-fix guardrail | Related Work | Verify DSCon, MERGE, STAGED, CMRCNet, and similar names before citing; decline if no stable source is found. | declined-citation rows in related-work ledger | No. | No phantom or weakly verified method is forced into the bibliography. |
| G15 | The benchmark may look too punitive because all strict gates can reject noisy biology. | Must-fix | Results 4.6, Discussion | Use threshold sensitivity and no-harm economics to explain conservative routing; distinguish rejection from absence of biology. | threshold calibration table; limitations text | Maybe only if CP-Q7 insufficient. | Strictness is framed as false-context control, not proof that biology is absent. |
| G16 | Computational cost of the benchmark may look high. | Optional but useful | Discussion, Data/Code | Keep compute-cost economics and add pointer to mini/core/full benchmark tiers. | Modal command ledger / runbook later | No for CP-Q8.6A. | Readers understand cheap smoke, core, and full benchmark modes. |

---

## 4) CP-Q8.6 Work Mapping

| CP-Q8.6 Card | Gaps Covered | Completion Signal |
|---|---|---|
| CP-Q8.6A gap ledger | G01-G16 | This file exists and every gap has severity, action, artifact, Modal decision, and acceptance criterion. |
| CP-Q8.6B method cards | G01-G03, G11 | All method families have method cards. |
| CP-Q8.6C route contract | G07, G09, G10, G15 | `c_{im}`, `\ell_i`, `d_i`, route precedence, and skip handling are formal. |
| CP-Q8.6D expanded result tables | G08, G12 | Supplement exposes per-dataset/per-task/method/control metrics. |
| CP-Q8.6E calibration/MDE audit | G05, G06, G15 | Threshold and detectability tables are generated or refreshed. |
| CP-Q8.6F leakage/residualization audit | G09-G11 | Examples and residualization caveats are visible. |
| CP-Q8.6G related work | G13-G14 | Verified literature ledger is integrated into manuscript citations. |
| CP-Q8.6H SOTA feasibility | G03-G04 | One of `run_limited_replay`, `adapter_only`, `cite_scope_only`, or `reject_for_release` is recorded. |
| CP-Q8.6I Modal rerun ladder | G04-G06, G08 | Re-execution level is chosen and justified. |
| CP-Q8.6J/K integration and validation | G01-G16 | Revised PDF and validation ledger pass. |

---

## 5) Immediate Next Actions

1. Start CP-Q8.6B and create method cards for every current method family.
2. Keep CP-Q8.6H as a decision gate, not a promise to run every modern model.
3. Do not rerun CP-Q6 or CP-Q7 until a missing metric or changed benchmark
   semantic requires it.
4. Keep the manuscript claim conservative: strict gate failures are evidence
   about benchmark support, not proof that the underlying biology is absent.

---

## 6) CP-Q8.6A Status

CP-Q8.6A is complete when this ledger is synchronized into:

- `CellPack_Research_Grade_Master_Plan.md`;
- `CellPack_TODO.md`;
- the validation ledger;
- and the next-task pointer moves to CP-Q8.6B.

