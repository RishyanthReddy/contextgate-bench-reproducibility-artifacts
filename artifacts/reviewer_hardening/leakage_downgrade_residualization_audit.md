# CP-Q8.6F Leakage, Downgrade, And Residualization Audit

> Reviewer-facing audit for leakage/confounding flags, downgrade reasons, and
> residualization assumptions.
>
> Status: CP-Q8.6F.

---

## Purpose

This audit makes three parts of ContextGate-Bench explicit:

1. how the leakage-audit pass gate is represented by `\ell_i`;
2. how downgrade reason `d_i` is assigned from failure classes and reason codes;
3. how residualization is interpreted when comparing context-aware methods with
   expression-only baselines.

The goal is not to prove that every possible leakage mode has been eliminated
from every public dataset. The goal is to make the benchmark's conservative
claim boundary reproducible: rows with known confounding, missing observability,
unreplicated signal, or residual evidence that does not beat expression-only are
blocked from `context_allowed`.

Generated supplement tables:

- `manuscript/tables/supp_table_s21_leakage_confounding_examples.*`
- `manuscript/tables/supp_table_s22_downgrade_examples.*`
- `manuscript/tables/supp_table_s23_residualization_audit.*`

---

## Leakage And Confounding Gate `\ell_i`

In the manuscript, `\ell_i` is a conservative pass gate: `\ell_i = 1` means the
row passes the registered evidence-isolation audit, while `\ell_i = 0` would
indicate a direct leakage failure. It is not a catch-all synonym for every
confounding or downgrade class. FOV/sample artifacts, synthetic confounds, and
unreplicated train-only biological hints are represented through wrong-context,
held-out replication, and downgrade gates.

Concrete examples appear in Supplementary Table S21, and the full gate counts
now appear in Supplementary Table S25:

- **FOV/sample-confounded synthetic signal:** 12 ContextGate rows route to
  `abstain_uncertain` instead of a spatial-neighbor claim.
- **Observed artifact/confound abstention:** real-data evidence carrying
  artifact or unreplicated-label failure classes is blocked from
  `context_allowed`.
- **Wrong-context control pressure:** control-ablation rows show that
  always-context comparators can retain high false-context behavior, with a
  maximum comparator false-context rate of 0.660 under the registered
  ablation table.
- **Unit-hash split alone:** unit-level splits are represented, but they are
  insufficient for a strict context claim unless held-out FOV/sample/donor or
  equivalent replication evidence also supports the row.
- **Held-out biological outcome not replicated:** candidate context evidence
  that does not replicate is downgraded rather than promoted from train-only
  evidence.

In the current CP-Q5 decision table, no row has `leakage_audit_passed = false`.
That is itself reported in Supplementary Table S25: the leakage-audit gate has
0 failures among the 63 non-positive-control decisions. The dominant blockers
are residual direction, FDR/power, held-out replication, wrong-context
separation, and explicit downgrade reasons.

This framing directly addresses the reviewer concern that split-aware language
was too abstract. The implementation does not ask readers to trust a single
sentence about leakage prevention; it exposes the cases, counts, and artifact
pointers.

---

## Downgrade Reason `d_i`

Downgrade reason `d_i` is derived from the failure taxonomy. Supplementary Table
S22 maps representative examples to the downgrade used in the claim audit:

| Failure class | Downgrade meaning |
|---|---|
| `panel_lacks_downstream_genes` | Panel or target observability is insufficient for a broad LR/pathway claim. |
| `labels_not_replicated` | Candidate context signal does not support held-out or donor-generalized claims. |
| `expression_absorbs_signal` | Expression-only is the safer route because residual context gain is unsupported. |
| `fov_or_sample_artifact` | No physical-neighbor claim is allowed without wrong-context and held-out controls. |
| `lr_without_downstream_response` | Measured ligand-receptor proximity is not downstream transcriptional response. |
| `insufficient_power` | Evidence remains abstention-level until more units, samples, or replicates exist. |
| `access_or_schema_blocker` | Dataset remains in the rejected/access ledger only. |

The table also includes counterexamples:

- `positive_control_only` when synthetic neighbor signal is detected;
- `abstain_uncertain` when null or confounded controls are rejected.

These counterexamples matter because they show the router is not simply a
machine for negative conclusions. It permits mechanics-only signal detection
while still blocking real-data biology claims that lack the full evidence
contract.

---

## Residualization Contract

Residualization asks a simple question:

> After center/expression-only information is used, does spatial neighbor
> context explain additional target signal under matched controls?

Supplementary Table S23 documents the residualization assumptions:

- **Expression-only baseline:** uses center/unmasked expression only and no
  neighbor tokens. This defines what the central cell already explains.
- **ContextGate residual delta:** measures routed context contribution beyond
  expression-only evidence.
- **Always-context comparator:** tests the cost of spending true-neighbor
  context on every row.
- **Wrong-context residual controls:** distinguish physical-neighbor evidence
  from random, coordinate-shuffled, or distant-neighbor artifacts.
- **Residual claim boundary:** residual hints are not promoted into biological
  claims unless strict route gates pass.

The residualization design is fair to context models because it does not ask
them to beat a straw baseline. It asks whether context explains what expression
alone misses. The design is also intentionally cautious: if expression-only
absorbs the target, if wrong-context controls behave similarly, or if the
residual delta is nonpositive, the correct route is expression-only or
abstention.

---

## Statistical Caveats

Residualization can still be misspecified:

- a weak expression-only baseline can make context look artificially helpful;
- an overly flexible expression-only baseline can absorb genuine neighbor
  effects;
- target genes may be missing from targeted panels;
- downstream pathway response may be delayed, unmeasured, or cell-type
  restricted;
- conditioning on center expression can introduce collider-style complications
  when center state is both a consequence of prior signaling and a predictor of
  current target expression.

These caveats do not invalidate the benchmark. They define the manuscript's
claim boundary: ContextGate-Bench is a reproducible decision framework for when
context is supported, misleading, or insufficiently evidenced in the available
data. It is not a universal biological negation.

---

## Modal Decision

No new Modal run is required for CP-Q8.6F. The audit is generated from existing
registered CP-Q4, CP-Q5, CP-Q6, and CP-Q7 artifacts. Modal would be required
only if the leakage logic, residual target construction, or benchmark semantics
changed; CP-Q8.6F changes only the reviewer-facing audit tables and
documentation.
