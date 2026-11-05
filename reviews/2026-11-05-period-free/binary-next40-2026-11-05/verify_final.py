from pathlib import Path
import json,csv,hashlib,subprocess,sys,re
from urllib.parse import unquote
W=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
lock=json.loads((W/'queue-seal.json').read_text(encoding='utf8'))
assert sha(W/'queue.csv')==lock['queue_sha256']
for p,h in lock['source_sha256'].items():assert sha(p)==h,p
checks=[]
for batch in lock['batch_sha256']:
 v=json.loads(subprocess.check_output([sys.executable,str(W/'validate_batch.py'),batch],text=True))
 a=json.loads((W/batch/'ROOT-ACCEPTANCE.json').read_text(encoding='utf8'));assert a['accepted'] is True
 for k in ['queue_sha256','results_sha256','manifest_sha256']:assert a[k]==v[k]
 assert v['completion']=={'COMPLETE':10};checks.append(v)
subprocess.run([sys.executable,str(W/'aggregate_accepted.py')],check=True,stdout=subprocess.DEVNULL)
s=json.loads((W/'accepted-summary.json').read_text(encoding='utf8'));assert s['root_accepted_complete']==40
proposal=json.loads((W/'integration/review-integration-proposal.json').read_text(encoding='utf8'))
assert proposal['reviewed_unique_targets']==250 and proposal['claims_added_by_this_proposal']==0
for p,h in proposal['source_sha256'].items():assert sha(p)==h,p
assert sha(W/'integration/review-integration-proposal.csv')==proposal['proposal_sha256']
for row in csv.DictReader((W/'accepted-results.csv').open(encoding='utf8')):
 assert row['novelty_status'] in ['KNOWN','SCOPED_NONMATCH'],row
packets=json.loads((W/'source-packet-index.json').read_text(encoding='utf8'))
assert len(packets['targets'])==40 and packets['verified_fits']==396
for r in packets['targets'].values():assert sha(r['packet'])==r['sha256']
cm=W/'shared-catalogues/SHA256SUMS.json';m=json.loads(cm.read_text(encoding='utf8'));files=m.get('files',m)
for n,h in files.items():
 p=Path(n);p=p if p.is_absolute() else cm.parent/p;assert sha(p)==h,p
for p,h in {W.parent/'binary-extension-2026-11-04/accounting/accepted-proposal-ledger.csv':'ede0e4dbe95779e510efc64f330d325516fc8bdd1d52991429988833aac449e0',W.parent/'binary-exploration-2026-11-04/candidate-backlog.csv':'6d85c06f682002f95189244daee3a6d28f69bb5160d82298dd14b55cc367fb2b'}.items():assert sha(p)==h,p
sys.path.insert(0,'[local-path-redacted]');from ctlbytes import mojibake
texts=links=0
for p in W.rglob('*'):
 if p.suffix.lower() not in ['.md','.txt','.json','.csv','.py']:continue
 t=p.read_text(encoding='utf8');assert '\ufffd' not in t and not mojibake(t),p;texts+=1
 if p.name.lower()=='report.md':
  for href in re.findall(r'\[[^\]]+\]\(([^)]+)\)',t):
   if href.startswith(('http:','https:','#','mailto:')):continue
   assert (p.parent/unquote(href.split('#')[0])).exists(),(p,href);links+=1
out={'status':'PASS',**s,'batches':checks,'source_packets_verified':40,'initial_fits_verification_record':396,'catalogue_files_verified':len(files),'catalogue_manifest_sha256':sha(cm),'utf8_text_files_checked':texts,'report_links_checked':links,'prior_ledger_backlog_unchanged':True}
(W/'FINAL-VERIFICATION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8');print(json.dumps({k:v for k,v in out.items() if k!='batches'},indent=2))
