# Conjunction test with the FULL Gaia covariance (corr_vec) instead of independent draws (s3/s6 MC ignored the
# strong omega-T_periastron correlation of low-e orbits). Param order for SB1 (DR3): period, Vcm, K1, e, omega, Tp;
# corr_vec = column-major upper triangle (last element = corr(omega,Tp), ~0.99 for low e, as observed).
import csv, json, re, numpy as np, sys
sys.path.insert(0,'[local path omitted]')
from common import conj_times
VD='[local path omitted]'
src={'372683900':'2194224406993202176','13106408':'2206975649496007936','372683622':'2194235436469405952','319185391':'2009695569526354048','62328710':'2165710668881281536'}
rows={r['source_id']:r for r in csv.DictReader(open(f'{VD}/s9_gaia_nss.csv')) if r['nss_solution_type']=='SB1'}
out=open(f'{VD}/s9b_conj_corr.txt','w')
def Pr(*a):
    s=' '.join(str(x) for x in a); print(s); out.write(s+'\n')
for tic,sid in src.items():
    r=rows[sid]; cv=np.array([float(x) for x in r['corr_vec'].strip('{}').split(',')])
    n=6; C=np.eye(n); k=0
    for j in range(1,n):
        for i in range(j): C[i,j]=C[j,i]=cv[k]; k+=1
    mu=np.array([float(r['period']),0,0,float(r['eccentricity']),float(r['arg_periastron']),float(r['t_periastron'])+389.0])
    sd=np.array([float(r['period_error']),1,1,float(r['eccentricity_error']),float(r['arg_periastron_error']),float(r['t_periastron_error'])])
    cov=C*np.outer(sd,sd); rng=np.random.default_rng(7)
    d=rng.multivariate_normal(mu,cov,40000,method='eigh')
    P,e,w,Tp=d[:,0],np.clip(d[:,3],0,0.95),d[:,4],d[:,5]
    tA,tB=conj_times(P,Tp,e,w)
    Pr(f'TIC {tic}: corr(omega,Tp)={C[4,5]:+.3f}, corr(e,omega)={C[3,4]:+.3f}, corr(P,Tp)={C[0,5]:+.3f}')
    try:
        s6=open(f'{VD}/s6_{tic}.txt').read()
    except FileNotFoundError:
        tA0=np.median(tA); Pr('   no orbital photometric signal; skipped'); continue
    T1=float(re.search(r'reference T\(min I\)=([0-9.]+)',s6).group(1)); R6=json.load(open(f'{VD}/s6_{tic}.json'))
    Pph=json.load(open(f'{VD}/s3_{tic}.json'))['Pphot'][0]; TII=T1+R6['summ']['ph2'][0]*Pph
    for nm,Tm in (('min I',T1),('min II',TII)):
        for cn,tc in (('A',tA),('B',tB)):
            nn=np.round((Tm-tc)/P); dd=((Tm-(tc+nn*P))/mu[0]+0.5)%1-0.5
            z=np.mean(np.exp(2j*np.pi*dd)); m_=np.angle(z)/(2*np.pi); s_=np.sqrt(-2*np.log(abs(z)))/(2*np.pi)
            Pr(f'   {nm} - conj {cn}: {m_:+.4f} +- {s_:.4f} phase ({m_/s_:+.1f} sigma)')
    dB=((tB-tA)/P)%1; Pr(f'   conj B - conj A: {np.median(dB):.4f} +- {np.std(dB):.4f}')
