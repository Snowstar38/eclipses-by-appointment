"""Event-level background-closure screen for archived SPOC two-minute light curves."""
import csv
import hashlib
import io
import json
import os
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import numpy as np
import pandas as pd
import requests
from astropy.io import fits
from astropy.time import Time
from scipy.signal import find_peaks

HERE = Path(__file__).resolve().parent
CONTROLS = {113655666: [43], 356752132: [42], 187261476: [59]}
FWHM_H = np.array([.16,.27,.45,.75,1.25,2.1,3.5,5.8,9.6,16.0])
MIN_SAP_PPT = 10.
MIN_RESTORE_PPT = 5.
EVENT_FIELDS = (
    'btjd', 'half_h', 'bracket_outer_h', 'quality_full',
    'n_in', 'n_left', 'n_right', 'left_fraction',
    'core_fraction', 'right_fraction', 'min_consecutive_sap', 'min_consecutive_restored',
    'sap_loss_e_per_s', 'background_gain_e_per_s', 'restored_loss_e_per_s', 'sap_baseline_e_per_s',
    'sap_depth_ppt', 'pdc_depth_ppt', 'background_gain_ppt', 'restored_loss_ppt',
    'restored_sigma_ppt', 'restored_lower_3sigma_ppt', 'restored_upper_3sigma_ppt', 'restored_point_scatter_ppt',
    'background_sigma_ppt', 'closure_tolerance_ppt', 'classification', 'segment_start_btjd',
    'segment_end_btjd', 'utc', 'tic', 'sector',
    'lc_url', 'tpf_url', 'fits_sha256', 'camera',
    'ccd',
)


def mad(x):
    return 1.4826*np.median(np.abs(x-np.median(x)))


def longest(mask,t=None,dt=None):
    hits = np.flatnonzero(mask)
    if not len(hits):
        return 0
    gap = np.diff(hits)>1
    if t is not None:
        gap |= np.diff(t[hits])>1.5*dt
    return max(len(run) for run in np.split(hits,np.flatnonzero(gap)+1))


def index_for(tics,index):
    files={}
    for chunk in pd.read_csv(index,chunksize=350000):
        for row in chunk[chunk.tic.isin(tics)].itertuples(index=False):
            files[(row.tic,row.sector)]=row.file
    return files


def urls(tic,sector,filename):
    digits=f"{tic:016d}"
    dirs="/".join(digits[j:j+4] for j in range(0,16,4))
    stem=f"tid/s{sector:04d}/{dirs}/"
    return (f"https://archive.stsci.edu/missions/tess/{stem}{filename}",
            f"https://stpubdata.s3.us-east-1.amazonaws.com/tess/public/{stem}{filename}",
            f"https://stpubdata.s3.us-east-1.amazonaws.com/tess/public/{stem}{filename.replace('_lc.fits','_tp.fits')}")


def default_cache():
    if custom := os.environ.get("TESS_BACKGROUND_CACHE"):
        return Path(custom).expanduser()
    base = os.environ.get("LOCALAPPDATA") if os.name == "nt" else os.environ.get("XDG_CACHE_HOME")
    return (Path(base).expanduser() if base else Path.home()/".cache")/"tess-background-pilot"


def read_products(path):
    receipts = json.loads(Path(path).read_text(encoding="utf-8-sig"))
    return {(int(row["tic"]),int(row["sector"])):row for row in receipts}


def download(tic,sector,product,cache):
    filename = product.get("filename")
    if not filename or Path(filename).name != filename:
        raise ValueError("no valid indexed 2-minute SPOC LC filename")
    lc, mirror, tp = (product[k] for k in ("lc_url","lc_mirror_url","tpf_url"))
    path = cache/filename
    expected = product.get("fits_sha256")
    if not path.exists():
        errors=[]
        for url in dict.fromkeys((lc,mirror)):
            try:
                result=requests.get(url,timeout=(7,25))
                result.raise_for_status()
                if expected and hashlib.sha256(result.content).hexdigest()!=expected:
                    raise ValueError("downloaded FITS SHA-256 differs from the coverage receipt")
                with fits.open(io.BytesIO(result.content),memmap=False) as test:
                    if int(test[0].header["TICID"])!=tic or int(test[0].header["SECTOR"])!=sector:
                        raise ValueError("downloaded FITS has a different TIC or sector")
                path.write_bytes(result.content)
                break
            except Exception as exc:
                errors.append(f"{url}: {exc}")
        else:
            raise RuntimeError(" | ".join(errors))
    with path.open("rb") as handle:
        sha=hashlib.file_digest(handle,"sha256").hexdigest()
    if expected and sha!=expected:
        raise ValueError(f"cached FITS SHA-256 differs from the coverage receipt: {path}")
    with fits.open(path,memmap=False) as hdus:
        h=hdus[1].header
        if int(hdus[0].header["TICID"])!=tic or int(hdus[0].header["SECTOR"])!=sector:
            raise ValueError("cached FITS has a different TIC or sector")
        units=[h.get(f"TUNIT{hdus[1].columns.names.index(k)+1}") for k in ("SAP_FLUX","SAP_BKG","PDCSAP_FLUX")]
        equal=units[0] is not None and units[0]==units[1]
        if not equal:
            raise ValueError(f"unequal SAP and SAP_BKG units: {units}")
        data=hdus[1].data
        vals={k:np.array(data[k],dtype=float) for k in ("TIME","TIMECORR","SAP_FLUX","SAP_BKG","PDCSAP_FLUX","POS_CORR1","POS_CORR2")}
        vals["QUALITY"]=np.array(data["QUALITY"],dtype=int)
        meta=dict(tic=tic,sector=sector,lc_url=lc,lc_mirror_url=mirror,tpf_url=tp,
                  fits_sha256=sha,filename=filename,units=units,camera=int(hdus[0].header["CAMERA"]),
                  ccd=int(hdus[0].header["CCD"]),crowdsap=h.get("CROWDSAP"),
                  flux_fraction=h.get("FLFRCSAP"),time_system=h.get("TIMESYS"),
                  bjdrefi=h.get("BJDREFI"),bjdreff=h.get("BJDREFF"))
    return vals,meta


def robust_line(time,y,n_blocks=5):
    edges=np.array_split(np.arange(len(time)),n_blocks)
    centers=np.array([np.median(time[e]) for e in edges if len(e)])
    vals=np.array([np.median(y[e],axis=0) for e in edges if len(e)])
    order=np.argsort(centers)
    centers,vals=centers[order],vals[order]
    A=np.c_[np.ones(len(centers)),centers]
    fit=np.linalg.lstsq(A,vals,rcond=None)[0]
    return fit


def effective_error(z, mask, dt, block_minutes=14):
    block=max(2,round(block_minutes/(dt*1440)))
    chunk=[z[a:min(a+block,len(z))] for a in range(0,len(z),block) if mask[a:min(a+block,len(z))].all()]
    means=np.array([np.mean(v) for v in chunk if len(v)>=2])
    robust=mad(z[mask]) if mask.sum()>1 else 0.
    floor=robust/np.sqrt(max(1,mask.sum()))
    if len(means)>1:
        return max(floor,mad(means)/np.sqrt(len(means)))
    return floor


def measure(t,Y,center,half,dt):
    distance=abs(t-center)
    inner=distance<=half
    outer_lim=2.75*half+14*dt
    inner_bracket=max(1.45*half,half+2*dt)
    bracketing=(distance>=inner_bracket)&(distance<=outer_lim)
    left=bracketing&(t<center)
    right=bracketing&(t>center)
    wing_width=outer_lim-inner_bracket
    fractions=[min(1.,n*dt/w) for n,w in ((left.sum(),wing_width),(inner.sum(),2*half),(right.sum(),wing_width))]
    if min(left.sum(),right.sum())<5 or inner.sum()<3 or min(fractions)<.72:
        return None
    fit=robust_line(t[bracketing]-center,Y[bracketing])
    base=fit[0]
    if min(base[0],base[2])<=0:
        return None
    resid=Y-np.c_[np.ones(len(t)),t-center]@fit
    diffs=np.mean(resid[inner],axis=0)
    diffs=np.array([diffs[0],diffs[1],diffs[2],diffs[0]+diffs[1]])
    slide=np.column_stack((resid,np.sum(resid[:,:2],axis=1)))
    scatter=np.array([mad(slide[bracketing,k]) for k in range(4)])
    n=longest(-resid[inner,0]>max(.010*base[0],5*scatter[0]),t[inner],dt)
    dep=-diffs[0]/base[0]*1000
    if n<3 or dep<MIN_SAP_PPT or -diffs[0]<5*scatter[0]:
        return None
    restored=-diffs[3]/base[0]*1000
    errors=[]
    for k in range(4):
        v=slide[:,k]
        sigma=np.hypot(effective_error(v,inner,dt), effective_error(v,bracketing,dt))
        left_err=np.mean(v[left]); right_err=np.mean(v[right])
        # Baseline discrepancy guards against a curved or nonstationary shoulder.
        sigma=np.hypot(sigma,abs(right_err-left_err)/2)
        errors.append(sigma)
    err_rest=1000*errors[3]/base[0]
    bkg_ppt=1000*diffs[1]/base[0]
    closure_tol=max(MIN_RESTORE_PPT,.12*dep)
    pdc_ppt=-1000*diffs[2]/base[2]
    # Require a significant background excess and positive evidence of equivalence.
    excess=diffs[1]>max(5*errors[1],.005*base[0])
    pointwise=longest(-slide[inner,3]>max(.005*base[0],5*scatter[3]),t[inner],dt)
    if restored-3*err_rest>MIN_RESTORE_PPT or pointwise>=3:
        reason="retained_loss_with_background" if excess else "retained_loss"
    elif excess and restored < -MIN_RESTORE_PPT:
        reason="background_overclosure"
    elif excess and abs(restored)+3*err_rest<=closure_tol and pointwise<3:
        reason="background_closure"
    elif excess:
        reason="background_unresolved"
    else:
        reason="unexplained"
    segment_lim=min(fractions)>=.90
    return dict(btjd=float(center),half_h=24*half,bracket_outer_h=24*outer_lim,
                quality_full=bool(segment_lim), n_in=int(inner.sum()),n_left=int(left.sum()),n_right=int(right.sum()),
                left_fraction=fractions[0],core_fraction=fractions[1],right_fraction=fractions[2],
                min_consecutive_sap=n, min_consecutive_restored=pointwise,
                sap_loss_e_per_s=float(-diffs[0]),background_gain_e_per_s=float(diffs[1]),
                restored_loss_e_per_s=float(-diffs[3]),sap_baseline_e_per_s=float(base[0]),
                sap_depth_ppt=float(dep),pdc_depth_ppt=float(pdc_ppt),background_gain_ppt=float(bkg_ppt),
                restored_loss_ppt=float(restored),restored_sigma_ppt=float(err_rest),
                restored_lower_3sigma_ppt=float(restored-3*err_rest),
                restored_upper_3sigma_ppt=float(restored+3*err_rest),
                restored_point_scatter_ppt=float(scatter[3]/base[0]*1000),
                background_sigma_ppt=float(1000*errors[1]/base[0]),
                closure_tolerance_ppt=float(closure_tol),classification=reason)


def detect(data):
    t_raw=data["TIME"]
    q_raw=data["QUALITY"]
    total=np.isfinite(t_raw)
    good=(q_raw==0)&total
    for col in ("SAP_FLUX","SAP_BKG","PDCSAP_FLUX"):
        good &= np.isfinite(data[col])
    good&=(data["SAP_FLUX"]>0)&(data["PDCSAP_FLUX"]>0)
    t=t_raw[good]
    Y=np.column_stack([data[col][good] for col in ("SAP_FLUX","SAP_BKG","PDCSAP_FLUX")])
    dt=np.median(np.diff(t))
    split=np.flatnonzero(np.r_[True,np.diff(t)>8.5*dt,True])
    events=[]
    half_widths=np.unique(np.maximum(1,np.rint(FWHM_H/(48*dt)).astype(int)))
    usable=np.zeros(len(t),bool)
    full_scale_counts={float(h):0 for h in FWHM_H}
    for start,stop in zip(split[:-1],split[1:]):
        xs,ys=t[start:stop],Y[start:stop]
        if len(xs)<15:
            continue
        ps=np.r_[0,np.cumsum(ys[:,0])]
        scale_baseline=np.median(ys[:,0])
        for h in FWHM_H:
            half=max(1,round(h/(48*dt)))
            outer=int(np.ceil(2.75*(half+.1)))+14
            full_scale_counts[float(h)]+=max(0,len(xs)-2*outer)
        for half in half_widths:
            inner=max(half+2,int(np.ceil(1.45*half)))
            outer=int(np.ceil(2.75*(half+.1)))+14
            if len(xs)<=2*outer:
                continue
            usable[start+outer:stop-outer]=True
            i=np.arange(outer,len(xs)-outer)
            left=(ps[i-inner+1]-ps[i-outer])/(outer-inner+1)
            right=(ps[i+outer+1]-ps[i+inner])/(outer-inner+1)
            core=(ps[i+half+1]-ps[i-half])/(2*half+1)
            contrast=(np.minimum(left,right)-core)*1000/scale_baseline
            peaks=find_peaks(np.r_[0,contrast,0],height=7,distance=max(1,half))[0]-1
            for ix in i[peaks]:
                lo=ix-outer; hi=ix+outer+1
                event=measure(xs[lo:hi],ys[lo:hi],xs[ix],(half+.1)*dt,dt)
                if event is None:
                    continue
                event["segment_start_btjd"]=float(xs[0])
                event["segment_end_btjd"]=float(xs[-1])
                # Rank by total deficit to keep one event across durations.
                event["rank"]=event["sap_depth_ppt"]*np.sqrt(event["n_in"])
                events.append(event)
    ordered=sorted(events,key=lambda r:r["rank"],reverse=True)
    kept=[]
    for e in ordered:
        if any(abs(k["btjd"]-e["btjd"])*24 < k["half_h"]+e["half_h"] for k in kept):
            continue
        e.pop("rank")
        kept.append(e)
    coverage=dict(archive_cadences=len(t_raw),finite_time_cadences=int(total.sum()),
                  quality_zero_finite_usable=int(good.sum()),searchable_center_cadences=int(usable.sum()),
                  searchable_center_fraction=float(usable.mean()),cadence_minutes=float(dt*1440),
                  sector_start_btjd=float(t[0]),sector_end_btjd=float(t[-1]),
                  searchable_centers_by_full_width_h=full_scale_counts,
                  observing_segments=int(len(split)-1))
    return sorted(kept,key=lambda r:r["btjd"]),coverage


def with_context(records,meta,data):
    for r in records:
        near=abs(data["TIME"]-r["btjd"]).argmin() if np.all(np.isfinite(data["TIME"])) else np.nanargmin(abs(data["TIME"]-r["btjd"]))
        corr=data["TIMECORR"][near]
        time=Time(r["btjd"]-corr+2457000,format="jd",scale="tdb").utc.isot
        r.update(utc=time,**{k:meta[k] for k in ("tic","sector","lc_url","tpf_url","fits_sha256","camera","ccd")})
    return records


def run(job):
    tic,sector,product,cache=job
    try:
        data,meta=download(tic,sector,product,cache)
        events,cover=detect(data)
        return with_context(events,meta,data), dict(**meta,**cover)
    except Exception as exc:
        return [],dict(tic=tic,sector=sector,error=f"{type(exc).__name__}: {exc}")


def write_events(path,rows):
    pd.DataFrame(rows,columns=EVENT_FIELDS).to_csv(path,index=False)


def write_candidates(events,path):
    fields=["tic","sector","btjd","utc","classification","sap_depth_ppt","restored_loss_ppt","restored_sigma_ppt","lc_url","tpf_url","fits_sha256"]
    subset=[e for e in events if e["classification"].startswith("background_")]
    with path.open("w",newline="",encoding="utf8") as handle:
        w=csv.DictWriter(handle,fieldnames=fields,extrasaction="ignore")
        w.writeheader()
        w.writerows(subset)


def synthetic():
    rng=np.random.default_rng(12025)
    t=np.arange(3000,3004,2/1440)
    transit=np.exp(-.5*((t-3002)/.041)**2)
    result={}
    for name,astro in [("background_only",0),("mixed_eclipse_45_ppt",45),("mixed_eclipse_90_ppt",90)]:
        source=10000-astro*10*transit+rng.normal(0,7,len(t))
        background=1500+1450*transit+rng.normal(0,4,len(t))
        sap=source-(background-1500)
        data=dict(TIME=t,QUALITY=np.zeros(len(t),int),SAP_FLUX=sap,SAP_BKG=background,PDCSAP_FLUX=sap.copy())
        events,coverage=detect(data)
        result[name]=min(events,key=lambda e:abs(e["btjd"]-3002)) if events else {}
    return result


def main():
    import argparse
    p=argparse.ArgumentParser()
    p.add_argument("--controls",action="store_true",help="replay the known controls and synthetic checks")
    inputs = p.add_mutually_exclusive_group()
    inputs.add_argument("--coverage",type=Path,help="receipt of products, URLs and hashes to replay")
    inputs.add_argument("--index",type=Path,help="SPOC LC CSV or CSV.gz with tic, sector and file columns")
    p.add_argument("--batch",type=Path,help="TIC and pipe-delimited sector roster to use with --index")
    p.add_argument("--cache",type=Path,default=default_cache(),help="FITS cache directory, or set TESS_BACKGROUND_CACHE")
    p.add_argument("--output-dir",type=Path,default=Path("replay"),help="directory for generated CSV and JSON")
    a=p.parse_args()
    if a.batch and (not a.index or a.controls):
        p.error("--batch is for pilot selection with --index")
    tag="controls" if a.controls else "pilot"
    cache=a.cache.expanduser()
    dest=a.output_dir.expanduser()
    if dest.resolve()==HERE and any((HERE/f"{tag}-{suffix}").exists() for suffix in ("events.csv","coverage.json")):
        p.error("--output-dir must differ from the directory of the published results")
    if a.index:
        if a.controls:
            rows=CONTROLS
        else:
            roster=a.batch or next((path for path in (HERE/"batch.csv",HERE.parent/"batch.csv") if path.is_file()),None)
            if not roster:
                p.error("--batch is required with --index when there is no adjacent batch.csv")
            with roster.open(encoding="utf-8-sig",newline="") as handle:
                rows={int(r["tic"]):[int(s) for s in r["sectors"].split("|")] for r in csv.DictReader(handle)}
        files=index_for(set(rows),a.index)
        products={}
        for tic,sectors in rows.items():
            for sector in sectors:
                name=files.get((tic,sector))
                if name:
                    lc,mirror,tp=urls(tic,sector,name)
                    products[tic,sector]=dict(filename=name,lc_url=lc,lc_mirror_url=mirror,tpf_url=tp)
                else:
                    products[tic,sector]={}
    else:
        receipt=a.coverage or HERE/f"{tag}-coverage.json"
        if not receipt.is_file():
            p.error(f"no coverage receipt at {receipt}; provide --coverage or --index")
        products=read_products(receipt)
    cache.mkdir(parents=True,exist_ok=True)
    dest.mkdir(parents=True,exist_ok=True)
    jobs=[(t,s,product,cache) for (t,s),product in products.items()]
    all_events=[]
    coverage=[]
    with ThreadPoolExecutor(max_workers=12) as pool:
        for events,record in pool.map(run,jobs):
            coverage.append(record)
            all_events.extend(events)
            print(record.get("tic"),record.get("sector"),len(events),record.get("error",""),flush=True)
    write_events(dest/f"{tag}-events.csv",all_events)
    (dest/f"{tag}-coverage.json").write_text(json.dumps(coverage,indent=2,allow_nan=False),encoding="utf8")
    write_candidates(all_events,dest/f"{tag}-pixel-candidates.csv")
    if a.controls:
        (dest/"injection.json").write_text(json.dumps(synthetic(),indent=2,allow_nan=False),encoding="utf8")


if __name__=="__main__":
    main()
