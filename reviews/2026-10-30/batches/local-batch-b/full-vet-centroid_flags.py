import json,pathlib,numpy as np,csv
from astropy.io import fits
r=pathlib.Path(__file__).parent
for p in r.glob('*_measurements.json'):
 d=json.loads(p.read_text());rows=[]
 for e in d['events']:
  fn=r.parent/'data'/f"{d['tic']}_s{e['sector']:03}.fits";a=fits.getdata(fn,1);t=np.array(a['TIME'],float);q=np.array(a['QUALITY']);inn=(abs(t-e['tc'])<e['T14_d']/2)&(q==0);out=(abs(t-e['tc'])>e['T14_d']*.7)&(abs(t-e['tc'])<.6)&(q==0);row={'sector':e['sector'],'cycle':e['cycle'],'quality_flagged_within_0p3d':e['flagged_in_0p3d']}
  for col in ['SAP_X','SAP_Y']:
   if col in a.names:
    v=np.array(a[col],float);row[col+'_in_minus_out_px']=float(np.nanmedian(v[inn])-np.nanmedian(v[out])) if inn.sum() and out.sum() else None
  rows.append(row)
 (r/f"{d['tic']}_centroid_flags.json").write_text(json.dumps(rows,indent=2))
