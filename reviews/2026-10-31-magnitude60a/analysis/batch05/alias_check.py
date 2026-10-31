import json,numpy as np,matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from astropy.io import fits
from pathlib import Path
B=Path(__file__).parent;t='377389892';m=json.load(open(B/t/'measurements.json'));fig,ax=plt.subplots(2,1,figsize=(12,7));points=[]
for p in (B.parent/'shared-qlp').glob(t+'_s*.fits'):
 with fits.open(p) as h:a=h[1].data;tm=np.array(a['TIME']);f=np.array(a['SAP_FLUX']);q=np.array(a['QUALITY'])
 ok=np.isfinite(tm)&np.isfinite(f)&(q==0)&(f>0);tm=tm[ok];f=f[ok]/np.percentile(f[ok],80)
 for a,k in zip(ax,(1,4)):
  phase=((tm-m['primary_epoch_btjd'])/(m['period_days']/k)+.5)%1-.5;a.plot(phase,f,'.',ms=1);a.set_title('P=%.8fd'%(m['period_days']/k));a.set_ylim(.65,1.04)
 points.extend(zip([p.stem]*len(tm),tm,f))
fig.tight_layout();fig.savefig(B/t/'alias-check.png',dpi=150)
import csv
with open(B/t/'alias-points.csv','w',newline='') as fh:
 w=csv.writer(fh);w.writerow(['source','btjd','sap_over_sector80percentile']);w.writerows(points)
