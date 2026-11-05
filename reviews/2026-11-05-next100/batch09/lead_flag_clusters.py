import csv,json
from pathlib import Path
B=Path(__file__).resolve().parent;bulk=B.parent.parent/'binary-exploration-2026-11-04'/'bulk-results'
rows=[]
for q in csv.DictReader((B/'queue.csv').open(encoding='utf8',newline='')):
 d=json.loads((bulk/f"{q['tic']}.json").read_text())
 for f in d['files']:
  for w in f['windows']:
   if w.get('flag') and w['kind']=='dip':rows.append(dict(sample_id=q['sample_id'],tic=q['tic'],sector=f['sector'],camera=f['camera'],ccd=f['ccd'],time_btjd=w['time'],duration_days=w['duration'],depth_ppt=1000*w['depth']))
clusters=[]
for x in sorted(rows,key=lambda x:x['time_btjd']):
 matching=[c for c in clusters if c['sector']==x['sector'] and abs(c['center_btjd']-x['time_btjd'])<.6]
 if matching:
  c=matching[-1];c['events'].append(x);c['center_btjd']=sum(z['time_btjd'] for z in c['events'])/len(c['events'])
 else:clusters.append(dict(sector=x['sector'],center_btjd=x['time_btjd'],events=[x]))
out=[c for c in clusters if len(set(z['tic'] for z in c['events']))>1]
(B/'lead-flag-clusters.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
for c in out:print(c['sector'],round(c['center_btjd'],3),[(z['sample_id'],round(z['time_btjd'],3)) for z in c['events']])
