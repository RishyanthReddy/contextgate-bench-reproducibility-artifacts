# ContextGate-Bench Method Cards

> CP-Q8.6B reviewer-hardening supplement.
>
> These cards document the registered method families used by
> ContextGate-Bench. They are written for independent reimplementation and for
> manuscript reviewers who need to distinguish true model comparisons from
> benchmark-control and evidence-routing baselines.

---

## Scope

The CP-Q method suite is a benchmark-evaluation suite, not a claim that every
listed method is a full state-of-the-art trainable model. Some entries are
deterministic baselines, some are wrong-context controls, some are evidence
heuristics, and ContextGate is a transparent decision router. The tiny packed
context Transformer is a bounded capacity/smoke baseline, not a replacement for
large spatial foundation models.

All registered methods emit or are collapsed into the shared benchmark fields:

- `method_id`
- `method_family`
- `task_id`
- `dataset_id`
- `control_id`
- `split_id`
- `seed`
- `metric_family`
- `metric_value`
- `paired_delta_vs_expression`
- `paired_delta_vs_always_context`
- `false_positive_context_rate`
- `no_harm_rate`
- `abstention_rate`
- `regret_against_oracle`

Primary code pointers:

- `data/manifests/contextgate_benchmark_manifest.yaml`
- `src/cellpack/method_comparison.py`
- `src/cellpack/positive_control_ladder.py`
- `src/cellpack/contextgate.py`
- `src/cellpack/benchmark_matrix.py`
- `src/cellpack/models/baselines.py`
- `src/cellpack/models/cellpack_tiny.py`
- `src/cellpack/graph/spatial_graph.py`
- `src/cellpack/graph/control_graph.py`

---

## Card Inventory

| Method ID / Family | Card |
|---|---|
| `expression_only_linear` / `expression_only_or_center_only` | `expression_only_linear.md` |
| `always_true_neighbor_mean` / `always_true_neighbor_context` | `always_true_neighbor_mean.md` |
| `random_neighbor_control_model` / `wrong_context_random_neighbor` | `wrong_context_controls.md` |
| `coordinate_shuffled_control_model` / `wrong_context_coordinate_shuffled` | `wrong_context_controls.md` |
| `distant_neighbor_control_model` / `wrong_context_distant_neighbor` | `wrong_context_controls.md` |
| `spatial_statistics_heuristic` | `spatial_statistics_heuristic.md` |
| `ligand_receptor_pathway_heuristic` / `ligand_receptor_or_pathway_heuristic` | `lr_pathway_heuristics.md` |
| `lightweight_graphsage_aggregation` / `gnn_style_context_aggregation` | `graph_style_context_aggregation.md` |
| `cellpack_packed_context_tiny` / `cellpack_packed_context` | `tiny_packed_context_transformer.md` |
| `contextgate_transparent_router` | `contextgate_transparent_router.md` |
| oracle, true-neighbor reference, positive-control-only references | `oracle_positive_control_references.md` |

---

## Shared Data Contracts

All method cards assume the standard CellPack/ContextGate contracts:

- `unit_table`: one row per spatial unit with `unit_id`, `sample_id`,
  `slide_id`, `x`, `y`, optional `cell_type`, optional `qc_pass`.
- `gene_vocabulary`: one row per gene with `gene_index` and `gene_symbol`.
- `expression_matrix`: sparse unit x gene count or normalized expression matrix.
- `spatial_neighbors`: true physical graph from k-nearest or radius neighbors.
- `control_neighbors`: random, coordinate-shuffled, distant, and same-type
  distant controls where available.
- `split_assignments`: unit, FOV, sample/section, donor, or dataset holdout
  assignments.
- `context_utility` and `router_label` tables: run-level or stratum-level
  evidence summaries used by CP-Q2, CP-Q5, and CP-Q6.

The default spatial graph is deterministic k-nearest neighbors with `k=5`,
grouped by `sample_id` and `slide_id`, using `x,y` centroids and distance bins
`<=20`, `<=75`, `<=150`, and `>150` coordinate units.

---

## Shared Thresholds

Current CP-Q smoke/matrix thresholds are:

- expression-low context utility threshold: `0.01`
- full-context context utility threshold: `0.65`
- LR pair coverage threshold: `4`
- module target coverage threshold: `4`
- positive-control sensitivity threshold: `0.65`
- synthetic specificity threshold: `0.80`
- false positive context threshold: `0.05`
- positive-control route recovery threshold: `0.95`

CP-Q8.6E will add the threshold-calibration and minimum-detectable-effect
audit. These cards document the current implementation before that calibration
pass.

