"""Measure the archived fold prediction in each available alternate SPOC extraction."""
import argparse
import csv
import hashlib
import json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import urlencode

from astropy.io import fits
import numpy as np
import requests

HERE = Path(__file__).resolve().parent


def measure(t, y, center, width, dt):
    phase = (t-center)/width
    zones = [(phase>=-2)&(phase<=-.8), abs(phase)<=.35, (phase>=.8)&(phase<=2)]
    arr = [y[m & np.isfinite(y)] for m in zones]
    if any(len(x)<max(3,.55*n*width/dt) for x,n in zip(arr,(1.2,.7,1.2))):
        return None
    left,core,right = arr
    l,c,r = map(np.median,arr)
    base = .5*(l+r)
    if base<=0:
        return None
    residual = np.r_[left-l,right-r]
    scatter = 1.4826*np.median(abs(residual))
    error = max(scatter/np.sqrt(max(1,len(core)/3)), abs(l-r)/2, base*1e-5)
    return 1000*(base-c)/base,1000*error/base


def run(job):
    row, clock, folder = job
    tic,sector,uri = row["target_name"],row["sequence_number"],row["dataURL"]
    path = folder / uri.split("/")[-1]
    url = "https://mast.stsci.edu/api/v0.1/Download/file?"+urlencode({"uri":uri})
    rec = dict(tic=tic, sector=sector, pipeline=row["provenance_name"], url=url)
    if not path.exists():
        resp=requests.get(url,timeout=(10,60))
        resp.raise_for_status()
        if not resp.content.startswith(b"SIMPLE"):
            raise ValueError("Archive returned a non-FITS response")
        path.write_bytes(resp.content)
    rec["sha256"]=hashlib.sha256(path.read_bytes()).hexdigest()
    with fits.open(path) as h:
        if (int(h[0].header["TICID"]),int(h[0].header["SECTOR"]))!=(int(tic),sector):
            raise ValueError("Wrong product identity")
        d=h[1].data
        q=(d["QUALITY"]==0)&np.isfinite(d["TIME"])
        t=d["TIME"][q].astype(float)
        flux=[d[k][q].astype(float) for k in ("SAP_FLUX","PDCSAP_FLUX")]
    p,epoch,w,depth = (float(clock[k]) for k in ("period_d","epoch_btjd","duration_d","screen_depth_ppt"))
    rec.update(first_btjd=t.min(), last_btjd=t.max(),quality_zero=len(t))
    dt=np.median(np.diff(t))
    events=[]
    for n in range(int(np.ceil((t.min()-epoch)/p)),int(np.floor((t.max()-epoch)/p))+1):
        center=epoch+n*p
        record=dict(tic=tic,sector=sector,pipeline=row["provenance_name"],cycle=n,btjd=center,original_depth_ppt=depth)
        a,b=[measure(t,y,center,w,dt) for y in flux]
        if a is not None and b is not None:
            record.update(sap_depth_ppt=a[0],sap_error_ppt=a[1],pdc_depth_ppt=b[0],pdc_error_ppt=b[1])
            if all(x>max(5*err,.3*depth) for x,err in (a,b)):
                state="supports_original"
            elif all(x+3*err<.3*depth for x,err in (a,b)):
                state="sensitive_empty"
            else:
                state="indeterminate"
        else:
            state="insufficient_coverage"
        events.append(dict(**record,status=state))
    return rec,events


if __name__ == "__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("cache",type=Path)
    args=parser.parse_args()
    args.cache.mkdir(parents=True,exist_ok=True)
    rows=json.loads((HERE/"archive.json").read_bytes())["products"]
    with (HERE.parent/"ground/archived-clocks.csv").open() as f:
        clocks={r["tic"]:r for r in csv.DictReader(f)}
    jobs=[(r,clocks[r["target_name"]],args.cache) for r in rows if r["provenance_name"]!="QLP"]
    with ThreadPoolExecutor(5) as pool:
        results=list(pool.map(run,jobs))
    for name,items in [("products",[r for r,_ in results]),("events",[r for _,events in results for r in events])]:
        with (HERE/(name+".csv")).open("w",newline="") as f:
            w=csv.DictWriter(f,list(dict.fromkeys(k for row in items for k in row)),lineterminator="\n")
            w.writeheader()
            w.writerows(items)
