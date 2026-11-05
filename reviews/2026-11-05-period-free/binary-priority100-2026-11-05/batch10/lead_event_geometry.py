"""Compare measured eclipse centers against both Gaia conjunction kinds.

Uses the source-specific Gaia DR3 NSS correlation vector and edge-on
conjunction approximation. Event fit uncertainty is listed separately.
"""
import csv,json,math,hashlib
from pathlib import Path
import numpy as np
B=Path(__file__).resolve().parent;src=B.parent/'shared-catalogues/gaia_nss.csv'
nss={}
for r in csv.DictReader(src.open()):nss.setdefault(r['source_id'],[]).append(r)
seeds={
 'T091':{'deep':[2001.0008,2729.0102,3311.4182,3457.0186],'shallow':[1837.4763,2031.6106,3293.4966]},
 'T093':{'deep':[2312.9773,3044.2421],'shallow':[2341.1071]},
 'T095':{'deep':[1921.7669,2611.8693],'shallow':[1907.3921]},
 'T096':{'deep':[1455.3169,2478.5706,3228.9576],'shallow':[2181.1623,2454.0263,2488.1370,2522.2480,3238.5280]},
 'T097':{'deep':[1559.4177,2275.4556],'shallow':[3737.7306]},
 'T098':{'deep':[1795.4125,2908.5573],'shallow':[1805.0055,2883.4018]},
 'T099':{'deep':[1822.7651,2916.8088,3291.0574],'shallow':[1837.1432,2931.2046]},
 'T100':{'narrow':[2231.2842,2236.0406,2237.3993,2248.2674,2977.0231,2979.0604,2981.0976,3706.4598]}}
def conj(v,k):
 P,e,w,tp=v;nu=(math.pi/2 if k==0 else 3*math.pi/2)-w
 E=2*math.atan2(math.sqrt(1-e)*math.sin(nu/2),math.sqrt(1+e)*math.cos(nu/2))
 return tp+((E-e*math.sin(E))%(2*math.pi))/(2*math.pi)*P
out=[]
for row in csv.DictReader((B/'queue.csv').open()):
 sid=row['sample_id'];tic=row['tic'];packet=json.loads((B.parent/'source-packets'/tic/'sources.json').read_text());g=packet['target']['gaia'];matches=[r for r in nss[g['source_id']] if r['nss_solution_type']==g['nss_solution_type'] and abs(float(r['period'])-float(g['period']))<1e-8];assert len(matches)==1;(r,)=matches
 if not r['arg_periastron']:
  out.append(dict(sample_id=sid,tic=tic,status='Gaia omega unavailable; full NSS A/B/F/G required'));continue
 P=float(r['period']);v=np.array([P,float(r['eccentricity']),math.radians(float(r['arg_periastron'])),389+float(r['t_periastron'])]);sig=np.array([float(r['period_error']),float(r['eccentricity_error']),math.radians(float(r['arg_periastron_error'])),float(r['t_periastron_error'])]);nt=6 if r['nss_solution_type'] in ('SB1','SB1C') else 7;cv=[float(z) for z in r['corr_vec'].strip('{}').split(',')];assert len(cv)==nt*(nt-1)//2
 cor=np.eye(nt);z=0
 for i in range(1,nt):
  for j in range(i):cor[i,j]=cor[j,i]=cv[z];z+=1
 inds=[0,3,4,5] if nt==6 else [0,4,5,6];sub=cor[np.ix_(inds,inds)]
 m=json.loads((B/tic/'lead-numeric.json').read_text());events=[]
 for kind,seeds2 in seeds.get(sid,{}).items():
  for seed in seeds2:
   e=min(m['events'],key=lambda x:abs(x['fit_mid_btjd']-seed));assert abs(e['fit_mid_btjd']-seed)<.004
   epoch=e['fit_mid_btjd'];fits=[]
   for k in (0,1):
    c=conj(v,k);cyc=round((epoch-c)/P);pred=c+cyc*P;der=[]
    for j in range(4):
     step=max(sig[j]*.0001,1e-8);a=v.copy();b=v.copy();a[j]+=step;b[j]-=step;der.append(((conj(a,k)+cyc*a[0])-(conj(b,k)+cyc*b[0]))/(2*step)*sig[j])
    gs=math.sqrt(max(0,np.array(der)@sub@np.array(der)))
    fits.append(dict(gaia_conjunction_kind=k,gaia_cycle=cyc,pred_btjd=pred,offset_days=epoch-pred,gaia_linear_sigma_days=gs,offset_in_gaia_sigma=(epoch-pred)/gs))
   events.append(dict(eclipse_kind=kind,sector=e['sector'],measured_mid_btjd=epoch,fit_mid_formal_error_days=e.get('fit_mid_formal_error_days'),nearest=min(fits,key=lambda x:abs(x['offset_days'])),both=fits))
 out.append(dict(sample_id=sid,tic=tic,nss_type=r['nss_solution_type'],gaia_period_days=P,source_nss_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),source_packet_sha256=hashlib.sha256((B.parent/'source-packets'/tic/'sources.json').read_bytes()).hexdigest(),events=events,note='Measured raw-event fit center versus Gaia edge-on conjunction, with propagated source-specific linear NSS covariance. Correlated Gaia uncertainty excludes TESS event-fit error and nonlinear/systematic uncertainty. Comparison alone does not establish source or cycle clock.'))
 print(sid,[(e['eclipse_kind'],e['sector'],round(e['nearest']['offset_days'],3),round(e['nearest']['offset_in_gaia_sigma'],2)) for e in events],flush=True)
(B/'lead-event-geometry.json').write_text(json.dumps(out,indent=2)+'\n')
