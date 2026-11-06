import requests,csv,json,hashlib,concurrent.futures
from pathlib import Path
B=Path(__file__).resolve().parent;Q={r['tic']:r for r in csv.DictReader((B/'queue.csv').open())}
def get(tic):
 r=Q[tic];p={'-source':'I/355/gaiadr3','-c':r['ra_deg']+' '+r['dec_deg'],'-c.rs':'108','-out.max':'1000','-out':'Source,RA_ICRS,DE_ICRS,Gmag','-out.add':'_r'};z={'tic':tic,'params':p}
 try:
  rr=requests.get('https://vizier.cfa.harvard.edu/viz-bin/asu-tsv',params=p,timeout=35);rr.raise_for_status();f=B/tic/'helper-gaia.tsv';f.write_bytes(rr.content);z.update(url=rr.url,status=rr.status_code,sha256=hashlib.sha256(rr.content).hexdigest())
 except Exception as e:z['error']=repr(e)
 return z
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:o=list(ex.map(get,['185744410','149316567','378411251','387124290']))
(B/'helper-gaia-receipts.json').write_text(json.dumps(o,indent=2));print(o)
