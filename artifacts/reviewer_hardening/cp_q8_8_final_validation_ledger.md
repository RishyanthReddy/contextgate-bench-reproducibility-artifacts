# CP-Q8.8 Final Validation Ledger and Stop Rule

Date: 2026-05-05

Scope: final closure record for the expanded Paper-Wizard hidden-issue sweep.
This ledger closes CP-Q8.8A-L, records command evidence, and separates final
release polish from methodological review debt.

## Claim Boundary

The manuscript now states the central result as a ContextGate-defined evidence
decision: under the benchmark's pre-specified conservative gates, no real-data
setting in the registered targeted-panel imaging-based spatial transcriptomics
artifacts was routed to `context_allowed`. This is not an independent proof that
spatial tumor biology is absent and is not a conclusion about sequencing-based
or whole-transcriptome spatial assays.

## Issue Closure Ledger

| Issue | Final status | Evidence |
|---|---|---|
| A1 Title scope | Resolved | Title now scopes the benchmark to imaging-based spatial transcriptomic models. |
| B1 Abstract gate qualifier | Resolved | Abstract names the pre-specified conservative ContextGate evidence gate and uses imaging-based scope. |
| C1 Draft placeholders/readiness | Release-polish tracked | Release-readiness section lists graphical abstract, architecture figure, author metadata, acknowledgements, reference style, human rewrite, GitHub URL, reviewer link, and DOI as final submission items. |
| C2 Benchmark-family gap differentiation | Resolved | Related Work separates deconvolution, spatial-domain/SVG, LR/CCI, histology-to-ST, and ContextGate-Bench questions. |
| D1 Route-ground-truth independence | Resolved with limitation | Abstract, Results, Discussion, and Limitations frame real-data routing as ContextGate-defined rather than independently adjudicated. |
| D2 Leakage-audit gate | Resolved | Methods define `ell_i`; S25 reports gate-level decomposition and zero leakage-audit failures. |
| D3 LR/pathway and graph implementation | Resolved | Section 3.4 and S29 specify frozen LR source, graph construction, aggregation, thresholds, and method-card pointers. |
| D4 FCR null denominator stratification | Resolved | S24/Table 3 distinguish all-row exposure from null-denominator false-context rate. |
| D5 Threshold sensitivity | Resolved | S33A and Section 4.6 report threshold grid/projections and unchanged route counts across tested operating points. |
| D6 FDR scope and spatial dependence | Resolved | Methods and S27 define one-sided effect test, BH split-level correction scope, and spatial-dependence caveat. |
| D7 Spatial-statistics heuristic score | Resolved | Methods and S29 define score proxy, thresholds, score distribution, FCR, no-harm, abstention, and context-use rate. |
| D8 Utility normalization/oracle bias | Resolved | Methods and S27 define normalized utility, empirical in-sample oracle, and non-absolute regret interpretation. |
| D9 Tuning equity | Resolved | Methods and S29 document fixed-a-priori comparator rules and CellPack smoke-scale tuning. |
| D10 Expression normalization | Resolved | Section 3.3 and S27 state task-layer normalization and avoid raw platform-scale pooling. |
| D11 Positive-control realism | Resolved with scope limit | Methods, Results, and Limitations scope ladder validation to linear mean-neighbor dependencies. |
| D12 Ladder signal/noise parameters | Resolved | S16 reports signal coefficients, effective strength, noise, prevalence, localization, and expected route. |
| D13 FOV graph boundaries | Resolved | Methods and S28 document k=5 Euclidean graph construction grouped by sample and slide/FOV. |
| D14 Injection/detection structural match | Resolved | Methods and Results state the injection is matched to the mean-neighbor operator and therefore validates that signal class. |
| D15 Minimum detectable effect | Resolved as synthetic floor | S19 reports smallest recovered synthetic signal and states it is not a real-data 80% power bound. |
| D16 Positive-control notation | Resolved | Section 3.3 defines the synthetic neighbor-marker summary explicitly. |
| D17 Aggregate threshold rationale | Resolved | Methods, S26, and S33A frame thresholds as safety-first publication operating points with sensitivity sweeps. |
| D18 Named spatial tools | Resolved with future scope | Methods and S29 list COMMOT, SpatialDM, SpaTalk, NicheCompass, CellNeighborEX, GraphST, STAGATE, SpaGCN, Nicheformer, and Novae as future adapters. |
| D19 Single-sample contribution | Resolved | S28/S30B stratify jobs and route counts by replication tier and dataset-task group. |
| D20 CellPack input ceiling | Resolved | Methods and S29 quantify the 64-128 gene ceiling and qualify neural conclusions as input-constrained. |
| D21 Threshold sweep ranges | Resolved | S33A lists threshold ranges, values, outcomes, and spatial-statistics helper-threshold scope. |
| D22 Registered definition | Resolved | Section 3.7 and S27 define registered artifacts as version-controlled manifest/registry entries, not external preregistration. |
| D23 Replication-tier transparency | Resolved | Methods, Results, Limitations, and S28 distinguish FOV-only evidence from multi-sample/donor evidence. |
| D24 Platform scope/generalizability | Resolved | Title, Abstract, Introduction, Results, Limitations, and Conclusion scope claims to targeted-panel imaging artifacts. |
| D25 GSE311609 freeze reason | Resolved | Table 1, Methods, Limitations, and S28 state the freeze reason and future-replay priority. |
| E1 Always-context FCR consistency | Resolved | S24, Figure 2 caption, and Table 3 distinguish all-row exposure 0.4783 from null-denominator FCR 1.000. |
| E2 Gate-by-gate decomposition | Resolved | S25 and Section 4.4 report gate failures for all non-positive-control decisions. |
| E3 Oracle-regret consistency | Resolved | Figure 2/3 captions distinguish CP-Q6 full-tier metrics from CP-Q2 oracle-regret scope. |
| E4 ContextGate vs expression-only FCR | Resolved | Table 3 and Section 4.5 state expression-only FCR is also 0.000 and ContextGate's added value is sensitivity plus auditability. |
| E5 Job-to-route aggregation | Resolved | S30A traces 100 route decisions to CP-Q3 ladder, CP-R1 context-utility, and rejected/access-blocked rows. |
| E6 Spatial-stats safety metrics | Resolved | S29 reports spatial-statistics FCR, no-harm, abstention, context-use, and context-use row identity. |
| E7 Per-dataset/task metrics | Resolved | S30B reports full-tier dataset-task metrics, skips, and route counts where applicable. |
| E8 Threshold perturbation parameters | Resolved | S33A lists perturbation ranges, directions, observed values, and outcomes. |
| E9 Dataset count consistency | Resolved | Results and S30A define the 11 dataset-card identifiers as six executed backbones plus five rejected/access-blocked rows. |
| E10 Rung-stratified sensitivity | Resolved | S16/S19 and Figure 4 expose strong, weak/noisy, and localized rung recovery. |
| E11 Route confidence definition | Resolved | Methods and S27 define confidence as deterministic route assurance, not a posterior probability. |
| E12 Panel observability test | Resolved | S32 stratifies context utility and failure classes by panel-depth group and keeps interpretation descriptive. |
| E13 Zero regret framing | Resolved | Results and Figure 3 caption state zero regret follows definitionally for the top empirical method. |
| E14 Sensitivity/specificity uncertainty | Resolved | S19 and Results report denominators plus Wilson intervals. |
| E15 Job-count disparity rationale | Resolved | S28 and S30B explain per-dataset job counts and fully skipped groups. |
| E16 Failure-taxonomy denominator | Resolved | S31 defines 449 taxonomy rows over 164 row IDs and co-occurrence rules. |
| E17 Gate-pass rate definition | Resolved | Methods and S27 define gate pass rate separately from sensitivity, specificity, and execution completeness. |
| E18 Stress-family list consistency | Resolved | S33B and Figure 8 distinguish seven row-generating stress families from the separate claim-survival audit. |
| E19 Seventh downgrade accounting | Resolved | S33B and Section 4.6 reconcile the stale count: five row-level threshold downgrades plus one claim-survival downgrade. |
| E20 Sensitivity-safety tradeoff | Resolved | S19 and S33A report positive-control misses and operating-point sensitivity/safety projections. |
| E21 Model-capacity framing | Resolved | Results now says the ladder partially addresses capacity objections for linear mean-neighbor dependencies only. |
| F1 Practitioner workflow | Resolved | Discussion states the workflow operationalizes ContextGate logic but is not independently validated against alternative workflows. |
| F2 Biological motivation transition | Resolved | Discussion distinguishes established spatial biology from the benchmark's methodological finding. |
| F3 Foundation-model claims | Resolved | Discussion and Limitations describe foundation/graph models as future benchmark-tier adapters. |
| G1 Figure method representation | Resolved | S29 maps method-family names to figure labels; captions explain figure-specific scope. |
| G2 Figure 2 display conventions | Resolved | Figure 2 removes the constant skip-reason column, uses explicit zero labels, and uses adaptive annotation contrast. |
| G3 Figure 4 signal axis | Resolved | Figure 4 labels dimensionless signal coefficient `s` and marks weak/noisy, localized, and strong rungs. |
| G4 Figure 3/8 sorting and labels | Resolved | Figure 3 uses descending regret with alphabetical tie-breaks; Figure 8 labels nonzero downgrade/failure segments. |
| G5 Figure 4/7 rendering artifacts | Resolved | Figure 7 labels are stripped of trailing hyphens; Figure 4 uses a legend and guide labels. |
| H1 Artifact accessibility | Release-polish tracked | Data and Code Availability names reviewer-access archive, public repository, DOI placeholders, and the required archive contents. |

## Command Evidence

| Check | Command / artifact | Result |
|---|---|---|
| Manuscript table rebuild | `python scripts\build_contextgate_manuscript_tables.py --output-dir manuscript\tables` | Passed; 41 generated table families; all claim-source, no-harm, benchmark-matrix, robustness, expanded-table, calibration, FCR, gate, threshold, metric-definition, dataset-scope, method-scope, disaggregation, and stress-accounting validations passed. |
| Publication figure rebuild | `python scripts\build_contextgate_publication_figures.py` | Passed; regenerated 10 curated PNG/PDF/EPS figure families. |
| LaTeX compile | Bundled Tectonic into `manuscript/build_cp_q8_8l/` | Passed; wrote 47-page `contextgate_bench_elsevier_template.pdf`. Remaining warnings are nonfatal draft hbox/fontconfig warnings, not missing references. |
| PDF render | `pdftoppm -png -r 120 manuscript/build_cp_q8_8l/contextgate_bench_elsevier_template.pdf tmp/pdfs/cp_q8_8l/pages/page` | Passed; rendered all 47 pages. |
| PDF visual QA | Contact sheets in `tmp/pdfs/cp_q8_8l/contact_sheets/` | Passed visual inspection for all page contact sheets and the regenerated figure sheet. |
| Citation/ref/stale-wording audit | Regex audit over TeX and `pdftotext` output | Passed; no missing citation markers, no LaTeX reference warnings, scoped title/abstract wording present, no stale `predictive transcriptomic models`, no stale `intended for release`, and no stale `11 datasets`; 11 figure/table labels, 19 refs, 0 uncited labels. |
| Unit/integration tests | `python -m pytest -q` | Passed with the existing one skipped opt-in Modal integration test. |
| Live Modal smoke | `RUN_MODAL_TESTS=1 python -m pytest tests/integration/test_modal_live_smoke.py -q -rs` | Passed; CP-Q5 live Modal smoke returned success through pytest. |
| Lint | `python -m ruff check src scripts tests modal` | Passed. `scripts/build_contextgate_manuscript_tables.py` now has a file-level E501 exemption because it stores long publication-facing prose constants. |
| Python compile check | `python -m compileall -q src scripts tests modal` | Passed. |
| Diff hygiene | `git diff --check` | Passed. |

## Modal Decision

The live Modal smoke test passed and is recorded as a deployment/entrypoint
health check. It is not a Level 4 bounded refresh and not a Level 5 full matrix
rerun. No CP-Q8.8A-L change modifies route logic, thresholds, benchmark matrix
semantics, metric definitions, registered cloud entrypoints, or source data
contracts in a way that would require a bounded or full Modal rerun.

## Stop Rule

CP-Q8.8 is closed. No active Level 4 or Level 5 trigger remains after the local
validation suite and live Modal smoke test.

Remaining work is final release polish rather than hidden methodological review
debt:

- replace the graphical abstract placeholder;
- replace the architecture placeholder;
- complete author/affiliation metadata;
- complete acknowledgements;
- normalize references to the journal style;
- perform the final human editorial rewrite and source-by-source reference
  check;
- insert the reviewer-access archive link, public GitHub URL, and archival DOI
  before submission.
