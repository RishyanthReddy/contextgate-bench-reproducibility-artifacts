# Method Card: Spatial-Statistics Heuristic

## Registry

- `method_id`: `spatial_statistics_heuristic`
- `method_family`: `spatial_statistics_heuristic`
- Primary role: lightweight evidence heuristic for spatial context utility.
- Code pointers:
  - `src/cellpack/method_comparison.py`
  - `src/cellpack/positive_control_ladder.py`
  - `src/cellpack/benchmark_matrix.py`
  - upstream context-utility artifacts from `src/cellpack/evaluation/context_utility.py`

## Scientific Purpose

This heuristic asks whether registered context-utility scores are strong enough
to justify using context, weak enough to prefer expression-only, or ambiguous
enough to abstain.

## Inputs

- `context_utility_score` from run-level or stratum-level context utility
  artifacts.
- Evidence class and route label from router labels.
- Optional gene count and coverage fields from run tables.
- Registered split ID and dataset/task metadata.

## Feature Construction

The method does not directly train on expression matrices in CP-Q2. It consumes
precomputed context-utility evidence:

- `context_utility_score`;
- `evidence_class`;
- dataset/task/split metadata.

In positive/null-control testing, the same heuristic is applied to synthetic
control levels with known expected context positivity.

## Decision Rule

Current CP-Q2 thresholds:

- if `context_utility_score <= 0.01`, predict `expression_only`;
- if `context_utility_score >= 0.65`, predict `full_context`;
- otherwise predict `abstain_uncertain`.

Confidence values:

- expression-only: `0.80`;
- full-context: `0.80`;
- abstain: `0.65`.

## Hyperparameters

- `expression_score_threshold = 0.01`
- `full_context_score_threshold = 0.65`

CP-Q8.6E will calibrate these thresholds against stress and positive/null
control artifacts.

## Splits

The heuristic inherits split information from context-utility rows. It does not
create a new split. It must not pool held-out biological outcome labels into
training rows.

## Output Metrics

- mean utility;
- mean regret;
- false-positive context rate;
- no-harm rate;
- abstention rate;
- context-use rate;
- paired deltas versus expression-only and always-context.

## Failure / Skip Conditions

- Missing context-utility score.
- Missing router labels or evidence class.
- Missing upstream artifacts needed to construct context utility.

## Interpretation Rule

This is a transparent heuristic, not a biological model. It is useful when a
reviewer wants to know whether a simple score threshold performs competitively
with more complicated context usage.

