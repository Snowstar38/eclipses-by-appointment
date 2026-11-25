import numpy as np,json,pathlib
from astropy.io import fits
p=pathlib.Path(__file__).parent;e=json.loads((p/'evidence.json').read_text());
with fits.open(p/'lc.fits') as h:
 d=h[1].data;t=d['TIME'];q=d['QUALITY']; v=(q==0)&np.isfinite(t)
 for name,centers in [('shallow',e['shallow_centers'])]:
  vals={k:[] for k in ['SAP_BKG','MOM_CENTR1','MOM_CENTR2','POS_CORR1','POS_CORR2']}; quality=[]
  for c in centers:
   delta=t-c; inn=v&(abs(delta)<.035); out=v&(((delta>-.15)&(delta<-.09))|((delta>.09)&(delta<.15))); quality.append([int(np.sum((abs(delta)<.035)&(q!=0))),int(np.sum(abs(delta)<.035))])
   for k in vals: vals[k].append(float(np.nanmedian(d[k][inn])-np.nanmedian(d[k][out])))
  print('quality nonzero,total',quality)
  for k,x in vals.items():print(k,'median and range',np.nanmedian(x),np.nanmin(x),np.nanmax(x))
 print('deep background baseline',np.nanmedian(d['SAP_BKG'][v&(((t>2917)&(t<2917.25))|((t>2918.25)&(t<2918.5)))]))
