import requests,json,csv,io,concurrent.futures,hashlib
from pathlib import Path
b=Path('[workspace]/Astra/made/final-night-2026-11-05/fresh18/batch01');pop=json.loads((b.parent.parent/'fresh-band-next400/population.json').read_text())['targets'];rows=list(csv.DictReader((b/'queue.csv').open()))
def run(r):
 tic=r['tic'];p=pop[tic];q=f"select source_id,ra,dec,phot_g_mean_mag from gaiadr3.gaia_source where 1=contains(point('ICRS',ra,dec),circle('ICRS',{p['ra']},{p['dec']},0.05))"
 try:
  z=requests.post('https://gea.esac.esa.int/tap-server/tap/sync',data=dict(REQUEST='doQuery',LANG='ADQL',FORMAT='csv',QUERY=q),timeout=40);z.raise_for_status();(b/tic/'gaia-neighbors.csv').write_text(z.text);return dict(tic=tic,status='success',query=q,url=z.url,sha256=hashlib.sha256(z.content).hexdigest(),n=len(list(csv.DictReader(io.StringIO(z.text)))))
 except Exception as e:return dict(tic=tic,status='failed',error=str(e),query=q)
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:o=list(ex.map(run,rows))
(b/'lead-neighbor-receipts.json').write_text(json.dumps(o,indent=2));print(o)
