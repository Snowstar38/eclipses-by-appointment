import requests,csv,json,hashlib,concurrent.futures
from pathlib import Path
B=Path(__file__).resolve().parent;Q={r['tic']:r for r in csv.DictReader((B/'queue.csv').open())}
def get(tic):
 r=Q[tic];query=f"SELECT source_id,ra,dec,phot_g_mean_mag FROM gaiadr3.gaia_source WHERE 1=CONTAINS(POINT('ICRS',ra,dec),CIRCLE('ICRS',{r['ra_deg']},{r['dec_deg']},0.03))";z=dict(tic=tic,query=query)
 try:
  rr=requests.post('https://gea.esac.esa.int/tap-server/tap/sync',data={'REQUEST':'doQuery','LANG':'ADQL','FORMAT':'csv','QUERY':query},timeout=35);p=B/tic/'lead-neighbours.csv';p.write_bytes(rr.content);z.update(status=rr.status_code,sha256=hashlib.sha256(rr.content).hexdigest(),rows=list(csv.DictReader(rr.text.splitlines())));rr.raise_for_status()
 except Exception as e:z['error']=str(e)
 return z
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:out=list(ex.map(get,['233405109','27681485']))
(B/'lead-neighbour-receipts.json').write_text(json.dumps(out,indent=2));print([(x['tic'],len(x.get('rows',[])),x.get('error')) for x in out])
