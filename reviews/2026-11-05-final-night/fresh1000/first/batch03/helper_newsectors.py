import requests,zipfile,io,hashlib,json
from pathlib import Path
from astropy.io import fits
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
D=Path(r'[workspace]/Astra\made\final-night-2026-11-05\fresh1000\first\batch03\47853068'); out=[]
for sec in (107,108,109):
 try:
  r=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/astrocut',params={'ra':98.0530429272,'dec':-21.6313341331,'x':7,'y':7,'units':'px','sector':sec},timeout=120); r.raise_for_status(); z=zipfile.ZipFile(io.BytesIO(r.content)); raw=z.read(z.namelist()[0]); p=D/f'helper-s{sec}-tesscut.fits';p.write_bytes(raw)
  with fits.open(io.BytesIO(raw)) as f:
   t=np.array(f[1].data['TIME'],float); q=np.array(f[1].data['QUALITY'],int); cube=np.array(f[1].data['FLUX'],float)
  yy,xx=np.indices(cube.shape[1:]); ap=(abs(xx-3)<=1)&(abs(yy-3)<=1); sky=np.hypot(xx-3,yy-3)>2.8; bg=np.nanmedian(cube[:,sky],axis=1); flux=np.nansum(cube[:,ap]-bg[:,None],axis=1); good=(q==0)&np.isfinite(t)&np.isfinite(flux); norm=np.nanmedian(flux[good]);
  fig,ax=plt.subplots(figsize=(12,3));ax.plot(t[good],flux[good]/norm,'.',ms=1);ax.set_title(f'TIC 47853068 S{sec} 3x3, quality=0');ax.set_xlabel('BTJD');ax.set_ylabel('relative flux');fig.tight_layout();fig.savefig(D/f'helper-s{sec}-full.png',dpi=140);plt.close(fig)
  out.append({'sector':sec,'status':'ok','url':r.url,'zip_sha256':hashlib.sha256(r.content).hexdigest(),'fits_sha256':hashlib.sha256(raw).hexdigest(),'n_quality_zero':int(good.sum()),'first_btjd':float(t[good].min()),'last_btjd':float(t[good].max())})
 except Exception as e:out.append({'sector':sec,'status':'failed','error':repr(e)})
 print(out[-1],flush=True)
(D/'helper-newsectors.json').write_text(json.dumps(out,indent=2))
