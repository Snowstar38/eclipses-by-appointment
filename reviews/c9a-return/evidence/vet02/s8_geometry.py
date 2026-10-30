# Geometry vs Gaia SB1 orbit. Monte Carlo (20000 draws) of (P, e, omega, Tp) with the Gaia corr_vec
# (parameter order assumed P, Vcm, K1, e, omega, Tp; tried column- and row-major and uncorrelated).
# Conjunction A: nu = 90 - omega (companion in front of the RV primary); B: nu = 270 - omega.
import numpy as np, pandas as pd
rng=np.random.default_rng(42)
g=pd.read_csv('gaia_nss_tap.csv')
OBS={ # TESS eclipse ephemeris from s6 (joint for 470235665; primaries for 379251709) and secondary phases
 2287291537931000064:dict(tic='470235665',P=10.326180,eP=0.000001,T0=1795.74251,eT0=0.00016,phs=0.52275,ephs=0.00002),
 519027491846682624:dict(tic='379251709',P=12.323912,eP=0.000007,T0=1961.25375,eT0=0.00060,phs=0.4960,ephs=0.0010),
}
def corrmat(cv,order):
    n=6; C=np.eye(n); k=0
    if order=='col':
        for j in range(1,n):
            for i in range(j): C[i,j]=C[j,i]=cv[k]; k+=1
    else:
        for i in range(n):
            for j in range(i+1,n): C[i,j]=C[j,i]=cv[k]; k+=1
    return C
def conj_time(Tp,P,e,w,nu_deg):
    nu=np.radians(nu_deg)
    E=2*np.arctan2(np.sqrt(1-e)*np.sin(nu/2),np.sqrt(1+e)*np.cos(nu/2))
    M=(E-e*np.sin(E))%(2*np.pi); return Tp+P*(M/(2*np.pi))
out=open('s8_geometry.txt','w')
def pr(*a):
    s=' '.join(str(x) for x in a); print(s); out.write(s+'\n')
for _,r in g.iterrows():
    o=OBS[r.source_id]; tic=o['tic']
    cv=np.array([float(x) for x in r.corr_vec.strip('{}').split(',')])
    mu=np.array([r.period,r.center_of_mass_velocity,r.semi_amplitude_primary,r.eccentricity,r.arg_periastron,r.t_periastron+389.0])
    sd=np.array([r.period_error,1.0,r.semi_amplitude_primary_error,r.eccentricity_error,r.arg_periastron_error,r.t_periastron_error])
    pr('='*8,'TIC',tic,'Gaia P=%.5f+-%.5f e=%.3f+-%.3f w=%.1f+-%.1f Tp(BTJD)=%.3f+-%.3f K1=%.2f+-%.2f'%(r.period,r.period_error,r.eccentricity,r.eccentricity_error,r.arg_periastron,r.arg_periastron_error,mu[5],r.t_periastron_error,r.semi_amplitude_primary,r.semi_amplitude_primary_error))
    C=corrmat(cv,'col'); pr('  corr (col-major) P-e %.2f P-w %.2f P-Tp %.2f e-w %.2f e-Tp %.2f w-Tp %.2f'%(C[0,3],C[0,4],C[0,5],C[3,4],C[3,5],C[4,5]))
    for order in ['col','row','none']:
        C=corrmat(cv,order) if order!='none' else np.eye(6)
        ev=np.linalg.eigvalsh(C)
        if ev.min()<=0: pr(f'  [{order}] correlation matrix not positive definite (min eig {ev.min():.3f}); skipped'); continue
        X=rng.multivariate_normal(mu,np.outer(sd,sd)*C,20000)
        P,e,w,Tp=X[:,0],np.abs(X[:,3]),X[:,4],X[:,5]
        tA=conj_time(Tp,P,e,w,90-w); tB=conj_time(Tp,P,e,w,270-w)
        dphB=((tB-tA)/P)%1
        # (a) forward: predict at the TESS epoch nearest T0 using Gaia P
        N=np.round((o['T0']-np.median(tA))/r.period)
        predA=tA+N*P; predB=tB+N*P
        # observed primary and secondary at that epoch
        oP=o['T0']; oS=o['T0']+o['phs']*o['P']
        def cmp(obs,pred):
            ph=(obs-pred)/o['P']; mu=np.angle(np.mean(np.exp(2j*np.pi*ph)))/(2*np.pi)  # circular mean
            d=((ph-mu+0.5)%1-0.5+mu)*o['P']      # unwrapped around the circular mean
            return np.median(d), np.std(d)
        aA=cmp(oP,predA); aB=cmp(oP,predB); sA=cmp(oS,predA); sB=cmp(oS,predB)
        # (b) backward: TESS ephemeris to the Gaia epoch, compared with Gaia conjunction (no P lever arm)
        Nb=np.round((np.median(tA)-o['T0'])/o['P']); tT=o['T0']+Nb*o['P']
        bA=cmp(tT,tA); bB=cmp(tT,tB)
        pr(f'  [{order}] predicted secondary phase (B-A)={np.median(dphB):.4f}+-{np.std(dphB):.4f} (16-84%: {np.percentile(dphB,16):.4f}-{np.percentile(dphB,84):.4f});  measured {o["phs"]:.4f}+-{o["ephs"]:.4f} -> {(o["phs"]-np.median(dphB))/np.hypot(np.std(dphB),o["ephs"]):+.2f} sigma; alt (primary=B): measured 1-phs={1-o["phs"]:.4f} -> {((1-o["phs"])-np.median(dphB))/np.hypot(np.std(dphB),o["ephs"]):+.2f} sigma')
        pr(f'    forward to TESS epoch N={int(N)} (BTJD {np.median(predA):.3f}): obs primary - conjA = {aA[0]:+.3f}+-{aA[1]:.3f} d ({aA[0]/aA[1]:+.2f} sig); obs primary - conjB = {aB[0]:+.3f}+-{aB[1]:.3f} d ({aB[0]/aB[1]:+.2f} sig)')
        pr(f'                               obs secondary - conjA = {sA[0]:+.3f}+-{sA[1]:.3f} d ({sA[0]/sA[1]:+.2f} sig); obs secondary - conjB = {sB[0]:+.3f}+-{sB[1]:.3f} d ({sB[0]/sB[1]:+.2f} sig)')
        pr(f'    backward to Gaia epoch (TESS P): obs primary - conjA = {bA[0]:+.3f}+-{bA[1]:.3f} d ({bA[0]/bA[1]:+.2f} sig); obs primary - conjB = {bB[0]:+.3f}+-{bB[1]:.3f} d ({bB[0]/bB[1]:+.2f} sig)')
        ecw=e*np.cos(np.radians(w)); esw=e*np.sin(np.radians(w))
        pr(f'    Gaia e cos w = {np.median(ecw):+.4f}+-{np.std(ecw):.4f}; e sin w = {np.median(esw):+.4f}+-{np.std(esw):.4f}')
    # TESS-implied e cos w from the secondary phase (exact for i=90: solve numerically on a grid)
    pr('  TESS-only e cos w (i=90, from secondary phase, small-e formula (pi/2)(phs-0.5)): %.4f'%((np.pi/2)*(o['phs']-0.5)))
    # duration-ratio e sin w (equal impact parameters assumed): (Tsec/Tpri-1)/(Tsec/Tpri+1)
out.close()
