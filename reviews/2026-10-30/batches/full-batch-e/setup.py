from pathlib import Path
import json,csv,os,shutil
D=Path(__file__).parent; B=D.parent; S=B/'shared-full-review'; F=D/'full-vet'
ids='273724854 365181558 370251176 119301005 377656542 194609413 323434013 327209313 330659284 82620363'.split()
targets=json.load(open(S/'targets-selected.json')); targets={x:targets[x] for x in ids}
json.dump(targets,open(D/'targets-selected.json','w'),indent=2)
original=Path('C:/Home/Fable 5/made/sb1-scale'); paper=Path('C:/Home/Fable 5.1/made/paper/tables/batch_candidates.csv')
rows={r['tic']:r for r in csv.DictReader(open(paper))}; audit=[]
for tic in ids:
 r=rows[tic]; existing=(original/'pervet'/('vet'+tic)).exists(); audit.append(dict(tic=tic,status=r['status'],existing_vet=existing,resolved_period=r['period_d']))
 assert r['status']=='candidate' and not existing,(tic,r,existing)
json.dump(audit,open(D/'source-audit.json','w'),indent=2)
search=[]
with open(Path(os.environ['TEMP'])/'hunt-sb1-scale'/'search.jsonl') as h:
 for line in h:
  r=json.loads(line)
  if str(r['tic']) in ids:search.append(r)
assert len(search)==10
json.dump({'search.jsonl':search},open(D/'receipts.json','w'),indent=2)
for name in ['c3-vetsum-out.txt','c4-vetsum-out.txt','c3-sapdepth-out.txt','c4-sapdepth-out.txt']:
 p=original/name
 if p.exists(): (D/name).write_text('\n'.join(l for l in p.read_text(errors='replace').splitlines() if any(t in l for t in ids)))
for name in ['diffrun.jsonl','diffrun-c4.jsonl']:
 p=original/'diffimg'/name
 (D/name).write_text('\n'.join(l for l in p.read_text(errors='replace').splitlines() if any(t in l for t in ids)))
for name in ['fit_batch.py','orbit_gates.py','secondary_fit.py','shape_secondary.py','geometry.py','idia_archives.py','neighbor_ari.py','neighbors_summary.py']:
 s=(B/'local-batch-a'/'full-vet'/name).read_text();s=s.replace("D=pathlib.Path(r'C:\\Home\\Astra\\made\\binary-handoff-2026-10-30\\local-batch-a\\full-vet')","D=pathlib.Path(__file__).parent")
 (F/name).write_text(s)
shutil.copy(B/'full-batch-c'/'full-vet'/'download_qlp.py',F/'download_qlp.py')
(D/'.gitignore').write_text('data/\n*.fits\n__pycache__/\n')
print(audit)
for r in search: print(r['tic'], 'P',r['P'],'P2',r.get('P2'))

