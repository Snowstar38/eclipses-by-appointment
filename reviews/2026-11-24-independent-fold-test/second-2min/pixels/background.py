"""Measure and plot the deep HD 276904 event before and after background subtraction."""
import hashlib
import json
from pathlib import Path

from astropy.io import fits
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

here = Path(__file__).resolve().parent
prior = json.loads((here / "evidence.json").read_bytes())
product = here / "tp.fits"
with product.open("rb") as stream:
    digest = hashlib.file_digest(stream, "sha256").hexdigest()
assert digest == prior["sha256"]["tp.fits"]
with fits.open(product) as hdus:
    assert (hdus[0].header["TICID"], hdus[0].header["SECTOR"]) == (187261476, 59)
    data = hdus[1].data
    aperture = (hdus["APERTURE"].data & 2) != 0
    t = data["TIME"].astype(float)
    keep = (data["QUALITY"] == 0) & np.isfinite(t)
    flux = data["FLUX"][:, aperture].sum(axis=1, dtype=float)
    sky = data["FLUX_BKG"][:, aperture].sum(axis=1, dtype=float)
    counts = data["RAW_CNTS"][:, aperture]
    raw = np.where(np.all(counts >= 0, axis=1), counts.sum(axis=1, dtype=float), np.nan)

windows = prior["deep_windows"]
def window(bounds):
    return keep & (t >= bounds[0]) & (t <= bounds[1])

core = window(windows["in"])
baseline = window(windows["out"][0]) | window(windows["out"][1])
shown = window([windows["out"][0][0], windows["out"][1][1]])
measurements = {}
fig, axes = plt.subplots(2, 1, sharex=True, figsize=(9, 5.5), layout="constrained")
fig.suptitle("HD 276904   ·   TESS sector 59   ·   Deep event in the target aperture")
for key, series in dict(subtracted=flux, restored=flux + sky, background=sky, raw=raw).items():
    before = np.nanmedian(series[baseline])
    during = np.nanmedian(series[core])
    measurements[key] = dict(baseline=before, event=during, change=during-before,
                             percent_change=100 * (during / before - 1))
    if key in ("restored", "raw"):
        ax = axes[int(key == "raw")]
        delta = 100 * (series / before - 1)
        ax.plot(t[shown] - 2917, delta[shown], ".", ms=2, color="#185f61")
        ax.set_ylabel("Restored flux\nchange (%)" if key == "restored" else "Raw counts\nchange (%)")
        for lo, hi in windows["out"]:
            ax.axvspan(lo-2917, hi-2917, color="#e6e9ed", zorder=0)
        ax.axvspan(windows["in"][0]-2917, windows["in"][1]-2917, color="#ffefbb", zorder=0)
        ax.axhline(0, color=".4", lw=.6, zorder=0)
        ax.spines[["right", "top"]].set_visible(False)
axes[-1].set_xlabel("Days since BTJD 2917.0")
fig.savefig(here / "background.png", dpi=180)
result = dict(sha256=digest, aperture_pixels=int(aperture.sum()), windows_btjd=windows,
              core_cadences=int(core.sum()), baseline_cadences=int(baseline.sum()),
              measurements=measurements)
(here / "background.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf8")
