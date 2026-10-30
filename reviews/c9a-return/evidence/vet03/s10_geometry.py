# Gaia SB1 geometry vs TESS eclipses: conjunction A (nu=90-omega: companion in front of the RV star)
# and B (nu=270-omega: RV star in front). MC with (a) independent errors, (b) Gaia corr_vec.
import numpy as np, csv, json
rows={r['source_id']:r for r in csv.DictReader(open('s10a_gaia_nss.csv'))}
obs={'70665829':dict(sid='3890379452571731456',T0=2576.73361,eT0=0.00015,P=3.4657658,eP=1.0e-6,phi2=0.46049,ephi2=0.00005,src='s4_period_70665829.out SPOC'),
     '331293467':dict(sid='5866907704116761728',T0=4066.68168,eT0=0.00032,P=5.2568187,eP=1.7e-6,phi2=0.5002,ephi2=0.0001,src='s4_period_331293467.out QLP + s5 secondary')}
names=['P','Vcm','K','e','w','Tp']   # SB1 parameter order in Gaia DR3 corr_vec (column-major upper triangle)
def corrmat(cv):
    C=np.eye(6); k=0
    for j in range(1,6):
        for i in range(j): C[i,j]=C[j,i]=cv[k]; k+=1
    return C
def tconj(nu_deg,e,w_deg,Tp,P):
    nu=np.radians(nu_deg); E=2*np.arctan2(np.sqrt(1-e)*np.sin(nu/2),np.sqrt(1+e)*np.cos(nu/2)); M=E-e*np.sin(E)
    return Tp+(M/(2*np.pi))%1*P
rng=np.random.default_rng(42); N=20000
out={}
for tic,o in obs.items():
    r=rows[o['sid']]; cv=[float(x) for x in r['corr_vec'].strip('{}').split(',')]
    mu=np.array([float(r['period']),float(r['center_of_mass_velocity']),float(r['semi_amplitude_primary']),float(r['eccentricity']),float(r['arg_periastron']),float(r['t_periastron'])+389.0])
    sig=np.array([float(r['period_error']),1.0,float(r['semi_amplitude_primary_error']),float(r['eccentricity_error']),float(r['arg_periastron_error']),float(r['t_periastron_error'])])
    C=corrmat(cv); ev=np.linalg.eigvalsh(C)
    print(f'=== TIC {tic} (Gaia {o["sid"]}); observed from {o["src"]}')
    print('  Gaia: P=%.6f+-%.6f e=%.4f+-%.4f w=%.1f+-%.1f Tp(BTJD)=%.4f+-%.4f K1=%.2f'%(mu[0],sig[0],mu[3],sig[3],mu[4],sig[4],mu[5],sig[5],mu[2]))
    print('  corr(w,Tp)=%.4f corr(P,Tp)=%.3f corr(e,w)=%.3f corr(e,Tp)=%.3f; corr-matrix min eigenvalue %.4f'%(C[4,5],C[0,5],C[3,4],C[3,5],ev.min()))
    print('  e cos w (Gaia, MC) and e sin w:')
    res={}
    def wrapc(x):  # wrap phases around their circular mean
        c=np.angle(np.mean(np.exp(2j*np.pi*x)))/(2*np.pi); return ((x-c+0.5)%1-0.5)+c
    Sig=C*np.outer(sig,sig)
    for mode in ['independent','correlated','corr|P=P_TESS']:
        if mode=='independent': X=mu+rng.standard_normal((N,6))*sig; Pprop=X[:,0]
        elif mode=='correlated': X=rng.multivariate_normal(mu,Sig,N,method='eigh'); Pprop=X[:,0]
        else:
            # condition Gaia's Gaussian on the period measured by TESS; propagate with TESS P
            iP=0; r_=[1,2,3,4,5]; dP=o['P']-mu[0]
            m_c=mu[r_]+Sig[r_,iP]/Sig[iP,iP]*dP; S_c=Sig[np.ix_(r_,r_)]-np.outer(Sig[r_,iP],Sig[iP,r_])/Sig[iP,iP]
            Y=rng.multivariate_normal(m_c,S_c,N,method='eigh'); X=np.column_stack([np.full(N,o['P']),Y])
            Pprop=o['P']+rng.standard_normal(N)*o['eP']
            print(f'  [conditioning] P_TESS-P_Gaia = {dP/sig[0]:+.2f} sigma_Gaia; conditional shifts: Tp {m_c[4]-mu[5]:+.4f} d, w {m_c[3]-mu[4]:+.2f} deg, e {m_c[2]-mu[3]:+.4f}')
        P,e,w,Tp=X[:,0],np.abs(X[:,3]),X[:,4],X[:,5]
        tA=tconj(90-w,e,w,Tp,P); tB=tconj(270-w,e,w,Tp,P)
        dphiAB=((tB-tA)/P)%1
        ecw=e*np.cos(np.radians(w)); esw=e*np.sin(np.radians(w))
        n=np.round((o['T0']-np.median(tA))/mu[0])
        pA=wrapc((o['T0']-(tA+n*Pprop))/o['P']); pB=wrapc((o['T0']-(tB+n*Pprop))/o['P'])
        mA,sA,mB,sB=np.median(pA),np.std(pA),np.median(pB),np.std(pB)
        print(f'  [{mode:13s}; {int(n)} cycles from Gaia Tp] observed deep eclipse minus conj A = {mA:+.4f} +- {sA:.4f} P ({mA/sA:+.2f} sig, {mA*o["P"]*24:+.1f} h); minus conj B = {mB:+.4f} +- {sB:.4f} P ({mB/sB:+.2f} sig)')
        q=np.percentile(dphiAB,[16,50,84]); sd=(q[2]-q[0])/2
        print(f'      predicted (tB-tA)/P = {q[1]:.4f} (+{q[2]-q[1]:.4f}/-{q[1]-q[0]:.4f}); e cos w = {np.median(ecw):+.4f} +- {np.std(ecw):.4f}; e sin w = {np.median(esw):+.4f} +- {np.std(esw):.4f}')
        print(f'      observed phi2={o["phi2"]:.5f}: if deep=A need {o["phi2"]:.4f} -> {(o["phi2"]-q[1])/sd:+.2f} sig; if deep=B need {1-o["phi2"]:.4f} -> {(1-o["phi2"]-q[1])/sd:+.2f} sig; fraction of draws with (tB-tA)/P<0.5: {np.mean(dphiAB<0.5):.3f}')
        res[mode]=dict(dA=mA,sA=sA,dB=mB,sB=sB,dphiAB=list(q))
    # exact e cos w from observed phase (i=90, solve with e sin w at Gaia value)
    from scipy.optimize import brentq
    esw0=mu[3]*np.sin(np.radians(mu[4]))
    def f(ecw):
        e=np.hypot(ecw,esw0); w=np.degrees(np.arctan2(esw0,ecw)); return ((tconj(270-w,e,w,0,1)-tconj(90-w,e,w,0,1))%1)-o['phi2']
    try: ex=brentq(f,-0.3,0.3); print(f'  exact e cos w implied by observed phi2 if deep=A (e sin w fixed at Gaia {esw0:+.4f}): {ex:+.5f}; first-order pi/2(phi2-0.5) = {np.pi/2*(o["phi2"]-0.5):+.5f}')
    except Exception as E_: print('  exact solve failed',E_)
    out[tic]=res
json.dump(out,open('s10_geometry.json','w'),indent=1,default=float)
