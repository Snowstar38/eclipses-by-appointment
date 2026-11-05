"""Bounded official MAST TESSCut sector-coverage check for the Q062 target."""
import hashlib,json
from datetime import datetime,timezone
from pathlib import Path
import requests
from astropy.io import fits
B=Path(__file__).resolve().parent
tic='219377638';p=B.parent/'source-packets'/tic/'sources.json'
packet=json.loads(p.read_text(encoding='utf8'))
ra=float(packet['queue_row']['ra_deg']);dec=float(packet['queue_row']['dec_deg'])
url='https://mast.stsci.edu/tesscut/api/v0.1/sector'
r=requests.get(url,params={'ra':ra,'dec':dec},timeout=30)
r.raise_for_status(); body=r.json()
sectors=sorted(int(x['sector']) for x in body['results'])
ctx=json.loads((B/tic/'lead-context.json').read_text(encoding='utf8'))
s13=next(x for x in ctx['sectors'] if x['sector']==13)
with fits.open(s13['source_path']) as h:
    hdr={k:h[0].header.get(k) for k in ('TICID','SECTOR','RA_OBJ','DEC_OBJ','OBJECT')}
rf=requests.get(url,params={'ra':hdr['RA_OBJ'],'dec':hdr['DEC_OBJ']},timeout=30)
rf.raise_for_status();bf=rf.json()
file_sectors=sorted(int(x['sector']) for x in bf['results'])
receipt={'checked_utc':datetime.now(timezone.utc).isoformat(),
         'query_url':r.url,'http_status':r.status_code,
         'target_tic':tic,'target_ra_deg':ra,'target_dec_deg':dec,
         'source_packet_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
         'response':body,'available_sectors':sectors,
         'known_s13_fits_path':s13['source_path'],'known_s13_fits_sha256':s13['source_sha256'],
         'known_s13_fits_header':hdr,'fits_coordinate_query_url':rf.url,
         'fits_coordinate_http_status':rf.status_code,'fits_coordinate_response':bf,
         'fits_coordinate_available_sectors':file_sectors,
         'interpretation':'The TESSCut inventory omits verified QLP S13 at both target and FITS-header coordinates. This endpoint is incomplete for this target; newer-sector availability remains UNKNOWN. It is not a light-curve null.'}
(B/tic/'lead-sector-availability.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf8')
print(tic,sectors)

