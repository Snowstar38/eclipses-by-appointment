"""Compare the two flagged TESS exposures with field stars and shifted exposures."""
import argparse
import csv
import hashlib
from collections import Counter
from pathlib import Path

from astropy.io import fits
from astropy.coordinates import SkyCoord
import numpy as np
import requests

HERE = Path(__file__).resolve().parent
TARGETS = {302399892,388584591,390126467}
EPOCHS = [38482,38490]+[38482+i*16 for i in range(-10,11) if i]


def write(name, rows):
    with (HERE / name).open("w", newline="") as f:
        w=csv.DictWriter(f,list(dict.fromkeys(k for r in rows for k in r)),lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


def draw(cache):
    excluded = {int(r["tic"]) for r in csv.DictReader((HERE.parent/"batch.csv").read_text().splitlines())}
    chosen, points, counts = [], [], Counter()
    key = lambda f: hashlib.sha256(("mixed26-field-v1/"+f.name).encode()).digest()
    paths = sorted(cache.glob("*_s026.fits"),key=key)
    def point(head):
        return SkyCoord(float(head["RA_OBJ"]),float(head["DEC_OBJ"]),unit="deg")
    omit = [point(fits.getheader(p)) for p in paths if int(p.name.split("_")[0]) in excluded]
    for f in paths:
        head=fits.getheader(f)
        tic=int(head["TICID"])
        pair=(head["CAMERA"],head["CCD"])
        pos=point(head)
        if tic in excluded and tic not in TARGETS:
            continue
        if tic not in TARGETS:
            if counts[pair]>=12 or any(pos.separation(c).arcmin<6 for c in omit+points):
                continue
            counts[pair]+=1
            points.append(pos)
        digits=f"{tic:016d}"
        dirs="/".join(digits[i:i+4] for i in range(0,16,4))
        url=f"https://archive.stsci.edu/hlsps/qlp/s0026/{dirs}/hlsp_qlp_tess_ffi_s0026-{digits}_tess_v01_llc.fits"
        chosen.append(dict(tic=tic,role="trigger" if tic in TARGETS else "field",camera=pair[0],ccd=pair[1],
                           ra_deg=pos.ra.deg,dec_deg=pos.dec.deg,filename=f.name,url=url,
                           sha256=hashlib.sha256(f.read_bytes()).hexdigest()))
    write("roster.csv",chosen)
    return chosen


def check(row, cache):
    f=cache/row["filename"]
    if not f.exists():
        r=requests.get(row["url"],timeout=50)
        r.raise_for_status()
        f.write_bytes(r.content)
    if hashlib.sha256(f.read_bytes()).hexdigest()!=row["sha256"]:
        raise ValueError("Archive FITS hash mismatch for "+str(row["tic"]))
    with fits.open(f) as hdus:
        d=hdus[1].data
        n=d["CADENCENO"]
        a,b=d["SAP_FLUX"],d["KSPSAP_FLUX"]
        good=(d["QUALITY"]==0)&np.isfinite(a)&np.isfinite(b)
        results=[]
        for epoch in EPOCHS:
            delta=n.astype(int)-epoch
            left,right=good&(delta>=-4)&(delta<0),good&(delta<=4)&(delta>0)
            core=good&(delta==0)
            rec=dict(tic=row["tic"],role=row["role"],camera=row["camera"],ccd=row["ccd"],cadenceno=epoch)
            if core.sum()!=1 or min(left.sum(),right.sum())<2:
                results.append(dict(**rec,status="missing_or_flagged"))
                continue
            changes=[]
            for y in (a,b):
                base=(np.median(y[left])+np.median(y[right]))/2
                changes.append(float(1000*(1-y[core][0]/base)) if base>0 else np.nan)
            sap,cor=changes
            if not np.isfinite(changes).all():
                results.append(dict(**rec,status="invalid_baseline"))
                continue
            results.append(dict(**rec,status="measured",btjd=float(d["TIME"][core][0]),sap_loss_ppt=sap,
                                corrected_loss_ppt=cor,large_corrected_only=abs(sap)<10 and cor>50))
    return results


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("cache",type=Path)
    p.add_argument("--draw",action="store_true",help="Draw from the original numbered QLP FITS cache")
    args=p.parse_args()
    args.cache.mkdir(parents=True,exist_ok=True)
    rows=draw(args.cache) if args.draw else list(csv.DictReader((HERE/"roster.csv").read_text().splitlines()))
    write("measurements.csv",[r for star in rows for r in check(star,args.cache)])
