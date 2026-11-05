"""Reproduce bounded raw-SAP windows, coverage, and local eclipse fits for F011-F020."""
import csv, hashlib, json
from pathlib import Path
import numpy as np
from astropy.io import fits
from scipy.optimize import least_squares
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

B=Path(__file__).resolve().parent
ROOT=B.parent
ROWS=list(csv.DictReader((B/'queue.csv').open(newline='',encoding='utf-8')))

def trap(p,x):
    base,slope,depth,center,width,ingress=p
    return base+slope*x-depth*np.clip((width/2-np.abs(x-center))/ingress,0,1)

for row in ROWS:
    tic=row['tic']; sid=row['sample_id']; out=B/tic; out.mkdir(exist_ok=True)
    packet=json.loads((ROOT/'source-packets'/tic/'sources.json').read_text(encoding='utf-8'))
    bulk=Path(packet['bulk_result']); assert hashlib.sha256(bulk.read_bytes()).hexdigest()==packet['bulk_result_sha256']
    detector=json.loads(bulk.read_text(encoding='utf-8'))
    files={int(Path(v['path']).stem.split('_s')[-1]):v for v in packet['verified_files']}
    all_events=[]; cover=[]; panels=[]
    for item in detector['files']:
        if item.get('status')!='ok':continue
        sector=int(item['sector']); src=files[sector]; fp=Path(src['path'])
        assert hashlib.sha256(fp.read_bytes()).hexdigest()==src['sha256']
        with fits.open(fp,memmap=False) as h:
            a=h[1].data; t=np.asarray(a['TIME'],float); f=np.asarray(a['SAP_FLUX'],float); qual=np.asarray(a['QUALITY'],int)
        valid=np.isfinite(t)&np.isfinite(f)&(f>0)&(qual==0); t=t[valid]; f=f[valid]
        cadence=float(np.median(np.diff(t))); gaps=np.diff(t); cover.append(dict(sector=sector,start=float(t.min()),end=float(t.max()),quality0_positive=len(t),cadence_days=cadence,gaps_over_0p2_days=[[float(t[i]),float(t[i+1])] for i in np.where(gaps>.2)[0]]))
        windows=[w for w in item['windows'] if w.get('flag') and w.get('kind')=='dip']
        for w in windows:
            pred=float(w['time']); duration=float(w['duration']); radius=max(.65,min(2.5,3*duration)); ix=np.abs(t-pred)<radius
            x=t[ix]-pred;y=f[ix]; initial=np.median(y); y=y/initial
            if len(x)<15:continue
            edge=np.abs(x)>max(.25,1.5*min(duration,.24)); edge=edge if edge.sum()>10 else np.abs(x)>radius*.5
            baseline=np.polyfit(x[edge],y[edge],1); resid=y-np.polyval(baseline,x)
            noise=float(1.4826*np.median(np.abs(resid[edge]-np.median(resid[edge])))); noise=max(noise,1e-6)
            width0=max(.05,min(.5,duration)); center0=float(x[np.argmin(np.convolve(resid,np.ones(min(5,len(resid)))/min(5,len(resid)),mode='same'))])
            p0=[float(baseline[1]),float(baseline[0]),min(.5,max(.002,abs(float(w['depth'])))),np.clip(center0,-.3,.3),width0,max(.015,width0*.15)]
            low=[.7,-.3,0,-.4,.025,.008]; high=[1.3,.3,.8,.4,1.5,.5]
            try:
                fit=least_squares(lambda p:(y-trap(p,x))/noise,p0,bounds=(low,high),max_nfev=2000)
                p=fit.x; singular=np.linalg.cond(fit.jac.T@fit.jac)>1e10
                cov=np.linalg.pinv(fit.jac.T@fit.jac); formal=float(np.sqrt(cov[3,3])) if not singular else None
                event=dict(sector=sector,screen_center_btjd=pred,screen_duration_days=duration,measured_center_btjd=float(pred+p[3]),formal_center_error_days=formal,depth_ppt=float(p[2]*min(1,p[4]/(2*p[5]))*1000),fit_width_days=float(p[4]),fit_ingress_days=float(p[5]),noise_ppt=noise*1000,fit_singular=bool(singular),fit_boundary=bool(any(abs(p[i]-low[i])<1e-4 or abs(p[i]-high[i])<1e-4 for i in range(6))),core_start_btjd=float(pred+p[3]-p[4]/2),core_end_btjd=float(pred+p[3]+p[4]/2),raw_flux_median=float(initial),points=int(len(x)),source_sha256=src['sha256'])
                panels.append((event,x,y,trap(p,x)))
            except Exception as ex:
                import traceback
                event=dict(sector=sector,screen_center_btjd=pred,fit_error=traceback.format_exc())
            all_events.append(event)
    data=dict(sample_id=sid,tic=tic,gaia=packet['target']['gaia'],source_receipts=packet['verified_files'],bulk_result=packet['bulk_result'],bulk_sha256=packet['bulk_result_sha256'],coverage=cover,screen_flagged_dips=all_events,fit_caveat='Local trapezoids are screening measurements; event kinds, alias nulls, and source ownership require separate review.')
    (out/'lead-measurements.json').write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    if panels:
        fig,axs=plt.subplots(len(panels),1,figsize=(9,2.3*len(panels)),squeeze=False)
        for ax,(ev,x,y,fit) in zip(axs[:,0],panels):
            ax.plot(x,y,'.',ms=2);ax.plot(x,fit,'r-',lw=1);ax.axvline(0,color='k',alpha=.2)
            ax.set_title(f"S{ev['sector']} at {ev['measured_center_btjd']:.4f}; depth {ev['depth_ppt']:.1f} ppt",fontsize=9)
            ax.set_ylabel('SAP / local median')
        fig.tight_layout();fig.savefig(out/'lead-event-panels.png',dpi=115);plt.close(fig)
    print(sid,tic,'events',len(all_events),flush=True)
