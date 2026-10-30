import csv,json,os
ids={'295945076','372376841','416525506','451493289','348737250'}
out=r'C:\Home\Astra\made\binary-handoff-2026-10-30\local-batch-b'
with open(r'C:\Home\Fable 5.1\made\paper\tables\batch_candidates.csv',encoding='utf-8-sig',newline='') as f:
 rows=[r for r in csv.DictReader(f) if str(r.get('tic','')) in ids]
print('ROWS',json.dumps(rows))
tmp=os.path.join(os.environ['TEMP'],'hunt-sb1-scale')
with open(os.path.join(tmp,'targets.json'),encoding='utf8') as f: t=json.load(f)
with open(os.path.join(tmp,'search.jsonl'),encoding='utf8') as f: s=[json.loads(x) for x in f if str(json.loads(x).get('tic')) in ids]
json.dump({'rows':rows,'targets':{k:t[k] for k in ids},'search':s},open(os.path.join(out,'selected.json'),'w'),indent=2)
print('SEARCH',json.dumps(s))
print('TARGETS',json.dumps({k:t[k] for k in ids}))
