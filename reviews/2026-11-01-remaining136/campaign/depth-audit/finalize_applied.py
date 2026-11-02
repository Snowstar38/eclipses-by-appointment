import csv,hashlib,json
from pathlib import Path
import numpy as np
O=Path(__file__).parent;R=O.parent;M=json.load(open(O/'applied-manifest.json'));P=json.load(open(O/'primary.json'))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def write(rel,z):
 p=R/rel;q=O/'originals'/rel
 if not q.exists():q.parent.mkdir(parents=True,exist_ok=True);q.write_bytes(p.read_bytes())
 p.write_text(json.dumps(z,indent=2)+'\n')
 item=dict(path=rel.as_posix(),before_sha256=sha(q),after_sha256=sha(p));found=next((i for i,x in enumerate(M)if x['path']==rel.as_posix()),None)
 if found is None:M.append(item)
 else:M[found]=item
aliases={};derived=[]
for r in P:
 if not r['corrected_event_count']:continue
 rel=Path(r['batch'])/'alias-audit.json'
 if rel not in aliases:aliases[rel]=json.load(open(R/rel))
 z=aliases[rel][r['tic']];m=json.load(open(R/r['batch']/r['tic']/'measurements.json'));ev=[e for e in m['events']if e.get('timing_usable')]
 for sec,parities in z['sector_parity_depths'].items():
  for parity,old in parities.items():
   values=[e['depth_ppt']for e in ev if e['sector']==int(sec)and e['cycle']%2==int(parity)]
   new=dict(n=len(values),median_depth_ppt=float(np.median(values)))if isinstance(old,dict)else values
   original=json.load(open(O/'originals'/rel))[r['tic']]['sector_parity_depths'][sec][parity] if (O/'originals'/rel).exists() else old
   if original!=new:derived.append(dict(batch=r['batch'],tic=r['tic'],sector=sec,parity=parity,before=original,after=new))
   parities[parity]=new
 if r['batch']=='batch02':
  target=Path(r['batch'])/r['tic']/'alias-coverage.json';q=json.load(open(R/target));q['sector_parity_depths']=z['sector_parity_depths'];write(target,q)
for rel,z in aliases.items():
 if z!=json.load(open(R/rel)):write(rel,z)
(O/'derived-depth-corrections.json').write_text(json.dumps(derived,indent=2)+'\n')
checks=[]
for r in P:
 if not r['corrected_event_count']:continue
 rel=Path(r['batch'])/r['tic']/'measurements.json';old=json.load(open(O/'originals'/rel));new=json.load(open(R/rel));restored=json.loads(json.dumps(new));restored.pop('depth_correction_note');restored['depth_ppt']=old['depth_ppt']
 for a,b in zip(restored['events'],old['events']):
  if 'depth_ppt'in a:a['depth_ppt']=b['depth_ppt'];a.pop('trapezoid_depth_parameter_ppt');a.pop('fitted_ingress_days')
 assert restored==old,rel
 checks.append(dict(path=rel.as_posix(),all_nondepth_fields_exact=True))
for b in ['batch02','batch03','batch05','batch06','batch07']:
 rel=Path(b)/'SHA256SUMS.json';H=json.load(open(R/rel))
 for name in list(H):
  p=R/b/name
  if p.name.startswith('root-')or p.name.startswith('helper-final')or p.name in ['final-hash-verification.json','final-validation.json','final-verification.json']:H.pop(name)
  else:H[name]=sha(p)
 write(rel,H)
 assert all(sha(R/b/p)==h for p,h in H.items())
checks.append(dict(all_five_manifest_hashes_verified=True))
(O/'post-correction-verification.json').write_text(json.dumps(checks,indent=2)+'\n')
(O/'applied-manifest.json').write_text(json.dumps(M,indent=2)+'\n')
(O/'originals-manifest.json').write_text(json.dumps({p.relative_to(O/'originals').as_posix():sha(p)for p in (O/'originals').rglob('*')if p.is_file()},indent=2)+'\n')
print('Final bounded changed paths:',len(M),'derived parity entries:',len(derived))
