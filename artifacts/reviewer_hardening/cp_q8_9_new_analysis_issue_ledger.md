# CP-Q8.9 New-Analysis Issue Ledger

Date: 2026-05-07

Scope: 26 minor issues from the 2026-05-07 Paper-Wizard new-analysis report
for the ContextGate-Bench Elsevier draft.

Source plan:
`manuscript/contextgate_bench_cp_q8_9_new_analysis_minor_issue_plan.md`

## Status Key

- `triaged`: source of truth identified; implementation handled by a later
  CP-Q8.9 card.
- `planned`: mapped to a CP-Q8.9 card but not yet patched.
- `needs local artifact`: requires a derived local table/audit from existing
  registered artifacts.
- `needs prose/caption patch`: no metric rerun expected.
- `stop if inconsistent`: requires Modal or semantic decision if trace does
  not reconcile from registered artifacts.

## Ledger

| Issue | Short name | Primary Linear issue | Current status | Evidence or next action |
|---|---|---|---|---|
| A1 | Abstract aggregation ratio | RIS-14 / CP-Q8.9I | patched | Abstract now states that 2,760 planned jobs, 2,324 completed jobs, 436 skips, and 34,860 metric rows are infrastructure metric/skip/robustness evidence, while the primary claim-to-evidence outputs are the 100 ContextGate route decisions. |
| B1 | Utility matrix construction | RIS-7 / CP-Q8.9B | patched | Methods now define CP-Q2 route-label utility and CP-Q6 metric utility separately; Supplementary Table S34 lists the route utility matrix and tier glossary. |
| B2 | Missing-panel control category | RIS-8 / CP-Q8.9C | patched | Added Supplementary Table S35 with registered null/control denominator, panel-blocked positive rung, and null/control summaries excluding missing-panel rows. Registered labels were preserved. |
| B3 | Threshold derivation | RIS-9 / CP-Q8.9D | patched | Methods now add qualitative loss framing for false-context costs, threshold asymmetry, route-recovery floor, and S38 threshold-policy audit. |
| B4 | Injection/evaluation operator identity | RIS-10, RIS-14 / CP-Q8.9E/I | patched | Abstract, Section 4.3, Conclusion, Limitations, and S39 now scope sensitivity to the registered matched linear mean-neighbor synthetic operator rather than nonlinear spatial biology. |
| B5 | q-gate spatial autocorrelation | RIS-9 / CP-Q8.9D | patched | Revised q_i wording to nominal within-split BH evidence under spatial dependence; conservative policy now attributed to the full conjunctive gate. |
| B6 | CP-Q/CP-R terminology | RIS-7 / CP-Q8.9B | patched | Added first-use tier glossary in Methods and Supplementary Table S34 with artifact-scope definitions. |
| B7 | Shared-score method independence | RIS-7, RIS-12 / CP-Q8.9B/G | patched | Section 4.2 and S34/S37 now state spatial-stats, graph proxy, and ContextGate are threshold-policy comparators over shared CP-R1 evidence. |
| B8 | k-neighborhood sensitivity | RIS-10 / CP-Q8.9E | patched | S39 records that CP-Q3 artifacts are k=5 only and that k={3,10} robustness would require a bounded future replay; manuscript detectability claims are limited to k=5. |
| B9 | LR starter-list coverage | RIS-12 / CP-Q8.9G | patched | Added S37 with the 16-pair `common_lr_starter` list, CP-R1/registry available-pair counts by dataset, module-target counts, and row-level >=4 threshold scope. |
| B10 | SOTA exclusion scope | RIS-12, RIS-14 / CP-Q8.9G/I | patched | Abstract and Table 3 now scope the zero `context_allowed` result to registered lightweight method-family implementations/current comparators; S37 says named SOTA tools require future adapter tiers. |
| B11 | CellPack gene-cap boundary | RIS-12 / CP-Q8.9G | patched | Section 4.4 and S37 clarify that CellPack's 64-128 gene cap is an input-constrained comparator limitation, not the source of universal gate-1 failure across full-panel evidence. |
| B12 | Conjunctive-gate directional bias | RIS-9 / CP-Q8.9D | patched | Added S25 pass-rate column, S38 policy table, and Section 4.4 false-negative-bias statement with threshold-sweep evidence. |
| C1 | Figure 2/prose false-context values | RIS-6, RIS-13 / CP-Q8.9A/H | patched | Section 4.2 now labels the 0.4783/0.000 false-context values as CP-Q2 route-comparison values and explicitly distinguishes them from Figure 2's CP-Q6 q1 all-row exposure cells (e.g., 0.6226 and 0.0647). |
| C2 | 36 vs 37 positive-control-only count | RIS-6, RIS-8 / CP-Q8.9A/C | patched | Main text and Table 3 now state 37 = 36 CP-Q3 positive ladder rows plus one CP-R1 synthetic-mechanics-only `positive_control_only` row. |
| C3 | Power taxonomy independence | RIS-11 / CP-Q8.9F | patched | Added Supplementary Table S36 with split/job coverage, residual-delta CI-width proxies, and explicit power-vs-null unresolved wording; taxonomy prose no longer treats non-significance as independent proof of low power. |
| C4 | Positive-control sensitivity score | RIS-6, RIS-8 / CP-Q8.9A/C | patched | Methods now separate continuous sensitivity/specificity score means from binary route recovery/rejection; S27/S35 expose score and Wilson intervals. |
| C5 | CP-Q2 regret vs CP-Q6 regret | RIS-6, RIS-7 / CP-Q8.9A/B | patched | Section 4.2 now reports CP-Q2 regret 0.0261 alongside CP-Q6 q1 regret 0.343, core 0.437, and mini 0.216; S34 records scope differences. |
| C6 | Synthetic effect calibration | RIS-10 / CP-Q8.9E | patched | S39 reports registered s/effective-strength ranges and states the coefficient is unitless synthetic ladder strength, not a residual-SD or published LR effect-size calibration. |
| C7 | Per-split cell counts | RIS-11 / CP-Q8.9F | patched | S36 reports registered dataset-level cell/unit counts by CP-Q6 split and states that per-fold train/test cell counts are not serialized in local artifacts; formal MDE requires a bounded future artifact refresh. |
| C8 | Spatial-stats zero-regret independence | RIS-6, RIS-7 / CP-Q8.9A/B | patched | Section 4.2 states zero regret follows from in-sample CP-Q2 oracle label alignment; S34 frames this as route-label utility rather than independent predictive optimality. |
| C9 | Panel-depth confounding | RIS-12 / CP-Q8.9G | patched | Section 4.4 now presents cancer type, donor/sample structure, FOV constraints, replication depth, and target-definition confounders before interpreting panel-depth strata; S37 records the same boundary. |
| D1 | Conditional utility framing | RIS-10, RIS-14 / CP-Q8.9E/I | patched | Abstract, keywords, Table 3, and conclusion now frame "conditional" as a normative evidence-release rule and explicitly state that no real-data context utility was detected under the registered targeted-panel datasets and method families. |
| E1 | Figure method coverage consistency | RIS-13 / CP-Q8.9H | patched | Figures 2-5 captions now state their CP-Q tier, displayed-method eligibility, and S29/S37 method-roster pointers. |
| E2 | Figure 2 metric polarity | RIS-13 / CP-Q8.9H | patched | Figure 2 caption now states which metrics are higher-better and lower-better despite the shared colormap. |
| E3 | Figure 4 weak/noisy tick | RIS-13 / CP-Q8.9H | patched | Publication figure builder now fixes the positive-control x-axis at 0.50--1.03 with explicit ticks at 0.55, 0.75, and 1.00; regenerated Figure 4 artifacts show the weak/noisy rung on-axis. |

## CP-Q8.9A Stop-Rule Result

No CP-Q8.9A trace requires an immediate Level 4 or Level 5 rerun.

- C1 reconciles as CP-Q2 prose versus CP-Q6 figure scope.
- C2 reconciles as 36 CP-Q3 positive-control-only decisions plus one CP-R1
  synthetic-mechanics-only positive-control decision.
- C4 reconciles as continuous sensitivity/specificity score versus binary
  route recovery.
- C5 reconciles as CP-Q2 subset regret versus CP-Q6 full-matrix regret.
- C8 needs a manuscript caveat or registry pointer, not a rerun.

Implementation cards CP-Q8.9B, CP-Q8.9C, and CP-Q8.9H must now patch the
manuscript/tables/figures so these distinctions are visible to readers.

## CP-Q8.9J Final Closeout

Final validation is recorded in
`manuscript/reviewer_hardening/cp_q8_9_final_validation_ledger.md`.

All 26 CP-Q8.9 new-analysis minor issues are now patched, limitation-resolved,
or release-deferred for non-method submission packaging reasons. No active
Level 4 or Level 5 rerun trigger remains after the final local rebuilds, PDF
QA, stale-text audit, and bounded live Modal smoke.
