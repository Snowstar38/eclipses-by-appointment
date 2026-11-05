"""Final integrity verification; no scientific acceptance is inferred here."""
from pathlib import Path
from collections import Counter
import csv,json,hashlib,subprocess,sys
W=Path(__file__).resolve().parent
sys.path.insert(0,'[local-path-redacted]')
from ctlbytes import mojibake
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
seal=json.loads((W/'queue-seal.json').read_text(encoding='utf8'))
assert sha(W/'queue.csv')==seal['queue_sha256']
assert sha(seal['source'])==seal['source_sha256']
checks=[]
for batch in seal['batch_sha256']:
 v=json.loads(subprocess.check_output([sys.executable,str(W/'validate_batch.py'),batch],text=True))
 a=json.loads((W/batch/'ROOT-ACCEPTANCE.json').read_text(encoding='utf8'))
 assert a['accepted'] is True
 for key in ['queue_sha256','results_sha256','manifest_sha256']:assert a[key]==v[key],(batch,key)
 assert v['completion']=={'COMPLETE':10}
 checks.append(v)
subprocess.run([sys.executable,str(W/'aggregate_accepted.py')],check=True,stdout=subprocess.DEVNULL)
rows=list(csv.DictReader((W/'accepted-results.csv').open(encoding='utf8')))
assert len(rows)==len({r['tic'] for r in rows})==100
assert Counter(r['novelty_status'] for r in rows)=={'UNKNOWN':100}
packets=json.loads((W/'source-packet-index.json').read_text(encoding='utf8'))
assert len(packets['targets'])==100 and packets['verified_fits']==705
for tic,r in packets['targets'].items():assert sha(r['packet'])==r['sha256'],tic
cm=W/'shared-catalogues/SHA256SUMS.json'
ca=json.loads((W/'catalogue-root-verification.json').read_text(encoding='utf8'))
assert sha(cm)==ca['manifest_sha256']
files=json.loads(cm.read_text(encoding='utf8'));files=files.get('files',files)
for path,h in files.items():
 p=Path(path)
 if not p.is_absolute():p=cm.parent/p
 assert sha(p)==h,p
ledger=W.parent/'binary-extension-2026-11-04/accounting/accepted-proposal-ledger.csv'
assert sha(ledger)=='ede0e4dbe95779e510efc64f330d325516fc8bdd1d52991429988833aac449e0'
text_count=0
for p in W.rglob('*'):
 if p.suffix.lower() not in ['.md','.txt','.py','.csv','.json']:continue
 s=p.read_text(encoding='utf8');assert '\ufffd' not in s,p
 assert not mojibake(s),('double-encoded prose',str(p))
 text_count+=1
out={'status':'PASS','selected':100,'root_accepted_complete':100,'verdicts':dict(Counter(r['physical_verdict'] for r in rows)),
 'queue_sha256':seal['queue_sha256'],'parent_backlog_unchanged':True,'prior_accepted_ledger_unchanged':True,
 'source_packets_verified':100,'initial_fits_verification_record':705,'catalogue_files_verified':len(files),
 'utf8_text_files_checked':text_count,'batches':checks,
 'limits':'Integrity checks verify preserved evidence and explicit acceptance, not catalogue novelty or scientific truth independently.'}
(W/'FINAL-VERIFICATION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in out.items() if k!='batches'},indent=2))
