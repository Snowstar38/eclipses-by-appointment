import json
from pathlib import Path
import numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent
receipts=json.loads((B/'lead-extra-sector-receipts.json').read_text());out=[]
for r in receipts:
 if 'fits_path' not in r:continue
 with fits.open(r['fits_path']) as h:
  a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['FLUX'],float);q=np.asarray(a['QUALITY'],int);hdr=h[2].header
 # Simple centered 3x3 aperture, four corner background. It is a descriptive second reduction only.
 sky=np.nanmedian(f[:,[0,0,4,4],[0,4,0,4]],axis=1)
 flux=np.nansum(f[:,1:4,1:4],axis=(1,2))-9*sky
 ok=np.isfinite(t)&np.isfinite(flux)&(flux>0)&(q==0)
 tt=t[ok];y=flux[ok];
 if len(tt)<10:continue
 med=np.median(y);yn=y/med
 res=dict(tic=r['tic'],sector=r['sector'],source_sha256=r['fits_sha256'],first_btjd=float(tt.min()),last_btjd=float(tt.max()),n=len(tt),median_target_region_flux=float(med),median_sky_pixel=float(np.median(sky[ok])),wcs_center=(hdr.get('CRVAL1'),hdr.get('CRVAL2')),minimum_btjd=float(tt[np.argmin(yn)]),minimum_normalized_flux=float(np.min(yn)))
 out.append(res)
 fig,ax=plt.subplots(figsize=(11,2.8));ax.plot(tt,yn,'.',ms=.8);ax.set_ylim(max(.4,np.quantile(yn,.001)-.03),min(1.6,np.quantile(yn,.999)+.03));ax.set_title(f"TIC {r['tic']} S{r['sector']} centered 3x3 TESSCut aperture, exploratory");ax.set_xlabel('BTJD');ax.set_ylabel('normalized flux');fig.tight_layout();fig.savefig(B/r['tic']/f'lead-extra-s{r["sector"]}.png',dpi=140);plt.close(fig)
 print(r['tic'],r['sector'],round(tt.min(),2),round(tt.max(),2),len(tt),round(med,2),flush=True)
(B/'lead-extra-photometry.json').write_text(json.dumps(out,indent=2),encoding='utf8')
