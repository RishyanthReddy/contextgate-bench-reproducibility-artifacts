# Method Card: Graph-Style Context Aggregation

## Registry

- `method_id`: `lightweight_graphsage_aggregation`
- `method_family`: `gnn_style_context_aggregation`
- Primary role: lightweight graph-neighborhood comparator.
- Code pointers:
  - `src/cellpack/method_comparison.py`
  - `src/cellpack/positive_control_ladder.py`
  - `src/cellpack/benchmark_matrix.py`
  - `src/cellpack/graph/spatial_graph.py`

## Scientific Purpose

This method family represents simple message-passing or GraphSAGE-style
aggregation. It asks whether aggregating spatial neighbors adds utility beyond
center expression and whether such gain survives wrong-context controls.

## Inputs

- Center expression vector `x_i`.
- Neighbor expression vectors `x_j` from true or control graphs.
- Optional graph edge metadata: distance, rank, distance bin.
- Dataset/task/split metadata and context-utility score.

## Feature Construction

The conceptual GraphSAGE-style feature is:

`h_i = concat(x_i, aggregate({x_j: j in N(i)}))`

where the current bounded implementation uses mean-style neighborhood evidence
and route-level context-utility summaries rather than training a deep graph
network for every CP-Q6 matrix row.

For the CP-Q2 route-level comparator, graph aggregation predicts:

- `full_context` if `gene_count >= 900` and `context_utility_score > 0.01`;
- otherwise `abstain_uncertain`.

## Scoring / Training Procedure

The current CP-Q implementation is a lightweight benchmark proxy, not a full
multi-layer trainable GraphSAGE model. It consumes registered evidence profiles
and emits route/utility metrics in the shared schema.

In positive/null-control testing, the family can recover strong injected
neighbor signal but should abstain or fail specificity under missing-panel and
confounded controls.

## Hyperparameters

- Gene-count gate: `900`.
- Context utility threshold: `0.01`.
- Default graph: true kNN with `k=5`.
- CP-Q matrix seeds: `0,1,2`.
- Current route confidence:
  - context route: `0.68`;
  - abstain route: `0.58`.

## Splits

Evaluated under the same split registry as other methods. The strongest claims
require FOV, sample/section, donor, or dataset holdout. Random unit splits are
not sufficient for strong spatial claims because nearby cells can leak local
tissue state.

## Output Metrics

- utility and regret;
- no-harm rate;
- false-positive context rate;
- abstention rate;
- paired deltas versus expression-only and always-context;
- positive/null-control sensitivity and specificity when evaluated in CP-Q3.

## Failure / Skip Conditions

- Missing graph.
- Missing expression matrix.
- Gene panel below the current evidence gate.
- No measurable context-utility score.
- Control graph unavailable for task/control combinations that require it.

## Interpretation Rule

This card should be described as a lightweight graph-style comparator. It is
not a claim that ContextGate-Bench has benchmarked every modern high-capacity
GNN or graph transformer. CP-Q8.6H decides whether any additional SOTA replay is
feasible.

