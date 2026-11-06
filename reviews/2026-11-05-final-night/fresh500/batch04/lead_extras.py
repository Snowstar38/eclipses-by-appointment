import json,requests,io,zipfile,hashlib,numpy as np
from pathlib import Path
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
b=Path(__file__).resolve().parent;p=json.load(open(b.parent.parent/'fresh-band-extra500/population.json'))['targets'];out=[]
for tic,secs in [('48099288',[87,107,108,109]),('179293951',[65,102])]:
 for sec in secs:
  d=b/tic;receipt=dict(tic=tic,sector=sec,ra=p[tic]['ra'],dec=p[tic]['dec'])
  try:
   r=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/astrocut',params=dict(ra=p[tic]['ra'],dec=p[tic]['dec'],x=5,y=5,units='px',sector=sec),timeout=90);r.raise_for_status();z=zipfile.ZipFile(io.BytesIO(r.content));raw=z.read(z.namelist()[0]);f=d/f'extra-s{sec}.fits';f.write_bytes(raw)
   with fits.open(io.BytesIO(raw)) as h:t=np.array(h[1].data['TIME']);q=np.array(h[1].data['QUALITY']);cube=np.array(h[1].data['FLUX']);flux=np.nansum(cube[:,1:4,1:4],axis=(1,2))-9*np.nanmedian(cube[:,[0,0,0,0,0,4,4,4,4,4],[0,1,2,3,4,0,1,2,3,4]],axis=1)
   good=np.isfinite(t)&np.isfinite(flux)&(q==0);t=t[good];flux=flux[good];flux/=np.median(flux);np.savez_compressed(d/f'extra-s{sec}.npz',time=t,flux=flux)
   fig,ax=plt.subplots(figsize=(12,2.5));ax.plot(t,flux,'.',ms=.8);ax.set_title(f'TIC{tic} S{sec} custom central3x3 same photons');ax.grid(alpha=.2);fig.tight_layout();fig.savefig(d/f'extra-s{sec}.png',dpi=100);plt.close(fig)
   receipt.update(status='success',path=str(f),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),request_url=r.url,n=len(t),first=float(t.min()),last=float(t.max()))
  except Exception as e:receipt.update(status='failed',error=repr(e))
  out.append(receipt);print(tic,sec,receipt['status'],receipt.get('error'),flush=True)
(b/'lead-extra-sector-receipts.json').write_text(json.dumps(out,indent=2))
