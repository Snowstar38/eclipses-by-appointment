"""Rebuild the summary figures from host-stars.csv: python figures/plot-summary.py (Python 3, Matplotlib)."""
import csv
import math
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
SEARCHES = {'SPOC two-minute threshold-crossing events not promoted to objects of interest': ('SPOC two-minute TCEs', '#0072B2'), 'TESS-SPOC full-frame threshold-crossing events not promoted to objects of interest': ('TESS-SPOC full-frame TCEs', '#E69F00'), 'Spectroscopic binaries from ground-based surveys (LAMOST, APOGEE, GALAH, RAVE, Gaia-ESO)': ('Ground-survey spectroscopic binaries', '#CC79A7')}   # search label -> (short name, colour); Okabe-Ito colours, safe for colour-blind readers
NF = "no earlier eclipse candidate found"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10, "axes.spines.top": False,
                     "axes.spines.right": False, "axes.edgecolor": "#555555", "axes.labelcolor": "#222222",
                     "xtick.color": "#444444", "ytick.color": "#444444"})


def rows():
    with (HERE.parent / "host-stars.csv").open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def hist(rows, column, fname, xlabel, title, lo, hi):
    edges = [10 ** (math.log10(lo) + i * (math.log10(hi) - math.log10(lo)) / 30) for i in range(31)]
    fig, axes = plt.subplots(len(SEARCHES), 1, figsize=(7.5, 6.2), sharex=True, dpi=150)
    for ax, (label, (short, colour)) in zip(axes, SEARCHES.items()):
        vals = [float(r[column]) for r in rows if r["search"] == label and r[column]]
        ax.hist(vals, bins=edges, color=colour, edgecolor="white", linewidth=0.8)
        ax.set_xscale("log")
        ticks = [t for t in (0.1, 0.3, 1, 3, 10, 30, 100, 300, 1000) if lo <= t <= hi]
        ax.set_xticks(ticks, [f"{t:g}" for t in ticks])
        ax.minorticks_off()
        ax.set_ylabel("systems")
        ax.grid(axis="y", color="#e5e5e5", linewidth=0.6)
        ax.set_axisbelow(True)
        ax.set_ylim(0, ax.get_ylim()[1] * 1.3)
        ax.text(0.01, 0.97, f"{short} (n = {len(vals)})", transform=ax.transAxes, ha="left", va="top",
                color="#222222")
    axes[-1].set_xlabel(xlabel)
    fig.suptitle(title, x=0.01, ha="left", fontsize=11.5)
    fig.tight_layout()
    fig.savefig(HERE / fname, metadata={"Software": "Matplotlib"})
    plt.close(fig)


def split(rows):
    labels = list(SEARCHES)
    parts = [("confirmed", NF, "confirmed, no earlier candidate", 1.0, None),
             ("probable", NF, "probable, no earlier candidate", 0.45, None),
             ("confirmed", None, "confirmed, prior machine candidate", 1.0, "///"),
             ("probable", None, "probable, prior machine candidate", 0.45, "///")]
    fig, ax = plt.subplots(figsize=(8.5, 3.4), dpi=150)
    left = [0] * len(labels)
    for tier, group, name, alpha, hatch in parts:
        n = [sum(r["search"] == l and r["physical_tier"] == tier and ((r["publication_group"] == NF) == (group == NF))
                 for r in rows) for l in labels]
        for i, l in enumerate(labels):
            ax.barh(i, n[i], left=left[i], color=SEARCHES[l][1], alpha=alpha, hatch=hatch,
                    edgecolor="white", linewidth=1.5)
            if n[i] >= 10:
                ax.text(left[i] + n[i] / 2, i, str(n[i]), ha="center", va="center", fontsize=8.5, color="#111111")
        ax.barh(-9, 0, color="#777777", alpha=alpha, hatch=hatch, edgecolor="white", label=name)
        left = [a + b for a, b in zip(left, n)]
    for i, total in enumerate(left):
        ax.text(total + 4, i, f"{total}", va="center", fontsize=9, color="#222222")
    ax.set_yticks(range(len(labels)), [SEARCHES[l][0] for l in labels])
    ax.set_ylim(-0.6, len(labels) - 0.4)
    ax.invert_yaxis()
    ax.set_xlabel("systems added")
    ax.set_xlim(0, max(left) * 1.12)
    ax.legend(frameon=False, fontsize=8.5, ncol=2, loc="upper left", bbox_to_anchor=(0.0, -0.22))
    ax.set_title("Systems added, by search, tier and earlier eclipse evidence", loc="left", fontsize=11.5)
    fig.savefig(HERE / "flag-split.png", metadata={"Software": "Matplotlib"}, bbox_inches="tight", pad_inches=0.15)
    plt.close(fig)


if __name__ == "__main__":
    r = rows()
    hist(r, "adopted_period_days", "periods.png", "adopted period (days, log scale)",
         "Adopted periods of the added systems", 0.15, 200)
    hist(r, "depth_ppt", "depths.png", "primary eclipse depth (parts per thousand, log scale)",
         "Primary eclipse depths of the added systems", 0.3, 1000)
    split(r)
    print("wrote periods.png, depths.png, flag-split.png")
