"""Build single-purpose publication figures for ContextGate-Bench.

This script exports individual figures from registered CP-Q result tables.
Each plot is intentionally narrow in purpose so manuscript assembly can choose
single figures or clean two-panel combinations without overcrowding.
"""

from __future__ import annotations

import argparse
import json
import os
from collections.abc import Iterable
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

PROJECT_ROOT = Path(__file__).resolve().parents[1]
REPORT_ROOT = PROJECT_ROOT / "results" / "reports"
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "manuscript" / "figures" / "singles"
FIGURE_SOURCE_DATE_EPOCH = "1777939200"  # 2026-05-05T00:00:00Z.

TABLE_ONLY_RECOMMENDATIONS = {
    "claim_survival_audit": {
        "source": "cp_q7_robustness_stress/claim_survival_audit.csv",
        "reason": "Only two outcome counts; state in text or claim-to-evidence table.",
    },
    "method_no_harm_profile": {
        "source": "cp_q2_method_comparison/method_metrics.csv",
        "reason": (
            "Sparse no-harm/false-context points; full-benchmark metric profile "
            "and no-harm table carry the evidence more cleanly."
        ),
    },
    "modal_matrix_execution": {
        "source": "cp_q6_benchmark_matrix/job_status.csv",
        "reason": "Administrative job counts are better as a reproducibility table.",
    },
    "registered_no_harm_dumbbell": {
        "source": "cp_q5_contextgate_decisions/contextgate_no_harm.csv",
        "reason": (
            "Mostly zero-valued false-context rates; report as a no-harm "
            "audit row."
        ),
    },
    "synthetic_no_harm_dumbbell": {
        "source": "cp_q5_contextgate_decisions/contextgate_no_harm.csv",
        "reason": (
            "Mostly zero-valued false-context rates; report as a no-harm "
            "audit row."
        ),
    },
    "threshold_leave_one_out_checks": {
        "source": (
            "cp_q7_robustness_stress/threshold_sensitivity.csv and "
            "leave_one_out_stress.csv"
        ),
        "reason": "Four count values; a robustness table is clearer than a bar chart.",
    },
    "utility_delta_vs_always_context": {
        "source": "cp_q2_method_comparison/paired_method_deltas.csv",
        "reason": (
            "The key contrast is already covered by regret/metric-profile figures; "
            "use a sentence or supplementary method-delta table."
        ),
    },
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
    "random_neighbor_control_model": "Random neighbor",
    "spatial_statistics_heuristic": "Spatial stats",
}

ROUTE_LABELS = {
    "abstain_uncertain": "Abstain",
    "expression_only": "Expression only",
    "positive_control_only": "Positive control",
    "context_allowed": "Context allowed",
}

DATASET_LABELS = {
    "cosmx_6k_bcc_yerly_2024": "CosMx BCC 6K",
    "cosmx_nsclc_ffpe_v1": "CosMx NSCLC",
    "discovery_index_without_direct_artifact": "Discovery index",
    "gse277782_cosmx_pdac_metastasis": "CosMx PDAC metastasis",
    "gse310352_cosmx_pdac_1k": "CosMx PDAC 1K",
    "htapp_mbc_scp2702_merfish": "HTAPP MBC",
    "private_or_login_only_source": "Private/login source",
    "private_or_login_only_sources": "Private/login source",
    "scarna_visium_deconvolution_index": "scRNA+Visium index",
    "scrna_visium_deconvolution_cell_claim": "scRNA+Visium claim",
    "standard_visium_spot_level_only": "Spot-level Visium",
    "standard_visium_spot_level_source": "Spot-level Visium",
    "xenium_breast_biomarkers_v1": "Xenium breast biomarkers",
    "xenium_breast_v1": "Xenium breast 5K",
}

TASK_LABELS = {
    "context_utility_detection": "Context\nutility",
    "dataset_access": "Dataset\naccess",
    "not_recorded": "Not\nrecorded",
    "positive_null_control_ladder": "Positive/null\nladder",
}

METRIC_LABELS = {
    "no_harm_rate": "No-harm\n↑ better",
    "false_positive_context_rate": "False\ncontext\n↓ better",
    "abstention_rate": "Abstention\n↓ better",
    "regret_against_oracle": "Oracle\nregret\n↓ better",
    "heldout_replication_rate": "Held-out\nreplication\n↑ better",
    "skip_reason_rate": "Skip\nreason",
}

METRIC_PROFILE_ORDER = [
    "no_harm_rate",
    "false_positive_context_rate",
    "abstention_rate",
    "regret_against_oracle",
    "heldout_replication_rate",
]
LOWER_IS_BETTER_METRICS = {
    "false_positive_context_rate",
    "abstention_rate",
    "regret_against_oracle",
    "skip_reason_rate",
}

POSITIVE_SIGNAL_XTICKS = [0.55, 0.75, 1.00]

FAILURE_LABELS = {
    "access_or_schema_blocker": "Access/schema blocker",
    "expression_absorbs_signal": "Expression absorbs signal",
    "fov_or_sample_artifact": "FOV/sample artifact",
    "insufficient_power": "Insufficient power",
    "labels_not_replicated": "Labels not replicated",
    "lr_without_downstream_response": "LR without downstream response",
    "panel_lacks_downstream_genes": "Panel lacks downstream genes",
}

STRESS_LABELS = {
    "compute_sensitivity": "Compute sensitivity",
    "contextgate_reason_ablation": "Router-reason ablation",
    "control_ablation": "Control ablation",
    "leave_one_out": "Leave-one-out",
    "positive_control_ablation": "Positive-control ablation",
    "seed_sweep": "Seed sweep",
    "threshold_sensitivity": "Threshold sensitivity",
}

SCALE_AXIS_LABELS = {
    "cancer_or_tissue_contexts": "Cancer/tissue contexts",
    "control_families": "Control families",
    "core_factorial_jobs": "Core factorial jobs",
    "main_figures": "Main figures",
    "method_families": "Method families",
    "metric_families": "Metric families",
    "mini_factorial_jobs": "Mini factorial jobs",
    "positive_control_levels": "Positive-control levels",
    "q1_factorial_jobs": "Full factorial jobs",
    "q1_nominal_jobs_soft_max": "Full jobs soft cap",
    "stochastic_seeds": "Stochastic seeds",
    "supplementary_tables": "Supplementary tables",
}

COLORS = {
    "blue": "#2F5D8C",
    "teal": "#2A9D8F",
    "green": "#4C956C",
    "orange": "#D98C3A",
    "red": "#B94A48",
    "purple": "#6A4C93",
    "gray": "#6C757D",
    "dark": "#1F2933",
}


def _read_csv(*parts: str) -> pd.DataFrame:
    path = REPORT_ROOT.joinpath(*parts)
    if not path.exists():
        raise FileNotFoundError(path)
    return pd.read_csv(path)


def _as_bool_series(series: pd.Series) -> pd.Series:
    if pd.api.types.is_bool_dtype(series):
        return series.fillna(False).astype(bool)
    normalized = series.astype(str).str.strip().str.lower()
    return normalized.isin({"true", "1", "yes", "y"})


def _shorten_label(value: object, max_len: int = 28) -> str:
    text = str(value).replace("_", " ")
    if len(text) <= max_len:
        return text
    return text[: max_len - 1].rstrip() + "..."


def _method_label(method_id: object) -> str:
    return METHOD_LABELS.get(str(method_id), _shorten_label(method_id, 22))


def _dataset_label(dataset_id: object) -> str:
    return DATASET_LABELS.get(str(dataset_id), _shorten_label(dataset_id, 30))


def _task_label(task_id: object) -> str:
    return TASK_LABELS.get(str(task_id), _shorten_label(task_id, 22))


def _failure_label(failure_class: object) -> str:
    return FAILURE_LABELS.get(str(failure_class), _shorten_label(failure_class, 30))


def _stress_label(stress_family: object) -> str:
    return STRESS_LABELS.get(str(stress_family), _shorten_label(stress_family, 28))


def _scale_axis_label(axis_name: object) -> str:
    return SCALE_AXIS_LABELS.get(str(axis_name), _shorten_label(axis_name, 30))


def _contrast_text_color(image: object, value: float) -> str:
    rgba = image.cmap(image.norm(float(value)))
    luminance = 0.2126 * rgba[0] + 0.7152 * rgba[1] + 0.0722 * rgba[2]
    return COLORS["dark"] if luminance > 0.55 else "white"


def _style_axes(ax: plt.Axes, *, xgrid: bool = True, ygrid: bool = False) -> None:
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#ADB5BD")
    ax.spines["bottom"].set_color("#ADB5BD")
    ax.tick_params(colors=COLORS["dark"], labelsize=8)
    if xgrid:
        ax.grid(axis="x", color="#DEE2E6", linewidth=0.7)
    if ygrid:
        ax.grid(axis="y", color="#DEE2E6", linewidth=0.7)
    ax.set_axisbelow(True)


def _save_figure(fig: plt.Figure, stem: str, output_dir: Path) -> dict[str, str]:
    output_dir.mkdir(parents=True, exist_ok=True)
    os.environ.setdefault("SOURCE_DATE_EPOCH", FIGURE_SOURCE_DATE_EPOCH)
    paths = {
        "pdf": output_dir / f"{stem}.pdf",
        "eps": output_dir / f"{stem}.eps",
        "png": output_dir / f"{stem}.png",
    }
    for suffix, path in paths.items():
        if suffix == "png":
            fig.savefig(path, dpi=600, bbox_inches="tight", facecolor="white")
        else:
            fig.savefig(path, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return {key: str(value) for key, value in paths.items()}


def _annotate_hbars(
    ax: plt.Axes,
    values: Iterable[float],
    *,
    fmt: str = "{:.0f}",
    pad: float = 0.02,
) -> None:
    for patch, value in zip(ax.patches, values, strict=False):
        ax.text(
            patch.get_width() + pad,
            patch.get_y() + patch.get_height() / 2,
            fmt.format(value),
            va="center",
            ha="left",
            fontsize=7,
            color=COLORS["dark"],
        )


def _annotate_vbars(
    ax: plt.Axes,
    values: Iterable[float],
    *,
    fmt: str = "{:.0f}",
) -> None:
    for patch, value in zip(ax.patches, values, strict=False):
        ax.text(
            patch.get_x() + patch.get_width() / 2,
            patch.get_height() + 0.02,
            fmt.format(value),
            va="bottom",
            ha="center",
            fontsize=7,
            color=COLORS["dark"],
        )


def build_scale_contract_coverage(output_dir: Path) -> dict[str, str]:
    scale = _read_csv("cp_q6_benchmark_matrix", "scale_contract_compliance.csv")
    scale = scale.copy()
    scale["target_min"] = scale["target_min"].replace(0, np.nan)
    scale["target_ratio"] = scale["observed_count"] / scale["target_min"]
    scale = scale.sort_values("target_ratio", ascending=True).tail(12)

    fig, ax = plt.subplots(figsize=(6.2, 4.6))
    ratios = scale["target_ratio"].clip(upper=5.0).fillna(5.0)
    y = np.arange(len(scale))
    colors = [
        COLORS["green"] if passed else COLORS["red"]
        for passed in scale["passed"]
    ]
    ax.barh(y, ratios, color=colors, edgecolor="white", linewidth=0.5)
    ax.axvline(1.0, color=COLORS["dark"], linewidth=1.0)
    ax.set_yticks(y)
    ax.set_yticklabels([_scale_axis_label(v) for v in scale["axis"]])
    ax.set_xlabel("Observed / required minimum")
    ax.set_title("Scale-contract coverage")
    ax.set_xlim(0, 5.45)
    for idx, row in enumerate(scale.itertuples(index=False)):
        text = (
            f"{int(row.observed_count)} observed"
            if pd.isna(row.target_min)
            else f"{int(row.observed_count)} / {int(row.target_min)}"
        )
        ax.text(
            min(float(ratios.iloc[idx]) + 0.08, 5.05),
            idx,
            text,
            va="center",
            fontsize=7,
            color=COLORS["dark"],
        )
    _style_axes(ax)
    fig.tight_layout()
    return _save_figure(fig, "scale_contract_coverage", output_dir)


def build_modal_matrix_execution(output_dir: Path) -> dict[str, str]:
    jobs = _read_csv("cp_q6_benchmark_matrix", "job_status.csv")
    status = (
        jobs.groupby(["benchmark_tier", "status"])
        .size()
        .unstack(fill_value=0)
        .reindex(["mini", "core", "q1"])
        .rename(index={"q1": "full"})
    )
    fig, ax = plt.subplots(figsize=(5.2, 4.0))
    bottom = np.zeros(len(status))
    status_colors = {
        "completed": COLORS["green"],
        "skipped": COLORS["orange"],
        "failed": COLORS["red"],
    }
    for status_name in ["completed", "skipped", "failed"]:
        values = status[status_name] if status_name in status else 0
        ax.bar(
            status.index,
            values,
            bottom=bottom,
            color=status_colors[status_name],
            edgecolor="white",
            linewidth=0.5,
            label=status_name.capitalize(),
        )
        bottom += np.asarray(values, dtype=float)
    ax.set_ylabel("Jobs")
    ax.set_title("Modal matrix execution")
    ax.legend(frameon=False, fontsize=8, loc="upper left")
    _style_axes(ax, xgrid=False, ygrid=True)
    fig.tight_layout()
    return _save_figure(fig, "modal_matrix_execution", output_dir)


def build_pipeline_architecture(output_dir: Path) -> dict[str, str]:
    fig, ax = plt.subplots(figsize=(7.1, 3.8))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    stages = [
        (
            0.03,
            0.62,
            "Dataset eligibility\ncell coordinates\nimaging panel\nsplit metadata",
            "Contract\nregistry",
            "#E7F0FF",
        ),
        (
            0.23,
            0.62,
            "Method/control\nmatrix\nexpression-only\ncontext controls",
            "CP-Q2/Q6",
            "#E9F7EF",
        ),
        (
            0.43,
            0.62,
            "Synthetic ladder\nand CP-R1 score\npositive/null rows\nreal-data utility",
            "CP-Q3/R1",
            "#FFF4E5",
        ),
        (
            0.63,
            0.62,
            "ContextGate\nsix-gate router\nresidual utility\nreplication\ndowngrades",
            "CP-Q5",
            "#F3E8FF",
        ),
        (
            0.83,
            0.62,
            "Claim release\nroute counts\nfailure taxonomy\nstress audit",
            "CP-Q7/Q8",
            "#E6F7F8",
        ),
    ]
    box_w = 0.15
    box_h = 0.28
    for idx, (x, y, body, tag, color) in enumerate(stages):
        patch = FancyBboxPatch(
            (x, y),
            box_w,
            box_h,
            boxstyle="round,pad=0.015,rounding_size=0.018",
            linewidth=1.0,
            edgecolor="#495057",
            facecolor=color,
        )
        ax.add_patch(patch)
        ax.text(
            x + box_w / 2,
            y + box_h - 0.045,
            tag,
            ha="center",
            va="center",
            fontsize=8,
            fontweight="bold",
            color=COLORS["dark"],
        )
        ax.text(
            x + box_w / 2,
            y + 0.105,
            body,
            ha="center",
            va="center",
            fontsize=6.8,
            color=COLORS["dark"],
            linespacing=1.15,
        )
        if idx < len(stages) - 1:
            start = (x + box_w + 0.012, y + box_h / 2)
            end = (stages[idx + 1][0] - 0.012, y + box_h / 2)
            ax.add_patch(
                FancyArrowPatch(
                    start,
                    end,
                    arrowstyle="-|>",
                    mutation_scale=11,
                    linewidth=1.2,
                    color="#495057",
                )
            )

    audit_boxes = [
        (0.04, "Machine-readable artifacts\nCSV/YAML/JSON\nfigure scripts"),
        (0.36, "Controls expose false context\nwrong-neighbor/null\npanel-blocked rows"),
        (0.68, "Stress tests preserve boundary\nthresholds/ablations\nreplay hooks"),
    ]
    for x, label in audit_boxes:
        patch = FancyBboxPatch(
            (x, 0.18),
            0.28,
            0.18,
            boxstyle="round,pad=0.012,rounding_size=0.014",
            linewidth=0.9,
            edgecolor="#6C757D",
            facecolor="#F8F9FA",
        )
        ax.add_patch(patch)
        ax.text(
            x + 0.14,
            0.27,
            label,
            ha="center",
            va="center",
            fontsize=6.6,
            color=COLORS["dark"],
            linespacing=1.15,
        )

    ax.text(
        0.5,
        0.06,
        "Primary route evidence: CP-R1 real-data rows + CP-Q3 synthetic ladder + dataset-card exclusions",
        ha="center",
        va="center",
        fontsize=7.5,
        color=COLORS["dark"],
    )
    fig.tight_layout()
    return _save_figure(fig, "pipeline_architecture", output_dir)


def build_full_benchmark_metric_profile(output_dir: Path) -> dict[str, str]:
    metrics = _read_csv("cp_q6_benchmark_matrix", "aggregate_metrics.csv")
    selected = metrics[
        (metrics["benchmark_tier"] == "q1")
        & metrics["metric_name"].isin(METRIC_LABELS)
    ].copy()
    pivot = selected.pivot_table(
        index="method_id",
        columns="metric_name",
        values="mean_metric_value",
        aggfunc="mean",
    )
    method_order = [
        "contextgate_transparent_router",
        "expression_only_linear",
        "always_true_neighbor_mean",
        "spatial_statistics_heuristic",
        "ligand_receptor_pathway_heuristic",
        "cellpack_packed_context_tiny",
        "random_neighbor_control_model",
        "coordinate_shuffled_control_model",
    ]
    metric_order = METRIC_PROFILE_ORDER
    pivot = pivot.reindex(method_order).dropna(how="all").reindex(columns=metric_order)

    desirability = pivot.copy()
    for metric_name in desirability.columns:
        if metric_name in LOWER_IS_BETTER_METRICS:
            desirability[metric_name] = 1.0 - desirability[metric_name]

    fig, ax = plt.subplots(figsize=(6.7, 4.3))
    image = ax.imshow(
        desirability.fillna(0).to_numpy(),
        aspect="auto",
        cmap="viridis",
        vmin=0,
        vmax=1,
    )
    ax.set_yticks(np.arange(len(pivot)))
    ax.set_yticklabels([_method_label(v) for v in pivot.index])
    ax.set_xticks(np.arange(len(pivot.columns)))
    ax.set_xticklabels([METRIC_LABELS[v] for v in pivot.columns])
    ax.set_title("Full-benchmark metric profile")
    for i in range(pivot.shape[0]):
        for j in range(pivot.shape[1]):
            value = pivot.iloc[i, j]
            if pd.isna(value):
                continue
            ax.text(
                j,
                i,
                f"{value:.2f}",
                ha="center",
                va="center",
                fontsize=6.5,
                color=_contrast_text_color(image, float(desirability.iloc[i, j])),
            )
    colorbar = fig.colorbar(image, ax=ax, fraction=0.046, pad=0.02)
    colorbar.set_label("Visual desirability", fontsize=7)
    colorbar.ax.tick_params(labelsize=7)
    fig.tight_layout()
    return _save_figure(fig, "full_benchmark_metric_profile", output_dir)


def build_method_utility_ranking(output_dir: Path) -> dict[str, str]:
    metrics = _read_csv("cp_q2_method_comparison", "method_metrics.csv")
    order = [
        "contextgate_transparent_router",
        "expression_only_linear",
        "spatial_statistics_heuristic",
        "ligand_receptor_pathway_heuristic",
        "cellpack_packed_context_tiny",
        "always_true_neighbor_mean",
    ]
    data = metrics[metrics["method_id"].isin(order)].copy()
    data["method_label"] = pd.Categorical(
        [_method_label(v) for v in data["method_id"]],
        categories=[_method_label(v) for v in order],
        ordered=True,
    )
    data = data.sort_values("mean_utility", ascending=True)
    fig, ax = plt.subplots(figsize=(5.8, 4.0))
    y = np.arange(len(data))
    ax.barh(y, data["mean_utility"], color=COLORS["teal"], edgecolor="white")
    ax.set_yticks(y)
    ax.set_yticklabels(data["method_label"])
    ax.set_xlim(0, 1.05)
    ax.set_xlabel("Mean utility")
    ax.set_title("Method utility ranking")
    _annotate_hbars(ax, data["mean_utility"], fmt="{:.2f}", pad=0.015)
    _style_axes(ax)
    fig.tight_layout()
    return _save_figure(fig, "method_utility_ranking", output_dir)


def build_method_oracle_regret(output_dir: Path) -> dict[str, str]:
    metrics = _read_csv("cp_q2_method_comparison", "method_metrics.csv")
    order = [
        "contextgate_transparent_router",
        "expression_only_linear",
        "spatial_statistics_heuristic",
        "ligand_receptor_pathway_heuristic",
        "cellpack_packed_context_tiny",
        "always_true_neighbor_mean",
    ]
    data = metrics[metrics["method_id"].isin(order)].copy()
    data["method_label"] = [_method_label(v) for v in data["method_id"]]
    data = data.sort_values(
        ["mean_regret", "method_label"],
        ascending=[False, True],
    )
    fig, ax = plt.subplots(figsize=(5.8, 4.0))
    y = np.arange(len(data))
    ax.barh(y, data["mean_regret"], color=COLORS["orange"], edgecolor="white")
    ax.set_yticks(y)
    ax.set_yticklabels(data["method_label"])
    ax.set_xlim(0, 1.0)
    ax.set_xlabel("Mean regret against oracle")
    ax.set_title("Oracle-regret audit")
    _annotate_hbars(ax, data["mean_regret"], fmt="{:.2f}", pad=0.015)
    ax.invert_yaxis()
    _style_axes(ax)
    fig.tight_layout()
    return _save_figure(fig, "method_oracle_regret", output_dir)


def build_method_no_harm_profile(output_dir: Path) -> dict[str, str]:
    metrics = _read_csv("cp_q2_method_comparison", "method_metrics.csv")
    order = [
        "contextgate_transparent_router",
        "expression_only_linear",
        "spatial_statistics_heuristic",
        "ligand_receptor_pathway_heuristic",
        "cellpack_packed_context_tiny",
        "always_true_neighbor_mean",
    ]
    data = metrics[metrics["method_id"].isin(order)].copy()
    data["method_label"] = pd.Categorical(
        [_method_label(v) for v in data["method_id"]],
        categories=[_method_label(v) for v in order],
        ordered=True,
    )
    data = data.sort_values("method_label")
    y = np.arange(len(data))

    fig, ax = plt.subplots(figsize=(5.8, 4.0))
    for idx, row in enumerate(data.itertuples(index=False)):
        ax.plot(
            [row.false_positive_context_rate, row.no_harm_rate],
            [idx, idx],
            color="#CED4DA",
            linewidth=1.5,
            zorder=1,
        )
    ax.scatter(
        data["false_positive_context_rate"],
        y,
        color=COLORS["red"],
        s=42,
        label="False context",
        zorder=2,
    )
    ax.scatter(
        data["no_harm_rate"],
        y,
        color=COLORS["green"],
        s=42,
        label="No-harm",
        zorder=2,
    )
    ax.set_yticks(y)
    ax.set_yticklabels(data["method_label"])
    ax.set_xlim(-0.02, 1.04)
    ax.set_xlabel("Rate")
    ax.set_title("False-context and no-harm profile")
    ax.legend(frameon=False, fontsize=8, loc="lower right")
    _style_axes(ax)
    fig.tight_layout()
    return _save_figure(fig, "method_no_harm_profile", output_dir)


def build_utility_delta_vs_always(output_dir: Path) -> dict[str, str]:
    deltas = _read_csv("cp_q2_method_comparison", "paired_method_deltas.csv")
    order = [
        "contextgate_transparent_router",
        "expression_only_linear",
        "spatial_statistics_heuristic",
        "ligand_receptor_pathway_heuristic",
        "cellpack_packed_context_tiny",
        "always_true_neighbor_mean",
    ]
    data = deltas[deltas["method_id"].isin(order)].copy()
    data["method_label"] = pd.Categorical(
        [_method_label(v) for v in data["method_id"]],
        categories=[_method_label(v) for v in order],
        ordered=True,
    )
    data = data.sort_values("method_label")
    values = data["utility_delta_vs_always_context"]
    colors = [COLORS["green"] if value >= 0 else COLORS["red"] for value in values]
    fig, ax = plt.subplots(figsize=(5.8, 4.0))
    ax.barh(np.arange(len(data)), values, color=colors, edgecolor="white")
    ax.axvline(0, color=COLORS["dark"], linewidth=1.0)
    ax.set_yticks(np.arange(len(data)))
    ax.set_yticklabels(data["method_label"])
    ax.set_xlabel("Utility delta vs always-context")
    ax.set_title("No free pass for context")
    _style_axes(ax)
    fig.tight_layout()
    return _save_figure(fig, "utility_delta_vs_always_context", output_dir)


def build_positive_control_recovery(output_dir: Path) -> dict[str, str]:
    recovery = _read_csv("cp_q3_positive_null_control_ladder", "recovery_curve.csv")
    selected_methods = [
        "contextgate_transparent_router",
        "always_true_neighbor_mean",
        "cellpack_packed_context_tiny",
        "expression_only_linear",
        "lightweight_graphsage_aggregation",
    ]
    method_colors = {
        "contextgate_transparent_router": COLORS["teal"],
        "always_true_neighbor_mean": COLORS["red"],
        "cellpack_packed_context_tiny": COLORS["purple"],
        "expression_only_linear": COLORS["gray"],
        "lightweight_graphsage_aggregation": COLORS["blue"],
    }
    rec = recovery[recovery["method_id"].isin(selected_methods)].copy()
    rec = (
        rec.groupby(["method_id", "injected_signal_strength"], as_index=False)
        .agg(sensitivity=("sensitivity", "mean"))
        .sort_values("injected_signal_strength")
    )
    fig, ax = plt.subplots(figsize=(6.8, 4.1))
    for method_id, group in rec.groupby("method_id", sort=False):
        ax.plot(
            group["injected_signal_strength"],
            group["sensitivity"],
            marker="o",
            linewidth=2.0,
            color=method_colors[method_id],
            label=_method_label(method_id),
        )
    rung_labels = {
        0.55: "Weak/noisy",
        0.75: "Localized",
        1.00: "Strong",
    }
    for signal_strength, label in rung_labels.items():
        ax.axvline(
            signal_strength,
            color="#CED4DA",
            linewidth=0.8,
            linestyle=":",
            zorder=0,
        )
        ax.text(
            signal_strength,
            1.035,
            label,
            ha="center",
            va="bottom",
            fontsize=7,
            color=COLORS["dark"],
            clip_on=True,
        )
    ax.set_xlabel("Injected signal coefficient s (dimensionless)")
    ax.set_ylabel("Sensitivity")
    ax.set_ylim(-0.03, 1.08)
    ax.set_xlim(0.50, 1.03)
    ax.set_xticks(POSITIVE_SIGNAL_XTICKS)
    ax.set_title("Positive-control recovery")
    ax.legend(
        frameon=False,
        fontsize=7,
        loc="center left",
        bbox_to_anchor=(1.02, 0.5),
        borderaxespad=0,
    )
    _style_axes(ax, ygrid=True)
    fig.tight_layout()
    return _save_figure(fig, "positive_control_recovery", output_dir)


def build_null_control_heatmap(output_dir: Path) -> dict[str, str]:
    false_positive = _read_csv(
        "cp_q3_positive_null_control_ladder",
        "false_positive_curve.csv",
    )
    selected_methods = [
        "contextgate_transparent_router",
        "expression_only_linear",
        "cellpack_packed_context_tiny",
        "always_true_neighbor_mean",
        "lightweight_graphsage_aggregation",
    ]
    order = [
        "null_no_context_signal",
        "missing_panel_or_target_dropout_signal",
        "fov_or_sample_confounded_signal",
    ]
    control_labels = ["Null", "Panel/dropout", "FOV confound"]
    data = false_positive[false_positive["method_id"].isin(selected_methods)].copy()
    data = (
        data.groupby(["method_id", "control_level"], as_index=False)
        .agg(false_positive_context_rate=("false_positive_context_rate", "mean"))
    )
    pivot = data.pivot_table(
        index="method_id",
        columns="control_level",
        values="false_positive_context_rate",
        fill_value=0,
    ).reindex(selected_methods)
    pivot = pivot.reindex(columns=order)

    fig, ax = plt.subplots(figsize=(5.8, 3.8))
    image = ax.imshow(pivot.to_numpy(), aspect="auto", cmap="Reds", vmin=0, vmax=1)
    ax.set_yticks(np.arange(len(pivot)))
    ax.set_yticklabels([_method_label(v) for v in pivot.index])
    ax.set_xticks(np.arange(len(order)))
    ax.set_xticklabels(control_labels)
    ax.set_title("False context under null and confounded controls")
    for i in range(pivot.shape[0]):
        for j in range(pivot.shape[1]):
            value = pivot.iloc[i, j]
            ax.text(
                j,
                i,
                f"{value:.2f}",
                ha="center",
                va="center",
                fontsize=7,
                color="white" if value > 0.55 else COLORS["dark"],
            )
    colorbar = fig.colorbar(image, ax=ax, fraction=0.046, pad=0.02)
    colorbar.ax.tick_params(labelsize=7)
    fig.tight_layout()
    return _save_figure(fig, "null_control_false_context_heatmap", output_dir)


def build_failure_class_distribution(output_dir: Path) -> dict[str, str]:
    summary = _read_csv("cp_q4_failure_taxonomy", "failure_class_summary.csv")
    data = summary.sort_values("failure_count", ascending=True)
    fig, ax = plt.subplots(figsize=(6.0, 4.0))
    ax.barh(
        np.arange(len(data)),
        data["failure_count"],
        color=COLORS["blue"],
        edgecolor="white",
    )
    ax.set_yticks(np.arange(len(data)))
    ax.set_yticklabels([_failure_label(v) for v in data["failure_class"]])
    ax.set_xlabel("Failure rows")
    ax.set_title("Failure-class distribution")
    _annotate_hbars(ax, data["failure_count"], fmt="{:.0f}", pad=1.5)
    _style_axes(ax)
    fig.tight_layout()
    return _save_figure(fig, "failure_class_distribution", output_dir)


def build_dataset_task_failure_heatmap(output_dir: Path) -> dict[str, str]:
    matrix = _read_csv("cp_q4_failure_taxonomy", "dataset_task_failure_matrix.csv")
    pivot = matrix.pivot_table(
        index="dataset_id",
        columns="task_id",
        values="total_failure_count",
        aggfunc="sum",
        fill_value=0,
    )
    pivot = pivot.loc[pivot.sum(axis=1).sort_values(ascending=False).index]
    fig, ax = plt.subplots(figsize=(6.4, 4.8))
    image = ax.imshow(pivot.to_numpy(), aspect="auto", cmap="Blues")
    ax.set_yticks(np.arange(len(pivot.index)))
    ax.set_yticklabels([_dataset_label(v) for v in pivot.index])
    ax.set_xticks(np.arange(len(pivot.columns)))
    ax.set_xticklabels([_task_label(v) for v in pivot.columns])
    ax.set_title("Dataset-task failure matrix")
    max_value = pivot.to_numpy().max()
    for i in range(pivot.shape[0]):
        for j in range(pivot.shape[1]):
            value = pivot.iloc[i, j]
            if not value:
                continue
            ax.text(
                j,
                i,
                f"{int(value)}",
                ha="center",
                va="center",
                fontsize=7,
                color="white" if value > max_value * 0.50 else COLORS["dark"],
            )
    colorbar = fig.colorbar(image, ax=ax, fraction=0.046, pad=0.02)
    colorbar.ax.tick_params(labelsize=7)
    fig.tight_layout()
    return _save_figure(fig, "dataset_task_failure_heatmap", output_dir)


def build_contextgate_route_decisions(output_dir: Path) -> dict[str, str]:
    routes = _read_csv("cp_q5_contextgate_decisions", "contextgate_route_summary.csv")
    route_colors = {
        "expression_only": COLORS["blue"],
        "abstain_uncertain": COLORS["orange"],
        "positive_control_only": COLORS["green"],
        "context_allowed": COLORS["purple"],
    }
    data = routes.sort_values("decision_count", ascending=True)
    fig, ax = plt.subplots(figsize=(5.4, 3.3))
    ax.barh(
        np.arange(len(data)),
        data["decision_count"],
        color=[route_colors.get(v, COLORS["gray"]) for v in data["route_label"]],
        edgecolor="white",
    )
    ax.set_yticks(np.arange(len(data)))
    ax.set_yticklabels(
        [str(ROUTE_LABELS.get(v, v)).rstrip(" -") for v in data["route_label"]]
    )
    ax.set_xlabel("Decision count")
    ax.set_title("Transparent ContextGate decisions")
    _annotate_hbars(ax, data["decision_count"], fmt="{:.0f}", pad=0.6)
    _style_axes(ax)
    fig.tight_layout()
    return _save_figure(fig, "contextgate_route_decisions", output_dir)


def _build_no_harm_dumbbell(
    output_dir: Path,
    *,
    analysis_domain: str,
    stem: str,
    title: str,
) -> dict[str, str]:
    no_harm = _read_csv("cp_q5_contextgate_decisions", "contextgate_no_harm.csv")
    data = no_harm[no_harm["analysis_domain"] == analysis_domain].copy()
    data = data.sort_values("comparator_false_positive_context_rate")
    labels = [_method_label(v) for v in data["comparator_method_id"]]
    y = np.arange(len(data))

    fig, ax = plt.subplots(figsize=(5.7, 3.6))
    for idx, row in enumerate(data.itertuples(index=False)):
        ax.plot(
            [
                row.contextgate_false_positive_context_rate,
                row.comparator_false_positive_context_rate,
            ],
            [idx, idx],
            color="#ADB5BD",
            linewidth=1.6,
            zorder=1,
        )
    ax.scatter(
        data["contextgate_false_positive_context_rate"],
        y,
        color=COLORS["teal"],
        s=46,
        label="ContextGate",
        zorder=2,
    )
    ax.scatter(
        data["comparator_false_positive_context_rate"],
        y,
        color=COLORS["red"],
        s=46,
        label="Comparator",
        zorder=2,
    )
    ax.set_yticks(y)
    ax.set_yticklabels(labels)
    ax.set_xlim(-0.02, 1.05)
    ax.set_xlabel("False context rate")
    ax.set_title(title)
    ax.legend(frameon=False, fontsize=8, loc="lower right")
    _style_axes(ax)
    fig.tight_layout()
    return _save_figure(fig, stem, output_dir)


def build_registered_no_harm_dumbbell(output_dir: Path) -> dict[str, str]:
    return _build_no_harm_dumbbell(
        output_dir,
        analysis_domain="registered_context_utility",
        stem="registered_no_harm_dumbbell",
        title="Registered no-harm audit",
    )


def build_synthetic_no_harm_dumbbell(output_dir: Path) -> dict[str, str]:
    return _build_no_harm_dumbbell(
        output_dir,
        analysis_domain="positive_null_control_ladder",
        stem="synthetic_no_harm_dumbbell",
        title="Synthetic/null no-harm audit",
    )


def _stress_rows() -> pd.DataFrame:
    stress_files = [
        "leave_one_out_stress.csv",
        "threshold_sensitivity.csv",
        "seed_sweep.csv",
        "control_ablation.csv",
        "positive_control_ablation.csv",
        "contextgate_reason_ablation.csv",
        "compute_sensitivity.csv",
    ]
    return pd.concat(
        [
            _read_csv("cp_q7_robustness_stress", filename)
            for filename in stress_files
        ],
        ignore_index=True,
    )


def build_stress_family_outcomes(output_dir: Path) -> dict[str, str]:
    stress_rows = _stress_rows()
    stress_rows["downgraded"] = (
        stress_rows["claim_downgrade"].astype(str).str.lower() != "none"
    )
    stress_rows["passed"] = _as_bool_series(stress_rows["passed"])
    stress_rows["passed_without_downgrade"] = (
        stress_rows["passed"] & ~stress_rows["downgraded"]
    )
    stress_rows["failed_without_downgrade"] = (
        ~stress_rows["passed"] & ~stress_rows["downgraded"]
    )
    summary = (
        stress_rows.groupby("stress_family", as_index=False)
        .agg(
            passed_without_downgrade=("passed_without_downgrade", "sum"),
            downgraded=("downgraded", "sum"),
            failed_without_downgrade=("failed_without_downgrade", "sum"),
            stress_rows=("stress_id", "count"),
        )
        .sort_values("stress_rows", ascending=True)
    )
    fig, ax = plt.subplots(figsize=(6.0, 4.1))
    y = np.arange(len(summary))
    left = np.zeros(len(summary))
    stacks = [
        ("Passed", "passed_without_downgrade", COLORS["green"]),
        ("Downgraded", "downgraded", COLORS["orange"]),
        ("Failed no downgrade", "failed_without_downgrade", COLORS["red"]),
    ]
    for label, column, color in stacks:
        values = summary[column].to_numpy(dtype=float)
        segment_left = left.copy()
        ax.barh(
            y,
            values,
            left=left,
            color=color,
            edgecolor="white",
            linewidth=0.5,
            label=label,
        )
        if column != "passed_without_downgrade":
            for idx, value in enumerate(values):
                if value <= 0:
                    continue
                if value >= 3:
                    ax.text(
                        segment_left[idx] + value / 2,
                        idx,
                        str(int(value)),
                        ha="center",
                        va="center",
                        fontsize=6.5,
                        color=COLORS["dark"],
                    )
                else:
                    ax.text(
                        segment_left[idx] + value + 0.25,
                        idx,
                        str(int(value)),
                        ha="left",
                        va="center",
                        fontsize=6.5,
                        color=COLORS["dark"],
                    )
        left += values
    for idx, total in enumerate(summary["stress_rows"]):
        ax.text(
            float(total) + 0.5,
            idx,
            str(int(total)),
            va="center",
            fontsize=7,
            color=COLORS["dark"],
        )
    ax.set_yticks(y)
    ax.set_yticklabels([_stress_label(v) for v in summary["stress_family"]])
    ax.set_xlabel("Stress rows")
    ax.set_title("Stress-family outcomes")
    ax.legend(frameon=False, fontsize=7, loc="lower right")
    _style_axes(ax)
    fig.tight_layout()
    return _save_figure(fig, "stress_family_outcomes", output_dir)


def build_claim_survival_audit(output_dir: Path) -> dict[str, str]:
    claim_audit = _read_csv("cp_q7_robustness_stress", "claim_survival_audit.csv")
    counts = claim_audit["claim_status"].value_counts().reindex(
        ["survives", "downgraded"],
        fill_value=0,
    )
    fig, ax = plt.subplots(figsize=(4.2, 3.5))
    ax.bar(
        ["Survives", "Downgraded"],
        counts.values,
        color=[COLORS["green"], COLORS["orange"]],
        edgecolor="white",
    )
    ax.set_ylabel("Claims")
    ax.set_title("Claim survival audit")
    _annotate_vbars(ax, counts.values, fmt="{:.0f}")
    _style_axes(ax, xgrid=False, ygrid=True)
    fig.tight_layout()
    return _save_figure(fig, "claim_survival_audit", output_dir)


def build_threshold_leave_one_out_checks(output_dir: Path) -> dict[str, str]:
    threshold = _read_csv("cp_q7_robustness_stress", "threshold_sensitivity.csv")
    leave_one = _read_csv("cp_q7_robustness_stress", "leave_one_out_stress.csv")
    threshold_passed = _as_bool_series(threshold["passed"])
    leave_one_passed = _as_bool_series(leave_one["passed"])
    threshold_counts = threshold_passed.value_counts().reindex(
        [True, False],
        fill_value=0,
    )
    leave_one_pass = int(leave_one_passed.sum())
    leave_one_fail = int((~leave_one_passed).sum())
    categories = [
        "Threshold\npasses",
        "Threshold\ndowngrades",
        "Leave-one-out\npasses",
        "Leave-one-out\nfails",
    ]
    values = [
        int(threshold_counts.loc[True]),
        int(threshold_counts.loc[False]),
        leave_one_pass,
        leave_one_fail,
    ]
    colors = [COLORS["green"], COLORS["orange"], COLORS["green"], COLORS["red"]]
    fig, ax = plt.subplots(figsize=(5.0, 3.6))
    ax.bar(categories, values, color=colors, edgecolor="white")
    ax.set_ylabel("Stress rows")
    ax.set_title("Threshold and leave-one-out checks")
    _annotate_vbars(ax, values, fmt="{:.0f}")
    _style_axes(ax, xgrid=False, ygrid=True)
    fig.tight_layout()
    return _save_figure(fig, "threshold_leave_one_out_checks", output_dir)


def build_all_figures(output_dir: Path) -> dict[str, dict[str, str]]:
    figure_builders = {
        "pipeline_architecture": build_pipeline_architecture,
        "scale_contract_coverage": build_scale_contract_coverage,
        "full_benchmark_metric_profile": build_full_benchmark_metric_profile,
        "method_utility_ranking": build_method_utility_ranking,
        "method_oracle_regret": build_method_oracle_regret,
        "positive_control_recovery": build_positive_control_recovery,
        "null_control_false_context_heatmap": build_null_control_heatmap,
        "failure_class_distribution": build_failure_class_distribution,
        "dataset_task_failure_heatmap": build_dataset_task_failure_heatmap,
        "contextgate_route_decisions": build_contextgate_route_decisions,
        "stress_family_outcomes": build_stress_family_outcomes,
    }
    outputs: dict[str, dict[str, str]] = {}
    for name, builder in figure_builders.items():
        outputs[name] = builder(output_dir)
    manifest_path = output_dir / "publication_figure_manifest.json"
    manifest_path.write_text(
        json.dumps(outputs, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    table_only_path = output_dir / "table_or_text_only_evidence.json"
    table_only_path.write_text(
        json.dumps(TABLE_ONLY_RECOMMENDATIONS, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    return outputs


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help="Directory for individual manuscript figure exports.",
    )
    args = parser.parse_args()
    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 9,
            "axes.titlesize": 10,
            "axes.labelsize": 9,
            "figure.dpi": 120,
            "savefig.dpi": 600,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
        }
    )
    outputs = build_all_figures(args.output_dir)
    print(json.dumps(outputs, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
