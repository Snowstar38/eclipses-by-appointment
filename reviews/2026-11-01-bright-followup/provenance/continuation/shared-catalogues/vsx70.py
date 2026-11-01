"""Fresh IDIA VSX 60-arcsec cones; preserve raw results and errors."""
import hashlib, json, urllib.parse, urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
HERE=Path(__file__).resolve().parent
DEST=HERE/'vsx';DEST.mkdir(exist_ok=True)
targets=json.loads((HERE/'targets-selected.json').read_text())
def fetch(item):
    tic,t=item
    params={'-source':'B/vsx/vsx','-c':f"{t['ra']} {t['dec']}",'-c.rs':60,'-out':'Name,Type,Period,RAJ2000,DEJ2000','-out.add':'_r','-out.max':100,'-sort':'_r'}
    url='http[local path omitted]'+urllib.parse.urlencode(params)
    r={'tic':tic,'url':url,'queried_at_utc':datetime.now(timezone.utc).isoformat()}
    try:
        with urllib.request.urlopen(url,timeout=15) as response:raw=response.read(1000000)
        (DEST/(tic+'.tsv')).write_bytes(raw)
        text=raw.decode('latin-1')
        assert 'VizieR' in text and '<html' not in text.lower(), 'Unexpected response'
        assert '#ERROR' not in text and 'QUERY_STATUS=ERROR' not in text,'Service error'
        lines=[x for x in text.splitlines() if x and not x.startswith('#')]
        if lines:
            header=[x.strip() for x in lines[0].split('\t')]
            assert 'Name' in header and 'Type' in header,'Unknown table layout'
            matches=[dict(zip(header,[v.strip() for v in line.split('\t')])) for line in lines[3:]]
            assert len(matches)<100,'Possible truncated cone'
        else:
            assert 'B/vsx/vsx' in text and ('No object found' in text or '#INFO' in text), 'Empty response not established'
            matches=[]
        r.update(status='success',rows=matches,sha256=hashlib.sha256(raw).hexdigest())
    except Exception as ex:r.update(status='unavailable',error=str(ex))
    return r
with ThreadPoolExecutor(max_workers=8) as pool:results=list(pool.map(fetch,targets.items()))
(HERE/'vsx70-receipts.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
print(json.dumps({'queried':len(results),'success':sum(r['status']=='success' for r in results),'with_rows':sum(bool(r.get('rows')) for r in results),'failed':[{'tic':r['tic'],'error':r['error']} for r in results if r['status']!='success']},indent=2))

