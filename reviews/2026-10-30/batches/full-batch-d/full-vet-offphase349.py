import json,numpy as np
import fit_batch as f
F=f.ROOT;diag=json.load(open(F/'review-diagnostics.json'));out=[]
for c in diag['349273287']['offphase_deep']:
 tc=c['tc'];T=c['duration'];controls=[]
 for tic in f.targets:
  for s in f.read(tic):
   if s['sec']!=c['sec'] or not min(s['t'])<tc<max(s['t']):continue
   f.P=5.54727;a=f.event(s,tc,T,.35,scan=False)
   a['tic']=tic;controls.append(a)
 out.append(dict(census=c,controls=controls))
 print(tc,[(x['tic'],x.get('depth'),x.get('depth_with_background'),x.get('background_fake_depth'),x.get('flagged_core')) for x in controls])
json.dump(out,open(F/'349273287'/'offphase-controls.json','w'),indent=2)
