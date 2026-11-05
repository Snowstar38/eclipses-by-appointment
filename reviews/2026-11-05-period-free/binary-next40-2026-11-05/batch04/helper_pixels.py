from pathlib import Path
import numpy as np,json,hashlib
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
p=Path('batch04/51321183/helper-tesscut-s061.fits')
with fits.open(p) as h:
 t=np.array(h[1].data['TIME']);F=np.array(h[1].data['FLUX']);q=np.array(h[1].data['QUALITY']);w=WCS(h[2].header)
g=np.isfinite(t)&(q==0)&np.isfinite(F).all(axis=(1,2));t=t[g];F=F[g]
bg=np.median(F[:,[0,0,-1,-1],[0,-1,0,-1]],axis=1);F=F-bg[:,None,None]
a=w.all_world2pix([[128.7041155236352,-6.074294318670607],[128.70346859527072,-6.072300151505652]],0)
in1=abs(t-2980.63936)<.055;out=(abs(t-2980.63936)>.25)&(abs(t-2980.63936)<.50)
O=np.median(F[out],axis=0);D=O-np.median(F[in1],axis=0)
y,x=np.indices(O.shape);mask=(abs(x-5)<=3)&(abs(y-5)<=3)
def cent(z):
 z=z*mask;return [(z*x).sum()/z.sum(),(z*y).sum()/z.sum()]
print('wcs',a,'centroids',cent(O),cent(D),'sky',np.median(bg),'center',np.median(F[:,5,5]),'n',sum(in1),sum(out))
fig,ax=plt.subplots(1,3,figsize=(13,4));ax[0].imshow(O,origin='lower');ax[1].imshow(D,origin='lower');ax[2].plot(t,F[:,4:7,4:7].sum((1,2))/np.median(F[:,4:7,4:7].sum((1,2))),'.',ms=1);ax[2].set_xlim(2980,2981.3)
for z in ax[:2]:z.plot(*a[0],'r+',ms=12);z.plot(*a[1],'cx',ms=9);z.plot(*cent(D),'wo',fillstyle='none')
fig.tight_layout();fig.savefig('batch04/51321183/helper-pixels.png',dpi=150)
o=dict(fits_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),target_xy=a[0].tolist(),neighbor_xy=a[1].tolist(),baseline_centroid=cent(O),difference_centroid=cent(D),sky_median=float(np.median(bg)),target_pixel_median=float(np.median(F[:,5,5])),n_in=int(sum(in1)),n_out=int(sum(out)),core_btjd=[float(t[in1].min()),float(t[in1].max())],baseline_coverage=[float(t[out].min()),float(t[out].max())],method='median difference, 7x7 signed centroid, four corner median sky; target +, capable neighbor x',caveat='WCS and PRF systematic errors; proximity 0.36 pixel; centroid alone cannot establish source ownership')
Path('batch04/51321183/helper-pixels.json').write_text(json.dumps(o,indent=2))
