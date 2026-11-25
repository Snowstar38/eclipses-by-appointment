"""Plot the changing illumination of background pixels at the two false dips."""
from pathlib import Path
from io import BytesIO
import hashlib
import json

from astropy.io import fits
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import requests

here = Path(__file__).resolve().parent
fig, grid = plt.subplots(2, 4, figsize=(9, 5.6), layout="constrained")
for axes, tic in zip(grid, ["113655666", "356752132"]):
    folder = here / f"single-{tic}"
    if tic == "113655666":
        record = json.loads((folder / "receipt.json").read_bytes())
        center, shoulders = record["t0_btjd"], record["baseline_offsets_d"]
    else:
        evidence = json.loads((folder / "evidence.json").read_bytes())
        center = evidence["measurement_center_btjd"]
        shoulders = evidence["shoulder_abs_limits_d"]
        record = evidence["files"]["target-tpf.fits"]
    file = folder / "target-tpf.fits"
    if file.exists():
        content = file.read_bytes()
    else:
        response = requests.get(record["url"], timeout=45)
        response.raise_for_status()
        content = response.content
    assert hashlib.sha256(content).hexdigest() == record["sha256"]
    with fits.open(BytesIO(content)) as hdus:
        assert str(hdus[0].header["TICID"]) == tic
        data = hdus[1].data
        dt = data["TIME"] - center
        valid = (data["QUALITY"] == 0) & np.isfinite(dt)
        quiet = valid & (abs(dt) > shoulders[0]) & (abs(dt) < shoulders[1])
        pixels = data["FLUX"] + data["FLUX_BKG"]
        baseline = np.nanmedian(pixels[quiet], axis=0)
        mask = hdus["APERTURE"].data
        frames = []
        times = [-1, 0, .5, 1]
        for hour in times:
            use = valid & (abs(24 * dt - hour) <= .07)
            frames.append(np.nanmedian(pixels[use], axis=0) - baseline)

    for ax, frame, hour in zip(axes, frames, times):
        ax.imshow(frame, vmin=0, vmax=np.nanmax(frames), cmap="inferno", origin="lower")
        ax.contour((mask & 2) != 0, levels=[.5], colors=["white"], linewidths=1.3)
        y, x = np.where((mask & 4) != 0)
        ax.scatter(x, y, marker="s", s=20, facecolors="none", edgecolors="#68d5e8", linewidths=.7)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_title(f"{hour:+g} h" if hour else "Dip center")
    axes[0].set_ylabel(f"TIC {tic}")
fig.suptitle("Excess light moving through the background pixels")
fig.supxlabel("White outline = stellar aperture     ·     Blue squares = background pixels\n"
              "Brighter colors show more excess light. Each row has a fixed intensity scale.", fontsize=10)
fig.savefig(here / "background-sequence.png", dpi=165)
