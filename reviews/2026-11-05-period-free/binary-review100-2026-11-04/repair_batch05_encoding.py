"""Repair remaining verified double-encoded prose; retain before/after receipts."""
from pathlib import Path
import sys,json,hashlib,subprocess
W=Path(__file__).resolve().parent;B=W/'batch05'
sys.path.insert(0,'[local-path-redacted]')
from ctlbytes import mojibake
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
changes=[]
for p in B.rglob('*'):
 if p.suffix not in ['.md','.py','.csv']:continue
 data=p.read_bytes();s=data.decode('utf8');hits=mojibake(s)
 if not hits:continue
 before=sha(p)
 for i,old,new in reversed(hits):s=s[:i]+new+s[i+len(old):]
 p.write_bytes(s.encode('utf8'))
 changes.append({'path':p.relative_to(B).as_posix(),'before_sha256':before,'after_sha256':sha(p),'replacements':len(hits)})
assert changes
a=json.loads((B/'ROOT-ACCEPTANCE.json').read_text(encoding='utf8'))
receipt={'reason':'Remaining double-encoded en dashes and apostrophe in prose repaired. No numeric measurements, verdicts, sample IDs or completion status changed. Byte-preserved line endings.', 'changes':changes,'previous_results_sha256':a['results_sha256'],'previous_manifest_sha256':a['manifest_sha256']}
(B/'ROOT-ENCODING-CORRECTION.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf8')
subprocess.run([sys.executable,str(B/'freeze_hashes.py')],check=True)
v=json.loads(subprocess.check_output([sys.executable,str(W/'validate_batch.py'),'batch05'],text=True))
a.update(results_sha256=v['results_sha256'],manifest_sha256=v['manifest_sha256'],manifest_files_verified=v['manifest_files'],encoding_correction='ROOT-ENCODING-CORRECTION.json; prose only, no numerical or classification changes')
(B/'ROOT-ACCEPTANCE.json').write_text(json.dumps(a,indent=2)+'\n',encoding='utf8')
print(changes)
