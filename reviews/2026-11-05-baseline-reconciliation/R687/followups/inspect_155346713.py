"""Inspect adaptive older QLP data around the Gaia-period single event."""
import hashlib
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits
from scipy.ndimage import median_filter

HERE = Path(__file__).resolve().parent
SEARCH = HERE.parent
TIC = "155346713"
download = json.loads((HERE / "downloads-155346713.json").read_text())
original = [r for r in json.loads((SEARCH / "downloads.json").read_text()) if r["tic"] == TIC]
products = original + download["products"]
fig, axs = plt.subplots(5, 1, figsize=(12, 12), sharey=False)
summary = []
for ax, rec in zip(axs, sorted(products, key=lambda r: r["sector"])):
    path = Path(rec.get("file") or rec.get("path"))
    assert hashlib.sha256(path.read_bytes()).hexdigest() == rec["sha256"]
    with fits.open(path) as h:
        d = h[1].data
        t = np.asarray(d["TIME"], float)
        f = np.asarray(d["SAP_FLUX"], float)
        q = np.asarray(d["QUALITY"], int)
    good = np.isfinite(t) & np.isfinite(f) & (f > 0) & (q == 0)
    t, f = t[good], f[good]
    f = f / np.median(f)
    ax.plot(t, f, ".", ms=1, alpha=.6)
    smooth = median_filter(f, size=max(3, int(.3 / np.median(np.diff(t))) | 1))
    ax.plot(t, smooth, "r-", lw=.8)
    period = 33.63348396287843
    anchor = 3702.3228
    for n in range(-100, 1):
        predicted = anchor + n * period
        if t.min() - 3 <= predicted <= t.max() + 3:
            ax.axvline(predicted, color="green", ls=":", lw=1)
            ax.text(predicted, np.quantile(f, .98), str(n), color="green", fontsize=7)
    ax.set_title(f"TIC {TIC} s{rec['sector']} quality-zero raw SAP, median-normalized")
    ax.set_ylabel("flux")
    summary.append({"sector": rec["sector"], "q0_n": len(t), "btjd_span": [float(t.min()), float(t.max())],
                    "min_normalized_flux": float(f.min()), "median_cadence_minutes": float(np.median(np.diff(t)) * 1440)})
axs[-1].set_xlabel("BTJD")
fig.tight_layout()
fig.savefig(HERE / "155346713-all-sectors.png", dpi=160)
(HERE / "coverage-155346713.json").write_text(json.dumps(summary, indent=2))
print(json.dumps(summary, indent=2))
