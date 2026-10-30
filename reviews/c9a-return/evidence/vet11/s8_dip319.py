# TIC 319185391: is the narrow residual dip at min I (s6: ~0.9 ppt, width 0.01-0.02 phase, 6/6 sectors) an eclipse?
# Fold at P_phot, K=6 harmonic + per-segment cubic fitted with the |phase|<0.04 window masked; then residuals in fine
# bins; trapezoid-free box fit (depth, centre, width) by grid; per-sector and odd/even depths with errors from the
# out-of-window scatter of same-width boxes (look-elsewhere / red-noise check); same test at other star(s) for control.
import sys, json, numpy as np
sys.path.insert(0,'[local path omitted]')
from common import *
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
VD='[local path omitted]'
tic=sys.argv[1]; binmin=float(sys.argv[2]) if len(sys.argv)>2 else 10.0
R3=json.load(open(f'{VD}/s3_{tic}.json')); R6=json.load(open(f'{VD}/s6_{tic}.json'))
Pph=R3['Pphot'][0]
out=open(f'{VD}/s8_{tic}_b{int(binmin)}.txt','w')
def Pr(*a):
    s=' '.join(str(x) for x in a); print(s); out.write(s+'\n')
t,f,seg,sec=load_qlp(tic,'SAP_FLUX',binmin=binmin)
# T1 from s6 (phase 0 = min I)
import re
T1=float(re.search(r'reference T\(min I\)=([0-9.]+)',open(f'{VD}/s6_{tic}.txt').read()).group(1))
ph=((t-T1)/Pph+0.5)%1-0.5
win=np.abs(ph)<0.04
A=np.hstack([poly_cols(t,seg,3),harm_cols(t,Pph,T1,6)]); m=~win
for _ in range(4):
    c,*_=np.linalg.lstsq(A[m],f[m],rcond=None); r=f-A@c; s=1.4826*np.median(np.abs(r[m&~win])); m=(np.abs(r)<4*s)&~win
good=np.abs(r)<4*s
Pr(f'TIC {tic}: P_phot={Pph:.6f}, T(min I)={T1:.4f}, {binmin}-min bins, N={len(t)}, robust sigma {s*1e3:.2f} ppt; model fitted with |phase|<0.04 masked')
# fine-binned residual profile near phase 0
edges=np.arange(-0.06,0.0601,0.005)
prof=[]
for a,b in zip(edges[:-1],edges[1:]):
    q=good&(ph>=a)&(ph<b); prof.append((0.5*(a+b),np.mean(r[q])*1e3,np.std(r[q])/np.sqrt(q.sum())*1e3,q.sum()))
Pr('residual profile near min I (phase centre, mean ppt, err, n): '+'; '.join(f'{p:+.4f} {v:+.2f}+-{e:.2f}' for p,v,e,n in prof))
# box grid fit
best=None
for w in (0.006,0.008,0.010,0.012,0.015,0.020,0.025,0.030):
    for c0 in np.arange(-0.02,0.0201,0.001):
        q=good&(np.abs(ph-c0)<w/2); qo=good&(np.abs(ph)<0.06)&~(np.abs(ph-c0)<w/2)
        d=np.mean(r[qo])-np.mean(r[q]); e=np.sqrt(np.var(r[q])/q.sum()+np.var(r[qo])/qo.sum()); snr=d/e
        if best is None or snr>best[0]: best=(snr,d*1e3,e*1e3,c0,w)
snr,dep,edep,c0,w=best
Pr(f'best box: depth {dep:.3f}+-{edep:.3f} ppt (white), centre phase {c0:+.4f}, full width {w:.3f} phase = {w*Pph*24:.2f} h, S/N {snr:.1f}')
inb=good&(np.abs(ph-c0)<w/2); ref=good&(np.abs(ph)<0.06)&~inb
# look-elsewhere: same box at 200 random phases outside |phase|<0.05 (after a model fitted with ALL phases, K=6)
A2=A; m2=np.ones(len(t),bool)
for _ in range(4):
    cc,*_=np.linalg.lstsq(A2[m2],f[m2],rcond=None); rr=f-A2@cc; ss=1.4826*np.median(np.abs(rr[m2])); m2=np.abs(rr)<4*ss
rng=np.random.default_rng(3); vals=[]
for c1 in rng.uniform(0.06,0.94,400):
    phc=((t-T1)/Pph-c1+0.5)%1-0.5; q=m2&(np.abs(phc)<w/2); qo=m2&(np.abs(phc)<0.06)&~q
    vals.append((np.mean(rr[qo])-np.mean(rr[q]))*1e3)
vals=np.array(vals); phc=ph; q=m2&(np.abs(ph-c0)<w/2); qo=m2&(np.abs(ph)<0.06)&~q; d0=(np.mean(rr[qo])-np.mean(rr[q]))*1e3
Pr(f'look-elsewhere (all-phase K=6 model, same box width at 400 random phases 0.06-0.94): depth at min I {d0:.3f} ppt; random-phase depths mean {vals.mean():+.3f}, std {vals.std():.3f} ppt -> empirical S/N {d0/vals.std():.1f}; fraction of random phases with depth >= min-I depth: {np.mean(vals>=d0):.4f}')
# per-sector and odd/even depths (masked-window model), with empirical error = std of same-width boxes at random phases in that subset
cyc=np.floor((t-T1)/Pph+0.5).astype(int)
def sub_depth(sel):
    q=sel&inb; qo=sel&ref
    if q.sum()<3: return None
    d=(np.mean(r[qo])-np.mean(r[q]))*1e3
    v=[]
    for c1 in rng.uniform(0.06,0.94,150):
        phc=((t-T1)/Pph-c1+0.5)%1-0.5; qq=sel&m2&(np.abs(phc)<w/2); qqo=sel&m2&(np.abs(phc)<0.06)&~qq
        if qq.sum()>2: v.append((np.mean(rr[qqo])-np.mean(rr[qq]))*1e3)
    return d,np.std(v),q.sum()
ps=[]
for s_ in sorted(set(sec.tolist())):
    x=sub_depth(good&(sec==s_))
    if x: ps.append((s_,)+x)
Pr('per-sector box depth (sector, ppt, empirical err, n in box): '+'; '.join(f's{a}: {b:.2f}+-{c:.2f} ({n})' for a,b,c,n in ps))
dd=np.array([p[1] for p in ps]); ee=np.array([p[2] for p in ps]); wm=np.sum(dd/ee**2)/np.sum(1/ee**2); ewm=1/np.sqrt(np.sum(1/ee**2))
Pr(f'  weighted mean {wm:.3f}+-{ewm:.3f} ppt; chi2 about mean {np.sum(((dd-wm)/ee)**2):.1f} for {len(dd)-1} dof; sectors positive {np.sum(dd>0)}/{len(dd)}')
for nm,sel in (('even cycles',good&(cyc%2==0)),('odd cycles',good&(cyc%2==1))):
    x=sub_depth(sel); Pr(f'  {nm}: {x[0]:.3f}+-{x[1]:.3f} ppt (n={x[2]})')
# same box at min II (phase 0.5+offset from s6) for a secondary eclipse
ph2=R6['summ']['ph2'][0]
phb=((t-T1)/Pph-ph2+0.5)%1-0.5; q=m2&(np.abs(phb)<w/2); qo=m2&(np.abs(phb)<0.06)&~q
Pr(f'same box at min II (phase {ph2:.4f}): depth {(np.mean(rr[qo])-np.mean(rr[q]))*1e3:.3f} ppt (empirical err ~{vals.std():.3f})')
json.dump(dict(best=best,d0=d0,lee_std=vals.std(),persector=ps),open(f'{VD}/s8_{tic}_b{int(binmin)}.json','w'),default=float,indent=1)
if len(sys.argv)>3:
    fig,ax=plt.subplots(1,2,figsize=(8,3.2))
    phf=((t-T1)/Pph)%1; fl=(f-A[:,:A.shape[1]-12]@c[:A.shape[1]-12])
    nb=200; b=np.floor(phf*nb).astype(int); mu=np.array([np.mean(fl[good&(b==i)]) for i in range(nb)])
    ax[0].plot((np.arange(nb)+0.5)/nb,(mu-np.median(mu))*1e3,'k.',ms=3); pp=np.linspace(0,1,1000); ax[0].plot(pp,(harm_model(pp,c[-12:])-np.median(harm_model(pp,c[-12:])))*1e3,'r-',lw=0.8)
    ax[0].set_xlabel('phase at P_phot (0 = min I)'); ax[0].set_ylabel('SAP flux, ppt'); ax[0].set_title(f'TIC {tic} fold, 0.005-phase bins',fontsize=8)
    pc=[p[0] for p in prof]; pv=[p[1] for p in prof]; pe=[p[2] for p in prof]
    ax[1].errorbar(pc,pv,pe,fmt='k.',ms=4); ax[1].axhline(0,color='0.5',lw=0.5); ax[1].axvspan(c0-w/2,c0+w/2,color='r',alpha=0.15)
    ax[1].set_xlabel('phase'); ax[1].set_ylabel('residual from K=6 (ppt)'); ax[1].set_title('residuals near min I (window masked in fit)',fontsize=8)
    plt.tight_layout(); plt.savefig(f'{VD}/dip_{tic}.png',dpi=100)
