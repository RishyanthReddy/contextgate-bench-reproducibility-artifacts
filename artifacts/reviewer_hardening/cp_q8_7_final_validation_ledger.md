# CP-Q8.7 Final Validation Ledger and Stop Rule

Date: 2026-05-05

Scope: final closure record for the Paper-Wizard consistency and
claim-hardening pass. This ledger closes CP-Q8.7A-I and records the remaining
items that are deliberately deferred to final release polish rather than
methodological revision.

## Claim Boundary

The manuscript now states the central result as a benchmark-defined decision:
under the pre-specified ContextGate gates, no real-data setting was routed to
`context_allowed`. This is not an independent proof that tumor neighborhoods
lack biology. It means that, for the registered public datasets, tasks, panels,
controls, splits, thresholds, and artifacts, the evidence was not sufficient to
publish a strong biological context-benefit claim.

## Paper-Wizard Issue Closure

| Issue | Status | Manuscript / Artifact Resolution | Modal Rerun Level |
|---|---|---|---|
| D1 route independence | Resolved with explicit claim boundary; independent real-data adjudication deferred to future work | Abstract, Section 4.4, Limitations, Conclusion, Data and Code Availability, `paper_wizard_literature_concordance_audit.*`, and `cp_q8_7_paper_wizard_issue_ledger.md` now distinguish ContextGate-defined real-data route decisions from externally anchored synthetic and wrong-context controls. | Level 1 prose/supplement patch |
| D2 leakage-audit gate | Resolved | Section 3.5/3.6 defines `ell_i=1` as the leakage-audit pass state from `leakage_audit_passed`; Supplementary Table S25 decomposes non-positive-control decisions and reports zero leakage-audit failures. | Level 2 local derived-table rebuild |
| D3 LR/pathway and graph specification | Resolved | Section 3.4 specifies the frozen ligand-receptor source, observability gates, neighbor-ligand aggregation, receptor/module residual targets, kNN graph construction, graph metadata, mean-neighbor aggregation, thresholds, confidence values, and method-card pointers. | Level 1 prose/specification patch |
| D4 stratified FCR denominator | Resolved | Supplementary Table S24 separates real explicit negative-context rows, unsupported/abstention rows, all-row exposure, positive controls, synthetic null rows, panel/dropout rows, and FOV-confounded rows. Table 3 and captions now distinguish all-row exposure from null-denominator FCR. | Level 2 local derived-table rebuild |
| D5 threshold sensitivity | Resolved | Supplementary Table S26 reports registered conservative, moderate reviewer-stress, and permissive exploratory operating points plus axis-level sensitivity. Section 4.6 states that zero `context_allowed` routes persist across the tested operating region. | Level 2 local derived-table rebuild |
| E1 always-context FCR inconsistency | Resolved | `paper_wizard_metric_consistency_audit.md`, S24, Table 3, and Figure 2 caption clarify that `0.4783` is the CP-Q2 all-row false-context flag mean, while null-denominator always-context FCR is `1.000`. | Level 2 local audit/rebuild |
| E2 gate-by-gate failure decomposition | Resolved | Supplementary Table S25 and Section 4.4 report residual, FDR/effect, wrong-context, held-out, leakage-audit, and downgrade gate failures for all non-positive-control decisions. | Level 2 local derived-table rebuild |
| E3 oracle-regret consistency | Resolved | `paper_wizard_metric_consistency_audit.md` and revised Figure 2/Figure 3 captions separate CP-Q6 full-tier aggregate metrics from CP-Q2 method-comparison oracle regret. | Level 2 local audit/rebuild |
| E4 expression-only comparator | Resolved | S24, Table 3, Section 4.2, and Section 4.5 state that expression-only also has FCR `0.000`; ContextGate's added value is retaining positive-control sensitivity and auditable abstention rather than real-data differential FCR in the current datasets. | Level 2 local table/prose rebuild |
| H1 artifact accessibility | Partially resolved; final URL/DOI deferred for release polish | Data and Code Availability now requires reviewer-accessible repository/archive access before submission and maps code, schemas, tables, figures, and reviewer-hardening artifacts. Public GitHub/Zenodo URL insertion remains a non-methodological release-polish item. | Level 1 prose/release-prep patch |

## Command Evidence

| Check | Command / Artifact | Result |
|---|---|---|
| Manuscript table rebuild | `python scripts\build_contextgate_manuscript_tables.py` | Passed; 31 generated table families; claim-source, no-harm, benchmark-matrix, robustness, S24, S25, and S26 gates passed. |
| Publication figure rebuild | `python scripts\build_contextgate_publication_figures.py` | Passed; regenerated the curated 10 PNG/PDF/EPS figure set with deterministic export metadata. |
| LaTeX compile | `tectonic.exe --outdir build_cp_q8_7 contextgate_bench_elsevier_template.tex` from `manuscript/` | Passed; wrote `manuscript/build_cp_q8_7/contextgate_bench_elsevier_template.pdf`. Warnings are draft hbox/fontconfig warnings, not missing references or fatal build errors. |
| PDF page render | `pdftoppm -png -r 120 manuscript\build_cp_q8_7\contextgate_bench_elsevier_template.pdf manuscript\build_cp_q8_7\render_cp_q8_7i_pages\page` | Passed; rendered 40 pages. |
| PDF visual QA | Contact sheets in `manuscript/build_cp_q8_7/contact_sheets_cp_q8_7i/` | Passed visual inspection for all 40 manuscript pages and both publication-figure contact sheets. Intentional draw.io graphical abstract and architecture placeholders remain. |
| Citation/ref/stale-wording audit | Python `pypdf`/regex audit over the TeX, figure manifest, table/text evidence JSON, and compiled PDF | Passed; 40 pages, 74 cited keys, 74 bibliography entries, no missing citations, no missing corrected caption tokens, no stale journal-tier or `Modal-executed` wording. |
| Unit/integration tests | `python -m pytest -q` | Passed with the existing one skipped test. |
| Lint | `python -m ruff check src scripts tests modal` | Passed. |
| Python compile check | `python -m compileall -q src scripts tests modal` | Passed. |

## Modal Rerun Decision

No active Level 4 or Level 5 Modal rerun trigger remains.

| CP-Q8.7 Card | Rerun Level | Reason |
|---|---|---|
| CP-Q8.7A | Level 1 | Issue ledger and claim-boundary planning only. |
| CP-Q8.7B | Level 2 | Metric values were reproducible from registered artifacts; denominator/scope labeling was corrected locally. |
| CP-Q8.7C | Level 2 | Stratified FCR and expression-only comparator tables were derived from CP-Q2, CP-Q3, and CP-Q5 artifacts. |
| CP-Q8.7D | Level 2 | Gate decomposition used existing CP-Q5 gate columns. |
| CP-Q8.7E | Level 2 | Threshold operating points used existing CP-Q7, CP-Q5, CP-Q6, and CP-Q3 artifacts. |
| CP-Q8.7F | Level 1 | Method specification prose and method-card pointers only. |
| CP-Q8.7G | Level 1 | Claim language and reviewer-hardening notes only. |
| CP-Q8.7H | Level 2 | Tables, figures, captions, compile, and visual QA rebuilt from registered artifacts. |
| CP-Q8.7I | Level 1 | Final ledger, stop-rule record, and local validation closure only. |

Because CP-Q8.7 changed documentation, derived tables, captions, figures, and
claim boundaries without changing benchmark entrypoints, thresholds, route
logic, or registered CP-Q6 matrix semantics, a live Modal refresh would not add
new evidentiary value for this pass.

## Stop Rule

CP-Q8.7 is closed. The next task may return to CP-Q8 final release polish.

Remaining deferred items are non-methodological release-polish work:

- normalize final Elsevier reference formatting;
- complete Elsevier formatting and author/affiliation metadata;
- insert the public GitHub, reviewer-access, or DOI link before submission;
- replace draw.io graphical abstract and architecture placeholders with final
  professional artwork;
- perform the user's final human rewrite and source-by-source reference check.
