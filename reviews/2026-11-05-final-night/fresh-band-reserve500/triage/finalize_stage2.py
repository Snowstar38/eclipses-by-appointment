import csv,json,hashlib,collections
from pathlib import Path
p=Path(__file__).resolve().parent.parent;t=p/'triage';old=p/'stage1-disk-limited'
sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
m=json.loads((p/'stage2-change-manifest.json').read_text())
assert sha(old/'population.json')==m['stage1_population_sha256']
assert sha(p/'population.json')==m['stage2_population_sha256']
assert sha(old/'triage/visual-triage.csv')==m['stage1_visual_sha256']
pop=json.loads((p/'population.json').read_text());op=json.loads((old/'population.json').read_text())
changed={x['tic'] for x in m['changed']};unchanged={x['tic'] for x in m['unchanged']}
rows=sorted(csv.DictReader(open(p/'screening-summary.csv',newline='')),key=lambda x:(x['control']=='True',int(x['tic'])))
original_fields=list(rows[0]);prior={x['tic']:x for x in csv.DictReader(open(old/'triage/visual-triage.csv',newline=''))}
assert len(rows)==495 and len(changed)==313 and len(unchanged)==182 and not changed&unchanged
assert changed|unchanged=={x['tic'] for x in rows}
verification=[]
for tic in sorted(unchanged,key=int):
 a={(x['sector'],x['sha256']) for x in pop['targets'][tic]['files']};b={(x['sector'],x['sha256']) for x in op['targets'][tic]['files']}
 assert a==b
 result={}
 for folder in ('appointment-results','bulk-results'):
  x=sha(p/folder/(tic+'.json'));y=sha(old/folder/(tic+'.json'));assert x==y;result[folder]=x
 verification.append(dict(tic=tic,source_hash_set=sorted(a),numeric_result_sha256=result))
obs=json.loads((t/'stage2-observations.json').read_text())
cats=dict(r='repeated_discrete',u='single_discrete',a='ambiguous',s='step_gap_or_instrumental',b='broad_variability',n='noise',d='no_data')
reasons={
'r':'Distinct localized troughs recur in separate displayed sector windows, with ingress/egress or recovery and surrounding higher flux; morphology flag only, phase coherence and attribution untested.',
'u':'One displayed sector contains a localized trough with a discernible recovery and higher surrounding flux; other displayed sectors do not establish repetition.',
'a':'A local deficit is visible, but sparse points, gaps, unequal baselines or structured variability prevent a secure discrete-event morphology; retained for review.',
's':'Selected deficit is dominated by a baseline discontinuity, gap boundary, asymmetric settling/recovery or adjacent positive excursion; no clean isolated trough established in these panels.',
'b':'Smooth or cyclic structured changes extend beyond the selected box, with sloping/curved baselines or successive broad minima; discrete isolated-event morphology not established.',
'n':'Scatter and isolated outliers dominate the displayed windows without a convincing resolved localized trough.',
'd':'Blank displayed row: archive/local product unavailable; no_data is an availability outcome, not a physical negative.'}
special={
'15527953':'Rapid successive deep narrow minima recur within S101 and S99; S37 is sparse. Repeated discrete morphology, with short-cycle variability visible; no Gaia phase or source attribution established.',
'15994632':'S75 shows a narrow resolved downward excursion with recovery; S14 is sparse and S82 has broad structured variability. Single-discrete morphology retained.',
'97279198':'S7 and S6 show localized cup-shaped deficits with recovery. S88 has an extreme discontinuity and rising baseline; repeated local morphology retained with instrumental contamination unresolved.',
'257464332':'S94 contains a resolved narrow deep trough near the left edge, away from the selected central box. Other displayed panels show steps; single-event morphology retained without timing attribution.',
'316790264':'S87 and S33 plunge to the lower plotting boundary with abrupt edges and flat bottoms; S98 has an unequal baseline/step. Extreme clipping-like morphology makes physical interpretation uncertain; retained ambiguous.',
'352725084':'S81 shows a localized cup-shaped trough with sharp ingress/egress; S54 and S80 have broad variability and gap/step structure, so repetition is not established.',
'296080348':'S80 shows a narrow multi-point localized trough with recovery; S53 and S26 show broad gap-associated deficits. Single-discrete morphology retained.',
'467460090':'Very deep discrete troughs recur within and across S100, S99 and S90 with intervening higher flux; repeated morphology, with attribution and physical interpretation untested.',
'408996985':'Flat-bottomed localized deficits with abrupt ingress and recovery recur in S59, S86 and S73; surrounding gaps and baseline offsets remain, and no physical attribution is made.'}
records={}
for idx,x in enumerate(rows):
 tic=x['tic'];sheet=idx//8+1;row=idx%8+1
 assert x['sheet']==f'triage/sheet-{sheet:02d}.png'
 codes=obs[str(sheet)].split();assert len(codes)==len(rows[(sheet-1)*8:sheet*8])
 if tic in changed:
  code=codes[row-1];assert (code=='d')==(int(x['files'])==0)
  cat=cats[code];reason=special.get(tic,reasons[code])
  x.update(classification=cat,visual_reason=f'Current sheet {sheet}, row {row}: '+reason,visual_review_status='reviewed_stage2',visual_stage_provenance='stage2_current_visual_inspection',carryforward_verification='')
 else:
  q=prior[tic]
  x.update({k:q[k] for k in ('classification','visual_reason')})
  x.update(visual_review_status='verified_carryforward',visual_stage_provenance='stage1-disk-limited/triage/visual-triage.csv',carryforward_verification='identical sector/source SHA256 set and appointment/bulk result SHA256; stage1 table SHA256 verified')
 x.update(sheet_row=row,priority={'repeated_discrete':1,'single_discrete':2,'ambiguous':3}.get(x['classification'],''),flag_scope='control_only' if x['control']=='True' else 'science_screen_flag',physical_classification='NOT_ESTABLISHED')
 records.setdefault(str(sheet),[]).append(dict(x))
fields=original_fields+[k for k in rows[0] if k not in original_fields]
def write(name,rr):
 with (t/name).open('w',newline='',encoding='utf8') as f:
  w=csv.DictWriter(f,fields);w.writeheader();w.writerows(rr)
science=[x for x in rows if x['control']!='True'];controls=[x for x in rows if x['control']=='True']
queue=sorted([x for x in science if x['priority']!=''],key=lambda x:(x['priority'],int(x['tic'])))
write('visual-triage.csv',rows);write('review-queue.csv',queue);write('controls.csv',controls)
(t/'visual-sheet-records.json').write_text(json.dumps(records,indent=2)+'\n')
(t/'carryforward-verification.json').write_text(json.dumps(verification,indent=2)+'\n')
downloads=json.loads((p/'downloads.json').read_text());success=[x for x in downloads if x['status']=='success'];assert len(success)==2276
bad=[]
for x in success:
 f=Path(x['path'])
 if not f.exists() or sha(f)!=x['sha256']:bad.append(x['path'])
assert not bad
assert sha(p/'selection.json')==pop['selection_sha256'];assert sha(p/'downloads.json')==pop['downloads_sha256']
assert sha(p/'population.json')==json.loads((p/'screen-seal.json').read_text())['population_sha256']
counts=dict(collections.Counter(x['classification'] for x in science));cc=dict(collections.Counter(x['classification'] for x in controls))
assert sum(x['classification']=='no_data' for x in science)==8
summary=f'''# Reserve 500 final visual triage

Completed 495 mapped rows: 493 science plus 2 controls. Exactly 313 changed rows received new current-sheet visual annotations; 182 unchanged rows have verified phase-1 carry-forward annotations, not newly claimed visual reviews. All 62 current sheets were opened to inspect changed rows in their frozen numeric-TIC display positions. Every row is reviewed_stage2 or verified_carryforward. All current screening-summary.csv columns and values are preserved except its placeholder classification, replaced by morphology.

Science morphology counts: {counts}. Controls: {cc}. Science queue: {sum(x['priority'] in (1,2) for x in science)} priority-1/2 strong morphology flags and {sum(x['priority']==3 for x in science)} priority-3 ambiguous rows. Controls are excluded from the science queue and saved separately. Eight archive-no-data science rows remain availability outcomes, never physical negatives. The frozen selection contains 500 science sources: 493 mapped display rows and 7 identity failures outside this table.

All 2276 successful retained FITS products were independently hashed with zero mismatches. Phase-1 population and visual-table SHA256 and current population SHA256 match stage2-change-manifest.json. Each of 182 carry-forwards independently matches its archived sector/source hash set and both appointment/bulk numeric-result hashes. Per-row evidence is in carryforward-verification.json. Selection, download manifest and population seal references also match.

Review scope is morphology in existing quality-zero raw SAP local windows, up to three selected sectors. Source scores, appointment shape passes and sector flags are screening inputs, not physical verdicts. Repeated morphology does not establish phase coherence, astrophysical nature, source attribution, occurrence or completeness. Physical classification remains NOT_ESTABLISHED for every row. No new downloads, full physical reviews, ledger or public edits were performed.

Incremental inspection observations are in stage2-observations.json; complete annotated rows are in visual-sheet-records.json. Stage provenance is explicit per row. coverage-and-hashes.json records input, 62 sheet and output hashes, plus source-product verification. Phase-1 artifacts remain archived in stage1-disk-limited/triage.
'''
(t/'SUMMARY.md').write_text(summary,encoding='utf8')
inputs={str(f.relative_to(p)):sha(f) for f in [p/'population.json',p/'selection.json',p/'downloads.json',p/'screen-seal.json',p/'screening-summary.csv',p/'stage2-change-manifest.json',old/'population.json',old/'triage/visual-triage.csv']}
outputs={f.name:sha(f) for f in [t/'visual-triage.csv',t/'review-queue.csv',t/'controls.csv',t/'visual-sheet-records.json',t/'carryforward-verification.json',t/'stage2-observations.json',t/'SUMMARY.md',Path(__file__)]}
(t/'coverage-and-hashes.json').write_text(json.dumps(dict(rows=495,science_rows=493,control_rows=2,new_visual_rows=313,verified_carryforward_rows=182,science_counts=counts,control_counts=cc,successful_downloads=2276,download_bytes=sum(x['bytes'] for x in success),download_mismatches=bad,inputs=inputs,sheet_sha256={f.name:sha(f) for f in sorted(t.glob('sheet-*.png'))},outputs=outputs),indent=2)+'\n')
print(summary)

h=json.loads((t/'coverage-and-hashes.json').read_text())
h['numeric_result_sha256']={str(f.relative_to(p)):sha(f) for folder in ('appointment-results','bulk-results') for f in sorted((p/folder).glob('*.json'))}
h['source_products_verified']=[dict(path=x['path'],sha256=x['sha256'],bytes=x['bytes']) for x in success]
current={x['tic']:x for x in rows}
for x in csv.DictReader(open(p/'screening-summary.csv',newline='')):
 for k,v in x.items():
  if k!='classification':assert str(current[x['tic']][k])==v
h['current_score_columns_verified']=True
(t/'coverage-and-hashes.json').write_text(json.dumps(h,indent=2)+'\n')
