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
