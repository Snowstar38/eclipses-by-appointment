"""Overview of raw QLP SAP_FLUX (all cadences; red = flagged), SAP_BKG, with predicted A/B from classifier eclipse ephemeris."""
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vetlib import load_qlp
D='[local path omitted]'; S=[12,39,65,103]
P=26.2618; T0=2372.695; ph2=0.302
fig,ax=plt.subplots(8,1,figsize=(18,26))
for i,s in enumerate(S):
    d=load_qlp(D+f'255077215_s{s:03d}.fits'); t,f,q,b=d['t'],d['f'],d['q'],d['bkg']
    print(s, len(t), (q==0).sum(), t.min(), t.max(), 'flag bits', np.unique(q))
    a=ax[2*i]; a.plot(t[q==0],f[q==0],'k.',ms=1); a.plot(t[q!=0],f[q!=0],'r.',ms=1); a.set_ylim(0.92,1.02)
    for k in range(-40,80):
        for off,c in ((0,'b'),(ph2,'g')):
            x=T0+(k+off)*P
            if t.min()-1<x<t.max()+1: a.axvline(x,color=c,alpha=.4)
    a.set_title(f's{s}')
    a=ax[2*i+1]; a.plot(t,b,'k.',ms=1); a.set_title('bkg')
plt.tight_layout(); plt.savefig('overview.png',dpi=50)
