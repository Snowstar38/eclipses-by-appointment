# Gaia SB1 orbit -> predicted conjunction phases (A: nu=90-omega, companion in front of RV star; B: nu=270-omega),
# secondary phase B-A, with Monte Carlo (20000 draws) using the corvec (column-major upper triangle,
# order P, Vcm, K1, e, omega, Tp; checked for positive-definiteness) and uncorrelated draws for comparison.
import numpy as np, sys
rng=np.random.default_rng(42)
def E_of_M(M,e):
    E=M.copy()
    for _ in range(60): E=E-(E-e*np.sin(E)-M)/(1-e*np.cos(E))
    return E
def M_of_nu(nu,e):
    E=2*np.arctan2(np.sqrt(1-e)*np.sin(nu/2),np.sqrt(1+e)*np.cos(nu/2))
    return np.mod(E-e*np.sin(E),2*np.pi)
G={ # P,eP,Tp(BTJD),eTp,e,ee,w,ew,K1,eK1,Vcm,eVcm, corvec
'468827621':(11.04137773281629364,1.9555840e-03,4.894630993382568+389.0,0.0999704500,0.3554870641615797688,0.0238574390,350.128119749201,3.86920360,42.03433587695695905,0.713511100,-56.858,0.8167,
 [1.8433902e-01,1.8961528e-01,-5.6626443e-03,-1.7428014e-01,-7.1983665e-01,6.307422e-02,-6.4187255e-03,-3.4488810e-01,-2.5343972e-01,3.5665860e-01,1.6692448e-02,-5.2076167e-01,-3.2164046e-01,4.9390838e-01,9.089153e-01]),
'416285595':(4.61556532062107561,5.5868560e-04,1.816657647671532+389.0,0.4645553800,0.0778609211601530987,0.0438552870,104.180565040703,36.30308500,46.42402829378382734,2.433333900,-9.4976,1.3515,
 [1.5332453e-01,-1.8934159e-01,-2.6794526e-01,-1.8369476e-01,-3.2158917e-01,2.447659e-01,-2.1312721e-01,-2.7020904e-01,6.1535794e-01,2.5828350e-01,-2.4208560e-01,-2.7457958e-01,6.1106770e-01,2.8173956e-01,9.976720e-01]),
}
def corrmat(cv,n=6):
    C=np.eye(n); k=0
    for j in range(1,n):
        for i in range(j):
            C[i,j]=C[j,i]=cv[k]; k+=1
    return C
def draws(tic,N=20000,corr=True):
    P,eP,Tp,eTp,e,ee,w,ew,K,eK,V,eV,cv=G[tic]
    mu=np.array([P,V,K,e,w,Tp]); sd=np.array([eP,eV,eK,ee,ew,eTp])
    C=corrmat(cv) if corr else np.eye(6)
    X=rng.multivariate_normal(mu,C*np.outer(sd,sd),N)
    X[:,3]=np.clip(X[:,3],0,0.95)
    return X
def conj(X):
    P,V,K,e,w,Tp=X.T
    wr=np.radians(w)
    MA=M_of_nu(np.pi/2-wr,e); MB=M_of_nu(3*np.pi/2-wr,e)
    tA=Tp+MA/(2*np.pi)*P; tB=Tp+MB/(2*np.pi)*P
    return tA,tB,np.mod((tB-tA)/P,1)
if __name__=='__main__':
    for tic in G:
        P,eP,Tp,eTp,e,ee,w,ew,K,eK,V,eV,cv=G[tic]
        C=corrmat(cv); ev=np.linalg.eigvalsh(C)
        print(f'== {tic}: corr matrix min eigenvalue {ev.min():.4f} (posdef={ev.min()>0}); corr(w,Tp)={C[4,5]:.3f} corr(e,w)={C[3,4]:.3f}')
        nom=conj(np.array([[P,V,K,e,w,Tp]]))
        print(f'  nominal: e cos w={e*np.cos(np.radians(w)):+.4f} e sin w={e*np.sin(np.radians(w)):+.4f}; tA={nom[0][0]:.4f} tB={nom[1][0]:.4f} BTJD (Gaia epoch); phase(B-A)={nom[2][0]:.4f}')
        for corr in [True,False]:
            X=draws(tic,corr=corr); tA,tB,ph=conj(X)
            print(f'  MC corr={corr}: phase(B-A)={np.median(ph):.4f} +- {np.std(ph):.4f} [16-84%: {np.percentile(ph,16):.4f}-{np.percentile(ph,84):.4f}]; tA sd={np.std(tA):.4f} d, tB sd={np.std(tB):.4f} d; ecosw={np.mean(X[:,3]*np.cos(np.radians(X[:,4]))):+.4f}+-{np.std(X[:,3]*np.cos(np.radians(X[:,4]))):.4f}')
