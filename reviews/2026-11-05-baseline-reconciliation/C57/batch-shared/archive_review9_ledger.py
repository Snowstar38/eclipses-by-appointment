"""Preserve review9's selection-time ledger after later R688 acceptance."""
import hashlib,json,subprocess
from pathlib import Path
W=Path(__file__).resolve().parent; R=W/'review9'
seal=json.loads((R/'queue-seal.json').read_text())
key=next(k for k in seal['source_hashes'] if k.endswith('accepted-proposal-ledger.csv'))
p='Astra/made/binary-extension-2026-11-04/accounting/accepted-proposal-ledger.csv'
b=subprocess.check_output(['git','show','ae248529f:'+p],cwd='[local-path-redacted]')
expected=seal['source_hashes'][key]
# Git's text normalization may remove CRLF; reproduce exact selection-time bytes.
if hashlib.sha256(b).hexdigest()!=expected:b=b.replace(b'\r\n',b'\n').replace(b'\n',b'\r\n')
assert hashlib.sha256(b).hexdigest()==expected
(R/'selection-time-ledger.csv').write_bytes(b)
(R/'selection-ledger-provenance.json').write_text(json.dumps({'original_source':key,'sha256':expected,'archived_at':'selection-time-ledger.csv','reason':'Root subsequently accepted excluded plausible R688. Original queue and selection-time counts remain unchanged.','recovered_from_commit':'ae248529f'},indent=2)+'\n',encoding='utf-8')
print('selection ledger archived, matching frozen queue seal')
