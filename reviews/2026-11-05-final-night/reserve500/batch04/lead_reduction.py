import json,numpy as np
from pathlib import Path
from astropy.io import fits
b=Path(__file__).resolve().parent
for dp in b.glob('*/lead-context.json'):
 d=json.loads(dp.read_text());out=[]
 for e in json.loads((dp.parent/'lead-timing.json').read_text()):
  if not e.get('fit_usable'):continue
  c=e['center_btjd'];dur=e['duration_d'];s=next(x for x in d['source'] if x['sector']==e['sector'])
  with fits.open(s['path']) as h:
   a=h[1].data;t=np.asarray(a['TIME'],float);q=np.asarray(a['QUALITY']);values={key:np.asarray(a[key],float) for key in ('SAP_FLUX','KSPSAP_FLUX') if key in a.columns.names}
  o={'sector':e['sector'],'center_btjd':c,'duration_d':dur,'source_sha256':s['sha256'],'kind':e['kind'],'reductions':{}}
  for key,y in values.items():
   good=np.isfinite(t)&np.isfinite(y)&(y>0)&(q==0);core=good&(abs(t-c)<dur*.25);left=good&(t>c-dur*1.5)&(t<c-dur*.7);right=good&(t>c+dur*.7)&(t<c+dur*1.5)
   if min(core.sum(),left.sum(),right.sum())<3:o['reductions'][key]={'status':'insufficient'};continue
   tl=np.median(t[left]);tr=np.median(t[right]);fl=np.median(y[left]);fr=np.median(y[right]);base=fl+(fr-fl)*(t-tl)/(tr-tl);z=y/base
   o['reductions'][key]={'depth_ppt':float((1-np.median(z[core]))*1000),'side_rms_ppt':float(np.std(z[left|right])*1000),'n_core':int(core.sum()),'n_left':int(left.sum()),'n_right':int(right.sum())}
  out.append(o)
 (dp.parent/'lead-reduction.json').write_text(json.dumps({'events':out,'note':'KSPSAP and SAP use same QLP photons; no independent observation or independent aperture asserted. Local linear sideband interpolation.'},indent=2))
 print(d['tic'],[(z['sector'],{k:round(v.get('depth_ppt',0),2) for k,v in z['reductions'].items()}) for z in out])
