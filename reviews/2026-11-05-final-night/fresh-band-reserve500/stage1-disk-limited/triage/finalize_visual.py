import csv,json,hashlib,collections
from pathlib import Path
p=Path(__file__).resolve().parent.parent
t=p/'triage'
sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
rows=sorted(csv.DictReader(open(p/'screening-summary.csv',newline='')),key=lambda x:(x['control']=='True',int(x['tic'])))
rec=json.load(open(t/'visual-sheet-records.json',encoding='utf-8-sig'))
fullrec={}
for n in range(1,63):
 active=iter([(x['classification'],x['visual_reason']) for x in rec[str(n)] if int(x['files'])] if rec[str(n)] and isinstance(rec[str(n)][0],dict) else rec[str(n)]); sr=[]
 for i,x in enumerate(rows[(n-1)*8:n*8],1):
  cat,reason=next(active) if int(x['files']) else ('no_data','Blank displayed row: no downloaded local product/window available; download_unavailable, not a physical negative.')
  x.update(classification=cat,visual_reason=reason,sheet_row=i,visual_review_status='reviewed' if int(x['files']) else 'download_unavailable',priority={'repeated_discrete':1,'single_discrete':2,'ambiguous':3}.get(cat,''),flag_scope='control_only' if x['control']=='True' else 'science_screen_flag',physical_classification='NOT_ESTABLISHED')
  sr.append(dict(x))
 fullrec[str(n)]=sr
 assert next(active,None) is None
(t/'visual-sheet-records.json').write_text(json.dumps(fullrec,indent=2)+'\n')
fields=list(rows[0])
def write(name,rr):
 with open(t/name,'w',newline='') as f:
  w=csv.DictWriter(f,fields);w.writeheader();w.writerows(rr)
write('visual-triage.csv',rows)
science=[x for x in rows if x['control']!='True']; controls=[x for x in rows if x['control']=='True']
queue=sorted([x for x in science if x['priority']!=''],key=lambda x:(x['priority'],int(x['tic'])))
write('review-queue.csv',queue);write('controls.csv',controls)
seal=json.load(open(p/'screen-seal.json'));pop=json.load(open(p/'population.json'))
assert sha(p/'population.json')==seal['population_sha256']
assert sha(p/'selection.json')==pop['selection_sha256']
assert sha(p/'downloads.json')==pop['downloads_sha256']
downloads=json.load(open(p/'downloads.json'));success=[x for x in downloads if x['status']=='success'];bad=[]
for x in success:
 f=Path(x['path'])
 if not f.exists() or sha(f)!=x['sha256']:bad.append(x['path'])
assert not bad
inputs={f.name:sha(f) for f in [p/'population.json',p/'selection.json',p/'downloads.json',p/'screen-seal.json',p/'screening-summary.csv',p/'identity-outcomes.json',p/'screen-targets.json']}
sheets={f.name:sha(f) for f in sorted(t.glob('sheet-*.png'))}
counts=dict(collections.Counter(x['classification'] for x in science));cc=dict(collections.Counter(x['classification'] for x in controls))
summary=f'''# Reserve 500 visual screening

Visually inspected all 62 sheets and all 495 display-row positions in frozen numeric TIC science order followed by two controls. All available raw-window panels were inspected; blank positions were retained as no_data/download_unavailable. All original screening-summary.csv columns are preserved. The frozen selection has 500 science sources, 493 mapped science rows and 7 identity failures outside the mapped display; 485 mapped science targets have QLP availability. Availability does not imply a successful local download.

Science morphology counts: {counts}. Controls: {cc}. Science review queue contains {sum(x['priority'] in (1,2) for x in science)} strong visual flags at priority 1/2 and {sum(x['priority']==3 for x in science)} ambiguous rows at priority 3. Controls remain separate and are excluded from the science queue.

Disk-floor interruption left 1450 products unavailable; the retained downloads manifest has {len(downloads)} records, {len(success)} successful products across {len(set(x['tic'] for x in success))} TICs. No-data rows are availability failures, never physical negatives. No population member was removed based on its result. All download and population receipts remain intact.

These are morphology screening flags, not physical classifications or full-review passes. Review used rendered quality-zero raw SAP local windows, up to three sectors per target. Repeated discrete shape does not establish phase coherence, source attribution, astrophysical nature, or occurrence rates. Gaps, steps, settling, slopes, positive excursions and sparse sampling are recorded in row reasons. No new download, full physical review, ledger or public edit was performed.

Incremental per-sheet observations were saved during review and expanded to complete row records in visual-sheet-records.json. Every row has a classification and concrete reason. Sheet 62 has seven positions; other sheets have eight. Inspection crops in inspection/ were made solely from existing sheet bytes for legibility; no plots were regenerated from flux or new data.

Integrity: population hash matches screen-seal.json, and selection/downloads manifest hashes match population references. Independently hashed every one of the {len(success)} successful manifest products ({sum(x['bytes'] for x in success)} bytes); zero mismatches. Scope is these successful retained local products, not missing archive products or the full parent catalogue. Input, all 62 original sheet, and output SHA-256 receipts are in coverage-and-hashes.json.
'''
(t/'SUMMARY.md').write_text(summary)
outputs={f.name:sha(f) for f in [t/'visual-triage.csv',t/'review-queue.csv',t/'controls.csv',t/'visual-sheet-records.json',t/'SUMMARY.md',Path(__file__)]}
(t/'coverage-and-hashes.json').write_text(json.dumps(dict(rows=len(rows),science_rows=len(science),control_rows=len(controls),sheets=62,science_counts=counts,control_counts=cc,successful_downloads=len(success),successful_tics=len(set(x['tic'] for x in success)),download_bytes=sum(x['bytes'] for x in success),download_mismatches=bad,population_verified=True,inputs=inputs,sheet_sha256=sheets,outputs=outputs),indent=2)+'\n')
print(summary)
