# Supplementary Table S12: CP-Q6 Method-Task Safety Summary

| Task | Method | Datasets | Metric rows | Mean regret | Regret IQR low | Regret IQR high | Mean FCR | Mean no-harm | Mean abstention | Mean sensitivity/proxy | Mean specificity/proxy | Mean replication |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cell type or spatial label prediction | Spatial stats | 5 | 420 | 0.3427 | 0.2391 | 0.4469 | 0.0 | 1.0 | 0.4783 | 0.6573 | 1.0 | 0.5997 |
| cell type or spatial label prediction | ContextGate | 5 | 420 | 0.3616 | 0.2581 | 0.4689 | 0.0 | 1.0 | 0.4 | 0.6384 | 1.0 | 0.5898 |
| cell type or spatial label prediction | Expression only | 5 | 420 | 0.4626 | 0.3752 | 0.5539 | 0.0 | 1.0 | 0.0 | 0.5374 | 1.0 | 0.524 |
| cell type or spatial label prediction | LR/pathway | 5 | 420 | 0.6027 | 0.5363 | 0.6685 | 0.0 | 1.0 | 0.4348 | 0.3973 | 1.0 | 0.4348 |
| cell type or spatial label prediction | Always context | 5 | 420 | 0.8878 | 0.8679 | 0.9046 | 0.5452 | 0.44 | 0.0 | 0.1122 | 0.4548 | 0.2525 |
| cell type or spatial label prediction | Random control | 5 | 420 | 0.8887 | 0.8707 | 0.9114 | 0.5452 | 0.44 | 0.0 | 0.1113 | 0.4548 | 0.2513 |
| cell type or spatial label prediction | Coord. shuffled | 5 | 420 | 0.8951 | 0.8868 | 0.9096 | 0.5452 | 0.44 | 0.0 | 0.1049 | 0.4548 | 0.2443 |
| ligand receptor recovery | Spatial stats | 6 | 480 | 0.3804 | 0.2852 | 0.4814 | 0.0 | 1.0 | 0.4783 | 0.6196 | 1.0 | 0.5734 |
| ligand receptor recovery | ContextGate | 6 | 480 | 0.3942 | 0.2963 | 0.4902 | 0.0 | 1.0 | 0.4 | 0.6058 | 1.0 | 0.5652 |
| ligand receptor recovery | Expression only | 6 | 480 | 0.489 | 0.4058 | 0.5672 | 0.0 | 1.0 | 0.0 | 0.511 | 1.0 | 0.5062 |
| ligand receptor recovery | LR/pathway | 6 | 480 | 0.6257 | 0.5677 | 0.6837 | 0.0 | 1.0 | 0.4348 | 0.3743 | 1.0 | 0.4218 |
| ligand receptor recovery | Random control | 6 | 480 | 0.894 | 0.8764 | 0.9095 | 0.5452 | 0.44 | 0.0 | 0.106 | 0.4548 | 0.2533 |
| ligand receptor recovery | Coord. shuffled | 6 | 480 | 0.8951 | 0.8771 | 0.9089 | 0.5452 | 0.44 | 0.0 | 0.1049 | 0.4548 | 0.2536 |
| ligand receptor recovery | Always context | 6 | 480 | 0.8988 | 0.8916 | 0.9087 | 0.5452 | 0.44 | 0.0 | 0.1012 | 0.4548 | 0.2475 |
| masked gene reconstruction | Spatial stats | 6 | 480 | 0.1894 | 0.0646 | 0.3117 | 0.0 | 1.0 | 0.4783 | 0.8106 | 1.0 | 0.696 |
| masked gene reconstruction | ContextGate | 6 | 480 | 0.2106 | 0.0824 | 0.3387 | 0.0 | 1.0 | 0.4 | 0.7894 | 1.0 | 0.6812 |
| masked gene reconstruction | Expression only | 6 | 480 | 0.3376 | 0.2283 | 0.4464 | 0.0 | 1.0 | 0.0 | 0.6624 | 1.0 | 0.5985 |
| masked gene reconstruction | LR/pathway | 6 | 480 | 0.5127 | 0.4337 | 0.5933 | 0.0 | 1.0 | 0.4348 | 0.4873 | 1.0 | 0.4931 |
| masked gene reconstruction | Coord. shuffled | 6 | 480 | 0.8691 | 0.8526 | 0.8835 | 0.5452 | 0.44 | 0.0 | 0.1309 | 0.4548 | 0.2696 |
| masked gene reconstruction | Always context | 6 | 480 | 0.8692 | 0.8513 | 0.8872 | 0.5452 | 0.44 | 0.0 | 0.1308 | 0.4548 | 0.2703 |
| masked gene reconstruction | Random control | 6 | 480 | 0.8693 | 0.8542 | 0.8846 | 0.5452 | 0.44 | 0.0 | 0.1307 | 0.4548 | 0.2688 |
| positive null control ladder | ContextGate | 6 | 480 | 0.2232 | 0.1079 | 0.3372 | 0.0 | 1.0 | 0.3333 | 0.7768 | 1.0 | 0.6747 |
| positive null control ladder | LR/pathway | 6 | 480 | 0.3508 | 0.2422 | 0.4583 | 0.38 | 0.7763 | 0.1667 | 0.6492 | 0.62 | 0.5929 |
| positive null control ladder | Spatial stats | 6 | 480 | 0.4763 | 0.4027 | 0.5595 | 0.38 | 0.6097 | 0.3333 | 0.5237 | 0.62 | 0.514 |
| positive null control ladder | Always context | 6 | 480 | 0.5993 | 0.535 | 0.6626 | 1.0 | 0.35 | 0.0 | 0.4007 | 0.0 | 0.4383 |
| positive null control ladder | Expression only | 6 | 480 | 0.6036 | 0.549 | 0.6628 | 0.0 | 0.5 | 0.0 | 0.3964 | 1.0 | 0.4358 |
| positive null control ladder | Coord. shuffled | 6 | 480 | 0.9817 | 0.9743 | 0.9892 | 1.0 | 0.0 | 0.0 | 0.0183 | 0.0 | 0.2 |
| positive null control ladder | Random control | 6 | 480 | 0.9826 | 0.9738 | 0.9911 | 1.0 | 0.0 | 0.0 | 0.0174 | 0.0 | 0.197 |
| residual pathway module prediction | Spatial stats | 6 | 480 | 0.4146 | 0.3275 | 0.507 | 0.0 | 1.0 | 0.4783 | 0.5854 | 1.0 | 0.5524 |
| residual pathway module prediction | ContextGate | 6 | 480 | 0.4283 | 0.3403 | 0.5191 | 0.0 | 1.0 | 0.4 | 0.5717 | 1.0 | 0.5447 |
| residual pathway module prediction | Expression only | 6 | 480 | 0.5192 | 0.4465 | 0.5895 | 0.0 | 1.0 | 0.0 | 0.4808 | 1.0 | 0.488 |
| residual pathway module prediction | LR/pathway | 6 | 480 | 0.6474 | 0.5872 | 0.707 | 0.0 | 1.0 | 0.4348 | 0.3526 | 1.0 | 0.4076 |
| residual pathway module prediction | Coord. shuffled | 6 | 480 | 0.9003 | 0.8853 | 0.9097 | 0.5452 | 0.44 | 0.0 | 0.0997 | 0.4548 | 0.2507 |
| residual pathway module prediction | Random control | 6 | 480 | 0.9006 | 0.8857 | 0.9147 | 0.5452 | 0.44 | 0.0 | 0.0994 | 0.4548 | 0.2499 |
| residual pathway module prediction | Always context | 6 | 480 | 0.9016 | 0.8943 | 0.9078 | 0.5452 | 0.44 | 0.0 | 0.0984 | 0.4548 | 0.2476 |
| residual receptor prediction | Spatial stats | 6 | 480 | 0.4309 | 0.3478 | 0.5185 | 0.0 | 1.0 | 0.4783 | 0.5691 | 1.0 | 0.5414 |
| residual receptor prediction | ContextGate | 6 | 480 | 0.4422 | 0.3562 | 0.5297 | 0.0 | 1.0 | 0.4 | 0.5578 | 1.0 | 0.5372 |
| residual receptor prediction | Expression only | 6 | 480 | 0.5328 | 0.462 | 0.6036 | 0.0 | 1.0 | 0.0 | 0.4672 | 1.0 | 0.48 |
| residual receptor prediction | LR/pathway | 6 | 480 | 0.6518 | 0.6025 | 0.6998 | 0.0 | 1.0 | 0.4348 | 0.3482 | 1.0 | 0.4026 |
| residual receptor prediction | Always context | 6 | 480 | 0.9016 | 0.8855 | 0.9153 | 0.5452 | 0.44 | 0.0 | 0.0984 | 0.4548 | 0.2494 |
| residual receptor prediction | Random control | 6 | 480 | 0.9022 | 0.8869 | 0.9178 | 0.5452 | 0.44 | 0.0 | 0.0978 | 0.4548 | 0.248 |
| residual receptor prediction | Coord. shuffled | 6 | 480 | 0.9054 | 0.8909 | 0.919 | 0.5452 | 0.44 | 0.0 | 0.0946 | 0.4548 | 0.2478 |
