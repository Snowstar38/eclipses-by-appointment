import json,requests,hashlib
from pathlib import Path
B=Path(__file__).resolve().parent; D=json.loads((B/'SOURCE-SNAPSHOT.json').read_text()); H=B/'helper-pixels'; H.mkdir(exist_ok=True)
q='SELECT source_id,ra,dec,phot_g_mean_mag FROM gaiadr3.gaia_source WHERE '+' OR '.join("1=CONTAINS(POINT('ICRS',ra,dec),CIRCLE('ICRS',%s,%s,0.0166666666667))"%(v['target']['gaia']['ra'],v['target']['gaia']['dec']) for v in D.values())
r=requests.post('https://gaia.aip.de/tap/sync',data={'REQUEST':'doQuery','LANG':'ADQL','FORMAT':'votable','QUERY':q},timeout=180); (H/'gaia-all.raw').write_bytes(r.content); (H/'gaia-receipt.json').write_text(json.dumps({'url':r.url,'query':q,'status':r.status_code,'headers':dict(r.headers),'raw_sha256':hashlib.sha256(r.content).hexdigest()},indent=2));r.raise_for_status(); print(r.status_code,len(r.content))
