import csv,json,hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent; bulk=B.parent.parent/'binary-exploration-2026-11-04'/'bulk-results'; out={}
for row in csv.DictReader((B/'queue.csv').open()):
 tic=row['tic']; src=bulk/(tic+'.json'); d=json.loads(src.read_text()); rec=[]; plots=[]
 for file in d['files']:
  p=Path(file['path']); actual=hashlib.sha256(p.read_bytes()).hexdigest(); rec.append({'path':str(p),'actual_sha256':actual,'expected_sha256':file['sha256'],'match':actual==file['sha256'],'sector':file['sector']})
  with fits.open(p,memmap=False) as hd:
   a=hd[1].data;t=np.asarray(a['TIME'],float);q=np.asarray(a['QUALITY']); f=np.asarray(a['SAP_FLUX'],float)
  ok=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0)
  for w in file['windows']:
   if not w['flag']:continue
   x=t[ok]-w['time']; y=f[ok]; sel=abs(x)<max(3.5*w['duration'],1.5);x=x[sel];y=y[sel]
   if len(y): plots.append((file['sector'],w,x,y/np.median(y)))
 out[tic]={'bulk_receipt':str(src),'bulk_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'files':rec,'flag_count':len(plots)}
 if plots:
  fig,axs=plt.subplots(len(plots),1,figsize=(9,1.6*len(plots)),squeeze=False)
  for ax,(s,w,x,y) in zip(axs[:,0],plots):
   ax.plot(x,y,'.',ms=1.3);ax.axvline(0,color='red',lw=.6);ax.set_title(f"s{s} {w['kind']} screen {w['time']:.3f} dur {w['duration']}",fontsize=8);ax.tick_params(labelsize=6)
  fig.tight_layout();fig.savefig(B/f'helper-{tic}-flags.png',dpi=100);plt.close(fig)
 print(tic,len(plots),all(z['match'] for z in rec),flush=True)
(B/'helper-source-receipts.json').write_text(json.dumps(out,indent=2)+'\n')
