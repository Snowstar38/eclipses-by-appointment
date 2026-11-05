"""Bounded official MAST TESSCut sector-coverage check for the Q051 target."""
import hashlib,json
from datetime import datetime,timezone
from pathlib import Path
import requests
B=Path(__file__).resolve().parent
tic='373314632';p=B.parent/'source-packets'/tic/'sources.json'
packet=json.loads(p.read_text(encoding='utf8'))
ra=float(packet['queue_row']['ra_deg']);dec=float(packet['queue_row']['dec_deg'])
url='https://mast.stsci.edu/tesscut/api/v0.1/sector'
r=requests.get(url,params={'ra':ra,'dec':dec},timeout=30)
r.raise_for_status(); body=r.json()
sectors=sorted(int(x['sector']) for x in body['results'])
receipt={'checked_utc':datetime.now(timezone.utc).isoformat(),
         'query_url':r.url,'http_status':r.status_code,
         'target_tic':tic,'target_ra_deg':ra,'target_dec_deg':dec,
         'source_packet_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
         'response':body,'available_sectors':sectors,
         'interpretation':'TESSCut coverage availability only; not a search for additional eclipses or a negative detection.'}
(B/tic/'lead-sector-availability.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf8')
print(tic,sectors)
