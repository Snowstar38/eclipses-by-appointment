import json
from pathlib import Path
import numpy as np
from astropy.io import fits
from scipy.ndimage import median_filter
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;D=json.loads((B/'SOURCE-SNAPSHOT.json').read_text());G=json.loads((B/'gaia-geometry.json').read_text());out={}
for tic,src in D.items():
 m=json.loads((B/tic/'measurements.json').read_text());P=m['period_days'];ep=m['reference_epoch_btjd'];xs=[];ys=[];sectors=[]
 for r in src['target']['file_receipts']:
  with fits.open(r['path']) as h:a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'])
  ok=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[ok];f=f[ok];cad=np.median(np.diff(t));base=median_filter(f,size=int(1.5/cad)//2*2+1,mode='nearest');y=f/base;x=((t-ep)/P)%1;xs.extend(x);ys.extend(y)
  sectors.append(dict(sector=r['sector'],quality0_n=len(t),flagged_finite_n=int(np.sum(np.isfinite(a['TIME'])&(a['QUALITY']!=0)))))
 x=np.array(xs);y=np.array(ys);bins=np.linspace(0,1,501);cent=(bins[:-1]+bins[1:])/2;med=np.array([np.median(y[(x>=l)&(x<r)]) if sum((x>=l)&(x<r))>2 else np.nan for l,r in zip(bins[:-1],bins[1:])]);other=[c for c in G[tic]['conjunctions'] if c['kind']!=G[tic]['closest']['kind']][0];phase=((other['gaia_conjunction_btjd']-ep)/P)%1
 fig,axs=plt.subplots(2,1,figsize=(11,7));axs[0].plot(x,y,'.',ms=.5,alpha=.15);axs[0].plot(cent,med,'r.',ms=3);axs[0].set_ylim(.9,1.02);axs[0].axvline(phase,color='g');axs[0].set_title(f'{tic}: raw SAP / 1.5-day running median (diagnostic only), all cached sectors; green Gaia other conjunction')
 axs[1].plot(cent,med,'r.',ms=4);axs[1].set_ylim(.985,1.01);axs[1].axvline(phase,color='g');axs[1].set_xlabel('phase from measured selected-kind epoch');fig.tight_layout();fig.savefig(B/tic/'kind-fold.png',dpi=130);plt.close(fig)
 out[tic]=dict(other_gaia_conjunction_phase=phase,sectors=sectors,diagnostic='Quality0 raw SAP divided by 1.5-day running median for fold visualization only; event timing and depths use local linear baseline and no median filtering.',bins=[dict(phase=float(c),normalized_median=float(y)) for c,y in zip(cent,med) if np.isfinite(y)])
(B/'kind-fold.json').write_text(json.dumps(out,indent=2)+'\n')
