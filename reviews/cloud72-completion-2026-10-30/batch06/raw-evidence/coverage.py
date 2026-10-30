from pathlib import Path
import json,numpy as np
from astropy.io import fits
R=Path(__file__).parent;recs=json.load(open(R/'search-receipts.json'));out={}
for rec in recs:
 tic=rec['tic'];s=rec['P'];rows=[]
 for p in sorted((R/tic).glob('qlp*.fits')):
  with fits.open(p) as h:
   a=h[1].data;t=np.array(a['TIME']);y=np.array(a['SAP_FLUX']);q=np.array(a['QUALITY']);m=np.isfinite(t)&np.isfinite(y)&(y>0)&(q==0);t=t[m];y=y[m]/np.median(y[m])
  for n in np.arange(np.ceil((t.min()-s['t0'])/s['P']),np.floor((t.max()-s['t0'])/s['P'])+1):
   tc=s['t0']+n*s['P'];d=s['dur'];x=t-tc;i=abs(x)<.3*d;pre=(x<-.75*d)&(x> -1.75*d);post=(x>.75*d)&(x<1.75*d);r={'sector':int(p.stem[-3:]),'cycle':int(n),'nominal_tc':tc,'n_in':int(i.sum()),'n_pre':int(pre.sum()),'n_post':int(post.sum())};r['covered']=bool(min(i.sum(),pre.sum(),post.sum())>=3)
   if r['covered']:r['signed_depth'] = float((np.median(y[pre])+np.median(y[post]))/2-np.median(y[i]));r['local_rms']=float(np.std(y[pre|post]))
   rows.append(r)
 out[tic]={'conditional_search_period_d':s['P'],'search_depth_fraction':s['depth']*1e-6,'eclipse_period_established':False,'nominal_tests':rows,'warning':'Conditional search phases, not measured eclipses or a derived period. Coverage tests characterize failure to recover candidate; morphology governs verdict.'}
json.dump(out,open(R/'predicted-coverage.json','w'),indent=2)
print([(k,[(x['sector'],round(x.get('signed_depth',float('nan')),5)) for x in v['nominal_tests'] if x['covered']]) for k,v in out.items()])
