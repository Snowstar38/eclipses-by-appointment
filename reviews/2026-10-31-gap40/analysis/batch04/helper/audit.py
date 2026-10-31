import json, numpy as np, pathlib, hashlib
from astropy.io import fits
b=pathlib.Path(r'[local path omitted]'); f=pathlib.Path(r'[local path omitted] 5/made/sb1-scale/diffimg'); o={}
for p in b.glob('*/measurements.json'):
 d=json.loads(p.read_text()); e=[x for x in d['events'] if 'mid_btjd' in x]; z={}
 for parity in (0,1):
  q=[x for x in e if x['cycle']%2==parity]; z[str(parity)]={'n':len(q),'median_depth_ppt':float(np.median([x['depth_ppt'] for x in q])) if q else None,'cycles':[x['cycle'] for x in q]}
 o[d['tic']]={'parity':z,'large_uncertainties':[{'cycle':x['cycle'],'sigma':x['timing_error_days']} for x in e if x['timing_error_days']>1], 'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
for tic in ('37948318','77176486'):
 j=json.loads((f/tic/'diff_s98.json').read_text()); p=pathlib.Path(fr'[local path omitted]')
 with fits.open(p,memmap=True) as h:
  a=h[1].data;t=np.array(a['TIME']);q=np.array(a['QUALITY']);flux=a['FLUX']; ds=[]
  for ev in j['events']:
   dt=abs(t-ev['t']);dur=.12 if tic=='37948318' else .261
   inside=(dt<dur*.3)&(q==0); outside=(dt>dur)&(dt<dur*2.5)&(q==0)
   if inside.sum()<3 or outside.sum()<3:continue
   diff=np.nanmedian(flux[outside],axis=0)-np.nanmedian(flux[inside],axis=0)
   tx,ty=np.rint(j['target_px']).astype(int); x,y=np.indices(diff.shape); mask=(x-ty)**2+(y-tx)**2<=4
   positive=np.nan_to_num(np.maximum(diff,0))*mask; centroid=[float((positive*y).sum()/positive.sum()),float((positive*x).sum()/positive.sum())]
   ds.append({'cycle':ev['cycle'],'n_in':int(inside.sum()),'n_out':int(outside.sum()),'target_pixel_deficit':float(diff[ty,tx]),'target_local_centroid':centroid,'neighbor_pixel_deficit':float(diff[round(j['brightest_neighbour_60']['px'][1]),round(j['brightest_neighbour_60']['px'][0])])})
 o[tic]['independent_cutout']={'cutout_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'historical_json_sha256':hashlib.sha256((f/tic/'diff_s98.json').read_bytes()).hexdigest(),'events':ds}
(b/'helper'/'audit-numbers.json').write_text(json.dumps(o,indent=2))
print(json.dumps(o,indent=2))

