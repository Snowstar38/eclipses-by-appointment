from pathlib import Path
import requests,json,csv,hashlib
B=Path(__file__).resolve().parent;r=next(r for r in csv.DictReader((B/'queue.csv').open()) if r['tic']=='27681485');query=f"SELECT source_id,ra,dec,phot_g_mean_mag FROM gaiadr3.gaia_source WHERE 1=CONTAINS(POINT('ICRS',ra,dec),CIRCLE('ICRS',{r['ra_deg']},{r['dec_deg']},0.03))"
z={'tic':r['tic'],'query':query}
try:
 rr=requests.get('https://gea.esac.esa.int/tap-server/tap/sync',params={'REQUEST':'doQuery','LANG':'ADQL','FORMAT':'csv','QUERY':query},timeout=25);rr.raise_for_status();(B/r['tic']/'lead-neighbours-retry.csv').write_bytes(rr.content);z.update(url=rr.url,status=rr.status_code,sha256=hashlib.sha256(rr.content).hexdigest(),rows=list(csv.DictReader(rr.text.splitlines())))
except Exception as e:z['error']=str(e)
(B/'lead-neighbour-retry.json').write_text(json.dumps(z,indent=2));print(z)
