"""Own Gaia covariance, fixed-shape secondary gates, and RV physics.
Phase scan is diagnostic only. Tests at Gaia-predicted conjunction are fixed
before examining flux; controls at other phases calibrate excess scatter.
"""
import csv,json,math
import numpy as np
from pathlib import Path
import fit_batch as f
ROOT=Path(__file__).parent
GROOT=ROOT.parents[1]/'shared-full-review'
gaia=list(csv.DictReader(open(GROOT/'gaia-nss-ari.csv')))
def conj(P,e,w,tp,kind):
    nu=(np.pi/2 if kind=='A' else 3*np.pi/2)-w
    E=2*np.arctan2(np.sqrt(1-e)*np.sin(nu/2),np.sqrt(1+e)*np.cos(nu/2))
    return tp+((E-e*np.sin(E))%(2*np.pi))/(2*np.pi)*P
def covariance(n):
    # ESA DR3 datamodel SB1: bit_index=127, six parameters ordered
    # P,gamma,K1,e,omega,Tp. Corr vector is strict lower triangle row-wise.
    # https://gea.esac.esa.int/archive/documentation/GDR3/Gaia_archive/chap_datamodel/sec_dm_non--single_stars_tables/ssec_dm_nss_two_body_orbit.html
    assert n['nss_solution_type']=='SB1' and int(n['bit_index'])==127
    vals=[float(x) for x in n['corr_vec'].strip('{}[]()').split(',')]
    assert len(vals)==15, 'Unexpected SB1 correlation vector layout'
    C=np.eye(6);k=0
    for i in range(1,6):
      for j in range(i):C[i,j]=C[j,i]=vals[k];k+=1
    ix=[0,3,4,5];err=np.array([float(n[x]) for x in ['period_error','eccentricity_error','arg_periastron_error','t_periastron_error']]);err[2]*=np.pi/180
    mean=np.array([float(n['period']),float(n['eccentricity']),float(n['arg_periastron'])*np.pi/180,float(n['t_periastron'])+389])
    cov=C[np.ix_(ix,ix)]*np.outer(err,err)
    eig=np.linalg.eigvalsh(cov)
    if eig.min()<-1e-7:raise ValueError('invalid covariance')
    draw=np.random.default_rng(473).multivariate_normal(mean,cov,20000)
    return mean,draw[(draw[:,1]>=0)&(draw[:,1]<1)],C[4,5],int(n['bit_index'])
def combine(rows):
    a=[x for x in rows if x['status']=='fit']; d=np.array([x['depth'] for x in a]);e=np.array([x['depth_error'] for x in a]);w=1/e**2
    if not len(a):return dict(n=0)
    mu=float(sum(w*d)/sum(w));err=float(1/np.sqrt(sum(w)))
    return dict(n=len(a),depth=mu,error=err,snr=mu/err,scatter=float(np.std(d)),chi2=float(sum(w*(d-mu)**2)),dof=len(a)-1)
for tic,tg in f.targets.items():
    dest=ROOT/tic;raw=json.load(open(dest/'fit-results.json'));eph=raw['ephemeris'];sh=raw['shape'];secs=f.read(tic);f.P=eph['P']
    ns=[x for x in gaia if x['source_id']==tg['gaia']['source_id'] and x['nss_solution_type']=='SB1'];assert len(ns)==1
    n=ns[0];json.dump(n,open(dest/'gaia-nss.json','w'),indent=2);mu,dr,corr,bit=covariance(n)
    offsets={};res=[]
    for which in ['A','B']:
        nominal=conj(*mu,which);draw=conj(*dr.T,which);draw-=dr[:,0]*np.round((draw-nominal)/dr[:,0])
        predicted=nominal+mu[0]*round((eph['Tref']-nominal)/mu[0]);delta=(eph['Tref']-predicted+mu[0]/2)%mu[0]-mu[0]/2
        offsets[which]=float(delta);observations=[]
        for ev in raw['events']:
            if ev['status']!='fit':continue
            epoch=round((ev['tc']-nominal)/mu[0]);dd=draw+epoch*dr[:,0];center=float(np.median(dd));err=float(np.std(dd));dt=float((ev['tc']-center+mu[0]/2)%mu[0]-mu[0]/2)
            observations.append(dict(sec=ev['sec'],tc=ev['tc'],gaia_conjunction=center,gaia_error=err,offset_days=dt,z=dt/np.hypot(err,ev['tc_error'])))
        epoch=round((389-eph['T0'])/eph['P']);tphot=eph['T0']+epoch*eph['P'];ge=round((tphot-nominal)/mu[0]);pred=draw+ge*dr[:,0];dt=float((tphot-np.median(pred)+mu[0]/2)%mu[0]-mu[0]/2)
        res.append(dict(kind=which,epoch389_offset=dt,epoch389_gaia_error=float(np.std(pred)),events=observations))
    primary=min(offsets,key=lambda x:abs(offsets[x]));other='B' if primary=='A' else 'A'
    phase=float(((conj(*mu,other)-conj(*mu,primary))/mu[0])%1)
    # Translate Gaia's relative conjunction to the precisely measured primary.
    control=[];allrows={}
    phases=list(np.arange(.1,.951,.05))+[phase]
    for ph in phases:
      rows=[]
      for s in secs:
        lo=int(np.ceil((s['t'].min()-eph['T0'])/eph['P']-ph));hi=int(np.floor((s['t'].max()-eph['T0'])/eph['P']-ph))
        for cyc in range(lo,hi+1):
            r=f.event(s,eph['T0']+(cyc+ph)*eph['P'],sh['T14'],sh['fr'],scan=False);r['cycle']=cyc;rows.append(r)
      stat=combine(rows);stat['phase']=float(ph);control.append(stat)
      if ph==phase:allrows['gaia_other_windows']=rows;secondary=stat
    # Conservative fixed-phase upper limit includes empirical control scatter.
    clean=[x for x in control[:-1] if x.get('n',0) and abs(x['phase']-phase)>.1]
    noise=max(secondary.get('error',0),float(np.std([x['depth'] for x in clean])))
    secondary['control_scatter']=noise;secondary['upper_3sigma']=max(0,secondary.get('depth',0))+3*noise
    # Minimum mass, separation and central duration under explicit main-sequence
    # companion-radius approximation; grazing systems need full geometry check.
    physics=[]
    for m1 in ([.9,1.2,1.6] if tg.get('mass') is None else [float(tg['mass'])]):
        P=float(n['period']);ecc=float(n['eccentricity']);K=float(n['semi_amplitude_primary']);fm=1.036149e-7*P*K**3*(1-ecc**2)**1.5
        low,high=.001,5.
        for _ in range(80):
            m2=(low+high)/2
            if m2**3/(m1+m2)**2>fm:high=m2
            else:low=m2
        m2=(low+high)/2;a=4.208278*(m1+m2)**(1/3)*P**(2/3);r1=float(tg['rad']);r2=m2**.8 if m2<1 else m2**.57
        durations={kind:float(P/np.pi*(r1+r2)/a*np.sqrt(1-ecc**2)/(1+(1 if kind=='A' else -1)*ecc*np.sin(mu[2]))*24) for kind in ['A','B']}
        physics.append(dict(m1=m1,m2_min=m2,f_mass=fm,a_rsun=a,r1_rsun=r1,r2_approx_rsun=r2,central_T14_hours=durations,observed_T14_hours=sh['T14']*24))
    out=dict(gaia_source='shared-full-review/gaia-nss-ari.csv',gaia_bit_index=bit,w_tp_corr=corr,gaia_comparison=res,primary_conjunction=primary,predicted_secondary_phase=phase,secondary=secondary,secondary_windows=allrows,controls=control,physics=physics,period_delta_sigma=(eph['P']-mu[0])/np.hypot(eph['P_error'],float(n['period_error'])))
    json.dump(out,open(dest/'orbit-gates.json','w'),indent=2);print(tic,'primary',primary,'secondary phase/stat',phase,secondary,'physics',physics,flush=True)
