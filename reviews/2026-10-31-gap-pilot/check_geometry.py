import csv,json,pathlib,sys,math
import numpy as np
from scipy.optimize import brentq
O=pathlib.Path(__file__).parent;sys.path.insert(0,'[local path omitted] 5.1/made/appointments');import appoint
ns={r['source_id']:r for r in csv.DictReader(open(O/'catalogues/gaia-nss-full.csv'))};tg=json.load(open(O/'catalogues/targets-selected.json'));tim=json.load(open(O/'timing-results.json'));out={}
for k,v in tg.items():
 if k not in ['167178300','325573958']:
  ss=[l for l in (O/k/'tic-stellar.tsv').read_text().splitlines() if l and not l.startswith('#')];hh=[x.strip() for x in ss[0].split('\t')];rr=[dict(zip(hh,[x.strip() for x in l.split('\t')])) for l in ss[3:]];rr=next(r for r in rr if r['TIC']==k);v['mass']=float(rr['Mass']);v['rad']=float(rr['Rad'])
 g=ns[v['gaia']['source_id']];P=float(g['period']);e=float(g['eccentricity']);K=float(g['semi_amplitude_primary']);w=math.radians(float(g['arg_periastron']));t0=tim[k]['epoch_btjd'];con=appoint.conjunctions(g,rng=np.random.default_rng(int(k)));r={'gaia':g,'eclipse_period_difference_sigma':(tim[k]['period_days']-P)/float(g['period_error']),'conjunctions':{}}
 for kind,(tc,p,st,sp,circ) in con.items():
  n=round((t0-tc)/p);pred=tc+n*p;sig=math.hypot(st,n*sp);r['conjunctions'][kind]={'predicted_btjd':pred,'sigma_days':sig,'observed_minus_predicted_days':t0-pred,'offset_sigma':(t0-pred)/sig}
 fm=1.036149e-7*(1-e*e)**1.5*K**3*P;r['mass_function_solar']=fm
 if v.get('mass') and v.get('rad'):
  M=float(v['mass']);R=float(v['rad']);m=brentq(lambda z:z**3/(M+z)**2-fm,.01,20);a=4.208278*(M+m)**(1/3)*P**(2/3);r.update(primary_mass_TIC=M,primary_radius_TIC=R,minimum_companion_mass_solar=m,separation_solar_radii=a,illustrative_central_duration_hours={kind:P/math.pi*(R+1.0)/a*math.sqrt(1-e*e)/(1+sg*e*math.sin(w))*24 for kind,sg in [('A',1),('B',-1)]},geometry_note='IllustrativeR2=1solar radius; largercompanions/inclination remainfree. Notafitted physicalmodel.')
 else:r['geometry_note']='Conjunction timing andperiod checked usingfullGaiaNSS; no stellarparameters inpilotmatching table, no radius/impactfit.'
 out[k]=r;print(k,r['eclipse_period_difference_sigma'],r['conjunctions'],flush=True)
(O/'geometry-results.json').write_text(json.dumps(out,indent=1))
