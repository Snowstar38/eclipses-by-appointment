"""Bounded uncached-sector target 3x3 cutouts for N005 S93 and N010 S102."""
from pathlib import Path
import csv,json,hashlib,requests,zipfile,io
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;Q={r['sample_id']:r for r in csv.DictReader((B/'queue.csv').open())}
out=[]
for sid,sector in [('N005',93),('N010',102)]:
 r=Q[sid];p=B/r['tic']/f's{sector}-tesscut.fits';url='https://mast.stsci.edu/tesscut/api/v0.1/astrocut';params={'ra':r['ra_deg'],'dec':r['dec_deg'],'x':11,'y':11,'units':'px','sector':sector};rec={'sample_id':sid,'tic':r['tic'],'sector':sector,'request_url':requests.Request('GET',url,params=params).prepare().url}
 try:
  if not p.exists():
   v=requests.get(url,params=params,timeout=120);rec['http_status']=v.status_code;v.raise_for_status();z=zipfile.ZipFile(io.BytesIO(v.content));p.write_bytes(z.read(z.namelist()[0]))
  rec['fits_sha256']=hashlib.sha256(p.read_bytes()).hexdigest()
  with fits.open(p,memmap=False) as h:
   a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['FLUX'],float);q=np.asarray(a['QUALITY'],int);w=WCS(h[2].header)
  tx,ty=map(float,w.all_world2pix(float(r['ra_deg']),float(r['dec_deg']),0));yy,xx=np.indices(f.shape[1:]);mask=(abs(xx-round(tx))<=1)&(abs(yy-round(ty))<=1)
  good=np.isfinite(t)&(q==0)&np.isfinite(f).all(axis=(1,2));t=t[good];f=f[good]
  rec.update(total_rows=int(len(q)),quality0_rows=int(np.sum(q==0)),finite_good_rows=int(np.sum(good)))
  if len(t)==0:
   rec.update(target_pixel=[tx,ty],mask_pixels=int(mask.sum()),interpretation='No valid q0 finite cutout cadences; cannot furnish a sensitive null.')
   out.append(rec);print(rec,flush=True);continue
  bg=np.median(np.sort(f.reshape(len(f),-1),axis=1)[:,:40],axis=1);flux=(f-bg[:,None,None])[:,mask].sum(axis=1)
  rec.update(target_pixel=[tx,ty],mask_pixels=int(mask.sum()),first_btjd=float(t.min()),last_btjd=float(t.max()),n=len(t),median_flux=float(np.median(flux)),positive_fraction=float(np.mean(flux>0)),max_gap_days=float(np.max(np.diff(t))))
  fig,ax=plt.subplots(figsize=(13,4));ax.plot(t,flux,'.',ms=1);ax.set_title(f'{sid} S{sector} target 3x3 raw TESSCut q0');ax.set_xlabel('BTJD');fig.tight_layout();fig.savefig(B/r['tic']/f's{sector}-raw.png',dpi=150);plt.close(fig)
 except Exception as ex:rec['error']=repr(ex)
 out.append(rec);print(rec,flush=True)
(B/'latest-check.json').write_text(json.dumps(out,indent=2)+'\n')
