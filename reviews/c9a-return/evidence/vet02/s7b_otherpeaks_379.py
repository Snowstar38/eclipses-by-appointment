# Which individual windows produce the off-eclipse box-scan peaks (SPOC phase 0.2235, QLP 0.077)?
import numpy as np, importlib.util, sys
spec=importlib.util.spec_from_file_location('s7','s7_secondary_379.py')
src=open('s7_secondary_379.py').read().split("out=open(")[0]
exec(src)
for pipe,phc in [('SPOC',0.2235),('QLP',0.077),('QLP',0.4955)]:
    t,r,s=detrended(pipe,())
    n0=int(np.floor((t.min()-T0)/P))-1; n1=int(np.ceil((t.max()-T0)/P))+1
    print(pipe,'phase',phc)
    for n in range(n0,n1+1):
        tc=T0+(n+phc)*P; inb=np.abs(t-tc)<4.1/48
        if inb.sum()<3: continue
        dt=np.diff(t); 
        near_gap=np.min(np.abs(np.r_[t[np.where(dt>0.3)[0]],t[np.where(dt>0.3)[0]+1],t.min(),t.max()]-tc))
        print(f'   s{int(s[inb][0])} E{n} tc={tc:.3f} box mean={1e3*np.mean(r[inb]):+.2f} ppt n={inb.sum()} dist_to_gap_or_edge={near_gap:.2f} d')
