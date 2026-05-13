"""Build H7 Overleaf-ready data figures for ContextGate-Bench.

This builder intentionally excludes Figure 1 and the graphical abstract. It
redraws only the seven manuscript data figures used by the current Overleaf
draft, preserving original CP-Q denominators while adding clearly labeled
additive hardening evidence where needed.
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
REPORT_ROOT = PROJECT_ROOT / "results" / "reports"
HARDENING_ROOT = PROJECT_ROOT / "manuscript" / "reviewer_hardening"
DEFAULT_OUTPUT_DIR = (
    PROJECT_ROOT / "manuscript" / "h7_overleaf_artifacts" / "figures" / "singles"
)
SOURCE_DATE_EPOCH = "1778716800"  # 2026-05-14T00:00:00Z.

COLORS = {
    "blue": "#2F5D8C",
    "teal": "#2A9D8F",
    "green": "#4C956C",
    "orange": "#D98C3A",
    "red": "#B94A48",
    "purple": "#6A4C93",
    "gray": "#6C757D",
    "light": "#F5F7FA",
    "dark": "#1F2933",
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

ROUTE_COLORS = {
    "expression_only": COLORS["blue"],
    "abstain_uncertain": COLORS["orange"],
    "positive_control_only": COLORS["green"],
    "context_allowed": COLORS["purple"],
}

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

METRIC_LABELS = {
    "no_harm_rate": "No-harm\nhigher better",
    "false_positive_context_rate": "False context\nlower better",
    "abstention_rate": "Abstention\nlower better",
    "regret_against_oracle": "Oracle regret\nlower better",
    "heldout_replication_rate": "Held-out\nhigher better",
}

METRIC_ORDER = [
    "no_harm_rate",
    "false_positive_context_rate",
    "abstention_rate",
    "regret_against_oracle",
    "heldout_replication_rate",
]

LOWER_IS_BETTER = {
    "false_positive_context_rate",
    "abstention_rate",
    "regret_against_oracle",
}


def _read_report(*parts: str) -> pd.DataFrame:
    path = REPORT_ROOT.joinpath(*parts)
    if not path.exists():
        raise FileNotFoundError(path)
    return pd.read_csv(path)


def _read_hardening(*parts: str) -> pd.DataFrame:
    path = HARDENING_ROOT.joinpath(*parts)
    if not path.exists():
        raise FileNotFoundError(path)
    return pd.read_csv(path)


def _method_label(method_id: object) -> str:
    return METHOD_LABELS.get(str(method_id), str(method_id).replace("_", " "))


def _failure_label(failure_class: object) -> str:
    return FAILURE_LABELS.get(str(failure_class), str(failure_class).replace("_", " "))


def _stress_label(stress_family: object) -> str:
    return STRESS_LABELS.get(str(stress_family), str(stress_family).replace("_", " "))


def _rung_label(rung_id: object) -> str:
    text = str(rung_id).replace("_", " ")
    replacements = {
        "k3 linear contact signal": "k=3 contact",
        "k5 linear reference signal": "k=5 reference",
        "k10 linear diluted signal": "k=10 diluted",
        "radius40 contact signal": "40 um radius",
        "radius120 paracrine signal": "120 um radius",
        "distance decay short range signal": "Distance decay",
        "threshold gated sender signal": "Threshold gated",
        "receiver state specific signal": "Receiver-state",
        "rare niche local strong signal": "Rare niche",
        "null no context scale control": "Null control",
        "fov confounded positive trap": "FOV confounded trap",
    }
    return replacements.get(text, text[:28])


def _clean_axes(ax: plt.Axes) -> None:
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#B8C0CC")
    ax.spines["bottom"].set_color("#B8C0CC")
    ax.tick_params(colors=COLORS["dark"], labelsize=8)
    ax.set_axisbelow(True)


def _panel_label(ax: plt.Axes, label: str) -> None:
    ax.text(
        -0.08,
        1.06,
        label,
        transform=ax.transAxes,
        fontsize=11,
        fontweight="bold",
        ha="left",
        va="top",
        color=COLORS["dark"],
    )


def _annotate_hbars(
    ax: plt.Axes,
    values: pd.Series | np.ndarray,
    *,
    pad: float,
    fmt: str = "{:.2f}",
) -> None:
    for patch, value in zip(ax.patches, values, strict=False):
        ax.text(
            patch.get_width() + pad,
            patch.get_y() + patch.get_height() / 2,
            fmt.format(float(value)),
            ha="left",
            va="center",
            fontsize=7,
            color=COLORS["dark"],
        )


def _save(fig: plt.Figure, stem: str, output_dir: Path) -> dict[str, str]:
    output_dir.mkdir(parents=True, exist_ok=True)
    os.environ.setdefault("SOURCE_DATE_EPOCH", SOURCE_DATE_EPOCH)
    outputs = {
        "pdf": output_dir / f"{stem}.pdf",
        "png": output_dir / f"{stem}.png",
        "eps": output_dir / f"{stem}.eps",
    }
    for suffix, path in outputs.items():
        if suffix == "png":
            fig.savefig(path, dpi=600, bbox_inches="tight", facecolor="white")
        else:
            fig.savefig(path, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return {key: str(value) for key, value in outputs.items()}


def build_full_benchmark_metric_profile(output_dir: Path) -> dict[str, str]:
    metrics = _read_report("cp_q6_benchmark_matrix", "aggregate_metrics.csv")
    selected = metrics[
        (metrics["benchmark_tier"] == "q1")
        & metrics["metric_name"].isin(METRIC_ORDER)
    ].copy()
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
    pivot = selected.pivot_table(
        index="method_id",
        columns="metric_name",
        values="mean_metric_value",
        aggfunc="mean",
    ).reindex(method_order)
    pivot = pivot.dropna(how="all").reindex(columns=METRIC_ORDER)

    desirability = pivot.copy()
    for metric in desirability.columns:
        if metric in LOWER_IS_BETTER:
            desirability[metric] = 1.0 - desirability[metric]

    fig, ax = plt.subplots(figsize=(6.9, 4.2))
    image = ax.imshow(
        desirability.fillna(0).to_numpy(),
        aspect="auto",
        cmap="viridis",
        vmin=0,
        vmax=1,
    )
    ax.set_title("Full-benchmark metric profile", pad=10)
    ax.set_yticks(np.arange(len(pivot.index)))
    ax.set_yticklabels([_method_label(v) for v in pivot.index])
    ax.set_xticks(np.arange(len(METRIC_ORDER)))
    ax.set_xticklabels([METRIC_LABELS[v] for v in METRIC_ORDER], fontsize=7)
    ax.tick_params(length=0)
    for i in range(pivot.shape[0]):
        for j in range(pivot.shape[1]):
            value = pivot.iloc[i, j]
            if pd.isna(value):
                continue
            display_value = desirability.iloc[i, j]
            color = "white" if float(display_value) < 0.45 else COLORS["dark"]
            ax.text(j, i, f"{value:.2f}", ha="center", va="center", fontsize=7, color=color)
    colorbar = fig.colorbar(image, ax=ax, fraction=0.046, pad=0.02)
    colorbar.set_label("Visual desirability", fontsize=7)
    colorbar.ax.tick_params(labelsize=7)
    fig.tight_layout()
    return _save(fig, "full_benchmark_metric_profile", output_dir)


def build_method_oracle_regret(output_dir: Path) -> dict[str, str]:
    metrics = _read_report("cp_q2_method_comparison", "method_metrics.csv")
    methods = [
        "always_true_neighbor_mean",
        "ligand_receptor_pathway_heuristic",
        "cellpack_packed_context_tiny",
        "expression_only_linear",
        "contextgate_transparent_router",
        "spatial_statistics_heuristic",
    ]
    data = metrics[metrics["method_id"].isin(methods)].copy()
    data["method_label"] = data["method_id"].map(_method_label)
    data = data.sort_values(["mean_regret", "method_label"], ascending=[False, True])

    fig, ax = plt.subplots(figsize=(5.9, 3.8))
    y = np.arange(len(data))
    ax.barh(y, data["mean_regret"], color=COLORS["orange"], edgecolor="white")
    ax.set_yticks(y)
    ax.set_yticklabels(data["method_label"])
    ax.set_xlim(0, 0.95)
    ax.set_xlabel("Mean regret against oracle")
    ax.set_title("Method-comparison oracle regret", pad=10)
    _annotate_hbars(ax, data["mean_regret"], pad=0.015, fmt="{:.2f}")
    ax.invert_yaxis()
    _clean_axes(ax)
    fig.tight_layout()
    return _save(fig, "method_oracle_regret", output_dir)


def build_positive_control_recovery(output_dir: Path) -> dict[str, str]:
    recovery = _read_report("cp_q3_positive_null_control_ladder", "recovery_curve.csv")
    expanded = _read_hardening(
        "h6_expanded_synthetic_ladder",
        "expanded_ladder_scale_sensitivity.csv",
    )
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

    fig, axes = plt.subplots(1, 2, figsize=(10.6, 4.3), gridspec_kw={"width_ratios": [1.12, 1.0]})

    ax = axes[0]
    for method_id, group in rec.groupby("method_id", sort=False):
        ax.plot(
            group["injected_signal_strength"],
            group["sensitivity"],
            marker="o",
            linewidth=2.0,
            color=method_colors[method_id],
            label=_method_label(method_id),
        )
    for signal_strength, label in {0.55: "Weak/noisy", 0.75: "Localized", 1.0: "Strong"}.items():
        ax.axvline(signal_strength, color="#D4DAE2", linewidth=0.8, linestyle=":")
        ax.text(signal_strength, 1.035, label, ha="center", va="bottom", fontsize=7)
    ax.set_xlabel("Injected signal coefficient s")
    ax.set_ylabel("Sensitivity")
    ax.set_xlim(0.50, 1.03)
    ax.set_ylim(-0.03, 1.08)
    ax.set_xticks([0.55, 0.75, 1.00])
    ax.set_title("Original CP-Q3 ladder")
    ax.legend(frameon=False, fontsize=6.8, loc="lower right")
    _clean_axes(ax)
    _panel_label(ax, "A")

    ax = axes[1]
    expanded = expanded.copy()
    expanded["display_score"] = np.where(
        expanded["route"].isin(["expression_only", "abstain_uncertain"]),
        expanded["specificity"],
        expanded["sensitivity"],
    )
    expanded["label"] = expanded["rung_id"].map(_rung_label)
    expanded = expanded.sort_values(["route", "display_score"], ascending=[True, True])
    y = np.arange(len(expanded))
    colors = [ROUTE_COLORS.get(route, COLORS["gray"]) for route in expanded["route"]]
    ax.barh(y, expanded["display_score"], color=colors, edgecolor="white")
    ax.set_yticks(y)
    ax.set_yticklabels(expanded["label"], fontsize=7)
    ax.set_xlim(0, 1.08)
    ax.set_xlabel("Sensitivity or specificity")
    ax.set_title("H6 expanded ladder: ContextGate")
    for idx, row in enumerate(expanded.itertuples(index=False)):
        route_label = ROUTE_LABELS.get(row.route, row.route)
        ax.text(
            float(row.display_score) + 0.018,
            idx,
            f"{row.display_score:.2f} ({route_label})",
            va="center",
            fontsize=6.2,
            color=COLORS["dark"],
        )
    _clean_axes(ax)
    _panel_label(ax, "B")
    fig.tight_layout(w_pad=1.4)
    return _save(fig, "positive_control_recovery", output_dir)


def build_null_control_false_context_heatmap(output_dir: Path) -> dict[str, str]:
    false_positive = _read_report(
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
    control_order = [
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
    pivot = pivot.reindex(columns=control_order)

    fig, ax = plt.subplots(figsize=(5.9, 3.6))
    image = ax.imshow(pivot.to_numpy(), aspect="auto", cmap="Reds", vmin=0, vmax=1)
    ax.set_title("False context under null and confounded controls", pad=10)
    ax.set_yticks(np.arange(len(pivot.index)))
    ax.set_yticklabels([_method_label(v) for v in pivot.index])
    ax.set_xticks(np.arange(len(control_labels)))
    ax.set_xticklabels(control_labels)
    ax.tick_params(length=0)
    for i in range(pivot.shape[0]):
        for j in range(pivot.shape[1]):
            value = float(pivot.iloc[i, j])
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
    return _save(fig, "null_control_false_context_heatmap", output_dir)


def build_failure_class_distribution(output_dir: Path) -> dict[str, str]:
    summary = _read_report("cp_q4_failure_taxonomy", "failure_class_summary.csv")
    data = summary.sort_values("failure_count", ascending=True)
    fig, ax = plt.subplots(figsize=(6.2, 3.9))
    y = np.arange(len(data))
    ax.barh(y, data["failure_count"], color=COLORS["blue"], edgecolor="white")
    ax.set_yticks(y)
    ax.set_yticklabels([_failure_label(v) for v in data["failure_class"]])
    ax.set_xlabel("Failure taxonomy rows")
    ax.set_title("Failure-class distribution", pad=10)
    _annotate_hbars(ax, data["failure_count"], pad=1.7, fmt="{:.0f}")
    ax.set_xlim(0, max(data["failure_count"]) * 1.15)
    _clean_axes(ax)
    fig.tight_layout()
    return _save(fig, "failure_class_distribution", output_dir)


def build_contextgate_route_decisions(output_dir: Path) -> dict[str, str]:
    original = _read_report(
        "cp_q5_contextgate_decisions",
        "contextgate_route_summary.csv",
    )
    h5d_routes = _read_hardening(
        "h5d_gse311609_marker_replay",
        "gse311609_marker_replay_route_decisions.csv",
    )
    h65a_summary = _read_hardening(
        "h6_5a_nsclc_cd274_section_expansion",
        "nsclc_cd274_replication_summary.csv",
    ).iloc[0]
    h65b = pd.read_json(
        HARDENING_ROOT
        / "h6_5b_single_adapter_probe"
        / "single_adapter_probe_summary.json",
        typ="series",
    )

    fig, axes = plt.subplots(1, 2, figsize=(10.2, 3.8), gridspec_kw={"width_ratios": [1.0, 1.2]})

    ax = axes[0]
    route_order = [
        "context_allowed",
        "expression_only",
        "positive_control_only",
        "abstain_uncertain",
    ]
    original_counts = (
        original.set_index("route_label")["decision_count"]
        .reindex(route_order, fill_value=0)
        .reset_index()
    )
    y = np.arange(len(original_counts))
    ax.barh(
        y,
        original_counts["decision_count"],
        color=[ROUTE_COLORS.get(v, COLORS["gray"]) for v in original_counts["route_label"]],
        edgecolor="white",
    )
    ax.set_yticks(y)
    ax.set_yticklabels([ROUTE_LABELS.get(v, v) for v in original_counts["route_label"]])
    ax.set_xlabel("Decision count")
    ax.set_title("Original CP-Q route matrix")
    ax.set_xlim(0, max(original_counts["decision_count"]) * 1.18)
    _annotate_hbars(ax, original_counts["decision_count"], pad=0.7, fmt="{:.0f}")
    _clean_axes(ax)
    _panel_label(ax, "A")

    ax = axes[1]
    h5d_counts = (
        h5d_routes["observed_route"].value_counts()
        .rename_axis("route")
        .reset_index(name="count")
    )
    additive = pd.DataFrame(
        [
            {
                "label": "H5D context-allowed route",
                "count": int(h5d_counts[h5d_counts["route"] == "context_allowed"]["count"].sum()),
                "color": COLORS["purple"],
            },
            {
                "label": "H5D abstained route",
                "count": int(h5d_counts[h5d_counts["route"] == "abstain_uncertain"]["count"].sum()),
                "color": COLORS["orange"],
            },
            {
                "label": "H6.5A NSCLC effect-gate sections",
                "count": int(h65a_summary["effect_gate_section_count"]),
                "color": COLORS["teal"],
            },
            {
                "label": "H6.5B adapter-confirmed rows",
                "count": int(h65b["claim_eligible_adapter_count"]),
                "color": COLORS["gray"],
            },
        ]
    )
    additive = additive.iloc[::-1].reset_index(drop=True)
    y = np.arange(len(additive))
    ax.barh(y, additive["count"], color=additive["color"], edgecolor="white")
    ax.set_yticks(y)
    ax.set_yticklabels(additive["label"], fontsize=7.4)
    ax.set_xlabel("Count")
    ax.set_title("Additive hardening evidence")
    ax.set_xlim(0, max(additive["count"].max() * 1.22, 2))
    for patch, value in zip(ax.patches, additive["count"], strict=False):
        ax.text(
            patch.get_width() + 0.22,
            patch.get_y() + patch.get_height() / 2,
            str(int(value)),
            ha="left",
            va="center",
            fontsize=7,
            color=COLORS["dark"],
        )
    ci_low = float(h65a_summary["bootstrap_ci_low"])
    ci_high = float(h65a_summary["bootstrap_ci_high"])
    ax.text(
        0.02,
        -0.28,
        f"NSCLC CD274 bootstrap CI: [{ci_low:.6f}, {ci_high:.6f}]\nFull 41-section validation and mature-adapter confirmation are not claimed.",
        transform=ax.transAxes,
        ha="left",
        va="top",
        fontsize=6.6,
        color=COLORS["dark"],
    )
    _clean_axes(ax)
    _panel_label(ax, "B")
    fig.tight_layout(w_pad=1.5)
    return _save(fig, "contextgate_route_decisions", output_dir)


def build_stress_family_outcomes(output_dir: Path) -> dict[str, str]:
    stress_files = [
        "leave_one_out_stress.csv",
        "threshold_sensitivity.csv",
        "seed_sweep.csv",
        "control_ablation.csv",
        "positive_control_ablation.csv",
        "contextgate_reason_ablation.csv",
        "compute_sensitivity.csv",
    ]
    stress_rows = pd.concat(
        [_read_report("cp_q7_robustness_stress", filename) for filename in stress_files],
        ignore_index=True,
    )
    stress_rows["downgraded"] = (
        stress_rows["claim_downgrade"].astype(str).str.lower() != "none"
    )
    passed = stress_rows["passed"].astype(str).str.lower().isin({"true", "1", "yes"})
    stress_rows["passed_without_downgrade"] = passed & ~stress_rows["downgraded"]
    stress_rows["failed_without_downgrade"] = ~passed & ~stress_rows["downgraded"]
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

    fig, ax = plt.subplots(figsize=(6.4, 4.0))
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
        ax.barh(y, values, left=left, color=color, edgecolor="white", linewidth=0.5, label=label)
        for idx, value in enumerate(values):
            if value <= 0 or column == "passed_without_downgrade":
                continue
            x = segment_left[idx] + value / 2 if value >= 3 else segment_left[idx] + value + 0.35
            ax.text(x, idx, str(int(value)), ha="center" if value >= 3 else "left", va="center", fontsize=7)
        left += values
    for idx, total in enumerate(summary["stress_rows"]):
        ax.text(float(total) + 0.65, idx, str(int(total)), va="center", fontsize=7)
    ax.set_yticks(y)
    ax.set_yticklabels([_stress_label(v) for v in summary["stress_family"]])
    ax.set_xlabel("Stress rows")
    ax.set_title("Robustness and sensitivity outcomes", pad=10)
    ax.set_xlim(0, max(summary["stress_rows"]) * 1.18)
    ax.legend(frameon=False, fontsize=7, loc="lower right")
    _clean_axes(ax)
    fig.tight_layout()
    return _save(fig, "stress_family_outcomes", output_dir)


def build_all(output_dir: Path) -> dict[str, dict[str, str]]:
    builders = {
        "full_benchmark_metric_profile": build_full_benchmark_metric_profile,
        "method_oracle_regret": build_method_oracle_regret,
        "positive_control_recovery": build_positive_control_recovery,
        "null_control_false_context_heatmap": build_null_control_false_context_heatmap,
        "failure_class_distribution": build_failure_class_distribution,
        "contextgate_route_decisions": build_contextgate_route_decisions,
        "stress_family_outcomes": build_stress_family_outcomes,
    }
    outputs = {name: builder(output_dir) for name, builder in builders.items()}
    (output_dir / "h7_data_figure_manifest.json").write_text(
        json.dumps(outputs, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    action_rows = [
        {
            "figure_file": "full_benchmark_metric_profile.pdf",
            "decision": "regenerate_polished",
            "reason": "Original CP-Q full-tier metric profile remains valid; redraw with cleaner labels and journal styling.",
        },
        {
            "figure_file": "method_oracle_regret.pdf",
            "decision": "regenerate_polished",
            "reason": "Original CP-Q2 regret values remain valid; redraw without nonessential gridlines.",
        },
        {
            "figure_file": "positive_control_recovery.pdf",
            "decision": "regenerate_with_h6_panel",
            "reason": "Adds H6 expanded synthetic ladder while preserving original CP-Q3 ladder panel.",
        },
        {
            "figure_file": "null_control_false_context_heatmap.pdf",
            "decision": "regenerate_polished",
            "reason": "Original null-control denominator remains valid; redraw for visual consistency.",
        },
        {
            "figure_file": "failure_class_distribution.pdf",
            "decision": "regenerate_polished",
            "reason": "Original failure taxonomy remains valid; redraw without gridlines.",
        },
        {
            "figure_file": "contextgate_route_decisions.pdf",
            "decision": "regenerate_with_hardening_panel",
            "reason": "Separates original CP-Q route counts from additive H5D/H6.5A/H6.5B evidence.",
        },
        {
            "figure_file": "stress_family_outcomes.pdf",
            "decision": "regenerate_polished",
            "reason": "Original CP-Q7 stress accounting remains valid; redraw without nonessential gridlines.",
        },
    ]
    pd.DataFrame(action_rows).to_csv(output_dir / "h7_data_figure_action_table.csv", index=False)
    return outputs


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args()
    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 8.5,
            "axes.titlesize": 10,
            "axes.labelsize": 8.5,
            "figure.dpi": 140,
            "savefig.dpi": 600,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
        }
    )
    outputs = build_all(args.output_dir)
    print(json.dumps(outputs, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
