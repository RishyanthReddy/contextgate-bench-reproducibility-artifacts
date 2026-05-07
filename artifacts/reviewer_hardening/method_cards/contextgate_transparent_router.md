# Method Card: ContextGate Transparent Router

## Registry

- `method_id`: `contextgate_transparent_router`
- `method_family`: `contextgate_transparent_router`
- Primary role: deterministic evidence router.
- Code pointers:
  - `src/cellpack/contextgate.py`
  - `src/cellpack/failure_taxonomy.py`
  - `src/cellpack/method_comparison.py`
  - `src/cellpack/benchmark_matrix.py`

## Scientific Purpose

ContextGate decides whether a dataset/task/target row should use
expression-only evidence, allow real context, abstain, or be labeled
positive-control-only. Its purpose is false-context control and claim
discipline, not maximizing context-use frequency.

## Inputs

- Run-level context utility rows.
- Positive/null-control ladder rows.
- Failure taxonomy rows.
- Evidence class and route recommendation.
- Gate booleans:
  - residual signal;
  - wrong-context check;
  - FDR/effect check;
  - held-out replication;
  - leakage audit.

## Route Labels

Allowed routes:

- `expression_only`;
- `context_allowed`;
- `abstain_uncertain`;
- `positive_control_only`.

The router does not use arbitrary free-text route labels.

## Decision Rule

Real context is allowed only when strict evidence passes:

- evidence class is `strict_positive`;
- residual signal gate passes;
- strict conditioned gate passes;
- held-out gate passes;
- FDR control passes.

Positive-control rows can receive `positive_control_only` when injected
true-neighbor signal is detected, but this does not become a biological
context claim.

Negative context evidence or expression-only recommendations route to
`expression_only`. Access blockers, panel gaps, non-replication, confounding,
and uncertainty route to `abstain_uncertain` unless the row is explicitly
negative enough for expression-only.

## Thresholds

Current `ContextGateConfig` values:

- false-positive context threshold: `0.05`;
- positive-control route recovery threshold: `0.95`;
- positive-control sensitivity threshold: `0.65`;
- synthetic specificity threshold: `0.80`.

CP-Q8.6C will formalize route precedence and CP-Q8.6E will calibrate
thresholds.

## Outputs

Each decision row includes:

- `contextgate_decision_id`;
- `route_label`;
- `reason_code`;
- `reason_detail`;
- gate booleans;
- `evidence_pointer`;
- artifact IDs;
- `claim_level`;
- split/seed/control-level metadata;
- confidence;
- `uses_real_context`;
- `uses_synthetic_context`.

## Splits

ContextGate consumes split-aware upstream evidence. It does not create new
splits. Held-out replication and leakage-audit status are part of the route.

## Output Metrics

- route distribution;
- no-harm rate;
- false-positive context rate;
- abstention rate;
- claim level counts;
- utility/regret when compared with oracle labels.

## Failure / Skip Conditions

- Missing required decision columns.
- Unknown route label.
- Missing upstream context utility and failure-taxonomy rows.
- Missing positive/null-control ladder rows for synthetic checks.

## Interpretation Rule

ContextGate is deliberately conservative. An abstention or expression-only
route means the evidence contract did not justify context use under the current
benchmark row. It is not proof that the underlying biology is absent.

