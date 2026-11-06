"""Bounded event-anchored Gaia-period recurrence test; no measured period claimed."""
import json,csv,numpy as np
from pathlib import Path
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent
out={}
for row in csv.DictReader((B/'queue.csv').open()):
 tic=row['tic'];d=json.loads((B/tic/'lead-context.json').read_text());ev=json.loads((B/tic/'lead-timing.json').read_text())[0];t0=ev['center_btjd'];dur=ev['duration_d'];P=float(row['gaia_period']);rows=[];plot=[]
 for src in d['source']:
  with fits.open(src['path']) as f:
   a=f[1].data;t=np.asarray(a['TIME'],float);y=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'])
  ok=np.isfinite(t)&np.isfinite(y)&(y>0)&(q==0);t=t[ok];y=y[ok]
  for n in range(int(np.ceil((t.min()-t0)/P)),int(np.floor((t.max()-t0)/P))+1):
   c=t0+n*P;core=abs(t-c)<dur*.3;left=(t>c-dur*1.8)&(t<c-dur*.7);right=(t>c+dur*.7)&(t<c+dur*1.8);r=dict(sector=src['sector'],cycle=n,predicted_btjd=c,n_core=int(core.sum()),n_left=int(left.sum()),n_right=int(right.sum()),source_sha256=src['sha256'])
   cad=np.median(np.diff(t));r['core_coverage_fraction']=float(core.sum()*cad/(dur*.6));r['covered']=bool(min(core.sum(),left.sum(),right.sum())>=3 and r['core_coverage_fraction']>.75)
   if r['covered']:
    tl=np.median(t[left]);tr=np.median(t[right]);fl=np.median(y[left]);fr=np.median(y[right]);base=fl+(fr-fl)*(t-tl)/(tr-tl);r['depth_ppt']=float((1-np.median((y/base)[core]))*1000)
   sel=abs(t-c)<max(1.,2.5*dur)
   if sel.sum():plot.append((r,t[sel]-c,y[sel]/np.median(y[sel])))
   rows.append(r)
 out[tic]=dict(epoch_btjd=t0,assumed_period_d=P,windows=rows,note='Fixed Gaia period anchored to one observed candidate. Not measured ephemeris; uncertainty drift and arbitrary other periods remain. Gaps and unbracketed windows are not clean nulls.')
 fig,axs=plt.subplots(len(plot),1,figsize=(10,2.2*len(plot)),squeeze=False)
 for ax,(r,x,z) in zip(axs[:,0],plot):
  ax.plot(x,z,'.',ms=1);ax.axvspan(-dur*.3,dur*.3,alpha=.2);ax.set_title(f"S{r['sector']} cycle{r['cycle']} t{r['predicted_btjd']:.3f} covered{r['covered']}");ax.grid(alpha=.2)
 fig.tight_layout();fig.savefig(B/tic/'lead-clockwindows.png',dpi=100);plt.close(fig)
(B/'lead-clockcheck.json').write_text(json.dumps(out,indent=2))
