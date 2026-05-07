# Method Card: Oracle and Positive-Control References

## Registry

These references are not deployable biological methods. They are benchmark
calibration devices.

Relevant code pointers:

- `src/cellpack/method_comparison.py`
- `src/cellpack/positive_control_ladder.py`
- `src/cellpack/benchmark_matrix.py`

## Oracle Route Reference

The oracle route is the route label already assigned by the benchmark evidence
standard for a row. Utility is computed by comparing a method's predicted route
with the oracle/true route.

Route utility is defined by a fixed lookup table:

- perfect route match receives utility `1.0`;
- compatible context variants can receive partial utility;
- abstention receives partial credit in uncertain settings;
- false full-context use on expression-only rows receives low or zero utility.

Oracle regret is:

`oracle_utility - method_utility`.

The oracle is not a trained model and must not be presented as achievable
biological performance.

## Positive-Control-Only Reference

Positive-control-only rows are synthetic or injected-control evidence rows.
They answer:

> Can the benchmark detect true-neighbor signal when such signal is deliberately
> injected?

They do not answer:

> Is real biological signaling present in the public dataset?

## Positive/Null Control Levels

Registered levels:

- `null_no_context_signal`;
- `strong_injected_context_signal`;
- `weak_or_noisy_injected_context_signal`;
- `localized_context_signal`;
- `missing_panel_or_target_dropout_signal`;
- `fov_or_sample_confounded_signal`.

## Synthetic Features

Each control case includes:

- injected signal strength;
- noise fraction;
- prevalence;
- localization scope;
- expected route;
- missing-panel dropout flag;
- FOV/sample confounding flag.

The current implementation uses deterministic case construction and method
rules to test sensitivity, specificity, abstention, and false-context behavior.

## Metrics

- positive-control sensitivity;
- null/control specificity;
- false-positive context rate;
- abstention rate;
- gate-pass rate;
- recovery curve by signal strength;
- false-positive curve by control type.

## Interpretation Rule

Positive controls defend benchmark sensitivity. Null and confounded controls
defend specificity. Neither should be converted into biological claims unless
real-data gates also pass under held-out and wrong-context controls.

