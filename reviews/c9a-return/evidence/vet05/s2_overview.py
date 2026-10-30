import numpy as np, sys
from common import *
for tic,secs in [('15855794',[44,70,71]),('92881948',[5,6,32,98])]:
    for a in ['QLP','TESS-SPOC']:
        for s in secs:
            r=load(tic,a,s)
            if r is None: continue
            t,f,e,q=r
            dt=np.median(np.diff(t))
            print(tic,a,s,'N=%d'%len(t),'t=%.3f-%.3f'%(t.min(),t.max()),'cad=%.2fmin'%(dt*1440),
                  'rms=%.2fppt'%(1e3*np.std(np.diff(f))/np.sqrt(2)),'min=%.4f'%f.min(), 'Nflagged=%d'%(q!=0).sum())
