import numpy as np
from astropy.io import fits
p=r'[local path omitted]'
with fits.open(p) as h:
 z=h[1].data;t=np.array(z['TIME']); f=np.array(z['FLUX']);q=np.array(z['QUALITY']);print('columns',z.names)
b=np.nanmedian(np.sort(f.reshape(len(t),-1),axis=1)[:,:32],axis=1)
inw=np.isfinite(t)&(abs(t-4271.61686)<.06); out=np.isfinite(t)&(abs(t-4271.61686)>.3)&(abs(t-4271.61686)<1)
print('in count and flags',inw.sum(),np.unique(q[inw],return_counts=True)); print('background med in/out',np.nanmedian(b[inw]),np.nanmedian(b[out]),'out scatter',np.nanstd(b[out]));print('A all cadence range',np.nanmin(t[(abs(t-4279.33528)<1.5)]),np.nanmax(t[(abs(t-4279.33528)<1.5)]));print('A within .4 all/q0',sum(abs(t-4279.33528)<.4),sum((abs(t-4279.33528)<.4)&(q==0)))
print('P 34', (4271.616860567667-3196.0997)/34,'neighbor cycles',[(4271.616860567667-3196.0997)/n for n in [33,35]])
