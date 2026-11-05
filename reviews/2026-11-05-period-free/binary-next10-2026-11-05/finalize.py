"""Verify explicit root acceptance and produce row-derived final summary."""
from pathlib import Path
from collections import Counter
import csv,json,hashlib,subprocess,sys,re
from urllib.parse import unquote
W=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
lock=json.loads((W/'queue-seal.json').read_text(encoding='utf8'))
assert sha(W/'queue.csv')==lock['queue_sha256']
for p,h in lock['source_sha256'].items():assert sha(p)==h,p
v=json.loads(subprocess.check_output([sys.executable,str(W/'validate_batch.py'),'batch01'],text=True))
a=json.loads((W/'batch01/ROOT-ACCEPTANCE.json').read_text(encoding='utf8'))
assert a['accepted'] is True
for k in ['queue_sha256','results_sha256','manifest_sha256']:assert a[k]==v[k],k
assert v['completion']=={'COMPLETE':10}
rows=list(csv.DictReader((W/'batch01/RESULTS.csv').open(encoding='utf8')))
assert len(rows)==len({r['tic'] for r in rows})==10
(W/'accepted-results.csv').write_bytes((W/'batch01/RESULTS.csv').read_bytes())
counts=Counter(r['physical_verdict'] for r in rows);novelty=Counter(r['novelty_status'] for r in rows)
summary={'selected':10,'completed_root_accepted':10,'original_priority_ranks':[101,110],'verdicts':dict(counts),'novelty':dict(novelty),'remaining_parent_leads':2694,'caveat':'Priority-selected descriptive follow-up, not a random sample or calibrated yield estimate. No new-system claim inferred from physical status.'}
(W/'accepted-summary.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf8')
lines=['# Next ten multi-sector dip candidates','', 'All ten original priority ranks 101–110 have completed bounded review and root acceptance. This fixed follow-up contains no substitutions.','',', '.join(f'{n} {k.lower()}' for k,n in counts.items())+'. Catalogue status: '+', '.join(f'{n} {k.lower()}' for k,n in novelty.items())+'.','', '| ID | TIC | Physical result | Catalogue status | Adopted period (d) |','|---|---|---|---|---|']
for r in rows:
 p=Path(r['report']).relative_to(W).as_posix()
 lines.append(f"| [{r['sample_id']}]({p}) | {r['tic']} | {r['physical_verdict']} | {r['novelty_status']} | {r['period_days'] or 'unresolved'} |")
lines+=['','TIC 62374377 (N008) gained a third target-centered eclipse-like occasion in newly checked sector 105. The roughly equal long gaps strengthen recurrence but leave integer-cycle aliases and the Gaia association unresolved. Two other attractive dip trains (N002 and N009) were localized to neighboring-source regions in two sectors each; their refuted status concerns attribution to the queued targets. N003 selected flags were raw-flux steps, drifts and gap-related structures.','', 'N006 is the known TOI-5746 eclipsing binary. Its plausible label here reflects this campaign\'s stricter requirement for photometrically resolved integer cycles from the available sparse events. The older confirmation used a Gaia-supported cycle inference; this review does not refute the published binary identification or rewrite that earlier result.','', 'Selection follows the original unchanged priority order after excluding the completed hundred. These ten come from the multi-sector dip lane. The original ordering was informed by earlier outcomes; this small selected batch cannot establish a population yield or validate the ranking. All remaining leads are retained.','', 'Physical classification and catalogue novelty are separate. Known recoveries do not count as new systems; unknown novelty is not clearance. Reports preserve incomplete checks, aliases and association uncertainties. No shared claim ledger, paper, or public catalogue was changed.','', 'The previous hundred and this ten leave 2,694 of the original 2,804 priority leads without these reviews. Original frozen queues remain unchanged.','', 'Evidence is in the linked reports, shared-catalogues, source-packets, and batch01. Root acceptance binds the batch manifest. Raw FITS remain in local caches, with identities and hashes recorded; the repository is not a self-contained raw-data archive.','']
(W/'REPORT.md').write_text('\n'.join(lines),encoding='utf8')
packets=json.loads((W/'source-packet-index.json').read_text(encoding='utf8'))
assert len(packets['targets'])==10 and packets['verified_fits']==73
for t,r in packets['targets'].items():assert sha(r['packet'])==r['sha256'],t
cm=W/'shared-catalogues/SHA256SUMS.json'
manifest=json.loads(cm.read_text(encoding='utf8'));files=manifest.get('files',manifest)
for name,h in files.items():
 p=Path(name);p=p if p.is_absolute() else cm.parent/p
 assert sha(p)==h,p
for p,h in {W.parent/'binary-extension-2026-11-04/accounting/accepted-proposal-ledger.csv':'ede0e4dbe95779e510efc64f330d325516fc8bdd1d52991429988833aac449e0',W.parent/'binary-exploration-2026-11-04/candidate-backlog.csv':'6d85c06f682002f95189244daee3a6d28f69bb5160d82298dd14b55cc367fb2b'}.items():assert sha(p)==h,p
sys.path.insert(0,'[local-path-redacted]')
from ctlbytes import mojibake
textcount=links=0
for p in W.rglob('*'):
 if p.suffix.lower() not in ['.md','.txt','.json','.csv','.py']:continue
 s=p.read_text(encoding='utf8');assert '\ufffd' not in s and not mojibake(s),p
 textcount+=1
 if p.name=='REPORT.md':
  for href in re.findall(r'\[[^\]]+\]\(([^)]+)\)',s):
   if href.startswith(('http:','https:','#','mailto:')):continue
   assert (p.parent/unquote(href.split('#')[0])).exists(),(p,href)
   links+=1
out={'status':'PASS',**summary,'batch_validation':v,'source_packets_verified':10,'initial_fits_verification_record':73,'catalogue_manifest_sha256':sha(cm),'catalogue_files_verified':len(files),'utf8_text_files_checked':textcount,'report_links_checked':links,'prior_ledger_and_backlog_unchanged':True}
(W/'FINAL-VERIFICATION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps(out,indent=2))
