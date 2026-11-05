import csv,json,requests,hashlib,zipfile,io,concurrent.futures
from pathlib import Path
B=Path(__file__).resolve().parent; Q={r['tic']:r for r in csv.DictReader((B/'queue.csv').open())}; H=B/'helper-pixels';H.mkdir(exist_ok=True)
def run(case):
 tic,sector=case; z=Q[tic]; h=H/tic;h.mkdir(exist_ok=True); s={'sector':sector}
 q="SELECT source_id,ra,dec,phot_g_mean_mag FROM gaiadr3.gaia_source WHERE 1=CONTAINS(POINT('ICRS',ra,dec),CIRCLE('ICRS',%s,%s,0.0166666666667))"%(z['ra_deg'],z['dec_deg'])
 for typ in ['gaia','tesscut']:
  try:
   if typ=='gaia': r=requests.post('https://gaia.aip.de/tap/sync',data={'REQUEST':'doQuery','LANG':'ADQL','FORMAT':'votable','QUERY':q},timeout=45)
   else: r=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/astrocut',params={'ra':z['ra_deg'],'dec':z['dec_deg'],'y':11,'x':11,'units':'px','sector':sector},timeout=45)
   (h/(typ+'.raw')).write_bytes(r.content);s[typ]={'url':r.url,'status':r.status_code,'sha256':hashlib.sha256(r.content).hexdigest()};r.raise_for_status()
   if typ=='tesscut':
    v=zipfile.ZipFile(io.BytesIO(r.content)); data=v.read(v.namelist()[0]);(h/'tesscut.fits').write_bytes(data);s[typ]['fits_sha256']=hashlib.sha256(data).hexdigest()
  except Exception as e:s[typ+'_error']=repr(e)
 (h/'receipt.json').write_text(json.dumps(s,indent=2));print(tic,s,flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:list(ex.map(run,[('299187993',38),('294257329',36),('224631871',55),('113645244',67)]))
