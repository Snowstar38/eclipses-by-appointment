"""Bounded, inspectable raw-SAP review of the fixed batch01 candidate windows."""
import csv, hashlib, json
from pathlib import Path
import numpy as np
from astropy.io import fits
from scipy.optimize import curve_fit
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

B=Path(__file__).resolve().parent
Q=list(csv.DictReader((B/'queue.csv').open(newline='',encoding='utf-8')))
ROOT=B.parent

def shape(x,base,slope,dep,center,width,edge):
    return base+slope*x-dep*np.clip((width/2-np.abs(x-center))/edge,0,1)

for row in Q:
    tic=row['tic']; out=B/tic; out.mkdir(exist_ok=True)
    packet=json.loads((ROOT/'source-packets'/tic/'sources.json').read_text())
    bulk=json.loads(Path(r'[local-path-redacted]',tic+'.json').read_text())
    events=[]; coverage=[]; panels=[]; sources=[]
    for rf in bulk['files']:
        if rf['status']!='ok': continue
        fp=Path(rf['path']); digest=hashlib.sha256(fp.read_bytes()).hexdigest()
        if digest!=rf['sha256']: raise ValueError('hash mismatch '+str(fp))
        with fits.open(fp,memmap=False) as hd:
            h=hd[1].data; t=np.asarray(h['TIME'],float); f=np.asarray(h['SAP_FLUX'],float); q=np.asarray(h['QUALITY'],int)
            alt=np.asarray(h['KSPSAP_FLUX'],float) if 'KSPSAP_FLUX' in h.names else None
        sel=np.isfinite(t)&np.isfinite(f)&(f>0);t=t[sel];f=f[sel];q=q[sel]
        if alt is not None: alt=alt[sel]
        cadence=float(np.median(np.diff(t)))
        coverage.append(dict(sector=rf['sector'],start_btjd=float(t.min()),end_btjd=float(t.max()),n_all=int(len(t)),n_quality0=int(sum(q==0)),cadence_days=cadence,max_internal_gap_days=float(np.max(np.diff(t)))))
        sources.append(dict(path=str(fp),sha256=digest,sector=rf['sector']))
        for w in rf['windows']:
            if not w['flag'] or w['kind']!='dip':continue
            seed=float(w['time']); dur=float(w['duration']); span=max(3*dur,0.7)
            local=(np.abs(t-seed)<span)&(q==0); x=t[local]-seed;y=f[local]
            if len(x)<12:continue
            side=(np.abs(x)>max(dur*.7,.1))&(np.abs(x)<span)
            base=float(np.median(y[side])) if sum(side)>5 else float(np.median(y))
            yn=y/base; scatter=float(1.4826*np.median(np.abs(yn[side]-np.median(yn[side])))) if sum(side)>5 else None
            core=np.abs(x)<dur/2
            coremed=float(np.median(yn[core])) if sum(core) else None
            rec=dict(sector=rf['sector'],screen_btjd=seed,screen_duration_days=dur,screen_depth_ppt=1000*w['depth'],quality0_local_n=int(len(x)),quality0_core_n=int(sum(core)),raw_core_median_deficit_ppt=1000*(1-coremed) if coremed else None,raw_side_scatter_ppt=1000*scatter if scatter else None,first_local_btjd=float(seed+x.min()),last_local_btjd=float(seed+x.max()),local_max_gap_days=float(np.max(np.diff(np.sort(x)))),source_sha256=digest)
            try:
                p,cov=curve_fit(shape,x,yn,p0=[1,0,min(max(w['depth'],.002),.5),0,max(dur,.1),max(dur*.2,.02)],bounds=([.5,-1,0,-max(dur,.5),.03,.005],[1.5,1,.9,max(dur,.5),max(2,4*dur),1]),maxfev=15000)
                err=float(np.sqrt(cov[3,3])) if np.isfinite(cov[3,3]) and cov[3,3]>0 else None
                rec.update(fit_mid_btjd=float(seed+p[3]),fit_mid_formal_error_days=err,fit_depth_ppt=float(1000*p[2]*min(1,p[4]/(2*p[5]))),fit_duration_days=float(p[4]),fit_edge_days=float(p[5]),fit_slope_per_day=float(p[1]))
                line=shape(x,*p)
            except Exception as ex:rec['fit_error']=str(ex);line=None
            events.append(rec);panels.append((rec,x,yn,line))
    (out/'lead-numeric.json').write_text(json.dumps(dict(sample_id=row['sample_id'],tic=tic,gaia_period_days=float(row['gaia_period_days']),sources=sources,coverage=coverage,events=events,method='Local trapezoid fits to quality-zero raw SAP at period-free retained dip flags. Fits are exploratory, never sufficient for an eclipse verdict or cycle alias. Screen windows are not centers.'),indent=2)+'\n')
    # All flags, split into legible pages of up to eight panels.
    for start in range(0,len(panels),8):
        chunk=panels[start:start+8];fig,axs=plt.subplots(len(chunk),1,figsize=(9,2.25*len(chunk)),squeeze=False)
        for ax,(rec,x,y,line) in zip(axs[:,0],chunk):
            ax.plot(x,y,'.',ms=2); 
            if line is not None: ax.plot(x,line,'r-',lw=1)
            ax.axvline(0,color='gray',alpha=.4)
            ax.set_title(f"s{rec['sector']} screen {rec['screen_btjd']:.3f} raw deficit {rec['raw_core_median_deficit_ppt']:.1f} ppt fit {rec.get('fit_mid_btjd',float('nan')):.4f}",fontsize=9)
            ax.set_ylabel('SAP / side');ax.set_xlabel('days from screen')
        fig.tight_layout();fig.savefig(out/f'lead-raw-{start//8+1:02d}.png',dpi=115);plt.close(fig)
    print(row['sample_id'],tic,len(events),[round(e.get('fit_mid_btjd',0),4) for e in events[:8]],flush=True)
