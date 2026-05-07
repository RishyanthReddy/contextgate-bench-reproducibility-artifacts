# CP-Q8.7B Paper-Wizard Metric Consistency Audit

> Status: CP-Q8.7B audit complete.
>
> Purpose: reconcile the false-context-rate and oracle-regret values flagged by
> Paper-Wizard before any manuscript, figure, or table rewrite.

---

## 1) Source Artifacts Audited

| Artifact | Role in Audit | Result |
|---|---|---|
| `results/reports/cp_q2_method_comparison/method_predictions.csv` | Row-level CP-Q2 route predictions, utilities, regret, context-use flags, and false-context flags. | Reproduces CP-Q2 method table values. |
| `results/reports/cp_q2_method_comparison/method_metrics.csv` | CP-Q2 method-family means used by the current method-regret figure. | Reproduces the current Figure 3/text values. |
| `results/reports/cp_q3_positive_null_control_ladder/method_summary.csv` | Positive/null-control sensitivity, specificity, and null false-context rates. | Reproduces the current null-ladder values. |
| `results/reports/cp_q5_contextgate_decisions/contextgate_no_harm.csv` | ContextGate no-harm comparison against always-context, expression-only, and CellPack tiny comparators. | Reproduces Table 3 support text but inherits CP-Q2 FCR denominator ambiguity. |
| `results/reports/cp_q6_benchmark_matrix/aggregate_metrics.csv` | Full q1 benchmark metric profile plotted in the current Figure 2. | Reproduces Figure 2 metric-profile values. |
| `results/reports/cp_q6_benchmark_matrix/benchmark_metric_matrix.csv` | Row-level CP-Q6 matrix used for regret distribution table S17. | Reproduces full-benchmark regret values. |
| `manuscript/tables/supp_table_s17_q6_regret_distribution.csv` | Derived CP-Q6 regret distribution. | Matches CP-Q6 row-level metric matrix. |

No audited value was unreproducible from registered local artifacts.

---

## 2) E1 Audit: Always-Context `0.4783` False-Context Value

### What the Current Artifacts Store

In CP-Q2, `src/cellpack/method_comparison.py` defines
`false_positive_context_use` as:

```text
true_route == "expression_only" and predicted_route in CONTEXT_ROUTES
```

The CP-Q2 method table then reports:

```text
false_positive_context_rate = mean(false_positive_context_use over all 23 rows)
```

For the always-context method, the 23 CP-Q2 registered rows split as:

| Route/evidence class | Rows | Always-context uses context | Stored false-positive rows |
|---|---:|---:|---:|
| `expression_only` / `negative_context` | 11 | 11 | 11 |
| `abstain_uncertain` / borderline, coverage, insufficient, localized | 11 | 11 | 0 |
| `full_context` / `positive_control_only` | 1 | 1 | 0 |

Therefore the stored value is:

```text
11 / 23 = 0.4783
```

This is a row-mean false-positive flag across the full CP-Q2 registered row
set. It is reproducible, but it is not the null-denominator false-context rate
defined in the current manuscript equation.

### Equation-Compatible Denominators

The current manuscript says FCR is the fraction of settings where a method uses
or favors context when the benchmark says it should not. Under that broader
wording:

| Denominator Definition | Always-Context Value | Interpretation |
|---|---:|---|
| Negative-context rows only (`true_route == expression_only`) | `11 / 11 = 1.000` | Always-context falsely uses context on every explicit negative-context row. |
| Unsupported real rows excluding the positive-control-only row | `22 / 22 = 1.000` | Always-context uses context on every explicit negative or abstention/unsupported row. |
| All CP-Q2 registered rows using stored `false_positive_context_use` flag | `11 / 23 = 0.4783` | Current artifact value; this is a global row-mean false-positive flag, not Equation 3 FCR. |
| Positive/null ladder null rows from CP-Q3 | `36 / 36 = 1.000` | Current manuscript's null-ladder value; this is internally consistent. |

### Decision

The value `0.4783` must not be called the primary Equation 3 FCR unless the
equation is rewritten to match the all-row stored flag denominator. The safer
revision is:

- reserve **null-denominator FCR** for denominator-specific values such as
  `1.000` on CP-Q2 negative-context rows and `1.000` on CP-Q3 null ladder rows;
- rename `0.4783` as an **all-row registered false-context flag mean** or
  **global false-context exposure** if retained;
- report expression-only beside ContextGate because both have `0.000` under the
  current real-data false-context flag, while expression-only has zero
  positive-control sensitivity and ContextGate has positive-control sensitivity
  of `0.8633`.

### Modal Decision for E1

No Level 5 Modal rerun is triggered by E1. The values are reproducible. The
required action is CP-Q8.7C local derivation of stratified denominator tables,
followed by CP-Q8.7G/H manuscript and figure/table wording changes.

---

## 3) E3 Audit: Oracle-Regret Values Across Figures and Text

### Current Figure/Text Sources

| Display or Text Claim | Source Artifact | Scope | Key Values |
|---|---|---|---|
| Current Figure 2 full benchmark metric profile | `cp_q6_benchmark_matrix/aggregate_metrics.csv` | q1/full benchmark matrix metric profile | ContextGate regret `0.3430`; spatial stats regret `0.3730`; expression-only regret `0.4914`; always-context regret `0.8421`. |
| Current Figure 3 method-family oracle regret | `cp_q2_method_comparison/method_metrics.csv` | CP-Q2 registered context-utility smoke comparison over 23 rows | Spatial stats regret `0.0000`; ContextGate regret `0.0261`; expression-only regret `0.1870`; always-context regret `0.8609`. |
| Current Results Section 4.2 paragraph | `cp_q2_method_comparison/method_metrics.csv` | CP-Q2 method table | Reports always-context regret `0.8609`, ContextGate regret `0.0261`, and spatial stats zero regret. |
| Supplementary Table S17 | `cp_q6_benchmark_matrix/benchmark_metric_matrix.csv` | CP-Q6 regret distribution by benchmark tier | Full benchmark spatial stats regret `0.3730`, ContextGate `0.3430`, always-context `0.8421`; core always-context `0.9016`; mini always-context `0.7336`. |

### Decision

The regret values are reproducible, but the current manuscript and figure
placement make different scopes look like conflicting estimates of the same
quantity. The CP-Q2 method-regret figure is a small registered context-utility
smoke comparison. The full metric-profile figure is a q1/full benchmark matrix
summary. They should not be interpreted as the same aggregate.

CP-Q8.7H should do one of the following:

1. regenerate the method-family oracle-regret figure from CP-Q6 full-benchmark
   regret values so Figure 2, Figure 3, and the main text share the same scope;
   or
2. keep the CP-Q2 regret figure but explicitly label it as the CP-Q2
   23-row registered context-utility smoke comparison and move the
   full-benchmark regret values into the main Results text.

The preferred reviewer-safe option is option 1, because the manuscript is
positioned as a benchmark paper and the main figure should use the broadest
registered benchmark scope.

### Modal Decision for E3

No Level 5 Modal rerun is triggered by E3. CP-Q6 regret values are reproducible
from the registered matrix. The required action is a Level 2 local figure/table
rebuild and caption/text reconciliation.

---

## 4) Immediate Claim Changes Required Later in CP-Q8.7

These are not applied in CP-Q8.7B; they are queued for CP-Q8.7C/G/H.

| Current Risk | Required Change |
|---|---|
| "Always-context baseline used context in every row and had a false-context rate of 0.4783." | Replace with denominator-specific wording: always-context had `1.000` FCR on explicit negative-context/null rows; the stored `0.4783` value is the all-row registered false-context flag mean. |
| "ContextGate reduces false context use" without expression-only comparison. | Reframe: ContextGate and expression-only both avoid real-data false-context use under current artifacts; ContextGate differs by retaining positive-control sensitivity (`0.8633`) and abstention. |
| "Spatial-statistics heuristic had zero mean regret" in the main benchmark Results. | Scope it to CP-Q2 only or replace with CP-Q6 full-benchmark regret (`0.3730`), where ContextGate has lower mean regret (`0.3430`). |
| Figure 2 and Figure 3 appear to report conflicting regret values. | Use common CP-Q6 scope or explicitly state CP-Q2 versus CP-Q6 scopes in captions and Results text. |
| Table 3 support text uses "always-context comparator 0.478 higher" as FCR. | Rebuild Table 3 support after S24 stratified FCR table exists. |

---

## 5) Modal Rerun Level

**Selected level:** Level 2 local rebuild from registered artifacts.

**Rationale:**

- CP-Q2, CP-Q3, CP-Q5, and CP-Q6 values are reproducible from their registered
  local artifacts.
- The E1 problem is a metric-label/denominator mismatch between manuscript
  Equation 3 and stored row-mean false-context flags.
- The E3 problem is a scope mismatch between CP-Q2 and CP-Q6 figure sources.
- No Modal entrypoint changed.
- No missing row-level metric evidence was discovered.
- No CP-Q6 metric row was unreconcilable with its source artifact.

**No current trigger for:**

- Level 3 live Modal smoke;
- Level 4 bounded Modal refresh;
- Level 5 full CP-Q6 Modal matrix rerun.

---

## 6) Acceptance Criteria Status

| CP-Q8.7B Criterion | Status | Evidence |
|---|---|---|
| Audit all FCR values in Figure 2, Figure 3, Table 3, and top-line text. | PASS | CP-Q2, CP-Q3, CP-Q5, and CP-Q6 source tables inspected. |
| Decide whether `0.4783` changes or is relabeled. | PASS | Relabel as all-row registered false-context flag mean/global exposure; null-denominator FCR is `1.000` on explicit negative/null rows for always-context. |
| Decide whether Figure 2/Figure 3 regret values are stale or scoped differently. | PASS | Scoped differently: Figure 2 uses CP-Q6 q1/full benchmark; Figure 3/text use CP-Q2 23-row method comparison. |
| Decide Modal rerun level. | PASS | Level 2 local rebuild; no Modal rerun now. |
| Stop if registered matrix semantics are invalid. | PASS | No stop trigger found; proceed to CP-Q8.7C. |

---

## 7) Next Task

Proceed to CP-Q8.7C:

1. build stratified FCR/expression-only comparator tables from CP-Q2/CP-Q3/CP-Q5
   registered artifacts;
2. distinguish null-denominator FCR, unsupported-context exposure, all-row
   false-context flag mean, specificity, positive-control sensitivity, and
   route recovery;
3. update Table 3 support only after the new S24 tables exist.
