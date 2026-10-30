from pathlib import Path
import csv,json,hashlib,collections
B=Path('[local working path omitted; see provenance receipts]');D=B.parent
rows=list(csv.DictReader((B/'RESULTS.csv').open()));ids=[r['tic'] for r in rows];q=[r['tic'] for r in csv.DictReader((D/'queue.csv').open()) if r['batch']=='3'];assert ids==q and len(ids)==10
assert len(list(B.glob('TIC-*.md')))==10
R=json.loads((B/'raw-evidence/raw-events.json').read_text());I=json.loads((B/'raw-evidence/independent-results.json').read_text());checks=[]
for i in I:
 assert i['measurements'] and all(m['depth']>0 for m in i['measurements'])
 if 'TESScut' not in i['provenance']:assert all(i['identity'][k] for k in ['header_tic_matches','header_sector_matches','uri_contains_padded_tic'])
 assert len([x for x in R[i['tic']]['events'] if 'tc'in x and not x['edge']])>=2
 checks.append(i['tic'])
for p in B.glob('TIC-*.md'):assert '\u00e2\u20ac\u201c' not in p.read_text(encoding='utf-8')
v=dict(queue_positions='21-30',rows=10,reports=10,verdicts=dict(collections.Counter(r['physical_verdict'] for r in rows)),execution_completion='all10complete',independent_archive=9,independent_custom_extraction='431535710',scientific_ambiguity='186100980: flux-capable close neighbour unresolved; Gaia orbit agreement favours target but does not uniquely localize',lead_review='Representative raw event panel; targeted cached difference images143517607,186100980,242199703; all numerical source and geometry receipts',catalogues='central existing seven-scope coverage reused',publication='No publication, source edits or commits')
(B/'validation.json').write_text(json.dumps(v,indent=2))
manifest=[dict(path=str(p.relative_to(B)),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in B.rglob('*') if p.is_file() and p.name!='manifest.json']
(B/'manifest.json').write_text(json.dumps(manifest,indent=2));print(v);print('hashed',len(manifest))
