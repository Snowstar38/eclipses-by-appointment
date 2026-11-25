"""Search early-sector photometry for a periodic signal and check it at fixed later times."""
import argparse
import csv
import json
import warnings
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

from astropy.io import fits
from astropy.timeseries import BoxLeastSquares, LombScargle
import numpy as np
from scipy.ndimage import median_filter
from scipy.signal import find_peaks
from scipy.stats import binned_statistic

HERE = Path(__file__).resolve().parent
MASK = {2:{38490},3:{38491},4:{38482}}


def read(path):
    with fits.open(path) as h:
        sector = h[0].header['SECTOR']
        z = h[1].data
        cor = 'KSPSAP_FLUX' if 'KSPSAP_FLUX' in z.names else 'DET_FLUX'
        ok = (z['QUALITY']==0) & np.isfinite(z['TIME'])
        if sector==26:
            ok &= ~np.isin(z['CADENCENO'],list(MASK.get(h[0].header['CAMERA'],())))
        for name in ('SAP_FLUX',cor):
            ok &= np.isfinite(z[name]) & (z[name]>0)
        if ok.sum()<100:
            return None
        t=z['TIME'][ok]
        edges=np.arange(t.min()-.0125,t.max()+.026,.025)
        y=np.array([binned_statistic(t,z[name][ok],statistic='median',bins=edges)[0] for name in ('SAP_FLUX',cor)])
    t=(edges[1:]+edges[:-1])/2
    good=np.isfinite(y).all(axis=0)
    if good.sum()<50:
        return None
    # Gap interpolation is used for the running continuum only.
    detrend=[]
    for channel in y:
        fill=np.interp(t,t[good],channel[good])
        detrend.append(1000*(channel[good]/median_filter(fill,size=121,mode='nearest')[good]-1))
    return sector,t[good],np.array(detrend)


def proposals(t,y,periods):
    span=np.ptp(t)
    step=.20/span
    freq=np.arange(.012,12.1,step)
    base=freq[(freq>=1/64)&(freq<=3.9)]
    guesses=list(periods)
    for channel in y:
        # Limit individual excursions for discovery; all event depths use unclipped samples.
        clipped=np.clip(channel,*np.quantile(channel,[.004,.996]))
        power=LombScargle(t,clipped).power(freq,method='fast',assume_regular_frequency=True)
        summed=sum(np.interp(base*h,freq,power)/np.sqrt(h) for h in (1,2,3))
        peaks=find_peaks(summed)[0]
        ranked=peaks[np.argsort(summed[peaks])[::-1]]
        retained=[]
        for idx in ranked:
            f=base[idx]
            if all(abs(f-a)>1.4/span for a in retained):
                retained.append(f)
            if len(retained)==5:break
        guesses.extend(1/f for f in retained)
    return np.array(sorted(set(round(p,8) for p in guesses if .25<p<68)))


def windows(parts,channel,p,epoch,w,sign,training):
    rows=[]
    for sector,t,ys in parts:
        for n in range(int(np.ceil((t[0]-epoch)/p)),int(np.floor((t[-1]-epoch)/p))+1):
            center=epoch+n*p
            a,b=np.searchsorted(t,[center-2*w,center+2*w])
            d=t[a:b]-center
            masks=(abs(d)<=w/2,(d>=-1.75*w)&(d<-.65*w),(d>.65*w)&(d<=1.75*w))
            if any(m.sum()<max(2,.60*w/.025) for m in masks):continue
            im,l,r=masks
            if np.max(np.diff(np.r_[-w/2,d[im],w/2]))>max(.035,.4*w):continue
            depth=[]
            scatter=[]
            for y in ys[:,a:b]:
                baseline=np.interp(d,[np.median(d[l]),np.median(d[r])],[np.median(y[l]),np.median(y[r])])
                residual=sign*(baseline-y)
                depth.append(float(np.median(residual[im])))
                side=residual[l|r]
                scatter.append(float(max(.12,1.4826*np.median(abs(side-np.median(side))))))
            rows.append((sector,sector in training,n,center,*depth,*scatter))
    return rows


def search(job):
    row,folder=job
    tic=row['tic']
    parts=[v for f in sorted(folder.glob(tic+'_s*.fits')) if (v:=read(f)) is not None]
    if len(parts)<2:return dict(tic=tic,clocks=[])
    split=max(1,min(len(parts)-1,round(len(parts)*.62)))
    training={x[0] for x in parts[:split]}
    t=np.concatenate([x[1] for x in parts[:split]])
    y=np.concatenate([x[2] for x in parts[:split]],axis=1)
    seeds=[float(row[k]) for k in ('gaia_period_days','pilot_period_d','fold_screening_period_days') if row.get(k)]
    periods=proposals(t,y,seeds)
    pgrid=np.unique(np.concatenate([1/(1/p+np.linspace(-.68,.68,19)/np.ptp(t)) for p in periods]))
    pgrid=pgrid[(pgrid>.25)&(pgrid<70)]
    sign=-1 if row['priority_group']=='brightening_lead' else 1
    fits_found=[]
    for ch in (0,1):
        z=sign*np.clip(y[ch],*np.quantile(y[ch],[.002,.998]))
        bls=BoxLeastSquares(t,z)
        fitted=[]
        for low,high,widths in ((.25,1.1,[.055,.085,.14]),(1.1,5,[.075,.14,.24]),(5,71,[.12,.28,.55,1.0])):
            candidates=pgrid[(pgrid>=low)&(pgrid<high)]
            if not len(candidates):continue
            result=bls.power(candidates,widths,oversample=5)
            for i in np.argsort(result.power)[::-1][:min(35,len(candidates))]:
                fitted.append(tuple(float(k[i]) for k in (result.power,result.period,result.transit_time,result.duration)))
        keep=[]
        for power,p,e,w in sorted(fitted,reverse=True):
            if all(abs(1/p-1/q)>.9/np.ptp(t) for q in keep):
                keep.append(p)
                meas=windows(parts,ch,p,e,w,sign,training)
                item=dict(channel=('SAP','corrected')[ch],period_d=p,epoch_btjd=e,width_d=w,
                          sign=('brightening' if sign==-1 else 'dip'),power=power)
                for label,flag in [('train',True),('test',False)]:
                    subset=[a for a in meas if a[1]==flag]
                    depths=np.array([a[4+ch] for a in subset])
                    passes=[a for a in subset if a[4+ch]>max(.6,1.2*a[6+ch])]
                    item.update({label+'_covered':len(subset),label+'_hits':len(passes),
                                 label+'_hit_sectors':len(set(a[0] for a in passes)),
                                 label+'_median_ppt':round(float(np.median(depths)),4) if len(depths) else None})
                fits_found.append(item)
            if len(keep)==2:break
    return dict(tic=tic,train_sectors=sorted(training),test_sectors=[a[0] for a in parts[split:]],clocks=fits_found)


if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('cache',type=Path)
    ap.add_argument('--workers',type=int,default=3)
    ap.add_argument('--roster',type=Path,default=HERE.parent/'roster.csv')
    ap.add_argument('--output',type=Path,default=HERE/'trials')
    a=ap.parse_args()
    a.output.mkdir(parents=True,exist_ok=True)
    with a.roster.open() as f: rows=list(csv.DictReader(f))
    pending=[(r,a.cache) for r in rows if not (a.output/(r['tic']+'.json')).exists()]
    with ProcessPoolExecutor(a.workers) as pool:
        for r in pool.map(search,pending):
            (a.output/(r['tic']+'.json')).write_text(json.dumps(r,indent=1,allow_nan=False)+'\n')
            print(r['tic'],flush=True)
