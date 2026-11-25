"""Test TIC 388158330 against the Gaia SB1 orbit and cached ground photometry."""
import argparse
import csv
import gzip
import sys
from pathlib import Path

from astropy.coordinates import EarthLocation, SkyCoord
from astropy.time import Time
from astropy.timeseries import LombScargle
import astropy.units as u
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/"batch06"))
from review_lane import add_panel, csv_read, csv_write, load_curve

TIC = "388158330"
EVENTS = [(54,2784.4596037103465),(81,3509.6499910103466)]
WIDTH = .48
ASAS_PERIOD = 30.177


def orbit():
    row, = csv_read(HERE/f"{TIC}-gaia-orbit.csv")
    names = ["period","eccentricity","arg_periastron","t_periastron"]
    value = np.array([float(row[k]) for k in names])
    sigma = np.array([float(row[k+"_error"]) for k in names])
    assert row["bit_index"] == "127" and row["nss_solution_type"] == "SB1"
    full = np.eye(6)
    i,j = np.tril_indices(6,-1)
    full[i,j] = np.fromstring(row["corr_vec"].strip("()"),sep=",")
    full[j,i] = full[i,j]
    # Gaia SB1 covariance order is P, gamma, K, eccentricity, omega, T0.
    ix = [0,3,4,5]
    cov = full[np.ix_(ix,ix)]*np.outer(sigma,sigma)
    draws = np.random.default_rng(int(TIC)).multivariate_normal(value,cov,20000)
    draws = draws[(draws[:,0]>0)&(draws[:,1]>=0)&(draws[:,1]<1)]
    ref = Time(2016,format="jyear",scale="tcb").jd
    results = []
    for sector,t in EVENTS:
        dt = Time(2457000+t,format="jd",scale="tdb").tcb.jd-ref
        for deg in (0,90,270):
            def oc(parameters):
                p,e,w,peri = np.asarray(parameters).T
                half_true_anomaly = np.deg2rad(deg-w)/2 if deg else np.zeros_like(p)
                anomaly = 2*np.arctan2(np.sqrt(1-e)*np.sin(half_true_anomaly),
                                       np.sqrt(1+e)*np.cos(half_true_anomaly))
                offset = p*(anomaly-e*np.sin(anomaly))/(2*np.pi)
                return (dt-peri-offset+p/2)%p-p/2
            nominal = oc(value)
            sampled = nominal+(oc(draws)-nominal+value[0]/2)%value[0]-value[0]/2
            lo,hi = np.quantile(sampled,[.025,.975])
            results.append(dict(sector=sector,center_btjd=t,event="conjunction" if deg else "periastron",
                                longitude_deg=deg if deg else "",nominal_oc_d=nominal,lo95_d=lo,hi95_d=hi,
                                overlaps_core=bool(lo<=WIDTH/2 and hi>=-WIDTH/2)))
    csv_write(HERE/f"{TIC}-orbit-timing.csv",results)
    return value, results


def ground(cache):
    data = {}
    with gzip.open(cache/f"asassn-{TIC}.csv.gz","rt",encoding="utf-8") as stream:
        for r in csv.DictReader(stream):
            if r["quality"] != "G":
                continue
            t,m,e = (float(r[k]) for k in ("jd","mag","mag_err"))
            if not np.isfinite(t+m+e) or not 0<e<.1:
                continue
            key = r["phot_filter"],r["camera"],int(t//365.25)
            data.setdefault(key,[]).append((t,m))
    fixed = {}
    for (band,_,_), values in data.items():
        if len(values) < 8:
            continue
        t,m = np.array(values).T
        fixed.setdefault(band,[]).extend(zip(t,m-np.median(m)))
    result = {}
    for band, samples in fixed.items():
        nights = {}
        for t,m in samples:
            nights.setdefault(int(t+.5),[]).append((t,m))
        t,m = np.array([np.median(v,axis=0) for v in nights.values()]).T
        loc = EarthLocation.from_geocentric(0,0,0,unit=u.m)
        time = Time(t,format="jd",scale="utc",location=loc)
        coord = SkyCoord(300.09602107790806,15.167031083836694,unit="deg")
        btjd = (time.tdb+time.light_travel_time(coord)).jd-2457000
        result[band] = btjd,m*1000
    return result


def contrasts(series, tests):
    evidence = []
    for band,(t,resid) in series.items():
        for name,p,e in tests:
            k = np.rint((t-e)/p).astype(int)
            dt = t-e-k*p
            core = abs(dt)<WIDTH/2
            wing = (abs(dt)>=WIDTH/2)&(abs(dt)<=1.5*WIDTH)
            outside = ~core&~wing
            row = dict(band=band,clock=name,period_d=p,epoch_btjd=e,width_d=WIDTH,night_count=len(t),
                       core_nights=int(core.sum()),wing_nights=int(wing.sum()),core_cycles=len(np.unique(k[core])),
                       outside_mad_mmag=1.4826*np.median(abs(resid[outside]-np.median(resid[outside]))),
                       depth_mmag="",lo95_mmag="",hi95_mmag="")
            if core.sum()>=5 and wing.sum()>=10 and len(np.unique(k[core]))>=4:
                c = resid[core]
                w = resid[wing]
                row["depth_mmag"] = np.median(c)-np.median(w)
                cycles = np.unique(k[core|wing])
                blocks = [(resid[core&(k==cycle)],resid[wing&(k==cycle)]) for cycle in cycles]
                rng = np.random.default_rng(388158330)
                boot = []
                for chosen in rng.integers(0,len(cycles),size=(1500,len(cycles))):
                    c = np.concatenate([blocks[i][0] for i in chosen])
                    w = np.concatenate([blocks[i][1] for i in chosen])
                    if len(c)*len(w):
                        boot.append(np.median(c)-np.median(w))
                row["lo95_mmag"],row["hi95_mmag"] = np.quantile(boot,[.025,.975])
            evidence.append(row)
    csv_write(HERE/f"{TIC}-ground-contrasts.csv",evidence)


def diagnostics(root, series, tests):
    fig,axes=plt.subplots(2,2,figsize=(10,6))
    rows=[]
    for ax,(sector,t) in zip(axes[0],EVENTS):
        curve = load_curve(root/f"sky/data/qlp-sb-p20-60/{TIC}_s{sector:03d}.fits",{})
        add_panel(ax,curve,t,WIDTH,f"S{sector} at {t:.4f} BTJD | SAP blue, corrected orange")
    periods = np.linspace(25,35,3000)
    for ax,(band,(t,m)) in zip(axes[1],series.items()):
        ls=LombScargle(t,m)
        power=ls.power(1/periods)
        top=int(np.argmax(power))
        for label,p,_ in tests:
            if 25<p<35:
                amplitudes = ls.model_parameters(1/p)[1:]
                rows.append(dict(band=band,period_type=label,period_d=p,power=float(ls.power(1/p)),
                                 semi_amplitude_mmag=np.linalg.norm(amplitudes)))
        rows.append(dict(band=band,period_type="ground_peak_25_to_35_d",period_d=periods[top],power=power[top],
                         semi_amplitude_mmag=np.linalg.norm(ls.model_parameters(1/periods[top])[1:])))
        for half, sel in (("early",t<np.median(t)),("late",t>=np.median(t))):
            score=LombScargle(t[sel],m[sel]).power(1/periods)
            imax=int(np.argmax(score))
            rows.append(dict(band=band,period_type=f"ground_{half}_peak_25_to_35_d",
                             period_d=periods[imax],power=score[imax],semi_amplitude_mmag=""))
        ax.plot(periods,power,c="#28457d")
        ax.axvline(ASAS_PERIOD,c="#d7803e",label="ASAS-SN catalog period")
        ax.set(xlabel="Period (days)",ylabel="Lomb–Scargle power",title=f"ASAS-SN {band}")
        ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(HERE/"plots"/f"{TIC}-orbit-ground.png",dpi=120)
    plt.close(fig)
    csv_write(HERE/f"{TIC}-ground-periodogram.csv",rows)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ground_cache",type=Path)
    parser.add_argument("--root",type=Path,default=Path.cwd())
    a=parser.parse_args()
    pars,timing=orbit()
    p=pars[0]
    first,last=(x[1] for x in EVENTS)
    near_phase=next(r["nominal_oc_d"] for r in timing if r["sector"]==54 and r["longitude_deg"]==270)
    other_phase=next(r["nominal_oc_d"] for r in timing if r["sector"]==54 and r["longitude_deg"]==90)
    tests=[("tess_pair_31_cycles",(last-first)/31,first),("tess_pair_24_cycles",(last-first)/24,first),
           ("gaia_period_assumed_tess_phase",p,first),("gaia_270_deg_conjunction",p,first-near_phase),
           ("gaia_90_deg_conjunction",p,first-other_phase),
           ("asassn_catalog_period_assumed_tess_phase",ASAS_PERIOD,first)]
    series=ground(a.ground_cache)
    contrasts(series,tests)
    diagnostics(a.root,series,tests)


if __name__=="__main__":
    main()
