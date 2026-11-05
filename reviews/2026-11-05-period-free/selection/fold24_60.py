"""Bounded 24--60 d cached Gaia period-fold screen.

Input sealed pilot JSON: targets keyed by TIC with gaia and files (paths).
No fetching or selection here. All successful and failed attempts persist.
"""
from pathlib import Path
import argparse
import hashlib
import json
import time
import numpy as np
from astropy.io import fits
from astropy.timeseries import BoxLeastSquares

DUR = np.array([.04, .07, .12, .20, .32, .50])
CONFIG = dict(period_bounds_days=[24,60], null_bounds_days=[.6,60],
              null_draws=128, seed='int(TIC) modulo 2**32',
              durations_days=DUR.tolist(), quality=0, gap_days=.2,
              edge_pad_days=.5, bin_days=10/1440, flatten_days=2.,
              flare_upper_mad=4, min_points_before_and_after_edges=200,
              narrow_halfwidth='max(5*period_error,0.001*period)',
              period_grid_min=100, period_grid_max=1600,
              flag='z >= 5 OR (depth_ppm > 5000 AND snr > 3*null_median > 0)',
              flux='KSPSAP_FLUX if present, otherwise SAP_FLUX',
              purpose='screening only; raw-flux review required')

def sha(p):
    h=hashlib.sha256()
    with Path(p).open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
    return h.hexdigest()

def prep(path,tic,expected_hash):
    if sha(path) != expected_hash:raise ValueError('frozen FITS hash mismatch')
    with fits.open(path) as h:
        assert int(h[0].header['TICID'])==int(tic)
        d=h[1].data
        col='KSPSAP_FLUX' if 'KSPSAP_FLUX' in d.columns.names else 'SAP_FLUX'
        mask=np.isfinite(d['TIME']) & np.isfinite(d[col]) & (d['QUALITY']==0)
        t=np.array(d['TIME'][mask],dtype=float)
        f=np.array(d[col][mask],dtype=float)
        sector=int(h[0].header['SECTOR'])
    info=dict(path=str(path),sha256=sha(path),sector=sector,flux_column=col,n_quality=int(len(t)))
    if len(t)<200:return None,dict(info,status='insufficient_quality_cadences')
    if np.any(np.diff(t)<0):raise ValueError('nonmonotonic times')
    median=np.median(f)
    if not np.isfinite(median) or median<=0:raise ValueError('invalid flux median')
    f=f/median
    dt=np.diff(t);starts=np.r_[t[0],t[1:][dt>.2]];ends=np.r_[t[:-1][dt>.2],t[-1]]
    m=np.ones(len(t),bool)
    for a,b in zip(starts,ends):m &= ~((t>=a)&(t<a+.5)) & ~((t>b-.5)&(t<=b))
    t,f=t[m],f[m]
    if len(t)<200:return None,dict(info,status='insufficient_after_edge_mask',n_edges=int(len(t)))
    w=10/1440
    if np.median(np.diff(t))<=.8*w:
        k=np.floor((t-t[0])/w).astype(int);_,inv,n=np.unique(k,return_inverse=True,return_counts=True)
        t,f=np.bincount(inv,t)/n,np.bincount(inv,f)/n
    lo=np.searchsorted(t,t-1);hi=np.searchsorted(t,t+1)
    trend=np.array([np.median(f[a:b]) for a,b in zip(lo,hi)])
    if np.any(~np.isfinite(trend)) or np.any(trend<=0):raise ValueError('invalid flatten trend')
    f=f/trend;r=f-1;s=1.4826*np.median(np.abs(r-np.median(r)))
    if not np.isfinite(s) or s<=0:raise ValueError('zero or invalid noise scale')
    m=r<4*s;t,f=t[m],f[m]
    return (t,f,np.full(len(t),s)),dict(info,status='ok',n_used=int(len(t)),scatter=float(s))

def window(p,sig,base):
    w=max(5*sig,.001*p)
    n=int(min(1600,max(100,2*w/(.25*.04*p/base))))
    grid=np.linspace(p-w,p+w,n)
    if grid.min()<=DUR.max():raise ValueError('uncertain period window intersects durations')
    return grid

def one(tic,tg):
    parts=[];receipts=[]
    for item in tg['files']:
        p=item['path']
        try:r,rec=prep(p,tic,item['sha256'])
        except Exception as ex:r=None;rec=dict(path=str(p),status='unavailable',error=repr(ex))
        receipts.append(rec)
        if r is not None:parts.append(r)
    out=dict(tic=tic,control=bool(tg.get('control')),files=receipts)
    if not parts:return dict(out,status='no_usable_data')
    sectors=[r['sector'] for r in receipts if r['status']=='ok']
    if len(set(sectors))!=len(sectors):raise ValueError('duplicate sectors: choose one product per sector')
    t,f,e=[np.concatenate([r[i] for r in parts]) for i in range(3)]
    order=np.argsort(t);t,f,e=t[order],f[order],e[order]
    p=float(tg['gaia']['period']);sig=float(tg['gaia'].get('period_error') or 0)
    assert 24<=p<60,(tic,p)
    assert np.isfinite(sig) and sig>=0
    base=float(np.ptp(t));bls=BoxLeastSquares(t,f,e)
    out.update(status='ok',P_gaia=p,n=len(t),base=base,sig_ppm=float(1e6*np.median(e)))
    for tag,pc,err in [('P',p,sig),('P2',p/2,sig/2)]:
        grid=window(pc,err,base);r=bls.power(grid,DUR,objective='snr');i=int(np.argmax(r.power))
        out[tag]=dict(P=float(grid[i]),snr=float(r.power[i]),depth=float(1e6*r.depth[i]),
                      dur=float(r.duration[i]),t0=float(r.transit_time[i]),
                      grid_low=float(grid[0]),grid_high=float(grid[-1]),grid_count=len(grid))
    rng=np.random.default_rng(int(tic)%2**32)
    pn=np.exp(rng.uniform(np.log(.6),np.log(60),128));pn=pn[np.abs(np.log(pn/p))>.02]
    powers=bls.power(pn,DUR,objective='snr').power
    med=float(np.median(powers));mad=float(1.4826*np.median(np.abs(powers-med)))
    out.update(null_med=med,null_mad=mad,null_max=float(np.max(powers)),null_count=len(pn),null_periods=pn.tolist())
    for tag in ['P','P2']:
        b=out[tag];b['z']=(b['snr']-med)/mad if mad>0 else None
        b['flag']=(b['z'] is not None and b['z']>=5) or (b['depth']>5000 and med>0 and b['snr']>3*med)
    out['flag']=any(out[tag]['flag'] for tag in ['P','P2'])
    # Same established harmonic subtraction, without a network-dependent veto.
    best=max(['P','P2'],key=lambda k:out[k]['z'] if out[k]['z'] is not None else -np.inf)
    b=out[best];physical_period=b['P']*(2 if best=='P2' else 1)
    phase=2*np.pi*t/physical_period
    A=np.vstack([np.ones_like(t),np.sin(phase),np.cos(phase),np.sin(2*phase),np.cos(2*phase)]).T
    c,*_=np.linalg.lstsq(A,f,rcond=None);res=f-A@c+1
    rr=BoxLeastSquares(t,res,e).power(np.linspace(b['P']*(1-2e-5),b['P']*(1+2e-5),21),DUR,objective='snr')
    i=int(np.argmax(rr.power))
    out['harmonic_check']=dict(best_tag=best,snr_resid=float(rr.power[i]),depth_resid_ppm=float(1e6*rr.depth[i]),sin1_ppm=float(1e6*np.hypot(c[1],c[2])),sin2_ppm=float(1e6*np.hypot(c[3],c[4])))
    return out

def main():
    ap=argparse.ArgumentParser();ap.add_argument('pilot',type=Path);ap.add_argument('--limit',type=int);args=ap.parse_args()
    pilot=json.loads(args.pilot.read_text(encoding='utf-8'));targets=pilot['targets'];outdir=args.pilot.parent
    seal=dict(pilot_sha256=sha(args.pilot),runner_sha256=sha(__file__),config=CONFIG)
    sealpath=outdir/'run-seal.json'
    if sealpath.exists():assert json.loads(sealpath.read_text())==seal,'Run inputs changed'
    else:sealpath.write_text(json.dumps(seal,indent=2)+'\n',encoding='utf-8')
    out=outdir/'screening.jsonl';done={json.loads(l)['tic'] for l in out.read_text().splitlines()} if out.exists() else set()
    count=0
    with out.open('a',encoding='utf-8') as f:
        for tic,tg in targets.items():
            if tic in done:continue
            if args.limit is not None and count>=args.limit:break
            start=time.time()
            try:r=one(tic,tg)
            except Exception as ex:r=dict(tic=tic,status='failed',error=repr(ex))
            r['elapsed_seconds']=time.time()-start
            f.write(json.dumps(r,allow_nan=False)+'\n');f.flush();count+=1
            print(tic,r['status'],'flag',r.get('flag'),'seconds',round(r['elapsed_seconds'],1),flush=True)

if __name__=='__main__':main()
