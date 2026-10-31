"""s006 around the post-gap event: flux, background, centroids (QLP and TESS-SPOC), and same post-gap interval in s033 for comparison -> zoom6.png"""
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt, glob
from astropy.io import fits
V='[local path omitted]'
fl=[(V+'60583013_s006.fits','SAP_FLUX','SAP_BKG','SAP_X','SAP_Y'),(glob.glob(V+'vet60583013/*tess-spoc*s0006*')[0],'SAP_FLUX','SAP_BKG','MOM_CENTR1','MOM_CENTR2')]
fig,ax=plt.subplots(4,2,figsize=(14,12),sharex=True)
for j,(fn,fc,bc,xc,yc) in enumerate(fl):
    d=fits.getdata(fn,1); t=d['TIME']; m=(t>1477.9)&(t<1481)&np.isfinite(d[fc]); q=d['QUALITY'][m]
    for i,c in enumerate((fc,bc,xc,yc)):
        v=d[c][m]; ax[i,j].plot(t[m][q==0],v[q==0],'k.',ms=3); ax[i,j].plot(t[m][q!=0],v[q!=0],'r.',ms=3); ax[i,j].set_ylabel(c); ax[i,j].axvspan(1478.63,1479.02,color='y',alpha=.3)
    ax[0,j].set_title(fn.split('/')[-1][:40])
plt.tight_layout(); plt.savefig('zoom6.png',dpi=60)
