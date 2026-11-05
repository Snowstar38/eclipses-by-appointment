"""Bind a root-authored batch decision to the final mechanically verified files."""
from pathlib import Path
import sys,subprocess,json,csv
W=Path(__file__).resolve().parent;b=W/sys.argv[1]
decision=json.loads((W/'root-decisions'/f'{b.name}.json').read_text(encoding='utf8'))
assert decision['accepted'] is True and decision['root_review']
v=json.loads(subprocess.check_output([sys.executable,str(W/'validate_batch.py'),b.name],text=True))
assert v['completion']=={'COMPLETE':10} and v['verdicts']==decision['expected_verdicts']
rows=list(csv.DictReader((b/'RESULTS.csv').open(encoding='utf8')))
out={k:v[k] for k in ['batch','queue_sha256','results_sha256','manifest_sha256','rows','manifest_files']}
out.update(decision)
out['decisions']={r['sample_id']:{k:r[k] for k in ['tic','physical_verdict','full_review_completion','novelty_status']} for r in rows}
(b/'ROOT-ACCEPTANCE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in out.items() if k not in ['root_review','decisions']},indent=2))
