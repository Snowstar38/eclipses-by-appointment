from pathlib import Path
import numpy as np,json
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).parent
with fits.open(B/'helper-cut-1535458-s98.fits') as h:
 a=h[1].data;t=np.array(a['TIME']);f=np.array(a['FLUX']);q=np.array(a['QUALITY']);ok=(q==0)&np.isfinite(t)&np.isfinite(f).all(axis=(1,2));t=t[ok];f=f[ok];wins=[(4015.3,4015.6),(4016.3,4016.6),(4017.8,4018.1)];ims=[np.median(f[(t>l)&(t<r)],axis=0) for l,r in wins];diff=(ims[0]+ims[2])/2-ims[1];bg=[float(np.median(np.sort(i.ravel())[:30])) for i in ims];d=diff-(bg[0]+bg[2])/2+bg[1];fig,axs=plt.subplots(1,2,figsize=(9,4));axs[0].imshow(ims[0],origin='lower');axs[1].imshow(d,origin='lower',cmap='RdBu_r');
 for ax in axs:ax.plot(5.949,5.206,'gx');
 fig.tight_layout();fig.savefig(B/'helper-Q005-s98-diff.png');print('background',bg,'target pixel difference',float(d[5,6]));(B/'helper-Q005-s98-diff.json').write_text(json.dumps({'windows':wins,'background_medians':bg,'target_pixel_difference':float(d[5,6])},indent=2))
