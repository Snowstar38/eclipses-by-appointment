import hashlib
import json
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

p = Path(__file__).parent
query = "SELECT a.id FROM ident AS a JOIN ident AS b ON a.oidref=b.oidref WHERE b.id='Gaia DR3 1989520523290696832'"
url = 'http[local path omitted]'
receipt = {'url': url, 'query': query, 'queried_at_utc': datetime.now(timezone.utc).isoformat()}
try:
    data = urllib.parse.urlencode({'REQUEST': 'doQuery', 'LANG': 'ADQL', 'FORMAT': 'csv', 'QUERY': query}).encode()
    raw = urllib.request.urlopen(url, data, timeout=25).read()
    assert raw.startswith(b'id\n') or raw.startswith(b'ID\n')
    (p / 'vsx-alias-simbad-identifiers.csv').write_bytes(raw)
    receipt.update(status='success', sha256=hashlib.sha256(raw).hexdigest(), aliases=raw.decode().splitlines()[1:])
except Exception as exc:
    receipt.update(status='unavailable', error=repr(exc))
(p / 'vsx-alias-receipt.json').write_text(json.dumps(receipt, indent=2))
print(json.dumps(receipt, indent=2))
