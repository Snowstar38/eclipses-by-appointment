import json,math
from pathlib import Path
B=Path(__file__).resolve().parent;g=json.loads((B.parent/'source-packets/467963921/sources.json').read_text())['target']['gaia']; P=float(g['period']);e=float(g['eccentricity']);w=float(g['arg_periastron']);tp=float(g['t_periastron']);sig=[float(g[k]) for k in ('period_error','eccentricity_error','arg_periastron_error','t_periastron_error')]
def f(vals,n):
 p,e,w,t=vals;nu=math.pi/2-math.radians(w);E=2*math.atan2(math.sqrt(1-e)*math.sin(nu/2),math.sqrt(1+e)*math.cos(nu/2));return 389+t+((E-e*math.sin(E))%(2*math.pi))/(2*math.pi)*p+n*p
v=[P,e,w,tp];out=[]
for n,obs in [(54,3119.898300253734),(69,3865.639013448697),(75,4163.932907633012)]:
 pred=f(v,n);components=[]
 for i,s in enumerate(sig):
  h=s/100; x=v.copy();x[i]+=h;y=v.copy();y[i]-=h;components.append((f(x,n)-f(y,n))/(2*h)*s)
 out.append({'n':n,'prediction':pred,'observed':obs,'observed_minus_prediction':obs-pred,'one_sigma_components_independent_days':components,'independent_quadrature_days':sum(x*x for x in components)**.5})
print(json.dumps(out,indent=2));(B/'helper-orbit-uncertainty.json').write_text(json.dumps({'events':out,'note':'First-order diagonal-only propagation of Gaia published marginal uncertainties, assumes no correlations; input covariance not present in source packet; model edge-on and timing template approximate. Not a calibrated compatibility test.'},indent=2))

