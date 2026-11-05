"""Bounded, reproducible SAP event inspection for the sealed single-object queue."""
import hashlib, json
from pathlib import Path
import numpy as np
from astropy.io import fits
from scipy.optimize import minimize_scalar
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE=Path(__file__).parent
PILOT=HERE.parent/'pilot48'/'pilot.json'
SCREEN=HERE.parent/'pilot48'/'screening.jsonl'
p=json.loads(PILOT.read_text())['targets']['412639100']
s=next(x for x in map(json.loads,SCREEN.read_text().splitlines()) if x['tic']=='412639100')
P=s['P']['P']; T0=s['P']['t0']; width=s['P']['dur']
out=[]; pooled=[]
fig,axs=plt.subplots(4,3,figsize=(14,12),layout='constrained')
for rec in p['file_receipts']:
    path=Path(rec['path']); sha=hashlib.sha256(path.read_bytes()).hexdigest()
    assert sha==rec['sha256']
    with fits.open(path,memmap=False) as h:
        assert int(h[0].header['TICID'])==412639100 and int(h[0].header['SECTOR'])==rec['sector']
        d=h[1].data
        t=np.array(d['TIME'],float);f=np.array(d['SAP_FLUX'],float);q=np.array(d['QUALITY'],int)
    ok=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0)
    t=t[ok]; f=f[ok]
    for k in range(int(np.floor((t.min()-T0)/P))-1,int(np.ceil((t.max()-T0)/P))+2):
        pred=T0+k*P;x=t-pred;win=np.abs(x)<.85
        if win.sum()<25: continue
        x=x[win];y=f[win];base=(np.abs(x)>.35)&(np.abs(x)<.8)
        if base.sum()<12 or min(np.sum(base&(x<0)),np.sum(base&(x>0)))<4:continue
        coeff=np.polyfit(x[base],y[base],1)
        norm=y/np.polyval(coeff,x)
        # fixed center and free-center depth; the latter's center is diagnostic, not a measured timing when weak.
        core=np.abs(x)<width/2
        fixed=1-np.median(norm[core]) if core.sum()>=3 else np.nan
        def obj(c):
            m=np.abs(x-c)<width/2
            return np.median(norm[m]) if m.sum()>=3 else 1
        opt=minimize_scalar(obj,bounds=(-.28,.28),method='bounded',options={'xatol':.002})
        off=np.abs(x)>.3
        noise=1.4826*np.median(abs(norm[off]-np.median(norm[off])))
        entry=dict(sector=rec['sector'],cycle=k,predicted_btjd=pred,n_cadences=int(len(x)),n_core=int(core.sum()),fixed_window_depth_ppm=float(fixed*1e6),free_center_offset_days=float(opt.x),free_center_depth_ppm=float((1-opt.fun)*1e6),off_window_scatter_ppm=float(noise*1e6))
        out.append(entry);pooled.append((x,norm,rec['sector'],k))
for i,(entry,(x,y,sec,k)) in enumerate(zip(out,pooled)):
    ax=axs.flat[i];ax.plot(x*24,(y-1)*1e6,'.',ms=2,alpha=.55);ax.axvspan(-width*12,width*12,color='salmon',alpha=.2)
    ax.axvline(entry['free_center_offset_days']*24,color='purple',lw=.7)
    ax.set_title(f"s{sec} cycle{k} fixed {entry['fixed_window_depth_ppm']:.0f} ppm; free {entry['free_center_depth_ppm']:.0f} ppm",fontsize=9)
    ax.set_xlim(-18,18);ax.set_ylim(-1200,1200)
for ax in axs.flat[len(out):]:ax.axis('off')
fig.supxlabel('hours from screening BLS prediction');fig.supylabel('locally linear-detrended SAP residual (ppm)')
fig.savefig(HERE/'raw-events.png',dpi=150);plt.close(fig)
allx=np.concatenate([r[0] for r in pooled]);ally=np.concatenate([r[1] for r in pooled]);
bins=np.arange(-.81,.811,.04); mids=(bins[1:]+bins[:-1])/2
med=np.array([np.median(ally[(allx>=a)&(allx<b)]) if np.sum((allx>=a)&(allx<b))>0 else np.nan for a,b in zip(bins[:-1],bins[1:])]);
counts=np.array([np.sum((allx>=a)&(allx<b)) for a,b in zip(bins[:-1],bins[1:])])
fig,ax=plt.subplots(figsize=(10,4));ax.plot(allx,(ally-1)*1e6,'.',ms=1,alpha=.1);ax.plot(mids,(med-1)*1e6,'ko-',ms=3)
ax.axvspan(-width/2,width/2,color='salmon',alpha=.2);ax.set(xlim=(-.8,.8),ylim=(-800,800),xlabel='days from BLS prediction',ylabel='locally detrended SAP residual (ppm)')
fig.tight_layout();fig.savefig(HERE/'raw-stacked.png',dpi=170);plt.close(fig)
summary=dict(tic='412639100',gaia_source_id=p['gaia']['source_id'],raw_column='SAP_FLUX',quality_mask='QUALITY==0',baseline='linear fit in local 0.35-0.8 d shoulders on each side of predicted event',screening_period_days=P,screening_epoch_btjd=T0,screening_width_days=width,events=out,stack_bins=[dict(offset_days=float(a),median_residual_ppm=float((b-1)*1e6),n=int(c)) for a,b,c in zip(mids,med,counts)],source_receipts=p['file_receipts'])
(HERE/'sap-measurements.json').write_text(json.dumps(summary,indent=2)+'\n')
print('events',len(out),'fixed depths',[round(r['fixed_window_depth_ppm']) for r in out]);print('free center offsets',[round(r['free_center_offset_days'],3) for r in out]);print('median fixed',np.median([r['fixed_window_depth_ppm'] for r in out]))
