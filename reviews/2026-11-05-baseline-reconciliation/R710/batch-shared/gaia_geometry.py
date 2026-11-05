"""Source-specific Gaia SB covariance and conjunction comparison for review9."""
import csv,json,math
from pathlib import Path
import numpy as np
B=Path(__file__).resolve().parent
D=json.loads((B/'SOURCE-SNAPSHOT.json').read_text(encoding='utf-8'))
N={r['source_id']:r for r in csv.DictReader((B.parent/'remaining_cached'/'shared-catalogues'/'raw'/'gaia_nss.txt').open(encoding='utf-8',newline=''))}

def conj(v,k):
    P,e,w,tp=v;nu=(math.pi/2 if k==0 else 3*math.pi/2)-w
    E=2*math.atan2(math.sqrt(1-e)*math.sin(nu/2),math.sqrt(1+e)*math.cos(nu/2))
    return tp+((E-e*math.sin(E))%(2*math.pi))/(2*math.pi)*P

out={}
for tic,src in D.items():
    m=json.loads((B/tic/'measurements.json').read_text(encoding='utf-8'));g=src['target']['gaia'];r=N[g['source_id']]
    assert r['source_id']==g['source_id'] and abs(float(r['period'])-float(g['period']))<1e-8
    P=float(r['period']);e=float(r['eccentricity']);w=math.radians(float(r['arg_periastron']));tp=389+float(r['t_periastron'])
    v=np.array([P,e,w,tp]);sig=np.array([float(r['period_error']),float(r['eccentricity_error']),math.radians(float(r['arg_periastron_error'])),float(r['t_periastron_error'])]);nt=6 if r['nss_solution_type'] in ('SB1','SB1C') else 7
    cor=np.eye(nt);cv=[float(x) for x in r['corr_vec'].strip('{}').split(',')];assert len(cv)==nt*(nt-1)//2
    z=0
    for i in range(1,nt):
        for j in range(i):cor[i,j]=cor[j,i]=cv[z];z+=1
    inds=[0,3,4,5] if nt==6 else [0,4,5,6];sub=cor[np.ix_(inds,inds)]
    ep=m.get('reference_epoch_btjd',m['screen_epoch_btjd']); cs=[]
    for k in (0,1):
        c=conj(v,k);cyc=round((ep-c)/P);pred=c+cyc*P;der=[]
        for j in range(4):
            step=max(sig[j]*.0001,1e-8);a=v.copy();b=v.copy();a[j]+=step;b[j]-=step
            der.append(((conj(a,k)+cyc*a[0])-(conj(b,k)+cyc*b[0]))/(2*step)*sig[j])
        uncertainty=math.sqrt(max(0,np.array(der)@sub@np.array(der)))
        cs.append(dict(kind='A' if k==0 else 'B',gaia_cycle=cyc,gaia_conjunction_btjd=pred,offset_days=ep-pred,offset_phase=(ep-pred)/P,gaia_linear_covariance_error_days=uncertainty))
    K=float(r['semi_amplitude_primary']);fm=1.036149e-7*P*K**3*(1-e*e)**1.5
    pp=m.get('period_days')
    out[tic]=dict(gaia_source_id=r['source_id'],solution_type=r['nss_solution_type'],gaia_period_days=P,gaia_period_error_days=sig[0],photometric_period_days=pp,period_difference_days=pp-P if pp is not None else None,epoch_source='raw_event_fit' if pp is not None else 'screen_prediction_unverified',eccentricity=e,omega_deg=math.degrees(w),periastron_btjd=tp,conjunctions=cs,closest=min(cs,key=lambda c:abs(c['offset_days'])),covariance_order='P,gamma,K,e,omega,Tp' if nt==6 else 'P,gamma,K1,K2,e,omega,Tp',covariance_min_eigenvalue=float(np.linalg.eigvalsh(cor).min()),mass_function_solar=fm,semi_amplitude_primary_km_s=K,note='Gaia covariance submatrix and linear propagation at measured eclipse epoch; descriptive, not a calibrated ownership probability. Edge-on conjunction approximation. Mass function assumes published primary velocity.')
    print(tic,out[tic]['solution_type'],round(out[tic]['closest']['offset_phase'],4),round(out[tic]['closest']['gaia_linear_covariance_error_days'],3),round(fm,4))
(B/'gaia-geometry.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')

