from pathlib import Path
import csv,json,hashlib,shutil
W=Path(__file__).resolve().parent
P=W.parent/'binary-prioritization-2026-11-05'
OLD=W.parent/'binary-next10-2026-11-05'
sources=[P/'ranked-remaining.csv',W.parent/'binary-priority100-2026-11-05/accepted-results.csv',OLD/'accepted-results.csv']
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda p:list(csv.DictReader(p.open(encoding='utf8')))
rows=read(sources[0]);seen={r['tic'] for p in sources[1:] for r in read(p)}
remaining=[r for r in rows if r['tic'] not in seen]
assert len(rows)==2804 and len(seen)==110 and len(remaining)==2694
selected=remaining[:40]
assert [int(r['priority_rank']) for r in selected]==list(range(111,151))
for i,r in enumerate(selected,1):r.update(sample_id=f'F{i:03}',sample_stratum=r['priority_group'],batch=f'batch{(i-1)//10+1:02}')
def write(p,rs):
 with p.open('w',encoding='utf8',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rs[0]));w.writeheader();w.writerows(rs)
write(W/'queue.csv',selected)
batchhash={}
for n in range(1,5):
 b=W/f'batch{n:02}';b.mkdir(exist_ok=True);write(b/'queue.csv',selected[(n-1)*10:n*10]);batchhash[b.name]=sha(b/'queue.csv')
lock={'selection':'Next40 unchanged original priority ranks111-150 excluding accepted110; no substitutions. Outcome-informed descriptive selection, not random or calibrated.','selected':40,'parent_rows':2804,'previously_accepted':110,'remaining_before':2694,'remaining_after_if_completed':2654,'source_sha256':{str(p):sha(p) for p in sources},'queue_sha256':sha(W/'queue.csv'),'batch_sha256':batchhash}
(W/'queue-seal.json').write_text(json.dumps(lock,indent=2)+'\n',encoding='utf8')
for name in ['prepare_evidence.py','validate_batch.py','check_availability.py','seal_final.py','.gitignore']:shutil.copyfile(OLD/name,W/name)
brief=(OLD/'BRIEF.md').read_text(encoding='utf8');start=brief.index('Read queue-seal.json');end=brief.index('Physical definitions')
brief=brief[:start]+'Read queue-seal.json and your exact batch queue. New40 campaign F001-F040, original ranks111-150, after accepted110. Four fresh Sol/Terra pairs, one per ten. No substitutions or edits to sealed previous work. Only root accepts decisions. No population-yield inference or new-system claims. Preserve paper/registers during review; root will prepare integration assessment after all40.\n\n'+brief[end:]
(W/'BRIEF.md').write_text(brief,encoding='utf8')
lessons=(OLD/'REVIEW-LESSONS.txt').read_text(encoding='utf8')+'\nNext10 lessons: actual measured source-specific conjunction timing is required for a geometry claim; agreement with Gaia period or eccentricity alone is insufficient. Two kinds need separate recurrence checks. Three equally spaced long-baseline events can retain integer aliases; distinguish supported photometric recurrence from adopted orbital clock. Multiple clear same-kind occasions can support PROBABLE with unknown orbital period; two sparse ones remain PLAUSIBLE under current campaign convention. This narrower photometric cycle-uniqueness standard need not overturn historical Gaia-supported confirmations. Source ownership cannot rest on blended fractional-pixel depth ratios alone for close capable neighbors. Singular/bound-hitting fits cannot furnish precision errors. Verify actual finite positive target flux and valid sky, not positivefraction alone. Near-zero or detector-edge cutouts do not provide nulls. Check UTF8 generators as well as outputs with tools/ctlbytes.py mojibake. Exclude ROOT-ACCEPTANCE.json from leaf manifests.\n'
(W/'REVIEW-LESSONS.txt').write_text(lessons,encoding='utf8')
print(json.dumps({'selected':len(selected),'targets':[(r['sample_id'],r['tic']) for r in selected]},indent=2))
