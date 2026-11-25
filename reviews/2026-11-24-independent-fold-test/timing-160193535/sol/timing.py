import csv
import hashlib
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import least_squares, minimize_scalar

HERE = Path(__file__).resolve().parent
MN = 1440
TIC = 160193535


def shape(x, half, power):
    return np.clip(1-(x/half)**2, 0, 1)**power


def event_model(p, time, raw_center, cadence, fixed=None):
    center, depth, base, slope = p[:4]
    half, power = fixed if fixed else p[4:]
    offsets = np.linspace(-.5,.5,19)*cadence
    profile = shape(time[:,None]-raw_center-center+offsets, half, power).mean(axis=1)
    return base+slope*(time-raw_center)-depth*profile


def fit_dip(t, y, center, cadence, fixed=None):
    mask = (abs(t-center)<.32) & np.isfinite(y)
    time, flux = t[mask], y[mask]
    base = np.nanmedian(flux[abs(time-center)>.20])
    if not np.isfinite(base):
        base = np.nanmedian(y)
    flux = flux/base
    p0 = [0., .18, 1., 0.] + ([] if fixed else [.103, 1.5])
    lo = [-.085,.065,.88,-.65] + ([] if fixed else [.075,.6])
    hi = [.085,.30,1.12,.65] + ([] if fixed else [.16,4.])
    fit = least_squares(lambda p: event_model(p,time,center,cadence,fixed)-flux,p0,
                        bounds=(lo,hi), loss="soft_l1", f_scale=.002, x_scale="jac")
    p = fit.x
    half, power = fixed if fixed else p[4:]
    return dict(center=center+p[0], depth=p[1]/p[2]*1000, half=half, power=power,
                residual_ppt=np.sqrt(np.mean(fit.fun**2))*1000)


def load_all():
    data = {}
    inventory = json.loads((HERE/"archive.json").read_text(encoding="utf8"))
    for r in inventory:
        with np.load(HERE / f'cadences/{TIC}-{r["sector"]}.npz') as f:
            t, a, b = (f[k] for k in ("t","sap","pdc"))
        use = np.isfinite(a)&np.isfinite(b)&(a>0)&(b>0)
        t,a,b=t[use],a[use],b[use]
        c=np.median(np.diff(t))
        data[r["sector"]] = (t,a,b,c)
        r.update(start_btjd=t[0],end_btjd=t[-1],cadence_min=c*MN,n_both=len(t))
        r["cadence_cache_sha256"] = hashlib.sha256((HERE / f'cadences/{TIC}-{r["sector"]}.npz').read_bytes()).hexdigest()
    return inventory,data


def coverage(t, center, cadence):
    windows = [(-.28,-.13),(-.10,.10),(.13,.28)]
    counts = [int(np.sum((t-center>=a)&(t-center<b))) for a,b in windows]
    fractions = [min(1.,n*cadence/(b-a)) for n,(a,b) in zip(counts,windows)]
    core = t[abs(t-center)<=.10]
    edges = np.r_[center-.10,core,center+.10]
    gaps = np.diff(edges)
    return counts, fractions, gaps.max()*MN, (None if not len(core) else core[0]), (None if not len(core) else core[-1])


def detect(data):
    seeds=[]
    for sector,(t,a,b,c) in data.items():
        deep = np.flatnonzero(b / np.median(b) < .955)
        for group in np.split(deep,np.where(np.diff(t[deep])>.25)[0]+1):
            if len(group)<2:
                continue
            center = (t[group[0]]+t[group[-1]])/2
            shallow = 1000*(1-np.min(b[group])/np.median(b))
            fit = fit_dip(t,b,center,c)
            cnt, frac, gap, _, _=coverage(t,fit["center"],c)
            seeds.append(dict(sector=sector, rough=center, estimate_depth=shallow,
                              family="primary" if shallow>180 else "secondary", free=fit,
                              fit_for_template=(min(frac)>.9 and c<.01 and gap<2*c*MN)))
    templates={}
    for family in ("primary","secondary"):
        subset=[v["free"] for v in seeds if v["family"]==family and v["fit_for_template"]]
        templates[family] = (float(np.median([v["half"] for v in subset])),
                             float(np.median([v["power"] for v in subset])))
    out=[]
    for seed in seeds:
        sector, rough, family = (seed[k] for k in ("sector","rough","family"))
        t,a,b,c=data[sector]
        sap=fit_dip(t,a,rough,c,templates[family])
        pdc=fit_dip(t,b,rough,c,templates[family])
        btjd=(sap["center"]+pdc["center"])/2
        counts, fractions, gap, first, last=coverage(t,btjd,c)
        status = "full" if min(fractions)>=.78 and gap<2.1*c*MN else "partial"
        out.append(dict(sector=sector,family=family,status=status,btjd=btjd,
                        sap_btjd=sap["center"],pdc_btjd=pdc["center"],
                        sap_depth_ppt=sap["depth"],pdc_depth_ppt=pdc["depth"],
                        pdc_residual_ppt=pdc["residual_ppt"],cadence_minutes=MN*c,
                        n_left=counts[0],n_core=counts[1],n_right=counts[2],
                        core_max_gap_min=gap,first_core_btjd=first,last_core_btjd=last))
    return pd.DataFrame(out),templates


def ephemeris(events):
    use=events[(events.status=="full")]
    elapsed=use.btjd.to_numpy()-2944.61
    sec=(use.family=="secondary").to_numpy()
    cyc=np.rint(elapsed/17.1488-.504*sec)
    X=np.c_[np.ones(len(use)),cyc,sec]
    center, period, lag=np.linalg.lstsq(X,elapsed,rcond=None)[0]
    diff=(elapsed-X@[center,period,lag])*MN
    return float(2944.61+center),float(period),float(lag),float(np.std(diff,ddof=3))


def predict(data, events, name, period, epoch, lags):
    out=[]
    for s,(t,a,b,c) in data.items():
        for family,lag in lags:
            lo=int(np.floor((t[0]-epoch-lag)/period))
            hi=int(np.ceil((t[-1]-epoch-lag)/period))
            for n in range(lo,hi+1):
                center=epoch+n*period+lag
                if not t[0]-.10 <= center <= t[-1]+.10:
                    continue
                count,frac,maxgap,first,last=coverage(t,center,c)
                m=(abs(t-center)<=.03)
                pdc=b/np.median(b)
                nearby = events.loc[(events.sector==s)&(abs(events.btjd-center)<.11)]
                nnear = nearby.loc[abs(nearby.btjd-center)<.012]
                prior = t[t<center]
                after = t[t>=center]
                covered= min(frac)>=.78 and maxgap<2.1*c*MN
                excess=1000*(1-np.median(pdc[m])) if m.any() else None
                if covered:
                    status = "eclipse" if len(nnear) else "displaced_eclipse" if len(nearby) else "blank"
                else:
                    status = "partial_eclipse" if len(nnear) else "partial_displaced" if len(nearby) else "gap_or_partial"
                out.append(dict(clock=name,sector=s,family=family,cycle=n,
                                predicted_btjd=center,status=status,coverage_full=covered,
                                nearest_event_btjd=float(nearby.btjd.iloc[0]) if len(nearby) else None,
                                nearest_event_family=nearby.family.iloc[0] if len(nearby) else None,
                                last_cadence_before_center=prior[-1] if len(prior) else None,
                                first_cadence_after_center=after[0] if len(after) else None,
                                n_left=count[0],n_core=count[1],n_right=count[2],
                                left_fraction=frac[0],core_fraction=frac[1],right_fraction=frac[2],
                                core_max_gap_min=maxgap,first_core_btjd=first,last_core_btjd=last,
                                pdc_median_core_drop_ppt=excess))
    return out


def score_detection(events,period,epoch,lags):
    residuals=[]
    for r in events.itertuples():
        residuals.append(min(abs((r.btjd-epoch-lag+period/2)%period-period/2) for _,lag in lags))
    return dict(max_abs_hours=24*max(residuals), rms_hours=24*np.sqrt(np.mean(np.array(residuals)**2)),
                number_within_0p11d=int(np.sum(np.array(residuals)<.11)),
                number_within_0p012d=int(np.sum(np.array(residuals)<.012)))


def alias_fit(events,period, distinguish=True):
    ref=2944.61
    prim=events.loc[events.family=="primary","btjd"].to_numpy()
    sec=events.loc[events.family=="secondary","btjd"].to_numpy()
    def best_phase(times):
        x=(times-ref)%period
        grid=np.linspace(0,period,2048,endpoint=False)
        cost=lambda phase: np.sum(((x-phase+period/2)%period-period/2)**2)
        g=grid[np.argmin([cost(v) for v in grid])]
        return minimize_scalar(cost,bounds=(g-period/1024,g+period/1024),method="bounded").x
    if distinguish:
        ep=best_phase(prim)
        lag=(best_phase(sec)-ep)%period
        return ref+ep,[("primary",0.),("secondary",lag)]
    ep=best_phase(np.r_[prim,sec])
    return ref+ep,[("merged",0.)]


def main():
    inventory, data=load_all()
    events,templates=detect(data)
    epoch, period, lag, scatter=ephemeris(events)
    leave_one_sector = {int(s):ephemeris(events[events.sector!=s]) for s in data}
    fit_lags=[("primary",0.),("secondary",lag)]
    events["cycle"] = np.rint((events.btjd-epoch-np.where(events.family=="secondary",lag,0))/period).astype(int)
    events["fit_btjd"]=epoch+events.cycle*period+np.where(events.family=="secondary",lag,0)
    events["oc_minutes"]=(events.btjd-events.fit_btjd)*MN
    main_aliases=[("17.15_d_two_families",period,epoch,fit_lags),
                  ("8.57_d_single_family",period/2,epoch+(.5*lag-period/4),[("merged",0.)]),
                  ("8.57_d_two_families",period/2,epoch,[("primary",0.),("secondary",lag% (period/2))]),
                  ("2x17.15_d_four_families",period*2,epoch,fit_lags+[(f"{label}_odd",phase+period) for label,phase in fit_lags])]
    for name,p in [("12.13261_d_two_families",12.13261),("4.29_d_two_families",period/4),
                   ("5.72_d_two_families",period/3),("3.43_d_two_families",period/5),
                   ("2x17.15_d_two_families",period*2)]:
        e, lags=alias_fit(events,p)
        main_aliases.append((name,p,e,lags))
    windows=[]
    metrics=[]
    for name,p,e,l in main_aliases:
        pred=predict(data,events,name,p,e,l)
        windows.extend(pred)
        score=score_detection(events,p,e,l)
        metrics.append(dict(clock=name,period_d=p,epoch_btjd=e,phase_lags_days=l,
                            n_windows=len(pred), status_counts=pd.Series([r["status"] for r in pred]).value_counts().to_dict(),**score))
    events.to_csv(HERE/"events.csv",index=False)
    pd.DataFrame(windows).to_csv(HERE/"coverage.csv",index=False)
    (HERE/"ephemeris.json").write_text(json.dumps(dict(period_d=period,primary_epoch_btjd=epoch,
                secondary_lag_days=lag,secondary_phase=lag/period,full_event_rms_minutes=scatter,
                templates=templates, clocks=metrics,products=inventory,
                leave_one_sector_out=leave_one_sector,
                leave_one_sector_fields=["epoch_btjd","period_d","secondary_lag_d","residual_std_min"]),indent=2,allow_nan=False))
    fig,axes=plt.subplots(1,2,figsize=(11,4.2),layout="constrained")
    for fam,color in [("primary","#1d6598"),("secondary","#b76320")]:
        on=events.family==fam
        for status,marker in [("full","o"),("partial","x")]:
            show=on&(events.status==status)
            axes[0].scatter(events.btjd[show],events.oc_minutes[show],marker=marker,color=color,label=f"{fam}, {status}")
        for s,(t,_,f,_) in data.items():
            for r in events[on&(events.sector==s)].itertuples():
                ok=abs(t-r.btjd)<.18
                axes[1].plot((t[ok]-r.btjd)*24,1000*(f[ok]/np.nanmedian(f)-1),'.',ms=2,alpha=.27,color=color)
    axes[0].axhline(0,color=".5",lw=.8)
    axes[0].set(xlabel="BTJD",ylabel="Observed minus calculated (minutes)")
    axes[0].legend(fontsize=8)
    axes[1].set(xlabel="Hours from independently fitted event center",ylabel="PDCSAP relative flux (ppt)")
    fig.savefig(HERE/"timing.png",dpi=165)
    print(json.dumps(dict(ep=[epoch,period,lag,scatter],clocks=metrics),indent=2))


if __name__ == "__main__":
    main()
