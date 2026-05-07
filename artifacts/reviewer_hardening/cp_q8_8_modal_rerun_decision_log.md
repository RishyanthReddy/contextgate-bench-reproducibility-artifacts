# CP-Q8.8 Modal Rerun Decision Log

Date: 2026-05-05

Purpose: record the local-versus-Modal rerun decision for each CP-Q8.8 card so
reviewer-hardening edits do not accidentally trigger unnecessary cloud reruns,
while still preserving clear Level 4/5 escalation triggers.

## Rerun Levels

| Level | Meaning | Modal required? |
|---|---|---|
| Level 1 | Prose, caption, ledger, or claim-scope wording only. | No |
| Level 2 | Tables or figures regenerated from already registered artifacts. | No |
| Level 3 | New local audit artifacts/scripts derived from existing registered files. | No |
| Level 4 | Missing evidence requires a bounded cloud refresh. | Yes, bounded |
| Level 5 | Route logic, thresholds, benchmark matrix semantics, or cloud entrypoints change. | Yes, full/targeted matrix |

## Decisions

| Card | Decision | Rationale |
|---|---|---|
| CP-Q8.8A | Level 1, no Modal | Ledger and scope-lock task only; no manuscript claims, route logic, artifacts, metrics, or cloud entrypoints changed. |
| CP-Q8.8B | Level 1, no Modal | Title/abstract/Introduction/Discussion/Limitations/Conclusion wording now scopes the benchmark to registered targeted-panel imaging-based CosMx/Xenium artifacts and clarifies author-defined evidence-gate provenance. No metrics, route counts, thresholds, scripts, artifact tables, or Modal entrypoints changed. |
| CP-Q8.8C | Level 3, no Modal | Added a local S27 metric-definition audit table and manuscript definitions for task-layer normalization, utility/regret, FDR scope, confidence, gate-pass rate, aggregate thresholds, and registry semantics. The work derives from existing registered artifacts and source code; it does not change route logic, thresholds, cloud entrypoints, or benchmark matrix semantics. |
| CP-Q8.8D | Level 3, no Modal | Expanded local S16/S19 positive-control audit tables and manuscript wording from existing CP-Q3 ladder artifacts. No route logic, ladder generation code, thresholds, benchmark semantics, or cloud entrypoints changed; only derived table columns, tests, and claim-boundary prose were updated. |
| CP-Q8.8E | Level 3, no Modal | Added S28 dataset/split/scope audit and manuscript wording from existing manifest, CP-Q6 job status/manifest, CP-Q5 decisions, and source graph constructors. The audit documents k=5 sample/slide-bounded graph policy, replication tiers, job-count rationale, route counts, single-donor/FOV-only limits, and GSE311609 freeze rationale without changing route logic, benchmark semantics, cloud entrypoints, or metric values. |
| CP-Q8.8F | Level 3, no Modal | Added S29 method-scope/fairness audit and manuscript wording from existing CP-Q2 method metrics/predictions, CP-R1 context-utility scores, manifest gene counts, source route rules, and the SOTA feasibility ledger. The audit documents spatial-statistics safety metrics, CellPack input ceiling, fixed comparator tuning, method-label mappings, and named future-adapter tools without changing route logic, thresholds, benchmark semantics, cloud entrypoints, or metric values. |
| CP-Q8.8G | Level 3, no Modal | Added S30A/S30B/S31/S32 aggregation, disaggregation, failure-denominator, and panel-depth audits from existing CP-Q5 decisions, CP-Q6 job/metric artifacts, CP-Q4 failure taxonomy rows, CP-R1 context-utility scores, and manifest metadata. The audit clarifies decision units, per-dataset/per-task denominators, failure taxonomy row units, and panel-depth strata without changing route logic, thresholds, benchmark semantics, cloud entrypoints, or metric values. |
| CP-Q8.8H | Level 3, no Modal | Added S33A/S33B/S33C threshold-grid and stress-accounting audits from existing CP-Q7 stress tables, CP-Q5 route summaries, CP-Q6 execution summaries, and CP-Q3 ladder summaries. The audit reconciles seven row-generating stress families, the separate six-claim survival audit, and the 5+1 downgrade accounting without changing route logic, thresholds, benchmark semantics, cloud entrypoints, or metric values. |
| CP-Q8.8I | Level 2, no Modal | Regenerated publication figures from existing registered artifacts and patched only figure rendering/caption scope: Figure 2 display conventions, Figure 3 ordering, Figure 4 rung labels, Figure 7 route labels, and Figure 8 segment labels. No route logic, thresholds, metric definitions, benchmark semantics, cloud entrypoints, or Modal commands changed. |
| CP-Q8.8J | Level 1, no Modal | Added release-readiness and Data/Code Availability prose plus ledger updates only. The reviewer-access archive checklist and live-link placeholders do not change route logic, thresholds, metric definitions, artifacts, figures, tables, benchmark semantics, cloud entrypoints, or Modal commands. |
| CP-Q8.8K | Level 2, no Modal | Regenerated manuscript tables and publication figures from existing registered artifacts, compiled the manuscript, rendered all 47 PDF pages, created page/figure contact sheets, performed visual QA, and ran text/cross-reference audits. The only prose change tightened a stale abstract scope phrase; no route logic, thresholds, metric definitions, benchmark semantics, cloud entrypoints, or Modal commands changed. |
| CP-Q8.8L | Level 2 plus live Modal smoke; no bounded/full matrix rerun | Created the final validation ledger, reran local builders, compile/render/visual QA, full pytest, ruff, compileall, diff hygiene, and the opt-in CP-Q5 live Modal smoke. The live smoke passed as an entrypoint health check, but no Level 4 missing-evidence or Level 5 semantics trigger fired. |

## Current Stop Rule

No CP-Q8.8A--CP-Q8.8L change creates a Level 4 or Level 5 trigger. The
explicit live Modal smoke test passed, and no bounded or full Modal matrix
rerun is required for the expanded reviewer-hardening sweep.
