# CP-Q5 ContextGate Decisions

- Decision rows: `100`
- Biological/run decisions: `23`
- Synthetic-control decisions: `72`
- Access/schema decisions: `5`
- Context-allowed biological decisions: `0`
- Positive-control route recovery: `1.000000`
- Registered false-context reduction vs always-context: `0.478261`
- Synthetic false-context reduction vs always-context: `1.000000`
- CP-Q5 gate passed: `True`

ContextGate is transparent and conservative: real context is allowed only when strict replicated evidence exists; synthetic positives are kept mechanics-only; negative rows use expression-only; uncertain rows abstain with reason codes.
