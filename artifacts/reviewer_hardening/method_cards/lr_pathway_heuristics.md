# Method Card: Ligand-Receptor and Pathway Heuristics

## Registry

- `method_id`: `ligand_receptor_pathway_heuristic`
- `method_family`: `ligand_receptor_or_pathway_heuristic`
- Primary role: biologically motivated context heuristic.
- Code pointers:
  - `src/cellpack/method_comparison.py`
  - `src/cellpack/positive_control_ladder.py`
  - `src/cellpack/evaluation/ligand_receptor.py`
  - `src/cellpack/evaluation/biology_triage.py`

## Scientific Purpose

This heuristic tests whether neighbor context is supported by measured
ligand-receptor pairs or downstream pathway/module targets. It is intentionally
stricter than a generic context score because a spatial claim should be
observable in the measured panel.

## Inputs

- Center/receiver expression vector.
- True-neighbor or control-neighbor expression vectors.
- Frozen ligand-receptor pair list.
- Curated downstream pathway/module target sets.
- Available-pair count and available-module-target count from run metadata.
- Context-utility score and evidence class.

## Target Definition

For LR tasks, the target is receiver receptor expression or the residual
component of receiver receptor expression unexplained by center-only features.

For pathway/module tasks, the target is the residual activity or expression of
downstream module genes inside the receiver/center unit.

All LR/pathway claims remain association-level and do not imply causal
signaling.

## Feature Construction

For each center unit:

1. Identify neighbor units from the selected graph.
2. Aggregate ligand expression over neighbors for measured ligands.
3. Match those ligands to measured receiver receptors or downstream modules.
4. Compare true-neighbor scores against random, coordinate-shuffled, and
   distant controls.
5. Residual tasks subtract or condition on center-only expression before asking
   whether neighbor context explains remaining target variation.

## Decision Rule

Current CP-Q2 route-level rule:

- require `available_pair_count >= 4` or `available_module_target_count >= 4`;
- if coverage passes and `context_utility_score > 0.01`, predict
  `full_context`;
- if coverage passes but score is not positive, predict `expression_only`;
- if coverage fails, predict `abstain_uncertain`.

Confidence values:

- context or expression route with sufficient coverage: `0.70`;
- abstention from insufficient coverage: `0.60`.

## Hyperparameters

- LR pair threshold: `4`.
- Module target threshold: `4`.
- Expression-low context threshold: `0.01`.
- Controls required for strict claims: random, coordinate-shuffled, and distant
  where feasible.

## Splits

Preferred splits are FOV, sample/section, patient/donor, or dataset holdout
when metadata supports them. Random unit splits are weaker and must be marked
accordingly in claim scope.

## Output Metrics

- residual delta versus expression-only;
- FDR-adjusted p-value or q-value proxy;
- standardized effect size;
- replication rate under held-out splits;
- false-positive context rate against wrong-context controls;
- utility/regret route metrics in CP-Q2/CP-Q6.

## Failure / Skip Conditions

- Fewer than four measured LR pairs and fewer than four measured module targets.
- Target receptor or downstream genes missing from the panel.
- Controls unavailable.
- Labels or sample metadata insufficient for held-out validation.

## Interpretation Rule

If the heuristic abstains because panel targets are missing, the correct claim
is panel observability failure, not absence of biological communication.

