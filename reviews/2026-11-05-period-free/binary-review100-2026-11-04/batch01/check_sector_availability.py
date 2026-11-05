"""Bounded current TESScut sector-inventory check; no light-curve downloads."""
import hashlib,json
from pathlib import Path
import requests
B=Path(__file__).resolve().parent
out={}
for tic in ['277891015','268385893','322217134']:
    p=json.loads((B.parent/'source-packets'/tic/'sources.json').read_text())
    g=p['target']['gaia']
    params={'ra':g['ra'],'dec':g['dec']}
    try:
        r=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/sector',params=params,timeout=25)
        raw=r.content
        (B/tic/'sector-availability.raw').write_bytes(raw)
        entry={'url':r.url,'http_status':r.status_code,'response_sha256':hashlib.sha256(raw).hexdigest()}
        if r.ok:
            parsed=r.json();entry['response']=parsed
            sectors=sorted({int(x['sector']) for x in parsed.get('results',[]) if 'sector' in x})
            entry['available_sectors']=sectors
        else:entry['error']=r.text[:500]
    except Exception as exc:entry={'error':repr(exc),'status':'UNKNOWN'}
    out[tic]=entry
    print(tic,entry.get('http_status'),entry.get('available_sectors'),entry.get('error'),flush=True)
(B/'sector-availability.json').write_text(json.dumps(out,indent=2)+'\n')
