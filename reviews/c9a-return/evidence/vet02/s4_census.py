# Blind dip census on raw SAP (QUALITY==0): residual from 2-d running median; group runs below threshold.
import numpy as np, sys
D='/tmp/claude-0/-home-user-eclipses-paper-review/55c92ff4-798a-544f-be03-9888c6804905/scratchpad/data/vet02'
GP={'470235665':(10.32387058,391.4675317),'379251709':(12.32611934,384.9052416)}
def runmed(t,f,w):
    out=np.empty_like(f)
    for i in range(len(t)):
        m=np.abs(t-t[i])<w/2; out[i]=np.median(f[m])
    return out
for tic in GP:
    z=np.load(f'{D}/{tic}/lc_sap_q0.npz'); P,Tp=GP[tic]
    print('TIC',tic,'(phase relative to Gaia periastron, P_gaia)')
    for pipe in ['QLP','SPOC']:
        for sec in np.unique(z['s'][z['p']==pipe]):
            m=(z['p']==pipe)&(z['s']==sec); t=z['t'][m]; f=z['f'][m]
            # bin to 30 min for speed/uniformity
            tb=np.arange(t.min(),t.max()+0.0209,0.0208333); idx=np.digitize(t,tb)
            bt=np.array([t[idx==k].mean() for k in np.unique(idx)]); bf=np.array([np.median(f[idx==k]) for k in np.unique(idx)])
            r=bf-runmed(bt,bf,2.0); sig=1.4826*np.median(np.abs(r-np.median(r)))
            low=r< -max(4*sig,0.0015)
            gaps=np.where(np.diff(bt)>0.25)[0]
            # group
            ev=[];cur=[]
            for i in np.where(low)[0]:
                if cur and bt[i]-bt[cur[-1]]>0.1: ev.append(cur);cur=[]
                cur.append(i)
            if cur: ev.append(cur)
            s=f'  {pipe} s{sec}: sig30={1e3*sig:.2f}ppt gaps(>6h) at '+','.join(f'{bt[g]:.2f}-{bt[g+1]:.2f}' for g in gaps)
            print(s)
            for e in ev:
                if len(e)<2: continue
                k=e[np.argmin(r[e])]
                print(f'     dip t_min={bt[k]:.3f} depth={-1e3*r[k]:.1f}ppt npts={len(e)} dur~{(bt[e[-1]]-bt[e[0]])*24+0.5:.1f}h phase={((bt[k]-Tp)/P)%1:.4f}')
