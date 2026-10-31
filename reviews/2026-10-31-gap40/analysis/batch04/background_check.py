from pathlib import Path
import json,numpy as np,hashlib
from astropy.io import fits
b=Path(__file__).parent;j=json.load(open(b/'77176486/historical/diff_s98.json'));p=Path('[local path omitted]')
with fits.open(p) as h:
 a=h[1].data;t=np.array(a['TIME']);q=np.array(a['QUALITY']);f=np.array(a['FLUX']);bg=np.array(a['FLUX_BKG']);out=[]
 yy,xx=np.indices(f.shape[1:]);outer=(xx-7.523)**2+(yy-7.743)**2>25
 for ev in j['events']:
  dt=abs(t-ev['t']);i=(dt<.261*.3)&(q==0);o=(dt>.261)&(dt<.261*2.5)&(q==0);d=np.nanmedian(f[o],axis=0)-np.nanmedian(f[i],axis=0)
  out.append(dict(cycle=ev['cycle'],n_in=int(i.sum()),n_out=int(o.sum()),flagged_in=int(((dt<.261*.3)&(q!=0)).sum()),target_pixel_deficit=float(d[8,8]),neighbor_pixel_deficits=[dict(source_id=n['source_id'],deficit=float(d[round(n['px'][1]),round(n['px'][0])])) for n in j['neighbours_60'] if n['possible']],outer_pixel_median_deficit=float(np.nanmedian(d[outer])),background_model_median_in=float(np.nanmedian(bg[i])),background_model_median_out=float(np.nanmedian(bg[o]))))
r=dict(tic='77176486',sector=98,input_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),method='Quality-zero per-pixel median out-minus-in. Core +/-0.0783d; baseline0.261-0.6525d from historical predictions. Model background and outer pixels are diagnostic only, not a calibrated artifact test.',events=out)
json.dump(r,open(b/'77176486/background-check.json','w'),indent=2)
