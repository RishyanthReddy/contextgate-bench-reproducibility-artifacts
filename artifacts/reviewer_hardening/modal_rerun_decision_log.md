# CP-Q8.6I Modal Re-Execution Decision Log

Date: 2026-05-05

## Final Decision

**Current decision:** no new Modal rerun is required after CP-Q8.6A-H.

CP-Q8.6A-H hardened the manuscript and supplementary evidence through
documentation, formal contracts, local table builders, literature guardrails,
and feasibility ledgers. They did not change:

- Modal entrypoints;
- CP-Q6 benchmark job construction;
- core metric semantics;
- ContextGate implementation logic;
- scale-contract compliance rules;
- registered real-data artifacts;
- or SOTA/method rows in the benchmark matrix.

Therefore the correct rerun level is:

> **Level 1 for prose/citation/audit cards and Level 2 for derived local table
> rebuild cards. No Level 3, 4, or 5 Modal trigger is active.**

The machine-readable decision table is
`manuscript/reviewer_hardening/modal_rerun_decision_log.csv`.

## Rerun Ladder Applied

1. **No Modal rerun:** documentation, citation expansion, formal contracts,
   feasibility decisions, and explanations from existing artifacts.
2. **Local rebuild only:** tables or audits derived from already registered
   CP-Q artifacts.
3. **Live Modal smoke:** only if a Modal entrypoint or cloud code path changes.
4. **Bounded Modal artifact refresh:** only if a new calibration artifact,
   method adapter, SOTA replay, or CP-Q6/CP-Q7 artifact schema changes.
5. **Full Modal matrix rerun:** only if CP-Q6 job construction, metric
   semantics, ContextGate logic, or scale-contract compliance changes.

## Card-by-Card Outcome

CP-Q8.6A, B, C, G, H, and I are Level 1: no Modal rerun. They add reviewer
ledgers, method descriptions, route-contract documentation, citation
guardrails, SOTA feasibility decisions, and this rerun decision log.

CP-Q8.6D, E, and F are Level 2: local rebuild only. They extend
`scripts/build_contextgate_manuscript_tables.py` and generate supplementary
tables from already registered CP-Q2 through CP-Q7 artifacts. These cards were
validated by local table builds, unit tests, lint, compile checks, and full
default pytest. They did not change Modal code or benchmark semantics.

CP-Q8.6H is the key Modal decision point. It did not choose
`run_limited_replay`; it chose cite-scope and adapter-only future plans. That
means no bounded SOTA Modal refresh is triggered.

## Conditions That Would Reopen Modal

Run Modal later only if CP-Q8.6J or CP-Q8.6K introduces one of these concrete
changes:

- a new method adapter or SOTA baseline is added to CP-Q tables;
- a Modal entrypoint changes;
- CP-Q6 job construction changes;
- ContextGate route logic changes in code, not just prose;
- scale-contract compliance logic changes;
- CP-Q7 calibration rows are found insufficient and must be refreshed;
- manuscript integration uncovers a missing registered artifact that cannot be
  derived locally.

If none of those occur, CP-Q8.6J should do local manuscript/table integration
and Tectonic compilation only.

## Practical Implication For The User

The expensive Modal work already happened in CP-Q6 and CP-Q7. The reviewer-
hardening phase is now mostly publication packaging. That is good: the paper is
leaning on the existing benchmark matrix and stress-test evidence rather than
silently changing the experiment under the manuscript.

## Validation

This CP-Q8.6I card is validated by:

- CSV parse/status checks for `modal_rerun_decision_log.csv`;
- markdown fence checks for plan/TODO and rerun documents;
- full default local pytest;
- full lint across `src`, `scripts`, `tests`, and `modal`;
- compile checks across `src`, `scripts`, `tests`, and `modal`;
- `git diff --check`.

No Modal command is part of this validation because the artifact explicitly
documents that no active Modal trigger exists.
