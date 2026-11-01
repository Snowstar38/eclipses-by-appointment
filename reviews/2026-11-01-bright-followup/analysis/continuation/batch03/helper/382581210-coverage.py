from astropy.io import fits
import numpy as np,csv
from pathlib import Path
B=Path(__file__).parent
p=B.parent.parent/'shared-qlp'/'382581210_s029.fits'
with fits.open(p) as h:
 d=h[1].data;t=np.array(d['TIME']);f=np.array(d['SAP_FLUX']);q=np.array(d['QUALITY'])
 rows=[]
 for label,frac in [('event1',0),('quarter',.25),('third',1/3),('half',.5),('two_thirds',2/3),('three_quarters',.75),('event2',1)]:
  c=2090.5534699185+frac*15.6622731514; z=(abs(t-c)<.10)&np.isfinite(f);good=z&(q==0);base=(abs(t-c)>.2)&(abs(t-c)<.5)&np.isfinite(f)&(q==0)
  v=1000*(1-np.median(f[good])/np.median(f[base])) if good.sum() and base.sum() else None
  rows.append([label,frac,c,int(z.sum()),int(good.sum()),int(base.sum()),v])
with (B/'382581210-coverage.csv').open('w',newline='',encoding='utf-8') as f:
 w=csv.writer(f);w.writerow(['window','fraction','center_btjd','finite_count','quality_zero_count','baseline_count','median_deficit_ppt']);w.writerows(rows)
print(rows)

