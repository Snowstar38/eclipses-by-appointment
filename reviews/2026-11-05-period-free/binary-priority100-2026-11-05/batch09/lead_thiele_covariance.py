"""Linear Gaia NSS conjunction covariance for AstroSpectroSB1 (15-parameter rows).

Parameter order and column-major corr_vec are specified by Gaia DR3:
https://gea.esac.esa.int/archive/documentation/GDR3/Gaia_archive/chap_datamodel/sec_dm_non--single_stars_tables/ssec_dm_nss_two_body_orbit.html
"""
import csv,hashlib,json,math
from pathlib import Path
import numpy as np
B=Path(__file__).resolve().parent
nss=B.parent/'shared-catalogues/gaia_nss.csv'
rows=list(csv.DictReader(nss.open()))
geo={x['sample_id']:x for x in json.loads((B/'lead-thiele.json').read_text())}
keys=['a_thiele_innes','b_thiele_innes','f_thiele_innes','g_thiele_innes','eccentricity','period','t_periastron']
out=[]
for sid in ('T086','T087'):
 g=geo[sid];r=next(z for z in rows if z['source_id']==g['gaia_source_id'] and z['nss_solution_type']=='AstroSpectroSB1')
 assert r['bit_index']=='65535'
 v=np.array([float(r[k]) for k in keys]);sig=np.array([float(r[k+'_error']) for k in keys])
 vec=np.array([float(z) for z in r['corr_vec'].strip('{}').split(',')]);assert len(vec)==105
 full=np.eye(15);idx=0
 for j in range(1,15):
  for i in range(j):full[i,j]=full[j,i]=vec[idx];idx+=1
 ix=[5,6,7,8,12,13,14];cor=full[np.ix_(ix,ix)];cov=cor*np.outer(sig,sig)
 kind=g['closest']['kind'];cyc=g['closest']['gaia_cycle'];observed=g['evaluation_epoch_btjd']
 def when(a):
  A,Bb,F,G,e,P,tp=a
  omega=((math.atan2(Bb-F,A+G)-math.atan2(Bb+F,A-G))/2)%math.pi
  nu=(math.pi/2 if kind=='A' else 3*math.pi/2)-omega
  E=2*math.atan2(math.sqrt(1-e)*math.sin(nu/2),math.sqrt(1+e)*math.cos(nu/2))
  return 389+tp+((E-e*math.sin(E))%(2*math.pi))/(2*math.pi)*P+cyc*P
 center=when(v);assert abs(center-g['closest']['pred_btjd'])<1e-7
 deriv=[]
 for j in range(7):
  h=max(sig[j]*.001,1e-8);a=v.copy();b=v.copy();a[j]+=h;b[j]-=h
  deriv.append((when(a)-when(b))/(2*h))
 deriv=np.array(deriv)
 var=float(deriv@cov@deriv);dvar=float(np.sum((deriv*sig)**2))
 rec=dict(sample_id=sid,tic=g['tic'],gaia_source_id=g['gaia_source_id'],kind=kind,cycle=cyc,pred_btjd=center,observed_btjd=observed,offset_days=observed-center,linear_full_cov_sigma_days=math.sqrt(var),offset_sigma=(observed-center)/math.sqrt(var),diagonal_only_sigma_days=math.sqrt(dvar),jacobian_days_per_unit={k:float(d) for k,d in zip(keys,deriv)},correlation_min_eigenvalue=float(np.linalg.eigvalsh(full).min()),nss_file_sha256=hashlib.sha256(nss.read_bytes()).hexdigest(),covariance_indices_0based=ix,caution='Finite-difference linear propagation of Gaia 15-parameter full corr_vec into a fixed-cycle edge-on conjunction. No eclipse-timing measurement error or nonlinear/orbit model systematics included.')
 out.append(rec)
 print(sid,'offset',round(rec['offset_days'],4),'sigma full',round(rec['linear_full_cov_sigma_days'],4),'diag',round(rec['diagonal_only_sigma_days'],4),'z',round(rec['offset_sigma'],2))
(B/'lead-thiele-covariance.json').write_text(json.dumps(out,indent=2)+'\n')
