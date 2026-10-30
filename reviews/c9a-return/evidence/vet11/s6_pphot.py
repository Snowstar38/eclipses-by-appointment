# Re-analysis at the photometric period P_phot (from s3 chi2 scan) to remove the phase-drift
# artefacts of the Gaia-P fold (s3 residual "dips" changed sign between early and late sectors).
# Measures: minima/maxima heights and depths with per-sector errors; minimum widths (K=6 vs K=2);
# Gaussian-dip search in K=2 residuals at both minima; box-dip search; times of minima vs Gaia conjunctions.
import sys, json, numpy as np
sys.path.insert(0,'[local path omitted]')
from common import *
tic=sys.argv[1]; T=targets()[tic]; VD='[local path omitted]'
R3=json.load(open(f'{VD}/s3_{tic}.json'))
P0=float(T['gaia_Per']); eP=float(T['gaia_e_Per']); Tp=float(T['gaia_tperi_btjd']); eTp=float(T['gaia_e_Tperi'])
e0=float(T['gaia_ecc']); ee=float(T['gaia_e_ecc']); w0=float(T['gaia_omega']); ew=float(T['gaia_e_omega'])
Pph,ePph=R3['Pphot']
out=open(f'{VD}/s6_{tic}.txt','w'); R={}
def Pr(*a):
    s=' '.join(str(x) for x in a); print(s); out.write(s+'\n')
t,f,seg,sec=load_qlp(tic,'SAP_FLUX'); tmed=np.median(t)
# reference epoch: deeper minimum of a K=6 fit at P_phot, placed near the TESS median epoch
F=fit(t,f,seg,Pph,tmed,6); mins,maxs,ph,y=extrema(F['harm'])
T1=tmed+mins[0][0]*Pph; T1=T1-np.round((T1-tmed)/Pph)*Pph
Pr(f'TIC {tic}: P_phot={Pph:.6f}+-{ePph:.6f} d (s3), P_Gaia={P0:.6f}+-{eP:.6f}; ratio P_phot/P_Gaia={Pph/P0:.6f}; reference T(min I)={T1:.4f} BTJD (near median epoch {tmed:.1f})')
def harm_stats(F):
    hc=F['harm']; K=len(hc)//2; cov=np.linalg.pinv(F['A'][F['mask']].T@F['A'][F['mask']])*F['sig']**2; hv=cov[F['npoly']:,F['npoly']:]
    res=[]
    for k in range(K):
        a,b=hc[2*k],hc[2*k+1]; A=np.hypot(a,b); g=np.array([a,b])/A; res.append((A*1e3,np.sqrt(g@hv[2*k:2*k+2,2*k:2*k+2]@g)*1e3,a*1e3,np.sqrt(hv[2*k,2*k])*1e3))
    return res
def shape(hc,n=4000):
    ph=np.arange(n)/n; y=harm_model(ph,hc)
    i1=np.argmin(np.where(np.abs(((ph+0.5)%1)-0.5)<0.25,y,9)); i2=np.argmin(np.where(np.abs(ph-0.5)<0.25,y,9))
    j1=np.argmax(np.where(np.abs(ph-0.25)<0.15,y,-9)); j2=np.argmax(np.where(np.abs(ph-0.75)<0.15,y,-9))
    mx=0.5*(y[j1]+y[j2]); d=[]
    for i in (i1,i2):
        half=y[i]+0.5*(mx-y[i]); k=i; 
        while y[k%n]<half: k+=1
        r=k; k=i
        while y[k%n]<half: k-=1
        d.append(((r-k)/n,mx-y[i]))
    return dict(ph1=ph[i1],ph2=ph[i2],phmax1=ph[j1],phmax2=ph[j2],max1=y[j1]*1e3,max2=y[j2]*1e3,min1=y[i1]*1e3,min2=y[i2]*1e3,
                depth1=d[0][1]*1e3,depth2=d[1][1]*1e3,fwhm1=d[0][0],fwhm2=d[1][0])
# global fits (t0 = T1 so phase 0 = min I)
for K in (2,4,6,8):
    F=fit(t,f,seg,Pph,T1,K); hs=harm_stats(F); S=shape(F['harm'])
    Pr(f'K={K}: sigma {F["sig"]*1e3:.2f} ppt, chi2={F["chi2"]:.0f}; A_k (ppt, err; cos-coefficient c_k, + = brighter at min I): '+'; '.join(f'A{k+1}={a:.3f}+-{ea:.3f} (c={c:+.3f})' for k,(a,ea,c,ec) in enumerate(hs)))
    Pr('    shape: '+', '.join(f'{k}={v:.4f}' for k,v in S.items()))
    R[f'K{K}']=dict(hs=hs,S=S,chi2=F['chi2'])
    if K==2: F2=F
    if K==6: F6=F
Pr('    (pure cos 2phi has FWHM 0.2500 per minimum; narrower = sharpened, wider = flattened)')
# per-sector at P_phot, K=6, fixed t0=T1
rows=[]
Pr('PER-SECTOR at P_phot, K=6: sector n | depth1 depth2 (ppt, from mean max) | ph1 ph2 | max1-max2 | fwhm1 fwhm2 | A1 A2 A3 A4')
for s in sorted(set(sec.tolist())):
    m=sec==s
    if m.sum()<200: continue
    Fs=fit(t[m],f[m],seg[m],Pph,T1,6); S=shape(Fs['harm']); hs=harm_stats(Fs)
    rows.append([s,S['depth1'],S['depth2'],(S['ph1']+0.5)%1-0.5,S['ph2'],S['max1']-S['max2'],S['fwhm1'],S['fwhm2']]+[h[0] for h in hs[:4]])
    Pr(f'  s{s} {m.sum()} | {S["depth1"]:.3f} {S["depth2"]:.3f} | {(S["ph1"]+0.5)%1-0.5:+.4f} {S["ph2"]:.4f} | {S["max1"]-S["max2"]:+.3f} | {S["fwhm1"]:.4f} {S["fwhm2"]:.4f} | '+' '.join(f'{h[0]:.3f}' for h in hs[:4]))
rows=np.array(rows); n=len(rows)
def ms(x): return x.mean(), x.std(ddof=1)/np.sqrt(len(x))
lab=['depth1','depth2','ph1','ph2','dmax','fwhm1','fwhm2','A1','A2','A3','A4']
summ={l:ms(rows[:,i+1]) for i,l in enumerate(lab)}
Pr(f'  MEAN+-SEM over {n} sectors: '+'; '.join(f'{l}={v[0]:.4f}+-{v[1]:.4f}' for l,v in summ.items()))
dd=rows[:,1]-rows[:,2]; Pr(f'  depth1-depth2 = {dd.mean():.3f}+-{dd.std(ddof=1)/np.sqrt(n):.3f} ppt ({dd.mean()/(dd.std(ddof=1)/np.sqrt(n)):.1f} sigma); min-min separation ph2-ph1 = {np.mean(rows[:,4]-rows[:,3]):.4f}+-{np.std(rows[:,4]-rows[:,3],ddof=1)/np.sqrt(n):.4f}')
R['sectors']=rows.tolist(); R['summ']=summ
# residual tests on K=2 residuals: Gaussian dip at each minimum (and at phase 0.25/0.75 as controls), widths 0.01..0.08
ph=((t-T1)/Pph)%1; r2=F2['resid']; m2=F2['mask']; r6=F6['resid']; m6=F6['mask']
def gdip(r,m,c,w):
    dph=((ph-c+0.5)%1)-0.5; g=-np.exp(-0.5*(dph/w)**2)
    A=np.vstack([g,np.ones_like(g)]).T[m]; cc,*_=np.linalg.lstsq(A,r[m],rcond=None); rr=r[m]-A@cc; s=1.4826*np.median(np.abs(rr))
    cov=np.linalg.inv(A.T@A)*s**2; return cc[0]*1e3,np.sqrt(cov[0,0])*1e3
Pr('GAUSSIAN-DIP fits to K=2 residuals (depth ppt +- white err; + = extra dip): centre phase / sigma width')
for c,nm in ((0.0,'minI'),(summ['ph2'][0],'minII'),(0.25,'ctrl0.25'),(0.75,'ctrl0.75')):
    Pr(f'  {nm:8s} c={c:.3f}: '+'; '.join('w={:.3f}: {:+.3f}+-{:.3f}'.format(w,*gdip(r2,m2,c,w)) for w in (0.01,0.02,0.04,0.08)))
# per-sector Gaussian dip (w=0.02) at the two minima on K=2 residuals
for c,nm in ((0.0,'minI'),(summ['ph2'][0],'minII')):
    v=[]
    for s in sorted(set(sec.tolist())):
        q=(sec==s)
        if q.sum()<200: continue
        dph=((ph-c+0.5)%1)-0.5; g=-np.exp(-0.5*(dph/0.02)**2); A=np.vstack([g,np.ones_like(g)]).T[q&m2]; cc,*_=np.linalg.lstsq(A,r2[q&m2],rcond=None); v.append(cc[0]*1e3)
    v=np.array(v); Pr(f'  per-sector w=0.02 dip at {nm}: {np.round(v,3).tolist()} -> {v.mean():.3f}+-{v.std(ddof=1)/np.sqrt(len(v)):.3f} ppt')
# box search on K=2 and K=6 residuals, 200 bins
for lb,r,m in (('K=2',r2,m2),('K=6',r6,m6)):
    nb=200; b=np.floor(ph*nb).astype(int)
    mu=np.array([np.mean(r[m&(b==i)]) for i in range(nb)]); se=np.array([np.std(r[m&(b==i)])/np.sqrt(max(1,np.sum(m&(b==i)))) for i in range(nb)])
    best=(0,0,0,0)
    for w in (1,2,3,4,6,8,12):
        for i in range(nb):
            idx=np.arange(i,i+w)%nb; dep=-np.mean(mu[idx]); er=np.sqrt(np.sum(se[idx]**2))/w
            if dep/er>best[0]: best=(dep/er,dep*1e3,(i+w/2)/nb%1,w/nb)
    ps=[]
    inw=(((ph-(best[2]-best[3]/2))%1)<best[3])
    for s_ in sorted(set(sec.tolist())):
        q=m&(sec==s_)
        if np.sum(q&inw)>3: ps.append(round(float(-np.mean(r[q&inw])*1e3),3))
    Pr(f'BOX on {lb} residuals (P_phot fold): binned rms {np.std(mu)*1e3:.3f} ppt vs median bin err {np.median(se)*1e3:.3f}; chi2/dof {np.sum((mu/se)**2)/nb:.2f}; strongest dip {best[1]:.3f} ppt at phase {best[2]:.3f} width {best[3]:.3f} ({best[0]:.1f} sigma white); per-sector depth there {ps}')
    R[f'box{lb}']=best
# times of minima vs Gaia conjunctions (MC, 20000 draws); conj A = primary at superior conjunction (companion in front)
rng=np.random.default_rng(2); N=20000
Pd=rng.normal(P0,eP,N); Tpd=rng.normal(Tp,eTp,N); ed=np.clip(rng.normal(e0,ee,N),0,0.95); wd=rng.normal(w0,ew,N)
tA,tB=conj_times(Pd,Tpd,ed,wd)
TII=T1+summ['ph2'][0]*Pph
for nm,Tm in (('min I',T1),('min II',TII)):
    for cn,tc in (('A',tA),('B',tB)):
        nn=np.round((Tm-tc)/Pd); tpred=tc+nn*Pd; d=((Tm-tpred)/P0+0.5)%1-0.5
        z=np.mean(np.exp(2j*np.pi*d)); mu_=np.angle(z)/(2*np.pi); sd=np.sqrt(-2*np.log(abs(z)))/(2*np.pi)
        Pr(f'{nm} (T={Tm:.4f}) minus predicted conj {cn}: {mu_:+.4f} +- {sd:.4f} phase  ({mu_/sd:+.1f} sigma); [min-time phase error from sector scatter: {summ["ph2" if nm=="min II" else "ph1"][1]:.4f}]')
        R[f'{nm}-{cn}']=(mu_,sd)
dB=((tB-tA)/Pd)%1; Pr(f'Gaia-predicted conj B - conj A phase: {np.median(dB):.4f}+-{np.std(dB):.4f}; observed min II - min I: {summ["ph2"][0]-summ["ph1"][0]:.4f}; e cos w (Gaia) = {e0*np.cos(np.radians(w0)):+.3f}; implied by photometry (approx (pi/2)(dphi-0.5)): {np.pi/2*(summ["ph2"][0]-summ["ph1"][0]-0.5):+.4f}')
json.dump(R,open(f'{VD}/s6_{tic}.json','w'),default=float,indent=1)
