from pathlib import Path
import numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).parent
with fits.open(B/'helper-cut-1535458.fits') as h:
 a=h[1].data;t=np.array(a['TIME']);f=np.array(a['FLUX']);q=np.array(a['QUALITY']);good=(q==0)&np.isfinite(t)&np.isfinite(f).all(axis=(1,2));t=t[good];f=f[good];bg=np.median(np.sort(f.reshape(len(f),-1),axis=1)[:,:30],axis=1);x=t-2194.214; y=np.sum(f[:,4:7,5:8],axis=(1,2))-9*bg;cut=abs(x)<2; x=x[cut];y=y[cut]; y=y/np.median(y);fig,ax=plt.subplots(figsize=(9,3));ax.plot(x,y,'.',ms=2);ax.axvline(0,color='r');ax.grid();ax.set_title('Q005 s32 TESSCut 3x3 sky subtracted');fig.tight_layout();fig.savefig(B/'helper-Q005-aperture.png')
