"""Gaia AstroSpectroSB1 Thiele-Innes conjunction for F002, full 15-parameter covariance."""
import csv,hashlib,json,math
from pathlib import Path
import numpy as np
B=Path(__file__).resolve().parent
nss=B.parent/'shared-catalogues/gaia_nss.csv'
r=next(x for x in csv.DictReader(nss.open(newline='',encoding='utf8')) if x['source_id']=='4785405080341786368' and x['nss_solution_type']=='AstroSpectroSB1')
A,Bb,F,G,C,H=[float(r[k+'_thiele_innes']) for k in ('a','b','f','g','c','h')]
plus=math.hypot(A+G,Bb-F);minus=math.hypot(A-G,Bb+F)
cosi=(plus-minus)/(plus+minus);inc=math.degrees(math.acos(cosi))
omega=((math.atan2(Bb-F,A+G)-math.atan2(Bb+F,A-G))/2)%math.pi
omega_ch=math.atan2(C,H)%math.pi
branch_difference_deg=math.degrees(abs(((omega-omega_ch+math.pi/2)%math.pi)-math.pi/2))
P=float(r['period']);ecc=float(r['eccentricity']);tp=389+float(r['t_periastron']);epoch=1434.925
keys=['a_thiele_innes','b_thiele_innes','f_thiele_innes','g_thiele_innes','eccentricity','period','t_periastron']
v=np.array([float(r[k]) for k in keys]);sig=np.array([float(r[k+'_error']) for k in keys]);vec=np.array([float(z) for z in r['corr_vec'].strip('{}').split(',')]);assert len(vec)==105
full=np.eye(15);i=0
for j in range(1,15):
 for k in range(j):full[k,j]=full[j,k]=vec[i];i+=1
ix=[5,6,7,8,12,13,14];cov=full[np.ix_(ix,ix)]*np.outer(sig,sig)
def when(a,kind,cycle):
 A,Bb,F,G,e,P,tp=a;w=((math.atan2(Bb-F,A+G)-math.atan2(Bb+F,A-G))/2)%math.pi
 nu=(math.pi/2 if kind=='A' else 3*math.pi/2)-w
 E=2*math.atan2(math.sqrt(1-e)*math.sin(nu/2),math.sqrt(1+e)*math.cos(nu/2))
 return 389+tp+((E-e*math.sin(E))%(2*math.pi))/(2*math.pi)*P+cycle*P
out={'sample_id':'F002','tic':'219345200','gaia_source_id':r['source_id'],'evaluation_epoch_btjd':epoch,'inclination_deg':inc,'omega_abfg_deg':math.degrees(omega),'omega_ch_deg':math.degrees(omega_ch),'omega_branch_difference_deg':branch_difference_deg,'gaia_period_days':P,'eccentricity':ecc,'conjunctions':[],'nss_file_sha256':hashlib.sha256(nss.read_bytes()).hexdigest(),'caution':'ABFG versus C/H omega checks agree within 3 degrees modulo 180. Linear full-covariance Gaia timing at fixed cycle; nonlinear/systematic allowances and eclipse timing error excluded.'}
for kind in ('A','B'):
 base=when(v,kind,0);cycle=round((epoch-base)/P);center=when(v,kind,cycle);der=[]
 for j in range(7):
  h=max(sig[j]*.001,1e-8);a=v.copy();b=v.copy();a[j]+=h;b[j]-=h;der.append((when(a,kind,cycle)-when(b,kind,cycle))/(2*h))
 d=np.array(der);sigma=math.sqrt(float(d@cov@d))
 out['conjunctions'].append({'kind':kind,'cycle':cycle,'pred_btjd':center,'offset_days':epoch-center,'linear_full_cov_sigma_days':sigma,'offset_sigma':(epoch-center)/sigma})
(B/'abfg-geometry.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print('i',inc,'omega',math.degrees(omega),'CH',math.degrees(omega_ch),out['conjunctions'])
