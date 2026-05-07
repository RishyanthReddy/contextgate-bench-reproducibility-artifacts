# Method Card: Expression-Only / Center-Only Baseline

## Registry

- `method_id`: `expression_only_linear`
- `method_family`: `expression_only_or_center_only`
- Primary role: baseline and no-context comparator.
- Code pointers:
  - `src/cellpack/models/baselines.py`
  - `src/cellpack/method_comparison.py`
  - `src/cellpack/benchmark_matrix.py`

## Scientific Purpose

This baseline asks whether the center cell or spatial unit already contains
enough expression information to solve the task without using any neighbor
context. It is the reference that context methods must beat before any spatial
claim is allowed.

## Inputs

- Center unit expression vector `x_i`.
- Training split expression matrix for global and center-total scaled means.
- `unit_table`, `gene_vocabulary`, and `split_assignments`.
- No neighbor graph is consumed for the expression-only route decision.

## Targets

Targets depend on task family:

- masked-gene reconstruction: masked center-gene expression values;
- LR/receptor tasks: receiver receptor expression or residual targets;
- pathway tasks: downstream pathway/module residual targets;
- label tasks: broad cell/spatial labels where available;
- route tasks: registered `route_label` from router-label tables.

## Feature Construction and Normalization

The baseline uses center expression only. In the low-level CP-3 baseline
contract, two deterministic variants exist:

- global train-split gene mean;
- center-total scaled train gene fractions, where each unit total count is
  multiplied by train-split gene fractions.

The CP-Q route-level method-comparison suite abstracts this family as a
deterministic center-expression baseline that always predicts
`expression_only`.

## Scoring / Training Procedure

No stochastic training is used in the CP-Q route-level comparison. The method
predicts:

- `predicted_route = expression_only`
- confidence `0.95`
- reason: center-expression baseline.

In CP-3 prediction-table evaluations, metrics are MAE/RMSE style expression
errors grouped by model, graph type, and split.

## Hyperparameters

- Uses no neighbor graph.
- Uses no random seed.
- Route-level confidence: `0.95`.
- CP-3 baseline variants are controlled by `BaselineConfig`:
  - `include_global_mean = true`
  - `include_center_total_scaled_mean = true`
  - `include_neighbor_average = true`, although neighbor average belongs to
    context/reference baselines rather than the expression-only route.

## Splits

Uses the registered split assignment for each benchmark row:

- `unit_hash_split`
- `fov_holdout`
- `sample_or_section_holdout`
- `patient_or_donor_holdout` where available.

Training statistics must be computed from the train split only when a train
statistic is required.

## Output Metrics

- utility and regret against oracle route;
- paired delta versus always-context methods;
- no-harm rate;
- false-positive context rate, expected to be zero by construction;
- prediction error for expression-table tasks.

## Failure / Skip Conditions

- Missing expression matrix.
- Missing split assignment.
- Missing center unit IDs or duplicated unit IDs.
- Missing target labels for label-prediction tasks.

## Interpretation Rule

If expression-only matches or beats context methods, the manuscript may claim
that context was not required under that dataset/task/split/method setting. It
must not claim that biology lacks spatial communication.

