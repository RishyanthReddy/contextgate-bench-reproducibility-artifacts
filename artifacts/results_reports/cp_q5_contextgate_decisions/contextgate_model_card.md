# ContextGate Model Card

## Intended Use

ContextGate is a deterministic evidence router for ContextGate-Bench. It decides whether a benchmark row should use expression-only, allow real spatial context, abstain, or report synthetic positive-control evidence only.

## Non-Goals

- It is not a learned router.
- It does not infer causal cell-cell communication.
- It does not convert synthetic positive controls into biology claims.

## Current Behavior

- Decision rows: `100`
- Biological `context_allowed` rows: `0`
- Positive-control recovery: `1.000000`
- False-context rate on registered rows: `0.000000`

## Failure Behavior

When evidence is missing, panel-limited, FOV-confounded, localized only, or underpowered, ContextGate abstains or routes to expression-only and emits a reason code plus evidence pointer.
