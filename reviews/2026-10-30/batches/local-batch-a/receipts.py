import json,os,csv,pathlib
ids=set(json.load(open('targets-selected.json'))); root=pathlib.Path(r'C:\Home\Fable 5\made\sb1-scale'); out={}
for name in ['search.jsonl','triage.jsonl','triage-chunk1.jsonl','triage-c7.jsonl','triage-c8.jsonl','diffimg/diffrun.jsonl','diffimg/diffrun-c4.jsonl','diffimg/diffrun-c4b.jsonl']:
 p=root/name; matches=[]
 for line in open(p,encoding='utf-8'):
  try:
   r=json.loads(line)
   if str(r.get('tic','')) in ids: matches.append(r)
  except Exception: pass
 out[name]=matches
p=pathlib.Path(r'C:\Home\Fable 5.1\made\paper\tables\batch_candidates.csv')
with p.open(encoding='utf-8-sig',newline='') as f:
 rows=list(csv.DictReader(f)); print('CSV columns',rows[0].keys()); out['batch_candidates.csv']=[r for r in rows if any(str(v) in ids for v in r.values())]
for name in ['c3-vetsum-out.txt','c4-vetsum-out.txt','c4-marg-vetsum-out.txt','c3-sapdepth-out.txt','c4-sapdepth-out.txt','c4b-sapdepth-out.txt']:
 text=(root/name).read_text(encoding='utf-8',errors='replace'); blocks=text.split('=== TIC ')
 if 'sapdepth' in name: out[name]=['=== TIC '+b for b in blocks[1:] if b.split()[0] in ids]
 else: out[name]=[line for line in text.splitlines() if any(k in line for k in ids)]
json.dump(out,open('receipts.json','w'),indent=2)
for k,v in out.items(): print(k,len(v))

