import json,numpy as np
from astropy.io import fits
from pathlib import Path
root=Path(r'[local-path-redacted]'); out=root/'review412'; p=json.loads((root/'pilot48/pilot.json').read_text())['targets']['412639100']; P=20.574398116911674; t0=1746.9609111833931
rows=[]
for rec in p['file_receipts']:
 with fits.open(rec['path']) as h:
  d=h[1].data; m=np.isfinite(d['TIME'])&np.isfinite(d['SAP_FLUX'])&(d['QUALITY']==0); t=np.array(d['TIME'][m]); f=np.array(d['SAP_FLUX'][m]); f=f/np.median(f)
 for k in range(int((t.min()-t0)/P)-1,int((t.max()-t0)/P)+2):
  tc=t0+k*P; x=t-tc; a=np.abs(x)<.8; inner=np.abs(x)<.1305; outer=(np.abs(x)>.3)&a
  if inner.sum()<3 or outer.sum()<8 or (outer&(x<0)).sum()<4 or (outer&(x>0)).sum()<4:continue
  # linear local baseline fit to out of event, event mean residual; uncertainty via 0.1-d bins, acknowledging correlations
  b=np.polyfit(x[outer],f[outer],1); residual=(f-np.polyval(b,x))*1e6
  bins=np.floor((x[a]+.8)/.1).astype(int); means=np.array([np.mean(residual[a][bins==i]) for i in np.unique(bins)])
  depth=-np.mean(residual[inner]); err=np.std(means,ddof=1)/np.sqrt(max(1,inner.sum()*np.median(np.diff(t))/.1))
  rows.append(dict(sector=rec['sector'],cycle=k,predicted_btjd=tc,n_inner=int(inner.sum()),local_linear_box_depth_ppm=round(depth,1),heuristic_red_noise_error_ppm=round(err,1)))
print(json.dumps(rows,indent=2)); (out/'helper-local-depth.json').write_text(json.dumps(rows,indent=2)+'\n')
