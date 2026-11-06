from pathlib import Path
import csv,json,shutil
W=Path(__file__).resolve().parent;S=W/'fresh-review/shared-catalogues';O=W/'fresh18/shared-catalogues';O.mkdir(parents=True,exist_ok=True)
q=list(csv.DictReader((W/'fresh-band-next400/triage/review-queue.csv').open(encoding='utf8')));pop=json.loads((W/'fresh-band-next400/population.json').read_text())['targets']
t=[]
for i,r in enumerate(q,1):
    r.update(sample_id=f'Y{i:03d}',sample_stratum=r['category']);v=pop[r['tic']]
    t.append({'tic':r['tic'],'gaia':r['gaia_dr3'],'label':r['sample_id'],'ra':v['ra'],'dec':v['dec'],'scope':'pending'})
with (W/'fresh18/queue.csv').open('w',encoding='utf8',newline='') as f:
    wr=csv.DictWriter(f,fieldnames=list(q[0]));wr.writeheader();wr.writerows(q)
(O/'targets.json').write_text(json.dumps(t,indent=2)+'\n')
for name in ('cones.py','pending_gaia.py','parse_results.py','local_tables.py','local_tables_60.py','grep_sources.py','cites.json','table3-bulk.tsv','table4-bulk.tsv','toi.csv','post.py','kebc-all-enabled-campaigns.csv','kebc-receipt.json'):
    shutil.copy2(S/name,O/name)
(O/'claims.json').write_text(json.dumps({'claims':[r['tic'] for r in t],'gaia':{r['tic']:{'source_id':r['gaia']} for r in t},'labels':{r['tic']:r['label'] for r in t}}))
(O/'cones').mkdir(exist_ok=True)
print('Prepared',len(t))
