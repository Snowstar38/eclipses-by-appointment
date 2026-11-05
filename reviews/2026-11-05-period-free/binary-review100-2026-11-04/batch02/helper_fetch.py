import csv,json,requests,hashlib,zipfile,io
from pathlib import Path
B=Path(__file__).resolve().parent;Q={r['tic']:r for r in csv.DictReader((B/'queue.csv').open())};H=B/'helper-pixels';H.mkdir(exist_ok=True);tic='467963921';sector=94
q="SELECT source_id,ra,dec,phot_g_mean_mag FROM gaiadr3.gaia_source WHERE 1=CONTAINS(POINT('ICRS',ra,dec),CIRCLE('ICRS',%s,%s,0.0166666666667))"%(Q[tic]['ra_deg'],Q[tic]['dec_deg'])
try:
 r=requests.post('https://gaia.aip.de/tap/sync',data={'REQUEST':'doQuery','LANG':'ADQL','FORMAT':'votable','QUERY':q},timeout=50);(H/'gaia.raw').write_bytes(r.content);(H/'gaia-receipt.json').write_text(json.dumps({'query':q,'url':r.url,'status':r.status_code,'sha256':hashlib.sha256(r.content).hexdigest()},indent=2));r.raise_for_status()
except Exception as e: print('gaia error',repr(e),flush=True)
h=H/tic;h.mkdir(exist_ok=True);s={'sector':sector,'approx_mid_btjd':3865.633,'duration_days':.14}
try:
 r=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/astrocut',params={'ra':Q[tic]['ra_deg'],'dec':Q[tic]['dec_deg'],'y':11,'x':11,'units':'px','sector':sector},timeout=50);(h/'tesscut.raw').write_bytes(r.content);s.update(url=r.url,status=r.status_code,raw_sha256=hashlib.sha256(r.content).hexdigest());r.raise_for_status();z=zipfile.ZipFile(io.BytesIO(r.content));s['member']=z.namelist()[0];data=z.read(s['member']);(h/'tesscut.fits').write_bytes(data);s['fits_sha256']=hashlib.sha256(data).hexdigest()
except Exception as e:s['error']=repr(e)
(h/'receipt.json').write_text(json.dumps(s,indent=2));print(s,flush=True)
