# blind dip census on raw SAP (QUALITY==0): bin to 30 min, divide by 2-d running median, list contiguous runs below threshold
from common import *
def runmed(t,f,w):
    return np.array([np.nanmedian(f[np.abs(t-ti)<w/2]) for ti in t])
for tic in GAIA:
    print('=====',tic)
    for s in load(tic, author='QLP') + load(tic, author='TESS-SPOC'):
        t,f=s['t'],s['f']
        # bin 30 min
        tb=np.arange(t.min(),t.max()+0.0209,0.0208333)
        idx=np.digitize(t,tb); 
        bt=np.array([t[idx==i].mean() for i in np.unique(idx)]); bf=np.array([np.median(f[idx==i]) for i in np.unique(idx)])
        trend=runmed(bt,bf,2.0); r=bf/trend-1
        sig=1.4826*np.median(np.abs(r-np.median(r)))
        low=r< -max(3*sig,1.5e-3)
        # group runs
        runs=[];i=0
        while i<len(low):
            if low[i]:
                j=i
                while j+1<len(low) and low[j+1] and bt[j+1]-bt[j]<0.1: j+=1
                if j-i>=2: runs.append((bt[i],bt[j],r[i:j+1].min(),j-i+1))
                i=j+1
            else: i+=1
        print(s['author'],'s%d'%s['sector'],'sig30=%.2fppt'%(1e3*sig),' '.join('[%.3f-%.3f min%.1fppt n%d]'%(a,b,1e3*c,n) for a,b,c,n in runs))
