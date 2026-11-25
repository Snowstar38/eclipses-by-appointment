from pathlib import Path
import hashlib,io,json
import requests,numpy as np
from astropy.io import fits
D=Path(__file__).resolve().parent;t0=2491.27973197
source=next(r for r in json.loads((D.parent/'sol/archive.json').read_bytes()) if r['tic']=='113655666' and r['sector']==43)
url=source['url'].replace('https://archive.stsci.edu/missions/tess/tid/','https://stpubdata.s3.us-east-1.amazonaws.com/tess/public/tid/').replace('_lc.fits','_tp.fits')
res=requests.get(url,timeout=35);res.raise_for_status()
with fits.open(io.BytesIO(res.content)) as h:
 assert h[0].header['TICID']==113655666 and h[0].header['SECTOR']==43
 d=h[1].data;mask=(h['APERTURE'].data.astype(int)&2)>0;t=np.asarray(d['TIME']);valid=(d['QUALITY']==0)&np.isfinite(t)
 f=np.sum(d['FLUX'][:,mask],axis=1);b=np.sum(d['FLUX_BKG'][:,mask],axis=1);raw=d['RAW_CNTS'][:,mask].astype(float); raw[raw<0]=np.nan
 print(h[1].columns.names, 'raw finite',np.isfinite(raw).sum())
 sers={'FLUX':f,'FLUX_BKG':b,'FLUX_plus_FLUX_BKG':f+b,'RAW_CNTS':np.sum(raw,axis=1)}
 center=valid&(abs(t-t0)<=.010);shoulder=valid&(abs(t-t0)>=.15)&(abs(t-t0)<=.30)
 v={}
 for k,y in sers.items():
  sel=shoulder&np.isfinite(y);ev=center&np.isfinite(y)
  if not np.any(sel) or not np.any(ev):v[k]={'available':False};continue
  baseline=np.median(y[sel]);at_event=np.median(y[ev]);v[k]=dict(available=True,baseline=float(baseline),core=float(at_event),change=float(at_event-baseline),relative_change=float(at_event/baseline-1),baseline_scatter=float(np.median(abs(y[sel]-baseline))*1.4826))
 o=dict(tic='113655666',sector=43,t0_btjd=t0,url=url,sha256=hashlib.sha256(res.content).hexdigest(),aperture_pixels=int(mask.sum()),camera=h[0].header['CAMERA'],ccd=h[0].header['CCD'],core_n=int(center.sum()),baseline_n=int(shoulder.sum()),baseline_offsets_d=[.15,.3],core_halfwidth_d=.01,measurements=v)
 (D/'receipt.json').write_text(json.dumps(o,indent=2)+'\n');print(v)

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

hours = (t - t0) * 24
shown = valid & (abs(hours) <= 8)
fig, (budget, detector) = plt.subplots(
    2, 1, sharex=True, figsize=(9, 5.5), height_ratios=(2, 1), layout="constrained"
)
fig.suptitle("TIC 113655666   ·   TESS sector 43   ·   Two-minute aperture measurements")
for key, label, color in [
    ("FLUX", "After background subtraction", "#216491"),
    ("FLUX_BKG", "Estimated background", "#a34d13"),
    ("FLUX_plus_FLUX_BKG", "With background restored", "#13705a"),
]:
    change = sers[key] - v[key]["baseline"]
    budget.plot(hours[shown], change[shown], ".", ms=2.7, label=label, color=color)
budget.set_ylabel("Change from baseline (e⁻/s)")
budget.legend(loc="upper right", fontsize=8, markerscale=2)

raw_change = 100 * (sers["RAW_CNTS"] / v["RAW_CNTS"]["baseline"] - 1)
detector.plot(hours[shown], raw_change[shown], ".", ms=3, color="#4b426e")
detector.set_ylabel("Raw counts\nchange (%)")
detector.set_xlabel(f"Hours from BTJD {t0:.6f}")
for ax in (budget, detector):
    for start, stop in [(-7.2, -3.6), (3.6, 7.2)]:
        ax.axvspan(start, stop, color="#e6e9ed", zorder=0)
    ax.axvspan(-.24, .24, color="#ffefbb", zorder=0)
    ax.axhline(0, color="#555555", lw=.6, zorder=0)
    ax.spines[["right", "top"]].set_visible(False)
    ax.set_xlim(-8, 8)
fig.savefig(D / "event.png", dpi=180)
plt.close(fig)
