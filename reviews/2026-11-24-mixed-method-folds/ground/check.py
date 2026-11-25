"""Test fixed TESS predictions in ground surveys and search a disjoint ground holdout."""
import argparse
from pathlib import Path

import astropy.units as u
from astropy.coordinates import EarthLocation, SkyCoord
from astropy.time import Time
from astropy.utils import iers
import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
PALOMAR = EarthLocation.from_geodetic(-116.865, 33.3563, 1712 * u.m)
iers.conf.auto_download = False


def observations(tic, cache):
    for survey, path in (("ASAS-SN", cache/f"asassn-{tic}.csv.gz"), ("ZTF", cache/f"{tic}.csv.gz")):
        if not path.exists():
            continue
        d = pd.read_csv(path)
        if d.empty:
            continue
        if survey == "ASAS-SN":
            d = d[(d.quality=="G") & (d.mag_err>0) & (d.mag_err<.2)].copy()
            d["btjd_approx"] = d.jd-2457000
            keys = ["asas_sn_id", "phot_filter"]
        else:
            d = d[(d.catflags==0) & (d.magerr>0) & (d.magerr<.2)].copy()
            coord=SkyCoord(np.median(d.ra),np.median(d.dec),unit="deg")
            tm = Time(d.mjd.to_numpy()+d.exptime.to_numpy()/172800,format="mjd",scale="utc",location=PALOMAR)
            d["btjd_approx"]=(tm.tdb+tm.light_travel_time(coord)).jd-2457000
            d["mag_err"]=d.magerr
            d["camera"]="ZTF"
            keys=["oid","filtercode"]
        for (oid, band), group in d.groupby(keys):
            parts=[]
            for _, cam in group.groupby("camera"):
                cam=cam[np.isfinite(cam.mag)].copy()
                if len(cam)>=15:
                    cam["residual"]=cam.mag-np.median(cam.mag)
                    parts.append(cam)
            if parts and sum(len(c) for c in parts)>=30:
                q=pd.concat(parts).sort_values("btjd_approx")
                yield dict(survey=survey,object_id=str(oid),band=band), q.btjd_approx.to_numpy(), q.residual.to_numpy(), q.mag_err.to_numpy()


def sample(t, y, period, epoch, half):
    phase = (t-epoch)/period
    cycle = np.rint(phase).astype(int)
    use = abs((phase-cycle)*period)<=half
    cs = np.unique(cycle[use])
    values = [float(np.median(y[use & (cycle==n)])) for n in cs]
    return np.array(values), int(use.sum())


def assess(t, y, err, period, epoch, half):
    levels, n = sample(t,y,period,epoch,half)
    scatter=max(.005,float(np.median(err)),float(1.4826*np.median(abs(y-np.median(y)))))
    depth=float(np.median(levels)) if len(levels) else None
    shifts=[]
    for phase in np.arange(1,101)/101:
        if min(phase,1-phase)*period<2*half:
            continue
        v,_=sample(t,y,period,epoch+phase*period,half)
        if len(v)>=3:
            shifts.append(np.median(v))
    rank=float(np.mean(np.array(shifts)<depth)) if shifts and depth is not None else None
    positive=(len(levels)>=4 and depth>=3*scatter and len(shifts)>=40 and rank>=.95)
    return dict(observations=len(t),points_in_core=n,cycles=len(levels),depth_mag=depth,
                robust_scatter_mag=scatter,shifted_comparisons=len(shifts),fraction_shifted_shallower=rank,
                passes=bool(positive))


def heldout(t,y,err,p,width):
    # Pick one phase in the early time interval; evaluate that single prediction in the late interval.
    early=t < np.median(t)
    if min(early.sum(),(~early).sum())<30:
        return {}
    half=min(.04*p,.36*width)
    # Centering bin grid at the first exposure is independent of flux.
    epoch=t[0]
    candidates=[]
    for x in np.arange(256)/256:
        e=epoch+p*x
        v,_=sample(t[early],y[early],p,e,half)
        if len(v)>=4:
            candidates.append((np.median(v),e,len(v)))
    if not candidates:
        return {}
    depth,e,cycles=max(candidates)
    check=assess(t[~early],y[~early],err[~early],p,e,half)
    return dict(period_d=p,selected_epoch=e,halfwidth_d=half,training_depth_mag=depth,training_cycles=cycles,
                split_btjd=float(np.median(t)),**check)


def run(cache, extra):
    batch=pd.read_csv(HERE.parent/"batch.csv",dtype={"tic":str})
    clocks=pd.read_csv(HERE/"archived-clocks.csv",dtype={"tic":str})
    if extra:
        clocks=pd.concat([clocks,pd.read_csv(extra,dtype={"tic":str})],ignore_index=True)
    fixed=[]; validation=[]; summary=[]
    for star in batch.itertuples():
        targets=clocks[clocks.tic==star.tic]
        groups=list(observations(star.tic,cache))
        checks=[]
        for ids,t,y,err in groups:
            for row in targets.itertuples():
                half=min(.04*row.period_d,.36*row.duration_d)
                a=assess(t,y,err,row.period_d,row.epoch_btjd,half)
                a.update(tic=star.tic,**ids,clock_source=row.clock_source,period_d=row.period_d,
                         epoch_btjd=row.epoch_btjd,halfwidth_d=half)
                if ids["survey"]=="ASAS-SN":
                    for dt,label in [(-.008,"minus"),(.008,"plus")]:
                        b=assess(t,y,err,row.period_d,row.epoch_btjd+dt,half)
                        a[label+"_cycles"]=b["cycles"]
                        a[label+"_pass"]=b["passes"]
                checks.append(a)
            arch=targets.iloc[0]
            b=heldout(t,y,err,star.gaia_period_days,arch.duration_d)
            if b:
                validation.append(dict(tic=star.tic,**ids,**b))
        fixed.extend(checks)
        primary=[a for a in checks if a["clock_source"]=="archived_TESS"]
        robust=[a for a in primary if a["passes"] and a.get("minus_pass",True) and a.get("plus_pass",True)]
        eligible=[a for a in primary if a["cycles"]>=4 and a["shifted_comparisons"]>=40]
        summary.append(dict(tic=star.tic,series=len(groups),ground_observations=sum(len(t) for _,t,_,_ in groups),
                            ztf_good=sum(len(t) for ids,t,_,_ in groups if ids["survey"]=="ZTF"),
                            asassn_good=sum(len(t) for ids,t,_,_ in groups if ids["survey"]=="ASAS-SN"),
                            max_cycles=max((a["cycles"] for a in primary),default=0),
                            fixed_test_status="recovered" if robust else "no_recovery" if eligible else "insufficient_core_or_control_coverage",
                            robust_series_clocks=len(robust),
                            secondary_clocks_passing="|".join(sorted({a["clock_source"] for a in checks if
                                a["clock_source"]!="archived_TESS" and a["passes"] and a.get("minus_pass",True) and a.get("plus_pass",True)}))))
    pd.DataFrame(fixed).to_csv(HERE/"phase-checks.csv",index=False)
    pd.DataFrame(validation).to_csv(HERE/"ground-holdout.csv",index=False)
    pd.DataFrame(summary).to_csv(HERE/"outcomes.csv",index=False)


if __name__ == "__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("cache",type=Path)
    parser.add_argument("--extra",type=Path,help="Additional TESS-only clock CSV with same columns")
    args=parser.parse_args()
    run(args.cache,args.extra)
