"""Build manuscript tables and claim-to-evidence audit for ContextGate-Bench."""
# ruff: noqa: E501

from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd
import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[1]
REPORT_ROOT = PROJECT_ROOT / "results" / "reports"
MANIFEST_ROOT = PROJECT_ROOT / "data" / "manifests"
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "manuscript" / "tables"

DATASET_LABELS = {
    "cosmx_6k_bcc_yerly_2024": "CosMx BCC 6K",
    "cosmx_nsclc_ffpe_v1": "CosMx NSCLC",
    "discovery_index_without_direct_artifact": "Discovery index",
    "gse277782_cosmx_pdac_metastasis": "CosMx PDAC metastasis",
    "gse310352_cosmx_pdac_1k": "CosMx PDAC 1K",
    "gse311609_xenium_lung_breast_validation": "GSE311609 Xenium",
    "htapp_mbc_scp2702_merfish": "HTAPP MBC MERFISH",
    "private_or_login_only_sources": "Private/login sources",
    "scrna_visium_deconvolution_cell_claim": "scRNA+Visium claim",
    "standard_visium_spot_level_only": "Spot-level Visium",
    "xenium_breast_biomarkers_v1": "Xenium breast biomarkers",
    "xenium_breast_v1": "Xenium breast 5K",
}

METHOD_LABELS = {
    "always_true_neighbor_mean": "Always context",
    "cellpack_packed_context_tiny": "CellPack tiny",
    "contextgate_transparent_router": "ContextGate",
    "coordinate_shuffled_control_model": "Coord. shuffled",
    "distant_neighbor_control_model": "Distant control",
    "expression_only_linear": "Expression only",
    "ligand_receptor_pathway_heuristic": "LR/pathway",
    "lightweight_graphsage_aggregation": "GraphSAGE style",
    "random_neighbor_control_model": "Random control",
    "spatial_statistics_heuristic": "Spatial stats",
}

ROUTE_LABELS = {
    "abstain_uncertain": "Abstain",
    "compressed_context": "Compressed context",
    "context_allowed": "Context allowed",
    "expression_only": "Expression only",
    "full_context": "Full context",
    "positive_control_only": "Positive-control only",
}

ROLE_LABELS = {
    "rejected_or_access_blocked": "Rejected/access blocked",
    "usable": "Included",
    "validation_frozen": "Validation frozen",
}

TIER_LABELS = {
    "mini": "Mini",
    "core": "Core",
    "q1": "Full benchmark",
}

AXIS_LABELS = {
    "cancer_or_tissue_contexts": "Cancer/tissue contexts",
    "control_families": "Control families",
    "core_factorial_jobs": "Core factorial jobs",
    "main_figures": "Main figures",
    "method_families": "Method families",
    "metric_families": "Metric families",
    "mini_factorial_jobs": "Mini factorial jobs",
    "platforms": "Platforms",
    "positive_control_levels": "Positive-control levels",
    "q1_factorial_jobs": "Full factorial jobs",
    "q1_nominal_jobs_soft_max": "Full jobs soft cap",
    "rejected_or_access_blocked_dataset_rows": "Rejected/access rows",
    "split_families": "Split families",
    "stochastic_seeds": "Seeds",
    "supplementary_tables": "Supplementary tables",
    "task_families": "Task families",
    "usable_dataset_backbone_rows": "Usable dataset rows",
}

CLAIM_TEXT = {
    "all_failed_stress_tests_have_downgrades": (
        "Failed stress tests carry explicit machine-readable downgrades."
    ),
    "contextgate_reduces_false_context": (
        "ContextGate preserves false-context safety while retaining "
        "positive-control sensitivity."
    ),
    "positive_null_ladder_detects_synthetic_signal": (
        "The benchmark detects injected neighbor-context signal and rejects "
        "null/confounded controls."
    ),
    "spatial_context_is_conditional_not_universal": (
        "Spatial neighbor context is conditional rather than universally useful."
    ),
    "strong_biological_context_claim": (
        "A strong biological context-benefit claim is not supported by the "
        "current strict gates."
    ),
    "wrong_context_controls_are_necessary": (
        "Wrong-context controls are required before making spatial-context claims."
    ),
}

CONTEXT_ROUTES = {"compressed_context", "context_allowed", "full_context"}

CP_Q7_STRESS_FILES = {
    "leave_one_out": "cp_q7_robustness_stress/leave_one_out_stress.csv",
    "threshold_sensitivity": ("cp_q7_robustness_stress/threshold_sensitivity.csv"),
    "seed_sweep": "cp_q7_robustness_stress/seed_sweep.csv",
    "contextgate_reason_ablation": (
        "cp_q7_robustness_stress/contextgate_reason_ablation.csv"
    ),
    "control_ablation": "cp_q7_robustness_stress/control_ablation.csv",
    "positive_control_ablation": (
        "cp_q7_robustness_stress/positive_control_ablation.csv"
    ),
    "compute_sensitivity": "cp_q7_robustness_stress/compute_sensitivity.csv",
}

METHOD_SCOPE_METADATA = {
    "expression_only_linear": {
        "family": "Expression-only or center-cell baseline",
        "rule": "Always route by center-cell expression only; no neighbor features used.",
        "tuning": "Deterministic registered baseline; no hyperparameter search.",
        "scope": "Safety floor and comparator, not a context-aware method.",
        "source": "src/cellpack/method_comparison.py; cp_q2_method_comparison",
    },
    "always_true_neighbor_mean": {
        "family": "Always-context true-neighbor baseline",
        "rule": "Always uses the true k-neighbor mean context feature.",
        "tuning": "Deterministic safety stress comparator; no tuning.",
        "scope": "High false-context exposure comparator, not recommended for claims.",
        "source": "src/cellpack/method_comparison.py; cp_q2_method_comparison",
    },
    "contextgate_transparent_router": {
        "family": "ContextGate transparent decision router",
        "rule": "Six-gate route rule with explicit abstention and downgrade reasons.",
        "tuning": "Registered conservative publication-facing gates; no result-time tuning.",
        "scope": "Preferred for auditable claim release, not because it maximizes raw utility.",
        "source": "src/cellpack/contextgate.py; cp_q5_contextgate_decisions",
    },
    "spatial_statistics_heuristic": {
        "family": "Spatial-statistics heuristic",
        "rule": "Context-utility score <=0.01 routes expression-only; >=0.65 routes context; otherwise abstains.",
        "tuning": "Registered thresholds from MethodComparisonConfig; no post-hoc sweep used for CP-Q2 ranking.",
        "scope": "Zero regret follows from matching the in-sample empirical oracle; it is not an absolute quality claim.",
        "source": "src/cellpack/method_comparison.py; cp_r1_context_utility_atlas",
    },
    "ligand_receptor_pathway_heuristic": {
        "family": "Ligand-receptor or pathway heuristic",
        "rule": "Frozen pair/module coverage plus context-utility score decides expression/context/abstain.",
        "tuning": "Uses data/manifests/ligand_receptor_pairs.tsv and fixed coverage thresholds.",
        "scope": "Panel-observability heuristic; does not infer causal communication.",
        "source": "data/manifests/ligand_receptor_pairs.tsv; src/cellpack/method_comparison.py",
    },
    "lightweight_graphsage_aggregation": {
        "family": "Graph-style context aggregation",
        "rule": "GraphSAGE-style proxy routes context when panel size >=900 and context-utility score >0.01.",
        "tuning": "Fixed k=5 within sample/slide graph proxy; no learned SOTA GNN hyperparameter search.",
        "scope": "Generic bounded graph comparator, not a claim about GraphST, STAGATE, SpaGCN, or all GNNs.",
        "source": "src/cellpack/method_comparison.py; Supplementary Table S28",
    },
    "cellpack_packed_context_tiny": {
        "family": "Tiny packed-context transformer-style baseline",
        "rule": "Small packed context model routes context only when context-utility score >=0.65.",
        "tuning": "Fixed a priori smoke-scale architecture: 1-2 layers, 4 heads, d_model 32/64, FF 64-128.",
        "scope": "64-128 measured genes cover 0.7%-23.6% of current panels; high-plex datasets are input-starved.",
        "source": "src/cellpack/method_comparison.py; data/manifests/contextgate_benchmark_manifest.yaml",
    },
    "random_neighbor_control_model": {
        "family": "Wrong-context random-neighbor control",
        "rule": "Uses random-neighbor context as a deliberately wrong-context safety control.",
        "tuning": "Deterministic control family; no tuning.",
        "scope": "Falsification control, not a deployable spatial model.",
        "source": "src/cellpack/method_comparison.py; cp_q2_method_comparison",
    },
    "coordinate_shuffled_control_model": {
        "family": "Wrong-context coordinate-shuffled control",
        "rule": "Uses coordinate-shuffled context as a deliberately wrong-context safety control.",
        "tuning": "Deterministic control family; no tuning.",
        "scope": "Falsification control, not a deployable spatial model.",
        "source": "src/cellpack/method_comparison.py; cp_q2_method_comparison",
    },
    "distant_neighbor_control_model": {
        "family": "Wrong-context distant-neighbor control",
        "rule": "Uses distant-neighbor context as a deliberately wrong-context safety control.",
        "tuning": "Deterministic control family; no tuning.",
        "scope": "Falsification control, not a deployable spatial model.",
        "source": "src/cellpack/method_comparison.py; cp_q2_method_comparison",
    },
}

FUTURE_METHOD_SCOPE_ROWS = [
    {
        "candidate": "SpatialDM",
        "category": "spatial ligand-receptor testing",
        "release_decision": "future_adapter",
        "primary_blocker": "Interaction p-values/scores require a CP-Q residual-utility adapter and a matched false-context denominator.",
        "future_adapter_note": "Evaluate as a CCC-specific route family after freezing task-specific LR output schemas.",
    },
    {
        "candidate": "SpaTalk",
        "category": "spatial cell-cell communication",
        "release_decision": "future_adapter",
        "primary_blocker": "Communication-network outputs are not CP-Q prediction rows without a supervised target adapter.",
        "future_adapter_note": "Use as a future CCC adapter once route labels and panel observability rules are fixed.",
    },
    {
        "candidate": "NicheCompass",
        "category": "niche-aware representation learning",
        "release_decision": "future_adapter",
        "primary_blocker": "Requires a representation-to-task head and fairness protocol before CP-Q utility/FCR rows exist.",
        "future_adapter_note": "Freeze embeddings and train the same CP-Q heads as other representation methods.",
    },
    {
        "candidate": "CellNeighborEX",
        "category": "neighbor-dependent expression modeling",
        "release_decision": "future_adapter",
        "primary_blocker": "Closest conceptual match, but still needs an adapter that emits CP-Q route predictions and controls.",
        "future_adapter_note": "High-priority future adapter for direct neighbor-expression replay.",
    },
    {
        "candidate": "STAGATE",
        "category": "graph attention spatial representation",
        "release_decision": "future_adapter",
        "primary_blocker": "Representation/domain objective differs from CP-Q supervised residual utility.",
        "future_adapter_note": "Freeze representations and compare under the CP-Q method-head contract.",
    },
    {
        "candidate": "SpaGCN",
        "category": "spatial graph convolution / domain detection",
        "release_decision": "future_adapter",
        "primary_blocker": "Spatial-domain objective does not directly emit masked-expression or LR/pathway route rows.",
        "future_adapter_note": "Adapter can be added as a graph-feature baseline in a future tier.",
    },
]

GATE_DEFINITIONS = [
    (
        "residual_utility",
        "Residual utility",
        "Delta_i > 0",
        "residual_gate_passed",
    ),
    (
        "fdr_effect",
        "Effect-control evidence",
        "a_i_eff = 1",
        "fdr_effect_gate_passed",
    ),
    (
        "wrong_context_separation",
        "Wrong-context separation",
        "Delta_i - Delta_i_wrong > 0",
        "wrong_context_gate_passed",
    ),
    (
        "heldout_replication",
        "Held-out replication",
        "h_i = 1",
        "heldout_replication_passed",
    ),
    (
        "leakage_audit",
        "Leakage audit",
        "ell_i = 1",
        "leakage_audit_passed",
    ),
    (
        "no_unresolved_downgrade",
        "No unresolved downgrade",
        "d_i = 0",
        "no_unresolved_downgrade_passed",
    ),
]

OPERATING_POINT_DEFINITIONS = [
    {
        "id": "registered_conservative",
        "label": "Registered conservative",
        "fdr_threshold": 0.05,
        "residual_threshold": 0.0,
        "wrong_context_rule": "Delta_i - Delta_i_wrong > 0",
        "route_recovery_threshold": 0.95,
        "fcr_ceiling": 0.05,
        "sensitivity_floor": 0.65,
        "specificity_floor": 0.80,
        "replication_floor": 0.60,
        "no_harm_floor": 0.95,
        "scope": "registered publication claim",
    },
    {
        "id": "moderate_reviewer_stress",
        "label": "Moderate reviewer stress",
        "fdr_threshold": 0.10,
        "residual_threshold": 0.0,
        "wrong_context_rule": "Delta_i - Delta_i_wrong > 0",
        "route_recovery_threshold": 0.85,
        "fcr_ceiling": 0.10,
        "sensitivity_floor": 0.60,
        "specificity_floor": 0.75,
        "replication_floor": 0.50,
        "no_harm_floor": 0.90,
        "scope": "reviewer sensitivity analysis",
    },
    {
        "id": "permissive_exploratory",
        "label": "Permissive exploratory",
        "fdr_threshold": 0.20,
        "residual_threshold": 0.0,
        "wrong_context_rule": "Delta_i - Delta_i_wrong > 0",
        "route_recovery_threshold": 0.70,
        "fcr_ceiling": 0.20,
        "sensitivity_floor": 0.50,
        "specificity_floor": 0.60,
        "replication_floor": 0.50,
        "no_harm_floor": 0.80,
        "scope": "exploratory, not a registered claim",
    },
]

DOWNGRADE_REASON_CODES = {
    "access_or_schema_blocker",
    "artifact_or_confound_abstention",
    "insufficient_power_or_uncertainty",
    "panel_or_target_coverage_gap",
    "synthetic_confound_abstention",
    "synthetic_missing_panel_abstention",
    "uncertain_default_abstention",
    "unreplicated_context_signal",
}

REASON_GATE_MAP = {
    "access_or_schema_blocker": [
        "residual_utility",
        "wrong_context_separation",
        "fdr_effect",
        "heldout_replication",
        "no_unresolved_downgrade",
    ],
    "artifact_or_confound_abstention": [
        "wrong_context_separation",
        "heldout_replication",
        "no_unresolved_downgrade",
    ],
    "insufficient_power_or_uncertainty": [
        "fdr_effect",
        "heldout_replication",
        "no_unresolved_downgrade",
    ],
    "panel_or_target_coverage_gap": [
        "residual_utility",
        "fdr_effect",
        "no_unresolved_downgrade",
    ],
    "synthetic_confound_abstention": [
        "wrong_context_separation",
        "no_unresolved_downgrade",
    ],
    "synthetic_missing_panel_abstention": [
        "residual_utility",
        "no_unresolved_downgrade",
    ],
    "synthetic_null_rejected": ["residual_utility"],
    "uncertain_default_abstention": [
        "fdr_effect",
        "heldout_replication",
        "no_unresolved_downgrade",
    ],
    "unreplicated_context_signal": [
        "heldout_replication",
        "no_unresolved_downgrade",
    ],
}

FAILURE_CLASS_GATE_MAP = {
    "access_or_schema_blocker": [
        "residual_utility",
        "wrong_context_separation",
        "fdr_effect",
        "heldout_replication",
        "no_unresolved_downgrade",
    ],
    "expression_absorbs_signal": [
        "residual_utility",
        "no_unresolved_downgrade",
    ],
    "fov_or_sample_artifact": [
        "wrong_context_separation",
        "heldout_replication",
        "no_unresolved_downgrade",
    ],
    "insufficient_power": [
        "fdr_effect",
        "heldout_replication",
        "no_unresolved_downgrade",
    ],
    "labels_not_replicated": [
        "heldout_replication",
        "no_unresolved_downgrade",
    ],
    "lr_without_downstream_response": [
        "residual_utility",
        "no_unresolved_downgrade",
    ],
    "panel_lacks_downstream_genes": [
        "residual_utility",
        "fdr_effect",
        "no_unresolved_downgrade",
    ],
}


def _read_csv(relative_path: str) -> pd.DataFrame:
    path = REPORT_ROOT / relative_path
    if not path.exists():
        raise FileNotFoundError(path)
    return pd.read_csv(path)


def _read_json(relative_path: str) -> dict:
    path = REPORT_ROOT / relative_path
    if not path.exists():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8"))


def _read_manifest(name: str) -> dict:
    path = MANIFEST_ROOT / name
    if not path.exists():
        raise FileNotFoundError(path)
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _friendly(value: object) -> str:
    if pd.isna(value):
        return ""
    text = str(value).replace("_", " ")
    text = text.replace("q1", "full benchmark")
    text = text.replace("Q1", "full benchmark")
    return text


def _dataset_label(value: object) -> str:
    return DATASET_LABELS.get(str(value), _friendly(value))


def _method_label(value: object) -> str:
    return METHOD_LABELS.get(str(value), _friendly(value))


def _route_label(value: object) -> str:
    return ROUTE_LABELS.get(str(value), _friendly(value))


def _tier_label(value: object) -> str:
    return TIER_LABELS.get(str(value), _friendly(value).title())


def _panel_depth_group(value: object) -> str:
    if pd.isna(value):
        return "No registered panel"
    genes = int(value)
    if genes <= 0:
        return "No registered panel"
    if genes < 1100:
        return "<1,100 genes"
    if genes >= 5000:
        return ">=5,000 genes"
    return "1,100-4,999 genes"


def _axis_label(value: object) -> str:
    return AXIS_LABELS.get(str(value), _friendly(value).title())


def _round_numeric(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    for column in out.columns:
        if pd.api.types.is_float_dtype(out[column]):
            out[column] = out[column].map(lambda value: round(float(value), 4))
    return out


def _compact_unique(values: pd.Series, *, limit: int = 3) -> str:
    items = sorted({str(value) for value in values.dropna() if str(value) != ""})
    if not items:
        return ""
    if len(items) <= limit:
        return ", ".join(items)
    return ", ".join(items[:limit]) + f", +{len(items) - limit} more"


def _metric_mean(
    df: pd.DataFrame,
    metric_family: str,
    *,
    value_column: str = "metric_value",
) -> float | None:
    values = pd.to_numeric(
        df.loc[df["metric_family"] == metric_family, value_column],
        errors="coerce",
    ).dropna()
    if values.empty:
        return None
    return float(values.mean())


def _metric_quantile(
    df: pd.DataFrame,
    metric_family: str,
    quantile: float,
) -> float | None:
    values = pd.to_numeric(
        df.loc[df["metric_family"] == metric_family, "metric_value"],
        errors="coerce",
    ).dropna()
    if values.empty:
        return None
    return float(values.quantile(quantile))


def _as_bool(series: pd.Series) -> pd.Series:
    return series.map(lambda value: str(value).strip().lower() == "true")


def _wilson_interval(successes: int, total: int) -> tuple[float | None, float | None]:
    if total <= 0:
        return None, None
    z = 1.96
    p_hat = successes / total
    denominator = 1.0 + (z * z / total)
    center = (p_hat + (z * z / (2 * total))) / denominator
    half_width = (
        z
        * ((p_hat * (1.0 - p_hat) / total) + (z * z / (4 * total * total))) ** 0.5
        / denominator
    )
    return max(0.0, center - half_width), min(1.0, center + half_width)


def _mean_interval(values: pd.Series) -> tuple[float | None, float | None]:
    numeric = pd.to_numeric(values, errors="coerce").dropna()
    if numeric.empty:
        return None, None
    if len(numeric) == 1:
        value = float(numeric.iloc[0])
        return value, value
    mean = float(numeric.mean())
    half_width = 1.96 * float(numeric.std(ddof=1)) / (len(numeric) ** 0.5)
    return max(0.0, mean - half_width), min(1.0, mean + half_width)


def _markdown_table(df: pd.DataFrame) -> str:
    rendered = _round_numeric(df).astype(str)
    headers = list(rendered.columns)
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    for _, row in rendered.iterrows():
        cells = [str(row[column]).replace("|", "\\|") for column in headers]
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines) + "\n"


def _write_table(
    df: pd.DataFrame,
    *,
    stem: str,
    title: str,
    output_dir: Path,
) -> dict[str, str]:
    output_dir.mkdir(parents=True, exist_ok=True)
    csv_path = output_dir / f"{stem}.csv"
    md_path = output_dir / f"{stem}.md"
    tex_path = output_dir / f"{stem}.tex"
    out = _round_numeric(df)
    out.to_csv(csv_path, index=False)
    md_path.write_text(f"# {title}\n\n{_markdown_table(out)}", encoding="utf-8")
    latex = out.to_latex(index=False, escape=True)
    tex_path.write_text(
        "% Auto-generated by scripts/build_contextgate_manuscript_tables.py\n"
        f"% {title}\n"
        f"{latex}",
        encoding="utf-8",
    )
    return {
        "csv": str(csv_path),
        "md": str(md_path),
        "tex": str(tex_path),
        "rows": str(len(out)),
    }


def build_dataset_eligibility() -> pd.DataFrame:
    manifest = _read_manifest("contextgate_benchmark_manifest.yaml")
    cards = pd.DataFrame(manifest["dataset_cards"])
    job_status = _read_csv("cp_q6_benchmark_matrix/job_status.csv")

    status_counts = (
        job_status.pivot_table(
            index="dataset_id",
            columns="status",
            values="job_id",
            aggfunc="count",
            fill_value=0,
        )
        .reset_index()
        .rename_axis(None, axis=1)
    )
    for column in ["completed", "skipped", "failed"]:
        if column not in status_counts:
            status_counts[column] = 0

    out = cards.merge(status_counts, on="dataset_id", how="left")
    for column in ["completed", "skipped", "failed"]:
        out[column] = out[column].fillna(0).astype(int)

    role_order = {
        "usable": 0,
        "validation_frozen": 1,
        "rejected_or_access_blocked": 2,
    }
    out["sort_key"] = out["benchmark_role"].map(role_order).fillna(99)
    out = out.sort_values(["sort_key", "dataset_id"])
    return (
        out[
            [
                "dataset_id",
                "benchmark_role",
                "platform",
                "cancer_or_tissue_context",
                "unit_type",
                "sample_count",
                "donor_count",
                "cell_or_unit_count",
                "gene_count",
                "coordinate_status",
                "label_status",
                "source_access_status",
                "skip_reason",
                "claim_scope",
                "completed",
                "skipped",
                "failed",
            ]
        ]
        .rename(
            columns={
                "dataset_id": "Dataset",
                "benchmark_role": "Role",
                "platform": "Platform",
                "cancer_or_tissue_context": "Cancer/tissue context",
                "unit_type": "Unit",
                "sample_count": "Samples",
                "donor_count": "Donors",
                "cell_or_unit_count": "Units",
                "gene_count": "Genes",
                "coordinate_status": "Coordinates",
                "label_status": "Labels",
                "source_access_status": "Access",
                "skip_reason": "Skip reason",
                "claim_scope": "Claim scope",
                "completed": "Completed jobs",
                "skipped": "Skipped jobs",
                "failed": "Failed jobs",
            }
        )
        .assign(
            Dataset=lambda frame: frame["Dataset"].map(_dataset_label),
            Role=lambda frame: frame["Role"].map(
                lambda value: ROLE_LABELS.get(str(value), _friendly(value).title())
            ),
            Unit=lambda frame: frame["Unit"].map(_friendly),
            Access=lambda frame: frame["Access"].map(_friendly),
            Coordinates=lambda frame: frame["Coordinates"].map(_friendly),
            Labels=lambda frame: frame["Labels"].map(_friendly),
            **{
                "Cancer/tissue context": lambda frame: frame[
                    "Cancer/tissue context"
                ].map(_friendly),
                "Skip reason": lambda frame: frame["Skip reason"].map(_friendly),
                "Claim scope": lambda frame: frame["Claim scope"].map(_friendly),
            },
        )
    )


def build_benchmark_matrix() -> pd.DataFrame:
    job_manifest = _read_csv("cp_q6_benchmark_matrix/job_manifest.csv")
    job_status = _read_csv("cp_q6_benchmark_matrix/job_status.csv")
    metric_matrix = _read_csv("cp_q6_benchmark_matrix/benchmark_metric_matrix.csv")

    status_counts = (
        job_status.pivot_table(
            index="benchmark_tier",
            columns="status",
            values="job_id",
            aggfunc="count",
            fill_value=0,
        )
        .reset_index()
        .rename_axis(None, axis=1)
    )
    for column in ["completed", "skipped", "failed"]:
        if column not in status_counts:
            status_counts[column] = 0

    planned = (
        job_manifest.groupby("benchmark_tier")
        .agg(
            planned_jobs=("job_id", "count"),
            datasets=("dataset_id", "nunique"),
            tasks=("task_family", "nunique"),
            methods=("method_family", "nunique"),
            controls=("control_family", "nunique"),
            splits=("split_id", "nunique"),
            seeds=("seed", "nunique"),
        )
        .reset_index()
    )
    metrics = (
        metric_matrix.groupby("benchmark_tier")
        .agg(
            metric_rows=("metric_name", "count"),
            metric_families=("metric_family", "nunique"),
        )
        .reset_index()
    )

    out = planned.merge(status_counts, on="benchmark_tier", how="left")
    out = out.merge(metrics, on="benchmark_tier", how="left")
    for column in ["completed", "skipped", "failed", "metric_rows"]:
        out[column] = out[column].fillna(0).astype(int)
    out["evidence_complete"] = out["completed"] > 0
    out["sort_key"] = out["benchmark_tier"].map({"mini": 0, "core": 1, "q1": 2})
    out = out.sort_values("sort_key")
    return (
        out[
            [
                "benchmark_tier",
                "planned_jobs",
                "completed",
                "skipped",
                "failed",
                "datasets",
                "tasks",
                "methods",
                "controls",
                "splits",
                "seeds",
                "metric_families",
                "metric_rows",
                "evidence_complete",
            ]
        ]
        .rename(
            columns={
                "benchmark_tier": "Benchmark tier",
                "planned_jobs": "Planned jobs",
                "completed": "Completed jobs",
                "skipped": "Skipped jobs",
                "failed": "Failed jobs",
                "datasets": "Datasets",
                "tasks": "Task families",
                "methods": "Method families",
                "controls": "Control families",
                "splits": "Split families",
                "seeds": "Seeds",
                "metric_families": "Metric families",
                "metric_rows": "Metric rows",
                "evidence_complete": "Completed evidence",
            }
        )
        .assign(
            **{"Benchmark tier": lambda frame: frame["Benchmark tier"].map(_tier_label)}
        )
    )


def build_claim_audit() -> pd.DataFrame:
    q5_summary = _read_json(
        "cp_q5_contextgate_decisions/contextgate_decision_summary.json"
    )
    q6_summary = _read_json("cp_q6_benchmark_matrix/benchmark_matrix_summary.json")
    q7_summary = _read_json("cp_q7_robustness_stress/robustness_stress_summary.json")
    claim_survival = _read_csv("cp_q7_robustness_stress/claim_survival_audit.csv")
    q5_no_harm = _read_csv("cp_q5_contextgate_decisions/contextgate_no_harm.csv")
    registered_expression = q5_no_harm[
        q5_no_harm["analysis_id"].eq("registered_vs_expression_only_linear")
    ]
    if registered_expression.empty:
        raise ValueError("Missing expression-only no-harm comparator row.")
    registered_expression = registered_expression.iloc[0]
    contextgate_registered_fcr = float(
        registered_expression["contextgate_false_positive_context_rate"]
    )
    expression_registered_fcr = float(
        registered_expression["comparator_false_positive_context_rate"]
    )
    q3_methods = _read_csv("cp_q3_positive_null_control_ladder/method_summary.csv")
    q3_lookup = q3_methods.set_index("method_id")
    contextgate_positive_sensitivity = float(
        q3_lookup.loc[
            "contextgate_transparent_router",
            "mean_sensitivity_positive",
        ]
    )
    expression_positive_sensitivity = float(
        q3_lookup.loc[
            "expression_only_linear",
            "mean_sensitivity_positive",
        ]
    )
    always_null_fcr = float(
        q3_lookup.loc[
            "always_true_neighbor_mean",
            "false_positive_context_rate_negative",
        ]
    )

    support = {
        "all_failed_stress_tests_have_downgrades": (
            f"{q7_summary['failed_without_downgrade_count']} stress rows failed "
            "without an explicit downgrade."
        ),
        "contextgate_reduces_false_context": (
            "ContextGate registered false-context flag rate "
            f"{contextgate_registered_fcr:.3f}; expression-only comparator "
            f"{expression_registered_fcr:.3f}; "
            "ContextGate positive-control sensitivity "
            f"{contextgate_positive_sensitivity:.3f} versus expression-only "
            f"{expression_positive_sensitivity:.3f}; always-context null "
            f"FCR {always_null_fcr:.3f}."
        ),
        "positive_null_ladder_detects_synthetic_signal": (
            "Positive-control route recovery "
            f"{q5_summary['positive_control_route_recovery_rate']:.3f}; "
            "synthetic false-context rate "
            f"{q5_summary['synthetic_contextgate_false_positive_context_rate']:.3f}."
        ),
        "spatial_context_is_conditional_not_universal": (
            f"{q5_summary['context_allowed_decision_count']} strict biological "
            "context-allowed decisions; "
            f"{q5_summary['expression_only_decision_count']} expression-only, "
            f"{q5_summary['abstention_decision_count']} abstain, "
            f"{q5_summary['positive_control_only_decision_count']} "
            "positive-control-only decisions."
        ),
        "strong_biological_context_claim": (
            "Strong biological context-benefit claim remains downgraded; "
            f"{q7_summary['downgraded_claim_count']} claim was downgraded."
        ),
        "wrong_context_controls_are_necessary": (
            f"{q6_summary['control_family_count']} control families included in "
            "the benchmark matrix."
        ),
    }
    source_files = {
        "all_failed_stress_tests_have_downgrades": (
            "results/reports/cp_q7_robustness_stress/claim_survival_audit.csv"
        ),
        "contextgate_reduces_false_context": (
            "results/reports/cp_q5_contextgate_decisions/contextgate_no_harm.csv"
        ),
        "positive_null_ladder_detects_synthetic_signal": (
            "results/reports/cp_q3_positive_null_control_ladder/"
            "positive_control_ladder.csv"
        ),
        "spatial_context_is_conditional_not_universal": (
            "results/reports/cp_q5_contextgate_decisions/contextgate_decisions.csv"
        ),
        "strong_biological_context_claim": (
            "results/reports/cp_q7_robustness_stress/claim_survival_audit.csv"
        ),
        "wrong_context_controls_are_necessary": (
            "results/reports/cp_q6_benchmark_matrix/job_manifest.csv"
        ),
    }
    out = claim_survival.copy()
    out["Claim"] = out["claim_id"].map(CLAIM_TEXT)
    out["Quantitative support"] = out["claim_id"].map(support)
    out["Source artifact"] = out["claim_id"].map(source_files)
    out["Publication status"] = out["claim_survives"].map(
        {True: "Survives", False: "Downgraded"}
    )
    out["Boundary"] = out["claim_downgrade"].map(
        lambda value: "No downgrade" if value == "none" else _friendly(value)
    )
    return out[
        [
            "claim_id",
            "Claim",
            "Publication status",
            "Boundary",
            "Quantitative support",
            "Source artifact",
            "notes",
        ]
    ].rename(
        columns={
            "claim_id": "Claim ID",
            "notes": "Notes",
        }
    )


def build_scale_contract() -> pd.DataFrame:
    df = _read_csv("cp_q6_benchmark_matrix/scale_contract_compliance.csv")
    out = df[
        [
            "axis",
            "observed_count",
            "target_min",
            "required",
            "passed",
            "claim_downgrade_if_failed",
            "notes",
        ]
    ].rename(
        columns={
            "axis": "Scale axis",
            "observed_count": "Observed",
            "target_min": "Target minimum",
            "required": "Required",
            "passed": "Passed",
            "claim_downgrade_if_failed": "Downgrade if failed",
            "notes": "Notes",
        }
    )
    out["Scale axis"] = out["Scale axis"].map(_axis_label)
    out["Downgrade if failed"] = out["Downgrade if failed"].map(_friendly)
    out["Notes"] = out["Notes"].map(_friendly)
    return out


def build_method_metrics() -> pd.DataFrame:
    df = _read_csv("cp_q2_method_comparison/method_metrics.csv")
    out = df[
        [
            "method_id",
            "method_family",
            "row_count",
            "mean_utility",
            "mean_regret",
            "no_harm_rate",
            "false_positive_context_rate",
            "abstention_rate",
            "context_use_rate",
        ]
    ].sort_values(["mean_regret", "false_positive_context_rate"])
    return out.rename(
        columns={
            "method_id": "Method",
            "method_family": "Method family",
            "row_count": "Rows",
            "mean_utility": "Mean utility",
            "mean_regret": "Mean regret",
            "no_harm_rate": "No-harm rate",
            "false_positive_context_rate": "False-context rate",
            "abstention_rate": "Abstention rate",
            "context_use_rate": "Context-use rate",
        }
    ).assign(
        Method=lambda frame: frame["Method"].map(_method_label),
        **{"Method family": lambda frame: frame["Method family"].map(_friendly)},
    )


def build_positive_null_summary() -> pd.DataFrame:
    df = _read_csv("cp_q3_positive_null_control_ladder/method_summary.csv")
    out = df[
        [
            "method_id",
            "row_count",
            "positive_row_count",
            "negative_row_count",
            "mean_sensitivity_positive",
            "mean_specificity_negative",
            "false_positive_context_rate_negative",
            "abstention_rate",
            "gate_pass_rate",
        ]
    ].sort_values(
        ["gate_pass_rate", "false_positive_context_rate_negative"],
        ascending=[False, True],
    )
    return out.rename(
        columns={
            "method_id": "Method",
            "row_count": "Rows",
            "positive_row_count": "Positive-control rows",
            "negative_row_count": "Null/control rows",
            "mean_sensitivity_positive": "Positive sensitivity",
            "mean_specificity_negative": "Null specificity",
            "false_positive_context_rate_negative": "Null false-context rate",
            "abstention_rate": "Abstention rate",
            "gate_pass_rate": "Gate pass rate",
        }
    ).assign(Method=lambda frame: frame["Method"].map(_method_label))


def build_failure_summary() -> pd.DataFrame:
    df = _read_csv("cp_q4_failure_taxonomy/failure_class_summary.csv")
    out = df.rename(
        columns={
            "failure_class": "Failure class",
            "failure_count": "Rows",
            "dataset_count": "Datasets",
            "task_count": "Tasks",
            "method_count": "Methods",
            "claim_downgrade": "Claim downgrade",
        }
    )
    out["Failure class"] = out["Failure class"].map(_friendly)
    out["Claim downgrade"] = out["Claim downgrade"].map(_friendly)
    return out


def build_contextgate_route_summary() -> pd.DataFrame:
    df = _read_csv("cp_q5_contextgate_decisions/contextgate_route_summary.csv")
    return df.rename(
        columns={
            "route_label": "Route",
            "decision_count": "Decisions",
            "dataset_count": "Datasets",
            "task_count": "Tasks",
            "mean_confidence": "Mean confidence",
            "claim_level": "Claim level",
        }
    ).assign(
        Route=lambda frame: frame["Route"].map(_route_label),
        **{"Claim level": lambda frame: frame["Claim level"].map(_friendly)},
    )


def build_contextgate_no_harm() -> pd.DataFrame:
    df = _read_csv("cp_q5_contextgate_decisions/contextgate_no_harm.csv")
    out = df.rename(
        columns={
            "analysis_id": "Analysis",
            "analysis_domain": "Domain",
            "comparator_method_id": "Comparator",
            "contextgate_false_positive_context_rate": (
                "ContextGate false-context rate"
            ),
            "comparator_false_positive_context_rate": ("Comparator false-context rate"),
            "false_positive_context_reduction": "False-context reduction",
            "contextgate_no_harm_rate": "ContextGate no-harm rate",
            "comparator_no_harm_rate": "Comparator no-harm rate",
            "contextgate_abstention_rate": "ContextGate abstention rate",
            "positive_control_route_recovery_rate": ("Positive-control route recovery"),
            "gate_passed": "Gate passed",
        }
    )
    out["Analysis"] = out["Analysis"].map(_friendly)
    out["Domain"] = out["Domain"].map(_friendly)
    out["Comparator"] = out["Comparator"].map(_method_label)
    return out


def build_stress_summary() -> pd.DataFrame:
    rows = []
    for family, relative_path in CP_Q7_STRESS_FILES.items():
        df = _read_csv(relative_path)
        rows.append(
            {
                "Stress family": _friendly(family),
                "Accounting role": "Row-generating stress family",
                "Included in 127 stress-row denominator": "Yes",
                "Rows": len(df),
                "Passed rows": int(df["passed"].sum()),
                "Downgraded rows": int((df["claim_downgrade"] != "none").sum()),
                "Failed without downgrade": int(
                    ((~df["passed"]) & (df["claim_downgrade"] == "none")).sum()
                ),
                "Source artifact": f"results/reports/{relative_path}",
            }
        )

    claim_survival = _read_csv("cp_q7_robustness_stress/claim_survival_audit.csv")
    rows.append(
        {
            "Stress family": "Claim survival audit",
            "Accounting role": "Separate claim-survival audit",
            "Included in 127 stress-row denominator": "No",
            "Rows": len(claim_survival),
            "Passed rows": int(claim_survival["claim_survives"].sum()),
            "Downgraded rows": int((claim_survival["claim_downgrade"] != "none").sum()),
            "Failed without downgrade": 0,
            "Source artifact": (
                "results/reports/cp_q7_robustness_stress/claim_survival_audit.csv"
            ),
        }
    )
    return pd.DataFrame(rows)


def build_table_only_evidence() -> pd.DataFrame:
    path = (
        PROJECT_ROOT
        / "manuscript"
        / "figures"
        / "singles"
        / "table_or_text_only_evidence.json"
    )
    data = json.loads(path.read_text(encoding="utf-8"))
    rows = [
        {
            "Evidence item": _friendly(key),
            "Source": value["source"],
            "Reason for table/text": value["reason"],
        }
        for key, value in sorted(data.items())
    ]
    return pd.DataFrame(rows)


def build_figure_inventory() -> pd.DataFrame:
    path = (
        PROJECT_ROOT
        / "manuscript"
        / "figures"
        / "singles"
        / "publication_figure_manifest.json"
    )
    data = json.loads(path.read_text(encoding="utf-8"))
    rows = []
    for stem, outputs in sorted(data.items()):
        rows.append(
            {
                "Figure stem": _friendly(stem),
                "PDF": Path(outputs["pdf"]).name,
                "EPS": Path(outputs["eps"]).name,
                "PNG preview": Path(outputs["png"]).name,
            }
        )
    return pd.DataFrame(rows)


def build_cp_q2_dataset_task_utility() -> pd.DataFrame:
    df = _read_csv("cp_q2_method_comparison/method_predictions.csv")
    rows = []
    for (dataset_id, task_id, method_id), group in df.groupby(
        ["dataset_id", "task_id", "method_id"],
        dropna=False,
    ):
        rows.append(
            {
                "Dataset": _dataset_label(dataset_id),
                "Task": _friendly(task_id),
                "Method": _method_label(method_id),
                "Rows": len(group),
                "True routes": _compact_unique(
                    group["true_route"].map(
                        lambda value: ROUTE_LABELS.get(str(value), _friendly(value))
                    )
                ),
                "Evidence classes": _compact_unique(
                    group["evidence_class"].map(_friendly)
                ),
                "Mean utility": pd.to_numeric(group["utility"], errors="coerce").mean(),
                "Mean oracle utility": pd.to_numeric(
                    group["oracle_utility"], errors="coerce"
                ).mean(),
                "Mean regret": pd.to_numeric(group["regret"], errors="coerce").mean(),
                "Context-use rate": pd.to_numeric(
                    group["uses_context"], errors="coerce"
                ).mean(),
                "False-context rate": pd.to_numeric(
                    group["false_positive_context_use"], errors="coerce"
                ).mean(),
                "No-harm rate": pd.to_numeric(
                    group["no_harm_success"], errors="coerce"
                ).mean(),
                "Abstention rate": pd.to_numeric(
                    group["abstained"], errors="coerce"
                ).mean(),
            }
        )
    return pd.DataFrame(rows).sort_values(
        ["Task", "Dataset", "Mean regret", "False-context rate", "Method"]
    )


def build_q6_dataset_task_method_metrics() -> pd.DataFrame:
    df = _read_csv("cp_q6_benchmark_matrix/benchmark_metric_matrix.csv")
    full = df[df["benchmark_tier"] == "q1"].copy()
    rows = []
    for (dataset_id, task_id, method_id), group in full.groupby(
        ["dataset_id", "task_id", "method_id"],
        dropna=False,
    ):
        jobs = group[
            ["control_id", "split_id", "seed", "artifact_registry_ids"]
        ].drop_duplicates()
        rows.append(
            {
                "Dataset": _dataset_label(dataset_id),
                "Task": _friendly(task_id),
                "Method": _method_label(method_id),
                "Completed job rows": len(jobs),
                "Mean prediction error": _metric_mean(group, "prediction_error"),
                "Mean macro-F1/proxy": _metric_mean(
                    group, "classification_accuracy_or_macro_f1"
                ),
                "Mean residual delta": _metric_mean(group, "residual_delta"),
                "Mean regret": _metric_mean(group, "regret_against_oracle"),
                "Mean FCR": _metric_mean(group, "false_positive_context_rate"),
                "Mean no-harm": _metric_mean(group, "no_harm_rate"),
                "Mean abstention": _metric_mean(group, "abstention_rate"),
                "Mean q-value proxy": _metric_mean(group, "fdr_adjusted_p_value"),
                "Mean runtime sec": _metric_mean(group, "compute_runtime"),
                "Mean delta vs expression": _metric_mean(
                    group,
                    "residual_delta",
                    value_column="paired_delta_vs_expression",
                ),
                "Mean delta vs always-context": _metric_mean(
                    group,
                    "residual_delta",
                    value_column="paired_delta_vs_always_context",
                ),
            }
        )
    return pd.DataFrame(rows).sort_values(
        ["Task", "Dataset", "Mean regret", "Mean FCR", "Method"]
    )


def build_q6_method_task_safety() -> pd.DataFrame:
    df = _read_csv("cp_q6_benchmark_matrix/benchmark_metric_matrix.csv")
    full = df[df["benchmark_tier"] == "q1"].copy()
    rows = []
    for (task_id, method_id), group in full.groupby(
        ["task_id", "method_id"],
        dropna=False,
    ):
        rows.append(
            {
                "Task": _friendly(task_id),
                "Method": _method_label(method_id),
                "Datasets": group["dataset_id"].nunique(),
                "Metric rows": len(group),
                "Mean regret": _metric_mean(group, "regret_against_oracle"),
                "Regret IQR low": _metric_quantile(
                    group,
                    "regret_against_oracle",
                    0.25,
                ),
                "Regret IQR high": _metric_quantile(
                    group,
                    "regret_against_oracle",
                    0.75,
                ),
                "Mean FCR": _metric_mean(group, "false_positive_context_rate"),
                "Mean no-harm": _metric_mean(group, "no_harm_rate"),
                "Mean abstention": _metric_mean(group, "abstention_rate"),
                "Mean sensitivity/proxy": _metric_mean(
                    group,
                    "classification_accuracy_or_macro_f1",
                ),
                "Mean specificity/proxy": 1.0
                - (_metric_mean(group, "false_positive_context_rate") or 0.0),
                "Mean replication": _metric_mean(group, "replication_rate"),
            }
        )
    return pd.DataFrame(rows).sort_values(["Task", "Mean regret", "Mean FCR", "Method"])


def build_contextgate_routes_by_dataset_task() -> pd.DataFrame:
    df = _read_csv("cp_q5_contextgate_decisions/contextgate_decisions.csv")
    route_counts = (
        df.pivot_table(
            index=["dataset_id", "task_id"],
            columns="route_label",
            values="contextgate_decision_id",
            aggfunc="count",
            fill_value=0,
        )
        .reset_index()
        .rename_axis(None, axis=1)
    )
    for route in ROUTE_LABELS:
        if route not in route_counts:
            route_counts[route] = 0
    summary = (
        df.groupby(["dataset_id", "task_id"], dropna=False)
        .agg(
            decisions=("contextgate_decision_id", "count"),
            mean_confidence=("confidence", "mean"),
            real_context_rows=("uses_real_context", "sum"),
            synthetic_context_rows=("uses_synthetic_context", "sum"),
            failure_classes=("failure_class", _compact_unique),
            reason_codes=("reason_code", _compact_unique),
        )
        .reset_index()
    )
    out = route_counts.merge(summary, on=["dataset_id", "task_id"], how="left")
    out = out.rename(
        columns={
            "dataset_id": "Dataset",
            "task_id": "Task",
            "expression_only": "Expression-only decisions",
            "context_allowed": "Context-allowed decisions",
            "abstain_uncertain": "Abstention decisions",
            "positive_control_only": "Positive-control-only decisions",
            "decisions": "Total decisions",
            "mean_confidence": "Mean confidence",
            "real_context_rows": "Real context rows",
            "synthetic_context_rows": "Synthetic context rows",
            "failure_classes": "Failure classes",
            "reason_codes": "Reason codes",
        }
    )
    out["Dataset"] = out["Dataset"].map(_dataset_label)
    out["Task"] = out["Task"].map(_friendly)
    out["Failure classes"] = out["Failure classes"].map(_friendly)
    out["Reason codes"] = out["Reason codes"].map(_friendly)
    return out[
        [
            "Dataset",
            "Task",
            "Total decisions",
            "Expression-only decisions",
            "Context-allowed decisions",
            "Abstention decisions",
            "Positive-control-only decisions",
            "Real context rows",
            "Synthetic context rows",
            "Mean confidence",
            "Failure classes",
            "Reason codes",
        ]
    ].sort_values(["Task", "Dataset"])


def build_q6_skip_infeasibility() -> pd.DataFrame:
    df = _read_csv("cp_q6_benchmark_matrix/skip_reason_table.csv")
    grouped = (
        df.groupby(
            ["benchmark_tier", "dataset_id", "task_id", "skip_reason"],
            dropna=False,
        )
        .agg(
            skipped_jobs=("row_count", "sum"),
            method_count=("method_id", "nunique"),
            control_count=("control_id", "nunique"),
            row_types=("row_type", _compact_unique),
        )
        .reset_index()
    )
    out = grouped.rename(
        columns={
            "benchmark_tier": "Benchmark tier",
            "dataset_id": "Dataset",
            "task_id": "Task",
            "skip_reason": "Skip reason",
            "skipped_jobs": "Skipped jobs",
            "method_count": "Methods affected",
            "control_count": "Controls affected",
            "row_types": "Row types",
        }
    )
    out["Benchmark tier"] = out["Benchmark tier"].map(_tier_label)
    out["Dataset"] = out["Dataset"].map(_dataset_label)
    out["Task"] = out["Task"].map(_friendly)
    out["Skip reason"] = out["Skip reason"].map(_friendly)
    out["Row types"] = out["Row types"].map(_friendly)
    return out.sort_values(
        ["Benchmark tier", "Skipped jobs", "Dataset", "Task"],
        ascending=[True, False, True, True],
    )


def build_claim_downgrade_distribution() -> pd.DataFrame:
    df = _read_csv("cp_q4_failure_taxonomy/claim_downgrade_audit.csv")
    out = df.rename(
        columns={
            "claim_downgrade": "Claim downgrade",
            "failure_class": "Failure class",
            "failure_count": "Rows",
            "dataset_count": "Datasets",
            "allowed_claim": "Allowed claim",
            "blocked_claim": "Blocked claim",
            "required_next_step": "Required next step",
        }
    )
    out["Claim downgrade"] = out["Claim downgrade"].map(_friendly)
    out["Failure class"] = out["Failure class"].map(_friendly)
    return out.sort_values(["Rows", "Failure class"], ascending=[False, True])


def build_positive_null_signal_strength() -> pd.DataFrame:
    recovery = _read_csv("cp_q3_positive_null_control_ladder/recovery_curve.csv")
    false_positive = _read_csv(
        "cp_q3_positive_null_control_ladder/false_positive_curve.csv"
    )
    cases = _read_csv("cp_q3_positive_null_control_ladder/ladder_cases.csv")
    case_params = {}
    for (dataset_id, control_level), group in cases.groupby(
        ["dataset_id", "control_level"],
        dropna=False,
    ):
        case_params[(dataset_id, control_level)] = {
            "Effective signal strength": pd.to_numeric(
                group["effective_signal_strength"],
                errors="coerce",
            ).mean(),
            "Noise fraction": pd.to_numeric(
                group["noise_fraction"],
                errors="coerce",
            ).mean(),
            "Prevalence": pd.to_numeric(
                group["prevalence"],
                errors="coerce",
            ).mean(),
            "Localization scope": _compact_unique(group["localization_scope"]),
            "Expected route": _compact_unique(group["expected_route"]),
            "Expected context-positive": bool(
                _as_bool(group["expected_context_positive"]).any()
            ),
            "Ladder description": _compact_unique(group["description"], limit=2),
        }

    def _params(row: pd.Series) -> dict:
        return case_params.get((row["dataset_id"], row["control_level"]), {})

    rows = []
    for _, row in recovery.iterrows():
        params = _params(row)
        rows.append(
            {
                "Curve": "positive_recovery",
                "Dataset": row["dataset_id"],
                "Control level": row["control_level"],
                "Method": row["method_id"],
                "Method family": row["method_family"],
                "Signal strength": row["injected_signal_strength"],
                "Effective signal strength": params.get("Effective signal strength"),
                "Noise fraction": params.get("Noise fraction"),
                "Prevalence": params.get("Prevalence"),
                "Localization scope": params.get("Localization scope"),
                "Expected route": params.get("Expected route"),
                "Expected context-positive": params.get("Expected context-positive"),
                "Sensitivity": row["sensitivity"],
                "Recovery rate": row["recovery_rate"],
                "Specificity": None,
                "False-context rate": None,
                "Abstention rate": row["abstention_rate"],
                "Rows": row["row_count"],
                "Ladder description": params.get("Ladder description"),
            }
        )
    for _, row in false_positive.iterrows():
        params = _params(row)
        rows.append(
            {
                "Curve": "null_or_confounded_specificity",
                "Dataset": row["dataset_id"],
                "Control level": row["control_level"],
                "Method": row["method_id"],
                "Method family": row["method_family"],
                "Signal strength": row["injected_signal_strength"],
                "Effective signal strength": params.get("Effective signal strength"),
                "Noise fraction": params.get("Noise fraction"),
                "Prevalence": params.get("Prevalence"),
                "Localization scope": params.get("Localization scope"),
                "Expected route": params.get("Expected route"),
                "Expected context-positive": params.get("Expected context-positive"),
                "Sensitivity": None,
                "Recovery rate": None,
                "Specificity": row["specificity"],
                "False-context rate": row["false_positive_context_rate"],
                "Abstention rate": row["abstention_rate"],
                "Rows": row["row_count"],
                "Ladder description": params.get("Ladder description"),
            }
        )
    out = pd.DataFrame(rows)
    out["Curve"] = out["Curve"].map(_friendly)
    out["Dataset"] = out["Dataset"].map(_dataset_label)
    out["Control level"] = out["Control level"].map(_friendly)
    out["Method"] = out["Method"].map(_method_label)
    out["Method family"] = out["Method family"].map(_friendly)
    return out.sort_values(["Curve", "Control level", "Signal strength", "Method"])


def build_q6_regret_distribution() -> pd.DataFrame:
    df = _read_csv("cp_q6_benchmark_matrix/benchmark_metric_matrix.csv")
    regret = df[df["metric_family"] == "regret_against_oracle"].copy()
    rows = []
    for (benchmark_tier, method_id), group in regret.groupby(
        ["benchmark_tier", "method_id"],
        dropna=False,
    ):
        values = pd.to_numeric(group["metric_value"], errors="coerce").dropna()
        rows.append(
            {
                "Benchmark tier": _tier_label(benchmark_tier),
                "Method": _method_label(method_id),
                "Rows": len(values),
                "Datasets": group["dataset_id"].nunique(),
                "Tasks": group["task_id"].nunique(),
                "Mean regret": values.mean(),
                "Median regret": values.median(),
                "Regret p25": values.quantile(0.25),
                "Regret p75": values.quantile(0.75),
                "Max regret": values.max(),
            }
        )
    return pd.DataFrame(rows).sort_values(
        ["Benchmark tier", "Mean regret", "Max regret", "Method"]
    )


def build_threshold_calibration_summary() -> pd.DataFrame:
    df = _read_csv("cp_q7_robustness_stress/threshold_sensitivity.csv")
    df["passed_bool"] = _as_bool(df["passed"])
    rows = []
    interpretations = {
        "effect_size_threshold": (
            "Effect-size screens pass alone, but strict context claims still "
            "require FDR, replication, and wrong-context controls."
        ),
        "false_positive_threshold": (
            "ContextGate remains below the tested false-context thresholds."
        ),
        "fdr_threshold": (
            "FDR is the limiting gate for the strong biological context claim."
        ),
        "min_row_count": (
            "The full benchmark tier has enough rows after explicit skips."
        ),
        "no_harm_threshold": "ContextGate satisfies the tested no-harm thresholds.",
        "replication_threshold": (
            "Replication is borderline: it passes a lenient threshold and fails "
            "stricter thresholds."
        ),
    }
    for axis, group in df.groupby("stress_axis", dropna=False):
        downgrades = group.loc[
            group["claim_downgrade"] != "none",
            "claim_downgrade",
        ]
        rows.append(
            {
                "Threshold axis": _friendly(axis),
                "Levels tested": _compact_unique(group["stress_level"], limit=6),
                "Observed value": pd.to_numeric(
                    group["observed_value"],
                    errors="coerce",
                ).mean(),
                "Threshold values": _compact_unique(
                    group["threshold_value"],
                    limit=6,
                ),
                "Passed levels": int(group["passed_bool"].sum()),
                "Failed levels": int((~group["passed_bool"]).sum()),
                "Downgrades triggered": _compact_unique(downgrades.map(_friendly)),
                "Claim IDs": _compact_unique(group["claim_id"].map(_friendly)),
                "Interpretation": interpretations.get(
                    str(axis),
                    "Threshold sensitivity row retained for reviewer audit.",
                ),
                "Source artifact": (
                    "results/reports/cp_q7_robustness_stress/threshold_sensitivity.csv"
                ),
            }
        )
    return pd.DataFrame(rows).sort_values(["Threshold axis"])


def build_detectability_min_effect() -> pd.DataFrame:
    df = _read_csv("cp_q3_positive_null_control_ladder/positive_control_ladder.csv")
    df["gate_passed_bool"] = _as_bool(df["gate_passed"])
    df["expected_positive_bool"] = _as_bool(df["expected_context_positive"])
    df["missing_panel_bool"] = _as_bool(df["missing_panel_dropout"])
    df["confounded_bool"] = _as_bool(df["fov_or_sample_confounded"])
    positive_routes = {
        "compressed_context",
        "context_allowed",
        "full_context",
        "positive_control_only",
    }
    always_positive_routes = set(
        df.loc[
            (df["method_id"] == "always_true_neighbor_mean")
            & df["expected_positive_bool"]
            & df["observed_route"].isin(positive_routes),
            "ladder_case_id",
        ].astype(str)
    )
    rows = []
    for method_id, group in df.groupby("method_id", dropna=False):
        positives = group[group["expected_positive_bool"]]
        recovered = positives[positives["gate_passed_bool"]]
        null_or_confounded = group[~group["expected_positive_bool"]]
        negative_passed = null_or_confounded[null_or_confounded["gate_passed_bool"]]
        missing_panel = group[group["missing_panel_bool"]]
        confounded = group[group["confounded_bool"]]
        positive_total = len(positives)
        recovered_total = len(recovered)
        negative_total = len(null_or_confounded)
        negative_passed_total = len(negative_passed)
        positive_wilson_low, positive_wilson_high = _wilson_interval(
            recovered_total,
            positive_total,
        )
        negative_wilson_low, negative_wilson_high = _wilson_interval(
            negative_passed_total,
            negative_total,
        )
        positive_score_ci_low, positive_score_ci_high = _mean_interval(
            positives["sensitivity"]
        )
        specificity_score_ci_low, specificity_score_ci_high = _mean_interval(
            null_or_confounded["specificity"]
        )
        weak = positives[
            positives["control_level"] == "weak_or_noisy_injected_context_signal"
        ]
        localized = positives[positives["control_level"] == "localized_context_signal"]
        strong = positives[
            positives["control_level"] == "strong_injected_context_signal"
        ]
        observed_positive_routes = set(
            positives.loc[
                positives["observed_route"].isin(positive_routes),
                "ladder_case_id",
            ].astype(str)
        )
        positive_route_misses = len(
            always_positive_routes.difference(observed_positive_routes)
        )
        rows.append(
            {
                "Method": _method_label(method_id),
                "Positive rows": positive_total,
                "Recovered positive rows": recovered_total,
                "Positive route recovery rate": (
                    recovered_total / positive_total if positive_total else None
                ),
                "Positive route recovery Wilson low": positive_wilson_low,
                "Positive route recovery Wilson high": positive_wilson_high,
                "Mean positive sensitivity score CI low": positive_score_ci_low,
                "Mean positive sensitivity score CI high": positive_score_ci_high,
                "Strong-signal recovery rate": (
                    pd.to_numeric(strong["gate_passed_bool"], errors="coerce").mean()
                    if not strong.empty
                    else None
                ),
                "Weak/noisy recovery rate": (
                    pd.to_numeric(weak["gate_passed_bool"], errors="coerce").mean()
                    if not weak.empty
                    else None
                ),
                "Localized recovery rate": (
                    pd.to_numeric(
                        localized["gate_passed_bool"],
                        errors="coerce",
                    ).mean()
                    if not localized.empty
                    else None
                ),
                "Positive route misses vs always-context": positive_route_misses,
                "Smallest recovered injected strength": (
                    pd.to_numeric(
                        recovered["injected_signal_strength"],
                        errors="coerce",
                    ).min()
                    if not recovered.empty
                    else None
                ),
                "Smallest recovered effective strength": (
                    pd.to_numeric(
                        recovered["effective_signal_strength"],
                        errors="coerce",
                    ).min()
                    if not recovered.empty
                    else None
                ),
                "Mean positive sensitivity": pd.to_numeric(
                    positives["sensitivity"],
                    errors="coerce",
                ).mean(),
                "Null/confounded rows": negative_total,
                "Null/confounded gate-pass rows": negative_passed_total,
                "Null/confounded gate-pass rate": (
                    negative_passed_total / negative_total if negative_total else None
                ),
                "Null/confounded gate-pass Wilson low": negative_wilson_low,
                "Null/confounded gate-pass Wilson high": negative_wilson_high,
                "Mean null/confounded specificity CI low": specificity_score_ci_low,
                "Mean null/confounded specificity CI high": specificity_score_ci_high,
                "Mean null/confounded specificity": pd.to_numeric(
                    null_or_confounded["specificity"],
                    errors="coerce",
                ).mean(),
                "Max null/confounded FCR": pd.to_numeric(
                    null_or_confounded["false_positive_context_rate"],
                    errors="coerce",
                ).max(),
                "Missing-panel abstention": pd.to_numeric(
                    missing_panel["abstention_rate"],
                    errors="coerce",
                ).mean(),
                "Confounded abstention": pd.to_numeric(
                    confounded["abstention_rate"],
                    errors="coerce",
                ).mean(),
                "Detectability interpretation": (
                    "Recovered all positive ladder rungs; synthetic floor is not a real-data power bound"
                    if recovered_total == positive_total and positive_total > 0
                    else (
                        "Recovered some injected positive rows; synthetic floor is method-limited"
                        if not recovered.empty
                        else "No injected positive signal recovered under this method"
                    )
                ),
                "Source artifact": (
                    "results/reports/cp_q3_positive_null_control_ladder/"
                    "positive_control_ladder.csv"
                ),
            }
        )
    return pd.DataFrame(rows).sort_values(
        [
            "Smallest recovered effective strength",
            "Max null/confounded FCR",
            "Method",
        ],
        na_position="last",
    )


def build_positive_control_scope_k_audit() -> pd.DataFrame:
    cases = _read_csv("cp_q3_positive_null_control_ladder/ladder_cases.csv")
    ladder = _read_csv("cp_q3_positive_null_control_ladder/positive_control_ladder.csv")
    summary = _read_json(
        "cp_q3_positive_null_control_ladder/positive_control_ladder_summary.json"
    )
    contextgate = ladder[ladder["method_id"] == "contextgate_transparent_router"].copy()
    contextgate["gate_passed_bool"] = _as_bool(contextgate["gate_passed"])
    contextgate["expected_positive_bool"] = _as_bool(
        contextgate["expected_context_positive"]
    )
    cases["expected_positive_bool"] = _as_bool(cases["expected_context_positive"])

    rows = [
        {
            "Audit item": "Registered neighborhood scale",
            "Registered CP-Q3 value": (
                "k=5 Euclidean nearest-neighbor mean pooling within registered "
                "sample/slide boundaries"
            ),
            "Observed CP-Q3 evidence": (
                f"{summary['ladder_case_count']} ladder cases; "
                f"{summary['positive_control_ladder_row_count']} method rows; "
                f"{summary['dataset_count']} datasets, {summary['split_count']} splits, "
                f"{summary['seed_count']} seeds"
            ),
            "Scope implication": (
                "Detectability statements apply to the registered k=5 graph, not "
                "to alternative radii or graph topologies."
            ),
            "K-sensitivity status": (
                "No k=3 or k=10 CP-Q3 route artifacts are registered locally."
            ),
            "Source artifact": "positive_control_ladder_summary.json",
            "Rerun decision": (
                "Level 3 local scope audit; bounded CP-Q3 rerun only if future "
                "claims require k-robustness."
            ),
        },
        {
            "Audit item": "Injection/evaluation operator match",
            "Registered CP-Q3 value": (
                "Synthetic injection uses the same k=5 mean-neighbor operator "
                "as the evaluator feature, over synthetic marker set L+"
            ),
            "Observed CP-Q3 evidence": (
                "ContextGate recovers matched linear mean-neighbor positives and "
                "rejects null/missing-panel/confounded controls."
            ),
            "Scope implication": (
                "The ladder validates wiring and matched linear mean-neighbor "
                "detectability, not broad sensitivity to nonlinear biology."
            ),
            "K-sensitivity status": "Fixed-k operator identity; no mismatched-k probe.",
            "Source artifact": "ladder_cases.csv; positive_control_ladder.csv",
            "Rerun decision": "No Modal trigger; manuscript claim is scoped to k=5.",
        },
    ]

    for control_level, group in cases.groupby("control_level", dropna=False):
        cg_group = contextgate[contextgate["control_level"] == control_level]
        row_count = len(cg_group)
        pass_count = int(cg_group["gate_passed_bool"].sum())
        effective = pd.to_numeric(group["effective_signal_strength"], errors="coerce")
        signal = pd.to_numeric(group["injected_signal_strength"], errors="coerce")
        noise = pd.to_numeric(group["noise_fraction"], errors="coerce")
        prevalence = pd.to_numeric(group["prevalence"], errors="coerce")
        expected_positive = bool(group["expected_positive_bool"].any())
        rows.append(
            {
                "Audit item": f"Ladder rung: {_friendly(control_level)}",
                "Registered CP-Q3 value": (
                    f"s={signal.mean():.2f}; effective range "
                    f"{effective.min():.3f}-{effective.max():.3f}; "
                    f"noise={noise.mean():.2f}; prevalence={prevalence.mean():.2f}; "
                    f"scope={_compact_unique(group['localization_scope'])}"
                ),
                "Observed CP-Q3 evidence": (
                    f"ContextGate pass {pass_count}/{row_count}; observed routes: "
                    f"{_compact_unique(cg_group['observed_route'])}"
                ),
                "Scope implication": (
                    "Target-observable synthetic positive rung."
                    if expected_positive
                    else (
                        "Control rung: correct behavior is rejection or abstention, "
                        "not a real context claim."
                    )
                ),
                "K-sensitivity status": (
                    "Measured only at k=5; no local k sweep for this rung."
                ),
                "Source artifact": "ladder_cases.csv; positive_control_ladder.csv",
                "Rerun decision": "No Modal trigger for scope-only manuscript hardening.",
            }
        )

    rows.append(
        {
            "Audit item": "Effect-size calibration boundary",
            "Registered CP-Q3 value": (
                "effective_signal_strength = registered s plus deterministic "
                "0-0.02 jitter, clipped at 1.0"
            ),
            "Observed CP-Q3 evidence": (
                "Smallest recovered ContextGate positive has s=0.55 and "
                "effective strength about 0.55-0.57 across seeds/datasets."
            ),
            "Scope implication": (
                "This is a unitless synthetic ladder coefficient, not a residual-SD "
                "or published LR/co-expression effect-size calibration."
            ),
            "K-sensitivity status": (
                "Effect-size boundary is tied to k=5 and the matched linear operator."
            ),
            "Source artifact": (
                "src/cellpack/positive_control_ladder.py; ladder_cases.csv"
            ),
            "Rerun decision": (
                "No Modal trigger; future literature-calibrated or residual-SD "
                "power claims would require new registered analysis."
            ),
        }
    )
    return pd.DataFrame(rows)


def build_real_vs_detectability_audit() -> pd.DataFrame:
    metric_matrix = _read_csv("cp_q6_benchmark_matrix/benchmark_metric_matrix.csv")
    q1_contextgate = metric_matrix[
        (metric_matrix["benchmark_tier"] == "q1")
        & (metric_matrix["method_id"] == "contextgate_transparent_router")
    ]
    threshold = _read_csv("cp_q7_robustness_stress/threshold_sensitivity.csv")
    ladder = _read_csv("cp_q3_positive_null_control_ladder/positive_control_ladder.csv")
    decisions = _read_csv("cp_q5_contextgate_decisions/contextgate_decisions.csv")

    threshold["passed_bool"] = _as_bool(threshold["passed"])
    ladder["gate_passed_bool"] = _as_bool(ladder["gate_passed"])
    ladder["expected_positive_bool"] = _as_bool(ladder["expected_context_positive"])
    contextgate_ladder = ladder[ladder["method_id"] == "contextgate_transparent_router"]
    recovered = contextgate_ladder[
        contextgate_ladder["expected_positive_bool"]
        & contextgate_ladder["gate_passed_bool"]
    ]
    min_recovered_effect = pd.to_numeric(
        recovered["effective_signal_strength"],
        errors="coerce",
    ).min()

    context_allowed_count = int((decisions["route_label"] == "context_allowed").sum())
    rows = [
        {
            "Calibration item": "FDR/q-value gate",
            "Observed real-data value": _metric_mean(
                q1_contextgate,
                "fdr_adjusted_p_value",
            ),
            "Reference threshold": 0.05,
            "Passes reference": False,
            "Interpretation": (
                "Mean ContextGate q-value proxy remains above the conventional "
                "FDR gate, so strong real-data context claims stay downgraded."
            ),
            "Source artifact": (
                "results/reports/cp_q6_benchmark_matrix/benchmark_metric_matrix.csv"
            ),
        },
        {
            "Calibration item": "Effect-size screen",
            "Observed real-data value": _metric_mean(q1_contextgate, "effect_size"),
            "Reference threshold": 0.05,
            "Passes reference": True,
            "Interpretation": (
                "Effect-size alone is not enough; it must also survive FDR, "
                "replication, residual, and wrong-context gates."
            ),
            "Source artifact": (
                "results/reports/cp_q7_robustness_stress/threshold_sensitivity.csv"
            ),
        },
        {
            "Calibration item": "False-context safety",
            "Observed real-data value": _metric_mean(
                q1_contextgate,
                "false_positive_context_rate",
            ),
            "Reference threshold": 0.05,
            "Passes reference": True,
            "Interpretation": (
                "The transparent router avoids real-data false-context use "
                "under the registered oracle labels."
            ),
            "Source artifact": (
                "results/reports/cp_q6_benchmark_matrix/benchmark_metric_matrix.csv"
            ),
        },
        {
            "Calibration item": "No-harm safety",
            "Observed real-data value": _metric_mean(q1_contextgate, "no_harm_rate"),
            "Reference threshold": 0.95,
            "Passes reference": True,
            "Interpretation": (
                "The router satisfies the tested no-harm threshold while "
                "remaining conservative."
            ),
            "Source artifact": (
                "results/reports/cp_q7_robustness_stress/threshold_sensitivity.csv"
            ),
        },
        {
            "Calibration item": "Held-out replication",
            "Observed real-data value": _metric_mean(
                q1_contextgate,
                "replication_rate",
            ),
            "Reference threshold": 0.6,
            "Passes reference": False,
            "Interpretation": (
                "Replication is approximately at the stricter threshold and "
                "does not rescue the strict real-data context claim."
            ),
            "Source artifact": (
                "results/reports/cp_q7_robustness_stress/threshold_sensitivity.csv"
            ),
        },
        {
            "Calibration item": "Residual delta direction",
            "Observed real-data value": _metric_mean(q1_contextgate, "residual_delta"),
            "Reference threshold": 0.0,
            "Passes reference": False,
            "Interpretation": (
                "Average residual delta is not a positive real-data context "
                "gain over expression-only baselines."
            ),
            "Source artifact": (
                "results/reports/cp_q6_benchmark_matrix/benchmark_metric_matrix.csv"
            ),
        },
        {
            "Calibration item": "Injected positive-control detectability",
            "Observed real-data value": min_recovered_effect,
            "Reference threshold": min_recovered_effect,
            "Passes reference": True,
            "Interpretation": (
                "The benchmark detects injected neighbor signal at this "
                "effective strength, so negative real-data gates are not a "
                "pure wiring failure."
            ),
            "Source artifact": (
                "results/reports/cp_q3_positive_null_control_ladder/"
                "positive_control_ladder.csv"
            ),
        },
        {
            "Calibration item": "Strict context-allowed route count",
            "Observed real-data value": context_allowed_count,
            "Reference threshold": 1,
            "Passes reference": context_allowed_count >= 1,
            "Interpretation": (
                "No real-data row reaches the strict route despite passing "
                "safety and positive-control mechanics checks."
            ),
            "Source artifact": (
                "results/reports/cp_q5_contextgate_decisions/contextgate_decisions.csv"
            ),
        },
    ]
    return pd.DataFrame(rows)


def _threshold_axis_value(frame: pd.DataFrame, axis: str) -> float:
    rows = frame[frame["stress_axis"].astype(str) == axis]
    if rows.empty:
        raise ValueError(f"Missing threshold-sensitivity axis: {axis}")
    values = pd.to_numeric(rows["observed_value"], errors="coerce").dropna()
    if values.empty:
        raise ValueError(f"Missing observed values for axis: {axis}")
    return float(values.mean())


def _threshold_level_list(values: pd.Series) -> str:
    numeric = pd.to_numeric(values, errors="coerce").dropna().sort_values()
    if not numeric.empty:
        return ", ".join(f"{value:g}" for value in numeric)
    return _compact_unique(values, limit=6)


def _pass_fail_levels(frame: pd.DataFrame, passed: bool) -> str:
    rows = frame[_as_bool(frame["passed"]) == passed]
    if rows.empty:
        return "none"
    return _threshold_level_list(rows["threshold_value"])


def build_threshold_operating_points() -> pd.DataFrame:
    threshold = _read_csv("cp_q7_robustness_stress/threshold_sensitivity.csv")
    q5_summary = _read_json(
        "cp_q5_contextgate_decisions/contextgate_decision_summary.json"
    )
    q6_summary = _read_json("cp_q6_benchmark_matrix/benchmark_matrix_summary.json")
    q3_methods = _read_csv("cp_q3_positive_null_control_ladder/method_summary.csv")
    decisions = _read_csv("cp_q5_contextgate_decisions/contextgate_decisions.csv")

    contextgate_ladder = q3_methods[
        q3_methods["method_id"] == "contextgate_transparent_router"
    ]
    if contextgate_ladder.empty:
        raise ValueError("Missing ContextGate positive/null summary row.")
    contextgate_ladder = contextgate_ladder.iloc[0]

    real_rows = decisions[
        decisions["source_table"].astype(str) != "positive_control_ladder"
    ]
    residual_pass_count = int(_as_bool(real_rows["residual_gate_passed"]).sum())

    observed = {
        "fdr": _threshold_axis_value(threshold, "fdr_threshold"),
        "effect_size": _threshold_axis_value(threshold, "effect_size_threshold"),
        "fcr": _threshold_axis_value(threshold, "false_positive_threshold"),
        "no_harm": _threshold_axis_value(threshold, "no_harm_threshold"),
        "replication": _threshold_axis_value(threshold, "replication_threshold"),
        "row_count": _threshold_axis_value(threshold, "min_row_count"),
        "route_recovery": float(q5_summary["positive_control_route_recovery_rate"]),
        "sensitivity": float(contextgate_ladder["mean_sensitivity_positive"]),
        "specificity": float(contextgate_ladder["mean_specificity_negative"]),
    }

    rows: list[dict] = []
    for definition in OPERATING_POINT_DEFINITIONS:
        fdr_pass = observed["fdr"] <= definition["fdr_threshold"]
        residual_pass = observed["effect_size"] > definition["residual_threshold"]
        fcr_pass = observed["fcr"] <= definition["fcr_ceiling"]
        route_recovery_pass = (
            observed["route_recovery"] >= definition["route_recovery_threshold"]
        )
        sensitivity_pass = observed["sensitivity"] >= definition["sensitivity_floor"]
        specificity_pass = observed["specificity"] >= definition["specificity_floor"]
        replication_pass = observed["replication"] >= definition["replication_floor"]
        no_harm_pass = observed["no_harm"] >= definition["no_harm_floor"]
        limiting = []
        if not fdr_pass:
            limiting.append("FDR")
        if not replication_pass:
            limiting.append("held-out replication")
        if residual_pass_count == 0:
            limiting.append("row-level residual utility")
        if not limiting:
            limiting.append("none")
        rows.append(
            {
                "Operating point": definition["label"],
                "Scope": definition["scope"],
                "FDR threshold": definition["fdr_threshold"],
                "Observed FDR stress value": observed["fdr"],
                "FDR passes": fdr_pass,
                "Residual-effect threshold": definition["residual_threshold"],
                "Observed effect-size stress value": observed["effect_size"],
                "Aggregate effect screen passes": residual_pass,
                "Real/source residual-pass rows": residual_pass_count,
                "Wrong-context separation rule": definition["wrong_context_rule"],
                "FCR ceiling": definition["fcr_ceiling"],
                "Observed FCR": observed["fcr"],
                "FCR passes": fcr_pass,
                "Route-recovery threshold": definition["route_recovery_threshold"],
                "Observed positive-control route recovery": observed["route_recovery"],
                "Route recovery passes": route_recovery_pass,
                "Sensitivity floor": definition["sensitivity_floor"],
                "Observed positive sensitivity": observed["sensitivity"],
                "Sensitivity passes": sensitivity_pass,
                "Specificity floor": definition["specificity_floor"],
                "Observed null specificity": observed["specificity"],
                "Specificity passes": specificity_pass,
                "Replication floor": definition["replication_floor"],
                "Observed replication stress value": observed["replication"],
                "Replication passes": replication_pass,
                "No-harm floor": definition["no_harm_floor"],
                "Observed no-harm": observed["no_harm"],
                "No-harm passes": no_harm_pass,
                "Expression-only decisions": int(
                    q5_summary.get("expression_only_decision_count", 0)
                ),
                "Abstain decisions": int(
                    q5_summary.get("abstention_decision_count", 0)
                ),
                "Positive-control-only decisions": int(
                    q5_summary.get("positive_control_only_decision_count", 0)
                ),
                "Context-allowed decisions": int(
                    q5_summary.get("context_allowed_decision_count", 0)
                ),
                "Skip decisions": int(q6_summary["skipped_jobs"]),
                "Central conclusion changes": "No",
                "Limiting criteria": "; ".join(limiting),
                "Rerun decision": (
                    "Local derivation from CP-Q5/CP-Q6/CP-Q7 artifacts; "
                    "no Modal rerun required."
                ),
                "Source artifacts": (
                    "results/reports/cp_q5_contextgate_decisions/"
                    "contextgate_decision_summary.json; "
                    "results/reports/cp_q6_benchmark_matrix/"
                    "benchmark_matrix_summary.json; "
                    "results/reports/cp_q7_robustness_stress/"
                    "threshold_sensitivity.csv"
                ),
            }
        )
    return pd.DataFrame(rows)


def build_threshold_axis_sensitivity() -> pd.DataFrame:
    threshold = _read_csv("cp_q7_robustness_stress/threshold_sensitivity.csv")
    threshold["passed_bool"] = _as_bool(threshold["passed"])
    rows: list[dict] = []
    axis_interpretation = {
        "effect_size_threshold": (
            "Effect-size thresholds pass at every tested level, but this does "
            "not override row-level residual, FDR, and replication gates."
        ),
        "false_positive_threshold": (
            "False-context safety is stable across tested FCR ceilings."
        ),
        "fdr_threshold": (
            "The strong biological context claim remains downgraded at every "
            "tested FDR threshold."
        ),
        "min_row_count": (
            "The benchmark has enough completed evidence rows for the stress "
            "suite after explicit skips."
        ),
        "no_harm_threshold": (
            "No-harm is stable across the tested conservative-to-lenient thresholds."
        ),
        "replication_threshold": (
            "Replication is the borderline axis: it passes only the lenient "
            "0.50 operating floor."
        ),
    }
    for axis, group in threshold.groupby("stress_axis", dropna=False):
        downgrades = group[group["claim_downgrade"] != "none"]
        rows.append(
            {
                "Threshold axis": _friendly(axis),
                "Observed value": pd.to_numeric(
                    group["observed_value"],
                    errors="coerce",
                ).mean(),
                "Threshold levels tested": _threshold_level_list(
                    group["threshold_value"]
                ),
                "Passing levels": _pass_fail_levels(group, True),
                "Failing levels": _pass_fail_levels(group, False),
                "Downgraded levels": (
                    _threshold_level_list(downgrades["threshold_value"])
                    if not downgrades.empty
                    else "none"
                ),
                "Downgrade reason": _compact_unique(
                    downgrades["claim_downgrade"].map(_friendly),
                    limit=4,
                )
                or "none",
                "Rows": len(group),
                "Interpretation": axis_interpretation.get(
                    str(axis),
                    "Threshold axis retained for operating-point audit.",
                ),
                "Source artifact": (
                    "results/reports/cp_q7_robustness_stress/threshold_sensitivity.csv"
                ),
            }
        )
    return pd.DataFrame(rows).sort_values(["Threshold axis"])


def _route_count_columns(q5_summary: dict, q6_summary: dict) -> dict:
    return {
        "Expression-only decisions": int(
            q5_summary.get("expression_only_decision_count", 0)
        ),
        "Abstain decisions": int(q5_summary.get("abstention_decision_count", 0)),
        "Positive-control-only decisions": int(
            q5_summary.get("positive_control_only_decision_count", 0)
        ),
        "Context-allowed decisions": int(
            q5_summary.get("context_allowed_decision_count", 0)
        ),
        "Skip decisions": int(q6_summary.get("skipped_jobs", 0)),
    }


def _threshold_direction(axis: str) -> str:
    directions = {
        "effect_size_threshold": "Absolute effect-size floor swept from 0.02 to 0.10.",
        "false_positive_threshold": "False-context ceiling swept from 0.00 to 0.10.",
        "fdr_threshold": "FDR/q-value ceiling swept from 0.01 to 0.10.",
        "min_row_count": "Minimum evidence-row floor swept from 3 to 30 rows.",
        "no_harm_threshold": "No-harm floor swept from 0.80 to 0.95.",
        "replication_threshold": "Held-out replication floor swept from 0.50 to 0.70.",
    }
    return directions.get(axis, "Registered threshold axis retained for audit.")


def _operating_projection_rows(
    q5_summary: dict,
    q6_summary: dict,
    observed: dict,
    residual_pass_count: int,
) -> list[dict]:
    route_counts = _route_count_columns(q5_summary, q6_summary)
    rows: list[dict] = []
    axes = [
        (
            "fdr_threshold",
            "FDR threshold",
            "fdr_threshold",
            "fdr",
            "Observed value <= threshold",
        ),
        (
            "false_context_ceiling",
            "False-context ceiling",
            "fcr_ceiling",
            "fcr",
            "Observed value <= threshold",
        ),
        (
            "route_recovery_floor",
            "Route-recovery floor",
            "route_recovery_threshold",
            "route_recovery",
            "Observed value >= threshold",
        ),
        (
            "positive_sensitivity_floor",
            "Positive sensitivity floor",
            "sensitivity_floor",
            "sensitivity",
            "Observed value >= threshold",
        ),
        (
            "null_specificity_floor",
            "Null specificity floor",
            "specificity_floor",
            "specificity",
            "Observed value >= threshold",
        ),
        (
            "replication_floor",
            "Held-out replication floor",
            "replication_floor",
            "replication",
            "Observed value >= threshold",
        ),
        (
            "no_harm_floor",
            "No-harm floor",
            "no_harm_floor",
            "no_harm",
            "Observed value >= threshold",
        ),
    ]
    for definition in OPERATING_POINT_DEFINITIONS:
        limiting = []
        if observed["fdr"] > definition["fdr_threshold"]:
            limiting.append("FDR")
        if residual_pass_count == 0:
            limiting.append("row-level residual utility")
        if observed["replication"] < definition["replication_floor"]:
            limiting.append("held-out replication")
        if not limiting:
            limiting.append("none")
        for axis_id, axis_label, threshold_key, observed_key, pass_rule in axes:
            threshold_value = definition[threshold_key]
            observed_value = observed[observed_key]
            if "<=" in pass_rule:
                passed = observed_value <= threshold_value
            else:
                passed = observed_value >= threshold_value
            rows.append(
                {
                    "Grid source": "Operating-point projection",
                    "Operating point": definition["label"],
                    "Threshold axis": axis_label,
                    "Axis id": axis_id,
                    "Threshold level": threshold_value,
                    "Observed value": observed_value,
                    "Comparator value": "",
                    "Pass rule": pass_rule,
                    "Passed": passed,
                    "Downgrade reason": (
                        "projected limiting criteria: " + "; ".join(limiting)
                    ),
                    "Claim": "strong biological context claim",
                    **route_counts,
                    "Central conclusion changes": "No",
                    "Direction tested": definition["scope"],
                    "Source artifact": (
                        "results/reports/cp_q5_contextgate_decisions/"
                        "contextgate_decision_summary.json; "
                        "results/reports/cp_q7_robustness_stress/"
                        "threshold_sensitivity.csv"
                    ),
                    "Notes": (
                        "Projection uses registered CP-Q5 route counts and "
                        "CP-Q7 observed stress values; it does not tune routes."
                    ),
                }
            )
    return rows


def build_threshold_grid_detail() -> pd.DataFrame:
    threshold = _read_csv("cp_q7_robustness_stress/threshold_sensitivity.csv")
    q5_summary = _read_json(
        "cp_q5_contextgate_decisions/contextgate_decision_summary.json"
    )
    q6_summary = _read_json("cp_q6_benchmark_matrix/benchmark_matrix_summary.json")
    q3_methods = _read_csv("cp_q3_positive_null_control_ladder/method_summary.csv")
    decisions = _read_csv("cp_q5_contextgate_decisions/contextgate_decisions.csv")

    contextgate_ladder = q3_methods[
        q3_methods["method_id"] == "contextgate_transparent_router"
    ]
    if contextgate_ladder.empty:
        raise ValueError("Missing ContextGate positive/null summary row.")
    contextgate_ladder = contextgate_ladder.iloc[0]

    real_rows = decisions[
        decisions["source_table"].astype(str) != "positive_control_ladder"
    ]
    residual_pass_count = int(_as_bool(real_rows["residual_gate_passed"]).sum())
    route_counts = _route_count_columns(q5_summary, q6_summary)
    observed = {
        "fdr": _threshold_axis_value(threshold, "fdr_threshold"),
        "effect_size": _threshold_axis_value(threshold, "effect_size_threshold"),
        "fcr": _threshold_axis_value(threshold, "false_positive_threshold"),
        "no_harm": _threshold_axis_value(threshold, "no_harm_threshold"),
        "replication": _threshold_axis_value(threshold, "replication_threshold"),
        "route_recovery": float(q5_summary["positive_control_route_recovery_rate"]),
        "sensitivity": float(contextgate_ladder["mean_sensitivity_positive"]),
        "specificity": float(contextgate_ladder["mean_specificity_negative"]),
    }

    rows: list[dict] = []
    for _, row in threshold.sort_values(
        ["stress_axis", "threshold_value", "stress_id"]
    ).iterrows():
        downgrade = str(row["claim_downgrade"])
        passed = str(row["passed"]).strip().lower() == "true"
        rows.append(
            {
                "Grid source": "CP-Q7 threshold-sensitivity row",
                "Operating point": "Axis-level CP-Q7 stress",
                "Threshold axis": _friendly(row["stress_axis"]),
                "Axis id": row["stress_axis"],
                "Threshold level": row["stress_level"],
                "Observed value": row["observed_value"],
                "Comparator value": row["comparator_value"],
                "Pass rule": "Observed value compared with threshold_value",
                "Passed": passed,
                "Downgrade reason": (
                    _friendly(downgrade) if downgrade != "none" else "none"
                ),
                "Claim": _friendly(row["claim_id"]),
                **route_counts,
                "Central conclusion changes": "No",
                "Direction tested": _threshold_direction(str(row["stress_axis"])),
                "Source artifact": (
                    "results/reports/cp_q7_robustness_stress/threshold_sensitivity.csv"
                ),
                "Notes": row["notes"],
            }
        )

    rows.extend(
        _operating_projection_rows(
            q5_summary=q5_summary,
            q6_summary=q6_summary,
            observed=observed,
            residual_pass_count=residual_pass_count,
        )
    )
    rows.extend(
        [
            {
                "Grid source": "Comparator threshold scope note",
                "Operating point": "Registered comparator helper",
                "Threshold axis": "Spatial-statistics expression-score threshold",
                "Axis id": "spatial_stats_expression_score_threshold",
                "Threshold level": "<=0.01 registered only",
                "Observed value": "",
                "Comparator value": "",
                "Pass rule": "Not swept in CP-Q7",
                "Passed": "",
                "Downgrade reason": "not row-generating in CP-Q7",
                "Claim": "method comparator scope",
                **route_counts,
                "Central conclusion changes": "No",
                "Direction tested": (
                    "Comparator-specific route threshold was documented, not "
                    "swept, because the strict ContextGate route count does "
                    "not depend on it."
                ),
                "Source artifact": (
                    "src/cellpack/method_comparison.py; "
                    "manuscript/tables/supp_table_s29_method_scope_fairness_audit.csv"
                ),
                "Notes": (
                    "Future method-tier sensitivity can sweep spatial-statistics "
                    "route thresholds such as >=0.50 or >=0.80."
                ),
            },
            {
                "Grid source": "Comparator threshold scope note",
                "Operating point": "Registered comparator helper",
                "Threshold axis": "Spatial-statistics context-score threshold",
                "Axis id": "spatial_stats_full_context_score_threshold",
                "Threshold level": ">=0.65 registered only",
                "Observed value": "",
                "Comparator value": "",
                "Pass rule": "Not swept in CP-Q7",
                "Passed": "",
                "Downgrade reason": "not row-generating in CP-Q7",
                "Claim": "method comparator scope",
                **route_counts,
                "Central conclusion changes": "No",
                "Direction tested": (
                    "Comparator-specific route threshold was documented, not "
                    "swept, because the strict ContextGate route count does "
                    "not depend on it."
                ),
                "Source artifact": (
                    "src/cellpack/method_comparison.py; "
                    "manuscript/tables/supp_table_s29_method_scope_fairness_audit.csv"
                ),
                "Notes": (
                    "The CP-Q8.8H stress audit does not use comparator-specific "
                    "threshold variants to support the zero real-data "
                    "context_allowed claim."
                ),
            },
        ]
    )
    return pd.DataFrame(rows)


def build_stress_family_accounting() -> pd.DataFrame:
    rows: list[dict] = []
    stress_totals = {
        "rows": 0,
        "passed": 0,
        "downgraded": 0,
        "failed_without_downgrade": 0,
    }
    for family, relative_path in CP_Q7_STRESS_FILES.items():
        df = _read_csv(relative_path)
        passed = int(_as_bool(df["passed"]).sum())
        downgraded = int((df["claim_downgrade"].astype(str) != "none").sum())
        failed_without = int(
            (
                (~_as_bool(df["passed"]))
                & (df["claim_downgrade"].astype(str) == "none")
            ).sum()
        )
        stress_totals["rows"] += len(df)
        stress_totals["passed"] += passed
        stress_totals["downgraded"] += downgraded
        stress_totals["failed_without_downgrade"] += failed_without
        rows.append(
            {
                "Accounting row": _friendly(family),
                "Accounting role": "Row-generating stress family",
                "Included in 127 stress-row denominator": "Yes",
                "Displayed in Figure 8": "Yes",
                "Rows": len(df),
                "Passed or survived rows": passed,
                "Downgraded rows": downgraded,
                "Failed without downgrade": failed_without,
                "Downgrade source": _compact_unique(
                    df.loc[
                        df["claim_downgrade"].astype(str) != "none",
                        "claim_downgrade",
                    ].map(_friendly),
                    limit=5,
                )
                or "none",
                "Denominator note": (
                    "Counts toward the 127 row-level CP-Q7 stress tests."
                ),
                "Source artifact": f"results/reports/{relative_path}",
            }
        )

    claim = _read_csv("cp_q7_robustness_stress/claim_survival_audit.csv")
    claim_survived = int(_as_bool(claim["claim_survives"]).sum())
    claim_downgraded = int((claim["claim_downgrade"].astype(str) != "none").sum())
    rows.append(
        {
            "Accounting row": "Claim survival audit",
            "Accounting role": "Separate claim-level audit",
            "Included in 127 stress-row denominator": "No",
            "Displayed in Figure 8": "No",
            "Rows": len(claim),
            "Passed or survived rows": claim_survived,
            "Downgraded rows": claim_downgraded,
            "Failed without downgrade": 0,
            "Downgrade source": _compact_unique(
                claim.loc[
                    claim["claim_downgrade"].astype(str) != "none",
                    "claim_downgrade",
                ].map(_friendly),
                limit=5,
            )
            or "none",
            "Denominator note": (
                "Separate six-claim audit; not a row-generating stress family "
                "and therefore not plotted in Figure 8."
            ),
            "Source artifact": (
                "results/reports/cp_q7_robustness_stress/claim_survival_audit.csv"
            ),
        }
    )
    rows.append(
        {
            "Accounting row": "Row-generating stress total",
            "Accounting role": "Stress-row denominator total",
            "Included in 127 stress-row denominator": "Yes",
            "Displayed in Figure 8": "Figure 8 sums these families",
            "Rows": stress_totals["rows"],
            "Passed or survived rows": stress_totals["passed"],
            "Downgraded rows": stress_totals["downgraded"],
            "Failed without downgrade": stress_totals["failed_without_downgrade"],
            "Downgrade source": "threshold sensitivity only",
            "Denominator note": (
                "Seven row-generating families produce 127 stress rows: "
                "122 pass and 5 carry explicit downgrades."
            ),
            "Source artifact": (
                "results/reports/cp_q7_robustness_stress/robustness_stress_summary.json"
            ),
        }
    )
    rows.append(
        {
            "Accounting row": "Combined reviewer accounting",
            "Accounting role": "Stress rows plus separate claim audit",
            "Included in 127 stress-row denominator": "No",
            "Displayed in Figure 8": "No",
            "Rows": stress_totals["rows"] + len(claim),
            "Passed or survived rows": stress_totals["passed"] + claim_survived,
            "Downgraded rows": stress_totals["downgraded"] + claim_downgraded,
            "Failed without downgrade": stress_totals["failed_without_downgrade"],
            "Downgrade source": "5 threshold-stress downgrades + 1 claim downgrade",
            "Denominator note": (
                "No seventh downgrade exists in the registered CP-Q7 artifacts; "
                "the manuscript wording is corrected to 5 + 1."
            ),
            "Source artifact": (
                "results/reports/cp_q7_robustness_stress/"
                "robustness_stress_summary.json; claim_survival_audit.csv"
            ),
        }
    )
    return pd.DataFrame(rows)


def build_claim_survival_reconciliation() -> pd.DataFrame:
    claim = _read_csv("cp_q7_robustness_stress/claim_survival_audit.csv")
    rows = []
    for _, row in claim.iterrows():
        survives = str(row["claim_survives"]).strip().lower() == "true"
        rows.append(
            {
                "Claim ID": row["claim_id"],
                "Claim": CLAIM_TEXT.get(row["claim_id"], _friendly(row["claim_id"])),
                "Claim status": _friendly(row["claim_status"]),
                "Claim survives": survives,
                "Claim downgrade": (
                    _friendly(row["claim_downgrade"])
                    if row["claim_downgrade"] != "none"
                    else "none"
                ),
                "Included in 127 stress-row denominator": "No",
                "Counts toward separate six-claim audit": "Yes",
                "Evidence pointer": row["evidence_pointer"],
                "Notes": row["notes"],
            }
        )
    return pd.DataFrame(rows)


def build_leakage_confounding_examples() -> pd.DataFrame:
    abstention = _read_csv(
        "cp_q5_contextgate_decisions/contextgate_abstention_audit.csv"
    )
    control_ablation = _read_csv("cp_q7_robustness_stress/control_ablation.csv")
    job_manifest = _read_csv("cp_q6_benchmark_matrix/job_manifest.csv")
    representative = _read_csv("cp_q4_failure_taxonomy/representative_examples.csv")

    def _abstention_row(reason_code: str) -> pd.Series | None:
        rows = abstention[abstention["reason_code"] == reason_code]
        if rows.empty:
            return None
        return rows.iloc[0]

    confound = _abstention_row("synthetic_confound_abstention")
    artifact = _abstention_row("artifact_or_confound_abstention")
    unreplicated = representative[
        representative["failure_class"] == "labels_not_replicated"
    ].iloc[0]
    unit_hash_jobs = int((job_manifest["split_id"] == "unit_hash_split").sum())
    heldout_jobs = int(
        job_manifest["split_id"].isin(["fov_holdout", "sample_holdout"]).sum()
    )
    max_comparator_fcr = pd.to_numeric(
        control_ablation["comparator_value"],
        errors="coerce",
    ).max()

    rows = [
        {
            "Audit example": "FOV/sample-confounded synthetic signal",
            "Leakage flag ell_i": 1,
            "Evidence rows": (
                int(confound["abstention_count"]) if confound is not None else 0
            ),
            "Route or gate effect": "abstain_uncertain",
            "Example pointer": (
                confound["example_evidence_pointer"] if confound is not None else ""
            ),
            "Reviewer interpretation": (
                "A signal tied to FOV/sample structure is not allowed to become "
                "a real spatial-neighbor claim."
            ),
        },
        {
            "Audit example": "Observed artifact/confound abstention",
            "Leakage flag ell_i": 1,
            "Evidence rows": (
                int(artifact["abstention_count"]) if artifact is not None else 0
            ),
            "Route or gate effect": "abstain_uncertain",
            "Example pointer": (
                artifact["example_evidence_pointer"] if artifact is not None else ""
            ),
            "Reviewer interpretation": (
                "Rows carrying FOV/sample artifact or unreplicated-label "
                "failure classes are blocked from context_allowed."
            ),
        },
        {
            "Audit example": "Wrong-context control pressure",
            "Leakage flag ell_i": 1,
            "Evidence rows": len(control_ablation),
            "Route or gate effect": "control_ablation_passed",
            "Example pointer": (
                "results/reports/cp_q7_robustness_stress/control_ablation.csv"
            ),
            "Reviewer interpretation": (
                "Always-context comparators retain high false-context behavior "
                f"(max comparator FCR {max_comparator_fcr:.3f}) when controls "
                "are ablated, supporting explicit wrong-context controls."
            ),
        },
        {
            "Audit example": "Unit-hash split alone is not a strict claim",
            "Leakage flag ell_i": 0,
            "Evidence rows": unit_hash_jobs,
            "Route or gate effect": "requires_heldout_support",
            "Example pointer": (
                "results/reports/cp_q6_benchmark_matrix/job_manifest.csv"
            ),
            "Reviewer interpretation": (
                f"Unit-hash jobs ({unit_hash_jobs}) are represented, but strict "
                f"context claims require held-out support; held-out jobs "
                f"represented here: {heldout_jobs}."
            ),
        },
        {
            "Audit example": "Held-out biological outcome not replicated",
            "Leakage flag ell_i": 1,
            "Evidence rows": 1,
            "Route or gate effect": "expression_only_or_abstain",
            "Example pointer": unreplicated["evidence_pointer"],
            "Reviewer interpretation": (
                "Candidate context signal that does not replicate is downgraded "
                "instead of being promoted by train-only evidence."
            ),
        },
    ]
    return pd.DataFrame(rows)


def build_downgrade_examples() -> pd.DataFrame:
    examples = _read_csv("cp_q4_failure_taxonomy/representative_examples.csv")
    downgrade = _read_csv("cp_q4_failure_taxonomy/claim_downgrade_audit.csv")
    merged = examples.merge(
        downgrade,
        on="failure_class",
        how="left",
    )
    out = merged[
        [
            "example_id",
            "example_type",
            "failure_class",
            "claim_downgrade",
            "dataset_id",
            "task_id",
            "method_id",
            "route_label",
            "blocked_claim",
            "required_next_step",
            "evidence_pointer",
            "interpretation",
        ]
    ].rename(
        columns={
            "example_id": "Example ID",
            "example_type": "Example type",
            "failure_class": "Failure class",
            "claim_downgrade": "Downgrade reason d_i",
            "dataset_id": "Dataset",
            "task_id": "Task",
            "method_id": "Method",
            "route_label": "Route",
            "blocked_claim": "Blocked claim",
            "required_next_step": "Required next step",
            "evidence_pointer": "Evidence pointer",
            "interpretation": "Interpretation",
        }
    )
    out["Failure class"] = out["Failure class"].map(_friendly)
    out["Downgrade reason d_i"] = (
        out["Downgrade reason d_i"].fillna("not_applicable").map(_friendly)
    )
    out["Dataset"] = out["Dataset"].map(_dataset_label)
    out["Task"] = out["Task"].map(_friendly)
    out["Method"] = out["Method"].map(_method_label)
    out["Route"] = out["Route"].map(
        lambda value: ROUTE_LABELS.get(str(value), _friendly(value))
    )
    out["Example type"] = out["Example type"].map(_friendly)
    return out


def build_residualization_audit() -> pd.DataFrame:
    metric_matrix = _read_csv("cp_q6_benchmark_matrix/benchmark_metric_matrix.csv")
    q1 = metric_matrix[metric_matrix["benchmark_tier"] == "q1"]
    contextgate = q1[q1["method_id"] == "contextgate_transparent_router"]
    expression = q1[q1["method_id"] == "expression_only_linear"]
    always_context = q1[q1["method_id"] == "always_true_neighbor_mean"]
    rows = [
        {
            "Audit item": "Expression-only residual baseline",
            "Feature set": "Center/unmasked expression only; no neighbor tokens.",
            "Target or metric": "Normalized target expression or task proxy.",
            "Observed value": _metric_mean(expression, "residual_delta"),
            "Fairness role": (
                "Defines what center expression already explains before "
                "neighbor context receives credit."
            ),
            "Known risk": (
                "If the baseline is underfit, context can appear useful; if it "
                "is too flexible, it can absorb true neighbor effects."
            ),
            "Source artifact": (
                "results/reports/cp_q6_benchmark_matrix/benchmark_metric_matrix.csv"
            ),
        },
        {
            "Audit item": "ContextGate residual delta",
            "Feature set": (
                "Evidence-routed context use; does not spend real context unless "
                "strict gates pass."
            ),
            "Target or metric": "residual_delta_vs_expression",
            "Observed value": _metric_mean(contextgate, "residual_delta"),
            "Fairness role": (
                "Measures whether routed context explains residual target "
                "signal beyond expression-only evidence."
            ),
            "Known risk": (
                "A conservative router may abstain from weak real effects that "
                "a future stronger model could exploit."
            ),
            "Source artifact": (
                "results/reports/cp_q6_benchmark_matrix/benchmark_metric_matrix.csv"
            ),
        },
        {
            "Audit item": "Always-context residual comparator",
            "Feature set": (
                "Center expression plus true-neighbor context for every row."
            ),
            "Target or metric": "residual_delta_vs_expression",
            "Observed value": _metric_mean(always_context, "residual_delta"),
            "Fairness role": (
                "Tests whether unconditional context use creates gains or "
                "false context when compared with expression-only."
            ),
            "Known risk": (
                "Can overuse spatial context and convert confounded/negative "
                "rows into false-context claims."
            ),
            "Source artifact": (
                "results/reports/cp_q6_benchmark_matrix/benchmark_metric_matrix.csv"
            ),
        },
        {
            "Audit item": "Wrong-context residual control",
            "Feature set": (
                "Center expression plus random, coordinate-shuffled, or distant "
                "neighbor context."
            ),
            "Target or metric": "false_positive_context_rate",
            "Observed value": _metric_mean(q1, "false_positive_context_rate"),
            "Fairness role": (
                "Separates physical-neighbor evidence from generic spatial, "
                "batch, or sampling artifacts."
            ),
            "Known risk": (
                "If controls are unavailable or mismatched, residual gains may "
                "be artifact-sensitive."
            ),
            "Source artifact": (
                "results/reports/cp_q6_benchmark_matrix/paired_method_tables.csv"
            ),
        },
        {
            "Audit item": "Residual claim boundary",
            "Feature set": "Registered CP-Q residual/task artifacts only.",
            "Target or metric": "strict_context_allowed_count",
            "Observed value": 0.0,
            "Fairness role": (
                "Prevents residual hints from being promoted into biological "
                "context-benefit claims without full gate support."
            ),
            "Known risk": (
                "This is a benchmark claim boundary, not proof that all "
                "biological residual context effects are absent."
            ),
            "Source artifact": (
                "results/reports/cp_q5_contextgate_decisions/contextgate_decisions.csv"
            ),
        },
    ]
    return pd.DataFrame(rows)


def _bool_mean(frame: pd.DataFrame, column: str) -> float | None:
    if frame.empty or column not in frame:
        return None
    return float(_as_bool(frame[column]).mean())


def _route_recovery(frame: pd.DataFrame) -> float | None:
    if frame.empty or {"true_route", "predicted_route"} - set(frame.columns):
        return None
    return float(
        (frame["true_route"].astype(str) == frame["predicted_route"].astype(str)).mean()
    )


def _add_q2_stratum(
    rows: list[dict],
    *,
    frame: pd.DataFrame,
    stratum: str,
    null_class: str,
    denominator_policy: str,
    primary_rate_label: str,
    interpretation: str,
) -> None:
    for method_id, group in frame.groupby("method_id", dropna=False):
        context_use_rate = _bool_mean(group, "uses_context")
        false_context_rate = _bool_mean(group, "false_positive_context_use")
        no_harm_rate = _bool_mean(group, "no_harm_success")
        if denominator_policy == "unsupported_context_exposure":
            primary_rate = context_use_rate
            specificity = None
        else:
            primary_rate = false_context_rate
            specificity = (
                None if false_context_rate is None else 1.0 - false_context_rate
            )
        rows.append(
            {
                "Source": "CP-Q2 method comparison",
                "Evidence stratum": stratum,
                "Null class": null_class,
                "Denominator policy": denominator_policy,
                "Method": _method_label(method_id),
                "Method family": _friendly(group["method_family"].iloc[0]),
                "Rows": len(group),
                "Context-use rate": context_use_rate,
                "False-context rows": int(
                    _as_bool(group["false_positive_context_use"]).sum()
                ),
                "Primary rate": primary_rate,
                "Primary rate label": primary_rate_label,
                "No-harm rate": no_harm_rate,
                "Null specificity": specificity,
                "Positive sensitivity": None,
                "Route recovery": _route_recovery(group),
                "Source artifact": (
                    "results/reports/cp_q2_method_comparison/method_predictions.csv"
                ),
                "Interpretation": interpretation,
            }
        )


def _add_q3_stratum(
    rows: list[dict],
    *,
    frame: pd.DataFrame,
    stratum: str,
    null_class: str,
    denominator_policy: str,
    primary_rate_label: str,
    interpretation: str,
) -> None:
    for method_id, group in frame.groupby("method_id", dropna=False):
        observed_context = group["observed_route"].astype(str).isin(CONTEXT_ROUTES)
        false_context = pd.to_numeric(
            group["false_positive_context_rate"],
            errors="coerce",
        )
        sensitivity = pd.to_numeric(group["sensitivity"], errors="coerce")
        specificity = pd.to_numeric(group["specificity"], errors="coerce")
        gate_passed = _as_bool(group["gate_passed"])
        if denominator_policy == "positive_control_sensitivity":
            primary_rate = float(sensitivity.mean())
            null_specificity = None
            positive_sensitivity = primary_rate
        else:
            primary_rate = float(false_context.mean())
            null_specificity = float(specificity.mean())
            positive_sensitivity = None
        rows.append(
            {
                "Source": "CP-Q3 positive/null ladder",
                "Evidence stratum": stratum,
                "Null class": null_class,
                "Denominator policy": denominator_policy,
                "Method": _method_label(method_id),
                "Method family": _friendly(group["method_family"].iloc[0]),
                "Rows": len(group),
                "Context-use rate": float(observed_context.mean()),
                "False-context rows": int((false_context > 0).sum()),
                "Primary rate": primary_rate,
                "Primary rate label": primary_rate_label,
                "No-harm rate": (
                    null_specificity
                    if denominator_policy != "positive_control_sensitivity"
                    else float(gate_passed.mean())
                ),
                "Null specificity": null_specificity,
                "Positive sensitivity": positive_sensitivity,
                "Route recovery": float(gate_passed.mean()),
                "Source artifact": (
                    "results/reports/cp_q3_positive_null_control_ladder/"
                    "positive_control_ladder.csv"
                ),
                "Interpretation": interpretation,
            }
        )


def _split_failure_classes(value: object) -> list[str]:
    if pd.isna(value):
        return []
    classes = [
        item.strip()
        for item in str(value).split(";")
        if item.strip() and item.strip() != "not_applicable"
    ]
    return classes


def _downgrade_gate_passed(row: pd.Series) -> bool:
    reason_code = str(row.get("reason_code", ""))
    if reason_code in DOWNGRADE_REASON_CODES:
        return False
    return len(_split_failure_classes(row.get("failure_class", ""))) == 0


def _mapped_gate_keys(row: pd.Series) -> list[str]:
    mapped: set[str] = set()
    reason_code = str(row.get("reason_code", ""))
    mapped.update(REASON_GATE_MAP.get(reason_code, []))
    for failure_class in _split_failure_classes(row.get("failure_class", "")):
        mapped.update(FAILURE_CLASS_GATE_MAP.get(failure_class, []))
    return [key for key, _, _, _ in GATE_DEFINITIONS if key in mapped]


def _gate_label(key: str) -> str:
    for gate_key, gate_label, _, _ in GATE_DEFINITIONS:
        if gate_key == key:
            return gate_label
    return _friendly(key)


def _gate_passes(row: pd.Series) -> dict[str, bool]:
    passes: dict[str, bool] = {}
    for key, _, _, column in GATE_DEFINITIONS:
        if key == "no_unresolved_downgrade":
            passes[key] = _downgrade_gate_passed(row)
        else:
            passes[key] = str(row.get(column, "")).strip().lower() == "true"
    return passes


def build_gate_failure_decomposition() -> pd.DataFrame:
    decisions = _read_csv("cp_q5_contextgate_decisions/contextgate_decisions.csv")
    rows = decisions[
        decisions["route_label"].astype(str) != "positive_control_only"
    ].copy()
    if rows.empty:
        raise ValueError("No non-positive-control ContextGate decisions found.")

    out_rows: list[dict] = []
    for _, row in rows.iterrows():
        passes = _gate_passes(row)
        failed_keys = [key for key, *_ in GATE_DEFINITIONS if not passes[key]]
        failed_labels = [_gate_label(key) for key in failed_keys]
        mapped_keys = _mapped_gate_keys(row)
        first_failed = failed_labels[0] if failed_labels else "none"
        first_non_residual = next(
            (_gate_label(key) for key in failed_keys if key != "residual_utility"),
            "none",
        )
        record = {
            "Decision ID": row["contextgate_decision_id"],
            "Source table": _friendly(row["source_table"]),
            "Dataset": _dataset_label(row["dataset_id"]),
            "Task": _friendly(row["task_id"]),
            "Target": _friendly(row["target_id"]),
            "Route": _route_label(row["route_label"]),
            "Reason code": _friendly(row["reason_code"]),
            "Failure class": _friendly(row["failure_class"]),
            "Failed gate count": len(failed_keys),
            "Failed gates": "; ".join(failed_labels) if failed_labels else "none",
            "First failed gate": first_failed,
            "First non-residual failed gate": first_non_residual,
            "Mapped taxonomy gates": (
                "; ".join(_gate_label(key) for key in mapped_keys)
                if mapped_keys
                else "none"
            ),
            "Evidence pointer": row["evidence_pointer"],
        }
        for key, label, _, _ in GATE_DEFINITIONS:
            record[f"{label} pass"] = int(passes[key])
        out_rows.append(record)

    order = {
        "Expression only": 0,
        "Abstain": 1,
    }
    out = pd.DataFrame(out_rows)
    out["route_sort"] = out["Route"].map(order).fillna(99)
    out = out.sort_values(
        [
            "route_sort",
            "Dataset",
            "Task",
            "Reason code",
            "Decision ID",
        ]
    )
    return out.drop(columns=["route_sort"])


def build_gate_failure_summary() -> pd.DataFrame:
    decomposition = build_gate_failure_decomposition()
    total_rows = len(decomposition)
    rows: list[dict] = []
    for key, label, condition, _ in GATE_DEFINITIONS:
        pass_column = f"{label} pass"
        failing = decomposition[decomposition[pass_column] == 0]
        pass_count = total_rows - len(failing)
        first_count = int((decomposition["First failed gate"] == label).sum())
        first_non_residual_count = int(
            (decomposition["First non-residual failed gate"] == label).sum()
        )
        mapped_count = int(
            decomposition["Mapped taxonomy gates"]
            .astype(str)
            .str.contains(label, regex=False)
            .sum()
        )
        if failing.empty:
            top_reasons = "none"
            top_failures = "none"
        else:
            top_reasons = "; ".join(
                f"{_friendly(reason)} ({count})"
                for reason, count in failing["Reason code"]
                .value_counts()
                .head(4)
                .items()
            )
            top_failures = "; ".join(
                f"{_friendly(reason)} ({count})"
                for reason, count in failing["Failure class"]
                .value_counts()
                .head(4)
                .items()
            )
        rows.append(
            {
                "Gate": label,
                "Equation condition": condition,
                "Failure count": len(failing),
                "Pass count": pass_count,
                "Pass rate": pass_count / total_rows if total_rows else None,
                "First-failing count": first_count,
                "First non-residual count": first_non_residual_count,
                "Mapped taxonomy/reason count": mapped_count,
                "Top failing reason codes": top_reasons,
                "Top failing failure classes": top_failures,
                "Interpretation": _gate_summary_interpretation(key),
                "Source artifact": (
                    "results/reports/cp_q5_contextgate_decisions/"
                    "contextgate_decisions.csv"
                ),
            }
        )
    return pd.DataFrame(rows)


def _gate_summary_interpretation(key: str) -> str:
    interpretations = {
        "residual_utility": (
            "Every non-positive-control row lacks positive residual utility, "
            "so the deterministic first-failing gate is residual direction."
        ),
        "fdr_effect": (
            "Rows failing here lack the registered effect-control evidence flag; "
            "this flag is distinct from the residual-utility sign gate."
        ),
        "wrong_context_separation": (
            "Rows failing here cannot separate true-neighbor evidence from "
            "wrong-context or access/artifact controls."
        ),
        "heldout_replication": (
            "Rows failing here do not meet held-out FOV/sample/donor "
            "replication requirements."
        ),
        "leakage_audit": (
            "Current rows pass the artifact-contract leakage audit; FOV/sample "
            "confounding is instead exposed through wrong-context, held-out, "
            "and downgrade gates."
        ),
        "no_unresolved_downgrade": (
            "Rows failing here carry explicit reason-code or failure-class "
            "downgrades that block context_allowed claims."
        ),
    }
    return interpretations[key]


def build_threshold_gate_policy() -> pd.DataFrame:
    gate_summary = build_gate_failure_summary()
    operating_points = build_threshold_operating_points()
    registered = operating_points[
        operating_points["Operating point"] == "Registered conservative"
    ]
    if registered.empty:
        raise ValueError("Missing registered conservative operating point.")
    registered = registered.iloc[0]

    rows = [
        {
            "Policy component": "False-context ceiling",
            "Registered value or observed rate": "FCR <= 0.05; observed FCR 0.000",
            "Rationale": (
                "Publication-facing context claims treat false spatial-context use "
                "as costlier than missed exploratory context leads; 0.05 is an "
                "expert-elicited strict false-claim ceiling rather than a "
                "biological constant."
            ),
            "Directionality": (
                "Biases against false positives and may increase abstain/expression-only routing."
            ),
            "Evidence table": "Supplementary Tables S24, S26, and S33A",
            "Rerun decision": "Local artifact/prose clarification; no Modal rerun.",
        },
        {
            "Policy component": "Positive-control route recovery",
            "Registered value or observed rate": "recovery >= 0.95; observed 1.000",
            "Rationale": (
                "A strict safety policy must still recover target-observable injected "
                "signal before negative real-data gates are interpretable, preventing "
                "the policy from achieving safety by never using context."
            ),
            "Directionality": (
                "Protects against a trivially safe never-context rule."
            ),
            "Evidence table": "Supplementary Tables S19, S26, and S35",
            "Rerun decision": "Local artifact/prose clarification; no Modal rerun.",
        },
        {
            "Policy component": "Sensitivity/specificity asymmetry",
            "Registered value or observed rate": (
                "sensitivity >= 0.65, specificity >= 0.80; observed 0.863/0.943"
            ),
            "Rationale": (
                "The operating point tolerates some false negatives while requiring "
                "stronger null rejection, reflecting publication rather than "
                "exploratory claim release and an explicit preference for avoiding "
                "false context claims over maximizing recall."
            ),
            "Directionality": (
                "False-negative leaning by design; exploratory users may inspect "
                "softer operating points with FCR exposed."
            ),
            "Evidence table": "Supplementary Tables S26, S33A, and S35",
            "Rerun decision": "Local artifact/prose clarification; no Modal rerun.",
        },
        {
            "Policy component": "Effect-control evidence gate",
            "Registered value or observed rate": (
                "a_i_eff = 1; observed CP-Q7 claim-level FDR-axis value "
                f"{float(registered['Observed FDR stress value']):.3f}"
            ),
            "Rationale": (
                "The registered effect-control flag records whether the row's "
                "source artifact clears its own BH/effect or synthetic-control "
                "evidence screen; it is not the same test as Delta_i > 0 and "
                "the CP-Q7 FDR-axis value is a claim-level stress statistic, not "
                "the row-level 40/63 pass count."
            ),
            "Directionality": (
                "Within-split BH screens do not control aggregate or spatially "
                "dependent FDR; the full AND gate supplies the conservative claim policy."
            ),
            "Evidence table": "Supplementary Tables S25, S26, and S33A",
            "Rerun decision": "Local artifact/prose clarification; no Modal rerun.",
        },
        {
            "Policy component": "Conjunctive gate design",
            "Registered value or observed rate": (
                "six mandatory row gates; 0 real/source residual-pass rows"
            ),
            "Rationale": (
                "Context is released only when residual utility, effect-control evidence, "
                "wrong-context separation, replication, leakage audit, and downgrade "
                "checks all support the claim; positive-control rows demonstrate the "
                "conjunction is passable when registered synthetic signal is present."
            ),
            "Directionality": (
                "Explicit false-negative bias; real-data marginal gate rates are "
                "diagnostics, and threshold sweeps still left zero context_allowed "
                "routes because residual-pass rows remained zero."
            ),
            "Evidence table": "Supplementary Tables S25, S26, and S33A",
            "Rerun decision": "Local artifact/prose clarification; no Modal rerun.",
        },
    ]

    for _, gate in gate_summary.iterrows():
        rows.append(
            {
                "Policy component": f"Gate pass rate: {gate['Gate']}",
                "Registered value or observed rate": (
                    f"{int(gate['Pass count'])}/{int(gate['Pass count']) + int(gate['Failure count'])} "
                    f"passed ({float(gate['Pass rate']):.3f})"
                ),
                "Rationale": gate["Interpretation"],
                "Directionality": (
                    "Shows which individual gate is binding before the AND rule is applied."
                ),
                "Evidence table": "Supplementary Table S25",
                "Rerun decision": "Derived from existing CP-Q5 decisions; no Modal rerun.",
            }
        )

    return pd.DataFrame(rows)


def build_stratified_false_context() -> pd.DataFrame:
    q2 = _read_csv("cp_q2_method_comparison/method_predictions.csv")
    q3 = _read_csv("cp_q3_positive_null_control_ladder/positive_control_ladder.csv")
    q3["expected_positive_bool"] = _as_bool(q3["expected_context_positive"])
    rows: list[dict] = []

    _add_q2_stratum(
        rows,
        frame=q2[q2["true_route"].astype(str) == "expression_only"],
        stratum="Real explicit negative-context rows",
        null_class="real negative context",
        denominator_policy="real_negative_fcr",
        primary_rate_label="Null-denominator FCR",
        interpretation=(
            "Strict real-data denominator where the registered route is "
            "expression-only."
        ),
    )
    _add_q2_stratum(
        rows,
        frame=q2[q2["true_route"].astype(str) == "abstain_uncertain"],
        stratum="Real unsupported or abstention rows",
        null_class="real unsupported evidence",
        denominator_policy="unsupported_context_exposure",
        primary_rate_label="Unsupported-context exposure",
        interpretation=(
            "Context use is counted as unsupported exposure rather than "
            "a strict false-positive flag."
        ),
    )
    _add_q2_stratum(
        rows,
        frame=q2,
        stratum="All CP-Q2 registered rows",
        null_class="all-row registered mix",
        denominator_policy="all_row_false_context_flag_mean",
        primary_rate_label="All-row false-context flag mean",
        interpretation=(
            "This is the source of the legacy 0.4783 always-context value; "
            "it is not the primary null-denominator FCR."
        ),
    )

    q3_strata = [
        (
            q3[q3["expected_positive_bool"]],
            "Synthetic positive-control rows",
            "positive controls",
            "positive_control_sensitivity",
            "Positive-control sensitivity",
            (
                "Sensitivity on injected spatial-signal rows; this separates "
                "ContextGate from expression-only despite equal real-data FCR."
            ),
        ),
        (
            q3[~q3["expected_positive_bool"]],
            "All synthetic null/control rows",
            "synthetic null/control",
            "synthetic_null_fcr",
            "Null-denominator FCR",
            "Full null-ladder denominator used for synthetic specificity.",
        ),
        (
            q3[q3["control_level"].astype(str) == "null_no_context_signal"],
            "Synthetic null no-context rows",
            "synthetic null",
            "synthetic_null_fcr",
            "Null-denominator FCR",
            "Evaluator-null rung with no injected neighbor dependency.",
        ),
        (
            q3[
                q3["control_level"].astype(str)
                == "missing_panel_or_target_dropout_signal"
            ],
            "Synthetic panel-limited/dropout rows",
            "panel-limited unobservable",
            "panel_limited_fcr",
            "Null-denominator FCR",
            (
                "Panel/dropout rung where neighbor context may be "
                "mathematically unobservable."
            ),
        ),
        (
            q3[q3["control_level"].astype(str) == "fov_or_sample_confounded_signal"],
            "Synthetic FOV/sample-confounded rows",
            "FOV/sample confounded",
            "confounded_context_fcr",
            "Null-denominator FCR",
            (
                "Confounded rung where apparent context tracks FOV/sample "
                "structure rather than permitted neighbor signal."
            ),
        ),
    ]
    for (
        frame,
        stratum,
        null_class,
        denominator_policy,
        primary_rate_label,
        interpretation,
    ) in q3_strata:
        _add_q3_stratum(
            rows,
            frame=frame,
            stratum=stratum,
            null_class=null_class,
            denominator_policy=denominator_policy,
            primary_rate_label=primary_rate_label,
            interpretation=interpretation,
        )

    out = pd.DataFrame(rows)
    method_order = {label: order for order, label in enumerate(METHOD_LABELS.values())}
    stratum_order = {
        "Real explicit negative-context rows": 0,
        "Real unsupported or abstention rows": 1,
        "All CP-Q2 registered rows": 2,
        "Synthetic positive-control rows": 3,
        "All synthetic null/control rows": 4,
        "Synthetic null no-context rows": 5,
        "Synthetic panel-limited/dropout rows": 6,
        "Synthetic FOV/sample-confounded rows": 7,
    }
    out["stratum_sort"] = out["Evidence stratum"].map(stratum_order).fillna(99)
    out["method_sort"] = out["Method"].map(method_order).fillna(99)
    return out.sort_values(["stratum_sort", "method_sort"]).drop(
        columns=["stratum_sort", "method_sort"]
    )


def build_control_taxonomy_sensitivity() -> pd.DataFrame:
    df = _read_csv("cp_q3_positive_null_control_ladder/positive_control_ladder.csv")
    df["gate_passed_bool"] = _as_bool(df["gate_passed"])
    df["expected_positive_bool"] = _as_bool(df["expected_context_positive"])
    df["missing_panel_bool"] = _as_bool(df["missing_panel_dropout"])
    df["confounded_bool"] = _as_bool(df["fov_or_sample_confounded"])

    strata = [
        {
            "Control taxonomy": "Registered positive controls",
            "frame": df[df["expected_positive_bool"]],
            "registered_denominator_role": "positive-control sensitivity numerator/denominator",
            "denominator_sensitivity_question": (
                "Injected target-observable neighbor signal."
            ),
        },
        {
            "Control taxonomy": "Registered null/control denominator",
            "frame": df[~df["expected_positive_bool"]],
            "registered_denominator_role": "primary synthetic null/control denominator",
            "denominator_sensitivity_question": (
                "Current registered specificity/FCR denominator, including "
                "panel-blocked rows."
            ),
        },
        {
            "Control taxonomy": "Null/control excluding panel-blocked rows",
            "frame": df[(~df["expected_positive_bool"]) & (~df["missing_panel_bool"])],
            "registered_denominator_role": "sensitivity analysis denominator",
            "denominator_sensitivity_question": (
                "Tests safety after removing structurally unobservable "
                "missing-panel/dropout rows."
            ),
        },
        {
            "Control taxonomy": "Pure synthetic null rung",
            "frame": df[df["control_level"].astype(str) == "null_no_context_signal"],
            "registered_denominator_role": "synthetic null sub-stratum",
            "denominator_sensitivity_question": (
                "No injected neighbor dependency; direct null rejection check."
            ),
        },
        {
            "Control taxonomy": "Panel-blocked positive rung",
            "frame": df[df["missing_panel_bool"]],
            "registered_denominator_role": (
                "reported separately; included in primary denominator as "
                "claim-unobservable"
            ),
            "denominator_sensitivity_question": (
                "High-amplitude sender signal with receiver/target "
                "observability deliberately blocked."
            ),
        },
        {
            "Control taxonomy": "FOV/sample-confounded rung",
            "frame": df[df["confounded_bool"]],
            "registered_denominator_role": "synthetic confound sub-stratum",
            "denominator_sensitivity_question": (
                "Nonlocal FOV/sample structure replaces permitted neighbor "
                "evidence."
            ),
        },
    ]

    rows: list[dict] = []
    for stratum in strata:
        frame = stratum["frame"]
        for method_id, group in frame.groupby("method_id", dropna=False):
            rows_total = len(group)
            gate_passed = int(group["gate_passed_bool"].sum())
            pass_low, pass_high = _wilson_interval(gate_passed, rows_total)
            sensitivity_low, sensitivity_high = _mean_interval(group["sensitivity"])
            specificity_low, specificity_high = _mean_interval(group["specificity"])
            false_context = pd.to_numeric(
                group["false_positive_context_rate"],
                errors="coerce",
            )
            observed_routes = "; ".join(
                f"{_route_label(route)} ({count})"
                for route, count in group["observed_route"]
                .astype(str)
                .value_counts()
                .sort_index()
                .items()
            )
            rows.append(
                {
                    "Control taxonomy": stratum["Control taxonomy"],
                    "Registered denominator role": (
                        stratum["registered_denominator_role"]
                    ),
                    "Method": _method_label(method_id),
                    "Rows": rows_total,
                    "Observed routes": observed_routes,
                    "Binary gate-pass rows": gate_passed,
                    "Binary gate-pass rate": (
                        gate_passed / rows_total if rows_total else None
                    ),
                    "Binary gate-pass Wilson low": pass_low,
                    "Binary gate-pass Wilson high": pass_high,
                    "Mean sensitivity score": pd.to_numeric(
                        group["sensitivity"],
                        errors="coerce",
                    ).mean(),
                    "Sensitivity score CI low": sensitivity_low,
                    "Sensitivity score CI high": sensitivity_high,
                    "Mean specificity score": pd.to_numeric(
                        group["specificity"],
                        errors="coerce",
                    ).mean(),
                    "Specificity score CI low": specificity_low,
                    "Specificity score CI high": specificity_high,
                    "False-context rate": false_context.mean(),
                    "False-context rows": int((false_context > 0).sum()),
                    "Denominator sensitivity question": (
                        stratum["denominator_sensitivity_question"]
                    ),
                    "Source artifact": (
                        "results/reports/cp_q3_positive_null_control_ladder/"
                        "positive_control_ladder.csv"
                    ),
                }
            )

    out = pd.DataFrame(rows)
    taxonomy_order = {
        "Registered positive controls": 0,
        "Registered null/control denominator": 1,
        "Null/control excluding panel-blocked rows": 2,
        "Pure synthetic null rung": 3,
        "Panel-blocked positive rung": 4,
        "FOV/sample-confounded rung": 5,
    }
    method_order = {label: order for order, label in enumerate(METHOD_LABELS.values())}
    out["taxonomy_sort"] = out["Control taxonomy"].map(taxonomy_order).fillna(99)
    out["method_sort"] = out["Method"].map(method_order).fillna(99)
    return out.sort_values(["taxonomy_sort", "method_sort"]).drop(
        columns=["taxonomy_sort", "method_sort"]
    )


def build_utility_matrix_construction() -> pd.DataFrame:
    q2_metrics = _read_csv("cp_q2_method_comparison/method_metrics.csv")
    q2_predictions = _read_csv("cp_q2_method_comparison/method_predictions.csv")
    q6_aggregate = _read_csv("cp_q6_benchmark_matrix/aggregate_metrics.csv")

    route_utility = {
        "expression_only": {
            "expression_only": 1.0,
            "abstain_uncertain": 0.60,
            "full_context": 0.0,
            "compressed_context": 0.0,
            "context_allowed": 0.0,
        },
        "full_context": {
            "full_context": 1.0,
            "context_allowed": 1.0,
            "compressed_context": 0.85,
            "abstain_uncertain": 0.40,
            "expression_only": 0.0,
        },
        "compressed_context": {
            "compressed_context": 1.0,
            "context_allowed": 0.85,
            "full_context": 0.85,
            "abstain_uncertain": 0.40,
            "expression_only": 0.0,
        },
        "abstain_uncertain": {
            "abstain_uncertain": 1.0,
            "expression_only": 0.70,
            "full_context": 0.20,
            "compressed_context": 0.20,
            "context_allowed": 0.20,
        },
    }

    rows: list[dict] = []
    tier_rows = [
        (
            "CP-Q2",
            "Route-comparison method subset",
            "23 CP-R1 route rows x 10 registered method-family rules",
            "Label-alignment utility and regret table used for Figure 3.",
            "results/reports/cp_q2_method_comparison/method_predictions.csv",
        ),
        (
            "CP-Q3",
            "Positive/null-control ladder",
            "72 ladder rows per registered method family",
            "Synthetic detectability and null/control safety checks.",
            "results/reports/cp_q3_positive_null_control_ladder/positive_control_ladder.csv",
        ),
        (
            "CP-Q5",
            "ContextGate decision table",
            "100 claim-to-evidence route decisions",
            "Strict route release table combining CP-Q3, CP-R1, and rejected/access rows.",
            "results/reports/cp_q5_contextgate_decisions/contextgate_decisions.csv",
        ),
        (
            "CP-Q6",
            "Full benchmark execution matrix",
            "2,760 planned jobs, 2,324 completed jobs, 34,860 metric rows",
            "Infrastructure-scale metric, skip, and robustness evidence; not one route decision per job.",
            "results/reports/cp_q6_benchmark_matrix/benchmark_metric_matrix.csv",
        ),
        (
            "CP-Q7",
            "Reviewer stress suite",
            "127 stress rows plus claim-survival audit",
            "Threshold, seed, ablation, compute, and claim-survival checks.",
            "results/reports/cp_q7_robustness_stress/stress_test_manifest.csv",
        ),
        (
            "CP-Q8.x",
            "Review-hardening layer",
            "Reviewer-facing audit tables, prose patches, and rerun decisions",
            "Manuscript hardening; does not change registered route logic unless a stop rule fires.",
            "manuscript/reviewer_hardening/",
        ),
        (
            "CP-R1",
            "Context-utility atlas",
            "23 route-level context-utility rows",
            "Route evidence rows feeding CP-Q2 and CP-Q5 context-utility decisions.",
            "results/reports/cp_r1_context_utility_atlas/run_context_utility.csv",
        ),
    ]
    for label, meaning, unit, role, source in tier_rows:
        rows.append(
            {
                "Audit group": "Tier glossary",
                "Item": label,
                "Setting or scope": unit,
                "Value": meaning,
                "Operational definition": role,
                "Reviewer boundary": (
                    "Tier labels name artifact scope; they are not interchangeable denominators."
                ),
                "Source artifact": source,
            }
        )

    for true_route, predicted_map in route_utility.items():
        for predicted_route, utility in predicted_map.items():
            rows.append(
                {
                    "Audit group": "Route utility matrix",
                    "Item": "u_im",
                    "Setting or scope": (
                        f"true={_route_label(true_route)}; "
                        f"predicted={_route_label(predicted_route)}"
                    ),
                    "Value": utility,
                    "Operational definition": (
                        "CP-Q2 route-level utility assigned before averaging method regret."
                    ),
                    "Reviewer boundary": (
                        "This is a registered route-label agreement utility, not an independent predictive metric."
                    ),
                    "Source artifact": "src/cellpack/method_comparison.py",
                }
            )

    q2_route_settings = q2_predictions[
        ["context_utility_id", "true_route"]
    ].drop_duplicates()
    true_route_counts = (
        q2_route_settings["true_route"].astype(str).value_counts().sort_index()
    )
    for route, count in true_route_counts.items():
        rows.append(
            {
                "Audit group": "CP-Q2 route mix",
                "Item": _route_label(route),
                "Setting or scope": "registered CP-Q2 true_route labels",
                "Value": int(count),
                "Operational definition": (
                    "Route rows over which CP-Q2 method utility and regret are averaged."
                ),
                "Reviewer boundary": (
                    "The CP-Q2 denominator is a 23-row route subset, not the full CP-Q6 matrix."
                ),
                "Source artifact": (
                    "results/reports/cp_q2_method_comparison/method_predictions.csv"
                ),
            }
        )

    for method_id in [
        "contextgate_transparent_router",
        "spatial_statistics_heuristic",
        "always_true_neighbor_mean",
    ]:
        method_row = q2_metrics[q2_metrics["method_id"] == method_id]
        if method_row.empty:
            continue
        row = method_row.iloc[0]
        rows.append(
            {
                "Audit group": "CP-Q2 method regret scope",
                "Item": _method_label(method_id),
                "Setting or scope": "CP-Q2 route-comparison subset",
                "Value": f"mean utility={float(row['mean_utility']):.4f}; mean regret={float(row['mean_regret']):.4f}",
                "Operational definition": (
                    "Mean route utility/regret over 23 CP-R1 route rows using the registered route utility matrix."
                ),
                "Reviewer boundary": (
                    "Measures agreement with CP-Q2 oracle route labels; does not prove biological optimality."
                ),
                "Source artifact": (
                    "results/reports/cp_q2_method_comparison/method_metrics.csv"
                ),
            }
        )

    q6_contextgate = q6_aggregate[
        (q6_aggregate["method_id"] == "contextgate_transparent_router")
        & (q6_aggregate["metric_name"] == "regret_against_oracle")
    ]
    for _, row in q6_contextgate.sort_values("benchmark_tier").iterrows():
        rows.append(
            {
                "Audit group": "CP-Q6 regret scope",
                "Item": f"ContextGate {row['benchmark_tier']}",
                "Setting or scope": "CP-Q6 full benchmark aggregate",
                "Value": (
                    f"mean regret={float(row['mean_metric_value']):.4f}; "
                    f"metric rows={int(row['row_count'])}"
                ),
                "Operational definition": (
                    "Aggregate CP-Q6 regret_against_oracle metric over benchmark-matrix rows."
                ),
                "Reviewer boundary": (
                    "Different tier and denominator from the CP-Q2 Figure 3 value."
                ),
                "Source artifact": (
                    "results/reports/cp_q6_benchmark_matrix/aggregate_metrics.csv"
                ),
            }
        )

    shared_score_rows = [
        (
            "spatial_statistics_heuristic",
            "Routes from CP-R1 context_utility_score using <=0.01 expression-only and >=0.65 context thresholds.",
        ),
        (
            "lightweight_graphsage_aggregation",
            "Uses the same CP-R1 context_utility_score plus gene-count availability as a graph-style proxy.",
        ),
        (
            "contextgate_transparent_router",
            "Uses residual context utility and evidence-class gates, then applies wrong-context, replication, leakage, and downgrade screens.",
        ),
    ]
    for method_id, definition in shared_score_rows:
        rows.append(
            {
                "Audit group": "Shared-score comparator boundary",
                "Item": _method_label(method_id),
                "Setting or scope": "CP-Q2/CP-R1 route proxy",
                "Value": "threshold-policy comparator",
                "Operational definition": definition,
                "Reviewer boundary": (
                    "These rows should be read as threshold-policy sensitivity over shared route evidence, not as independent algorithmic consensus."
                ),
                "Source artifact": (
                    "src/cellpack/method_comparison.py; "
                    "results/reports/cp_r1_context_utility_atlas/run_context_utility.csv"
                ),
            }
        )

    return pd.DataFrame(rows)


def build_metric_definition_audit() -> pd.DataFrame:
    rows = [
        {
            "Definition group": "Input normalization",
            "Quantity": "x_i expression vector",
            "Operational definition": (
                "Processed nonnegative platform matrix with standardized gene "
                "symbols and aligned unit metadata; task features apply the "
                "registered task-layer transforms rather than pooling raw CosMx "
                "and Xenium scales directly."
            ),
            "Computation or scope": (
                "LR/module and marker summaries use log1p or unit-interval "
                "summaries where registered; label centroid features use log1p "
                "plus row L2 normalization; CellPack rows use rank/order and "
                "expression-bin tokens from the same matrix."
            ),
            "Interpretation boundary": (
                "Cross-platform summaries aggregate route/utility metrics after "
                "task-level normalization; they are not claims that raw platform "
                "count depths are interchangeable."
            ),
            "Source artifact or code": (
                "manuscript Section 3.3; src/cellpack/evaluation/*; "
                "src/cellpack/sequence_builder.py"
            ),
        },
        {
            "Definition group": "Utility and regret",
            "Quantity": "u_im and r_im",
            "Operational definition": (
                "u_im is the registered route-label or benchmark-matrix metric "
                "utility mapped to [0,1]; r_im equals the in-setting empirical "
                "oracle utility minus u_im."
            ),
            "Computation or scope": (
                "Route-level utilities come from the registered route utility "
                "matrix summarized in Supplementary Table S34; CP-Q6 metric rows "
                "use the normalized/proxy metric_value fields generated by the "
                "benchmark matrix."
            ),
            "Interpretation boundary": (
                "The oracle is the best registered method in the evaluated set, "
                "not an absolute biological or algorithmic performance ceiling; "
                "CP-Q2 route regret measures label alignment."
            ),
            "Source artifact or code": (
                "Supplementary Table S34; "
                "src/cellpack/method_comparison.py; "
                "results/reports/cp_q6_benchmark_matrix/"
                "benchmark_metric_matrix.csv"
            ),
        },
        {
            "Definition group": "Effect-control evidence gate",
            "Quantity": "a_i_eff and source q-values",
            "Operational definition": (
                "Binary registered effect-control flag used in Equation 5. For "
                "split-level rows, the source artifacts may include BH-adjusted "
                "q-values for their own context-vs-reference contrasts; for "
                "synthetic rows, the flag is the registered control-consistency "
                "gate."
            ),
            "Computation or scope": (
                "ContextGate reads the source flag as fdr_effect_gate_passed. A "
                "numeric q-value, when present, belongs to the source comparison "
                "table and is not reinterpreted as a one-sided test of the "
                "aggregate Delta_i sign gate."
            ),
            "Interpretation boundary": (
                "The effect-control flag can pass when the residual-utility sign "
                "gate fails because the two gates are different registered "
                "evidence checks; context_allowed requires both. Within-split BH "
                "screens are nominal and do not control the aggregate 40/63 pass "
                "count or spatially dependent tests globally."
            ),
            "Source artifact or code": (
                "src/cellpack/evaluation/router_target_mining.py; "
                "results/reports/cp_q6_benchmark_matrix/"
                "benchmark_metric_matrix.csv"
            ),
        },
        {
            "Definition group": "Safety metrics",
            "Quantity": "all-row false-context exposure",
            "Operational definition": (
                "Fraction of all evaluated rows, regardless of null status, where "
                "a method uses context on a row labeled null, wrong-context, or "
                "unsupported."
            ),
            "Computation or scope": (
                "Uses all rows as the denominator, unlike Equation 3 FCR, whose "
                "denominator is restricted to n_i = 1 rows."
            ),
            "Interpretation boundary": (
                "This is a population-level exposure descriptor and need not be "
                "the complement of denominator-aware no-harm unless both are "
                "computed on the same row set."
            ),
            "Source artifact or code": (
                "Supplementary Table S24; results/reports/cp_q6_benchmark_matrix/"
                "benchmark_metric_matrix.csv"
            ),
        },
        {
            "Definition group": "Safety metrics",
            "Quantity": "FCR, no-harm, specificity",
            "Operational definition": (
                "False-context rate is context use among null or unsupported "
                "rows; no-harm is one minus that rate; null specificity is "
                "non-context routing among synthetic null/control ladder rows."
            ),
            "Computation or scope": (
                "Pooled and denominator-stratified calculations are reported "
                "separately so wrong-context, unsupported real-data, and "
                "synthetic-null rows are not silently conflated."
            ),
            "Interpretation boundary": (
                "Expression-only and ContextGate can share FCR=0; ContextGate's "
                "added value is safety plus positive-control detection and "
                "auditable abstention."
            ),
            "Source artifact or code": (
                "Supplementary Table S24; "
                "Supplementary Table S35; "
                "results/reports/cp_q2_method_comparison/method_predictions.csv; "
                "results/reports/cp_q3_positive_null_control_ladder/"
                "positive_control_ladder.csv"
            ),
        },
        {
            "Definition group": "Positive/null ladder",
            "Quantity": "sensitivity score and specificity score",
            "Operational definition": (
                "Continuous diagnostic scores stored in the CP-Q3 sensitivity "
                "and specificity columns and summarized as row means with "
                "normal-approximation mean intervals."
            ),
            "Computation or scope": (
                "The positive-control sensitivity score is averaged over the "
                "36 target-observable positive rows; the null/control "
                "specificity score is averaged over the 36 registered "
                "negative/control rows and repeated without panel-blocked rows "
                "in Supplementary Table S35."
            ),
            "Interpretation boundary": (
                "These score means are distinct from the binary route "
                "recovery/rejection proportions in Equation 4; for ContextGate, "
                "0.8633 and 0.9433 are score means, while 36/36 and 36/36 are "
                "binary route outcomes."
            ),
            "Source artifact or code": (
                "Supplementary Tables S19 and S35; "
                "results/reports/cp_q3_positive_null_control_ladder/"
                "positive_control_ladder.csv; "
                "results/reports/cp_q3_positive_null_control_ladder/"
                "method_summary.csv"
            ),
        },
        {
            "Definition group": "Positive/null ladder",
            "Quantity": "gate_pass_rate",
            "Operational definition": (
                "Mean of the per-row gate_passed indicator in the synthetic "
                "positive/null ladder for a method family."
            ),
            "Computation or scope": (
                "Positive rows pass when sensitivity clears the registered floor "
                "and route is context-positive; negative rows pass when "
                "specificity clears the floor, no false context is used, and "
                "route is negative or abstained."
            ),
            "Interpretation boundary": (
                "This is control-consistency over synthetic labels, not the same "
                "quantity as sensitivity, specificity, or execution completeness."
            ),
            "Source artifact or code": (
                "src/cellpack/positive_control_ladder.py; "
                "results/reports/cp_q3_positive_null_control_ladder/"
                "method_summary.csv"
            ),
        },
        {
            "Definition group": "Route audit scalar",
            "Quantity": "confidence",
            "Operational definition": (
                "Deterministic route-assurance scalar emitted by each registered "
                "method/router rule and averaged descriptively in route summaries."
            ),
            "Computation or scope": (
                "ContextGate emits 0.95 for strict or negative routes and 0.85 "
                "for abstentions; method-family comparators emit fixed scalars "
                "attached to their registered route rules."
            ),
            "Interpretation boundary": (
                "Confidence is not a calibrated posterior probability and is not "
                "used as the FDR test or as an independent biological claim."
            ),
            "Source artifact or code": (
                "src/cellpack/contextgate.py; src/cellpack/method_comparison.py; "
                "results/reports/cp_q5_contextgate_decisions/"
                "contextgate_decisions.csv"
            ),
        },
        {
            "Definition group": "Aggregate operating point",
            "Quantity": "FCR and sensitivity/specificity thresholds",
            "Operational definition": (
                "Publication-facing policy thresholds: FCR <= 0.05, route "
                "recovery >= 0.95, sensitivity >= 0.65, and specificity >= 0.80."
            ),
            "Computation or scope": (
                "Thresholds are checked at the aggregate ContextGate decision "
                "level and stress-tested against moderate and permissive "
                "operating points."
            ),
            "Interpretation boundary": (
                "These are safety-first claim-release rules, not universal "
                "biological constants; exploratory users may relax them with "
                "explicit false-context exposure."
            ),
            "Source artifact or code": (
                "Supplementary Table S26; src/cellpack/contextgate.py; "
                "src/cellpack/robustness_stress.py"
            ),
        },
        {
            "Definition group": "Registration",
            "Quantity": "registered artifact",
            "Operational definition": (
                "A dataset, method, threshold, schema, command, or result table "
                "materialized in repository manifests and artifact registries "
                "before manuscript claim release."
            ),
            "Computation or scope": (
                "Registry entries link artifact paths, generating commands, "
                "schema expectations, benchmark phases, and validation checks "
                "under version control."
            ),
            "Interpretation boundary": (
                "Registered here means version-controlled benchmark registration; "
                "it is distinct from clinical-trial preregistration or an "
                "external timestamped DOI until release deposition."
            ),
            "Source artifact or code": (
                "data/manifests/contextgate_benchmark_manifest.yaml; "
                "data/manifests/artifact_registry.yaml; "
                "manuscript/tables/manuscript_table_manifest.json"
            ),
        },
    ]
    return pd.DataFrame(rows)


def _replication_tier(row: pd.Series) -> str:
    role = str(row.get("benchmark_role", ""))
    samples = int(row.get("sample_count", 0) or 0)
    donors = int(row.get("donor_count", 0) or 0)
    if role == "usable" and samples <= 1 and donors <= 1:
        return "Single-donor/FOV-only"
    if role == "usable":
        return "Multi-sample/donor"
    if role == "validation_frozen":
        return "Validation frozen"
    return "Rejected/access blocked"


def _graph_boundary_policy(row: pd.Series) -> str:
    role = str(row.get("benchmark_role", ""))
    platform = str(row.get("platform", ""))
    if role != "usable":
        return "Not executed in CP-Q6 graph matrix."
    base = (
        "k=5 Euclidean kNN/control graphs grouped by sample_id+slide_id; "
        "distance bins <=20, <=75, <=150, >150."
    )
    if platform == "CosMx":
        return (
            base + " CosMx loaders encode slide_id from FOV, so edges do not cross "
            "FOV/sample boundaries."
        )
    if platform == "Xenium":
        return (
            base + " Xenium loaders encode slide_id as the section/slide boundary, "
            "so edges do not cross section/sample boundaries."
        )
    return base


def _replication_note(row: pd.Series) -> str:
    role = str(row.get("benchmark_role", ""))
    if role == "validation_frozen":
        return (
            "Not executed; validation-scale cohort reserved for first future "
            "whole-cohort replay after schema conversion."
        )
    if role != "usable":
        return "Rejected before CP-Q6; retained only as failure-taxonomy evidence."
    samples = int(row.get("sample_count", 0) or 0)
    donors = int(row.get("donor_count", 0) or 0)
    if samples <= 1 and donors <= 1:
        return (
            "Only FOV/within-section replication is available; donor-level "
            "confounding cannot be excluded."
        )
    return (
        "Sample/donor identifiers permit stronger replication than FOV-only "
        "rows, although CP-Q6 still reports the registered split-family matrix."
    )


def _split_power_interpretation(row: pd.Series) -> str:
    if int(row.get("Completed jobs", 0) or 0) == 0:
        return (
            "No completed CP-Q6 metric rows for this split; skip metadata, not "
            "statistical power, explains the absence of residual-delta evidence."
        )
    if int(row.get("Insufficient-power rows for split", 0) or 0) > 0:
        return (
            "Power-vs-null unresolved: these taxonomy rows mark non-significant "
            "or under-replicated evidence, but formal MDE needs per-fold cell "
            "counts and residual variance not serialized in local CP-Q6 artifacts."
        )
    return (
        "Completed residual-delta rows are available; no insufficient-power "
        "taxonomy row is mapped to this dataset/split, so the CI-width proxy is "
        "descriptive rather than a power diagnosis."
    )


def _freeze_or_exclusion_reason(row: pd.Series) -> str:
    role = str(row.get("benchmark_role", ""))
    if role == "validation_frozen":
        return (
            "Frozen because file-format conversion, label joins, preprocessing, "
            "and cloud cost were deferred; first future replay candidate."
        )
    if role == "rejected_or_access_blocked":
        return _friendly(row.get("skip_reason", "not_applicable"))
    return "not_applicable"


def _count_summary(frame: pd.DataFrame, column: str) -> str:
    if frame.empty or column not in frame.columns:
        return "none"
    counts = frame[column].fillna("not_recorded").astype(str).value_counts()
    if counts.empty:
        return "none"
    return "; ".join(
        f"{_friendly(index)}={int(value)}" for index, value in counts.items()
    )


def _numeric_range(values: pd.Series) -> str:
    numeric = pd.to_numeric(values, errors="coerce").dropna()
    if numeric.empty:
        return "not serialized"
    lower = int(numeric.min())
    upper = int(numeric.max())
    if lower == upper:
        return str(upper)
    return f"{lower}-{upper}"


def _numeric_max(values: pd.Series) -> float | None:
    numeric = pd.to_numeric(values, errors="coerce").dropna()
    if numeric.empty:
        return None
    return float(numeric.max())


def build_dataset_scope_split_audit() -> pd.DataFrame:
    manifest = _read_manifest("contextgate_benchmark_manifest.yaml")
    cards = pd.DataFrame(manifest["dataset_cards"])
    job_status = _read_csv("cp_q6_benchmark_matrix/job_status.csv")
    job_manifest = _read_csv("cp_q6_benchmark_matrix/job_manifest.csv")
    decisions = _read_csv("cp_q5_contextgate_decisions/contextgate_decisions.csv")

    status_counts = (
        job_status.pivot_table(
            index="dataset_id",
            columns="status",
            values="job_id",
            aggfunc="count",
            fill_value=0,
        )
        .reset_index()
        .rename_axis(None, axis=1)
    )
    for column in ["completed", "skipped", "failed"]:
        if column not in status_counts:
            status_counts[column] = 0
    status_counts["planned"] = (
        status_counts[["completed", "skipped", "failed"]].sum(axis=1).astype(int)
    )

    manifest_counts = job_manifest.groupby("dataset_id").agg(
        task_families=("task_family", "nunique"),
        methods=("method_id", "nunique"),
        controls=("control_id", "nunique"),
        split_families=("split_id", "nunique"),
        seeds=("seed", "nunique"),
        tiers=(
            "benchmark_tier",
            lambda values: ", ".join(
                _tier_label(value) for value in sorted({str(value) for value in values})
            ),
        ),
        planned_split_ids=("split_id", lambda values: _compact_unique(values, limit=5)),
    )
    method_control_pairs = (
        job_manifest[["dataset_id", "method_id", "control_id"]]
        .drop_duplicates()
        .groupby("dataset_id")
        .size()
        .rename("method_control_pairs")
    )
    manifest_counts = manifest_counts.join(method_control_pairs, how="left")
    manifest_counts = manifest_counts.reset_index()

    route_counts = (
        decisions.pivot_table(
            index="dataset_id",
            columns="route_label",
            values="contextgate_decision_id",
            aggfunc="count",
            fill_value=0,
        )
        .reset_index()
        .rename_axis(None, axis=1)
    )
    for route in [
        "expression_only",
        "abstain_uncertain",
        "positive_control_only",
        "context_allowed",
    ]:
        if route not in route_counts:
            route_counts[route] = 0

    out = (
        cards.merge(status_counts, on="dataset_id", how="left")
        .merge(manifest_counts, on="dataset_id", how="left")
        .merge(route_counts, on="dataset_id", how="left")
    )
    numeric_columns = [
        "completed",
        "skipped",
        "failed",
        "planned",
        "task_families",
        "methods",
        "controls",
        "split_families",
        "seeds",
        "method_control_pairs",
        "expression_only",
        "abstain_uncertain",
        "positive_control_only",
        "context_allowed",
    ]
    for column in numeric_columns:
        if column not in out:
            out[column] = 0
        out[column] = out[column].fillna(0).astype(int)
    for column in ["tiers", "planned_split_ids"]:
        out[column] = out[column].fillna("not_executed")

    skip_summaries = {
        dataset_id: _count_summary(group[group["status"] == "skipped"], "skip_reason")
        for dataset_id, group in job_status.groupby("dataset_id")
    }
    out["Skip reason counts"] = out["dataset_id"].map(skip_summaries).fillna("none")
    out["Replication tier"] = out.apply(_replication_tier, axis=1)
    out["Graph boundary policy"] = out.apply(_graph_boundary_policy, axis=1)
    out["Replication limitation"] = out.apply(_replication_note, axis=1)
    out["Freeze/exclusion reason"] = out.apply(_freeze_or_exclusion_reason, axis=1)
    out["Job-count rationale"] = out.apply(
        lambda row: (
            f"{int(row['planned'])} planned CP-Q6 rows from "
            f"{int(row['task_families'])} task families, "
            f"{int(row['method_control_pairs'])} method-control pairs, "
            f"{int(row['split_families'])} split families, "
            f"{int(row['seeds'])} seeds, tiers {row['tiers']}; skips: "
            f"{row['Skip reason counts']}."
            if row["benchmark_role"] == "usable"
            else row["Freeze/exclusion reason"]
        ),
        axis=1,
    )

    role_order = {
        "usable": 0,
        "validation_frozen": 1,
        "rejected_or_access_blocked": 2,
    }
    out["sort_key"] = out["benchmark_role"].map(role_order).fillna(99)
    out = out.sort_values(["sort_key", "dataset_id"])
    return (
        out[
            [
                "dataset_id",
                "benchmark_role",
                "platform",
                "sample_count",
                "donor_count",
                "gene_count",
                "Replication tier",
                "planned",
                "completed",
                "skipped",
                "failed",
                "Job-count rationale",
                "planned_split_ids",
                "Graph boundary policy",
                "expression_only",
                "abstain_uncertain",
                "positive_control_only",
                "context_allowed",
                "Replication limitation",
                "Freeze/exclusion reason",
            ]
        ]
        .rename(
            columns={
                "dataset_id": "Dataset",
                "benchmark_role": "Role",
                "platform": "Platform",
                "sample_count": "Samples",
                "donor_count": "Donors",
                "gene_count": "Genes",
                "planned": "Planned jobs",
                "completed": "Completed jobs",
                "skipped": "Skipped jobs",
                "failed": "Failed jobs",
                "planned_split_ids": "Planned split IDs",
                "expression_only": "Expression-only decisions",
                "abstain_uncertain": "Abstain decisions",
                "positive_control_only": "Positive-control-only decisions",
                "context_allowed": "Context-allowed decisions",
            }
        )
        .assign(
            Dataset=lambda frame: frame["Dataset"].map(_dataset_label),
            Role=lambda frame: frame["Role"].map(
                lambda value: ROLE_LABELS.get(str(value), _friendly(value).title())
            ),
            **{
                "Planned split IDs": lambda frame: frame["Planned split IDs"].map(
                    _friendly
                ),
            },
        )
    )


def build_method_scope_fairness_audit() -> pd.DataFrame:
    metrics = _read_csv("cp_q2_method_comparison/method_metrics.csv")
    predictions = _read_csv("cp_q2_method_comparison/method_predictions.csv")
    utility = _read_csv("cp_r1_context_utility_atlas/run_context_utility.csv")
    manifest = _read_manifest("contextgate_benchmark_manifest.yaml")
    cards = pd.DataFrame(manifest["dataset_cards"])
    included_cards = cards[cards["benchmark_role"] == "usable"]
    min_genes = int(included_cards["gene_count"].min())
    max_genes = int(included_cards["gene_count"].max())
    low_coverage = 64 / max_genes * 100
    high_coverage = 128 / min_genes * 100
    xenium_5k_low = 64 / max_genes * 100
    xenium_5k_high = 128 / max_genes * 100

    low_score = int((utility["context_utility_score"] <= 0.01).sum())
    high_score = int((utility["context_utility_score"] >= 0.65).sum())
    mid_score = int(
        (
            (utility["context_utility_score"] > 0.01)
            & (utility["context_utility_score"] < 0.65)
        ).sum()
    )
    score_distribution = (
        f"CP-R1 score distribution: {low_score} low, {mid_score} "
        f"intermediate, {high_score} high rows."
    )

    metric_rows = []
    for _, row in metrics.iterrows():
        method_id = str(row["method_id"])
        metadata = METHOD_SCOPE_METADATA.get(
            method_id,
            {
                "family": _friendly(row["method_family"]),
                "rule": "Registered CP-Q2 method-family rule.",
                "tuning": "See source artifact.",
                "scope": "See source artifact.",
                "source": "cp_q2_method_comparison",
            },
        )
        rule = metadata["rule"]
        scope = metadata["scope"]
        if method_id == "spatial_statistics_heuristic":
            spatial = predictions[predictions["method_id"] == method_id]
            context_use = spatial[_as_bool(spatial["uses_context"])]
            if not context_use.empty:
                evidence = _compact_unique(context_use["evidence_class"], limit=4)
                rule = f"{rule} {score_distribution} The only context-use row was {evidence}."
        if method_id == "cellpack_packed_context_tiny":
            scope = (
                f"64-128 measured genes cover {low_coverage:.1f}%-"
                f"{high_coverage:.1f}% of included panels and {xenium_5k_low:.1f}%-"
                f"{xenium_5k_high:.1f}% of the 9,475-gene panel; "
                "high-plex datasets are input-starved."
            )
        metric_rows.append(
            {
                "Audit group": "Registered CP-Q2 method family",
                "Section 3.4 family or tool": metadata["family"],
                "Figure/display label": _method_label(method_id),
                "Method id or candidate": method_id,
                "Included in CP-Q2": "Yes",
                "Rows": int(row["row_count"]),
                "Mean utility": float(row["mean_utility"]),
                "Mean regret": float(row["mean_regret"]),
                "No-harm rate": float(row["no_harm_rate"]),
                "False-context rate": float(row["false_positive_context_rate"]),
                "Abstention rate": float(row["abstention_rate"]),
                "Context-use rate": float(row["context_use_rate"]),
                "Route/proxy rule": rule,
                "Tuning/access note": metadata["tuning"],
                "Scope boundary": scope,
                "Source artifact or code": metadata["source"],
            }
        )

    ledger_path = (
        PROJECT_ROOT
        / "manuscript"
        / "reviewer_hardening"
        / "sota_feasibility_ledger.csv"
    )
    future = pd.read_csv(ledger_path)
    selected = {
        "BANKSY",
        "COMMOT",
        "GraphST",
        "Niche-DE / niche-LR",
        "Nicheformer",
        "Novae",
    }
    future_rows = []
    for _, row in future[future["candidate"].isin(selected)].iterrows():
        future_rows.append(
            {
                "Audit group": "Named tool scoped to future adapter",
                "Section 3.4 family or tool": str(row["category"]),
                "Figure/display label": str(row["candidate"]),
                "Method id or candidate": str(row["candidate"]),
                "Included in CP-Q2": "No",
                "Rows": pd.NA,
                "Mean utility": pd.NA,
                "Mean regret": pd.NA,
                "No-harm rate": pd.NA,
                "False-context rate": pd.NA,
                "Abstention rate": pd.NA,
                "Context-use rate": pd.NA,
                "Route/proxy rule": "No CP-Q2 route row; future adapter must emit CP-Q prediction tables.",
                "Tuning/access note": _friendly(row["release_decision"]),
                "Scope boundary": str(row["primary_blocker"]),
                "Source artifact or code": (
                    "manuscript/reviewer_hardening/sota_feasibility_ledger.csv"
                ),
            }
        )
    for row in FUTURE_METHOD_SCOPE_ROWS:
        future_rows.append(
            {
                "Audit group": "Named tool scoped to future adapter",
                "Section 3.4 family or tool": row["category"],
                "Figure/display label": row["candidate"],
                "Method id or candidate": row["candidate"],
                "Included in CP-Q2": "No",
                "Rows": pd.NA,
                "Mean utility": pd.NA,
                "Mean regret": pd.NA,
                "No-harm rate": pd.NA,
                "False-context rate": pd.NA,
                "Abstention rate": pd.NA,
                "Context-use rate": pd.NA,
                "Route/proxy rule": "No CP-Q2 route row; future adapter must emit CP-Q prediction tables.",
                "Tuning/access note": _friendly(row["release_decision"]),
                "Scope boundary": row["primary_blocker"],
                "Source artifact or code": (
                    "manuscript/reviewer_hardening/"
                    "cp_q8_8_full_paper_wizard_issue_ledger.md"
                ),
            }
        )

    out = pd.DataFrame(metric_rows + future_rows)
    order = {
        "Registered CP-Q2 method family": 0,
        "Named tool scoped to future adapter": 1,
    }
    out["_order"] = out["Audit group"].map(order)
    out = out.sort_values(["_order", "Figure/display label"]).drop(columns="_order")
    numeric_columns = [
        "Rows",
        "Mean utility",
        "Mean regret",
        "No-harm rate",
        "False-context rate",
        "Abstention rate",
        "Context-use rate",
    ]
    for column in numeric_columns:
        values = pd.to_numeric(out[column], errors="coerce")
        if column == "Rows":
            out[column] = values.map(lambda value: "" if pd.isna(value) else int(value))
        else:
            out[column] = values.map(
                lambda value: "" if pd.isna(value) else round(float(value), 4)
            )
    return out


def build_route_aggregation_trace() -> pd.DataFrame:
    decisions = _read_csv("cp_q5_contextgate_decisions/contextgate_decisions.csv")
    jobs = _read_csv("cp_q6_benchmark_matrix/job_status.csv")
    metrics = _read_csv("cp_q6_benchmark_matrix/benchmark_metric_matrix.csv")

    source_labels = {
        "failure_taxonomy": "Rejected/access-blocked dataset-card rows",
        "positive_control_ladder": "CP-Q3 positive/null-control ladder",
        "run_context_utility": "CP-R1 context-utility route rows",
    }
    unit_labels = {
        "failure_taxonomy": "dataset-card rejection row",
        "positive_control_ladder": "synthetic ladder row by dataset/control/method",
        "run_context_utility": "route-level context-utility row",
    }
    aggregation_rules = {
        "failure_taxonomy": (
            "Each rejected/access-blocked dataset-card row becomes one abstain "
            "decision with an access/schema reason."
        ),
        "positive_control_ladder": (
            "Each registered positive/null ladder row keeps its expected route; "
            "seed/split aggregation is already resolved in CP-Q3 artifacts."
        ),
        "run_context_utility": (
            "Each CP-R1 context-utility row becomes one route decision; the "
            "score/gate evidence is not majority-voted from CP-Q6 jobs."
        ),
    }
    relationship = {
        "failure_taxonomy": "Not part of the 2,324 executed jobs; retained as evidence-denominator ledger rows.",
        "positive_control_ladder": "Derived from CP-Q3 synthetic-control artifacts and cross-checked by CP-Q6 metrics.",
        "run_context_utility": "Derived from CP-R1 route artifacts and cross-linked to CP-Q6 metric tables.",
    }

    rows: list[dict] = []
    for source_table, group in decisions.groupby("source_table", dropna=False):
        route_counts = group["route_label"].value_counts()
        rows.append(
            {
                "Aggregation source": source_labels.get(
                    str(source_table),
                    _friendly(source_table),
                ),
                "Source table": source_table,
                "Source row unit": unit_labels.get(str(source_table), "registered row"),
                "Input rows": len(group),
                "Route decisions": len(group),
                "Datasets or dataset-card rows": group["dataset_id"].nunique(),
                "Task families": group["task_id"].nunique(),
                "Expression-only decisions": int(
                    route_counts.get("expression_only", 0)
                ),
                "Abstain decisions": int(route_counts.get("abstain_uncertain", 0)),
                "Positive-control-only decisions": int(
                    route_counts.get("positive_control_only", 0)
                ),
                "Context-allowed decisions": int(
                    route_counts.get("context_allowed", 0)
                ),
                "Mean confidence": float(group["confidence"].mean()),
                "Aggregation rule": aggregation_rules.get(
                    str(source_table),
                    "One registered source row becomes one ContextGate decision.",
                ),
                "Relationship to job matrix": relationship.get(
                    str(source_table),
                    "Cross-linked to registered artifacts.",
                ),
            }
        )

    status_counts = jobs["status"].value_counts()
    rows.append(
        {
            "Aggregation source": "CP-Q6 benchmark execution matrix",
            "Source table": "cp_q6_benchmark_matrix",
            "Source row unit": "planned benchmark job",
            "Input rows": int(len(jobs)),
            "Route decisions": 0,
            "Datasets or dataset-card rows": int(jobs["dataset_id"].nunique()),
            "Task families": int(jobs["task_id"].nunique()),
            "Expression-only decisions": 0,
            "Abstain decisions": 0,
            "Positive-control-only decisions": 0,
            "Context-allowed decisions": 0,
            "Mean confidence": "",
            "Aggregation rule": (
                "Execution jobs are not collapsed directly into the 100 route "
                "decisions; they supply metric, skip, and robustness evidence."
            ),
            "Relationship to job matrix": (
                f"{int(status_counts.get('completed', 0))} completed jobs, "
                f"{int(status_counts.get('skipped', 0))} skipped jobs, and "
                f"{len(metrics)} metric rows."
            ),
        }
    )

    out = pd.DataFrame(rows)
    out["Mean confidence"] = out["Mean confidence"].map(
        lambda value: "" if value == "" or pd.isna(value) else round(float(value), 4)
    )
    return out.sort_values(
        ["Route decisions", "Aggregation source"], ascending=[False, True]
    )


def build_dataset_task_performance_disaggregation() -> pd.DataFrame:
    manifest = _read_manifest("contextgate_benchmark_manifest.yaml")
    cards = pd.DataFrame(manifest["dataset_cards"])
    cards = cards[
        [
            "dataset_id",
            "benchmark_role",
            "platform",
            "sample_count",
            "donor_count",
            "gene_count",
        ]
    ]
    metrics = _read_csv("cp_q6_benchmark_matrix/benchmark_metric_matrix.csv")
    full = metrics[metrics["benchmark_tier"] == "q1"].copy()
    jobs = _read_csv("cp_q6_benchmark_matrix/job_status.csv")
    q1_jobs = jobs[jobs["benchmark_tier"] == "q1"].copy()
    decisions = _read_csv("cp_q5_contextgate_decisions/contextgate_decisions.csv")
    utility = _read_csv("cp_r1_context_utility_atlas/run_context_utility.csv")

    route_counts = (
        decisions.pivot_table(
            index=["dataset_id", "task_id"],
            columns="route_label",
            values="contextgate_decision_id",
            aggfunc="count",
            fill_value=0,
        )
        .reset_index()
        .rename_axis(None, axis=1)
    )
    for route in [
        "expression_only",
        "abstain_uncertain",
        "positive_control_only",
        "context_allowed",
    ]:
        if route not in route_counts:
            route_counts[route] = 0
    source_summary = (
        decisions.groupby(["dataset_id", "task_id"], dropna=False)
        .agg(
            decision_source_tables=("source_table", _compact_unique),
            route_decisions=("contextgate_decision_id", "count"),
        )
        .reset_index()
    )
    route_summary = route_counts.merge(
        source_summary,
        on=["dataset_id", "task_id"],
        how="left",
    )

    job_status = (
        q1_jobs.pivot_table(
            index=["dataset_id", "task_id"],
            columns="status",
            values="job_id",
            aggfunc="count",
            fill_value=0,
        )
        .reset_index()
        .rename_axis(None, axis=1)
    )
    for status in ["completed", "skipped", "failed"]:
        if status not in job_status:
            job_status[status] = 0

    utility_summary = (
        utility.groupby("source_dataset", dropna=False)
        .agg(
            context_utility_rows=("context_utility_id", "count"),
            mean_context_utility_score=("context_utility_score", "mean"),
            max_context_utility_score=("context_utility_score", "max"),
            high_score_rows=(
                "context_utility_score",
                lambda values: int(
                    (pd.to_numeric(values, errors="coerce") >= 0.65).sum()
                ),
            ),
            evidence_classes=("evidence_class", _compact_unique),
        )
        .reset_index()
        .rename(columns={"source_dataset": "dataset_id"})
    )

    rows: list[dict] = []
    job_groups = q1_jobs[["dataset_id", "task_id"]].drop_duplicates()
    for _, job_group in job_groups.sort_values(["task_id", "dataset_id"]).iterrows():
        dataset_id = job_group["dataset_id"]
        task_id = job_group["task_id"]
        group = full[(full["dataset_id"] == dataset_id) & (full["task_id"] == task_id)]
        job_source = q1_jobs[
            (q1_jobs["dataset_id"] == dataset_id) & (q1_jobs["task_id"] == task_id)
        ]
        cards_row = cards[cards["dataset_id"] == dataset_id]
        card = cards_row.iloc[0] if not cards_row.empty else pd.Series(dtype=object)
        job_row = job_status[
            (job_status["dataset_id"] == dataset_id)
            & (job_status["task_id"] == task_id)
        ]
        route_row = route_summary[
            (route_summary["dataset_id"] == dataset_id)
            & (route_summary["task_id"] == task_id)
        ]
        utility_row = utility_summary[utility_summary["dataset_id"] == dataset_id]
        genes = int(card.get("gene_count", 0) or 0)
        rows.append(
            {
                "Dataset": _dataset_label(dataset_id),
                "Task": _friendly(task_id),
                "Platform": card.get("platform", ""),
                "Dataset role": ROLE_LABELS.get(
                    str(card.get("benchmark_role", "")),
                    _friendly(card.get("benchmark_role", "")),
                ),
                "Samples": int(card.get("sample_count", 0) or 0),
                "Donors": int(card.get("donor_count", 0) or 0),
                "Panel genes": genes,
                "Panel-depth group": _panel_depth_group(genes),
                "Completed q1 jobs": int(job_row["completed"].iloc[0])
                if not job_row.empty
                else 0,
                "Skipped q1 jobs": int(job_row["skipped"].iloc[0])
                if not job_row.empty
                else 0,
                "Full-tier metric rows": len(group),
                "Methods": job_source["method_id"].nunique(),
                "Controls": job_source["control_id"].nunique(),
                "Splits": job_source["split_id"].nunique(),
                "Seeds": job_source["seed"].nunique(),
                "Mean prediction error": _metric_mean(group, "prediction_error"),
                "Mean residual delta": _metric_mean(group, "residual_delta"),
                "Mean regret": _metric_mean(group, "regret_against_oracle"),
                "Mean FCR": _metric_mean(group, "false_positive_context_rate"),
                "Mean no-harm": _metric_mean(group, "no_harm_rate"),
                "Mean abstention": _metric_mean(group, "abstention_rate"),
                "Route decisions": int(route_row["route_decisions"].iloc[0])
                if not route_row.empty
                else 0,
                "Expression-only decisions": int(route_row["expression_only"].iloc[0])
                if not route_row.empty
                else 0,
                "Abstain decisions": int(route_row["abstain_uncertain"].iloc[0])
                if not route_row.empty
                else 0,
                "Positive-control-only decisions": int(
                    route_row["positive_control_only"].iloc[0]
                )
                if not route_row.empty
                else 0,
                "Context-allowed decisions": int(route_row["context_allowed"].iloc[0])
                if not route_row.empty
                else 0,
                "Decision source tables": (
                    str(route_row["decision_source_tables"].iloc[0])
                    if not route_row.empty
                    else ""
                ),
                "Context-utility rows": (
                    int(utility_row["context_utility_rows"].iloc[0])
                    if not utility_row.empty
                    else 0
                ),
                "Mean context-utility score": (
                    float(utility_row["mean_context_utility_score"].iloc[0])
                    if not utility_row.empty
                    else pd.NA
                ),
                "Max context-utility score": (
                    float(utility_row["max_context_utility_score"].iloc[0])
                    if not utility_row.empty
                    else pd.NA
                ),
                "High-score context-utility rows": (
                    int(utility_row["high_score_rows"].iloc[0])
                    if not utility_row.empty
                    else 0
                ),
                "Context evidence classes": (
                    str(utility_row["evidence_classes"].iloc[0])
                    if not utility_row.empty
                    else ""
                ),
            }
        )
    return pd.DataFrame(rows).sort_values(["Task", "Dataset"])


def build_failure_taxonomy_denominator_audit() -> pd.DataFrame:
    taxonomy = _read_csv("cp_q4_failure_taxonomy/failure_taxonomy.csv")
    summary = _read_csv("cp_q4_failure_taxonomy/failure_class_summary.csv")
    total_rows = len(taxonomy)
    per_benchmark_row = (
        taxonomy.groupby("benchmark_row_id", dropna=False)["failure_class"]
        .nunique()
        .reset_index(name="class_count")
    )
    cooccurring_ids = set(
        per_benchmark_row.loc[
            per_benchmark_row["class_count"] > 1,
            "benchmark_row_id",
        ]
    )

    rows = [
        {
            "Failure class": "All failure taxonomy rows",
            "Failure taxonomy rows": total_rows,
            "Percent of taxonomy rows": 1.0,
            "Unique benchmark row IDs": taxonomy["benchmark_row_id"].nunique(),
            "Benchmark row IDs with another class": len(cooccurring_ids),
            "Datasets": taxonomy["dataset_id"].nunique(),
            "Tasks": taxonomy["task_id"].nunique(),
            "Methods": taxonomy["method_id"].nunique(),
            "Source tables": _compact_unique(taxonomy["source_table"], limit=6),
            "Route labels": _compact_unique(taxonomy["route_label"], limit=6),
            "Claim downgrade": "Multiple",
            "Denominator note": (
                "Unit is failure_taxonomy_id row; classes can co-occur for a "
                "benchmark_row_id and are not mutually exclusive."
            ),
        }
    ]
    for _, row in summary.iterrows():
        failure_class = row["failure_class"]
        class_rows = taxonomy[taxonomy["failure_class"] == failure_class]
        denominator_note = (
            "Non-significant/power-unresolved label: q_i or replication "
            "failure alone does not distinguish low power from a true null; "
            "Supplementary Table S36 reports split coverage and CI-width "
            "proxies."
            if failure_class == "insufficient_power"
            else "Counted as failure_taxonomy_id rows; see total row for co-occurrence rule."
        )
        rows.append(
            {
                "Failure class": _friendly(failure_class),
                "Failure taxonomy rows": int(row["failure_count"]),
                "Percent of taxonomy rows": int(row["failure_count"]) / total_rows,
                "Unique benchmark row IDs": class_rows["benchmark_row_id"].nunique(),
                "Benchmark row IDs with another class": int(
                    class_rows.loc[
                        class_rows["benchmark_row_id"].isin(cooccurring_ids),
                        "benchmark_row_id",
                    ].nunique()
                ),
                "Datasets": int(row["dataset_count"]),
                "Tasks": int(row["task_count"]),
                "Methods": int(row["method_count"]),
                "Source tables": _compact_unique(class_rows["source_table"], limit=6),
                "Route labels": _compact_unique(class_rows["route_label"], limit=6),
                "Claim downgrade": _friendly(row["claim_downgrade"]),
                "Denominator note": denominator_note,
            }
        )
    return pd.DataFrame(rows)


def build_panel_depth_observability_audit() -> pd.DataFrame:
    manifest = _read_manifest("contextgate_benchmark_manifest.yaml")
    cards = pd.DataFrame(manifest["dataset_cards"])
    jobs = _read_csv("cp_q6_benchmark_matrix/job_status.csv")
    utility = _read_csv("cp_r1_context_utility_atlas/run_context_utility.csv")
    taxonomy = _read_csv("cp_q4_failure_taxonomy/failure_taxonomy.csv")

    card_cols = [
        "dataset_id",
        "benchmark_role",
        "platform",
        "sample_count",
        "donor_count",
        "gene_count",
    ]
    cards = cards[card_cols].copy()
    cards["Panel-depth group"] = cards["gene_count"].map(_panel_depth_group)

    job_counts = (
        jobs.pivot_table(
            index="dataset_id",
            columns="status",
            values="job_id",
            aggfunc="count",
            fill_value=0,
        )
        .reset_index()
        .rename_axis(None, axis=1)
    )
    for status in ["completed", "skipped", "failed"]:
        if status not in job_counts:
            job_counts[status] = 0

    utility_cards = utility.merge(
        cards[["dataset_id", "Panel-depth group"]],
        left_on="source_dataset",
        right_on="dataset_id",
        how="left",
    )
    taxonomy_cards = taxonomy.merge(
        cards[["dataset_id", "Panel-depth group"]],
        on="dataset_id",
        how="left",
    )
    cards = cards.merge(job_counts, on="dataset_id", how="left")
    for status in ["completed", "skipped", "failed"]:
        cards[status] = cards[status].fillna(0).astype(int)

    rows: list[dict] = []
    for group_name, group_cards in cards.groupby("Panel-depth group", dropna=False):
        dataset_ids = set(group_cards["dataset_id"])
        utility_group = utility_cards[utility_cards["source_dataset"].isin(dataset_ids)]
        taxonomy_group = taxonomy_cards[taxonomy_cards["dataset_id"].isin(dataset_ids)]
        failure_counts = taxonomy_group["failure_class"].value_counts()
        rows.append(
            {
                "Panel-depth group": group_name,
                "Datasets": _compact_unique(
                    group_cards["dataset_id"].map(_dataset_label), limit=8
                ),
                "Dataset count": len(group_cards),
                "Included dataset count": int(
                    (group_cards["benchmark_role"] == "usable").sum()
                ),
                "Gene-count range": (
                    f"{int(group_cards['gene_count'].min())}-"
                    f"{int(group_cards['gene_count'].max())}"
                ),
                "Completed jobs": int(group_cards["completed"].sum()),
                "Skipped jobs": int(group_cards["skipped"].sum()),
                "Context-utility rows": int(len(utility_group)),
                "Mean context-utility score": (
                    float(utility_group["context_utility_score"].mean())
                    if not utility_group.empty
                    else ""
                ),
                "Max context-utility score": (
                    float(utility_group["context_utility_score"].max())
                    if not utility_group.empty
                    else ""
                ),
                "High-score context-utility rows": int(
                    (utility_group["context_utility_score"] >= 0.65).sum()
                ),
                "Failure taxonomy rows": int(len(taxonomy_group)),
                "Panel-coverage failure rows": int(
                    failure_counts.get("panel_lacks_downstream_genes", 0)
                ),
                "Insufficient-power rows": int(
                    failure_counts.get("insufficient_power", 0)
                ),
                "FOV/sample-artifact rows": int(
                    failure_counts.get("fov_or_sample_artifact", 0)
                ),
                "Interpretation": (
                    "Panel-depth stratum; row counts are descriptive and do not "
                    "establish a causal panel-depth effect."
                ),
            }
        )
    out = pd.DataFrame(rows)
    for column in ["Mean context-utility score", "Max context-utility score"]:
        out[column] = out[column].map(
            lambda value: ""
            if value == "" or pd.isna(value)
            else round(float(value), 4)
        )
    return out.sort_values(
        ["Included dataset count", "Context-utility rows"],
        ascending=[False, False],
    )


def build_power_mde_split_counts() -> pd.DataFrame:
    manifest = _read_manifest("contextgate_benchmark_manifest.yaml")
    cards = pd.DataFrame(manifest["dataset_cards"])
    cards = cards[cards["benchmark_role"] == "usable"][
        [
            "dataset_id",
            "platform",
            "sample_count",
            "donor_count",
            "cell_or_unit_count",
            "gene_count",
            "benchmark_role",
        ]
    ].copy()
    cards["Replication tier"] = cards.apply(_replication_tier, axis=1)

    jobs = _read_csv("cp_q6_benchmark_matrix/job_status.csv")
    metrics = _read_csv("cp_q6_benchmark_matrix/benchmark_metric_matrix.csv")
    taxonomy = _read_csv("cp_q4_failure_taxonomy/failure_taxonomy.csv")

    job_counts = (
        jobs.pivot_table(
            index=["dataset_id", "split_id"],
            columns="status",
            values="job_id",
            aggfunc="count",
            fill_value=0,
        )
        .reset_index()
        .rename_axis(None, axis=1)
    )
    for status in ["completed", "skipped", "failed"]:
        if status not in job_counts:
            job_counts[status] = 0
    job_counts["planned"] = (
        job_counts[["completed", "skipped", "failed"]].sum(axis=1).astype(int)
    )

    residual = metrics[metrics["metric_family"] == "residual_delta"].copy()
    residual["ci_half_width_proxy"] = (
        residual["confidence_high"] - residual["confidence_low"]
    ).abs() / 2
    residual_summary = (
        residual.groupby(["dataset_id", "split_id"], dropna=False)
        .agg(
            residual_delta_rows=("metric_value", "size"),
            median_residual_delta=("metric_value", "median"),
            median_q_value=("q_value", "median"),
            median_ci_half_width_proxy=("ci_half_width_proxy", "median"),
        )
        .reset_index()
    )

    insufficient = taxonomy[taxonomy["failure_class"] == "insufficient_power"].copy()
    insufficient_by_split = (
        insufficient.groupby(["dataset_id", "split_id"], dropna=False)
        .size()
        .reset_index(name="insufficient_power_rows_for_split")
    )
    insufficient_total = (
        insufficient.groupby("dataset_id", dropna=False)
        .size()
        .reset_index(name="insufficient_power_rows_dataset_total")
    )

    out = (
        job_counts.merge(cards, on="dataset_id", how="left")
        .merge(residual_summary, on=["dataset_id", "split_id"], how="left")
        .merge(insufficient_by_split, on=["dataset_id", "split_id"], how="left")
        .merge(insufficient_total, on="dataset_id", how="left")
    )
    numeric_columns = [
        "planned",
        "completed",
        "skipped",
        "failed",
        "residual_delta_rows",
        "insufficient_power_rows_for_split",
        "insufficient_power_rows_dataset_total",
    ]
    for column in numeric_columns:
        if column not in out:
            out[column] = 0
        out[column] = out[column].fillna(0).astype(int)
    for column in [
        "median_residual_delta",
        "median_q_value",
        "median_ci_half_width_proxy",
    ]:
        out[column] = out[column].map(
            lambda value: "" if pd.isna(value) else round(float(value), 4)
        )

    out["Within-split cell-count artifact"] = (
        "not serialized in local CP-Q6 artifacts; registered dataset-level "
        "cell/unit count is shown as the available denominator proxy"
    )
    out["MDE status"] = (
        "formal MDE unavailable without per-fold train/test cell counts and "
        "residual variance; median CI half-width is descriptive only"
    )
    out = out.rename(
        columns={
            "dataset_id": "Dataset",
            "split_id": "Split ID",
            "platform": "Platform",
            "sample_count": "Samples",
            "donor_count": "Donors",
            "cell_or_unit_count": "Registered cells/units",
            "gene_count": "Genes",
            "planned": "Planned jobs",
            "completed": "Completed jobs",
            "skipped": "Skipped jobs",
            "failed": "Failed jobs",
            "residual_delta_rows": "Residual-delta metric rows",
            "median_residual_delta": "Median residual delta",
            "median_q_value": "Median q value",
            "median_ci_half_width_proxy": "Median CI half-width proxy",
            "insufficient_power_rows_for_split": "Insufficient-power rows for split",
            "insufficient_power_rows_dataset_total": (
                "Insufficient-power rows for dataset"
            ),
        }
    )
    out["Interpretation"] = out.apply(_split_power_interpretation, axis=1)
    out["Dataset"] = out["Dataset"].map(_dataset_label)
    out["Split ID"] = out["Split ID"].map(_friendly)
    sort_order = {
        "unit hash split": 0,
        "fov holdout": 1,
        "sample or section holdout": 2,
    }
    out["sort_key"] = out["Split ID"].map(sort_order).fillna(99)
    return out.sort_values(["Dataset", "sort_key"])[
        [
            "Dataset",
            "Platform",
            "Split ID",
            "Replication tier",
            "Samples",
            "Donors",
            "Registered cells/units",
            "Genes",
            "Planned jobs",
            "Completed jobs",
            "Skipped jobs",
            "Failed jobs",
            "Residual-delta metric rows",
            "Median residual delta",
            "Median q value",
            "Median CI half-width proxy",
            "Insufficient-power rows for split",
            "Insufficient-power rows for dataset",
            "Within-split cell-count artifact",
            "MDE status",
            "Interpretation",
        ]
    ]


def build_method_scope_lr_coverage() -> pd.DataFrame:
    lr_pairs = pd.read_csv(MANIFEST_ROOT / "ligand_receptor_pairs.tsv", sep="\t")
    starter = lr_pairs[lr_pairs["pair_source"] == "common_lr_starter"].copy()
    manifest = _read_manifest("contextgate_benchmark_manifest.yaml")
    cards = pd.DataFrame(manifest["dataset_cards"])
    cards = cards[cards["benchmark_role"] == "usable"].copy()
    utility = _read_csv("cp_r1_context_utility_atlas/run_context_utility.csv")
    registry = pd.DataFrame(_read_manifest("artifact_registry.yaml")["artifacts"])
    registry_pair = registry[
        registry.get("available_pair_count", pd.Series(dtype=object)).notna()
    ].copy()

    rows: list[dict] = [
        {
            "Audit group": "LR starter list",
            "Subject": "common_lr_starter",
            "Registered detail": (
                "Frozen literature-curated starter list used by the LR/pathway "
                "heuristic."
            ),
            "Local artifact value": (
                f"{len(starter)} pairs; pathways: "
                f"{_compact_unique(starter['pathway'], limit=12)}"
            ),
            "Interpretation": (
                "Coverage failures can arise from this starter-list scope, the "
                "assay panel, or downstream module availability; they are not "
                "evidence that communication biology is absent."
            ),
            "Source artifact": "data/manifests/ligand_receptor_pairs.tsv",
        }
    ]

    for _, card in cards.sort_values("dataset_id").iterrows():
        dataset_id = card["dataset_id"]
        utility_rows = utility[utility["source_dataset"] == dataset_id]
        registry_rows = registry_pair[registry_pair["source_dataset"] == dataset_id]
        utility_pair_range = _numeric_range(utility_rows["available_pair_count"])
        utility_module_range = _numeric_range(
            utility_rows["available_module_target_count"]
        )
        registry_pair_range = _numeric_range(registry_rows["available_pair_count"])
        cp_r1_pair_max = _numeric_max(utility_rows["available_pair_count"])
        cp_r1_module_max = _numeric_max(utility_rows["available_module_target_count"])
        registry_pair_max = _numeric_max(registry_rows["available_pair_count"])
        cp_r1_threshold_passes = (
            (cp_r1_pair_max is not None and cp_r1_pair_max >= 4)
            or (cp_r1_module_max is not None and cp_r1_module_max >= 4)
        )
        registry_only_pair_support = (
            registry_pair_max is not None
            and registry_pair_max >= 4
            and cp_r1_pair_max is None
            and cp_r1_module_max is None
        )
        if cp_r1_threshold_passes:
            interpretation = (
                "The row-level CP-R1 coverage threshold can pass in at least "
                "one local route row; routing still depends on the shared "
                "context-utility score and downstream gate evidence."
            )
        elif registry_only_pair_support:
            interpretation = (
                "Registry pair-availability artifacts show measured pairs, but "
                "the CP-R1 route rows did not serialize the count; this is "
                "coverage evidence, not route permission by itself."
            )
        else:
            interpretation = (
                "Local CP-R1 route rows do not meet the LR/module coverage "
                "threshold, so LR/pathway use is blocked or abstained before "
                "any biological communication claim is released."
            )
        rows.append(
            {
                "Audit group": "LR coverage by dataset",
                "Subject": _dataset_label(dataset_id),
                "Registered detail": (
                    "LR route proxy evaluates row-level available_pair_count >= 4 "
                    "or available_module_target_count >= 4."
                ),
                "Local artifact value": (
                    f"starter pairs={len(starter)}; CP-R1 available pairs="
                    f"{utility_pair_range}; CP-R1 module targets="
                    f"{utility_module_range}; registry available pairs="
                    f"{registry_pair_range}; genes={int(card['gene_count'])}"
                ),
                "Interpretation": interpretation,
                "Source artifact": (
                    "results/reports/cp_r1_context_utility_atlas/"
                    "run_context_utility.csv; data/manifests/artifact_registry.yaml"
                ),
            }
        )

    rows.extend(
        [
            {
                "Audit group": "Shared-score comparator boundary",
                "Subject": "Spatial stats / GraphSAGE style / ContextGate",
                "Registered detail": (
                    "These comparators consume CP-R1 context_utility_score or "
                    "the same residual-utility evidence and differ primarily "
                    "by threshold and claim-release policy."
                ),
                "Local artifact value": (
                    "S29/S34 report CP-Q2 rows; S33A/S38 report threshold "
                    "stress and policy directionality."
                ),
                "Interpretation": (
                    "Their agreement is a threshold-policy sensitivity result, "
                    "not independent algorithmic consensus from unrelated "
                    "model classes."
                ),
                "Source artifact": (
                    "src/cellpack/method_comparison.py; "
                    "manuscript/tables/supp_table_s29_method_scope_fairness_audit.csv"
                ),
            },
            {
                "Audit group": "CellPack input ceiling",
                "Subject": "CellPack tiny",
                "Registered detail": (
                    "Smoke-scale packed-context transformer uses 64-128 genes "
                    "per sequence."
                ),
                "Local artifact value": (
                    "64-128 genes cover 0.7%-23.6% of included panels and "
                    "0.7%-1.4% of the 9,475-gene Xenium breast panel."
                ),
                "Interpretation": (
                    "CellPack is input-constrained; the universal real-data "
                    "gate-1 failure is not presented as a CellPack capacity "
                    "ceiling."
                ),
                "Source artifact": (
                    "manuscript/tables/supp_table_s29_method_scope_fairness_audit.csv"
                ),
            },
            {
                "Audit group": "SOTA exclusion scope",
                "Subject": "BANKSY, COMMOT, SpatialDM, SpaTalk, NicheCompass, CellNeighborEX, GraphST, STAGATE, SpaGCN, Nicheformer, Novae",
                "Registered detail": (
                    "No named high-capacity or domain-specialized tool emits "
                    "registered CP-Q route rows in the current release."
                ),
                "Local artifact value": (
                    "S29 lists all named tools as future adapters requiring "
                    "CP-Q prediction rows and matched wrong-context denominators."
                ),
                "Interpretation": (
                    "The 0 context_allowed count is scoped to registered "
                    "lightweight comparators and cannot be quoted as evidence "
                    "that these named tools fail."
                ),
                "Source artifact": (
                    "manuscript/tables/supp_table_s29_method_scope_fairness_audit.csv; "
                    "manuscript/reviewer_hardening/sota_feasibility_ledger.csv"
                ),
            },
            {
                "Audit group": "Panel-depth confounding",
                "Subject": "S32 panel-depth strata",
                "Registered detail": (
                    "Panel-depth summaries are descriptive strata, not a causal "
                    "panel-size experiment."
                ),
                "Local artifact value": (
                    "The <1,100-gene and >=5,000-gene strata differ in cancer "
                    "context, donor/sample structure, FOV constraints, and "
                    "target definitions."
                ),
                "Interpretation": (
                    "Panel observability remains one candidate explanation "
                    "among power, FOV/sample artifacts, replication limits, and "
                    "target-definition effects."
                ),
                "Source artifact": (
                    "manuscript/tables/supp_table_s32_panel_depth_observability_audit.csv"
                ),
            },
        ]
    )
    return pd.DataFrame(rows)


def _validate_outputs(claim_audit: pd.DataFrame, table_manifest: dict) -> dict:
    q5_summary = _read_json(
        "cp_q5_contextgate_decisions/contextgate_decision_summary.json"
    )
    q6_summary = _read_json("cp_q6_benchmark_matrix/benchmark_matrix_summary.json")
    q7_summary = _read_json("cp_q7_robustness_stress/robustness_stress_summary.json")
    missing_sources = []
    for source in claim_audit["Source artifact"]:
        path = PROJECT_ROOT / str(source)
        if not path.exists():
            missing_sources.append(str(source))

    strong_claim = claim_audit[
        claim_audit["Claim ID"] == "strong_biological_context_claim"
    ]
    strong_claim_downgraded = (
        not strong_claim.empty
        and strong_claim.iloc[0]["Publication status"] == "Downgraded"
    )

    validations = {
        "all_claim_sources_exist": len(missing_sources) == 0,
        "missing_claim_sources": missing_sources,
        "contextgate_gate_passed": bool(q5_summary["contextgate_gate_passed"]),
        "contextgate_no_harm_gate_passed": bool(q5_summary["no_harm_gate_passed"]),
        "benchmark_matrix_gate_passed": bool(q6_summary["modal_matrix_gate_passed"]),
        "benchmark_failed_jobs": int(q6_summary["failed_jobs"]),
        "robustness_gate_passed": bool(q7_summary["robustness_gate_passed"]),
        "failed_stress_rows_without_downgrade": int(
            q7_summary["failed_without_downgrade_count"]
        ),
        "strong_biological_context_claim_downgraded": strong_claim_downgraded,
        "generated_table_count": len(table_manifest),
    }
    expanded_stems = [
        "supp_table_s10_cp_q2_dataset_task_utility",
        "supp_table_s11_q6_dataset_task_method_metrics",
        "supp_table_s12_q6_method_task_safety",
        "supp_table_s13_contextgate_routes_by_dataset_task",
        "supp_table_s14_q6_skip_infeasibility",
        "supp_table_s15_claim_downgrade_distribution",
        "supp_table_s16_positive_null_signal_strength",
        "supp_table_s17_q6_regret_distribution",
    ]
    calibration_stems = [
        "supp_table_s18_threshold_calibration_summary",
        "supp_table_s19_detectability_min_effect",
        "supp_table_s20_real_vs_detectability_audit",
    ]
    audit_stems = [
        "supp_table_s21_leakage_confounding_examples",
        "supp_table_s22_downgrade_examples",
        "supp_table_s23_residualization_audit",
    ]
    stratified_stems = [
        "supp_table_s24_stratified_false_context",
    ]
    gate_decomposition_stems = [
        "supp_table_s25_gate_failure_decomposition",
        "supp_table_s25_gate_failure_summary",
    ]
    threshold_operating_stems = [
        "supp_table_s26_threshold_operating_points",
        "supp_table_s26_threshold_axis_sensitivity",
    ]
    metric_definition_stems = [
        "supp_table_s27_metric_definition_audit",
    ]
    utility_matrix_stems = [
        "supp_table_s34_utility_matrix_construction",
    ]
    dataset_scope_stems = [
        "supp_table_s28_dataset_scope_split_audit",
    ]
    method_scope_stems = [
        "supp_table_s29_method_scope_fairness_audit",
    ]
    disaggregation_stems = [
        "supp_table_s30a_route_aggregation_trace",
        "supp_table_s30b_dataset_task_performance_disaggregation",
        "supp_table_s31_failure_taxonomy_denominator_audit",
        "supp_table_s32_panel_depth_observability_audit",
    ]
    stress_accounting_stems = [
        "supp_table_s33a_threshold_grid_detail",
        "supp_table_s33b_stress_family_accounting",
        "supp_table_s33c_claim_survival_reconciliation",
    ]
    control_taxonomy_stems = [
        "supp_table_s35_control_taxonomy_sensitivity",
    ]
    power_mde_stems = [
        "supp_table_s36_power_mde_split_counts",
    ]
    method_scope_lr_stems = [
        "supp_table_s37_method_scope_lr_coverage",
    ]
    threshold_gate_policy_stems = [
        "supp_table_s38_threshold_gate_policy",
    ]
    positive_control_scope_stems = [
        "supp_table_s39_positive_control_scope_k_audit",
    ]
    validations["expanded_quantitative_tables_present"] = all(
        stem in table_manifest for stem in expanded_stems
    )
    validations["expanded_quantitative_table_count"] = sum(
        1 for stem in expanded_stems if stem in table_manifest
    )
    validations["expanded_quantitative_tables_nonempty"] = all(
        int(table_manifest[stem]["rows"]) > 0
        for stem in expanded_stems
        if stem in table_manifest
    )
    validations["calibration_tables_present"] = all(
        stem in table_manifest for stem in calibration_stems
    )
    validations["calibration_table_count"] = sum(
        1 for stem in calibration_stems if stem in table_manifest
    )
    validations["calibration_tables_nonempty"] = all(
        int(table_manifest[stem]["rows"]) > 0
        for stem in calibration_stems
        if stem in table_manifest
    )
    validations["leakage_downgrade_residual_tables_present"] = all(
        stem in table_manifest for stem in audit_stems
    )
    validations["leakage_downgrade_residual_table_count"] = sum(
        1 for stem in audit_stems if stem in table_manifest
    )
    validations["leakage_downgrade_residual_tables_nonempty"] = all(
        int(table_manifest[stem]["rows"]) > 0
        for stem in audit_stems
        if stem in table_manifest
    )
    validations["stratified_fcr_tables_present"] = all(
        stem in table_manifest for stem in stratified_stems
    )
    validations["stratified_fcr_table_count"] = sum(
        1 for stem in stratified_stems if stem in table_manifest
    )
    validations["stratified_fcr_tables_nonempty"] = all(
        int(table_manifest[stem]["rows"]) > 0
        for stem in stratified_stems
        if stem in table_manifest
    )
    validations["gate_decomposition_tables_present"] = all(
        stem in table_manifest for stem in gate_decomposition_stems
    )
    validations["gate_decomposition_table_count"] = sum(
        1 for stem in gate_decomposition_stems if stem in table_manifest
    )
    validations["gate_decomposition_tables_nonempty"] = all(
        int(table_manifest[stem]["rows"]) > 0
        for stem in gate_decomposition_stems
        if stem in table_manifest
    )
    validations["threshold_operating_tables_present"] = all(
        stem in table_manifest for stem in threshold_operating_stems
    )
    validations["threshold_operating_table_count"] = sum(
        1 for stem in threshold_operating_stems if stem in table_manifest
    )
    validations["threshold_operating_tables_nonempty"] = all(
        int(table_manifest[stem]["rows"]) > 0
        for stem in threshold_operating_stems
        if stem in table_manifest
    )
    validations["metric_definition_tables_present"] = all(
        stem in table_manifest for stem in metric_definition_stems
    )
    validations["metric_definition_table_count"] = sum(
        1 for stem in metric_definition_stems if stem in table_manifest
    )
    validations["metric_definition_tables_nonempty"] = all(
        int(table_manifest[stem]["rows"]) > 0
        for stem in metric_definition_stems
        if stem in table_manifest
    )
    validations["utility_matrix_tables_present"] = all(
        stem in table_manifest for stem in utility_matrix_stems
    )
    validations["utility_matrix_table_count"] = sum(
        1 for stem in utility_matrix_stems if stem in table_manifest
    )
    validations["utility_matrix_tables_nonempty"] = all(
        int(table_manifest[stem]["rows"]) > 0
        for stem in utility_matrix_stems
        if stem in table_manifest
    )
    validations["dataset_scope_tables_present"] = all(
        stem in table_manifest for stem in dataset_scope_stems
    )
    validations["dataset_scope_table_count"] = sum(
        1 for stem in dataset_scope_stems if stem in table_manifest
    )
    validations["dataset_scope_tables_nonempty"] = all(
        int(table_manifest[stem]["rows"]) > 0
        for stem in dataset_scope_stems
        if stem in table_manifest
    )
    validations["method_scope_tables_present"] = all(
        stem in table_manifest for stem in method_scope_stems
    )
    validations["method_scope_table_count"] = sum(
        1 for stem in method_scope_stems if stem in table_manifest
    )
    validations["method_scope_tables_nonempty"] = all(
        int(table_manifest[stem]["rows"]) > 0
        for stem in method_scope_stems
        if stem in table_manifest
    )
    validations["disaggregation_tables_present"] = all(
        stem in table_manifest for stem in disaggregation_stems
    )
    validations["disaggregation_table_count"] = sum(
        1 for stem in disaggregation_stems if stem in table_manifest
    )
    validations["disaggregation_tables_nonempty"] = all(
        int(table_manifest[stem]["rows"]) > 0
        for stem in disaggregation_stems
        if stem in table_manifest
    )
    validations["stress_accounting_tables_present"] = all(
        stem in table_manifest for stem in stress_accounting_stems
    )
    validations["stress_accounting_table_count"] = sum(
        1 for stem in stress_accounting_stems if stem in table_manifest
    )
    validations["stress_accounting_tables_nonempty"] = all(
        int(table_manifest[stem]["rows"]) > 0
        for stem in stress_accounting_stems
        if stem in table_manifest
    )
    validations["control_taxonomy_tables_present"] = all(
        stem in table_manifest for stem in control_taxonomy_stems
    )
    validations["control_taxonomy_table_count"] = sum(
        1 for stem in control_taxonomy_stems if stem in table_manifest
    )
    validations["control_taxonomy_tables_nonempty"] = all(
        int(table_manifest[stem]["rows"]) > 0
        for stem in control_taxonomy_stems
        if stem in table_manifest
    )
    validations["power_mde_tables_present"] = all(
        stem in table_manifest for stem in power_mde_stems
    )
    validations["power_mde_table_count"] = sum(
        1 for stem in power_mde_stems if stem in table_manifest
    )
    validations["power_mde_tables_nonempty"] = all(
        int(table_manifest[stem]["rows"]) > 0
        for stem in power_mde_stems
        if stem in table_manifest
    )
    validations["method_scope_lr_tables_present"] = all(
        stem in table_manifest for stem in method_scope_lr_stems
    )
    validations["method_scope_lr_table_count"] = sum(
        1 for stem in method_scope_lr_stems if stem in table_manifest
    )
    validations["method_scope_lr_tables_nonempty"] = all(
        int(table_manifest[stem]["rows"]) > 0
        for stem in method_scope_lr_stems
        if stem in table_manifest
    )
    validations["threshold_gate_policy_tables_present"] = all(
        stem in table_manifest for stem in threshold_gate_policy_stems
    )
    validations["threshold_gate_policy_table_count"] = sum(
        1 for stem in threshold_gate_policy_stems if stem in table_manifest
    )
    validations["threshold_gate_policy_tables_nonempty"] = all(
        int(table_manifest[stem]["rows"]) > 0
        for stem in threshold_gate_policy_stems
        if stem in table_manifest
    )
    validations["positive_control_scope_tables_present"] = all(
        stem in table_manifest for stem in positive_control_scope_stems
    )
    validations["positive_control_scope_table_count"] = sum(
        1 for stem in positive_control_scope_stems if stem in table_manifest
    )
    validations["positive_control_scope_tables_nonempty"] = all(
        int(table_manifest[stem]["rows"]) > 0
        for stem in positive_control_scope_stems
        if stem in table_manifest
    )
    validations["passed"] = all(
        [
            validations["all_claim_sources_exist"],
            validations["contextgate_gate_passed"],
            validations["contextgate_no_harm_gate_passed"],
            validations["benchmark_matrix_gate_passed"],
            validations["benchmark_failed_jobs"] == 0,
            validations["robustness_gate_passed"],
            validations["failed_stress_rows_without_downgrade"] == 0,
            validations["strong_biological_context_claim_downgraded"],
            validations["expanded_quantitative_tables_present"],
            validations["expanded_quantitative_tables_nonempty"],
            validations["calibration_tables_present"],
            validations["calibration_tables_nonempty"],
            validations["leakage_downgrade_residual_tables_present"],
            validations["leakage_downgrade_residual_tables_nonempty"],
            validations["stratified_fcr_tables_present"],
            validations["stratified_fcr_tables_nonempty"],
            validations["gate_decomposition_tables_present"],
            validations["gate_decomposition_tables_nonempty"],
            validations["threshold_operating_tables_present"],
            validations["threshold_operating_tables_nonempty"],
            validations["metric_definition_tables_present"],
            validations["metric_definition_tables_nonempty"],
            validations["utility_matrix_tables_present"],
            validations["utility_matrix_tables_nonempty"],
            validations["dataset_scope_tables_present"],
            validations["dataset_scope_tables_nonempty"],
            validations["method_scope_tables_present"],
            validations["method_scope_tables_nonempty"],
            validations["disaggregation_tables_present"],
            validations["disaggregation_tables_nonempty"],
            validations["stress_accounting_tables_present"],
            validations["stress_accounting_tables_nonempty"],
            validations["control_taxonomy_tables_present"],
            validations["control_taxonomy_tables_nonempty"],
            validations["power_mde_tables_present"],
            validations["power_mde_tables_nonempty"],
            validations["method_scope_lr_tables_present"],
            validations["method_scope_lr_tables_nonempty"],
            validations["threshold_gate_policy_tables_present"],
            validations["threshold_gate_policy_tables_nonempty"],
            validations["positive_control_scope_tables_present"],
            validations["positive_control_scope_tables_nonempty"],
        ]
    )
    return validations


def build_tables(output_dir: Path) -> dict:
    builders = [
        (
            "main_table_1_dataset_eligibility",
            "Main Table 1: Dataset Eligibility Summary",
            build_dataset_eligibility,
        ),
        (
            "main_table_2_benchmark_matrix",
            "Main Table 2: Benchmark Matrix Summary",
            build_benchmark_matrix,
        ),
        (
            "main_table_3_claim_to_evidence_audit",
            "Main Table 3: Claim-To-Evidence Audit",
            build_claim_audit,
        ),
        (
            "supp_table_s1_scale_contract",
            "Supplementary Table S1: Scale Contract Compliance",
            build_scale_contract,
        ),
        (
            "supp_table_s2_method_metrics",
            "Supplementary Table S2: Method Metrics",
            build_method_metrics,
        ),
        (
            "supp_table_s3_positive_null_summary",
            "Supplementary Table S3: Positive/Null-Control Summary",
            build_positive_null_summary,
        ),
        (
            "supp_table_s4_failure_summary",
            "Supplementary Table S4: Failure-Class Summary",
            build_failure_summary,
        ),
        (
            "supp_table_s5_contextgate_routes",
            "Supplementary Table S5: ContextGate Route Summary",
            build_contextgate_route_summary,
        ),
        (
            "supp_table_s6_contextgate_no_harm",
            "Supplementary Table S6: ContextGate No-Harm Audit",
            build_contextgate_no_harm,
        ),
        (
            "supp_table_s7_stress_summary",
            "Supplementary Table S7: Robustness Stress Summary",
            build_stress_summary,
        ),
        (
            "supp_table_s8_table_text_only_evidence",
            "Supplementary Table S8: Table/Text-Only Evidence",
            build_table_only_evidence,
        ),
        (
            "supp_table_s9_figure_inventory",
            "Supplementary Table S9: Figure Export Inventory",
            build_figure_inventory,
        ),
        (
            "supp_table_s10_cp_q2_dataset_task_utility",
            "Supplementary Table S10: CP-Q2 Dataset-Task Utility",
            build_cp_q2_dataset_task_utility,
        ),
        (
            "supp_table_s11_q6_dataset_task_method_metrics",
            "Supplementary Table S11: CP-Q6 Dataset-Task-Method Metrics",
            build_q6_dataset_task_method_metrics,
        ),
        (
            "supp_table_s12_q6_method_task_safety",
            "Supplementary Table S12: CP-Q6 Method-Task Safety Summary",
            build_q6_method_task_safety,
        ),
        (
            "supp_table_s13_contextgate_routes_by_dataset_task",
            "Supplementary Table S13: ContextGate Routes By Dataset And Task",
            build_contextgate_routes_by_dataset_task,
        ),
        (
            "supp_table_s14_q6_skip_infeasibility",
            "Supplementary Table S14: CP-Q6 Skip And Infeasibility Reasons",
            build_q6_skip_infeasibility,
        ),
        (
            "supp_table_s15_claim_downgrade_distribution",
            "Supplementary Table S15: Claim Downgrade Distribution",
            build_claim_downgrade_distribution,
        ),
        (
            "supp_table_s16_positive_null_signal_strength",
            "Supplementary Table S16: Positive And Null Signal Strength",
            build_positive_null_signal_strength,
        ),
        (
            "supp_table_s17_q6_regret_distribution",
            "Supplementary Table S17: CP-Q6 Regret Distribution",
            build_q6_regret_distribution,
        ),
        (
            "supp_table_s18_threshold_calibration_summary",
            "Supplementary Table S18: Threshold Calibration Summary",
            build_threshold_calibration_summary,
        ),
        (
            "supp_table_s19_detectability_min_effect",
            "Supplementary Table S19: Detectability And Minimum Effect Audit",
            build_detectability_min_effect,
        ),
        (
            "supp_table_s20_real_vs_detectability_audit",
            "Supplementary Table S20: Real-Data Gates Versus Detectability",
            build_real_vs_detectability_audit,
        ),
        (
            "supp_table_s21_leakage_confounding_examples",
            "Supplementary Table S21: Leakage And Confounding Examples",
            build_leakage_confounding_examples,
        ),
        (
            "supp_table_s22_downgrade_examples",
            "Supplementary Table S22: Downgrade Examples",
            build_downgrade_examples,
        ),
        (
            "supp_table_s23_residualization_audit",
            "Supplementary Table S23: Residualization Audit",
            build_residualization_audit,
        ),
        (
            "supp_table_s24_stratified_false_context",
            "Supplementary Table S24: Stratified False-Context Audit",
            build_stratified_false_context,
        ),
        (
            "supp_table_s25_gate_failure_decomposition",
            "Supplementary Table S25A: Gate-Failure Decomposition",
            build_gate_failure_decomposition,
        ),
        (
            "supp_table_s25_gate_failure_summary",
            "Supplementary Table S25B: Gate-Failure Summary",
            build_gate_failure_summary,
        ),
        (
            "supp_table_s26_threshold_operating_points",
            "Supplementary Table S26A: Threshold Operating Points",
            build_threshold_operating_points,
        ),
        (
            "supp_table_s26_threshold_axis_sensitivity",
            "Supplementary Table S26B: Threshold-Axis Sensitivity",
            build_threshold_axis_sensitivity,
        ),
        (
            "supp_table_s27_metric_definition_audit",
            "Supplementary Table S27: Metric Definition Audit",
            build_metric_definition_audit,
        ),
        (
            "supp_table_s28_dataset_scope_split_audit",
            "Supplementary Table S28: Dataset Scope And Split Audit",
            build_dataset_scope_split_audit,
        ),
        (
            "supp_table_s29_method_scope_fairness_audit",
            "Supplementary Table S29: Method Scope And Fairness Audit",
            build_method_scope_fairness_audit,
        ),
        (
            "supp_table_s30a_route_aggregation_trace",
            "Supplementary Table S30A: Route Aggregation Trace",
            build_route_aggregation_trace,
        ),
        (
            "supp_table_s30b_dataset_task_performance_disaggregation",
            "Supplementary Table S30B: Dataset-Task Performance Disaggregation",
            build_dataset_task_performance_disaggregation,
        ),
        (
            "supp_table_s31_failure_taxonomy_denominator_audit",
            "Supplementary Table S31: Failure Taxonomy Denominator Audit",
            build_failure_taxonomy_denominator_audit,
        ),
        (
            "supp_table_s32_panel_depth_observability_audit",
            "Supplementary Table S32: Panel-Depth Observability Audit",
            build_panel_depth_observability_audit,
        ),
        (
            "supp_table_s33a_threshold_grid_detail",
            "Supplementary Table S33A: Threshold Grid Detail",
            build_threshold_grid_detail,
        ),
        (
            "supp_table_s33b_stress_family_accounting",
            "Supplementary Table S33B: Stress Family Accounting",
            build_stress_family_accounting,
        ),
        (
            "supp_table_s33c_claim_survival_reconciliation",
            "Supplementary Table S33C: Claim Survival Reconciliation",
            build_claim_survival_reconciliation,
        ),
        (
            "supp_table_s34_utility_matrix_construction",
            "Supplementary Table S34: Utility Matrix And Tier Glossary",
            build_utility_matrix_construction,
        ),
        (
            "supp_table_s35_control_taxonomy_sensitivity",
            "Supplementary Table S35: Control Taxonomy And Sensitivity Scores",
            build_control_taxonomy_sensitivity,
        ),
        (
            "supp_table_s36_power_mde_split_counts",
            "Supplementary Table S36: Split Count And Power Proxy Audit",
            build_power_mde_split_counts,
        ),
        (
            "supp_table_s37_method_scope_lr_coverage",
            "Supplementary Table S37: Method Scope And LR Coverage",
            build_method_scope_lr_coverage,
        ),
        (
            "supp_table_s38_threshold_gate_policy",
            "Supplementary Table S38: Threshold Gate Policy",
            build_threshold_gate_policy,
        ),
        (
            "supp_table_s39_positive_control_scope_k_audit",
            "Supplementary Table S39: Positive-Control Scope And K Audit",
            build_positive_control_scope_k_audit,
        ),
    ]
    table_manifest = {}
    claim_audit = pd.DataFrame()
    for stem, title, builder in builders:
        df = builder()
        table_manifest[stem] = _write_table(
            df,
            stem=stem,
            title=title,
            output_dir=output_dir,
        )
        if stem == "main_table_3_claim_to_evidence_audit":
            claim_audit = df

    validations = _validate_outputs(claim_audit, table_manifest)
    manifest = {
        "generator": "scripts/build_contextgate_manuscript_tables.py",
        "target_journal": "Computational Biology and Chemistry",
        "source_report_root": str(REPORT_ROOT),
        "output_dir": str(output_dir),
        "tables": table_manifest,
        "validations": validations,
    }
    manifest_path = output_dir / "manuscript_table_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    if not validations["passed"]:
        raise RuntimeError(f"Manuscript table validation failed: {validations}")
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help="Directory for manuscript table CSV/Markdown/LaTeX outputs.",
    )
    args = parser.parse_args()
    manifest = build_tables(args.output_dir)
    print(json.dumps(manifest["validations"], indent=2))


if __name__ == "__main__":
    main()
