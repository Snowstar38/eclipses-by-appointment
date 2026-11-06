from pathlib import Path
import json,numpy as np
from astropy.io import fits
b=Path('[workspace]/Astra/made/final-night-2026-11-05/fresh1000/first/batch04');out={}
for fp in b.glob('*/lead-timing.json'):
 tic=fp.parent.name;ct=json.loads((fp.parent/'lead-context.json').read_text());events=[]
 for e in json.loads(fp.read_text()):
  src=next(s for s in ct['source'] if s['sector']==e['sector']);c=e.get('center_btjd',e['screen_btjd']);dur=e.get('duration_d',.5)
  with fits.open(src['path']) as h:
   a=h[1].data;t=np.array(a['TIME']);q=np.array(a['QUALITY']);z={}
   for col in ['SAP_FLUX','KSPSAP_FLUX']:
    if col not in a.columns.names:continue
    y=np.array(a[col]);ok=(q==0)&np.isfinite(t)&np.isfinite(y)&(y>0);core=ok&(abs(t-c)<dur*.25);side=ok&(abs(t-c)>dur*.75)&(abs(t-c)<dur*1.5)
    z[col]={'ncore':int(core.sum()),'nside':int(side.sum()),'depth_ppt':float((1-np.median(y[core])/np.median(y[side]))*1000) if core.any() and side.any() else None}
  events.append({'sector':e['sector'],'center_btjd':c,'duration_proxy_d':dur,'fit_usable':e.get('fit_usable'), 'reductions':z,'source_sha256':src['sha256']})
 out[tic]=events
(b/'lead-reduction-comparison.json').write_text(json.dumps(out,indent=2));print(json.dumps(out['232631356'],indent=2))
