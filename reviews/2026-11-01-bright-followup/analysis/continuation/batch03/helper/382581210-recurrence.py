from astropy.io import fits
import numpy as np,pathlib,csv
B=pathlib.Path(__file__).parent;p0=2090.5534699185;P=15.6622731514; rows=[]
for f in sorted(B.glob('382581210_s*.fits')):
 with fits.open(f) as h:
  d=h[1].data;t=np.array(d['TIME']);y=np.array(d['SAP_FLUX']);q=np.array(d['QUALITY'])
  for n in range(int((np.nanmin(t)-p0)/P)-1,int((np.nanmax(t)-p0)/P)+2):
   c=p0+n*P
   if not np.nanmin(t)<c<np.nanmax(t):continue
   z=(abs(t-c)<.1)&(q==0)&np.isfinite(y);o=(abs(t-c)>.2)&(abs(t-c)<.5)&(q==0)&np.isfinite(y)
   v=float(1000*(1-np.median(y[z])/np.median(y[o]))) if z.sum()>2 and o.sum()>3 else None
   rows.append([f.name,n,c,int(z.sum()),int(o.sum()),v])
with (B/'382581210-recurrence.csv').open('w',newline='',encoding='utf-8') as f:
 w=csv.writer(f);w.writerow(['file','cycle_relative_to_s29','predicted_center_btjd','quality_zero_window_count','quality_zero_baseline_count','median_deficit_ppt']);w.writerows(rows)
