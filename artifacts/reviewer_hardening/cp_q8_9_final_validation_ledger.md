# CP-Q8.9 Final Validation Ledger

Date: 2026-05-07

Scope: final integration check for the CP-Q8.9 new-analysis minor-issue sweep
covering A1, B1-B12, C1-C9, D1, and E1-E3.

Linear issue: RIS-15 / CP-Q8.9J.

## Validation Summary

Status: PASS.

All 26 review items are patched, limitation-resolved, or release-deferred for
non-method submission packaging reasons. The manuscript compiles, the PDF
renders, the route-count and tier-scope text audits pass, and the bounded Modal
smoke returned `status: pass`.

## Local Artifact Rebuilds

| Check | Command | Result |
|---|---|---|
| Manuscript tables | `python scripts\build_contextgate_manuscript_tables.py --output-dir manuscript\tables` | PASS; 47 tables generated from registered artifacts. |
| Publication figures | `python scripts\build_contextgate_publication_figures.py --output-dir manuscript\figures\singles` | PASS; figure artifacts regenerated from existing local artifacts. |
| Unit tests | `python -m pytest tests\unit -q` | PASS; unit suite completed with only the existing pytest-asyncio warning. |
| Ruff | `python -m ruff check src scripts tests modal` | PASS. |
| Compileall | `python -m compileall -q src scripts tests modal` | PASS. |
| Git whitespace check | `git diff --check` | PASS. |
| LaTeX compile | `tectonic --outdir manuscript\build_cp_q8_9 manuscript\contextgate_bench_elsevier_template.tex` | PASS; PDF emitted to `manuscript\build_cp_q8_9\contextgate_bench_elsevier_template.pdf`. |
| PDF render | `pdftoppm -png -r 120 manuscript\build_cp_q8_9\contextgate_bench_elsevier_template.pdf tmp\pdfs\cp_q8_9_final_rerender\page` | PASS; 50 rendered pages. |

## PDF QA

Rendered contact sheets:

- `tmp\pdfs\cp_q8_9_final_rerender\contact_sheet_pages_01.png`
- `tmp\pdfs\cp_q8_9_final_rerender\contact_sheet_pages_02.png`
- `tmp\pdfs\cp_q8_9_final_rerender\contact_sheet_pages_03.png`
- `tmp\pdfs\cp_q8_9_final_rerender\contact_sheet_pages_04.png`
- `tmp\pdfs\cp_q8_9_final_rerender\contact_sheet_pages_05.png`

Visual findings:

- PASS: Table 3 now appears in the Results section before the failure-taxonomy
  discussion and before the references.
- PASS: Figure 2, Figure 3, Figure 4, Figure 5, Figure 6, Figure 7, and
  Figure 8 render in sequence with captions.
- PASS: Figure 4 weak/noisy rung is on the labeled x-axis.
- PASS: Figure 2 caption includes CP-Q6 q1 scope and metric polarity wording.
- RELEASE-DEFERRED: graphical abstract and draw.io architecture figure remain
  explicit submission-packaging placeholders, as recorded in the manuscript's
  Release-Readiness Placeholders section.

## Text Audit

| Audit target | Result |
|---|---|
| No stale 36/37 inconsistency | PASS; manuscript states 37 positive-control-only decisions as 36 CP-Q3 target-observable synthetic positive rows plus one CP-R1 synthetic-mechanics-only row. |
| CP-Q/CP-R labels defined | PASS; Methods includes a tier-label glossary and captions point readers to S29/S37 where relevant. |
| No unqualified `0 context_allowed` claim | PASS; abstract, Table 3, and conclusion scope the zero count to registered targeted-panel imaging datasets and registered lightweight method families. |
| Figure 2 false-context mismatch | PASS; Section 4.2 distinguishes CP-Q2 route-comparison values from Figure 2's CP-Q6 q1 all-row exposure cells. |
| Keywords align with final claim | PASS; keywords now foreground benchmark, decision framework, null routing, and reproducibility rather than claiming detected real-data cell-cell communication. |

## Modal Smoke

Command:

```powershell
$env:PYTHONIOENCODING='utf-8'; $env:PYTHONUTF8='1'; python -m modal run scripts/pipeline_modal_smoke.py::pipeline_modal_smoke --dataset xenium_breast_v1 --input-label loader_smoke --output-label cp_q8_9j_mu64_mg64_k5_steps2 --max-units 64 --max-genes 64 --k 5 --train-steps 2 --seed 17
```

Result: PASS.

- Modal app URL:
  `https://modal.com/apps/rishyanthreddy101/main/ap-txI99ZObBurTXUfNDMptET`
- Dataset: `xenium_breast_v1`
- Output label: `cp_q8_9j_mu64_mg64_k5_steps2`
- Unit count: 64
- Gene count: 64
- k: 5
- Train steps: 2
- Runtime: 1.2959 seconds reported by the smoke payload
- Status: `pass`
- Local registry update: `data/manifests/artifact_registry.yaml` now records
  the EC-MODAL-01 smoke artifacts and checksums for the output label above.

The first Modal invocation failed before job submission because Windows console
encoding could not print Modal's checkmark character. The rerun forced UTF-8
and completed successfully.

## Stop-Rule Status

No active Level 4 or Level 5 trigger remains.

- No route logic changed.
- No ContextGate threshold changed.
- No CP-Q6 matrix semantics changed.
- No metric definition changed after the local artifact rebuilds.
- The bounded Modal smoke was confirmatory and did not replace the registered
  CP-Q2/CP-Q3/CP-Q6 source artifacts.

## Remaining Release Packaging

These are submission-packaging items, not CP-Q8.9 method blockers:

- Replace the graphical abstract placeholder.
- Replace the draw.io architecture figure placeholder.
- Normalize references to the target journal's final style.
- Complete author affiliations and acknowledgements.
- Insert the reviewer-access URL, GitHub URL, and DOI before submission.
