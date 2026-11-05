"""Source-specific Gaia SB1 conjunction check at selected measured raw dip centers."""
from pathlib import Path
import json, math
import numpy as np
B=Path(__file__).resolve().parent
targets=json.loads((B.parent/'shared-catalogues'/'target-evidence.json').read_text(encoding='utf8'))['targets']
epochs={'F022':2370.838,'F023':1747.380,'F023_late':3581.281,'F028':2229.571}
def conj(v,k):
    P,e,w,tp=v;nu=(math.pi/2 if k==0 else 3*math.pi/2)-w
    E=2*math.atan2(math.sqrt(1-e)*math.sin(nu/2),math.sqrt(1+e)*math.cos(nu/2))
    return tp+((E-e*math.sin(E))%(2*math.pi))*P/(2*math.pi)
out={}
for sid,ep in epochs.items():
    x=next(x for x in targets if x['sample_id']==sid.split('_')[0]);r=x['remote']['gaia_nss']['exact_rows'][0]
    P=float(r['period']);e=float(r['eccentricity']);w=math.radians(float(r['arg_periastron']));tp=389+float(r['t_periastron'])
    v=np.array([P,e,w,tp]);sig=np.array([float(r['period_error']),float(r['eccentricity_error']),math.radians(float(r['arg_periastron_error'])),float(r['t_periastron_error'])])
    cor=np.eye(6);cv=[float(y) for y in r['corr_vec'].strip('{}').split(',')];assert len(cv)==15
    z=0
    for i in range(1,6):
        for j in range(i):cor[i,j]=cor[j,i]=cv[z];z+=1
    sub=cor[np.ix_([0,3,4,5],[0,3,4,5])];cs=[]
    for k in (0,1):
        c=conj(v,k);n=round((ep-c)/P);pred=c+n*P;der=[]
        for j in range(4):
            step=max(sig[j]*.0001,1e-8);a=v.copy();b=v.copy();a[j]+=step;b[j]-=step
            der.append(((conj(a,k)+n*a[0])-(conj(b,k)+n*b[0]))/(2*step)*sig[j])
        unc=math.sqrt(max(0,np.array(der)@sub@np.array(der)))
        cs.append(dict(kind=k,gaia_cycle=n,gaia_conjunction_btjd=pred,measured_minus_pred_days=ep-pred,offset_phase=(ep-pred)/P,gaia_linear_covariance_days=unc))
    out[sid]=dict(tic=x['tic'],gaia_source_id=r['source_id'],raw_eclipse_epoch_btjd=ep,gaia_period_days=P,gaia_eccentricity=e,gaia_omega_deg=math.degrees(w),gaia_tperiastron_btjd=tp,conjunctions=cs,closest=min(cs,key=lambda v:abs(v['measured_minus_pred_days'])),uncertainty_note='Gaia covariance linearization only; does not include full non-Gaussian orbital or event-center model uncertainty. Epochs from raw local fits, some affected by baseline/gaps.')
(B/'lead-geometry.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
for sid,v in out.items(): print(sid,v['closest'])
