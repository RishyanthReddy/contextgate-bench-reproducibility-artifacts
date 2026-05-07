# CP-Q8.7A Paper-Wizard Issue Ledger and Claim Boundary

> Status: active Paper-Wizard consistency ledger for ContextGate-Bench.
>
> Source review: `contextgate_bench_elsevier_template_pw_review_standard.pdf`
> and user-provided full-text extraction from the same report.
>
> Purpose: convert the ten highlighted Paper-Wizard issues into concrete
> actions, artifacts, validation checks, and local/Modal rerun decisions before
> final release polish.

---

## 1) Claim Boundary Lock

The manuscript must not imply that ContextGate independently proves the
presence or absence of biological signaling in real data. ContextGate is the
pre-specified evidence contract used by this benchmark. Real-data route labels
are therefore **ContextGate-defined conservative decisions**, unless a later
subtask explicitly adds independent literature or expert anchoring for a
specific dataset-task pair.

The reviewer-safe claim is:

> Under pre-specified ContextGate evidence gates, no current real-data
> dataset-task setting was routed to `context_allowed`. This does not prove
> that tumor neighborhoods lack biological communication. It shows that, in
> the registered public benchmark artifacts, neighbor context did not clear the
> combined requirements for residual utility, FDR control, wrong-context
> separation, held-out replication, leakage clearance, and absence of
> unresolved downgrade.

The manuscript's strongest positive claim should be:

> ContextGate preserves false-context control while retaining positive-control
> sensitivity and auditable abstention behavior. Its advantage over
> expression-only is not that both have zero real-data false-context use under
> the current datasets; it is that ContextGate also detects injected context
> signal and records uncertainty instead of silently refusing context in every
> setting.

This boundary must be preserved in the abstract, Results, Table 3, Discussion,
Conclusion, and Data and Code Availability statement.

---

## 2) Severity and Rerun Definitions

| Severity | Meaning | Required Handling |
|---|---|---|
| Critical | A numerical inconsistency that can invalidate a central claim if unresolved. | Audit immediately; stop manuscript integration if not reconciled. |
| Must-fix | Likely reviewer objection that is fixable before release polish. | Address with manuscript text, tables, figures, or reproducibility artifacts. |
| Submission blocker later | Not required for current local draft, but must be resolved before journal submission. | Track as final release-polish blocker with a concrete access plan. |
| Deferred by user scope | User explicitly asked to ignore for now. | Keep out of CP-Q8.7 unless it affects metric validity. |

| Modal Level | Meaning | CP-Q8.7 Trigger |
|---|---|---|
| Level 1 | No Modal; prose, caption, ledger, or claim-boundary edit. | Use for D1, D3 prose, H1 placeholder wording. |
| Level 2 | Local rebuild from registered artifacts. | Use for FCR, regret, stratification, gate-decomposition tables if artifacts are sufficient. |
| Level 3 | Live Modal smoke only. | Use only if a Modal entrypoint or live command is changed. |
| Level 4 | Bounded Modal refresh. | Use only if gate/threshold/leakage rows are missing and not locally reconstructable. |
| Level 5 | Full CP-Q6 Modal matrix rerun. | Use only if registered CP-Q6 metric semantics are invalid. |

---

## 3) Paper-Wizard Issue Mapping

| ID | Review Issue | Severity | Affected Manuscript Areas | Affected Artifacts | Required Action | Initial Modal Level | Acceptance Criterion |
|---|---|---|---|---|---|---|---|
| D1 | Independence of route ground truth from the evaluated decision framework. | Must-fix | Abstract, Methods 3.5-3.6, Results 4.4-4.5, Discussion, Table 3. | ContextGate decision table, claim-to-evidence audit, optional literature-concordance audit. | Reframe real-data routes as ContextGate-defined decisions; distinguish synthetic and wrong-context labels as externally anchored by construction; add a limited literature-concordance mini-audit if feasible. | Level 1 initially; Level 2 only for concordance table if derived from existing sources. | Manuscript no longer implies independently adjudicated real-data biological nulls; D1 is explicitly acknowledged and bounded. |
| D2 | Leakage-audit gate `ell_i` is not operationally defined. | Must-fix | Methods 3.2, 3.5, 3.6; Results failure taxonomy; Appendix. | ContextGate contract, leakage/downgrade audit, future S25 gate-decomposition table. | Define the leakage audit input, pass/fail criterion, relation to FOV/sample artifact detection, and distinction from downgrade `d_i`; report leakage failures separately where possible. | Level 2 if reconstructable from CP-Q4/Q5/Q7 artifacts; Level 4 if required columns are absent. | A reviewer can identify what makes `ell_i=0`, what makes `ell_i=1`, and how many rows fail leakage versus downgrade. |
| D3 | LR/pathway and graph aggregation method families lack implementation detail. | Must-fix | Methods 3.3-3.4; Appendix method-card pointers. | Method cards; manuscript Methods patch. | Add compact main-text method specifications for LR/pathway and graph-style aggregation: source pair list, feature construction, graph parameters, aggregation/scoring rule, fixed versus learned weights, and skip conditions. | Level 1 unless method semantics change. | The main text plus method cards are sufficient for independent reimplementation. |
| D4 | FCR denominator pools distinct null classes. | Must-fix | Methods metric definitions; Results 4.2-4.3; Table 3; Abstract. | Future S24 stratified FCR table; positive/null ladder; no-harm table. | Stratify false-context rate and specificity by wrong-context controls, panel-limited or unobservable rows, synthetic-null ladder rows, and real unsupported rows when available. | Level 2 if local artifacts contain null-class labels; Level 4 if labels must be refreshed. | Pooled FCR is not the only reported safety result; denominator composition is transparent. |
| D5 | Threshold sensitivity for the primary routing outcome is underspecified. | Must-fix | Methods 3.6; Results 4.6; Discussion. | CP-Q7 threshold stress outputs; future S26 operating-point table. | Report threshold ranges and route counts under registered conservative, moderate, and permissive operating points; state whether zero real `context_allowed` persists. | Level 2 if CP-Q7 artifacts suffice; Level 4 if exact operating points are missing. | The zero real context-allowed result is shown as stable or explicitly labeled threshold-dependent. |
| E1 | Always-context FCR of 0.4783 contradicts Equation 3. | Critical | Abstract, Results 4.2-4.3, Table 3, metric definitions, figure captions. | CP-Q6 metrics; no-harm table; future metric consistency audit. | Recompute Equation 3 null-denominator FCR; either replace always-context FCR with 1.000 or relabel 0.4783 as a separate all-row/global context-exposure metric. | Level 2 first; Level 5 only if CP-Q6 artifacts themselves are semantically invalid. | Every FCR value uses one documented denominator; any all-row metric has a distinct name and formula. |
| E2 | Zero context-allowed decisions are not decomposed by failed gate. | Must-fix | Results 4.4, failure taxonomy, Appendix. | ContextGate decision table; failure taxonomy; future S25 gate-failure table. | Add all-failed-gates and first-failing-gate summaries for 23 expression-only plus 40 abstain real non-positive-control decisions; map failure classes to gates. | Level 2 if decisions include gate inputs; Level 4 if bounded route refresh is required. | Readers can distinguish residual failure, FDR/power failure, wrong-context failure, replication failure, leakage failure, and downgrade failure. |
| E3 | Oracle-regret values differ across Figure 2, Figure 3, and text. | Critical | Results 4.2, Figure 2 caption, Figure 3 caption, text values. | Figure-generation inputs, CP-Q6 method metrics, future metric consistency audit. | Audit exact row subsets and aggregation for metric-profile and oracle-regret figures; regenerate or relabel captions so values are reproducible. | Level 2 first; Level 5 only if registered method metrics cannot be reconciled. | Figure 2, Figure 3, and text either match or explicitly state different subsets/statistics. |
| E4 | ContextGate FCR is not distinct from expression-only on real data. | Must-fix | Abstract, Results 4.2/4.5, Table 3, Conclusion. | Future S24 expression-only comparator table; positive/null ladder. | Report expression-only FCR alongside ContextGate and always-context; reframe the added value as zero FCR plus positive-control sensitivity and abstention. | Level 2. | Manuscript no longer treats zero FCR alone as uniquely ContextGate-specific. |
| H1 | Benchmark artifacts are described as intended for release without an access path. | Submission blocker later | Data and Code Availability, Appendix artifact map, release checklist. | Repository, artifact registry, command ledger, final release archive. | Prepare reviewer-access wording now; final public GitHub/Zenodo/DOI strings remain release-polish placeholders until the package is ready. | Level 1. | Current draft states what will be accessible and which final fields are placeholders; final submission cannot keep "intended for release" without a URL/DOI/access link. |

---

## 4) User-Deferred Formatting and Placeholder Items

The user explicitly instructed CP-Q8.7 to ignore the following for now unless
they affect scientific consistency:

| Item | Status | Reason |
|---|---|---|
| Reference formatting | Deferred by user scope | Final Elsevier/reference cleanup belongs to release polish. |
| Whole Elsevier formatting | Deferred by user scope | Layout polish should follow metric and claim hardening. |
| Author names and affiliations | Deferred by user scope | Final author metadata will be added later. |
| Final GitHub link, Zenodo DOI, or repository access string | Deferred by user scope, but tracked as H1 final blocker | Scientific draft can use placeholders, but journal submission needs active access. |
| Two placeholder pictures, graphical abstract, and architecture diagram | Deferred by user scope | Final draw.io artwork happens after metric/caption consistency is stable. |

---

## 5) Claim-Language Change Targets

| Current Risky Framing | CP-Q8.7 Target Framing |
|---|---|
| "Across real tumor datasets, no biological context-benefit claim survived." | "Under the pre-specified ContextGate evidence contract, no current real-data setting was routed to `context_allowed`." |
| "ContextGate reduces false context use." | "ContextGate preserves zero false-context use while retaining positive-control sensitivity and abstention behavior; expression-only also has zero context use but cannot detect positive-control context." |
| "Always-context FCR = 0.4783." | Either "always-context null-denominator FCR = 1.000" or "always-context global context-exposure rate = 0.4783," depending on CP-Q8.7B audit. |
| "Spatial-statistics heuristic has zero regret." | State the exact subset and aggregation where this is true, or update the value after CP-Q8.7B. |
| "The failure taxonomy explains the zero context-allowed result." | Add gate-by-gate failure decomposition so the taxonomy is diagnostic rather than a substitute for gate evidence. |
| "Data and code are intended for release." | "All result tables, figure scripts, schemas, command entrypoints, and artifacts will be provided at final release; active reviewer/public access link to be inserted before submission." |

---

## 6) CP-Q8.7 Work Mapping

| CP-Q8.7 Card | Issues Covered | Main Work |
|---|---|---|
| CP-Q8.7A issue ledger | D1-D5, E1-E4, H1 | This file; plan/TODO synchronization; next pointer to CP-Q8.7B. |
| CP-Q8.7B metric consistency audit | E1, E3 | Recompute or relabel FCR and oracle-regret values; decide Modal level. |
| CP-Q8.7C stratified FCR/comparators | D4, E4 | Build S24 tables and update comparison language. |
| CP-Q8.7D gate decomposition/leakage | D2, E2 | Build S25 tables and define `ell_i` operationally. |
| CP-Q8.7E threshold operating points | D5 | Build S26 tables and state robustness range. |
| CP-Q8.7F method-spec patch | D3 | Patch Methods text for LR/pathway and graph families. |
| CP-Q8.7G claim rewrite/concordance | D1, E4, H1 | Rewrite abstract/results/discussion/data-code language and add mini-audit if feasible. |
| CP-Q8.7H figures/PDF QA | E1, E3, D4, E4 | Regenerate figures/tables and inspect compiled PDF. |
| CP-Q8.7I final ledger | D1-D5, E1-E4, H1 | Close issue status, tests, visual QA, and Modal decision. |

---

## 7) Immediate Next Actions

1. Start CP-Q8.7B with a metric consistency audit before changing prose.
2. Treat E1 and E3 as stop-rule items: if FCR or regret cannot be reconciled
   from registered artifacts, do not proceed to manuscript integration.
3. Do not run Modal blindly. Begin with local recomputation from registered
   CP-Q2 through CP-Q7 artifacts.
4. Keep final artwork, references, author names, and final repository access
   strings out of this pass unless they affect scientific traceability.

---

## 8) CP-Q8.7A Completion Criteria

CP-Q8.7A is complete when:

- this ledger exists;
- `CellPack_Research_Grade_Master_Plan.md` marks CP-Q8.7A as done and points
  to CP-Q8.7B;
- `CellPack_TODO.md` records the session row and next task;
- markdown fence balance and `git diff --check` pass;
- no Modal trigger is active for CP-Q8.7A.

