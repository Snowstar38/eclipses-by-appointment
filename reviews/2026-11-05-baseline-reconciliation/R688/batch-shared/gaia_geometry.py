import csv,json,math
from pathlib import Path
import numpy as np
H=Path(__file__).parent
rows=list(csv.DictReader(open(H.parent/'pilot48'/'shared-catalogues'/'raw'/'gaia_nss.txt')))
r=next(x for x in rows if x['source_id']=='2204160934098817280')
P=float(r['period']); e=float(r['eccentricity']); w=math.radians(float(r['arg_periastron'])); tp=389+float(r['t_periastron'])
ep=json.load(open(H/'sap-measurements.json'))['screening_epoch_btjd']
def conj(v,k):
    p,ec,om,per=v; nu=(math.pi/2 if k==0 else 3*math.pi/2)-om
    E=2*math.atan2(math.sqrt(1-ec)*math.sin(nu/2),math.sqrt(1+ec)*math.cos(nu/2))
    return per+((E-ec*math.sin(E))%(2*math.pi))/(2*math.pi)*p
v=np.array([P,e,w,tp]); sig=np.array([float(r['period_error']),float(r['eccentricity_error']),math.radians(float(r['arg_periastron_error'])),float(r['t_periastron_error'])])
cor=np.eye(7); vals=np.array([float(x) for x in r['corr_vec'].strip('{}').split(',')]);i=0
for a in range(1,7):
    for b in range(a):cor[a,b]=cor[b,a]=vals[i];i+=1
# SB2 order: P,gamma,K1,K2,e,omega,Tp.
sub=cor[np.ix_([0,4,5,6],[0,4,5,6])]
res=[]
for k in (0,1):
    c=conj(v,k);n=round((ep-c)/P); predicted=c+n*P
    deriv=[]
    for j in range(4):
        step=max(sig[j]*.0001,1e-8);a=v.copy();b=v.copy();a[j]+=step;b[j]-=step
        deriv.append(((conj(a,k)+n*a[0])-(conj(b,k)+n*b[0]))/(2*step)*sig[j])
    uncertainty=math.sqrt(max(0,np.array(deriv)@sub@np.array(deriv)))
    res.append(dict(kind=k,gaia_predicted_btjd=predicted,gaia_linear_covariance_error_days=uncertainty,screening_bls_offset_days=ep-predicted,screening_bls_offset_phase=(ep-predicted)/P))
K1=float(r['semi_amplitude_primary']);K2=float(r['semi_amplitude_secondary']);fac=1.036149e-7*P*(1-e*e)**1.5
m1sin3=fac*(K1+K2)**2*K2;m2sin3=fac*(K1+K2)**2*K1
a_sin=1.9758e-2*(K1+K2)*P*math.sqrt(1-e*e) # solar radii
info=dict(source_id=r['source_id'],solution_type=r['nss_solution_type'],period_days=P,period_error_days=sig[0],eccentricity=e,omega_deg=math.degrees(w),t_periastron_btjd=tp,gaia_reference='Gaia JD2016 offset: BTJD 389',correlation_order='P,gamma,K1,K2,e,omega,Tp; lower triangle',correlation_min_eigenvalue=float(np.linalg.eigvalsh(cor).min()),conjunctions=res,periastron_relative_phase_of_bls=((ep-tp)/P)%1,semi_amplitudes_km_s=[K1,K2],mass_ratio_m2_over_m1=K1/K2,m1_sin3_solar=m1sin3,m2_sin3_solar=m2sin3,a_sin_solar_radii=a_sin,notes='Conjunction assumes edge-on; BLS epoch is a screening prediction, not measured eclipse time. Linear covariance uncertainty is descriptive and Gaia-period extrapolation can dominate. Masses are minimum masses, assuming published SB2 velocities.')
(H/'gaia-geometry.json').write_text(json.dumps(info,indent=2)+'\n')
print(json.dumps(info,indent=2))
