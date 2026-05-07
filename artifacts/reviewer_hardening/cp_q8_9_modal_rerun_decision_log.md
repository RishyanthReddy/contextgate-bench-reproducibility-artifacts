# CP-Q8.9 Modal Rerun Decision Log

Date: 2026-05-07

Purpose: record whether each CP-Q8.9 card requires no Modal, live smoke only,
bounded Modal refresh, or full Modal matrix rerun.

## Rerun Ladder

| Level | Meaning |
|---|---|
| Level 1 | Prose/caption-only; no Modal. |
| Level 2 | Local table/figure rebuild from existing artifacts; no Modal. |
| Level 3 | New local audit table/script from existing artifacts; no Modal. |
| Level 4 | Bounded Modal refresh for missing evidence. |
| Level 5 | Full Modal rerun because route logic, threshold semantics, metric definitions, or CP-Q6 matrix validity changed. |

## Decisions

| Card | Decision | Rationale |
|---|---|---|
| CP-Q8.9A | Level 3 local trace only | C1, C2, C4, C5, and C8 reconcile to existing CP-Q2, CP-Q3, CP-Q5, CP-Q6, and CP-R1 artifacts. No route logic, threshold semantics, metric definition, cloud entrypoint, or source-data contract changed. |
| CP-Q8.9C | Level 3 local table/prose only | B2, C2, and C4 were resolved by preserving registered CP-Q3/CP-R1 labels, adding Supplementary Table S35 from existing artifacts, and clarifying score-versus-binary definitions in the manuscript. No primary control label, route-count truth, or metric semantics changed. |
| CP-Q8.9B | Level 3 local table/prose only | B1, B6, B7, C5, and C8 were resolved by adding Supplementary Table S34 from existing CP-Q2, CP-Q6, and CP-R1 artifacts and by clarifying CP-Q2 route-label utility versus CP-Q6 metric aggregates. No utility function, oracle rule, threshold, or route label changed. |
| CP-Q8.9D | Level 3 local table/prose only | B3, B5, and B12 were resolved by adding the S25 pass-rate column, creating Supplementary Table S38 from existing gate and threshold artifacts, and clarifying q_i as a nominal within-split BH screen plus the false-negative direction of the conjunctive gate. No threshold value, q-value computation, gate logic, route label, or CP-Q6 matrix row changed. |
| CP-Q8.9E | Level 3 local table/prose only | B4, B8, C6, and the first D1 framing pass were resolved by creating Supplementary Table S39 from existing CP-Q3 artifacts and by limiting positive-control sensitivity to the registered k=5 matched linear mean-neighbor ladder. No neighborhood graph, injected ladder row, route label, route threshold, or CP-Q3/CP-Q6 matrix artifact changed. |
| CP-Q8.9F | Level 3 local table/prose only | C3 and C7 were resolved by adding Supplementary Table S36 from existing CP-Q6, CP-Q4, and manifest artifacts and by qualifying the insufficient-power taxonomy as power-vs-null unresolved when per-fold train/test cell counts and residual variances are absent. No residual metric, q-value, split assignment, route label, or CP-Q6 matrix artifact changed. |
| CP-Q8.9G | Level 3 local table/prose only | B7, B9, B10, B11, and C9 were resolved by adding Supplementary Table S37 from existing CP-R1, artifact-registry, method-scope, and manifest artifacts and by tightening method-scope prose. No LR pair list, CP-R1 score, route threshold, method prediction, route label, or CP-Q6 matrix artifact changed. |
| CP-Q8.9H | Level 2 local figure/caption rebuild | C1, E1, E2, and E3 were resolved by regenerating Figure 4 from the existing CP-Q3 recovery curve and by adding CP-Q2/CP-Q6, method-eligibility, and metric-polarity caption qualifiers. No metric table, route label, threshold, or CP-Q6/CP-Q3 artifact changed. |
| CP-Q8.9I | Level 1 prose/table framing only | A1, B4, B10, and D1 were resolved by tightening abstract, keywords, Table 3, and conclusion claim-boundary language. No generated table/figure artifact, route label, threshold, metric, or benchmark matrix changed. |
| CP-Q8.9J | Level 2-3 local validation plus live Modal smoke | Final integration rebuilt tables and figures from existing artifacts, reran local tests and manuscript/PDF QA, and executed a bounded live Modal smoke (`xenium_breast_v1`, 64 units, 64 genes, k=5, 2 train steps). The smoke returned `status: pass` and only registered new EC-MODAL-01 smoke artifacts under output label `cp_q8_9j_mu64_mg64_k5_steps2`; it did not change CP-Q route logic, thresholds, metric definitions, or CP-Q6 matrix validity. |

## Current Stop Rule

No active Level 4 or Level 5 trigger after CP-Q8.9J.
