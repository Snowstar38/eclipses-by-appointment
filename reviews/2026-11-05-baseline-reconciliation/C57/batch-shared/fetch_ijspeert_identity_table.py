"""One compact full-table request to reduce future per-target service load."""
from pathlib import Path
import csv,datetime,hashlib,io,json,requests
O=Path(__file__).resolve().parent/'catalogue-archives'
p=O/'ijspeert-identity-table.tsv';rp=O/'ijspeert-identity-table.receipt.json';assert not rp.exists()
info=dict(endpoint='https://vizier.cfa.harvard.edu/viz-bin/asu-tsv',params={'-source':'J/A+A/691/A242/obaf-eb1','-out':'TIC,GaiaDR3,RAJ2000,DEJ2000','-out.max':'100000'},utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),expected_records_from_primary_metadata=69057)
try:
    r=requests.get(info['endpoint'],params=info['params'],timeout=30);p.write_bytes(r.content)
    info.update(url=r.url,http_status=r.status_code,bytes=len(r.content),sha256=hashlib.sha256(r.content).hexdigest());r.raise_for_status()
    assert len(r.content)<25000000 and 'J/A+A/691/A242/obaf-eb1' in r.text and '<html' not in r.text.lower()
    lines=[s for s in r.text.splitlines() if s and not s.startswith('#')]
    header=[s.strip() for s in lines[0].split('\t')];assert header==['TIC','GaiaDR3','RAJ2000','DEJ2000'],header
    rows=[dict(zip(header,[v.strip() for v in s.split('\t')])) for s in lines[3:]]
    assert len(rows)==69057 and len({x['TIC'] for x in rows})==69057
    assert all(x['TIC'].isdigit() and (not x['GaiaDR3'] or x['GaiaDR3'].isdigit()) for x in rows)
    assert any(x['TIC']=='80452824' for x in rows)
    out=io.StringIO(newline='');w=csv.DictWriter(out,fieldnames=header);w.writeheader();w.writerows(rows)
    (O/'ijspeert-identities.csv').write_text(out.getvalue(),encoding='utf-8',newline='')
    info.update(status='validated_full_identity_table',rows=len(rows),parsed_sha256=hashlib.sha256((O/'ijspeert-identities.csv').read_bytes()).hexdigest())
except Exception as e:info.update(status='unavailable_or_unvalidated',error=repr(e))
rp.write_text(json.dumps(info,indent=2)+'\n',encoding='utf-8');print(json.dumps(info,indent=2))
