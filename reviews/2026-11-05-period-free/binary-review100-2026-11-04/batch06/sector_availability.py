import csv, hashlib, json
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import requests
B=Path(__file__).resolve().parent
Q=list(csv.DictReader((B/'queue.csv').open()))
def check(q):
    tic=q['tic']
    try:
        r=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/sector',params={'ra':q['ra_deg'],'dec':q['dec_deg']},timeout=30)
        raw=r.content
        (B/tic/'sector-availability.raw').write_bytes(raw)
        rec={'url':r.url,'http_status':r.status_code,'response_sha256':hashlib.sha256(raw).hexdigest()}
        if r.ok:
            rec['available_sectors']=sorted({int(x['sector']) for x in r.json().get('results',[]) if 'sector' in x})
        else:rec['error']=r.text[:500]
    except Exception as exc:rec={'error':repr(exc),'status':'UNKNOWN'}
    return tic,rec
with ThreadPoolExecutor(max_workers=4) as ex:out=dict(ex.map(check,Q))
for q in Q:
    t=q['tic'];cached=set(int(x['sector']) for x in json.loads((B/t/'raw-inspection.json').read_text())['sectors']);available=set(out[t].get('available_sectors',[]));out[t]['uncached_sectors']=sorted(available-cached)
    print(q['sample_id'],t,'uncached',out[t]['uncached_sectors'],'error',out[t].get('error'),flush=True)
(B/'sector-availability.json').write_text(json.dumps(out,indent=2)+'\n')
