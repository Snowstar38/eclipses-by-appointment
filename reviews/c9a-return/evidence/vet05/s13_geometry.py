# Eclipse geometry vs Gaia DR3 SB1 orbit, Monte Carlo (20000 draws) with the NSS correlation matrix.
# corr_vec = upper triangle of the 6x6 correlation matrix stored column by column (checked: rows 5 and 6 then have
# near-identical correlations with params 1-4 and c56=+0.9996, i.e. the omega/T_peri degeneracy of a near-circular orbit).
# The order of params 1-4 (P, Vcm, K1, e in some order) is not certain, so every assignment is run and the spread is reported.
import numpy as np, json, csv, itertools
NS={r['source_id']:r for r in csv.DictReader(open('s9_gaia_nss.csv'))}
C=json.load(open('s12_compile.json'))
stars={'15855794':'53541096672533120','92881948':'2964506347485091072'}
def corrmat(vec,n=6):
    R=np.eye(n); k=0
    for j in range(1,n):
        for i in range(j):
            R[i,j]=R[j,i]=vec[k]; k+=1
    return R
def kep_M(nu,e):
    E=2*np.arctan2(np.sqrt(1-e)*np.sin(nu/2),np.sqrt(1+e)*np.cos(nu/2))
    return E-e*np.sin(E)
def wrap(x,P): return (x+P/2)%P-P/2
def cstat(d,P):
    # circular mean of a time offset (period P), robust sigma = half the 16-84% range about that mean, and 2.3/97.7% bounds
    ph=d/P; mu=np.angle(np.mean(np.exp(2j*np.pi*ph)))/(2*np.pi)
    c=wrap(ph-mu,1.0); p=np.percentile(c,[2.3,16,50,84,97.7])
    m=mu+p[2]
    return m*P,(p[3]-p[1])/2*P,(mu+p[0])*P,(mu+p[4])*P
out={}
rng=np.random.default_rng(42)
N=20000
for tic,sid in stars.items():
    r=NS[sid]
    val={'P':float(r['period']),'Vcm':float(r['center_of_mass_velocity']),'K':float(r['semi_amplitude_primary']),
         'e':float(r['eccentricity']),'w':float(r['arg_periastron']),'Tp':float(r['t_periastron'])+389.0}
    err={'P':float(r['period_error']),'Vcm':0.0,'K':float(r['semi_amplitude_primary_error']),
         'e':float(r['eccentricity_error']),'w':float(r['arg_periastron_error']),'Tp':float(r['t_periastron_error'])}
    err['Vcm']=1.0  # value irrelevant to geometry
    R=corrmat([float(x) for x in r['corr_vec'].strip('{}').split(',')])
    print('# offsets: circular mean over draws; sd = half the 16-84% range about it (the distribution has long wrapped tails)')
    print('='*10,tic,'Gaia: P=%.6f±%.6f Tp(BTJD)=%.4f±%.4f e=%.4f±%.4f w=%.2f±%.2f K1=%.2f±%.2f'%(val['P'],err['P'],val['Tp'],err['Tp'],val['e'],err['e'],val['w'],err['w'],val['K'],err['K']))
    print('   eigenvalues of corr matrix:',np.round(np.linalg.eigvalsh(R),5))
    J=C[f'{tic}_ephem_joint']; Tref,eTref,Pe,ePe,phS,ephS=J['Tref'],J['eTref'],J['P'],J['eP'],J['phaseS'],J['ephaseS']
    nb=round((Tref-val['Tp'])/Pe); TobsG=Tref-nb*Pe; eTobsG=np.hypot(eTref,nb*ePe)
    print(f'   observed primary: Tref={Tref:.5f}±{eTref:.5f}, P_ecl={Pe:.7f}±{ePe:.7f}; propagated back {nb} cycles to {TobsG:.4f}±{eTobsG:.4f} (Gaia epoch)')
    results=[]
    orders=[('uncorrelated',None)]+[(','.join(p)+',w,Tp',list(p)+['w','Tp']) for p in itertools.permutations(['P','Vcm','K','e'])]
    for lab,order in orders:
        names=order if order else ['P','Vcm','K','e','w','Tp']
        sd=np.array([err[n] for n in names]); mu=np.array([val[n] for n in names])
        cov=(R if order else np.eye(6))*np.outer(sd,sd)
        X=rng.multivariate_normal(mu,cov,N); d={n:X[:,i] for i,n in enumerate(names)}
        e=d['e']; w=np.radians(d['w']); neg=e<0; e=np.abs(e); w=np.where(neg,w+np.pi,w)   # e<0 draws reflected: e->|e|, w->w+180, Tp->Tp+P/2 (same orbit)
        P=d['P']; Tp=d['Tp']+np.where(neg,d['P']/2,0.0)
        TA=Tp+P*kep_M(np.pi/2-w,e)/(2*np.pi); TB=Tp+P*kep_M(3*np.pi/2-w,e)/(2*np.pi)
        TobsGd=TobsG+rng.normal(0,eTobsG,N)
        dA=wrap(TobsGd-TA,P); dB=wrap(TobsGd-TB,P)
        # forward: Gaia ephemeris carried to TESS with Gaia P
        nA=np.round((Tref-TA)/P); dAf=wrap(Tref-(TA+nA*P),P); nB=np.round((Tref-TB)/P); dBf=wrap(Tref-(TB+nB*P),P)
        phpred=((TB-TA)/P)%1
        ecw=e*np.cos(w)
        A=cstat(dA,val['P']); B=cstat(dB,val['P']); Af=cstat(dAf,val['P']); Bf=cstat(dBf,val['P'])
        res=dict(order=lab,dA_med=A[0],dA_sd=A[1],dA_p16=A[2],dA_p84=A[3],
                 dB_med=B[0],dB_sd=B[1],dAf_med=Af[0],dAf_sd=Af[1],dBf_med=Bf[0],dBf_sd=Bf[1],fracA_within_0p25d=float(np.mean(np.abs(dA)<0.25)),
                 ph_med=np.median(phpred),ph_sd=np.std(phpred),ph_p2=np.percentile(phpred,2.3),ph_p98=np.percentile(phpred,97.7),
                 ecw_med=np.median(ecw),ecw_sd=np.std(ecw),frac_ph_beyond_obs=float(np.mean(np.abs(phpred-0.5)>=abs(phS-0.5))))
        results.append(res)
    for rr in results[:2]:
        print(f"   [{rr['order']}] Gaia-epoch: obs - conjA = {rr['dA_med']:+.4f} d (robust sd {rr['dA_sd']:.4f}; 95% {rr['dA_p16']:+.4f}..{rr['dA_p84']:+.4f}; {100*rr['fracA_within_0p25d']:.0f}% of draws within 0.25 d) = {rr['dA_med']/rr['dA_sd']:+.2f} sigma; obs - conjB = {rr['dB_med']:+.4f} (sd {rr['dB_sd']:.4f}) = {rr['dB_med']/rr['dB_sd']:+.2f} sigma")
        print(f"        forward to TESS with Gaia P: obs - conjA = {rr['dAf_med']:+.4f} d (sd {rr['dAf_sd']:.4f}) = {rr['dAf_med']/rr['dAf_sd']:+.2f} sigma (phase {rr['dAf_med']/val['P']:+.4f}±{rr['dAf_sd']/val['P']:.4f}); obs - conjB = {rr['dBf_med']:+.4f} (sd {rr['dBf_sd']:.4f})")
        print(f"        predicted secondary phase (B-A) = {rr['ph_med']:.4f} ± {rr['ph_sd']:.4f} (95%: {rr['ph_p2']:.4f}..{rr['ph_p98']:.4f}); Gaia e cos w = {rr['ecw_med']:+.4f} ± {rr['ecw_sd']:.4f}; fraction of draws with |phase-0.5| >= observed: {rr['frac_ph_beyond_obs']:.3f}")
    cor=results[1:]
    rngA=[x['dA_med']/x['dA_sd'] for x in cor]; sdA=[x['dA_sd'] for x in cor]
    print(f"   over all 24 assignments of params 1-4: Gaia-epoch obs-conjA sd {min(sdA):.4f}..{max(sdA):.4f} d, offset {min(rngA):+.2f}..{max(rngA):+.2f} sigma; obs-conjB {min(x['dB_med']/x['dB_sd'] for x in cor):+.2f}..{max(x['dB_med']/x['dB_sd'] for x in cor):+.2f} sigma; forward obs-conjA {min(x['dAf_med']/x['dAf_sd'] for x in cor):+.2f}..{max(x['dAf_med']/x['dAf_sd'] for x in cor):+.2f} sigma; pred sec phase {min(x['ph_med'] for x in cor):.4f}..{max(x['ph_med'] for x in cor):.4f} (sd {min(x['ph_sd'] for x in cor):.4f}..{max(x['ph_sd'] for x in cor):.4f})")
    ecw_obs=np.pi/2*(phS-0.5); eecw=np.pi/2*ephS
    print(f'   observed secondary phase {phS:.5f}±{ephS:.5f} -> e cos w ~ (pi/2)(phi-0.5) = {ecw_obs:+.5f}±{eecw:.5f}  (first order, sin i ~ 1)')
    out[tic]=dict(gaia=val,gaia_err=err,TobsG=TobsG,eTobsG=eTobsG,n_back=nb,results=results,ecosw_obs=ecw_obs,eecosw_obs=eecw)
json.dump(out,open('s13_geometry.json','w'),indent=1,default=float)
