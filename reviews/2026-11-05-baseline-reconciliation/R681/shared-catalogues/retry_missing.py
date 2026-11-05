"""Bounded mirror retry of unavailable VizieR cones; never overwrites a failure with a nonmatch."""
import concurrent.futures
import json
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import run_catalogues as c

HERE = Path(__file__).resolve().parent
MIRRORS = ('vizier.cds.unistra.fr', 'vizier.cfa.harvard.edu', 'vizier.nao.ac.jp')
queue = json.loads((HERE / 'queue-lock.json').read_text())
c.QUEUE_HASH = queue['sha256']
assert c.sha(Path(queue['queue']).read_bytes()) == queue['sha256']
results = json.loads((HERE / 'catalogue-results.json').read_text())
paths = [HERE / r['receipt'] for r in results if r['status'] == 'unavailable']
paths += [p for p in (HERE / 'receipts').glob('positive-control-*.json') if json.loads(p.read_text())['status'] == 'unavailable']
paths = list(dict.fromkeys(paths))
assert len(paths) == 19, len(paths)
assert (HERE / 'failure-archive' / '2026-11-04-initial').is_dir(), 'archive failures first'


def retry(path):
    old = json.loads(path.read_text())
    assert old['queue_sha256'] == queue['sha256'] and old['status'] == 'unavailable'
    split = urllib.parse.urlsplit(old['url'])
    table = urllib.parse.parse_qs(split.query)['-source'][0]
    attempts = []
    for mirror in MIRRORS:
        url = urllib.parse.urlunsplit((split.scheme, mirror, split.path, split.query, split.fragment))
        try:
            request = urllib.request.Request(url, headers={'User-Agent': 'Astra-EB-catalogue-screen/1.0'})
            with urllib.request.urlopen(request, timeout=8) as response:
                raw = response.read(1000001)
            assert len(raw) <= 1000000
            parsed = c.parse_tsv(raw, table)
            if path.name.startswith('positive-control-'):
                control_name = path.stem.removeprefix('positive-control-')
                control = next(x for x in json.loads((Path('[local-path-redacted]') / 'service-controls.json').read_text()) if next((label for label, t, _ in c.TABLES if t == x['table']), None) == control_name)
                previous = (Path('[local-path-redacted]') / control['file']).read_bytes().decode('latin-1').splitlines()
                header = [x.strip() for x in next(line for line in previous if line and not line.startswith('#')).split('\t')]
                source = dict(zip(header, [x.strip() for x in previous[previous.index(next(line for line in previous if line and not line.startswith('#'))) + 3].split('\t')]))
                key = 'TIC' if 'TIC' in source else 'Name' if 'Name' in source else 'ASASSN-V'
                assert any(x.get(key, '').strip().lstrip('0') == source[key].strip().lstrip('0') for x in parsed), 'expected positive source absent'
            dest = HERE / 'raw' / (old['key'] + '.txt')
            dest.write_bytes(raw)
            new = dict(old, status='success', sha256=c.sha(raw), file=str(dest.relative_to(HERE)), bytes=len(raw),
                       retrieved_url=url, queried_at_utc=datetime.now(timezone.utc).isoformat())
            new.pop('error', None)
            c.write_json(path, new)
            attempts.append({'mirror': mirror, 'status': 'success', 'rows': len(parsed), 'sha256': new['sha256']})
            return {'key': old['key'], 'status': 'success', 'attempts': attempts}
        except Exception as exc:
            attempts.append({'mirror': mirror, 'status': 'unavailable', 'error': repr(exc)})
    return {'key': old['key'], 'status': 'unavailable', 'attempts': attempts}


with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
    outcome = list(pool.map(retry, paths))
c.write_json(HERE / 'retry-attempts.json', {'queue_sha256': queue['sha256'], 'results': outcome})
print(json.dumps({'retried': len(outcome), 'recovered': sum(r['status'] == 'success' for r in outcome),
                  'still_unavailable': [r['key'] for r in outcome if r['status'] != 'success']}))
