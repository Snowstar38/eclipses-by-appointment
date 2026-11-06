from pathlib import Path
import csv,json,hashlib,collections
B=Path(__file__).resolve().parent; rows=list(csv.DictReader((B/'screening-summary.csv').open(encoding='utf8',newline=''))); sci=sorted([r for r in rows if r['control']=='False'],key=lambda x:int(x['tic'])); controls=[r for r in rows if r['control']=='True']; ordered=sci+controls
codes='''I I I I N D I A
A I I I B B N A
I I R A I I I B
I I N B I I I N
I A I I I I B I
I I I B I I I I
I I I I A I A N
R R I I I A I N
N I I I B I I I
R I I I I I N N
I I I D I R I I
I I A I I I B N
N I I I B I I I
R I N I R N D I
N B I I N R A I
I N D I I B N I
N I I I A I N B
I I R I I S B I
I I R I I I R I
I I I I B B B B
N N N B I I N I
I I I I I I I I
I I I I I I I I
I A I N I A I I
B I I I I I I B
I I N A I I I I
I I I I I B I N
A I I I D B I I
I I R I I B N I
I I I I I B I I
B I I I I I I A
I I I I I I I B
I I I N I I I I
I I N I I S R B
I B B B I I I I
B I R I D N I N
I I B I I I I I
I I D I I I I I
I I D I N I I I
N I I I B I I B
I I I I I I I I
I I B I A I B I
B I I B I I I I
I I I I I I I B
I I N N R I B I
I R I I I I N I
I I I I N I B B
I I D N I I B N
D I I A A I I I
I I I R R'''.splitlines()
assert len(codes)==50
notes={'22559994':'S64/S100/S101 deep discrete dips; different depths need review.', '65684549':'S59/S73/S86 narrow repeated dips; inspect baseline and attribution.', '70554665':'S97/S104 compact similar dips; S104 recovery near edge.', '93330962':'S32/S98 narrow dips; S87 trend is different.', '111230893':'S34/S61/S87 deep narrow matching dips.', '122766753':'S19/S59/S73 compact dips; S19 sparse.', '125139230':'S7/S34/S61 similar deep discrete dips.', '140777703':'S19/S25/S59 compact matching dips; early cadences sparse.', '156747165':'S40/S80 deep matching dips; S53 shallower.', '162437782':'S10/S36/S90 resolved similar deep dips.', '167461087':'S55/S82/S83 narrow repeated dips.', '277772867':'S1/S95 deep discrete dips; S101 deep distorted partial feature.', '333795656':'S9/S90 deep similar dips; S63 differs.', '344853043':'S17/S58 deep flat-bottom dips, S24 shallower.', '436205524':'S14/S41/S55 deep repeat dips.', '440995465':'S64/S65 compact similar dips; S101 broad gap-context trough.', '159860053':'S28 deep compact dip; S68 shallower feature, not established same kind.', '332686088':'S58 compact dip; S85 noisy without clear repeat.', '127365016':'CONTROL: S17/S57/S84 deep matching dips.', '56130043':'CONTROL: S5/S32/S98 deep dips.'}
reason={'I':'Selected windows show gap, step, settling or edge-associated structure; event identity unresolved.', 'B':'Selected windows show broad smooth or complex variability; compact eclipse not established.', 'N':'Selected windows are sparse or noise dominated without clear compact coherent event.', 'A':'Selected windows contain a dip or irregular structure but contacts, recurrence, or baseline are uncertain.', 'D':'No QLP files available for the mapped target.', 'R':'Repeated compact dips in selected windows; recurrence and source attribution require full review.', 'S':'One compact dip in selected windows; repeat not established.'}
cat={'I':'step_gap_or_instrumental','B':'broad_variability','N':'noise','A':'ambiguous','D':'no_data','R':'repeated_discrete','S':'single_discrete'}
for i,r in enumerate(ordered):
 c=codes[i//8].split()[i%8]; assert (c=='D')==(int(r['files'])==0), (i,r['tic'],c,r['files']);r['category']=cat[c];r['visual_reason']=notes.get(r['tic'],reason[c]);r['review_priority']=str(c in ('R','S') and r['control']=='False');r.pop('classification',None)
fields=list(ordered[0]);o=B/'triage';
for path,data in [(o/'visual-triage.csv',ordered),(o/'review-queue.csv',[r for r in ordered if r['review_priority']=='True'])]:
 with path.open('w',encoding='utf8',newline='') as f:w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(data)
download=json.loads((B/'downloads.json').read_text());checks=[]
for d in download:
 if d.get('status')=='success':
  p=Path(d['path']); actual=hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else None
  if actual!=d['sha256']:checks.append({'tic':d['tic'],'sector':d['sector'],'expected':d['sha256'],'actual':actual})
seals=json.loads((B/'screen-seal.json').read_text());popsha=hashlib.sha256((B/'population.json').read_bytes()).hexdigest(); result={'selection_sha256':hashlib.sha256((B/'selection.json').read_bytes()).hexdigest(),'population_sha256':popsha,'sealed_population_sha256':seals['population_sha256'],'downloads_json_sha256':hashlib.sha256((B/'downloads.json').read_bytes()).hexdigest(),'successful_downloads_checked':sum(d.get('status')=='success' for d in download),'mismatches':checks};(o/'hash-verification.json').write_text(json.dumps(result,indent=2),encoding='utf8')
counts=collections.Counter(r['category'] for r in sci);assert len(sci)==395 and len(controls)==2 and len(ordered)==397 and len([r for r in ordered if r['review_priority']=='True'])==18
(o/'SUMMARY.md').write_text('# Visual triage, next 400\n\nAll 50 contact sheets inspected, covering 395 mapped science targets and two separately appended controls (397 displayed rows). The frozen cohort comprises 400 science selections; five unresolved identity outcomes are retained in `../identity-outcomes.json`. Ten mapped science rows have no QLP files, leaving 385 with QLP. Each displayed row is recorded in `visual-triage.csv`; 18 science candidates with repeated or single compact-looking events are in `review-queue.csv`. Controls remain separate.\n\nScience category counts: '+', '.join(f'{k}={v}' for k,v in sorted(counts.items()))+'.\n\nThis is triage of up to three contrast-ranked selected raw SAP windows, quality zero, within a preselected maximum eight sectors; the red boxes are screen windows, not fitted eclipse centers. Labels are visual screen categories, not physical verdicts or population occurrence rates. Gap/step labels record appearance, not proof of an instrumental cause. Ambiguous and other nonqueued rows are preserved for later reconsideration. Rankings and appointment shape flags are not verdicts.\n\n`hash-verification.json` records selection, population and download manifest hashes and per-file checks; compare the sealed population hash there. Full review, catalogue novelty, source attribution, aliases, orbital geometry and current-sector coverage are not performed here.\n',encoding='utf8')
print(json.dumps({'counts':counts,'hash':result,'queue':len([r for r in ordered if r['review_priority']=='True'])},indent=2))
