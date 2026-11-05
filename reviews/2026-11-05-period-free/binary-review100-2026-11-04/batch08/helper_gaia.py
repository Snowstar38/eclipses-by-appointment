import requests,csv,json
from pathlib import Path
B=Path(__file__).resolve().parent
rows={r['tic']:r for r in csv.DictReader((B/'queue.csv').open())}
out={}
for tic in ('423569223','393487481','41859748'):
 r=rows[tic];ra=r['ra_deg'];dec=r['dec_deg'];q=f"SELECT TOP 200 source_id,ra,dec,phot_g_mean_mag FROM gaiadr3.gaia_source WHERE 1=CONTAINS(POINT('ICRS',ra,dec),CIRCLE('ICRS',{ra},{dec},0.04)) ORDER BY phot_g_mean_mag"
 try:
  resp=requests.post('https://gea.esac.esa.int/tap-server/tap/sync',data={'REQUEST':'doQuery','LANG':'ADQL','FORMAT':'csv','QUERY':q},timeout=35);resp.raise_for_status(); (B/tic/'helper-gaia-neighbors.csv').write_text(resp.text);out[tic]={'status':resp.status_code,'bytes':len(resp.content),'query':q}
 except Exception as e:out[tic]={'error':repr(e),'query':q}
 print(tic,out[tic],flush=True)
(B/'helper-gaia-receipts.json').write_text(json.dumps(out,indent=2)+'\n')
