# CP-Q8.8 Full Paper-Wizard Hidden-Issue Ledger

Date: 2026-05-05

Scope: expanded Paper-Wizard online issue list supplied by the user after
CP-Q8.7. CP-Q8.7 closed the ten visible/highest-priority blockers. This ledger
maps every remaining visible hidden issue before any manuscript, table, or
figure edits are made in CP-Q8.8B-L.

## Claim and Scope Lock

CP-Q8.8 keeps the same scientific boundary established in CP-Q8.7:

> Under the benchmark's pre-specified conservative evidence gate, no real-data
> setting was routed to `context_allowed` in the registered imaging-based
> spatial transcriptomics benchmark. This is a ContextGate-defined evidence
> decision, not proof that tumor neighborhoods lack biology.

CP-Q8.8 is not a new dataset chase, not a named-tool benchmark, and not final
Elsevier release polish. It is a reviewer-hardening sweep that either patches,
documents, derives, or explicitly defers every expanded Paper-Wizard issue.

## Status Vocabulary

| Status | Meaning |
|---|---|
| Already resolved | CP-Q8.6/CP-Q8.7 already implemented the required fix; CP-Q8.8 only verifies and records it. |
| Needs prose patch | Main manuscript wording must change, but no new table/figure/result is required. |
| Needs local audit/table | Existing registered artifacts should be summarized into a new table or audit note. |
| Needs figure patch | Figure-generation or caption output must change and be visually inspected. |
| Release-polish deferred | Valid concern, but intentionally deferred because it is final submission packaging rather than method validity. |
| Modal decision pending | Local audit must first decide whether existing artifacts are enough or whether Level 4/5 rerun is triggered. |

## Rerun-Level Vocabulary

| Level | Meaning |
|---|---|
| Level 1 | Prose/caption/ledger only; no Modal rerun. |
| Level 2 | Derived table/figure from registered artifacts; local rebuild only. |
| Level 3 | New local audit script/schema artifact from existing files; full local tests. |
| Level 4 | Missing evidence requires bounded Modal refresh. |
| Level 5 | Route logic, thresholds, or CP-Q6 matrix semantics change; full Modal matrix rerun. |

## Title, Abstract, Introduction, Discussion, Figures, and Appendix Issues

| Issue | Short name | Current status | Owner card | Expected rerun | Required action |
|---|---|---|---|---|---|
| A1 | Title platform-scope alignment | Patched in CP-Q8.8B | CP-Q8.8B | Level 1 | Title now specifies imaging-based spatial transcriptomic models and aligns with Table 1 platform scope. |
| B1 | Abstract author-defined gate qualifier | Patched in CP-Q8.8B | CP-Q8.8B | Level 1 | Abstract route-count sentence now states the benchmark's pre-specified conservative ContextGate evidence gate. |
| C1 | Draft placeholders/readiness | Resolved as explicit release-polish boundary | CP-Q8.8J | Level 1 complete; no Modal | Manuscript now separates release-readiness placeholders from methodological evidence, listing graphical abstract, architecture figure, author metadata, AI-use/human rewrite, acknowledgements, reference formatting, reviewer-access link, GitHub URL, and DOI as final submission items. |
| C2 | Benchmark-family gap differentiation | Patched in CP-Q8.8B | CP-Q8.8B | Level 1 | Related Work now distinguishes deconvolution, spatial-domain/SVG, LR/CCI, histology-to-ST, and ContextGate-Bench questions. |
| F1 | Practitioner workflow evidentiary qualifier | Patched in CP-Q8.8B | CP-Q8.8B | Level 1 | Discussion now clarifies the workflow operationalizes ContextGate logic but is not independently validated against alternative workflows. |
| F2 | Biological motivation vs methodological finding transition | Patched in CP-Q8.8B | CP-Q8.8B | Level 1 | Discussion now states established spatial biology motivates the benchmark but is not itself tested by current route counts. |
| F3 | Foundation-model prospective language | Resolved in CP-Q8.8F | CP-Q8.8F | Level 3 complete; no Modal | Discussion and Methods now mark foundation/graph/CCC models as future benchmark-tier adapters rather than currently tested or defeated baselines; S29 records named-tool scope boundaries. |
| G1 | Method family representation across figures | Resolved in CP-Q8.8F and CP-Q8.8I | CP-Q8.8F, CP-Q8.8I | Level 2/3 complete; no Modal | S29 maps Section 3.4 method-family names to figure labels, captions point readers to the mapping, and CP-Q8.8I regenerated the affected figures with documented figure-specific inclusion/scope notes. |
| G2 | Figure 2 display conventions | Resolved in CP-Q8.8I | CP-Q8.8I | Level 2 complete; no Modal | Figure 2 now omits the constant skip-reason heatmap column, keeps explicit zero labels, uses adaptive annotation contrast, and points skip/infeasibility evidence to S14/S31. |
| G3 | Figure 4 injected-signal axis | Resolved in CP-Q8.8D and CP-Q8.8I | CP-Q8.8D, CP-Q8.8I | Level 2/3 complete; no Modal | Figure 4 now labels the x-axis as dimensionless signal coefficient `s`, marks the weak/noisy, localized, and strong rungs, and points to S16 for signal/noise/prevalence/effective-strength mapping. |
| G4 | Figure 3/Figure 8 sorting and labels | Resolved in CP-Q8.8H and CP-Q8.8I | CP-Q8.8I, CP-Q8.8H | Level 2/3 complete; no Modal | Figure 3 is sorted by descending mean regret with alphabetical tie-breaks; Figure 8 directly labels nonzero downgrade/failure segments and still shows only the seven row-generating stress families. |
| G5 | Figure 4/Figure 7 rendering artifacts | Resolved in CP-Q8.8I | CP-Q8.8I | Level 2 complete; no Modal | Figure 7 route labels are stripped of trailing hyphen artifacts, and Figure 4 uses a legend plus rung guide labels to avoid overlapping inline method labels. |
| H1 | Artifact accessibility | Archive contents specified; final link deferred | CP-Q8.8J, CP-Q8.8L | Level 1 complete; no Modal | Data and Code Availability now names the reviewer-access archive, public repository, and DOI placeholders and lists the required archive contents; insertion of live links remains a release-polish submission blocker for CP-Q8.8L/final packaging. |

## Methods Issues

| Issue | Short name | Status after CP-Q8.8A | Owner card | Expected rerun | Required action |
|---|---|---|---|---|---|
| D1 | Route-ground-truth independence | Already resolved; verify wording | CP-Q8.8A, CP-Q8.7G | Level 1 | Ensure CP-Q8.7 claim-boundary language remains in abstract, Section 4.4, limitations, and final ledger. |
| D2 | Leakage-audit gate | Already resolved; verify wording/table | CP-Q8.8A, CP-Q8.7D | Level 2 | Verify `ell_i` definition and S25 gate decomposition remain cited and consistent. |
| D3 | LR/pathway and graph implementation | Already resolved; verify details | CP-Q8.8A, CP-Q8.7F | Level 1 | Confirm Section 3.4 names pair source, graph `k=5`, aggregation, thresholds, and method-card pointers. |
| D4 | FCR null-stratum denominator | Already resolved; verify S24 | CP-Q8.8A, CP-Q8.7C | Level 2 | Confirm S24/Table 3 distinguish all-row exposure from null-denominator FCR. |
| D5 | Threshold sensitivity | Resolved in CP-Q8.8H | CP-Q8.8H | Level 3 complete; no Modal | S33A lists exact threshold grid rows, S26 reports operating points, and Section 4.6 states route counts remain 23/40/37/0 across the tested operating region. |
| D6 | FDR correction scope and spatial autocorrelation | Resolved in CP-Q8.8C | CP-Q8.8C | Level 3 complete; no Modal | Methods now define the one-sided effect-test q-value, BH split-level correction scope, and spatial-dependence caveat; S27 records the reproducible source code/artifact pointers. |
| D7 | Spatial-statistics heuristic score | Resolved in CP-Q8.8F | CP-Q8.8F | Level 3 complete; no Modal | Methods now define the CP-R1 context-utility score route proxy, thresholds, and CP-Q2 score distribution; S29 records the heuristic's FCR, no-harm, abstention, context-use, and scope boundary. |
| D8 | Utility normalization and oracle bias | Resolved in CP-Q8.8C | CP-Q8.8C | Level 3 complete; no Modal | Methods now define route/metric utility mapping, in-sample empirical oracle semantics, and the non-absolute interpretation of zero regret; S27 audits source artifacts. |
| D9 | Hyperparameter tuning equity | Resolved in CP-Q8.8F | CP-Q8.8F | Level 3 complete; no Modal | Methods state CellPack hyperparameters were fixed a priori and that expression-only, spatial-statistics, LR/pathway, and graph rows are deterministic registered comparator rules rather than separately optimized leaderboard entries; S29 records tuning/access notes. |
| D10 | Expression normalization across panels | Resolved in CP-Q8.8C | CP-Q8.8C | Level 3 complete; no Modal | Section 3.3 now states task-layer normalization and avoids raw CosMx/Xenium scale pooling; S27 summarizes the normalization boundary. |
| D11 | Biological realism of linear positive control | Resolved in CP-Q8.8D | CP-Q8.8D | Level 2/3 complete; no Modal | Methods, Results, and Limitations now state the ladder validates linear mean-neighbor dependencies and does not cover nonlinear, thresholded, or state-conditional biology. |
| D12 | Positive-control signal/noise parameters | Resolved in CP-Q8.8D | CP-Q8.8D | Level 3 complete; no Modal | S16 now reports injected/effective signal strength, noise fraction, prevalence, localization scope, expected route, and ladder descriptions from CP-Q3 artifacts. |
| D13 | FOV boundary constraints for neighbor graphs | Resolved in CP-Q8.8E | CP-Q8.8E | Level 3 complete; no Modal | Section 3.3 and S28 document k=5 Euclidean graph construction grouped by `sample_id`+`slide_id`; CosMx `slide_id` is FOV-derived and validation rejects sample/slide boundary crossings. |
| D14 | Injection/detection structural correspondence | Resolved in CP-Q8.8D | CP-Q8.8D | Level 1 complete; no Modal | Section 3.3 now explicitly states the injection uses the same k-neighbor mean-pooling operator as the detection feature and scopes the calibration accordingly. |
| D15 | Minimum detectable effect | Resolved as synthetic detectability floor in CP-Q8.8D | CP-Q8.8D | Level 3 complete; no Modal | S19 reports the smallest recovered ContextGate synthetic strength (`s=0.55`, effective about 0.56) and the text labels it as a ladder-specific floor, not a real-data 80% power bound. |
| D16 | Positive-control notation consistency | Resolved in CP-Q8.8D | CP-Q8.8D | Level 1 complete; no Modal | Section 3.3 defines `zbar_Nk(i),L+` as the mean over synthetic neighbor-marker set `L+`, linked to the existing mean-neighbor notation. |
| D17 | Aggregate threshold rationale | Resolved in CP-Q8.8C and CP-Q8.8H | CP-Q8.8C, CP-Q8.8H | Level 3 complete; no Modal | Methods frame thresholds as safety-first publication operating points; S33A now exposes exact route-recovery, sensitivity, specificity, replication, no-harm, FDR, and FCR operating-point projections. |
| D18 | Named spatial-tool coverage | Resolved in CP-Q8.8F | CP-Q8.8F | Level 3 complete; no Modal | Methods now name COMMOT, SpatialDM, SpaTalk, NicheCompass, CellNeighborEX, GraphST, STAGATE, SpaGCN, Nicheformer, and Novae as future adapter targets; S29 records why they are not CP-Q2 route rows in this release. |
| D19 | Single-sample contribution to aggregates | Resolved in CP-Q8.8E and cross-linked in CP-Q8.8G | CP-Q8.8E, CP-Q8.8G | Level 3 complete; no Modal | S28 stratifies jobs and route counts by multi-sample/donor versus single-donor/FOV-only rows; S30B adds full-tier dataset-task denominators and skipped-job groups. |
| D20 | CellPack input ceiling | Resolved in CP-Q8.8F | CP-Q8.8F | Level 3 complete; no Modal | Methods and S29 quantify the 64-128 gene CellPack ceiling as 0.7-23.6% of included panels and 0.7-1.4% of the 9,475-gene panel, qualifying neural conclusions as input-constrained. |
| D21 | Threshold-sweep ranges | Resolved in CP-Q8.8H | CP-Q8.8H | Level 3 complete; no Modal | S33A lists CP-Q7 row-level ranges and operating-point projections, records that spatial-statistics helper thresholds were not swept in CP-Q7, and confirms no tested/projection setting yields `context_allowed`. |
| D22 | Formal definition of registered | Resolved in CP-Q8.8C | CP-Q8.8C | Level 1/3 complete; no Modal | Section 3.7 now defines registered artifacts as version-controlled manifest/registry entries and distinguishes this from external pre-registration or DOI deposition. |
| D23 | Replication-tier transparency | Resolved in CP-Q8.8E | CP-Q8.8E | Level 3 complete; no Modal | Dataset Methods, Results, Limitations, and S28 distinguish single-donor/FOV-only evidence from multi-sample/donor rows and flag the stronger future replay target. |
| D24 | Platform coverage/generalizability | Resolved for CP-Q8.8E scope | CP-Q8.8B, CP-Q8.8E | Level 1/3 complete; no Modal | CP-Q8.8B scoped claims to targeted-panel imaging artifacts; CP-Q8.8E adds dataset-scope, replication-tier, and frozen validation cohort audit in S28. |
| D25 | GSE311609 freeze reason | Resolved in CP-Q8.8E | CP-Q8.8E | Level 3 complete; no Modal | Table 1, Methods, Limitations, and S28 state that GSE311609 is frozen due to file-format conversion, label joins, preprocessing, and cloud cost, and mark it as the first future replay candidate. |

## Results and Analysis Issues

| Issue | Short name | Status after CP-Q8.8A | Owner card | Expected rerun | Required action |
|---|---|---|---|---|---|
| E1 | Always-context FCR inconsistency | Already resolved; verify | CP-Q8.8A, CP-Q8.7B | Level 2 | Confirm `0.4783` is all-row exposure and null-denominator always-context FCR is `1.000`. |
| E2 | Gate-by-gate decomposition | Already resolved; verify | CP-Q8.8A, CP-Q8.7D | Level 2 | Confirm S25 gives gate failures for 63 non-positive-control decisions. |
| E3 | Oracle-regret figure/text consistency | Resolved; captions and figure sorting verified in CP-Q8.8I | CP-Q8.8A, CP-Q8.8I | Level 2 complete; no Modal | Figure 2 and Figure 3 scopes are labelled CP-Q6 versus CP-Q2, and Figure 3 is regenerated with documented descending regret order and alphabetical tie-breaks. |
| E4 | ContextGate versus expression-only FCR | Already resolved; verify | CP-Q8.8A, CP-Q8.7C | Level 2 | Confirm Table 3 states expression-only FCR `0.000` and positive-control sensitivity difference. |
| E5 | Job-to-route aggregation transparency | Resolved in CP-Q8.8G | CP-Q8.8G | Level 3 complete; no Modal | S30A traces the 100 route decisions to 72 CP-Q3 ladder rows, 23 CP-R1 context-utility rows, and 5 rejected/access-blocked dataset-card rows, and states that CP-Q6 jobs provide metric evidence rather than direct route votes. |
| E6 | Spatial-stats safety metrics | Resolved in CP-Q8.8F | CP-Q8.8F | Level 3 complete; no Modal | Results and S29 report spatial-statistics no-harm 1.000, FCR 0.000, abstention 0.4783, context-use 0.0435, and that its only context-use row is positive-control-only. |
| E7 | Per-dataset/per-task metrics | Resolved in CP-Q8.8G | CP-Q8.8G | Level 3 complete; no Modal | S30B reports all 36 full-tier dataset-task job groups with q1 completed/skipped jobs, metric rows, mean error, residual delta, regret, FCR, no-harm, abstention, and route counts where applicable. |
| E8 | Threshold perturbation parameters | Resolved in CP-Q8.8H | CP-Q8.8H | Level 3 complete; no Modal | S33A lists each perturbed threshold, range/direction, observed value, pass/downgrade outcome, and unchanged route counts. |
| E9 | Dataset count consistency | Resolved in CP-Q8.8G | CP-Q8.8G | Level 2/3 complete; no Modal | Results now defines "11 dataset-card identifiers" as six executed backbones plus five rejected/access-blocked ledger rows, not 11 executed datasets; S30A and S30B provide the route and q1 task denominators. |
| E10 | Rung-stratified sensitivity | Resolved in CP-Q8.8D and CP-Q8.8I | CP-Q8.8D, CP-Q8.8I | Level 2/3 complete; no Modal | S16 and S19 expose strong, weak/noisy, and localized rung recovery; Figure 4 now annotates those rungs directly while preserving the S16 coefficient mapping. |
| E11 | Route confidence definition | Resolved in CP-Q8.8C | CP-Q8.8C | Level 3 complete; no Modal | Methods and S27 now define confidence as a deterministic route-assurance scalar, not a calibrated posterior probability. |
| E12 | Panel observability test | Resolved in CP-Q8.8G | CP-Q8.8G | Level 3 complete; no Modal | S32 stratifies context-utility scores, high-score rows, panel-coverage failures, insufficient-power rows, and FOV/sample-artifact rows by panel-depth group; text now frames panel observability as descriptive, not proven monotonic. |
| E13 | Zero regret interpretation | Resolved in CP-Q8.8F | CP-Q8.8F | Level 3 complete; no Modal | Results and Figure 3 caption now state zero regret for the top method follows definitionally from matching the in-sample empirical oracle and is not an absolute quality claim. |
| E14 | Sensitivity/specificity uncertainty | Resolved in CP-Q8.8D | CP-Q8.8D | Level 2 complete; no Modal | S19 and the Results now report denominators plus Wilson route-recovery intervals and score intervals for ContextGate positive/null ladder estimates. |
| E15 | Job-count disparity rationale | Resolved in CP-Q8.8E and cross-linked in CP-Q8.8G | CP-Q8.8E, CP-Q8.8G | Level 3 complete; no Modal | S28 reports per-dataset planned/completed/skipped jobs, and S30B now exposes q1 dataset-task job groups including the fully skipped Xenium breast 5K label-prediction group. |
| E16 | Failure-taxonomy denominator | Resolved in CP-Q8.8G and visually verified in CP-Q8.8I | CP-Q8.8G, CP-Q8.8I | Level 2/3 complete; no Modal | S31 defines the unit as 449 `failure_taxonomy_id` rows over 164 unique benchmark row IDs, with six IDs carrying multiple classes; the regenerated figure/caption set keeps the denominator audit as table-facing support. |
| E17 | Gate pass rate definition | Resolved in CP-Q8.8C | CP-Q8.8C | Level 3 complete; no Modal | Methods and S27 now define gate_pass_rate as synthetic-control consistency over per-row gate_passed, distinct from sensitivity, specificity, or execution completeness. |
| E18 | Stress-family list consistency | Resolved in CP-Q8.8H and CP-Q8.8I | CP-Q8.8H, CP-Q8.8I | Level 2/3 complete; no Modal | S33B and Figure 8 caption distinguish seven row-generating stress families from the separate claim-survival audit, and Figure 8 now labels the nonzero downgrade segment directly. |
| E19 | Seventh downgrade accounting | Resolved in CP-Q8.8H and visually checked in CP-Q8.8I | CP-Q8.8H, CP-Q8.8I | Level 2/3 complete; no Modal | S33B shows the registered accounting is 5 threshold-stress downgrades + 1 claim-survival downgrade; no seventh downgrade exists in CP-Q7 artifacts, Section 4.6 corrects the stale count, and Figure 8 displays only the five row-level downgrades. |
| E20 | Sensitivity-safety tradeoff | Resolved in CP-Q8.8D and CP-Q8.8H | CP-Q8.8D, CP-Q8.8H | Level 3 complete; no Modal | S19 reports positive-route misses versus always-context; S33A adds operating-point floors showing ContextGate retains 1.000 positive-control route recovery while preserving FCR 0.000 across the tested/projection thresholds. |
| E21 | Model-capacity framing precision | Resolved in CP-Q8.8D | CP-Q8.8D, CP-Q8.8F | Level 1 complete; no Modal | Results now says the ladder "partially addresses" capacity objections for linear mean-neighbor dependencies rather than eliminating broader SOTA objections. |

## CP-Q8.8A Decisions

| Decision | Outcome |
|---|---|
| Do not edit manuscript prose in CP-Q8.8A | The first card is a ledger/scope-lock card; patches begin in CP-Q8.8B. |
| Do not run Modal in CP-Q8.8A | The ledger does not change metrics, route logic, thresholds, or artifacts. Modal decisions are recorded per issue and revisited during cards C-H. |
| Preserve CP-Q8.7 closure | D1-D5, E1-E4, and H1 remain closed at blocker level unless CP-Q8.8 verification finds a specific regression. |
| Keep release-polish separate | Draw.io artwork, final reference style, author metadata, acknowledgements, human rewrite, and public DOI/reviewer-link insertion are release-polish items, not hidden method blockers. |

## CP-Q8.8F Decisions

CP-Q8.8F closed the method-scope, spatial-statistics, named-tool, tuning, and
CellPack input-ceiling card by adding S29 and manuscript text for:

- Section 3.4 method-family names mapped to figure display labels;
- spatial-statistics FCR, no-harm, context-use, abstention, score thresholds,
  and CP-Q2 score distribution;
- zero-regret interpretation as an in-sample empirical-oracle identity;
- fixed-a-priori tuning policy across deterministic comparator rules;
- CellPack's 64--128 gene ceiling as an input-starvation boundary;
- COMMOT, SpatialDM, SpaTalk, NicheCompass, CellNeighborEX, GraphST, STAGATE,
  SpaGCN, Nicheformer, and Novae as future adapter targets rather than
  currently tested baselines.

CP-Q8.8F stayed Level 3 because it generated a local audit table from existing
registered artifacts, method-comparison outputs, source code, and the SOTA
feasibility ledger. It did not change route logic, thresholds, metric values,
benchmark semantics, cloud entrypoints, or Modal execution requirements.

## CP-Q8.8G Decisions

CP-Q8.8G closed the aggregation/disaggregation and denominator card by adding
S30A, S30B, S31, and S32 plus manuscript text for:

- the 100-route decision source trace: 72 CP-Q3 ladder rows, 23 CP-R1
  context-utility rows, and 5 rejected/access-blocked dataset-card rows;
- the CP-Q6 matrix boundary: 2,324 completed jobs and 436 skipped jobs supply
  metric evidence rather than direct route votes;
- all 36 full-tier dataset-task job groups, including fully skipped groups;
- panel-depth observability strata with context-utility and failure counts;
- failure-taxonomy row units, denominator, and co-occurrence rule.

CP-Q8.8G stayed Level 3 because it generated local audit tables from existing
registered artifacts and source files. It did not change route logic,
thresholds, metric values, benchmark semantics, cloud entrypoints, or Modal
execution requirements.

## CP-Q8.8H Decisions

CP-Q8.8H closed the threshold/stress-accounting card by adding S33A, S33B, and
S33C plus manuscript text for:

- exact CP-Q7 threshold-sensitivity rows and their tested ranges;
- S26 operating-point projections for FDR, FCR, route-recovery, sensitivity,
  specificity, replication, and no-harm floors;
- spatial-statistics helper-threshold scope: documented as registered
  comparator thresholds, not swept in CP-Q7 and not used to support the strict
  ContextGate route-count claim;
- stress-family accounting: seven row-generating stress families produce 127
  stress rows, while claim survival is a separate six-claim audit;
- downgrade reconciliation: 5 threshold-stress downgrades plus 1 claim-survival
  downgrade, with no registered seventh downgrade.

CP-Q8.8H stayed Level 3 because it generated local audit tables from existing
CP-Q7 stress artifacts, CP-Q5 route summaries, CP-Q6 execution summaries, and
CP-Q3 ladder summaries. It did not change route logic, thresholds, metric
values, benchmark semantics, cloud entrypoints, or Modal execution
requirements.

## CP-Q8.8J Decisions

CP-Q8.8J closed the release-readiness boundary card by adding manuscript text
for:

- a dedicated release-polish placeholder boundary that explicitly separates
  submission packaging from unresolved methodology;
- a reviewer-access archive checklist covering source code, schemas,
  manifests, registered result tables, CP-Q artifacts, manuscript tables,
  figures, figure manifests, reviewer-hardening ledgers, command/test/rerun
  logs, Modal/cloud entrypoints, environment files, dataset ledgers, and
  reproduction instructions;
- explicit placeholders for the reviewer-access archive, public GitHub URL,
  and archival DOI.

CP-Q8.8J stayed Level 1 because it patched manuscript prose and ledgers only.
It did not change route logic, thresholds, metric values, benchmark semantics,
figures, tables, cloud entrypoints, or Modal execution requirements. The live
reviewer-access link/DOI insertion remains release packaging, not a hidden
method blocker.

## CP-Q8.8K Decisions

CP-Q8.8K closed the manuscript integration and visual-QA card by:

- regenerating all manuscript table fragments and publication figures from
  registered local artifacts;
- compiling the Elsevier draft into
  `manuscript/build_cp_q8_8k/contextgate_bench_elsevier_template.pdf`;
- rendering all 47 PDF pages with `pdftoppm`;
- creating page and figure contact sheets under
  `tmp/pdfs/cp_q8_8k/contact_sheets/`;
- visually inspecting all rendered page/figure contact sheets;
- running citation/reference, stale wording, figure/table citation, and
  title/abstract scope audits.

The only manuscript prose patch in CP-Q8.8K tightened one stale abstract phrase
from broad "predictive transcriptomic models" wording to predictive models for
imaging-based spatial transcriptomic data. CP-Q8.8K stayed Level 2 because it
regenerated derived tables/figures and visual QA artifacts from existing
registered files. It did not change route logic, thresholds, metric values,
benchmark semantics, cloud entrypoints, or Modal execution requirements.

## CP-Q8.8L Decisions

CP-Q8.8L closed the expanded hidden-issue sweep by adding
`cp_q8_8_final_validation_ledger.md`. The final ledger marks every A-H issue as
resolved, resolved with a scope limitation, or release-polish tracked; records
the table/figure rebuild, manuscript compile, 47-page PDF render, visual QA,
text/cross-reference audit, full pytest, live Modal smoke, ruff, compileall,
and diff-hygiene evidence; and states that no active Level 4 or Level 5 trigger
remains.

The live Modal smoke test passed through
`RUN_MODAL_TESTS=1 python -m pytest tests/integration/test_modal_live_smoke.py -q -rs`.
This is an entrypoint health check rather than a bounded/full Modal matrix
rerun. No CP-Q8.8 change altered route logic, thresholds, metric values,
benchmark semantics, cloud entrypoints, or source-data contracts in a way that
requires rerunning the benchmark matrix.

## Immediate Next Card

CP-Q8.8L is complete. The next work can return to final release polish:
graphical abstract, architecture artwork, author metadata, acknowledgements,
reference normalization, human rewrite, reviewer-access link, public GitHub
URL, and archival DOI insertion.
