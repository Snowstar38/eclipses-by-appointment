"""Compare a QLP timing prediction with the TESS-SPOC aperture and PDC reductions."""
import argparse
import csv
from pathlib import Path

from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np

from retrieve import HERE, acquire, tpf_url


def run(cache):
    tic = "405590521"
    cache.mkdir(parents=True, exist_ok=True)
    centers = {int(r["sector"]):float(r["fitted_btjd"]) for r in
               csv.DictReader((HERE.parent/"batch2/405590521-centers.csv").open())}
    rows = []
    fig, axes = plt.subplots(1, 3, figsize=(12, 3.6), sharey=True, layout="constrained")
    for ax, sector in zip(axes, (76,83,84)):
        url = tpf_url(tic,sector).replace("_tp.fits", "_lc.fits")
        path = cache/f"{tic}-{sector}-lc.fits"
        row = acquire((path, url, {}, b"simple"))
        center = centers[sector]
        with fits.open(path) as hdu:
            assert int(hdu[0].header["TICID"])==int(tic) and hdu[0].header["SECTOR"]==sector
            z = hdu[1].data
            dt = z["TIME"]-center
            row.update(tic=tic, sector=sector, center_btjd=center)
            for col, color in (("SAP_FLUX","#205493"),("PDCSAP_FLUX","#d67620")):
                flux = z[col]
                good = (z["QUALITY"]==0) & np.isfinite(flux) & np.isfinite(dt)
                left = good & (dt>=-1.6) & (dt<=-.8)
                right = good & (dt>=.8) & (dt<=1.6)
                core = good & (abs(dt)<.24)
                level = np.interp(dt, [np.median(dt[m]) for m in (left,right)],
                                  [np.median(flux[m]) for m in (left,right)])
                resid = 1000*(flux/level-1)
                row[col+"_ppt"] = round(float(-np.median(resid[core])),3)
                row[col+"_core_n"] = int(core.sum())
                bins = np.arange(-2.,2.,.025)
                ax.plot(bins,[np.median(resid[m]) if np.any(m) else np.nan for x in bins
                              for m in [good & (abs(dt-x)<.0125)]],color=color,label=col)
        ax.axvspan(-.24,.24,color="gray",alpha=.12)
        ax.set(title=f"Sector {sector}", xlabel="Days from fitted QLP minimum")
        rows.append(row)
    axes[0].set_ylabel("Local flux difference (ppt)")
    axes[-1].legend(fontsize=8)
    fig.suptitle("TIC 405590521   |   independent reduction of the same TESS images")
    fig.savefig(HERE/"spoc-405590521.png",dpi=140)
    with (HERE/"spoc-405590521.csv").open("w",newline="") as f:
        w=csv.DictWriter(f,rows[0],lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


if __name__=="__main__":
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("cache",type=Path)
    run(ap.parse_args().cache)
