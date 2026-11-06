import csv,json,requests,hashlib,io,concurrent.futures
from pathlib import Path
from astropy.io import fits
from astropy.wcs import WCS
import numpy as np
from scipy.optimize import least_squares
b=Path(__file__).resolve().parent
def go(row):
 tic=row['tic'];d=b/tic;l=json.loads((d/'helper-localization.json').read_text());ra=l['ra'];dec=l['dec'];query=f"SELECT source_id,ra,dec,phot_g_mean_mag FROM gaiadr3.gaia_source WHERE 1=CONTAINS(POINT('ICRS',ra,dec),CIRCLE('ICRS',{ra},{dec},0.035))"
 try:
  r=requests.post('https://gaia.ari.uni-heidelberg.de/tap/sync',data={'REQUEST':'doQuery','LANG':'ADQL','FORMAT':'csv','QUERY':query},timeout=40);r.raise_for_status();(d/'helper-gaia-neighbors.csv').write_bytes(r.content);ns=list(csv.DictReader(io.StringIO(r.text)))
  with fits.open(d/'helper-tesscut.fits') as h:w=WCS(h[2].header)
  z=np.array(l['difference']);yy,xx=np.indices(z.shape)
  def fun(v):
   amp,x,y,s,bg=v;return (amp*np.exp(-((xx-x)**2+(yy-y)**2)/(2*s*s))+bg-z).ravel()
  iy,ix=np.unravel_index(np.argmax(z),z.shape); f=least_squares(fun,[z.max()-np.median(z),ix,iy,1,np.median(z)],bounds=([0,0,0,.3,-np.inf],[np.inf,6,6,3,np.inf]));v=f.x
  for n in ns:
   x,y=w.world_to_pixel_values(float(n['ra']),float(n['dec']));n['pixel_xy']=[float(x),float(y)];n['offset_from_difference_px']=float(np.hypot(x-v[1],y-v[2]));n['offset_from_target_px']=float(np.hypot(x-l['target_xy'][0],y-l['target_xy'][1]));n['relative_G_flux']=10**(-.4*(float(n['phot_g_mean_mag'])-float(row['gaia_G']))) if n['phot_g_mean_mag'] else None
  ns.sort(key=lambda n:n['offset_from_target_px']);out={'query':query,'url':r.url,'sha256':hashlib.sha256(r.content).hexdigest(),'gaussian_xy':v[1:3].tolist(),'sigma_px':v[3],'background':v[4],'target_offset_px':float(np.linalg.norm(v[1:3]-l['target_xy'])),'neighbors':ns};(d/'helper-neighbors.json').write_text(json.dumps(out,indent=2));print(tic,'fit',v,'targetoffset',out['target_offset_px'],'neighbors',[(n['source_id'],round(n['offset_from_target_px'],2),round(n['relative_G_flux'],4) if n['relative_G_flux'] else None) for n in ns if n['offset_from_target_px']<3],flush=True)
 except Exception as e:print(tic,repr(e),flush=True)
rows=[r for r in csv.DictReader((b/'queue.csv').open()) if r['tic'] in ['469894984','248308520']]
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:list(ex.map(go,rows))
