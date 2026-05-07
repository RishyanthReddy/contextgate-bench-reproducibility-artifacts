# Method Card: Always True-Neighbor Context

## Registry

- `method_id`: `always_true_neighbor_mean`
- `method_family`: `always_true_neighbor_context`
- Primary role: positive context reference and overuse-context comparator.
- Code pointers:
  - `src/cellpack/models/baselines.py`
  - `src/cellpack/graph/spatial_graph.py`
  - `src/cellpack/method_comparison.py`
  - `src/cellpack/benchmark_matrix.py`

## Scientific Purpose

This baseline tests what happens if a method always consumes physical neighbor
context. It is intentionally permissive: it can capture real local signal, but
it also exposes false-context risk when neighbor use is not justified.

## Inputs

- Center unit expression `x_i`.
- True spatial neighbor graph from k-nearest or radius graph construction.
- Neighbor expression vectors `x_j` for graph neighbors of unit `i`.
- Standard unit, gene, split, and expression contracts.

## Graph Construction

Default true-neighbor graph:

- k-nearest neighbors with `k=5`;
- grouped inside `sample_id` and `slide_id`;
- uses `x,y` centroids;
- excludes the center unit itself;
- sorts ties by distance then `unit_id`;
- writes distance bins using `20`, `75`, and `150` coordinate-unit edges.

## Feature Construction

For expression prediction, the neighbor feature is the mean expression vector
over true-neighbor units:

`mean_j x_j`, where `j` belongs to the true-neighbor set of center unit `i`.

For CP-Q route-level comparison, the method predicts `full_context` for every
row regardless of evidence.

## Scoring / Training Procedure

No learned model is trained in this baseline. It is deterministic given the
graph and expression matrix.

Route-level behavior:

- `predicted_route = full_context`
- confidence `0.95`
- reason: always use true-neighbor context.

## Hyperparameters

- `k = 5` for default kNN graphs.
- Group columns: `sample_id`, `slide_id`.
- Coordinate columns: `x`, `y`.
- QC filtering: uses `qc_pass` when present.

## Splits

The graph is constructed within spatial groups, then metrics are evaluated
under the registered split. For held-out split evaluation, the method must not
use labels or target outcomes from held-out groups when computing any fitted
statistics.

## Output Metrics

- context-use rate;
- false-positive context rate;
- no-harm rate;
- utility and regret against oracle route;
- paired deltas versus expression-only;
- expression prediction error for CP-3/CP-4-style prediction tables.

## Failure / Skip Conditions

- Missing coordinates.
- Fewer than two valid units within a graph group.
- Missing neighbor expression rows.
- Missing or invalid graph schema.

## Interpretation Rule

This baseline is not evidence that context should be used. It is a stress
reference: if it performs well only in positive controls and poorly under
wrong-context or real-data gates, the benchmark has evidence against
unconditional context use.

