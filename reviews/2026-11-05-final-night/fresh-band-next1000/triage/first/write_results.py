from pathlib import Path
import csv,json,hashlib
from collections import Counter
O=Path(__file__).resolve().parent; W=O.parent.parent
a=json.loads((O/'annotations.json').read_text())
src=sorted([r for r in csv.DictReader((W/'screening-summary.csv').open()) if r['control']=='False'],key=lambda r:int(r['tic']))[:496]
assert len(a)==62 and all(len(s)==8 for s in a) and len(src)==496
cats={'I':'step_gap_or_instrumental','R':'repeated_discrete','S':'single_discrete','A':'ambiguous','B':'broad_variability','N':'noise','D':'no_data'}
rows=[]
for i,(r,note) in enumerate(zip(src,sum(a,[]))):
    code,reason=note.split('|',1); sheet=i//8+1
    assert r['sheet']==f'triage/sheet-{sheet:02d}.png'
    rows.append(dict(tic=r['tic'],sheet=sheet,row=i%8+1,category=cats[code],reason=reason,review_priority={'R':1,'S':2,'A':3}.get(code,''),review_status='full_review_lead' if code in 'RS' else ('ambiguity_followup' if code=='A' else 'screened_only'),physical_verdict='NOT_ASSIGNED'))
def write(name,data):
    with (O/name).open('w',encoding='utf8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(data)
write('visual-triage.csv',rows)
queue=sorted([r for r in rows if r['review_priority']!=''],key=lambda r:(r['review_priority'],int(r['tic'])))
write('review-queue.csv',queue)
counts=Counter(r['category'] for r in rows)
hashes={name:hashlib.sha256((W/name).read_bytes()).hexdigest() for name in ['population.json','downloads.json','screen-seal.json','screening-summary.csv','screening-summary.json']}
hashes['../triage_fresh1000.py']=hashlib.sha256((W.parent/'triage_fresh1000.py').read_bytes()).hexdigest()
hashes.update({f'triage/sheet-{s:02d}.png':hashlib.sha256((W/'triage'/f'sheet-{s:02d}.png').read_bytes()).hexdigest() for s in range(1,63)})
(O/'input-hashes.json').write_text(json.dumps(hashes,indent=2)+'\n',encoding='utf8')
lines=['# First-half visual screening','', 'All 62 assigned sheets (01-62), all 496 science rows, visually inspected. Numeric TIC order verified against screening-summary.csv. No controls in this half. No data fetched and no full physical review performed.','', 'Selected raw SAP quality-zero local dip windows only; up to three distinct sectors. Blank rows mean no plotted dip-window data, not a claim that every possible source is absent. Display ranking and scores were not used as automatic verdicts. Gap, settling, flare, background-like offsets, and variable-baseline qualifiers are retained.','', 'Counts: '+json.dumps(dict(sorted(counts.items())))+'.','', 'Queue retains every repeated_discrete and single_discrete lead at priorities 1 and 2, plus all ambiguous rows at priority 3 for completeness. These are screening morphology labels and follow-up priorities, not physical classifications or accepted systems.','']
for cat in cats.values():
    rr=[r for r in rows if r['category']==cat]
    lines += [cat+': '+', '.join('TIC'+r['tic']+' (sheet '+str(r['sheet'])+', row '+str(r['row'])+')' for r in rr),'']
lines += ['Input and all 62 sheet SHA-256 hashes: input-hashes.json. Frozen source program hashes are preserved in screen-seal.json.','', 'Primary source hashes:']+[k+': '+v for k,v in hashes.items() if not k.startswith('triage/')]
(O/'SUMMARY.md').write_text('\n'.join(lines)+'\n',encoding='utf8')
assert len({r['tic'] for r in rows})==496
print(json.dumps({'rows':len(rows),'counts':counts,'queue':len(queue),'strong':[r['tic'] for r in queue if r['review_priority'] in [1,2]]},indent=2))
