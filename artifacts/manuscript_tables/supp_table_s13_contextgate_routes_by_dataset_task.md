# Supplementary Table S13: ContextGate Routes By Dataset And Task

| Dataset | Task | Total decisions | Expression-only decisions | Context-allowed decisions | Abstention decisions | Positive-control-only decisions | Real context rows | Synthetic context rows | Mean confidence | Failure classes | Reason codes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CosMx BCC 6K | context utility detection | 4 | 2 | 0 | 2 | 0 | 0 | 0 | 0.9 | labels not replicated, not applicable | uncertain default abstention, unreplicated context signal |
| CosMx NSCLC | context utility detection | 2 | 0 | 0 | 2 | 0 | 0 | 0 | 0.85 | not applicable | uncertain default abstention |
| CosMx PDAC 1K | context utility detection | 3 | 2 | 0 | 1 | 0 | 0 | 0 | 0.9167 | fov or sample artifact;labels not replicated, insufficient power | artifact or confound abstention, insufficient power or uncertainty |
| CosMx PDAC metastasis | context utility detection | 6 | 1 | 0 | 5 | 0 | 0 | 0 | 0.8667 | insufficient power, insufficient power;labels not replicated, labels not replicated | insufficient power or uncertainty, unreplicated context signal |
| Xenium breast 5K | context utility detection | 5 | 3 | 0 | 1 | 1 | 0 | 1 | 0.93 | expression absorbs signal;insufficient power, insufficient power, not applicable | insufficient power or uncertainty, positive control only, uncertain default abstention |
| Xenium breast biomarkers | context utility detection | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 0.95 | expression absorbs signal;insufficient power;panel lacks downstream genes | panel or target coverage gap |
| Discovery index | dataset access | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0.99 | access or schema blocker | access or schema blocker |
| HTAPP MBC MERFISH | dataset access | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0.99 | access or schema blocker | access or schema blocker |
| Private/login sources | dataset access | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0.99 | access or schema blocker | access or schema blocker |
| Spot-level Visium | dataset access | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0.99 | access or schema blocker | access or schema blocker |
| scRNA+Visium claim | dataset access | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0.99 | access or schema blocker | access or schema blocker |
| CosMx PDAC 1K | positive null control ladder | 36 | 6 | 0 | 12 | 18 | 0 | 18 | 0.9083 | not applicable | synthetic confound abstention, synthetic context signal detected, synthetic missing panel abstention, +1 more |
| Xenium breast biomarkers | positive null control ladder | 36 | 6 | 0 | 12 | 18 | 0 | 18 | 0.9083 | not applicable | synthetic confound abstention, synthetic context signal detected, synthetic missing panel abstention, +1 more |
