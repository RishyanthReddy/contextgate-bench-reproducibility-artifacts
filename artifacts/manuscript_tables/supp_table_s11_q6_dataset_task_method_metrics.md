# Supplementary Table S11: CP-Q6 Dataset-Task-Method Metrics

| Dataset | Task | Method | Completed job rows | Mean prediction error | Mean macro-F1/proxy | Mean residual delta | Mean regret | Mean FCR | Mean no-harm | Mean abstention | Mean q-value proxy | Mean runtime sec | Mean delta vs expression | Mean delta vs always-context |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CosMx BCC 6K | cell type or spatial label prediction | Spatial stats | 6 | 0.3392 | 0.6608 | -0.0592 | 0.3392 | 0.0 | 1.0 | 0.4783 | 0.3392 | 0.045 | 0.1218 | 0.5517 |
| CosMx BCC 6K | cell type or spatial label prediction | ContextGate | 6 | 0.3624 | 0.6376 | -0.0824 | 0.3624 | 0.0 | 1.0 | 0.4 | 0.3624 | 0.0433 | 0.0986 | 0.5285 |
| CosMx BCC 6K | cell type or spatial label prediction | Expression only | 6 | 0.4609 | 0.5391 | -0.1809 | 0.4609 | 0.0 | 1.0 | 0.0 | 0.4609 | 0.041 | 0.0 | 0.4299 |
| CosMx BCC 6K | cell type or spatial label prediction | LR/pathway | 6 | 0.6044 | 0.3956 | -0.3244 | 0.6044 | 0.0 | 1.0 | 0.4348 | 0.6044 | 0.035 | -0.1435 | 0.2864 |
| CosMx BCC 6K | cell type or spatial label prediction | Random control | 6 | 0.8862 | 0.1138 | -0.6062 | 0.8862 | 0.5452 | 0.44 | 0.0 | 0.8862 | 0.043 | -0.4252 | 0.0047 |
| CosMx BCC 6K | cell type or spatial label prediction | Coord. shuffled | 6 | 0.8899 | 0.1101 | -0.6099 | 0.8899 | 0.5452 | 0.44 | 0.0 | 0.8899 | 0.0367 | -0.4289 | 0.001 |
| CosMx BCC 6K | cell type or spatial label prediction | Always context | 6 | 0.8909 | 0.1091 | -0.6109 | 0.8909 | 0.5452 | 0.44 | 0.0 | 0.8909 | 0.0383 | -0.4299 | 0.0 |
| CosMx NSCLC | cell type or spatial label prediction | Spatial stats | 4 | 0.3436 | 0.6564 | -0.0636 | 0.3436 | 0.0 | 1.0 | 0.4783 | 0.3436 | 0.039 | 0.1165 | 0.5461 |
| CosMx NSCLC | cell type or spatial label prediction | ContextGate | 4 | 0.357 | 0.643 | -0.077 | 0.357 | 0.0 | 1.0 | 0.4 | 0.357 | 0.041 | 0.1031 | 0.5327 |
| CosMx NSCLC | cell type or spatial label prediction | Expression only | 4 | 0.4601 | 0.5399 | -0.1801 | 0.4601 | 0.0 | 1.0 | 0.0 | 0.4601 | 0.046 | 0.0 | 0.4296 |
| CosMx NSCLC | cell type or spatial label prediction | LR/pathway | 4 | 0.5977 | 0.4023 | -0.3177 | 0.5977 | 0.0 | 1.0 | 0.4348 | 0.5977 | 0.04 | -0.1375 | 0.292 |
| CosMx NSCLC | cell type or spatial label prediction | Always context | 4 | 0.8897 | 0.1103 | -0.6097 | 0.8897 | 0.5452 | 0.44 | 0.0 | 0.8897 | 0.036 | -0.4296 | 0.0 |
| CosMx NSCLC | cell type or spatial label prediction | Random control | 4 | 0.8939 | 0.1061 | -0.6139 | 0.8939 | 0.5452 | 0.44 | 0.0 | 0.8939 | 0.0425 | -0.4338 | -0.0042 |
| CosMx NSCLC | cell type or spatial label prediction | Coord. shuffled | 4 | 0.8959 | 0.1041 | -0.6159 | 0.8959 | 0.5452 | 0.44 | 0.0 | 0.8959 | 0.038 | -0.4358 | -0.0062 |
| CosMx PDAC 1K | cell type or spatial label prediction | Spatial stats | 6 | 0.3458 | 0.6542 | -0.0658 | 0.3458 | 0.0 | 1.0 | 0.4783 | 0.3458 | 0.0433 | 0.1232 | 0.5416 |
| CosMx PDAC 1K | cell type or spatial label prediction | ContextGate | 6 | 0.3651 | 0.6349 | -0.0851 | 0.3651 | 0.0 | 1.0 | 0.4 | 0.3651 | 0.0417 | 0.1039 | 0.5223 |
| CosMx PDAC 1K | cell type or spatial label prediction | Expression only | 6 | 0.469 | 0.531 | -0.189 | 0.469 | 0.0 | 1.0 | 0.0 | 0.469 | 0.043 | 0.0 | 0.4184 |
| CosMx PDAC 1K | cell type or spatial label prediction | LR/pathway | 6 | 0.5989 | 0.4011 | -0.3189 | 0.5989 | 0.0 | 1.0 | 0.4348 | 0.5989 | 0.037 | -0.13 | 0.2885 |
| CosMx PDAC 1K | cell type or spatial label prediction | Random control | 6 | 0.8862 | 0.1138 | -0.6062 | 0.8862 | 0.5452 | 0.44 | 0.0 | 0.8862 | 0.045 | -0.4172 | 0.0012 |
| CosMx PDAC 1K | cell type or spatial label prediction | Always context | 6 | 0.8874 | 0.1126 | -0.6074 | 0.8874 | 0.5452 | 0.44 | 0.0 | 0.8874 | 0.0367 | -0.4184 | 0.0 |
| CosMx PDAC 1K | cell type or spatial label prediction | Coord. shuffled | 6 | 0.9025 | 0.0975 | -0.6225 | 0.9025 | 0.5452 | 0.44 | 0.0 | 0.9025 | 0.035 | -0.4335 | -0.0151 |
| CosMx PDAC metastasis | cell type or spatial label prediction | Spatial stats | 6 | 0.3379 | 0.6621 | -0.0579 | 0.3379 | 0.0 | 1.0 | 0.4783 | 0.3379 | 0.0417 | 0.129 | 0.5467 |
| CosMx PDAC metastasis | cell type or spatial label prediction | ContextGate | 6 | 0.3603 | 0.6397 | -0.0803 | 0.3603 | 0.0 | 1.0 | 0.4 | 0.3603 | 0.04 | 0.1066 | 0.5243 |
| CosMx PDAC metastasis | cell type or spatial label prediction | Expression only | 6 | 0.4668 | 0.5332 | -0.1868 | 0.4668 | 0.0 | 1.0 | 0.0 | 0.4668 | 0.045 | 0.0 | 0.4178 |
| CosMx PDAC metastasis | cell type or spatial label prediction | LR/pathway | 6 | 0.6093 | 0.3907 | -0.3293 | 0.6093 | 0.0 | 1.0 | 0.4348 | 0.6093 | 0.039 | -0.1424 | 0.2753 |
| CosMx PDAC metastasis | cell type or spatial label prediction | Always context | 6 | 0.8846 | 0.1154 | -0.6046 | 0.8846 | 0.5452 | 0.44 | 0.0 | 0.8846 | 0.035 | -0.4178 | 0.0 |
| CosMx PDAC metastasis | cell type or spatial label prediction | Coord. shuffled | 6 | 0.8927 | 0.1073 | -0.6127 | 0.8927 | 0.5452 | 0.44 | 0.0 | 0.8927 | 0.037 | -0.4259 | -0.0081 |
| CosMx PDAC metastasis | cell type or spatial label prediction | Random control | 6 | 0.8946 | 0.1054 | -0.6146 | 0.8946 | 0.5452 | 0.44 | 0.0 | 0.8946 | 0.0433 | -0.4278 | -0.01 |
| Xenium breast biomarkers | cell type or spatial label prediction | Spatial stats | 6 | 0.3472 | 0.6528 | -0.0672 | 0.3472 | 0.0 | 1.0 | 0.4783 | 0.3472 | 0.0383 | 0.1082 | 0.5398 |
| Xenium breast biomarkers | cell type or spatial label prediction | ContextGate | 6 | 0.3618 | 0.6382 | -0.0818 | 0.3618 | 0.0 | 1.0 | 0.4 | 0.3618 | 0.0367 | 0.0936 | 0.5251 |
| Xenium breast biomarkers | cell type or spatial label prediction | Expression only | 6 | 0.4554 | 0.5446 | -0.1754 | 0.4554 | 0.0 | 1.0 | 0.0 | 0.4554 | 0.0417 | 0.0 | 0.4315 |
| Xenium breast biomarkers | cell type or spatial label prediction | LR/pathway | 6 | 0.6017 | 0.3983 | -0.3217 | 0.6017 | 0.0 | 1.0 | 0.4348 | 0.6017 | 0.043 | -0.1462 | 0.2853 |
| Xenium breast biomarkers | cell type or spatial label prediction | Random control | 6 | 0.8845 | 0.1155 | -0.6045 | 0.8845 | 0.5452 | 0.44 | 0.0 | 0.8845 | 0.04 | -0.429 | 0.0025 |
| Xenium breast biomarkers | cell type or spatial label prediction | Always context | 6 | 0.887 | 0.113 | -0.607 | 0.887 | 0.5452 | 0.44 | 0.0 | 0.887 | 0.039 | -0.4315 | 0.0 |
| Xenium breast biomarkers | cell type or spatial label prediction | Coord. shuffled | 6 | 0.8949 | 0.1051 | -0.6149 | 0.8949 | 0.5452 | 0.44 | 0.0 | 0.8949 | 0.041 | -0.4395 | -0.0079 |
| CosMx BCC 6K | ligand receptor recovery | Spatial stats | 6 | 0.3865 | 0.6135 | -0.1065 | 0.3865 | 0.0 | 1.0 | 0.4783 | 0.3865 | 0.035 | 0.1 | 0.5103 |
| CosMx BCC 6K | ligand receptor recovery | ContextGate | 6 | 0.3984 | 0.6016 | -0.1184 | 0.3984 | 0.0 | 1.0 | 0.4 | 0.3984 | 0.037 | 0.0881 | 0.4985 |
| CosMx BCC 6K | ligand receptor recovery | Expression only | 6 | 0.4865 | 0.5135 | -0.2065 | 0.4865 | 0.0 | 1.0 | 0.0 | 0.4865 | 0.0383 | 0.0 | 0.4103 |
| CosMx BCC 6K | ligand receptor recovery | LR/pathway | 6 | 0.6219 | 0.3781 | -0.3419 | 0.6219 | 0.0 | 1.0 | 0.4348 | 0.6219 | 0.0433 | -0.1355 | 0.2749 |
| CosMx BCC 6K | ligand receptor recovery | Coord. shuffled | 6 | 0.8924 | 0.1076 | -0.6124 | 0.8924 | 0.5452 | 0.44 | 0.0 | 0.8924 | 0.045 | -0.406 | 0.0044 |
| CosMx BCC 6K | ligand receptor recovery | Always context | 6 | 0.8968 | 0.1032 | -0.6168 | 0.8968 | 0.5452 | 0.44 | 0.0 | 0.8968 | 0.043 | -0.4103 | 0.0 |
| CosMx BCC 6K | ligand receptor recovery | Random control | 6 | 0.8991 | 0.1009 | -0.6191 | 0.8991 | 0.5452 | 0.44 | 0.0 | 0.8991 | 0.0367 | -0.4126 | -0.0023 |
| CosMx NSCLC | ligand receptor recovery | Spatial stats | 4 | 0.3716 | 0.6284 | -0.0916 | 0.3716 | 0.0 | 1.0 | 0.4783 | 0.3716 | 0.04 | 0.111 | 0.5306 |
| CosMx NSCLC | ligand receptor recovery | ContextGate | 4 | 0.3926 | 0.6074 | -0.1126 | 0.3926 | 0.0 | 1.0 | 0.4 | 0.3926 | 0.042 | 0.0899 | 0.5095 |
| CosMx NSCLC | ligand receptor recovery | Expression only | 4 | 0.4825 | 0.5175 | -0.2025 | 0.4825 | 0.0 | 1.0 | 0.0 | 0.4825 | 0.036 | 0.0 | 0.4196 |
| CosMx NSCLC | ligand receptor recovery | LR/pathway | 4 | 0.6315 | 0.3685 | -0.3515 | 0.6315 | 0.0 | 1.0 | 0.4348 | 0.6315 | 0.041 | -0.149 | 0.2706 |
| CosMx NSCLC | ligand receptor recovery | Coord. shuffled | 4 | 0.8906 | 0.1094 | -0.6106 | 0.8906 | 0.5452 | 0.44 | 0.0 | 0.8906 | 0.039 | -0.4081 | 0.0115 |
| CosMx NSCLC | ligand receptor recovery | Random control | 4 | 0.8974 | 0.1026 | -0.6174 | 0.8974 | 0.5452 | 0.44 | 0.0 | 0.8974 | 0.038 | -0.4149 | 0.0047 |
| CosMx NSCLC | ligand receptor recovery | Always context | 4 | 0.9021 | 0.0979 | -0.6221 | 0.9021 | 0.5452 | 0.44 | 0.0 | 0.9021 | 0.0425 | -0.4196 | 0.0 |
| CosMx PDAC 1K | ligand receptor recovery | Spatial stats | 6 | 0.3742 | 0.6258 | -0.0942 | 0.3742 | 0.0 | 1.0 | 0.4783 | 0.3742 | 0.037 | 0.1103 | 0.5288 |
| CosMx PDAC 1K | ligand receptor recovery | ContextGate | 6 | 0.3908 | 0.6092 | -0.1108 | 0.3908 | 0.0 | 1.0 | 0.4 | 0.3908 | 0.039 | 0.0937 | 0.5122 |
| CosMx PDAC 1K | ligand receptor recovery | Expression only | 6 | 0.4845 | 0.5155 | -0.2045 | 0.4845 | 0.0 | 1.0 | 0.0 | 0.4845 | 0.0367 | 0.0 | 0.4185 |
| CosMx PDAC 1K | ligand receptor recovery | LR/pathway | 6 | 0.6245 | 0.3755 | -0.3445 | 0.6245 | 0.0 | 1.0 | 0.4348 | 0.6245 | 0.0417 | -0.1399 | 0.2786 |
| CosMx PDAC 1K | ligand receptor recovery | Random control | 6 | 0.8959 | 0.1041 | -0.6159 | 0.8959 | 0.5452 | 0.44 | 0.0 | 0.8959 | 0.035 | -0.4114 | 0.0071 |
| CosMx PDAC 1K | ligand receptor recovery | Coord. shuffled | 6 | 0.8983 | 0.1017 | -0.6183 | 0.8983 | 0.5452 | 0.44 | 0.0 | 0.8983 | 0.0433 | -0.4137 | 0.0048 |
| CosMx PDAC 1K | ligand receptor recovery | Always context | 6 | 0.903 | 0.097 | -0.623 | 0.903 | 0.5452 | 0.44 | 0.0 | 0.903 | 0.045 | -0.4185 | 0.0 |
| CosMx PDAC metastasis | ligand receptor recovery | Spatial stats | 6 | 0.3846 | 0.6154 | -0.1046 | 0.3846 | 0.0 | 1.0 | 0.4783 | 0.3846 | 0.039 | 0.1135 | 0.5089 |
| CosMx PDAC metastasis | ligand receptor recovery | ContextGate | 6 | 0.3914 | 0.6086 | -0.1114 | 0.3914 | 0.0 | 1.0 | 0.4 | 0.3914 | 0.041 | 0.1067 | 0.5021 |
| CosMx PDAC metastasis | ligand receptor recovery | Expression only | 6 | 0.498 | 0.502 | -0.218 | 0.498 | 0.0 | 1.0 | 0.0 | 0.498 | 0.035 | 0.0 | 0.3954 |
| CosMx PDAC metastasis | ligand receptor recovery | LR/pathway | 6 | 0.6259 | 0.3741 | -0.3459 | 0.6259 | 0.0 | 1.0 | 0.4348 | 0.6259 | 0.04 | -0.1278 | 0.2676 |
| CosMx PDAC metastasis | ligand receptor recovery | Random control | 6 | 0.8935 | 0.1065 | -0.6135 | 0.8935 | 0.5452 | 0.44 | 0.0 | 0.8935 | 0.037 | -0.3954 | 0.0 |
| CosMx PDAC metastasis | ligand receptor recovery | Always context | 6 | 0.8935 | 0.1065 | -0.6135 | 0.8935 | 0.5452 | 0.44 | 0.0 | 0.8935 | 0.0433 | -0.3954 | 0.0 |
| CosMx PDAC metastasis | ligand receptor recovery | Coord. shuffled | 6 | 0.8935 | 0.1065 | -0.6135 | 0.8935 | 0.5452 | 0.44 | 0.0 | 0.8935 | 0.0417 | -0.3955 | -0.0 |
| Xenium breast 5K | ligand receptor recovery | Spatial stats | 4 | 0.3832 | 0.6168 | -0.1032 | 0.3832 | 0.0 | 1.0 | 0.4783 | 0.3832 | 0.044 | 0.1114 | 0.5127 |
| Xenium breast 5K | ligand receptor recovery | ContextGate | 4 | 0.3885 | 0.6115 | -0.1085 | 0.3885 | 0.0 | 1.0 | 0.4 | 0.3885 | 0.046 | 0.1061 | 0.5074 |
| Xenium breast 5K | ligand receptor recovery | Expression only | 4 | 0.4946 | 0.5054 | -0.2146 | 0.4946 | 0.0 | 1.0 | 0.0 | 0.4946 | 0.04 | 0.0 | 0.4013 |
| Xenium breast 5K | ligand receptor recovery | LR/pathway | 4 | 0.6296 | 0.3704 | -0.3496 | 0.6296 | 0.0 | 1.0 | 0.4348 | 0.6296 | 0.034 | -0.135 | 0.2662 |
| Xenium breast 5K | ligand receptor recovery | Random control | 4 | 0.8894 | 0.1106 | -0.6094 | 0.8894 | 0.5452 | 0.44 | 0.0 | 0.8894 | 0.042 | -0.3949 | 0.0064 |
| Xenium breast 5K | ligand receptor recovery | Always context | 4 | 0.8959 | 0.1041 | -0.6159 | 0.8959 | 0.5452 | 0.44 | 0.0 | 0.8959 | 0.041 | -0.4013 | 0.0 |
| Xenium breast 5K | ligand receptor recovery | Coord. shuffled | 4 | 0.8965 | 0.1035 | -0.6165 | 0.8965 | 0.5452 | 0.44 | 0.0 | 0.8965 | 0.0375 | -0.4019 | -0.0007 |
| Xenium breast biomarkers | ligand receptor recovery | Spatial stats | 6 | 0.3805 | 0.6195 | -0.1005 | 0.3805 | 0.0 | 1.0 | 0.4783 | 0.3805 | 0.043 | 0.1071 | 0.5212 |
| Xenium breast biomarkers | ligand receptor recovery | ContextGate | 6 | 0.4009 | 0.5991 | -0.1209 | 0.4009 | 0.0 | 1.0 | 0.4 | 0.4009 | 0.045 | 0.0868 | 0.5008 |
| Xenium breast biomarkers | ligand receptor recovery | Expression only | 6 | 0.4876 | 0.5124 | -0.2076 | 0.4876 | 0.0 | 1.0 | 0.0 | 0.4876 | 0.039 | 0.0 | 0.4141 |
| Xenium breast biomarkers | ligand receptor recovery | LR/pathway | 6 | 0.624 | 0.376 | -0.344 | 0.624 | 0.0 | 1.0 | 0.4348 | 0.624 | 0.0367 | -0.1364 | 0.2777 |
| Xenium breast biomarkers | ligand receptor recovery | Random control | 6 | 0.8884 | 0.1116 | -0.6084 | 0.8884 | 0.5452 | 0.44 | 0.0 | 0.8884 | 0.041 | -0.4008 | 0.0132 |
| Xenium breast biomarkers | ligand receptor recovery | Coord. shuffled | 6 | 0.8984 | 0.1016 | -0.6184 | 0.8984 | 0.5452 | 0.44 | 0.0 | 0.8984 | 0.0383 | -0.4108 | 0.0033 |
| Xenium breast biomarkers | ligand receptor recovery | Always context | 6 | 0.9017 | 0.0983 | -0.6217 | 0.9017 | 0.5452 | 0.44 | 0.0 | 0.9017 | 0.04 | -0.4141 | 0.0 |
| CosMx BCC 6K | masked gene reconstruction | Spatial stats | 6 | 0.1826 | 0.8174 | 0.0974 | 0.1826 | 0.0 | 1.0 | 0.4783 | 0.1826 | 0.039 | 0.1565 | 0.6858 |
| CosMx BCC 6K | masked gene reconstruction | ContextGate | 6 | 0.2098 | 0.7902 | 0.0702 | 0.2098 | 0.0 | 1.0 | 0.4 | 0.2098 | 0.041 | 0.1293 | 0.6585 |
| CosMx BCC 6K | masked gene reconstruction | Expression only | 6 | 0.3391 | 0.6609 | -0.0591 | 0.3391 | 0.0 | 1.0 | 0.0 | 0.3391 | 0.035 | 0.0 | 0.5293 |
| CosMx BCC 6K | masked gene reconstruction | LR/pathway | 6 | 0.5107 | 0.4893 | -0.2307 | 0.5107 | 0.0 | 1.0 | 0.4348 | 0.5107 | 0.04 | -0.1716 | 0.3576 |
| CosMx BCC 6K | masked gene reconstruction | Coord. shuffled | 6 | 0.865 | 0.135 | -0.585 | 0.865 | 0.5452 | 0.44 | 0.0 | 0.865 | 0.0417 | -0.5259 | 0.0033 |
| CosMx BCC 6K | masked gene reconstruction | Always context | 6 | 0.8684 | 0.1316 | -0.5884 | 0.8684 | 0.5452 | 0.44 | 0.0 | 0.8684 | 0.0433 | -0.5293 | 0.0 |
| CosMx BCC 6K | masked gene reconstruction | Random control | 6 | 0.8747 | 0.1253 | -0.5947 | 0.8747 | 0.5452 | 0.44 | 0.0 | 0.8747 | 0.037 | -0.5356 | -0.0064 |
| CosMx NSCLC | masked gene reconstruction | Spatial stats | 4 | 0.1945 | 0.8055 | 0.0855 | 0.1945 | 0.0 | 1.0 | 0.4783 | 0.1945 | 0.044 | 0.1483 | 0.6779 |
| CosMx NSCLC | masked gene reconstruction | ContextGate | 4 | 0.2136 | 0.7864 | 0.0664 | 0.2136 | 0.0 | 1.0 | 0.4 | 0.2136 | 0.046 | 0.1291 | 0.6588 |
| CosMx NSCLC | masked gene reconstruction | Expression only | 4 | 0.3427 | 0.6573 | -0.0627 | 0.3427 | 0.0 | 1.0 | 0.0 | 0.3427 | 0.04 | 0.0 | 0.5296 |
| CosMx NSCLC | masked gene reconstruction | LR/pathway | 4 | 0.5047 | 0.4953 | -0.2247 | 0.5047 | 0.0 | 1.0 | 0.4348 | 0.5047 | 0.034 | -0.1619 | 0.3677 |
| CosMx NSCLC | masked gene reconstruction | Random control | 4 | 0.8709 | 0.1291 | -0.5909 | 0.8709 | 0.5452 | 0.44 | 0.0 | 0.8709 | 0.042 | -0.5281 | 0.0015 |
| CosMx NSCLC | masked gene reconstruction | Always context | 4 | 0.8724 | 0.1276 | -0.5924 | 0.8724 | 0.5452 | 0.44 | 0.0 | 0.8724 | 0.041 | -0.5296 | 0.0 |
| CosMx NSCLC | masked gene reconstruction | Coord. shuffled | 4 | 0.8726 | 0.1274 | -0.5926 | 0.8726 | 0.5452 | 0.44 | 0.0 | 0.8726 | 0.0375 | -0.5299 | -0.0003 |
| CosMx PDAC 1K | masked gene reconstruction | Spatial stats | 6 | 0.1897 | 0.8103 | 0.0903 | 0.1897 | 0.0 | 1.0 | 0.4783 | 0.1897 | 0.041 | 0.1428 | 0.6754 |
| CosMx PDAC 1K | masked gene reconstruction | ContextGate | 6 | 0.2077 | 0.7923 | 0.0723 | 0.2077 | 0.0 | 1.0 | 0.4 | 0.2077 | 0.043 | 0.1248 | 0.6574 |
| CosMx PDAC 1K | masked gene reconstruction | Expression only | 6 | 0.3325 | 0.6675 | -0.0525 | 0.3325 | 0.0 | 1.0 | 0.0 | 0.3325 | 0.037 | 0.0 | 0.5326 |
| CosMx PDAC 1K | masked gene reconstruction | LR/pathway | 6 | 0.5181 | 0.4819 | -0.2381 | 0.5181 | 0.0 | 1.0 | 0.4348 | 0.5181 | 0.0383 | -0.1856 | 0.347 |
| CosMx PDAC 1K | masked gene reconstruction | Always context | 6 | 0.8651 | 0.1349 | -0.5851 | 0.8651 | 0.5452 | 0.44 | 0.0 | 0.8651 | 0.0417 | -0.5326 | 0.0 |
| CosMx PDAC 1K | masked gene reconstruction | Coord. shuffled | 6 | 0.8701 | 0.1299 | -0.5901 | 0.8701 | 0.5452 | 0.44 | 0.0 | 0.8701 | 0.04 | -0.5376 | -0.005 |
| CosMx PDAC 1K | masked gene reconstruction | Random control | 6 | 0.8703 | 0.1297 | -0.5903 | 0.8703 | 0.5452 | 0.44 | 0.0 | 0.8703 | 0.039 | -0.5378 | -0.0052 |
| CosMx PDAC metastasis | masked gene reconstruction | Spatial stats | 6 | 0.1914 | 0.8086 | 0.0886 | 0.1914 | 0.0 | 1.0 | 0.4783 | 0.1914 | 0.043 | 0.1489 | 0.6826 |
| CosMx PDAC metastasis | masked gene reconstruction | ContextGate | 6 | 0.2058 | 0.7942 | 0.0742 | 0.2058 | 0.0 | 1.0 | 0.4 | 0.2058 | 0.045 | 0.1345 | 0.6682 |
| CosMx PDAC metastasis | masked gene reconstruction | Expression only | 6 | 0.3403 | 0.6597 | -0.0603 | 0.3403 | 0.0 | 1.0 | 0.0 | 0.3403 | 0.039 | 0.0 | 0.5337 |
| CosMx PDAC metastasis | masked gene reconstruction | LR/pathway | 6 | 0.5183 | 0.4817 | -0.2383 | 0.5183 | 0.0 | 1.0 | 0.4348 | 0.5183 | 0.0367 | -0.178 | 0.3556 |
| CosMx PDAC metastasis | masked gene reconstruction | Random control | 6 | 0.8655 | 0.1345 | -0.5855 | 0.8655 | 0.5452 | 0.44 | 0.0 | 0.8655 | 0.041 | -0.5253 | 0.0084 |
| CosMx PDAC metastasis | masked gene reconstruction | Coord. shuffled | 6 | 0.87 | 0.13 | -0.59 | 0.87 | 0.5452 | 0.44 | 0.0 | 0.87 | 0.0383 | -0.5297 | 0.004 |
| CosMx PDAC metastasis | masked gene reconstruction | Always context | 6 | 0.8739 | 0.1261 | -0.5939 | 0.8739 | 0.5452 | 0.44 | 0.0 | 0.8739 | 0.04 | -0.5337 | 0.0 |
| Xenium breast 5K | masked gene reconstruction | Spatial stats | 4 | 0.1973 | 0.8027 | 0.0827 | 0.1973 | 0.0 | 1.0 | 0.4783 | 0.1973 | 0.0425 | 0.1373 | 0.6745 |
| Xenium breast 5K | masked gene reconstruction | ContextGate | 4 | 0.2161 | 0.7839 | 0.0639 | 0.2161 | 0.0 | 1.0 | 0.4 | 0.2161 | 0.039 | 0.1185 | 0.6557 |
| Xenium breast 5K | masked gene reconstruction | Expression only | 4 | 0.3346 | 0.6654 | -0.0546 | 0.3346 | 0.0 | 1.0 | 0.0 | 0.3346 | 0.044 | 0.0 | 0.5372 |
| Xenium breast 5K | masked gene reconstruction | LR/pathway | 4 | 0.511 | 0.489 | -0.231 | 0.511 | 0.0 | 1.0 | 0.4348 | 0.511 | 0.038 | -0.1764 | 0.3608 |
| Xenium breast 5K | masked gene reconstruction | Random control | 4 | 0.8643 | 0.1357 | -0.5843 | 0.8643 | 0.5452 | 0.44 | 0.0 | 0.8643 | 0.046 | -0.5297 | 0.0075 |
| Xenium breast 5K | masked gene reconstruction | Coord. shuffled | 4 | 0.8672 | 0.1328 | -0.5872 | 0.8672 | 0.5452 | 0.44 | 0.0 | 0.8672 | 0.036 | -0.5327 | 0.0046 |
| Xenium breast 5K | masked gene reconstruction | Always context | 4 | 0.8718 | 0.1282 | -0.5918 | 0.8718 | 0.5452 | 0.44 | 0.0 | 0.8718 | 0.034 | -0.5372 | 0.0 |
| Xenium breast biomarkers | masked gene reconstruction | Spatial stats | 6 | 0.1854 | 0.8146 | 0.0946 | 0.1854 | 0.0 | 1.0 | 0.4783 | 0.1854 | 0.0433 | 0.1517 | 0.6801 |
| Xenium breast biomarkers | masked gene reconstruction | ContextGate | 6 | 0.2135 | 0.7865 | 0.0665 | 0.2135 | 0.0 | 1.0 | 0.4 | 0.2135 | 0.0417 | 0.1236 | 0.6519 |
| Xenium breast biomarkers | masked gene reconstruction | Expression only | 6 | 0.3371 | 0.6629 | -0.0571 | 0.3371 | 0.0 | 1.0 | 0.0 | 0.3371 | 0.043 | 0.0 | 0.5283 |
| Xenium breast biomarkers | masked gene reconstruction | LR/pathway | 6 | 0.5102 | 0.4898 | -0.2302 | 0.5102 | 0.0 | 1.0 | 0.4348 | 0.5102 | 0.037 | -0.1731 | 0.3552 |
| Xenium breast biomarkers | masked gene reconstruction | Always context | 6 | 0.8654 | 0.1346 | -0.5854 | 0.8654 | 0.5452 | 0.44 | 0.0 | 0.8654 | 0.0367 | -0.5283 | 0.0 |
| Xenium breast biomarkers | masked gene reconstruction | Random control | 6 | 0.8689 | 0.1311 | -0.5889 | 0.8689 | 0.5452 | 0.44 | 0.0 | 0.8689 | 0.045 | -0.5318 | -0.0035 |
| Xenium breast biomarkers | masked gene reconstruction | Coord. shuffled | 6 | 0.8699 | 0.1301 | -0.5899 | 0.8699 | 0.5452 | 0.44 | 0.0 | 0.8699 | 0.035 | -0.5329 | -0.0045 |
| CosMx BCC 6K | positive null control ladder | ContextGate | 6 | 0.2177 | 0.7823 | 0.0623 | 0.2177 | 0.0 | 1.0 | 0.3333 | 0.2177 | 0.043 | 0.3796 | 0.3734 |
| CosMx BCC 6K | positive null control ladder | LR/pathway | 6 | 0.348 | 0.652 | -0.068 | 0.348 | 0.38 | 0.7763 | 0.1667 | 0.348 | 0.0383 | 0.2494 | 0.2431 |
| CosMx BCC 6K | positive null control ladder | Spatial stats | 6 | 0.4786 | 0.5214 | -0.1986 | 0.4786 | 0.38 | 0.6097 | 0.3333 | 0.4786 | 0.041 | 0.1187 | 0.1125 |
| CosMx BCC 6K | positive null control ladder | Always context | 6 | 0.5911 | 0.4089 | -0.3111 | 0.5911 | 1.0 | 0.35 | 0.0 | 0.5911 | 0.0417 | 0.0062 | 0.0 |
| CosMx BCC 6K | positive null control ladder | Expression only | 6 | 0.5973 | 0.4027 | -0.3173 | 0.5973 | 0.0 | 0.5 | 0.0 | 0.5973 | 0.037 | 0.0 | -0.0062 |
| CosMx BCC 6K | positive null control ladder | Coord. shuffled | 6 | 0.9798 | 0.0202 | -0.6998 | 0.9798 | 1.0 | 0.0 | 0.0 | 0.9798 | 0.04 | -0.3824 | -0.3887 |
| CosMx BCC 6K | positive null control ladder | Random control | 6 | 0.9877 | 0.0123 | -0.7077 | 0.9877 | 1.0 | 0.0 | 0.0 | 0.9877 | 0.039 | -0.3904 | -0.3966 |
| CosMx NSCLC | positive null control ladder | ContextGate | 4 | 0.2358 | 0.7642 | 0.0442 | 0.2358 | 0.0 | 1.0 | 0.3333 | 0.2358 | 0.0425 | 0.3628 | 0.3622 |
| CosMx NSCLC | positive null control ladder | LR/pathway | 4 | 0.3493 | 0.6507 | -0.0693 | 0.3493 | 0.38 | 0.7763 | 0.1667 | 0.3493 | 0.036 | 0.2494 | 0.2488 |
| CosMx NSCLC | positive null control ladder | Spatial stats | 4 | 0.4732 | 0.5268 | -0.1932 | 0.4732 | 0.38 | 0.6097 | 0.3333 | 0.4732 | 0.046 | 0.1254 | 0.1248 |
| CosMx NSCLC | positive null control ladder | Always context | 4 | 0.598 | 0.402 | -0.318 | 0.598 | 1.0 | 0.35 | 0.0 | 0.598 | 0.0375 | 0.0006 | 0.0 |
| CosMx NSCLC | positive null control ladder | Expression only | 4 | 0.5986 | 0.4014 | -0.3186 | 0.5986 | 0.0 | 0.5 | 0.0 | 0.5986 | 0.042 | 0.0 | -0.0006 |
| CosMx NSCLC | positive null control ladder | Random control | 4 | 0.9806 | 0.0194 | -0.7006 | 0.9806 | 1.0 | 0.0 | 0.0 | 0.9806 | 0.044 | -0.3819 | -0.3825 |
| CosMx NSCLC | positive null control ladder | Coord. shuffled | 4 | 0.9809 | 0.0191 | -0.7009 | 0.9809 | 1.0 | 0.0 | 0.0 | 0.9809 | 0.034 | -0.3823 | -0.3829 |
| CosMx PDAC 1K | positive null control ladder | ContextGate | 6 | 0.2175 | 0.7825 | 0.0625 | 0.2175 | 0.0 | 1.0 | 0.3333 | 0.2175 | 0.045 | 0.3919 | 0.3795 |
| CosMx PDAC 1K | positive null control ladder | LR/pathway | 6 | 0.3568 | 0.6432 | -0.0768 | 0.3568 | 0.38 | 0.7763 | 0.1667 | 0.3568 | 0.0367 | 0.2525 | 0.2401 |
| CosMx PDAC 1K | positive null control ladder | Spatial stats | 6 | 0.4771 | 0.5229 | -0.1971 | 0.4771 | 0.38 | 0.6097 | 0.3333 | 0.4771 | 0.043 | 0.1322 | 0.1198 |
| CosMx PDAC 1K | positive null control ladder | Always context | 6 | 0.5969 | 0.4031 | -0.3169 | 0.5969 | 1.0 | 0.35 | 0.0 | 0.5969 | 0.04 | 0.0124 | 0.0 |
| CosMx PDAC 1K | positive null control ladder | Expression only | 6 | 0.6093 | 0.3907 | -0.3293 | 0.6093 | 0.0 | 0.5 | 0.0 | 0.6093 | 0.039 | 0.0 | -0.0124 |
| CosMx PDAC 1K | positive null control ladder | Coord. shuffled | 6 | 0.9726 | 0.0274 | -0.6926 | 0.9726 | 1.0 | 0.0 | 0.0 | 0.9726 | 0.0383 | -0.3633 | -0.3757 |
| CosMx PDAC 1K | positive null control ladder | Random control | 6 | 0.9762 | 0.0238 | -0.6962 | 0.9762 | 1.0 | 0.0 | 0.0 | 0.9762 | 0.041 | -0.3669 | -0.3793 |
| CosMx PDAC metastasis | positive null control ladder | ContextGate | 6 | 0.2244 | 0.7756 | 0.0556 | 0.2244 | 0.0 | 1.0 | 0.3333 | 0.2244 | 0.0433 | 0.376 | 0.3811 |
| CosMx PDAC metastasis | positive null control ladder | LR/pathway | 6 | 0.3495 | 0.6505 | -0.0695 | 0.3495 | 0.38 | 0.7763 | 0.1667 | 0.3495 | 0.035 | 0.2509 | 0.256 |
| CosMx PDAC metastasis | positive null control ladder | Spatial stats | 6 | 0.4803 | 0.5197 | -0.2003 | 0.4803 | 0.38 | 0.6097 | 0.3333 | 0.4803 | 0.045 | 0.1201 | 0.1252 |
| CosMx PDAC metastasis | positive null control ladder | Expression only | 6 | 0.6004 | 0.3996 | -0.3204 | 0.6004 | 0.0 | 0.5 | 0.0 | 0.6004 | 0.041 | 0.0 | 0.0051 |
| CosMx PDAC metastasis | positive null control ladder | Always context | 6 | 0.6054 | 0.3946 | -0.3254 | 0.6054 | 1.0 | 0.35 | 0.0 | 0.6054 | 0.0383 | -0.0051 | 0.0 |
| CosMx PDAC metastasis | positive null control ladder | Random control | 6 | 0.9822 | 0.0178 | -0.7022 | 0.9822 | 1.0 | 0.0 | 0.0 | 0.9822 | 0.043 | -0.3818 | -0.3767 |
| CosMx PDAC metastasis | positive null control ladder | Coord. shuffled | 6 | 0.9897 | 0.0103 | -0.7097 | 0.9897 | 1.0 | 0.0 | 0.0 | 0.9897 | 0.0367 | -0.3893 | -0.3842 |
| Xenium breast 5K | positive null control ladder | ContextGate | 4 | 0.2214 | 0.7786 | 0.0586 | 0.2214 | 0.0 | 1.0 | 0.3333 | 0.2214 | 0.041 | 0.392 | 0.3724 |
| Xenium breast 5K | positive null control ladder | LR/pathway | 4 | 0.3542 | 0.6458 | -0.0742 | 0.3542 | 0.38 | 0.7763 | 0.1667 | 0.3542 | 0.04 | 0.2592 | 0.2396 |
| Xenium breast 5K | positive null control ladder | Spatial stats | 4 | 0.4816 | 0.5184 | -0.2016 | 0.4816 | 0.38 | 0.6097 | 0.3333 | 0.4816 | 0.039 | 0.1318 | 0.1122 |
| Xenium breast 5K | positive null control ladder | Always context | 4 | 0.5938 | 0.4062 | -0.3138 | 0.5938 | 1.0 | 0.35 | 0.0 | 0.5938 | 0.036 | 0.0196 | 0.0 |
| Xenium breast 5K | positive null control ladder | Expression only | 4 | 0.6134 | 0.3866 | -0.3334 | 0.6134 | 0.0 | 0.5 | 0.0 | 0.6134 | 0.046 | 0.0 | -0.0196 |
| Xenium breast 5K | positive null control ladder | Random control | 4 | 0.9847 | 0.0153 | -0.7047 | 0.9847 | 1.0 | 0.0 | 0.0 | 0.9847 | 0.0425 | -0.3712 | -0.3908 |
| Xenium breast 5K | positive null control ladder | Coord. shuffled | 4 | 0.9868 | 0.0132 | -0.7068 | 0.9868 | 1.0 | 0.0 | 0.0 | 0.9868 | 0.038 | -0.3734 | -0.393 |
| Xenium breast biomarkers | positive null control ladder | ContextGate | 6 | 0.226 | 0.774 | 0.054 | 0.226 | 0.0 | 1.0 | 0.3333 | 0.226 | 0.04 | 0.3782 | 0.3822 |
| Xenium breast biomarkers | positive null control ladder | LR/pathway | 6 | 0.3477 | 0.6523 | -0.0677 | 0.3477 | 0.38 | 0.7763 | 0.1667 | 0.3477 | 0.039 | 0.2565 | 0.2605 |
| Xenium breast biomarkers | positive null control ladder | Spatial stats | 6 | 0.468 | 0.532 | -0.188 | 0.468 | 0.38 | 0.6097 | 0.3333 | 0.468 | 0.0417 | 0.1363 | 0.1403 |
| Xenium breast biomarkers | positive null control ladder | Expression only | 6 | 0.6043 | 0.3957 | -0.3243 | 0.6043 | 0.0 | 0.5 | 0.0 | 0.6043 | 0.045 | 0.0 | 0.004 |
| Xenium breast biomarkers | positive null control ladder | Always context | 6 | 0.6082 | 0.3918 | -0.3282 | 0.6082 | 1.0 | 0.35 | 0.0 | 0.6082 | 0.035 | -0.004 | 0.0 |
| Xenium breast biomarkers | positive null control ladder | Coord. shuffled | 6 | 0.9818 | 0.0182 | -0.7018 | 0.9818 | 1.0 | 0.0 | 0.0 | 0.9818 | 0.037 | -0.3775 | -0.3736 |
| Xenium breast biomarkers | positive null control ladder | Random control | 6 | 0.9843 | 0.0157 | -0.7043 | 0.9843 | 1.0 | 0.0 | 0.0 | 0.9843 | 0.0433 | -0.3801 | -0.3761 |
| CosMx BCC 6K | residual pathway module prediction | Spatial stats | 6 | 0.4163 | 0.5837 | -0.1363 | 0.4163 | 0.0 | 1.0 | 0.4783 | 0.4163 | 0.0417 | 0.1106 | 0.4837 |
| CosMx BCC 6K | residual pathway module prediction | ContextGate | 6 | 0.4347 | 0.5653 | -0.1547 | 0.4347 | 0.0 | 1.0 | 0.4 | 0.4347 | 0.04 | 0.0922 | 0.4652 |
| CosMx BCC 6K | residual pathway module prediction | Expression only | 6 | 0.5269 | 0.4731 | -0.2469 | 0.5269 | 0.0 | 1.0 | 0.0 | 0.5269 | 0.045 | 0.0 | 0.373 |
| CosMx BCC 6K | residual pathway module prediction | LR/pathway | 6 | 0.6455 | 0.3545 | -0.3655 | 0.6455 | 0.0 | 1.0 | 0.4348 | 0.6455 | 0.039 | -0.1186 | 0.2544 |
| CosMx BCC 6K | residual pathway module prediction | Coord. shuffled | 6 | 0.8958 | 0.1042 | -0.6158 | 0.8958 | 0.5452 | 0.44 | 0.0 | 0.8958 | 0.037 | -0.3689 | 0.0042 |
| CosMx BCC 6K | residual pathway module prediction | Always context | 6 | 0.8999 | 0.1001 | -0.6199 | 0.8999 | 0.5452 | 0.44 | 0.0 | 0.8999 | 0.035 | -0.373 | 0.0 |
| CosMx BCC 6K | residual pathway module prediction | Random control | 6 | 0.901 | 0.099 | -0.621 | 0.901 | 0.5452 | 0.44 | 0.0 | 0.901 | 0.0433 | -0.3741 | -0.0011 |
| CosMx NSCLC | residual pathway module prediction | Spatial stats | 4 | 0.4128 | 0.5872 | -0.1328 | 0.4128 | 0.0 | 1.0 | 0.4783 | 0.4128 | 0.0375 | 0.1003 | 0.4877 |
| CosMx NSCLC | residual pathway module prediction | ContextGate | 4 | 0.4164 | 0.5836 | -0.1364 | 0.4164 | 0.0 | 1.0 | 0.4 | 0.4164 | 0.034 | 0.0966 | 0.4841 |
| CosMx NSCLC | residual pathway module prediction | Expression only | 4 | 0.513 | 0.487 | -0.233 | 0.513 | 0.0 | 1.0 | 0.0 | 0.513 | 0.039 | 0.0 | 0.3875 |
| CosMx NSCLC | residual pathway module prediction | LR/pathway | 4 | 0.6459 | 0.3541 | -0.3659 | 0.6459 | 0.0 | 1.0 | 0.4348 | 0.6459 | 0.044 | -0.1328 | 0.2547 |
| CosMx NSCLC | residual pathway module prediction | Coord. shuffled | 4 | 0.8987 | 0.1013 | -0.6187 | 0.8987 | 0.5452 | 0.44 | 0.0 | 0.8987 | 0.042 | -0.3857 | 0.0018 |
| CosMx NSCLC | residual pathway module prediction | Always context | 4 | 0.9005 | 0.0995 | -0.6205 | 0.9005 | 0.5452 | 0.44 | 0.0 | 0.9005 | 0.04 | -0.3875 | 0.0 |
| CosMx NSCLC | residual pathway module prediction | Random control | 4 | 0.9126 | 0.0874 | -0.6326 | 0.9126 | 0.5452 | 0.44 | 0.0 | 0.9126 | 0.041 | -0.3995 | -0.0121 |
| CosMx PDAC 1K | residual pathway module prediction | Spatial stats | 6 | 0.4121 | 0.5879 | -0.1321 | 0.4121 | 0.0 | 1.0 | 0.4783 | 0.4121 | 0.04 | 0.1023 | 0.4868 |
| CosMx PDAC 1K | residual pathway module prediction | ContextGate | 6 | 0.4337 | 0.5663 | -0.1537 | 0.4337 | 0.0 | 1.0 | 0.4 | 0.4337 | 0.0383 | 0.0807 | 0.4652 |
| CosMx PDAC 1K | residual pathway module prediction | Expression only | 6 | 0.5144 | 0.4856 | -0.2344 | 0.5144 | 0.0 | 1.0 | 0.0 | 0.5144 | 0.0433 | 0.0 | 0.3845 |
| CosMx PDAC 1K | residual pathway module prediction | LR/pathway | 6 | 0.6508 | 0.3492 | -0.3708 | 0.6508 | 0.0 | 1.0 | 0.4348 | 0.6508 | 0.041 | -0.1364 | 0.2481 |
| CosMx PDAC 1K | residual pathway module prediction | Always context | 6 | 0.8989 | 0.1011 | -0.6189 | 0.8989 | 0.5452 | 0.44 | 0.0 | 0.8989 | 0.037 | -0.3845 | 0.0 |
| CosMx PDAC 1K | residual pathway module prediction | Random control | 6 | 0.9028 | 0.0972 | -0.6228 | 0.9028 | 0.5452 | 0.44 | 0.0 | 0.9028 | 0.0417 | -0.3885 | -0.0039 |
| CosMx PDAC 1K | residual pathway module prediction | Coord. shuffled | 6 | 0.9049 | 0.0951 | -0.6249 | 0.9049 | 0.5452 | 0.44 | 0.0 | 0.9049 | 0.039 | -0.3905 | -0.006 |
| CosMx PDAC metastasis | residual pathway module prediction | Spatial stats | 6 | 0.4084 | 0.5916 | -0.1284 | 0.4084 | 0.0 | 1.0 | 0.4783 | 0.4084 | 0.0383 | 0.1069 | 0.4951 |
| CosMx PDAC metastasis | residual pathway module prediction | ContextGate | 6 | 0.4272 | 0.5728 | -0.1472 | 0.4272 | 0.0 | 1.0 | 0.4 | 0.4272 | 0.0367 | 0.0881 | 0.4763 |
| CosMx PDAC metastasis | residual pathway module prediction | Expression only | 6 | 0.5152 | 0.4848 | -0.2352 | 0.5152 | 0.0 | 1.0 | 0.0 | 0.5152 | 0.0417 | 0.0 | 0.3882 |
| CosMx PDAC metastasis | residual pathway module prediction | LR/pathway | 6 | 0.6478 | 0.3522 | -0.3678 | 0.6478 | 0.0 | 1.0 | 0.4348 | 0.6478 | 0.043 | -0.1326 | 0.2556 |
| CosMx PDAC metastasis | residual pathway module prediction | Random control | 6 | 0.8909 | 0.1091 | -0.6109 | 0.8909 | 0.5452 | 0.44 | 0.0 | 0.8909 | 0.04 | -0.3756 | 0.0126 |
| CosMx PDAC metastasis | residual pathway module prediction | Coord. shuffled | 6 | 0.8999 | 0.1001 | -0.6199 | 0.8999 | 0.5452 | 0.44 | 0.0 | 0.8999 | 0.041 | -0.3847 | 0.0035 |
| CosMx PDAC metastasis | residual pathway module prediction | Always context | 6 | 0.9035 | 0.0965 | -0.6235 | 0.9035 | 0.5452 | 0.44 | 0.0 | 0.9035 | 0.039 | -0.3882 | 0.0 |
| Xenium breast 5K | residual pathway module prediction | Spatial stats | 4 | 0.4207 | 0.5793 | -0.1407 | 0.4207 | 0.0 | 1.0 | 0.4783 | 0.4207 | 0.036 | 0.0952 | 0.4869 |
| Xenium breast 5K | residual pathway module prediction | ContextGate | 4 | 0.4322 | 0.5678 | -0.1522 | 0.4322 | 0.0 | 1.0 | 0.4 | 0.4322 | 0.038 | 0.0838 | 0.4754 |
| Xenium breast 5K | residual pathway module prediction | Expression only | 4 | 0.516 | 0.484 | -0.236 | 0.516 | 0.0 | 1.0 | 0.0 | 0.516 | 0.0375 | 0.0 | 0.3916 |
| Xenium breast 5K | residual pathway module prediction | LR/pathway | 4 | 0.6461 | 0.3539 | -0.3661 | 0.6461 | 0.0 | 1.0 | 0.4348 | 0.6461 | 0.0425 | -0.1301 | 0.2615 |
| Xenium breast 5K | residual pathway module prediction | Random control | 4 | 0.8977 | 0.1023 | -0.6177 | 0.8977 | 0.5452 | 0.44 | 0.0 | 0.8977 | 0.034 | -0.3817 | 0.01 |
| Xenium breast 5K | residual pathway module prediction | Coord. shuffled | 4 | 0.9035 | 0.0965 | -0.6235 | 0.9035 | 0.5452 | 0.44 | 0.0 | 0.9035 | 0.046 | -0.3875 | 0.0042 |
| Xenium breast 5K | residual pathway module prediction | Always context | 4 | 0.9076 | 0.0924 | -0.6276 | 0.9076 | 0.5452 | 0.44 | 0.0 | 0.9076 | 0.044 | -0.3916 | 0.0 |
| Xenium breast biomarkers | residual pathway module prediction | Spatial stats | 6 | 0.4185 | 0.5815 | -0.1385 | 0.4185 | 0.0 | 1.0 | 0.4783 | 0.4185 | 0.035 | 0.1082 | 0.4821 |
| Xenium breast biomarkers | residual pathway module prediction | ContextGate | 6 | 0.4228 | 0.5772 | -0.1428 | 0.4228 | 0.0 | 1.0 | 0.4 | 0.4228 | 0.037 | 0.1039 | 0.4778 |
| Xenium breast biomarkers | residual pathway module prediction | Expression only | 6 | 0.5267 | 0.4733 | -0.2467 | 0.5267 | 0.0 | 1.0 | 0.0 | 0.5267 | 0.0383 | 0.0 | 0.3739 |
| Xenium breast biomarkers | residual pathway module prediction | LR/pathway | 6 | 0.6476 | 0.3524 | -0.3676 | 0.6476 | 0.0 | 1.0 | 0.4348 | 0.6476 | 0.0433 | -0.1208 | 0.2531 |
| Xenium breast biomarkers | residual pathway module prediction | Coord. shuffled | 6 | 0.8995 | 0.1005 | -0.6195 | 0.8995 | 0.5452 | 0.44 | 0.0 | 0.8995 | 0.045 | -0.3727 | 0.0012 |
| Xenium breast biomarkers | residual pathway module prediction | Always context | 6 | 0.9007 | 0.0993 | -0.6207 | 0.9007 | 0.5452 | 0.44 | 0.0 | 0.9007 | 0.043 | -0.3739 | 0.0 |
| Xenium breast biomarkers | residual pathway module prediction | Random control | 6 | 0.9014 | 0.0986 | -0.6214 | 0.9014 | 0.5452 | 0.44 | 0.0 | 0.9014 | 0.0367 | -0.3746 | -0.0007 |
| CosMx BCC 6K | residual receptor prediction | Spatial stats | 6 | 0.4303 | 0.5697 | -0.1503 | 0.4303 | 0.0 | 1.0 | 0.4783 | 0.4303 | 0.0383 | 0.1022 | 0.4635 |
| CosMx BCC 6K | residual receptor prediction | ContextGate | 6 | 0.4412 | 0.5588 | -0.1612 | 0.4412 | 0.0 | 1.0 | 0.4 | 0.4412 | 0.0367 | 0.0913 | 0.4526 |
| CosMx BCC 6K | residual receptor prediction | Expression only | 6 | 0.5325 | 0.4675 | -0.2525 | 0.5325 | 0.0 | 1.0 | 0.0 | 0.5325 | 0.0417 | 0.0 | 0.3612 |
| CosMx BCC 6K | residual receptor prediction | LR/pathway | 6 | 0.6547 | 0.3453 | -0.3747 | 0.6547 | 0.0 | 1.0 | 0.4348 | 0.6547 | 0.043 | -0.1222 | 0.239 |
| CosMx BCC 6K | residual receptor prediction | Always context | 6 | 0.8938 | 0.1062 | -0.6138 | 0.8938 | 0.5452 | 0.44 | 0.0 | 0.8938 | 0.039 | -0.3612 | 0.0 |
| CosMx BCC 6K | residual receptor prediction | Random control | 6 | 0.8956 | 0.1044 | -0.6156 | 0.8956 | 0.5452 | 0.44 | 0.0 | 0.8956 | 0.04 | -0.3631 | -0.0018 |
| CosMx BCC 6K | residual receptor prediction | Coord. shuffled | 6 | 0.904 | 0.096 | -0.624 | 0.904 | 0.5452 | 0.44 | 0.0 | 0.904 | 0.041 | -0.3715 | -0.0102 |
| CosMx NSCLC | residual receptor prediction | Spatial stats | 4 | 0.4253 | 0.5747 | -0.1453 | 0.4253 | 0.0 | 1.0 | 0.4783 | 0.4253 | 0.036 | 0.1063 | 0.4895 |
| CosMx NSCLC | residual receptor prediction | ContextGate | 4 | 0.4356 | 0.5644 | -0.1556 | 0.4356 | 0.0 | 1.0 | 0.4 | 0.4356 | 0.038 | 0.096 | 0.4793 |
| CosMx NSCLC | residual receptor prediction | Expression only | 4 | 0.5316 | 0.4684 | -0.2516 | 0.5316 | 0.0 | 1.0 | 0.0 | 0.5316 | 0.0375 | 0.0 | 0.3832 |
| CosMx NSCLC | residual receptor prediction | LR/pathway | 4 | 0.6381 | 0.3619 | -0.3581 | 0.6381 | 0.0 | 1.0 | 0.4348 | 0.6381 | 0.0425 | -0.1065 | 0.2767 |
| CosMx NSCLC | residual receptor prediction | Coord. shuffled | 4 | 0.9073 | 0.0927 | -0.6273 | 0.9073 | 0.5452 | 0.44 | 0.0 | 0.9073 | 0.046 | -0.3757 | 0.0075 |
| CosMx NSCLC | residual receptor prediction | Always context | 4 | 0.9148 | 0.0852 | -0.6348 | 0.9148 | 0.5452 | 0.44 | 0.0 | 0.9148 | 0.044 | -0.3832 | 0.0 |
| CosMx NSCLC | residual receptor prediction | Random control | 4 | 0.9175 | 0.0825 | -0.6375 | 0.9175 | 0.5452 | 0.44 | 0.0 | 0.9175 | 0.034 | -0.3859 | -0.0027 |
| CosMx PDAC 1K | residual receptor prediction | Spatial stats | 6 | 0.4264 | 0.5736 | -0.1464 | 0.4264 | 0.0 | 1.0 | 0.4783 | 0.4264 | 0.0367 | 0.1023 | 0.4723 |
| CosMx PDAC 1K | residual receptor prediction | ContextGate | 6 | 0.4348 | 0.5652 | -0.1548 | 0.4348 | 0.0 | 1.0 | 0.4 | 0.4348 | 0.035 | 0.0939 | 0.4639 |
| CosMx PDAC 1K | residual receptor prediction | Expression only | 6 | 0.5287 | 0.4713 | -0.2487 | 0.5287 | 0.0 | 1.0 | 0.0 | 0.5287 | 0.04 | 0.0 | 0.37 |
| CosMx PDAC 1K | residual receptor prediction | LR/pathway | 6 | 0.6491 | 0.3509 | -0.3691 | 0.6491 | 0.0 | 1.0 | 0.4348 | 0.6491 | 0.045 | -0.1204 | 0.2496 |
| CosMx PDAC 1K | residual receptor prediction | Always context | 6 | 0.8987 | 0.1013 | -0.6187 | 0.8987 | 0.5452 | 0.44 | 0.0 | 0.8987 | 0.041 | -0.37 | 0.0 |
| CosMx PDAC 1K | residual receptor prediction | Random control | 6 | 0.9032 | 0.0968 | -0.6232 | 0.9032 | 0.5452 | 0.44 | 0.0 | 0.9032 | 0.0383 | -0.3745 | -0.0045 |
| CosMx PDAC 1K | residual receptor prediction | Coord. shuffled | 6 | 0.9116 | 0.0884 | -0.6316 | 0.9116 | 0.5452 | 0.44 | 0.0 | 0.9116 | 0.043 | -0.3829 | -0.0129 |
| CosMx PDAC metastasis | residual receptor prediction | Spatial stats | 6 | 0.4293 | 0.5707 | -0.1493 | 0.4293 | 0.0 | 1.0 | 0.4783 | 0.4293 | 0.035 | 0.1021 | 0.47 |
| CosMx PDAC metastasis | residual receptor prediction | ContextGate | 6 | 0.446 | 0.554 | -0.166 | 0.446 | 0.0 | 1.0 | 0.4 | 0.446 | 0.037 | 0.0854 | 0.4534 |
| CosMx PDAC metastasis | residual receptor prediction | Expression only | 6 | 0.5315 | 0.4685 | -0.2515 | 0.5315 | 0.0 | 1.0 | 0.0 | 0.5315 | 0.0383 | 0.0 | 0.3679 |
| CosMx PDAC metastasis | residual receptor prediction | LR/pathway | 6 | 0.6574 | 0.3426 | -0.3774 | 0.6574 | 0.0 | 1.0 | 0.4348 | 0.6574 | 0.0433 | -0.126 | 0.242 |
| CosMx PDAC metastasis | residual receptor prediction | Coord. shuffled | 6 | 0.893 | 0.107 | -0.613 | 0.893 | 0.5452 | 0.44 | 0.0 | 0.893 | 0.045 | -0.3615 | 0.0064 |
| CosMx PDAC metastasis | residual receptor prediction | Always context | 6 | 0.8994 | 0.1006 | -0.6194 | 0.8994 | 0.5452 | 0.44 | 0.0 | 0.8994 | 0.043 | -0.3679 | 0.0 |
| CosMx PDAC metastasis | residual receptor prediction | Random control | 6 | 0.9103 | 0.0897 | -0.6303 | 0.9103 | 0.5452 | 0.44 | 0.0 | 0.9103 | 0.0367 | -0.3788 | -0.0109 |
| Xenium breast 5K | residual receptor prediction | Spatial stats | 4 | 0.4397 | 0.5603 | -0.1597 | 0.4397 | 0.0 | 1.0 | 0.4783 | 0.4397 | 0.04 | 0.1037 | 0.466 |
| Xenium breast 5K | residual receptor prediction | ContextGate | 4 | 0.4477 | 0.5523 | -0.1677 | 0.4477 | 0.0 | 1.0 | 0.4 | 0.4477 | 0.042 | 0.0957 | 0.458 |
| Xenium breast 5K | residual receptor prediction | Expression only | 4 | 0.5434 | 0.4566 | -0.2634 | 0.5434 | 0.0 | 1.0 | 0.0 | 0.5434 | 0.036 | 0.0 | 0.3623 |
| Xenium breast 5K | residual receptor prediction | LR/pathway | 4 | 0.657 | 0.343 | -0.377 | 0.657 | 0.0 | 1.0 | 0.4348 | 0.657 | 0.041 | -0.1136 | 0.2487 |
| Xenium breast 5K | residual receptor prediction | Random control | 4 | 0.8966 | 0.1034 | -0.6166 | 0.8966 | 0.5452 | 0.44 | 0.0 | 0.8966 | 0.038 | -0.3532 | 0.0091 |
| Xenium breast 5K | residual receptor prediction | Coord. shuffled | 4 | 0.899 | 0.101 | -0.619 | 0.899 | 0.5452 | 0.44 | 0.0 | 0.899 | 0.039 | -0.3556 | 0.0067 |
| Xenium breast 5K | residual receptor prediction | Always context | 4 | 0.9057 | 0.0943 | -0.6257 | 0.9057 | 0.5452 | 0.44 | 0.0 | 0.9057 | 0.0425 | -0.3623 | 0.0 |
| Xenium breast biomarkers | residual receptor prediction | Spatial stats | 6 | 0.4354 | 0.5646 | -0.1554 | 0.4354 | 0.0 | 1.0 | 0.4783 | 0.4354 | 0.039 | 0.0966 | 0.4674 |
| Xenium breast biomarkers | residual receptor prediction | ContextGate | 6 | 0.4474 | 0.5526 | -0.1674 | 0.4474 | 0.0 | 1.0 | 0.4 | 0.4474 | 0.041 | 0.0846 | 0.4554 |
| Xenium breast biomarkers | residual receptor prediction | Expression only | 6 | 0.532 | 0.468 | -0.252 | 0.532 | 0.0 | 1.0 | 0.0 | 0.532 | 0.035 | 0.0 | 0.3708 |
| Xenium breast biomarkers | residual receptor prediction | LR/pathway | 6 | 0.6514 | 0.3486 | -0.3714 | 0.6514 | 0.0 | 1.0 | 0.4348 | 0.6514 | 0.04 | -0.1194 | 0.2514 |
| Xenium breast biomarkers | residual receptor prediction | Random control | 6 | 0.8935 | 0.1065 | -0.6135 | 0.8935 | 0.5452 | 0.44 | 0.0 | 0.8935 | 0.037 | -0.3615 | 0.0094 |
| Xenium breast biomarkers | residual receptor prediction | Always context | 6 | 0.9028 | 0.0972 | -0.6228 | 0.9028 | 0.5452 | 0.44 | 0.0 | 0.9028 | 0.0433 | -0.3708 | 0.0 |
| Xenium breast biomarkers | residual receptor prediction | Coord. shuffled | 6 | 0.9158 | 0.0842 | -0.6358 | 0.9158 | 0.5452 | 0.44 | 0.0 | 0.9158 | 0.0417 | -0.3838 | -0.013 |
