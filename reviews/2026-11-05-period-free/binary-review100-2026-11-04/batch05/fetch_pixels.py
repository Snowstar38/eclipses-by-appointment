"""Fetch TESSCut pixel stamps and nearby Gaia sources for two decisive events."""
import csv,json,requests,hashlib,zipfile,io
from pathlib import Path
B=Path(__file__).resolve().parent;Q={r['tic']:r for r in csv.DictReader((B/'queue.csv').open())};H=B/'lead-pixels';H.mkdir(exist_ok=True)
cases=[('313617927',15,1729.9,1.5),('198182954',74,3324.49,1.6),('246124257',66,3101.055,.12),('174187654',93,3837.15,1.6)]
query='SELECT source_id,ra,dec,phot_g_mean_mag FROM gaiadr3.gaia_source WHERE '+' OR '.join("1=CONTAINS(POINT('ICRS',ra,dec),CIRCLE('ICRS',%s,%s,0.0166666666667))"%(Q[t]['ra_deg'],Q[t]['dec_deg']) for t,_,_,_ in cases)
try:
 r=requests.post('https://gaia.aip.de/tap/sync',data={'REQUEST':'doQuery','LANG':'ADQL','FORMAT':'votable','QUERY':query},timeout=90)
 (H/'gaia.raw').write_bytes(r.content);(H/'gaia-receipt.json').write_text(json.dumps({'query':query,'url':r.url,'status':r.status_code,'sha256':hashlib.sha256(r.content).hexdigest()},indent=2));r.raise_for_status();print('gaia',r.status_code,len(r.content),flush=True)
except Exception as e: print('gaia error',repr(e),flush=True)
for tic,sector,mid,dur in cases:
 h=H/tic;h.mkdir(exist_ok=True);s={'sector':sector,'approx_mid_btjd':mid,'duration_days':dur}
 try:
  r=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/astrocut',params={'ra':Q[tic]['ra_deg'],'dec':Q[tic]['dec_deg'],'y':11,'x':11,'units':'px','sector':sector},timeout=90)
  (h/'tesscut.raw').write_bytes(r.content);s.update(url=r.url,status=r.status_code,raw_sha256=hashlib.sha256(r.content).hexdigest());r.raise_for_status();z=zipfile.ZipFile(io.BytesIO(r.content));s['member']=z.namelist()[0];data=z.read(s['member']);(h/'tesscut.fits').write_bytes(data);s['fits_sha256']=hashlib.sha256(data).hexdigest()
 except Exception as e:s['error']=repr(e)
 (h/'receipt.json').write_text(json.dumps(s,indent=2));print(tic,s,flush=True)

