"""Overview of the three QLP sectors, raw SAP, all cadences (flagged red). python look.py -> look.png, prints flags summary"""
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from astropy.io import fits
D='[local path omitted]'
fig,ax=plt.subplots(3,1,figsize=(18,10))
for a,s in zip(ax,(7,33,87)):
    d=fits.open(D+f'178486571_s{s:03d}.fits')[1].data
    t=d['TIME'];f=d['SAP_FLUX'];q=d['QUALITY'];ok=np.isfinite(t)&np.isfinite(f)
    t,f,q=t[ok],f[ok],q[ok]; f=f/np.median(f[q==0])
    print(s,d.columns.names, len(t), 'span',t.min(),t.max(),'flagged',(q!=0).sum(), np.unique(q))
    a.plot(t[q==0],f[q==0],'k.',ms=1);a.plot(t[q!=0],f[q!=0],'r.',ms=1);a.set_ylim(0.9,1.03);a.set_title(f's{s}')
plt.tight_layout();plt.savefig('look.png',dpi=60)
