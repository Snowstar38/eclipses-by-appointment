import requests,hashlib,json,csv,io
from pathlib import Path
B=Path(__file__).resolve().parent
jobs=[('147413927',163.21764583099278,-47.70130734349548),('265066551',347.36321314194146,68.42988151080459)]
out=[]
for tic,ra,dec in jobs:
 q=f"SELECT source_id,ra,dec,phot_g_mean_mag,DISTANCE(POINT('ICRS',ra,dec),POINT('ICRS',{ra},{dec}))*3600 AS sep_arcsec FROM gaiadr3.gaia_source WHERE 1=CONTAINS(POINT('ICRS',ra,dec),CIRCLE('ICRS',{ra},{dec},0.0333333333)) ORDER BY sep_arcsec"
 try:
  r=requests.post('https://gaia.ari.uni-heidelberg.de/tap/sync',data=dict(REQUEST='doQuery',LANG='ADQL',FORMAT='csv',QUERY=q),timeout=80);r.raise_for_status();p=B/tic/'helper-gaia-cone.csv';p.write_bytes(r.content); rows=list(csv.DictReader(io.StringIO(r.text)));out.append(dict(tic=tic,query=q,status=r.status_code,sha256=hashlib.sha256(r.content).hexdigest(),rows=len(rows)))
 except Exception as e:out.append(dict(tic=tic,query=q,error=repr(e)))
(B/'helper-gaia-cone-receipt.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
