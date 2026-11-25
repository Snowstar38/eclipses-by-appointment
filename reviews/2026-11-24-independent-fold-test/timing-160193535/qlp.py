"""Measure predicted eclipse windows using an independently reduced TESS full-frame light curve."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import io,json,hashlib
import numpy as np,requests
from astropy.io import fits
D=Path(__file__).resolve().parent
def run(sec):
    t="0000000160193535";tag=f"s{sec:04d}"
    stem=f"https://archive.stsci.edu/hlsps/qlp/{tag}/"+"/".join(t[i:i+4] for i in range(0,16,4))+"/"
    err=[]
    for v in ("01","02","03"):
        url=stem+f"hlsp_qlp_tess_ffi_{tag}-{t}_tess_v{v}_llc.fits"
        try:
            r=requests.get(url,timeout=12);r.raise_for_status()
            with fits.open(io.BytesIO(r.content),memmap=False) as hd:
                d=hd[1].data
                assert int(hd[0].header["TICID"])==int(t)
                assert int(hd[0].header["SECTOR"])==sec
                col=next(c for c in ("KSPSAP_FLUX","SAP_FLUX") if c in d.names)
                qualify=(d["QUALITY"]==0)&np.isfinite(d[col])&np.isfinite(d["TIME"])&(d[col]>0)
                ts,flux=d["TIME"][qualify],d[col][qualify]
                raw=d["SAP_FLUX"][qualify]
            break
        except Exception as ex:err.append(str(ex))
    else:return dict(sector=sec,errors=err)
    j=json.loads((D/"sol/ephemeris.json").read_bytes());p=j["period_d"];ep=j["primary_epoch_btjd"]
    events=[]
    for phase,lag in [("primary",0),("secondary",j["secondary_lag_days"])]:
        for k in range(int((ts.min()-ep)/p)-2,int((ts.max()-ep)/p)+2):
            tc=ep+k*p+lag;off=ts-tc
            core=abs(off)<.045;left=(off>-.30)&(off<-.14);right=(off>.14)&(off<.30)
            if min(core.sum(),left.sum(),right.sum())<3:continue
            depth=1000*(1-np.median(flux[core])/min(np.median(flux[left]),np.median(flux[right])))
            rawdepth=1000*(1-np.nanmedian(raw[core])/min(np.nanmedian(raw[left]),np.nanmedian(raw[right])))
            events.append(dict(family=phase,cycle=k,btjd=tc,n=int(core.sum()),depth_ppt=float(depth),sap_depth_ppt=float(rawdepth)))
    return dict(sector=sec,url=url,sha256=hashlib.sha256(r.content).hexdigest(),column=col,good_cadences=len(ts),events=events)
if __name__=="__main__":
    with ThreadPoolExecutor(4) as pool:
        rows=list(pool.map(run,[19,26,59,79]))
    (D/"qlp-check.json").write_text(json.dumps(rows,indent=1),encoding="utf8")
    print([(v["sector"],len(v.get("events",[])),v.get("errors",[])[:1]) for v in rows])
