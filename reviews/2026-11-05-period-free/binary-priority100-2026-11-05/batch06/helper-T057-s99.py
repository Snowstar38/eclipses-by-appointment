from pathlib import Path
from astropy.io import fits
from astropy.wcs import WCS
import numpy as np,hashlib,json
B=Path(__file__).resolve().parent;p=next((B/'280963520').glob('*astrocut.fits'))
with fits.open(p) as h:
 f=np.asarray(h[1].data['FLUX']);xy=WCS(h[2].header).world_to_pixel_values(144.7027809786,-49.51336098);med=np.nanmedian(f,axis=0)
 out={'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'n_frames':len(f),'target_wcs_zero_based_xy':[float(x) for x in xy],'median_flux_by_row':med.tolist(),'conclusion':'Target pixel and surrounding columns approximately zero; nonzero column 0. Invalid target-flux test; no sensitive recurrence conclusion.'}
 (B/'helper-T057-s99.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
