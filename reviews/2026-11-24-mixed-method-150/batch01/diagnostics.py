"""Build contact sheets and measure auxiliary FITS columns in archived event windows."""
import argparse
import csv
from pathlib import Path

import numpy as np
from astropy.io import fits
from PIL import Image, ImageDraw

HERE = Path(__file__).resolve().parent
parser = argparse.ArgumentParser()
parser.add_argument("batch_dir", type=Path, nargs="?", default=HERE)
parser.add_argument("--fits-dir", type=Path, default=(HERE.parents[2] if (HERE.parents[2]/"sky/data/qlp-sb-p20-60").is_dir() else HERE.parent/"inputs/workspace")/"sky/data/qlp-sb-p20-60")
args = parser.parse_args()
base = args.batch_dir
plots = base/"plots"


def read(name):
    with (base/f"{name}.csv").open(encoding="utf-8-sig",newline="") as f:
        return list(csv.DictReader(f))


targets = read("batch")
for idx in range(0,len(targets),5):
    sheet = Image.new("RGB",(1450,205*len(targets[idx:idx+5])),"white")
    for j,row in enumerate(targets[idx:idx+5]):
        for k,name in enumerate(("prior","Pilot","BLS_1")):
            path = plots/f'{row["tic"]}-{name}.png'
            if not path.exists():
                ImageDraw.Draw(sheet).text((484*k+12,205*j+55),f'{row["tic"]} {name}: no plottable windows',fill="black")
                continue
            with Image.open(path) as image:
                top = image.crop((0,0,image.width,min(image.height,250))).convert("RGB")
                top.thumbnail((482,201))
                sheet.paste(top,(484*k,205*j+5))
    sheet.save(plots/f"contact-{idx//5+1}.png")

sectors = {(r["tic"],r["sector"]):r["file"] for r in read("files")}
predictions = read("predictions")
widths = {(r["tic"],r["clock"]):float(r["width_d"]) for r in read("clocks")}
out = []
by_path = {}
for r in read("events"):
    by_path.setdefault(sectors[(r["tic"],r["sector"])],[]).append(("archive",r))
for r in predictions:
    if r["status"]!="measured":
        continue
    if r["clock"] not in {"Pilot","BLS 1","Fine 1","Fine 2","Fine 3","Fine 4"}:
        continue
    if min(float(r["raw_depth_ppt"]),float(r["corrected_depth_ppt"]))<1.5:
        continue
    w = widths[(r["tic"],r["clock"])]
    r["width_d"] = w
    by_path.setdefault(sectors[(r["tic"],r["sector"])],[]).append((r["clock"],r))
for fn,group in by_path.items():
    path = args.fits_dir/fn
    if not path.is_file():
        continue
    with fits.open(path) as h:
        z = h[1].data
        for label,r in group:
            c,w = (float(r[n]) for n in ("center_btjd","width_d"))
            d = np.asarray(z["TIME"]-c)
            core = abs(d)<=w/2
            good = z["QUALITY"]==0
            i = np.nanargmin(abs(d))
            record = dict(tic=r["tic"],sector=r["sector"],clock=label,center_btjd=c,width_d=w,
                          camera=h[0].header["CAMERA"],ccd=h[0].header["CCD"],
                          nearest_cadence=int(z["CADENCENO"][i]),
                          core_quality_zero=int(sum(core&good)),core_quality_nonzero=int(sum(core&~good)))
            for key in ("SAP_X","SAP_Y","SAP_BKG"):
                x = np.asarray(z[key],float)
                l = good & (d<-.65*w)&(d>=-1.75*w)&np.isfinite(x)
                h0 = good & (d>.65*w)&(d<=1.75*w)&np.isfinite(x)
                v = core & good & np.isfinite(x)
                delta = np.nan
                scale = np.nan
                if min(l.sum(),h0.sum(),v.sum())>=2:
                    m1,m2 = np.median(x[l]),np.median(x[h0])
                    delta = float(np.median(x[v])-(m1+m2)/2)
                    residual=np.r_[x[l]-m1,x[h0]-m2]
                    scale = float(1.4826*np.median(abs(residual-np.median(residual))))
                record[f"{key}_core_shift"] = delta
                record[f"{key}_shoulder_scatter"] = scale
            out.append(record)
with (base/"aux-windows.csv").open("w",newline="",encoding="utf-8") as f:
    w=csv.DictWriter(f,out[0].keys())
    w.writeheader()
    w.writerows(out)
