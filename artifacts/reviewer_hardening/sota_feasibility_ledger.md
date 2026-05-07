# CP-Q8.6H SOTA Feasibility and Limited Replay Gate

Date: 2026-05-05

## Decision

**Release decision:** `cite_scope_only` for the current manuscript release, with
`adapter_only` notes for the methods that are closest to future replay.

No additional high-capacity/SOTA replay is run before CP-Q8.6 manuscript
integration. This is intentional, not avoidance. The feasibility audit found no
candidate that simultaneously satisfies all six CP-Q8.6H requirements:

1. open implementation or enough detail to reproduce;
2. compatibility with the existing expression, coordinate, graph, task, split,
   and provenance contracts;
3. bounded Modal runtime/cost without adding a new large dependency surface;
4. direct output in the CP-Q benchmark metric schema;
5. no requirement for new private or large image/multimodal datasets;
6. enough expected value to justify delaying manuscript completion.

The manuscript should therefore state a scope boundary rather than imply that
ContextGate-Bench has defeated every modern spatial foundation model. The
correct wording is:

> High-capacity spatial graph, transformer, communication, and foundation
> models are important candidates for future replay. ContextGate-Bench does not
> claim they cannot exploit context. It provides the controlled decision
> framework those models should pass before context-dependent biological claims
> are trusted.

## Why No Replay Is Added Now

The closest peer-reviewed candidates fall into three groups.

First, graph/context models such as BANKSY, GraphST, SpaGT, STMGraph, SpaMask,
and SiGra exploit spatial neighborhoods, graph structure, masking, contrastive
learning, or image augmentation. They are important related work, but most
optimize clustering, denoising, domain detection, integration, or representation
learning. To force them into CP-Q masked-expression, ligand-receptor, pathway,
false-context, no-harm, and regret rows, we would need custom supervised heads
or feature adapters. At that point the benchmark would partly evaluate our
adapter choices rather than the published method.

Second, spatial foundation models such as Nicheformer and Novae are now strong
peer-reviewed anchors, but replaying them fairly would require foundation-model
tokenization, pretrained checkpoints, adapter heads, calibration rules, and
substantial compute decisions. That is a separate benchmark extension, not a
bounded reviewer-hardening patch.

Third, spatial communication and optimal-transport frameworks such as COMMOT,
SCOTIA, moscot, LIANA+, SpatialDM, SpaTalk, DeepTalk, and Niche-DE/niche-LR are
biologically close to the ligand-receptor/pathway part of ContextGate-Bench, but
they usually emit interaction scores, transport flows, niche-DE statistics, or
communication networks rather than CP-Q prediction tables across all tasks.
Several can be adapted later, especially COMMOT, LIANA+, and Niche-DE/niche-LR,
but they do not provide a drop-in full-matrix baseline.

Histology-to-spatial resources and models such as HEST-1k, SpaRED/SpaCKLE,
MERGE, CMRCNet, OmiCLIP/Loki, and STPath are valuable benchmark precedents and
future multimodal directions, but they require image inputs and answer a
different question.

## Candidate Outcomes

Source table: `manuscript/reviewer_hardening/sota_feasibility_ledger.csv`.

Summary counts:

- `adapter_only`: 5 candidates.
- `cite_scope_only`: 12 candidates.
- `reject_for_release`: 3 candidates.

The `adapter_only` candidates are the best future replay targets:

- BANKSY: freeze neighborhood-augmented features and train the same CP-Q heads.
- GraphST: freeze graph contrastive embeddings and train the same CP-Q heads.
- Niche-DE/niche-LR: add a niche-specific statistical gate for labeled subsets.
- COMMOT: add a CCC score adapter for LR/pathway gates.
- LIANA+: add a label-rich CCC resource adapter for LR/pathway gates.

The `cite_scope_only` candidates strengthen related work and limitations but do
not add release rows. The `reject_for_release` candidates are preprint-only,
unstable, or outside the current benchmark contract.

## Manuscript Integration Requirements

Section 2 should acknowledge modern context-heavy methods, but it should not
overclaim direct comparison. Section 6 should include one concise limitation:
high-capacity foundation and specialized CCC models were not replayed in this
release because no candidate was a drop-in CP-Q method row without adding new
adapters, modalities, or target definitions.

Section 6 should also convert the limitation into a positive future-work plan:
ContextGate-Bench can evaluate any future method once it emits the standard
prediction/score tables needed for expression-only, true-neighbor,
wrong-context, positive-control, null-control, no-harm, and route-decision
audits.

## Modal Decision

No Modal execution is required for CP-Q8.6H. This card records a no-replay
feasibility decision and does not add code, Modal entrypoints, new method rows,
or benchmark-matrix semantics. Under the CP-Q8.6 rerun ladder, Modal becomes
necessary only if CP-Q8.6H chooses `run_limited_replay`; it did not.

## Stop Rule

Do not add an extra SOTA baseline to the current manuscript unless all of the
following are true:

- the method can ingest current CP-Q contracts without new large data;
- outputs can be mapped to CP-Q metrics without a bespoke, unfair head;
- the adapter can be tested locally and in bounded Modal;
- tables can be regenerated without changing the CP-Q6 semantics;
- and the result would clarify the paper more than it delays release.

No candidate currently passes that rule.
