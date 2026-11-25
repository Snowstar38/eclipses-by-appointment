"""Fold resolved ZTF photometry at the period and phase measured in the TESS aperture."""
import argparse
import csv
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from sampling import HERE, observations


def plot(cache):
    with (HERE / "tests.csv").open() as stream:
        clocks = {r["tic"]: r for r in csv.DictReader(stream) if r["test"] == "donor_at_aperture_fit"}
    donors = [
        ("415033586148701056", "WISE J004852.7+510946"),
        ("462468648077150848", "WISE J032146.2+595213"),
    ]
    fig, axes = plt.subplots(1, 2, figsize=(10, 4), layout="constrained")
    for ax, (source, name) in zip(axes, donors):
        period = float(clocks[source]["period_d"])
        epoch = float(clocks[source]["epoch_btjd"])
        data = [s for s in observations(source, cache) if s[0]["survey"] == "ZTF"]
        for band, color in [("zg", "#227366"), ("zr", "#b84632")]:
            series = [s for s in data if s[0]["band"] == band]
            if not series:
                continue
            times = np.concatenate([s[1] for s in series])
            mags = np.concatenate([s[2] for s in series])
            phase = ((times - epoch) / period + .25) % 1 - .25
            ax.scatter(phase, mags, s=4, color=color, alpha=.14, rasterized=True)
            edges = np.linspace(-.25, .75, 41)
            inds = np.digitize(phase, edges)
            medians = [np.median(mags[inds == i]) if np.sum(inds == i) >= 3 else np.nan for i in range(1, len(edges))]
            ax.plot((edges[1:] + edges[:-1]) / 2, medians, color=color, label=band[-1] + " median")
        ax.set(xlabel="Orbital phase from TESS primary", ylabel="Magnitude relative to series median",
               title=f"{name}\nTESS period {period:.8f} d", xlim=(-.25, .75))
        lo, hi = np.quantile(np.concatenate([s[2] for s in data]), [.002, .998])
        ax.set_ylim(hi + .05, lo - .05)
        ax.axvline(0, lw=.7, ls="--", color="#444444")
        ax.legend()
    fig.savefig(HERE / "ztf-neighbors.png", dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("cache", type=Path)
    plot(parser.parse_args().cache)
