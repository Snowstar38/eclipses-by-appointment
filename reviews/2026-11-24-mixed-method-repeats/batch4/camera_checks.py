"""Compare individual events at exact exposure identifiers across the same camera."""
import argparse
import csv
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits

HERE = Path(__file__).resolve().parent
parser = argparse.ArgumentParser()
parser.add_argument("--fits-dir", type=Path, default=(HERE.parents[2] if (HERE.parents[2]/"sky/data/qlp-sb-p20-60").is_dir() else HERE.parent/"inputs/workspace")/"sky/data/qlp-sb-p20-60")
args = parser.parse_args()
TRIALS = [
    (85,3,1037602,13,("137203172","387410061")),
    (35,3,149463,4,("45184585",)),
    (35,3,149296,4,("45184585",)),
    (77,4,945988,13,("375783784",)),
    (22,4,32976,3,("387410061",)),
]
records = []
for sector, camera, mid, radius, targets in TRIALS:
    cadences = np.arange(mid-5*radius,mid+5*radius+1)
    traces = []
    for path in sorted(args.fits_dir.glob(f"*_s{sector:03d}.fits")):
        tic = path.stem.split("_")[0]
        with fits.open(path) as hdus:
            header = hdus[0].header
            if header.get("CAMERA")!=camera:
                continue
            ccd = header["CCD"]
            z = hdus[1].data
            corrected = next((k for k in ("KSPSAP_FLUX","DET_FLUX","PDCSAP_FLUX") if k in z.names),None)
            if corrected is None:
                continue
            ok = ((z["QUALITY"]==0)&np.isin(z["CADENCENO"],cadences)&
                  np.isfinite(z["SAP_FLUX"])&np.isfinite(z[corrected]))
            x = z["CADENCENO"][ok].astype(int)-mid
            if not len(x):
                continue
            f = np.stack([z[k][ok].astype(float) for k in ("SAP_FLUX",corrected)])
        inside = abs(x)<=radius
        before = (x<=-2*radius)&(x>=-4*radius)
        after = (x>=2*radius)&(x<=4*radius)
        if min(inside.sum(),before.sum(),after.sum())<max(radius//2,2):
            continue
        times = [np.median(x[before]),np.median(x[after])]
        values = np.column_stack([np.median(f[:,before],axis=1),np.median(f[:,after],axis=1)])
        baseline = np.array([np.interp(x,times,y) for y in values])
        residual = (f/baseline-1)*1000
        trace = np.full((2,len(cadences)),np.nan)
        trace[:,x+5*radius] = residual
        traces.append((tic,ccd,trace))
        raw,cor = -np.median(residual[:,inside],axis=1)
        records.append(dict(sector=sector,camera=camera,comparison_frame=mid,half_width_cadences=radius,
                            tic=tic,ccd=ccd,is_trigger=tic in targets,raw_depth_ppt=raw,corrected_depth_ppt=cor,
                            core_n=inside.sum(),left_n=before.sum(),right_n=after.sum()))
    if not traces:
        continue
    comparisons = {
        (85,1037602): ("434533064","467289467"),
        (35,149463): ("175252465","74885936"),
        (35,149296): ("175252465","74885936"),
    }.get((sector,mid),())
    fig, axes = plt.subplots(2,1,figsize=(10,6),layout="constrained",sharex=True)
    for channel,(ax,label) in enumerate(zip(axes,("Raw SAP","Pipeline corrected"))):
        for ccd in sorted({s for _,s,_ in traces}):
            control = [y[channel] for tic,s,y in traces if s==ccd and tic not in targets]
            if control:
                med = np.ma.median(np.ma.masked_invalid(control),axis=0).filled(np.nan)
                ax.plot(cadences-mid,med,label=f"CCD {ccd} controls (n={len(control)})",alpha=.65)
        for tic,ccd,y in traces:
            if tic in targets or tic in comparisons:
                ax.plot(cadences-mid,y[channel],label=f"TIC {tic} (CCD {ccd})",lw=1.3,marker=".",ms=3,
                        linestyle="-" if tic in targets else "--",alpha=1 if tic in targets else .75)
        ax.axvspan(-radius,radius,color="tab:orange",alpha=.10)
        ax.set_ylabel(f"{label} (ppt)")
        ax.legend(ncols=3,fontsize=7,loc="lower right")
    axes[-1].set_xlabel(f"CADENCENO minus {mid}")
    fig.suptitle(f"Sector {sector}, camera {camera}: same-exposure comparison")
    fig.savefig(HERE/"plots"/f"camera-S{sector}-{mid}.png",dpi=135)
    plt.close(fig)

with (HERE/"camera-comparisons.csv").open("w",newline="",encoding="utf-8") as stream:
    writer = csv.DictWriter(stream,records[0].keys())
    writer.writeheader()
    writer.writerows(records)
