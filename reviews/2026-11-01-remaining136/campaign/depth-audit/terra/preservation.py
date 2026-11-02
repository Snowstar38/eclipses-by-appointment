import json,math
from pathlib import Path
D=Path(__file__).resolve().parent.parent; P=json.loads((D/'primary.json').read_text()); V=json.loads((D/'verification.json').read_text()); N=json.loads((D/'neighbors.json').read_text()); M=json.loads((D/'correction-manifest.json').read_text()); errors=[]
for v in V:
 for k,x in v.items():
  if k.endswith('_exact') and not x: errors.append((v['tic'],k))
for n in N:
 if 'error' not in n and n['old_capable']!=n['corrected_capable']:errors.append(('capable',n['tic']))
for r in P:
 rel=Path(r['batch'])/r['tic']/'measurements.json'; a=D/'original'/rel; b=D/'corrected'/rel
 if not a.exists(): continue
 old=json.loads(a.read_text()); new=json.loads(b.read_text()); new.pop('depth_correction_note');new['depth_ppt']=old['depth_ppt']
 for e,f in zip(old['events'],new['events']):
  if 'depth_ppt' in e:
   if f.pop('trapezoid_depth_parameter_ppt')!=e['depth_ppt']:errors.append(('parameter',r['tic']))
   f.pop('fitted_ingress_days');f['depth_ppt']=e['depth_ppt']
 if old!=new:errors.append(('nondepth',r['tic']))
print('errors',errors,'secondary events',sum(len(s['events']) for s in json.loads((D/'secondary.json').read_text())),'capable targets',sum('error' not in n for n in N))
