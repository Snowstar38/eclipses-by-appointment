"""One alternate public VizieR mirror with an established IJspeert control."""
from pathlib import Path
import datetime,hashlib,json,requests
O=Path(__file__).resolve().parent/'catalogue-archives'
info=dict(endpoint='https://vizier.idia.ac.za/viz-bin/asu-tsv',params={'-source':'J/A+A/691/A242/obaf-eb1','TIC':'80452824','-out.all':'1','-out.max':'5'},utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
try:
    r=requests.get(info['endpoint'],params=info['params'],timeout=12);(O/'idia-control.tsv').write_bytes(r.content)
    info.update(url=r.url,status_code=r.status_code,bytes=len(r.content),sha256=hashlib.sha256(r.content).hexdigest());r.raise_for_status()
    assert '80452824' in r.text and 'GaiaDR3' in r.text and '<html' not in r.text.lower()
    info['status']='control_returned_requires_parser_audit'
except Exception as e:info.update(status='unavailable',error=repr(e))
(O/'idia-control-receipt.json').write_text(json.dumps(info,indent=2)+'\n',encoding='utf-8');print(json.dumps(info,indent=2))
