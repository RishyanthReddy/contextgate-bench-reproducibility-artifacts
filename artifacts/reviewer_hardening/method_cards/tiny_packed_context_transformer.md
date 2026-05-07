# Method Card: Tiny Packed-Context Transformer

## Registry

- `method_id`: `cellpack_packed_context_tiny`
- `method_family`: `cellpack_packed_context`
- Primary role: bounded packed-context neural baseline and positive-control
  capacity sanity check.
- Code pointers:
  - `src/cellpack/models/cellpack_tiny.py`
  - `src/cellpack/tokenization/sequence_builder.py`
  - `src/cellpack/method_comparison.py`
  - `src/cellpack/positive_control_ladder.py`

## Scientific Purpose

The tiny packed-context Transformer tests whether a compact sequence model can
consume center and neighbor tokens and recover injected spatial signal. It is
not intended to represent modern spatial foundation models.

## Inputs

- CellPack token sequences containing center and neighbor information.
- Token vocabulary.
- Padded `input_ids` and `attention_mask`.
- Optional focus genes or masked targets for training.
- Standard expression targets for center unit prediction.

## Architecture

The bounded CellPack-Tiny configuration is:

- Transformer encoder;
- `d_model = 64`;
- `n_heads = 4`;
- `n_layers = 2`;
- feed-forward dimension `128`;
- dropout `0.1`;
- maximum sequence length `512`;
- token and positional embeddings;
- pooling strategy: `mean` by default, with `first_token` available;
- output head: linear projection from pooled hidden state to gene count;
- output activation: `softplus` for nonnegative expression predictions, or
  identity when configured.

Approximate parameter count depends on token vocabulary and gene count because
embedding and output-head sizes are dataset-specific.

## Feature Construction

CellPack sequences flatten spatial-unit context into token IDs. The sequence
builder controls which center, neighbor, gene, and signal tokens are included.
The tiny model receives only token IDs and an attention mask; it does not
receive raw coordinates unless they were encoded into upstream tokens.

## Training Procedure

The CP-3 tiny training loop is bounded:

- default steps: `50`;
- learning rate: `0.01`;
- weight decay: `0.0`;
- gradient clipping: `1.0`;
- train split: `train`;
- optional masked-target weighting and focus-gene weighting.

CP-Q route-level comparisons use the family as a registered method proxy with
the following route rule:

- if `context_utility_score >= 0.65`, predict `full_context`;
- otherwise predict `abstain_uncertain`.

## Positive-Control Behavior

In CP-Q3 positive/null controls:

- strong and localized injected signals should be recoverable;
- missing-panel dropout should lead to abstention;
- confounded signal exposes overuse risk;
- null signal should route to expression-only.

This is the main defense against the claim that the benchmark cannot detect any
context signal. It is not proof that the tiny model is SOTA.

## Splits

Uses registered split assignments. Sequence/model training must be restricted
to train rows, with held-out rows used only for evaluation.

## Output Metrics

- expression prediction error when run through CP-3/CP-4 prediction contracts;
- utility/regret route metrics in CP-Q2/CP-Q6;
- positive-control sensitivity and null specificity in CP-Q3;
- false-positive context and no-harm metrics.

## Failure / Skip Conditions

- Token vocabulary missing.
- Empty token rows.
- Sequence length exceeds configured maximum after clipping policy.
- Missing expression target matrix.
- Positive/null-control task in CP-Q6 is marked not applicable for this method
  where the biological gate is not meaningful.

## Interpretation Rule

Use this model only as a bounded neural baseline and mechanics check. The
manuscript must not use its real-data failures to conclude that larger
SpaFormer-like, HEIST-like, Nicheformer-like, or other high-capacity models
would fail.

