# Per-star light-curve analysis at the Gaia period (QLP SAP, QUALITY==0, 10-min bins).
import sys, numpy as np, json
sys.path.insert(0,'[local path omitted]')
from common import *
from astropy.timeseries import LombScargle
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
tic=sys.argv[1]; T=targets()[tic]
P0=float(T['gaia_Per']); eP=float(T['gaia_e_Per']); Tp=float(T['gaia_tperi_btjd']); eTp=float(T['gaia_e_Tperi'])
e0=float(T['gaia_ecc']); ee=float(T['gaia_e_ecc']); w0=float(T['gaia_omega']); ew=float(T['gaia_e_omega'])
out=open(f's3_{tic}.txt','w'); R={}
def Pr(*a):
    s=' '.join(str(x) for x in a); print(s); out.write(s+'\n')
t,f,seg,sec=load_qlp(tic,'SAP_FLUX')
Pr(f'TIC {tic}: Gaia P={P0}+-{eP} Tp(BTJD)={Tp:.4f}+-{eTp} e={e0}+-{ee} w={w0}+-{ew}; N(10-min bins)={len(t)}; sectors={sorted(set(sec.tolist()))}; span {t.min():.1f}-{t.max():.1f}')
# ---- 1. MC Gaia conjunctions
rng=np.random.default_rng(1); N=20000
Pd=rng.normal(P0,eP,N); Tpd=rng.normal(Tp,eTp,N); ed=np.clip(rng.normal(e0,ee,N),0,0.95); wd=rng.normal(w0,ew,N)
tA,tB=conj_times(Pd,Tpd,ed,wd)
tA0=np.median(tA) if np.std(tA)<0.2*P0 else tA[0]
# robust circular reference
ang=2*np.pi*(tA-Tp)/P0; tA0=Tp+(np.angle(np.mean(np.exp(1j*ang)))/(2*np.pi)%1)*P0
dphB=((tB-tA)/Pd)%1
Pr(f'Gaia conj A ref epoch tA0={tA0:.4f} (BTJD, Gaia epoch); conj B - A phase = {np.median(dphB):.4f} +- {np.std(dphB):.4f} (circular would be 0.5)')
def pred_phase(tt):
    """predicted phase of conj A at time tt, in the fold (P0, tA0); returns mean, std (circular)"""
    n=np.round((tt-tA0)/P0); tpred=tA+n*Pd
    ph=((tpred-tA0)/P0+0.5)%1-0.5; z=np.mean(np.exp(2j*np.pi*ph))
    return np.angle(z)/(2*np.pi), np.sqrt(-2*np.log(abs(z)))/(2*np.pi)
tmed=np.median(t); pa,sa=pred_phase(tmed)
Pr(f'Predicted conj A phase at TESS median epoch {tmed:.1f}: {pa:+.4f} +- {sa:.4f}; conj B at {pa+np.median(dphB):+.4f}')
R['predA']=(pa,sa); R['dphB']=(float(np.median(dphB)),float(np.std(dphB)))
# ---- 2. periodograms
def simple_detrend(t,f,seg):
    A=poly_cols(t,seg,2); m=np.ones(len(t),bool)
    for _ in range(4):
        c,*_=np.linalg.lstsq(A[m],f[m],rcond=None); r=f-A@c; s=1.4826*np.median(np.abs(r[m])); m=np.abs(r)<5*s
    return r,m
for lab,col in [('SAP','SAP_FLUX'),('DET(KSPSAP/DET_FLUX)','DET')]:
    tt,ff,sg,_=(t,f,seg,sec) if col=='SAP_FLUX' else load_qlp(tic,'DET')
    r,m=simple_detrend(tt,ff,sg)
    fr=np.linspace(1/30.,10.,300000); pw=LombScargle(tt[m],r[m]).power(fr)
    # top peaks (local maxima separated)
    idx=np.argsort(pw)[::-1]; peaks=[]
    for i in idx:
        if all(abs(fr[i]-fr[j])>0.02 for j in peaks): peaks.append(i)
        if len(peaks)>=6: break
    Pr(f'LS {lab}: top peaks (P d, power, P/P_Gaia): '+'; '.join(f'{1/fr[i]:.5f} {pw[i]:.3f} {1/fr[i]/P0:.4f}' for i in peaks))
    if col=='SAP_FLUX': R['LS']=[(1/fr[i],pw[i]) for i in peaks]; PLS=1/fr[peaks[0]]
# ---- 3. chi2 period scan near Gaia P (and near the LS-implied period, if different)
def scan(Pc,K,width=0.004,nstep=None):
    span=t.max()-t.min(); df=1/span/40
    f0=1/Pc; fr=np.arange(f0*(1-width),f0*(1+width),df)
    ch=[]
    F0=fit(t,f,seg,Pc,tA0,K); mk=F0['mask']; s0=F0['sig']; Pp=poly_cols(t,seg,3)
    for ff_ in fr:
        A=np.hstack([Pp,harm_cols(t,1/ff_,tA0,K)])[mk]; c,*_=np.linalg.lstsq(A,f[mk],rcond=None)
        ch.append(np.sum(((f[mk]-A@c)/s0)**2))
    ch=np.array(ch); i=np.argmin(ch)
    # refine parabola
    if 0<i<len(ch)-1:
        y0,y1,y2=ch[i-1],ch[i],ch[i+1]; d=0.5*(y0-y2)/(y0-2*y1+y2); fb=fr[i]+d*df; curv=(y0-2*y1+y2)/df**2
        sf=np.sqrt(2/curv)
    else: fb=fr[i]; sf=np.nan
    # second-best local minimum (alias)
    loc=[j for j in range(1,len(ch)-1) if ch[j]<ch[j-1] and ch[j]<ch[j+1] and abs(fr[j]-fr[i])>2*df]
    j2=min(loc,key=lambda j:ch[j]) if loc else None
    alias=(1/fr[j2],ch[j2]-ch[i]) if j2 is not None else None
    return 1/fb, sf/fb**2, alias
Pbest,ePbest,al=scan(P0,6)
Pr(f'chi2 scan (K=6 harmonics, per-segment cubic) near Gaia P: P_phot={Pbest:.6f} +- {ePbest:.6f} d (formal, chi2 scaled to robust sigma); (P_phot-P_Gaia)/sqrt(err^2) = {(Pbest-P0)/np.hypot(ePbest,eP):+.2f} sigma; best alias {al[0]:.6f} d at dchi2={al[1]:.1f}' if al else f'P_phot={Pbest:.6f}+-{ePbest:.6f}')
R['Pphot']=(Pbest,ePbest)
if abs(PLS/P0-0.5)>0.02 and abs(PLS/P0-1)>0.02:
    Pl,ePl,al2=scan(PLS,4,width=0.004)
    Pr(f'chi2 scan near LS top peak {PLS:.5f}: P={Pl:.6f} +- {ePl:.6f}; ratio to Gaia P = {Pl/P0:.5f}; 1/ratio = {P0/Pl:.4f}')
    R['Pother']=(Pl,ePl)
# ---- 4. global fold fits at Gaia P (t0 = Gaia conj A, so prediction is phase 0 / dphB)
def describe(F,lab):
    hc=F['harm']; K=len(hc)//2
    cov=np.linalg.pinv(F['A'][F['mask']].T@F['A'][F['mask']])*F['sig']**2
    hcv=cov[F['npoly']:,F['npoly']:]
    amps=[]; 
    for k in range(K):
        a,b=hc[2*k],hc[2*k+1]; A=np.hypot(a,b); g=np.array([a,b])/A; eA=np.sqrt(g@hcv[2*k:2*k+2,2*k:2*k+2]@g)
        amps.append((A*1e3,eA*1e3,np.degrees(np.arctan2(b,a))))
    mins,maxs,ph,y=extrema(hc)
    return amps,mins,maxs,ph,y
def summ(mins,maxs,y):
    if len(mins)<2 or len(maxs)<2: return None
    m1,m2=mins[0],mins[1]; M1,M2=maxs[0],maxs[1]
    rng_=M1[1]-m1[1]
    # widths at 25% of full range above each minimum / below each maximum (half-cycle units)
    lev_lo=m1[1]+0.25*rng_; lev_hi=M1[1]-0.25*rng_
    return dict(min1_ph=m1[0],min1=(M1[1]-m1[1])*1e3,min2_ph=m2[0],min2=(M1[1]-m2[1])*1e3,dmin=(m2[1]-m1[1])*1e3,
                max1_ph=M1[0],max2_ph=M2[0],dmax=(M1[1]-M2[1])*1e3,ptp=rng_*1e3,
                frac_below=np.mean(y<lev_lo),frac_above=np.mean(y>lev_hi),nmin=len(mins))
for K in (2,6):
    F=fit(t,f,seg,P0,tA0,K); amps,mins,maxs,ph,y=describe(F,'')
    S=summ(mins,maxs,y)
    Pr(f'GLOBAL fold at Gaia P, K={K}: robust sigma {F["sig"]*1e3:.2f} ppt; harmonic amplitudes (ppt, err, phase deg): '+'; '.join(f'A{k+1}={a:.3f}+-{ea:.3f} ({p:.0f})' for k,(a,ea,p) in enumerate(amps)))
    if S: Pr('   extrema: '+', '.join(f'{k}={v:.4f}' if isinstance(v,float) else f'{k}={v}' for k,v in S.items()))
    else: Pr('   extrema: fewer than 2 minima', mins[:3], maxs[:3])
    R[f'glob{K}']=dict(amps=amps,S=S)
    if K==2: F2=F
    else: F6=F
# fold also at P_phot for comparison
Fp=fit(t,f,seg,Pbest,tA0,6); ampsp,minsp,maxsp,_,yp=describe(Fp,''); Sp=summ(minsp,maxsp,yp)
Pr('GLOBAL fold at P_phot, K=6: '+'; '.join(f'A{k+1}={a:.3f}+-{ea:.3f}' for k,(a,ea,p) in enumerate(ampsp[:4])))
if Sp: Pr('   extrema: '+', '.join(f'{k}={v:.4f}' if isinstance(v,float) else f'{k}={v}' for k,v in Sp.items()))
# ---- 5. per-sector fits at Gaia P
Pr('PER-SECTOR (P=Gaia, K=6, t0=Gaia conj A): sector, mid, n, min1(ppt) ph1, min2(ppt) ph2, dmin(ppt), dmax(ppt), dmin/ptp, predA(ph+-), A1,A2,A3,A4 ppt')
rows=[]
for s in sorted(set(sec.tolist())):
    m=sec==s
    if m.sum()<200: continue
    F=fit(t[m],f[m],seg[m],P0,tA0,6); amps,mins,maxs,ph,y=describe(F,''); S=summ(mins,maxs,y)
    if not S: Pr(f'  s{s}: <2 minima'); continue
    pa_s,sa_s=pred_phase(np.median(t[m]))
    rows.append([s,np.median(t[m]),S['min1'],S['min1_ph'],S['min2'],S['min2_ph'],S['dmin'],S['dmax'],S['dmin']/S['ptp']]+[a[0] for a in amps[:4]])
    Pr(f'  s{s} {np.median(t[m]):.1f} {m.sum()} {S["min1"]:.3f} {S["min1_ph"]:.4f} {S["min2"]:.3f} {S["min2_ph"]:.4f} {S["dmin"]:.3f} {S["dmax"]:.3f} {S["dmin"]/S["ptp"]:.4f} pred {pa_s:+.3f}+-{sa_s:.3f} | '+' '.join(f'{a[0]:.3f}' for a in amps[:4]))
rows=np.array(rows)
if len(rows)>1:
    n=len(rows)
    def ms(x): return np.mean(x),np.std(x,ddof=1)/np.sqrt(n)
    # circular mean of min phases (wrap)
    def cph(x):
        z=np.exp(2j*np.pi*x); mz=np.mean(z); return (np.angle(mz)/(2*np.pi))%1, np.std(((x-np.angle(mz)/(2*np.pi))+0.5)%1-0.5,ddof=1)/np.sqrt(n)
    Pr(f'  MEAN over {n} sectors: min1={ms(rows[:,2])[0]:.3f}+-{ms(rows[:,2])[1]:.3f} ppt at phase {cph(rows[:,3])[0]:.4f}+-{cph(rows[:,3])[1]:.4f}; min2={ms(rows[:,4])[0]:.3f}+-{ms(rows[:,4])[1]:.3f} at {cph(rows[:,5])[0]:.4f}+-{cph(rows[:,5])[1]:.4f}; dmin={ms(rows[:,6])[0]:.3f}+-{ms(rows[:,6])[1]:.3f} ppt ({ms(rows[:,6])[0]/ms(rows[:,6])[1]:.1f} sigma); dmax={ms(rows[:,7])[0]:.3f}+-{ms(rows[:,7])[1]:.3f}; dmin/ptp={ms(rows[:,8])[0]:.4f}+-{ms(rows[:,8])[1]:.4f}')
    # min1 is defined per sector as deeper -> biased positive; also signed difference at fixed phases:
    R['sectors']=rows.tolist()
# signed odd/even test without selection bias: depth at phase of global min1 vs global min2 per sector
S6=R['glob6']['S']
if S6:
    ph1,ph2=S6['min1_ph'],S6['min2_ph']; d=[]
    for s in sorted(set(sec.tolist())):
        m=sec==s
        if m.sum()<200: continue
        F=fit(t[m],f[m],seg[m],P0,tA0,6); hc=F['harm']
        d.append((harm_model(np.array([ph2]),hc)[0]-harm_model(np.array([ph1]),hc)[0])*1e3)
    d=np.array(d); Pr(f'  SIGNED min2-min1 flux at fixed global phases {ph1:.3f}/{ph2:.3f}: per-sector {np.round(d,3).tolist()} -> {d.mean():.3f} +- {d.std(ddof=1)/np.sqrt(len(d)):.3f} ppt ({d.mean()/(d.std(ddof=1)/np.sqrt(len(d))):.1f} sigma); sectors with min2 shallower: {np.sum(d>0)}/{len(d)}')
    R['signed_dmin']=(d.mean(),d.std(ddof=1)/np.sqrt(len(d)))
# ---- 6. residual dip search (K=2 and K=6 residuals at Gaia P)
for lab,F in (('K=2',F2),('K=6',F6)):
    m=F['mask']; ph=((t-tA0)/P0)%1; r=f-F['poly']-harm_model(ph,F['harm'])
    nb=200; b=np.floor(ph*nb).astype(int)
    mu=np.array([np.mean(r[m&(b==i)]) for i in range(nb)]); se=np.array([np.std(r[m&(b==i)])/np.sqrt(max(1,np.sum(m&(b==i)))) for i in range(nb)])
    best=(0,0,0,0)
    for w in (1,2,3,4,6,8,12):
        for i in range(nb):
            idx=np.arange(i,i+w)%nb; dep=-np.mean(mu[idx]); er=np.sqrt(np.sum(se[idx]**2))/w
            if dep/er>best[0]: best=(dep/er,dep*1e3,(i+w/2)/nb%1,w/nb)
    chi2b=np.sum((mu/se)**2)
    # per-sector depth of the strongest box (same phase window)
    lo_=best[2]-best[3]/2; hi_=best[2]+best[3]/2
    inw=(((ph-lo_)%1)<best[3]); ps=[]
    for s_ in sorted(set(sec.tolist())):
        q=m&(sec==s_); 
        if np.sum(q&inw)>3: ps.append((s_,round(-np.mean(r[q&inw])*1e3,3),round(np.std(r[q&inw])/np.sqrt(np.sum(q&inw))*1e3,3)))
    Pr(f'   per-sector depth in that window (sector, ppt, err): {ps}')
    Pr(f'RESIDUAL ({lab}) binned 200: rms {np.std(mu)*1e3:.3f} ppt, median bin err {np.median(se)*1e3:.3f} ppt, chi2/dof={chi2b/nb:.2f}; strongest box dip {best[1]:.3f} ppt at phase {best[2]:.3f}, width {best[3]:.3f} phase, {best[0]:.1f} sigma (white-noise, bin errors)')
    R[f'resid{lab}']=best
# DET shape check
td,fd,sgd,_=load_qlp(tic,'DET'); Fd=fit(td,fd,sgd,P0,tA0,6,order=1); _,minsd,maxsd,_,yd=describe(Fd,''); Sd=summ(minsd,maxsd,yd)
if Sd: Pr('DET (KSPSAP/DET_FLUX) fold at Gaia P, K=6: min1={min1:.3f} ppt at {min1_ph:.4f}, min2={min2:.3f} at {min2_ph:.4f}, dmin={dmin:.3f}, dmax={dmax:.3f}'.format(**Sd))
# ---- plot
ph=((t-tA0)/P0)%1; m=F6['mask']; fl=f-F6['poly']+1
nb=100; b=np.floor(ph*nb).astype(int); mu=np.array([np.mean(fl[m&(b==i)]) for i in range(nb)])
fig,ax=plt.subplots(2,1,figsize=(6,4.5),sharex=True,gridspec_kw={'height_ratios':[3,1]})
ax[0].plot(ph[m],(fl[m]-1)*1e3,',',color='0.7'); ax[0].plot((np.arange(nb)+0.5)/nb,(mu-1)*1e3,'k.',ms=4)
pp=np.linspace(0,1,500); ax[0].plot(pp,harm_model(pp,F6['harm'])*1e3,'r-',lw=1,label='K=6'); ax[0].plot(pp,harm_model(pp,F2['harm'])*1e3,'b--',lw=1,label='K=2')
for x,c in ((pa,'g'),((pa+R['dphB'][0])%1,'m')): ax[0].axvline(x%1,color=c,lw=0.8)
lo,hi=np.percentile((fl[m]-1)*1e3,[0.5,99.5]); ax[0].set_ylim(lo,hi); ax[0].set_ylabel('SAP rel. flux (ppt)'); ax[0].legend(fontsize=7)
ax[0].set_title(f'TIC {tic} fold at Gaia P={P0:.5f} d (green=conj A, magenta=conj B)',fontsize=8)
r2=fl-1-harm_model(ph,F2['harm']); mu2=np.array([np.mean(r2[m&(b==i)]) for i in range(nb)])
r6=fl-1-harm_model(ph,F6['harm']); mu6=np.array([np.mean(r6[m&(b==i)]) for i in range(nb)])
ax[1].plot((np.arange(nb)+0.5)/nb,mu2*1e3,'b.',ms=3,label='resid K=2'); ax[1].plot((np.arange(nb)+0.5)/nb,mu6*1e3,'r.',ms=3,label='resid K=6'); ax[1].axhline(0,color='k',lw=0.5)
ax[1].set_xlabel('phase (0 = Gaia conj A, Gaia epoch)'); ax[1].set_ylabel('ppt'); ax[1].legend(fontsize=6)
plt.tight_layout(); plt.savefig(f'fold_{tic}.png',dpi=110)
json.dump(R,open(f's3_{tic}.json','w'),default=float,indent=1)
