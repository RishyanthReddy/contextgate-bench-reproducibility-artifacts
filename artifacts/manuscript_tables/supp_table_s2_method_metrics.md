# Supplementary Table S2: Method Metrics

| Method | Method family | Rows | Mean utility | Mean regret | No-harm rate | False-context rate | Abstention rate | Context-use rate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Spatial stats | spatial statistics heuristic | 23 | 1.0 | 0.0 | 1.0 | 0.0 | 0.4783 | 0.0435 |
| ContextGate | contextgate transparent router | 23 | 0.9739 | 0.0261 | 1.0 | 0.0 | 0.5217 | 0.0 |
| Expression only | expression only or center only | 23 | 0.813 | 0.187 | 1.0 | 0.0 | 0.0 | 0.0 |
| CellPack tiny | cellpack packed context | 23 | 0.8087 | 0.1913 | 1.0 | 0.0 | 0.9565 | 0.0435 |
| LR/pathway | ligand receptor or pathway heuristic | 23 | 0.5913 | 0.4087 | 1.0 | 0.0 | 0.4348 | 0.3478 |
| GraphSAGE style | gnn style context aggregation | 23 | 0.4696 | 0.5304 | 1.0 | 0.0 | 0.6087 | 0.3913 |
| Always context | always true neighbor context | 23 | 0.1391 | 0.8609 | 0.5217 | 0.4783 | 0.0 | 1.0 |
| Coord. shuffled | wrong context coordinate shuffled | 23 | 0.1391 | 0.8609 | 0.5217 | 0.4783 | 0.0 | 1.0 |
| Distant control | wrong context distant neighbor | 23 | 0.1391 | 0.8609 | 0.5217 | 0.4783 | 0.0 | 1.0 |
| Random control | wrong context random neighbor | 23 | 0.1391 | 0.8609 | 0.5217 | 0.4783 | 0.0 | 1.0 |
