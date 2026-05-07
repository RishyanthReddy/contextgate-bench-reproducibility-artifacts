# Method Card: Wrong-Context Controls

## Registry

This card covers three registered wrong-context method families:

| Method ID | Family | Control Strategy |
|---|---|---|
| `random_neighbor_control_model` | `wrong_context_random_neighbor` | random same-slide context |
| `coordinate_shuffled_control_model` | `wrong_context_coordinate_shuffled` | coordinates permuted before neighbor construction |
| `distant_neighbor_control_model` | `wrong_context_distant_neighbor` | far units, same type where labels permit |

Code pointers:

- `src/cellpack/graph/control_graph.py`
- `src/cellpack/method_comparison.py`
- `src/cellpack/positive_control_ladder.py`
- `src/cellpack/benchmark_matrix.py`

## Scientific Purpose

Wrong-context controls test whether apparent spatial gains are caused by true
physical neighborhoods or by easier shortcuts such as cell-type composition,
sample/FOV artifacts, expression distribution, or any extra context tokens.

## Inputs

- `unit_table` with coordinates and group IDs.
- Optional `cell_type` or marker-rule label for same-type distant matching.
- Expression matrix and gene vocabulary.
- Registered split assignments.

## Control Graph Construction

### Random Same-Slide

For each center unit, choose `k=5` non-self units from the same graph group.
Candidates are sorted by a stable MD5 digest using the configured seed, not by
physical distance.

### Coordinate-Shuffled

Coordinates are deterministically permuted within group before neighbor
selection. The graph keeps unit identities but breaks the physical
coordinate-to-expression relationship.

### Distant Same-Type

For each center unit, candidate neighbors are sorted by decreasing true
distance. If a cell-type column exists and same-type candidates exist, the
method prefers same-type distant units; otherwise it falls back to distant
units when configured to allow fallback.

## Feature Construction

Wrong-context methods consume the same expression features and context shape as
true-neighbor methods, but the neighbor IDs come from the corresponding control
graph. This keeps capacity and input dimensionality comparable while breaking
the biological interpretation.

## Scoring / Training Procedure

In CP-Q2 route-level comparison, wrong-context methods predict `full_context`
with confidence `0.80`, with the prediction reason describing the control
family. In CP-Q3 positive/null controls, wrong-context methods can recover some
signal weakly but are expected to fail specificity under null or confounded
settings if they overuse context.

## Hyperparameters

- `k = 5`.
- Control seed: `13` for graph construction, CP-Q seeds `0,1,2` for matrix
  rows.
- Group columns: `sample_id`, `slide_id`.
- Coordinate columns: `x`, `y`.
- Distance bins: `<=20`, `<=75`, `<=150`, `>150`.

## Splits

Controls are evaluated under the same split IDs as the corresponding
true-neighbor jobs. Split leakage must be interpreted relative to the same
unit/FOV/sample/donor boundaries used by true-neighbor methods.

## Output Metrics

- false-positive context rate;
- no-harm rate;
- utility and regret against oracle;
- paired deltas versus expression-only and always-true-neighbor context;
- skip reason rate when a control graph is infeasible.

## Failure / Skip Conditions

- Missing coordinates.
- Missing graph group columns.
- Fewer than two units in a group.
- Distant same-type control cannot be formed and fallback is disabled.
- Placeholder labels when a same-type distant interpretation is required.

## Interpretation Rule

A context gain that also appears under wrong-context controls is not counted as
spatial biological evidence. It becomes a downgrade candidate for artifact,
confounding, or non-specific context capacity.

