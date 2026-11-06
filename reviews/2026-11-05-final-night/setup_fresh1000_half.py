from pathlib import Path
import csv,json,hashlib,shutil,sys
W=Path(__file__).resolve().parent;half=sys.argv[1];D=W/'fresh-band-next1000';O=W/'fresh1000'/half;G=O/'shared-catalogues';G.mkdir(parents=True,exist_ok=True)
def rows(p):return list(csv.DictReader(p.open(encoding='utf-8-sig')))
triage=rows(D/'triage'/half/'visual-triage.csv');assert len(triage)==(496 if half=='first' else 495)
leads=[r for r in triage if r['category'] in ('repeated_discrete','single_discrete') and r['tic'] not in ('127365016','56130043')]
leads.sort(key=lambda r:(r['category']!='repeated_discrete',int(r['tic'])))
pop=json.loads((D/'population.json').read_text())['targets'];known={r['tic'] for r in json.loads((D/'exact-prior-identities.json').read_text())['targets'] if r['prsa'] or r['ijspeert']};q=[];targets=[]
for i,r in enumerate(leads,1):
    t=r['tic'];v=pop[t];label=f'Z{(0 if half=="first" else 100)+i:03d}'
    q.append({'sample_id':label,'tic':t,'gaia_dr3':v['gaia']['source_id'],'gaia_period':v['gaia']['period'],'gaia_G':v['gaia']['phot_g_mean_mag'],'sample_stratum':r['category'],'visual_reason':r.get('reason',r.get('visual_reason','')),'exact_primary_prior':str(t in known)})
    targets.append(dict(tic=t,gaia=v['gaia']['source_id'],label=label,ra=v['ra'],dec=v['dec'],scope='pending'))
def write(p,rr):
    with p.open('w',encoding='utf8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rr[0]));w.writeheader();w.writerows(rr)
write(O/'queue.csv',q);eligible=[r for r in q if r['tic'] not in known]
for start in range(0,len(eligible),8):
    B=O/f'batch{start//8+1:02d}';B.mkdir(exist_ok=True);write(B/'queue.csv',eligible[start:start+8])
(O/'selection.json').write_text(json.dumps({'half':half,'visual_rows':len(triage),'strong_leads':len(q),'prior_known_before_review':[r['tic'] for r in q if r['tic'] in known],'full_review_queue':len(eligible),'rule':'Every repeated-discrete or single-discrete science visual lead; repeated leads ordered first, then TIC. Ambiguous and all other rows retained in complete screening register, not physically classified. Exact primary prior identities excluded before fullreview without replacement.','source_visual_sha256':hashlib.sha256((D/'triage'/half/'visual-triage.csv').read_bytes()).hexdigest(),'queue_sha256':hashlib.sha256((O/'queue.csv').read_bytes()).hexdigest()},indent=2)+'\n')
(G/'targets.json').write_text(json.dumps(targets,indent=2)+'\n');S=W/'fresh18/shared-catalogues'
for name in ('cones.py','pending_gaia.py','parse_results.py','local_tables.py','local_tables_60.py','grep_sources.py','cites.json','table3-bulk.tsv','table4-bulk.tsv','toi.csv','post.py','kebc-all-enabled-campaigns.csv','kebc-receipt.json'):
    shutil.copy2(S/name,G/name)
(G/'claims.json').write_text(json.dumps({'claims':[r['tic'] for r in targets],'gaia':{r['tic']:{'source_id':r['gaia']} for r in targets},'labels':{r['tic']:r['label'] for r in targets}}));(G/'cones').mkdir(exist_ok=True)
print(half,'strong',len(q),'fullreview',len(eligible),'batches',(len(eligible)+7)//8)
