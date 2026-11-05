from pathlib import Path
import csv,json,hashlib,shutil
W=Path(__file__).resolve().parent
P=W.parent/'binary-prioritization-2026-11-05'
OLD=W.parent/'binary-priority100-2026-11-05'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
rows=list(csv.DictReader((P/'ranked-remaining.csv').open(encoding='utf8')))
done=list(csv.DictReader((OLD/'accepted-results.csv').open(encoding='utf8')))
seen={r['tic'] for r in done}
remaining=[r for r in rows if r['tic'] not in seen]
assert len(rows)==2804 and len(seen)==100 and len(remaining)==2704
selected=remaining[:10]
assert [int(r['priority_rank']) for r in selected]==list(range(101,111))
for i,r in enumerate(selected,1):
 r.update(sample_id=f'N{i:03}',sample_stratum=r['priority_group'],batch='batch01')
def write(p,rs):
 with p.open('w',encoding='utf8',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rs[0]));w.writeheader();w.writerows(rs)
(W/'batch01').mkdir(exist_ok=True)
write(W/'queue.csv',selected);write(W/'batch01'/'queue.csv',selected)
lock={'selection':'Next ten in unchanged original priority order after excluding the accepted priority100. Outcome-informed descriptive selection, not random or a validated probability rank. No substitutions.','parent_rows':2804,'previously_accepted':100,'remaining_before':2704,'selected':10,'remaining_after_if_completed':2694,'source_sha256':{str(p):sha(p) for p in [P/'ranked-remaining.csv',OLD/'accepted-results.csv']},'queue_sha256':sha(W/'queue.csv'),'batch_sha256':{'batch01':sha(W/'batch01'/'queue.csv')}}
(W/'queue-seal.json').write_text(json.dumps(lock,indent=2)+'\n',encoding='utf8')
for name in ['prepare_evidence.py','validate_batch.py']:
 shutil.copyfile(OLD/name,W/name)
brief=(OLD/'BRIEF.md').read_text(encoding='utf8')
start=brief.index('Read queue-seal.json');end=brief.index('Physical definitions')
brief=brief[:start]+'Read queue-seal.json and the exact batch queue. This is a new ten-target campaign N001-N010, original ranks101-110, after the accepted top100; all ten are other multi-sector dip leads. Prior campaign is sealed and must remain untouched. No substitutions. No population yield inference or new-system claims. Only root accepts results. Preserve paper and registers.\n\n'+brief[end:]
(W/'BRIEF.md').write_text(brief,encoding='utf8')
lessons=(OLD/'REVIEW-LESSONS.txt').read_text(encoding='utf8')
lessons+='\nFinal priority100 lessons: single opposite-kind events cannot impose half-phase on eccentric systems. ABFG can encode missing explicit inclination/omega; examine source-specific geometry when deciding. Gaussian period accumulation alone is not full conjunction uncertainty. Sparse two-deep-event aliases require bounded neighboring integer-cycle tests; unsupported adopted periods stay blank. Same photons do not create extra observing occasions. Catalogue statuses must be established for this exact queue.\n'
(W/'REVIEW-LESSONS.txt').write_text(lessons,encoding='utf8')
(W/'.gitignore').write_text('__pycache__/\n*.fits\n*.fits.gz\n*.npz\n*.npy\n',encoding='utf8')
print(json.dumps({'targets':[(r['sample_id'],r['tic'],r['priority_rank']) for r in selected],**lock},indent=2))
