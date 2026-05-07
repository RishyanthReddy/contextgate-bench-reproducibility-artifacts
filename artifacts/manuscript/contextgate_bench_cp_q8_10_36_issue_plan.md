# CP-Q8.10 Reviewer Hardening Plan: 36 Minor Issues

Created: 2026-05-07

Scope: address the full 36-issue reviewer set covering abstract aggregation, Methods calibration, Results interpretation, Discussion/Conclusion framing, figure/table consistency, and reproducibility access. Linear project: `CP-Q8.10 reviewer hardening: 36 minor issues`.

## Workflow

1. Track every reviewer point as a Linear issue.
2. Apply manuscript and generator changes in coherent batches.
3. Regenerate affected supplementary tables and publication figures from scripts.
4. Compile the manuscript PDF and run targeted tests plus lint/whitespace checks.
5. Update Linear issue statuses as fixes are completed.
6. Commit and push the completed repair set.

## Issue Plan

### A1 - Abstract Route Decision Decomposition
Revise the abstract route-count sentence to state that the 100 decisions comprise 23 CP-R1 real-data rows, 72 CP-Q3 synthetic ladder rows, and 5 rejected/access-blocked dataset-card rows. Explicitly mark positive-control-only decisions as synthetic.

Deliverable: abstract wording that prevents readers from treating all 100 route decisions as real-data evidence.

### A2 - Abstract Qualification for Deferred GSE311609
Add a brief abstract qualifier noting that GSE311609 Xenium, the highest-replication deferred cohort with 41 samples and 27 donors, remains the priority replay needed to test whether null routing persists under stronger replication.

Deliverable: one concise abstract phrase or sentence aligned with Section 6.

### B2 - Joint Passage Probability for Six-Gate AND Structure
Add Methods or supplementary calibration text summarizing empirical positive-control joint passage and an approximate joint-gate passability rationale. Emphasize that marginal real-data gate rates are diagnostics, while positive controls demonstrate the conjunction can pass when registered signal is present.

Deliverable: Section 3.6 prose and, if needed, S38/S25 wording.

### B3 - External Verifiability of Threshold Pre-Specification
Update registration/release prose to distinguish internal registration from external timestamping. If a public repository is created or made available, insert the public URL and state that DOI/archival timestamp remains pending unless actually available.

Deliverable: Section 3.7 and Data Availability wording with an accessible repository URL or an honest pending DOI statement.

### B4 - Multiple-Testing Correction Scope
Clarify that within-split BH screens do not control FDR for the aggregate 40/63 diagnostic count. Frame the count as descriptive and not globally/hierarchically FDR-controlled.

Deliverable: Section 3.6 wording and S27/S38 alignment.

### B5 - Spatial Autocorrelation and Anti-Conservative FDR
Add quantitative context or bounding language for spatial autocorrelation. If no fold-level ICC calculation is locally available, state this as a limitation and refer to future block-permutation/effective-sample-size replay.

Deliverable: Section 3.6 limitation prose and possible S36/S38 note.

### B6 - Quantitative Grounding of Operating Thresholds
Add a compact threshold rationale for FCR, route recovery, sensitivity, and specificity. Frame values as expert-elicited publication operating points unless a formal derivation exists.

Deliverable: Methods threshold paragraph and S38 rationale updates.

### B7 - LR Starter List Coverage and Threshold Grounding
Clarify that the 16-pair LR starter list is canonical and limited, not comprehensive cancer-specific coverage. State that score > 0.01 is a minimal registered screen without formal power grounding.

Deliverable: Section 3.4 wording and S37 cross-reference.

### B8 - Linear Ladder Mismatch with Nonlinear TME Signaling
Add a Discussion sentence connecting registered LR axes to nonlinear, threshold, distance-decay, and state-conditional future ladder rungs.

Deliverable: Section 5 forward-looking caveat.

### C1 - Spatial-Statistics Heuristic Real-Data Comparator Validity
Add calibration rationale for the 0.65 threshold and explicitly state that it exceeds all real-data scores, so real-data zero FCR for the heuristic is arithmetic rather than independent discrimination.

Deliverable: Section 3.4 and 4.2 wording.

### C2 - Define or Correct FDR Stress Value 0.343
Audit the source of "FDR stress value = 0.343". If it is actually CP-Q6 regret, correct the text. If it is a separate metric, define numerator, denominator, and row set.

Deliverable: Section 4.6 corrected metric language and S33/S38 consistency.

### C3 - CP-Q2 Method Metric Uncertainty
Report uncertainty for CP-Q2 metrics across 23 rows, or add a supplementary table if available from existing artifacts. At minimum, add bootstrap/Wilson guidance and note that fine ranking among shared-score policies is not statistically independent.

Deliverable: generated table update or explicit limitation in Section 4.2.

### C4 - Residual Context Utility Distribution
Add a distributional summary of Delta_i over non-positive-control rows: mean, median, range, and sign/subthreshold pattern if derivable. Link to S36/S32.

Deliverable: supplementary table or Section 4.4 text based on existing route artifacts.

### C5 - Always-Context Sensitivity Statement vs Figure 4
Revise Section 4.3 to state that Always-context is higher only under specific weaker/rung-averaged conditions, while ContextGate matches or exceeds it at the strong rung if Figure 4 shows that pattern.

Deliverable: corrected prose tied to Figure 4.

### C6 - Threshold Sensitivity Scope Relative to Binding Gate
Clarify that threshold sweeps do not vary the universally binding Delta_i > 0 sign gate. Reframe robustness as non-binding operating-point insensitivity plus residual-distribution evidence.

Deliverable: Section 4.6 wording.

### C7 - MDEs for Insufficient-Power Failure Class
Use existing S36 proxies where possible; if fold-level residual variance is unavailable, state that full MDE computation requires new serialization and add bounding language. Avoid overstating the "insufficient power" label.

Deliverable: Section 4.4 and S36 note update.

### C8 - Tautology of Always-Context FCR = 1.000
Add a parenthetical that always-context null FCR = 1.000 is definitional, and move empirical safety emphasis to wrong-context controls and null ladder behavior.

Deliverable: Section 4.2 wording.

### C9 - Multi-Gate Evidence vs Operative Binding Gate
Revise gate-decomposition discussion to distinguish operative routing (residual utility binds all rows) from descriptive marginal diagnostics (effect-control, replication, downgrade gates).

Deliverable: Section 4.4 wording and S25 interpretation if needed.

### C10 - Formal All-Row False-Context Exposure Metric
Add a formal Methods definition of all-row false-context exposure with all rows as denominator, distinct from null-denominator FCR in Equation 3.

Deliverable: Section 3.6 equation or prose definition and Figure 2 caption alignment.

### C11 - Positive-Control Signal Strength Calibration
Contextualize s = 0.55 against published LR/spatial co-expression effect-size ranges at a qualitative level, and state sensitivity applies to registered synthetic magnitudes only.

Deliverable: Section 4.3 and/or Section 6 wording.

### C12 - Shared CP-R1 Score Across Method Families
Add abstract and Section 4.2 qualifier that several compared families are threshold-policy variants over a shared CP-R1 evidence score, not independent algorithmic triangulation.

Deliverable: abstract and Section 4.2 headline/prose update.

### C13 - Xenium High-Plex Arm Contribution
Clarify that high-plex multi-sample evidence mainly comes from CosMx BCC 6K, while Xenium breast 5K contributes limited standalone route evidence due to skips and single-donor/FOV-only structure.

Deliverable: Section 4.4 panel-depth paragraph update.

### C14 - CellPack Input-Constraint Framing
Co-locate the CellPack input-ceiling caveat with any competitiveness claim in Results.

Deliverable: Section 4.2 wording.

### C15 - CP-Q2 Regret vs Full CP-Q6 Regret
Lead or immediately contextualize the CP-Q2 regret value with the CP-Q6 full-matrix aggregate regret, making CP-Q2 illustrative rather than general.

Deliverable: Section 4.2 narrative reorder.

### C16 - Positive-Control Floor Anchoring in Panel Observability
Add a compact reference to published spatial LR effect-size ranges or explicitly state that the s = 0.55 floor is not anchored to those ranges.

Deliverable: Section 4.4 or S39 update.

### C17 - In-Sample Oracle Caveat Placement
Move the in-sample oracle caveat to immediately accompany zero-regret language for the spatial-statistics heuristic.

Deliverable: Section 4.2 paragraph reorder.

### C18 - Main-Text Stratified Specificity Excluding Panel-Blocked Rows
Bring the S35 finding into Section 4.3: FCR remains 0.000 and mean specificity remains about 0.945 on strict null/confounded rows excluding panel-blocked positives.

Deliverable: Section 4.3 wording.

### D1 - Real-Data Conditional Routing Not Yet Demonstrated
Add Discussion sentence stating that context_allowed routing has not yet been exercised on real data in this benchmark, and the separation from never-context rests on synthetic positive-control recovery pending high-replication/whole-transcriptome replay.

Deliverable: Section 5 wording.

### D2 - Failure Classes Linked to Gate Criteria
Add Discussion mapping from dominant failure classes to Equation 5 gates: FOV/sample artifacts, insufficient power, panel coverage, label non-replication, and unresolved downgrades.

Deliverable: Section 5 operational mapping.

### E1 - Conclusion Scope Qualification
Qualify the conclusion's prescriptive sentence with the tested targeted-panel imaging scope and the separate normative basis from wrong-context/null-control evidence.

Deliverable: Section 7 wording.

### E2 - Consistent Normative vs Empirical Conditionality
Update the Introduction's final contribution sentence to mirror the Conclusion: conditionality is both a design rule and an observed uniformly non-context_allowed result for registered configurations.

Deliverable: Section 1 wording.

### F1 - Figure 2 No-Harm and False-Context Consistency
Audit Figure 2 metric denominators. Either align no-harm and false-context values or relabel/caption them as distinct denominators and add the Methods all-row exposure definition.

Deliverable: figure script/caption update and regenerated Figure 2 if needed.

### F2 - Replace Figure 1 Pipeline Placeholder
Replace the Figure 1 placeholder with a concrete architecture diagram showing dataset contract -> method/control matrix -> CP-R1 evidence -> ContextGate route -> claim release, with CP-Q/CP-R tiers labeled.

Deliverable: generated Figure 1 asset and manuscript figure block update.

### F3 - Figure 4 Linear X-Axis Scaling
Ensure Figure 4 uses a proportional continuous x-axis for s = 0.55, 0.75, and 1.00, rather than equidistant categorical positions.

Deliverable: figure script update and regenerated Figure 4.

### F4 - Figure 2 Colormap Directionality
Update Figure 2 so color desirability is easier to read, either by reversed colormaps for low-is-better metrics or explicit directional column labels/caption wording.

Deliverable: figure script/caption update and regenerated Figure 2 if needed.

### G1 - Repository Accessibility for Reproducibility
Provide an accessible repository link. The current GitHub repo is private; either make it public or create a public artifact repository and update Data and Code Availability with the active URL. Do not claim a DOI unless one is actually minted.

Deliverable: public GitHub URL in manuscript and README/release notes identifying included artifacts.

## Verification Checklist

- Regenerate supplementary tables with `python scripts/build_contextgate_manuscript_tables.py --output-dir manuscript/tables`.
- Regenerate figures with the repository figure-generation script.
- Run targeted unit tests for manuscript tables/figures.
- Run `python -m ruff check` on changed Python files.
- Run `git diff --check`.
- Compile the LaTeX manuscript with Tectonic.
- Confirm Linear issues are marked Done only after corresponding fixes and verification land.
