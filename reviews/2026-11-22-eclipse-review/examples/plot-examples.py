"""Rebuild reduced diagnostic figures from the released CSV and JSON products."""
import argparse
import csv
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).resolve().parent


def table(name):
    with (HERE / name).open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def long_clock(directory):
    profiles = table("TIC-34691042-profiles.csv")
    events = table("TIC-34691042-events.csv")
    images = json.loads((HERE / "TIC-34691042-differences.json").read_text())
    fig, axes = plt.subplots(2, 3, figsize=(12, 6), constrained_layout=True)
    for axis_pair, event, image in zip(axes.T, events, images, strict=True):
        profile, pixels = axis_pair
        sector = event["sector"]
        samples = [r for r in profiles if r["sector"] == sector]
        profile.scatter([float(r["hours"]) for r in samples],
                        [float(r["sap_relative_ppt"]) for r in samples], s=5, alpha=.7)
        profile.axhline(0, color="0.5", linewidth=.6)
        profile.set(title=f"Sector {sector}", xlabel="Hours from eclipse", ylabel="SAP (ppt)")
        loss = np.asarray(image["median_flux_loss"])
        limit = np.max(np.abs(loss))
        pixels.imshow(loss, origin="lower", cmap="RdBu_r", vmin=-limit, vmax=limit)
        pixels.scatter(*image["target_xy"], color="black", marker="+", s=100, label="TIC position")
        pixels.scatter(*image["deficit_xy"], facecolors="none", edgecolors="lime",
                       marker="o", s=75, label="Loss centroid")
        pixels.set(xlabel="TESS pixel x", ylabel="TESS pixel y")
    axes[1, 0].legend(fontsize=8)
    fig.suptitle("TIC 34691042: three TESS eclipses")
    fig.savefig(directory / "TIC-34691042-reproduction.png", dpi=150)
    plt.close(fig)


def tgv(directory):
    profiles = table("TGV-184-profiles.csv")
    branches = [("Apri", -64), ("Apri", -53), ("Apri", -48), ("Asec", -48)]
    fig, axes = plt.subplots(2, 2, figsize=(10, 6), constrained_layout=True)
    for axis, (branch, cycle) in zip(axes.flat, branches, strict=True):
        samples = [r for r in profiles if r["branch"] == branch and int(r["cycle"]) == cycle]
        time = [float(r["dt_h"]) for r in samples]
        for column, label in (("tam_corrected_ppt", "SYSREM"), ("raw_corrected_ppt", "Raw")):
            axis.plot(time, [float(r[column]) for r in samples], "o-", markersize=3, label=label)
        axis.axhline(0, color="0.5", linewidth=.6)
        axis.axvline(0, color="0.5", linewidth=.6)
        axis.set(title=f"{branch}, cycle {cycle}", xlabel="Hours from prediction",
                 ylabel="Flux loss (ppt)")
    axes[0, 0].legend()
    fig.suptitle("TGV-184 A: historical SuperWASP windows")
    fig.savefig(directory / "TGV-184-reproduction.png", dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=Path.cwd())
    arguments = parser.parse_args()
    arguments.output_dir.mkdir(parents=True, exist_ok=True)
    long_clock(arguments.output_dir)
    tgv(arguments.output_dir)
