import json,hashlib,csv
from pathlib import Path
import numpy as np
O=Path(__file__).parent;R=O.parent
P=json.load(open(O/'primary.json'));S=json.load(open(O/'secondary.json'))
def save(n,x):(O/n).write_text(json.dumps(x,indent=2))
checks=[];neighbours=[];affected=[];plots=[]
for r in P:
 b=R/r['batch'];d=b/r['tic'];old=json.load(open(d/'measurements.json'))
 nondepth=lambda e:{k:v for k,v in e.items() if k not in ['corrected_depth_ppt','fitted_parameters']}
 checks.append(dict(batch=r['batch'],tic=r['tic'],primary_events_exact=old['events']==[nondepth(e) for e in r['events']],primary_median_exact=old['depth_ppt']==r['replayed_old_depth_ppt'],sources_exact=all(hashlib.sha256(Path(s['path']).read_bytes()).hexdigest()==s['sha256'] for s in old['sources'])))
 changed=[e for e in r['events'] if 'depth_ppt'in e and abs(e['depth_ppt']-e['corrected_depth_ppt'])>1e-8]
 for e in changed:affected.append(dict(batch=r['batch'],tic=r['tic'],sector=e['sector'],cycle=e['cycle'],old_ppt=e['depth_ppt'],corrected_ppt=e['corrected_depth_ppt'],timing_usable=e['timing_usable']))
 wins=[e for e in r['events'] if 'mid_btjd'in e];picks=np.linspace(0,len(wins)-1,min(len(wins),6)).astype(int)
 plotted=[dict(sector=wins[i]['sector'],cycle=wins[i]['cycle']) for i in picks if wins[i] in changed]
 if changed:plots.append(dict(batch=r['batch'],tic=r['tic'],changed_annotation_events=plotted,raw_event_image_requires_update=bool(plotted),report_requires_event_row_update=True))
 path=d/'fresh-pixels/diff_fresh.json'
 if not path.exists():
  neighbours.append(dict(batch=r['batch'],tic=r['tic'],error='No fresh-pixels/diff_fresh.json'));continue
 z=json.load(open(path));ratio=r['corrected_depth_ppt']/r['old_depth_ppt'];nb=z['neighbours_60'];new=[dict(source_id=n['source_id'],old_depth_needed=n['depth_needed'],corrected_depth_needed=n['depth_needed']*ratio,old_possible=n['possible'],corrected_possible=bool(n['depth_needed']*ratio<=1)) for n in nb]
 dep=r['old_depth_ppt']/1000;dep2=r['corrected_depth_ppt']/1000;G=z['target_G']
 neighbours.append(dict(batch=r['batch'],tic=r['tic'],pixel_source=str(path),old_G_limit=G-2.5*np.log10(dep),corrected_G_limit=G-2.5*np.log10(dep2),exact_pairwise_old_G_limit=G+2.5*np.log10((1-dep)/dep),exact_pairwise_corrected_G_limit=G+2.5*np.log10((1-dep2)/dep2),old_capable=[n['source_id'] for n in new if n['old_possible']],corrected_capable=[n['source_id'] for n in new if n['corrected_possible']],neighbours=new))
for r in S:
 b=R/r['batch'];name={'secondary_timing.py':'secondary-audit.json','secondary_measure.py':'secondary-measurements.json','secondary_check.py':'secondary-phases.json'}[r['script']];old=json.load(open(b/name))[r['tic']];es=old.get('events',[old] if 'depth_ppt'in old else [])
 new=[{k:v for k,v in e.items() if k not in ['corrected_depth_ppt','fitted_parameters']} for e in r['events']]
 checks.append(dict(batch=r['batch'],tic=r['tic'],secondary_script=r['script'],secondary_all_fields_exact=es==new,secondary_depth_corrections=sum(abs(e['depth_ppt']-e['corrected_depth_ppt'])>1e-8 for e in r['events'])))
save('verification.json',checks);save('neighbors.json',neighbours);save('changed-events.json',affected);save('plot-annotations.json',plots)
with open(O/'changed-events.csv','w',newline='')as f:
 w=csv.DictWriter(f,fieldnames=list(affected[0]));w.writeheader();w.writerows(affected)
print('Exact checks:',all(all(v for k,v in c.items() if k.endswith('_exact')) for c in checks))
print('Neighbor set changes:',[(n['tic'],n['old_capable'],n['corrected_capable'])for n in neighbours if 'error'not in n and n['old_capable']!=n['corrected_capable']])
print('Changed plotted events:',[p for p in plots if p['raw_event_image_requires_update']])
print('Secondary events:',sum(len(s['events'])for s in S))
