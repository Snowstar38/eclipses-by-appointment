import json,hashlib,statistics,math
from pathlib import Path
D=Path(__file__).resolve().parent.parent; R=D.parent
P=json.loads((D/'primary.json').read_text()); S=json.loads((D/'secondary.json').read_text()); M=json.loads((D/'correction-manifest.json').read_text()); V=json.loads((D/'verification.json').read_text())
errs=[]; changes=[]; med=[]
for r in P:
 vals=[]
 for e in r['events']:
  if 'fitted_parameters' not in e: continue
  p=e['fitted_parameters']; d=p[2]*1000*min(1,p[4]/(2*max(p[5],1e-5)))
  if not math.isclose(d,e['corrected_depth_ppt'],rel_tol=1e-13,abs_tol=1e-13):errs.append(('formula',r['tic']))
  if abs(d-e['depth_ppt'])>1e-8: changes.append((r['batch'],r['tic'],e['sector'],e['cycle']))
  if e.get('timing_usable') and (r['tic']!='371665307' or e['cycle']%2==0) and (r['tic']!='314040568' or e['cycle']%2==1):vals.append(d)
 if not math.isclose(statistics.median(vals),r['corrected_depth_ppt'],rel_tol=1e-13,abs_tol=1e-13):errs.append(('median',r['tic']))
 if abs(r['corrected_depth_ppt']-r['old_depth_ppt'])>1e-7:med.append((r['tic'],r['old_depth_ppt'],r['corrected_depth_ppt']))
for r in S:
 for e in r['events']:
  if 'fitted_parameters' in e:
   p=e['fitted_parameters']; d=p[2]*1000*min(1,p[4]/(2*max(p[5],1e-5)))
   if not math.isclose(d,e['corrected_depth_ppt'],rel_tol=1e-13,abs_tol=1e-13):errs.append(('secondary formula',r['tic']))
for m in M:
 for folder,key in [('original','original_sha256'),('corrected','corrected_sha256')]:
  f=D/folder/m['path']; h=hashlib.sha256(f.read_bytes()).hexdigest()
  if h!=m[key]:errs.append(('hash',folder,m['path']))
for v in V:
 for k in ['primary_events_exact','primary_median_exact','sources_exact']:
  if k in v and not v[k]:errs.append(('replay',v['tic'],k))
assert len(P)==70 and len(changes)==11 and len(set((a,b) for a,b,*_ in changes))==8 and len(med)==2
out={'primary_targets':len(P),'changed_events':changes,'changed_medians':med,'secondary_records':len(S),'manifest_entries':len(M),'verification_entries':len(V),'errors':errs}
(D/'terra'/'independent-check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
