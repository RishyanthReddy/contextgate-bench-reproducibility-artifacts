# CP-Q8.7 Local/Cloud Rerun Decision Log

Task family: CP-Q8.7 Paper-Wizard consistency hardening

Decision rule:

1. Prose, caption, or claim-boundary edits use Level 1 local validation only.
2. Derived denominator, gate, threshold, or comparator tables use Level 2 local
   rebuild from registered artifacts.
3. Changed cloud entrypoints require Level 3 live smoke.
4. Missing route/gate rows that cannot be reconstructed locally require Level 4
   bounded refresh.
5. Invalid matrix semantics require Level 5 full benchmark rerun.

## Decisions

| Card | Change Type | Rerun Level | Decision | Reason |
|---|---|---|---|---|
| CP-Q8.7A | Issue ledger and claim boundary | Level 1 | No cloud rerun | Planning artifact only; no executable semantics changed. |
| CP-Q8.7B | FCR and oracle-regret metric audit | Level 2 | No cloud rerun | Values reconciled from CP-Q2, CP-Q3, CP-Q5, and CP-Q6 artifacts. |
| CP-Q8.7C | Stratified FCR and expression-only comparator tables | Level 2 | No cloud rerun | S24 is derived from registered CP-Q2, CP-Q3, and CP-Q5 tables. |
| CP-Q8.7D | Gate decomposition and leakage definition | Level 2 | No cloud rerun | S25 is derived from existing CP-Q5 route columns. |
| CP-Q8.7E | Threshold operating-point tables | Level 2 | No cloud rerun | S26 is derived from CP-Q3, CP-Q5, CP-Q6, and CP-Q7 artifacts. |
| CP-Q8.7F | LR/pathway and graph method specification | Level 1 | No cloud rerun | Manuscript/specification patch only. |
| CP-Q8.7G | Claim rewrite and literature-concordance audit | Level 1 | No cloud rerun | Manuscript wording, reviewer supplement, and Data/Code wording only; no metrics, thresholds, scripts, or entrypoints changed. |

## Current Conclusion

No active CP-Q8.7G trigger requires a bounded or full cloud rerun. The stored
benchmark artifacts already support the revised, narrower claim language:
under the pre-specified ContextGate gates, no real-data setting is routed to
`context_allowed`, while positive-control detectability and false-context
safety remain explicit.
