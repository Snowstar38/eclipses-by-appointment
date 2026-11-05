"""Bounded raw-SAP measurements of selected period-free detector windows.

The detector's time is only a seed; fitted centers remain exploratory until
raw morphology, coverage, aliases and source attribution are adjudicated.
"""
import csv, hashlib, json
from pathlib import Path
import numpy as np
from astropy.io import fits
from scipy.optimize import curve_fit
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

B=Path(__file__).resolve().parent
R=B.parent
Q=list(csv.DictReader((B/'queue.csv').open(encoding='utf-8',newline='')))
def trap(x,b,s,d,c,w,k):
    return b+s*x-d*np.clip((w/2-np.abs(x-c))/k,0,1)

for row in Q:
    tic=row['tic']; out=B/tic;out.mkdir(exist_ok=True)
    packet=json.loads((R/'source-packets'/tic/'sources.json').read_text(encoding='utf-8'))
    bulk=json.loads((R.parent/'binary-exploration-2026-11-04'/'bulk-results'/(tic+'.json')).read_text(encoding='utf-8'))
    if packet['queue_row']['sample_id']!=row['sample_id']:raise ValueError('packet identity')
    flagged=[]
    for rf in bulk['files']:
        if rf['status']=='ok':
            for w in rf['windows']:
                if w['flag'] and w['kind']=='dip':flagged.append((rf,w))
    # Strongest seed per sector, then up to twelve representative sectors.
    best={}
    for rf,w in flagged:
        sector=int(rf['sector'])
        if sector not in best or w['contrast']>best[sector][1]['contrast']:best[sector]=(rf,w)
    choices=sorted(best.values(),key=lambda z:z[1]['contrast'],reverse=True)[:12]
    bypath={str(rf['path']):(rf,w) for rf,w in choices}
    coverage=[];sources=[];events=[];panels=[]
    for rf in bulk['files']:
        if rf['status']!='ok':continue
        fp=Path(rf['path']);digest=hashlib.sha256(fp.read_bytes()).hexdigest()
        if digest!=rf['sha256']:raise ValueError('hash mismatch '+str(fp))
        with fits.open(fp,memmap=False) as hd:
            h=hd[1].data;t=np.asarray(h['TIME'],float);f=np.asarray(h['SAP_FLUX'],float);q=np.asarray(h['QUALITY'],int)
            alt=np.asarray(h['KSPSAP_FLUX'],float) if 'KSPSAP_FLUX' in h.names else None
        ok=np.isfinite(t)&np.isfinite(f)&(f>0);t=t[ok];f=f[ok];q=q[ok]
        if alt is not None:alt=alt[ok]
        if not len(t):continue
        good=q==0;tg=t[good];fg=f[good]
        if len(tg)<10:continue
        cadence=float(np.median(np.diff(tg)))
        coverage.append(dict(sector=rf['sector'],start_btjd=float(tg.min()),end_btjd=float(tg.max()),n_all=int(len(t)),n_quality0=int(len(tg)),cadence_days=cadence,max_internal_gap_days=float(max(np.diff(tg)))))
        sources.append(dict(path=str(fp),sha256=digest,sector=rf['sector']))
        if str(fp) not in bypath:continue
        _,w=bypath[str(fp)];seed=float(w['time']);dur=float(w['duration']);span=max(3*dur,0.6)
        local=np.abs(tg-seed)<span;x=tg[local]-seed;y=fg[local]
        if len(x)<10:continue
        side=(np.abs(x)>max(dur*.7,.08))&(np.abs(x)<span)
        if sum(side)<6:continue
        base=float(np.median(y[side]));yn=y/base
        scatter=float(1.4826*np.median(np.abs(yn[side]-np.median(yn[side]))))
        core=np.abs(x)<dur/2
        rec=dict(sector=rf['sector'],seed_btjd=seed,screen_duration_days=dur,screen_contrast=w['contrast'],screen_depth_ppt=1000*w['depth'],core_n=int(sum(core)),side_n=int(sum(side)),core_deficit_ppt=float(1000*(1-np.median(yn[core]))) if sum(core) else None,side_scatter_ppt=1000*scatter,local_max_gap_days=float(max(np.diff(np.sort(x)))),source_sha256=digest)
        line=None
        try:
            p,cov=curve_fit(trap,x,yn,p0=[1,0,min(max(w['depth'],.002),.5),0,max(dur,.1),max(dur*.2,.02)],bounds=([.5,-1,0,-max(dur,.5),.03,.005],[1.5,1,.9,max(dur,.5),max(2,4*dur),1]),maxfev=12000)
            error=float(np.sqrt(cov[3,3])) if np.isfinite(cov[3,3]) and cov[3,3]>0 else None
            rec.update(fit_mid_btjd=float(seed+p[3]),fit_mid_formal_error_days=error,fit_depth_ppt=float(1000*p[2]*min(1,p[4]/(2*p[5]))),fit_duration_days=float(p[4]),fit_slope_per_day=float(p[1]))
            line=trap(x,*p)
        except Exception as ex:rec['fit_error']=str(ex)
        events.append(rec);panels.append((rec,x,yn,line))
    (out/'lead-numeric.json').write_text(json.dumps(dict(sample_id=row['sample_id'],tic=tic,gaia_period_days=float(row['gaia_period_days']),source_packet=str(R/'source-packets'/tic/'sources.json'),sources=sources,coverage=coverage,flag_count=len(flagged),representative_method='Maximum screen contrast per sector, up to twelve sectors; all available FITS checked for hash and endpoints.',events=events),indent=2,allow_nan=False)+'\n',encoding='utf-8')
    for start in range(0,len(panels),6):
        chunk=panels[start:start+6];fig,axs=plt.subplots(len(chunk),1,figsize=(9,2.3*len(chunk)),squeeze=False)
        for ax,(rec,x,y,line) in zip(axs[:,0],chunk):
            ax.plot(x,y,'.',ms=2)
            if line is not None:ax.plot(x,line,'r-',lw=1)
            ax.axvline(0,color='gray',alpha=.5)
            ax.set_title(f"s{rec['sector']} seed {rec['seed_btjd']:.3f} raw core {rec['core_deficit_ppt']:.1f} ppt fit {rec.get('fit_mid_btjd',float('nan')):.4f}",fontsize=9)
            ax.set_ylabel('raw SAP / side');ax.set_xlabel('days from screen')
        fig.tight_layout();fig.savefig(out/f'lead-raw-{start//6+1:02d}.png',dpi=110);plt.close(fig)
    print(row['sample_id'],tic,len(flagged),len(events),flush=True)
