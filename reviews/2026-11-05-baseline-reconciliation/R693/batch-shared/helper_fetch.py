import json,requests,concurrent.futures,zipfile,io,hashlib
from pathlib import Path
from astropy.io.votable import parse_single_table
B=Path(__file__).resolve().parent; H=B/'helper-pixels'; D=json.loads((B/'SOURCE-SNAPSHOT.json').read_text(encoding='utf8'))
def run(item):
 tic,s=item; h=H/tic;h.mkdir(exist_ok=True);g=s['target']['gaia'];ra=float(g['ra']);dec=float(g['dec']);m=json.loads((B/tic/'measurements.json').read_text(encoding='utf8')); ev=[x for x in m['events'] if x.get('timing_usable')]; out={'tic':tic}
 try:
  url='https://gaia.aip.de/conesearch/api/gaiadr3.gaia_source/';p=h/'gaia-cone.xml'; r=requests.get(url,params={'RA':ra,'DEC':dec,'SR':1/60},timeout=45);r.raise_for_status();p.write_bytes(r.content); tab=parse_single_table(p).to_table();ids=[str(x['datalinkID']) for x in tab];q='SELECT source_id,ra,dec,phot_g_mean_mag FROM gaiadr3.gaia_source WHERE source_id IN ('+','.join(ids)+')';r=requests.get('https://gaia.aip.de/tap/sync',params={'REQUEST':'doQuery','LANG':'ADQL','QUERY':q},timeout=45);r.raise_for_status();(h/'gaia.xml').write_bytes(r.content);out['gaia_count']=len(ids)
 except Exception as e:out['gaia_error']=repr(e)
 if ev:
  e=max(ev,key=lambda x:x['depth_ppt']/x['oot_scatter_ppt']);sec=e['sector'];out['event']=e
  try:
   url='https://mast.stsci.edu/tesscut/api/v0.1/astrocut';args={'ra':ra,'dec':dec,'y':11,'x':11,'units':'px','sector':sec};r=requests.get(url,params=args,timeout=120);r.raise_for_status(); z=zipfile.ZipFile(io.BytesIO(r.content)); (h/'tesscut.zip').write_bytes(r.content);name=z.namelist()[0];(h/'tesscut.fits').write_bytes(z.read(name));out['tesscut_url']=r.url;out['tesscut_sha256']=hashlib.sha256((h/'tesscut.fits').read_bytes()).hexdigest();out['tesscut_member']=name
  except Exception as x:out['tesscut_error']=repr(x)
 (h/'receipt.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8');return out
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
 for x in ex.map(run,D.items()):print(x['tic'],x.get('gaia_count'),x.get('gaia_error'),x.get('tesscut_error'),flush=True)
