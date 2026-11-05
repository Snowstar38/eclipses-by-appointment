"""Batch06 bounded first-pass SAP inspection. Predictions are not fitted events."""
import csv, glob, hashlib, json
from pathlib import Path
import numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

B=Path(__file__).resolve().parent
Q=list(csv.DictReader((B/'queue.csv').open(newline='',encoding='utf-8')))
BASE=Path(r'[local-path-redacted]')
for row in Q:
 tic=row['tic']; o=B/tic; o.mkdir(exist_ok=True)
 source=BASE/f'{tic}.json'; bulk=json.loads(source.read_text())
 receipts=[]; sectors=[]; chunks=[]
 for sf in bulk['files']:
  if sf['status']!='ok':continue
  fp=Path(sf['path']); digest=hashlib.sha256(fp.read_bytes()).hexdigest()
  if digest!=sf['sha256']:raise ValueError(f'hash mismatch: {fp}')
  with fits.open(fp,memmap=False) as h:
   a=h[1].data; t=np.array(a['TIME'],float); f=np.array(a['SAP_FLUX'],float); q=np.array(a['QUALITY'],int)
  valid=np.isfinite(t)&np.isfinite(f)&(f>0); t=t[valid];f=f[valid];q=q[valid]
  if not len(t):continue
  good=q==0; med=np.median(f[good]) if sum(good)>5 else np.median(f)
  ff=f/med
  chunks.append((sf['sector'],t,ff,q));receipts.append({'path':str(fp),'sha256':digest,'sector':sf['sector']})
  sectors.append({'sector':sf['sector'],'first':float(t.min()),'last':float(t.max()),'n':len(t),'n_quality0':int(sum(good)),'median_cadence_days':float(np.median(np.diff(t))),'max_gap_days':float(np.max(np.diff(t)))})
 flags=[]
 for sf in bulk['files']:
  if sf['status']=='ok':
   for w in sf['windows']:
    if w.get('flag'):flags.append({'sector':sf['sector'],'kind':w['kind'],'time':w['time'],'duration':w['duration'],'depth':w['depth'],'contrast':w['contrast']})
 fig,axs=plt.subplots(max(1,len(flags)),2,figsize=(12,2.2*max(1,len(flags))),squeeze=False)
 metrics=[]
 for i,w in enumerate(flags):
  match=[c for c in chunks if c[0]==w['sector']]
  if not match:continue
  sec,t,f,q=match[0]; c=w['time'];dur=w['duration'];x=t-c
  for j,half in enumerate((max(2.5*dur,1),max(6*dur,3))):
   ax=axs[i,j];ix=np.abs(x)<half;ax.plot(x[ix],f[ix],'.',ms=2,label='SAP');ax.plot(x[ix&(q!=0)],f[ix&(q!=0)],'x',ms=4,c='red',label='flagged');ax.axvspan(-dur/2,dur/2,color='orange',alpha=.15);ax.set_xlim(-half,half);ax.set_title(f's{sec} {w["kind"]} {c:.3f}, half={half:.1f}d',fontsize=9)
  core=np.abs(x)<dur/2;side=(np.abs(x)>dur)&(np.abs(x)<max(2*dur,.5)); clean=q==0
  base=np.median(f[side&clean]) if sum(side&clean)>5 else np.nan
  metrics.append({**w,'core_samples':int(sum(core)),'core_quality0':int(sum(core&clean)),'side_quality0':int(sum(side&clean)),'raw_core_median_ppt':float(1000*(1-np.median(f[core&clean])/base)) if sum(core&clean)>2 and np.isfinite(base) else None,'core_first':float(t[core].min()) if sum(core) else None,'core_last':float(t[core].max()) if sum(core) else None})
 fig.tight_layout();fig.savefig(o/'raw-flags.png',dpi=130);plt.close(fig)
 # Overview all sectors and fold. The period is the screening value, not an eclipse measurement.
 P=float(row['gaia_period_days']);t0=float(row['best_window_btjd'])
 fig,axs=plt.subplots(2,1,figsize=(12,7))
 for sec,t,f,q in chunks:
  sel=q==0;axs[0].plot(t[sel],f[sel],'.',ms=.8,label=str(sec));phase=((t[sel]-t0)/P+.5)%1-.5;axs[1].plot(phase,f[sel],'.',ms=.8,label=str(sec))
 axs[0].set_xlabel('BTJD');axs[1].set_xlabel('Gaia-period phase from flagged window');axs[1].set_xlim(-.5,.5)
 for ax in axs:ax.set_ylabel('raw SAP / sector median');ax.legend(ncol=8,fontsize=6)
 fig.tight_layout();fig.savefig(o/'raw-overview.png',dpi=130);plt.close(fig)
 out={'sample_id':row['sample_id'],'tic':tic,'gaia_period_days':P,'source_bulk':str(source),'source_bulk_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'file_receipts':receipts,'coverage':sectors,'retained_flag_windows':metrics,'note':'Retained windows and Gaia folds are predictions/screening only. Numeric core medians are not fitted eclipse depths.'}
 (o/'initial-numerics.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
 print(row['sample_id'],tic,'sectors',len(sectors),'flags',len(metrics),flush=True)
