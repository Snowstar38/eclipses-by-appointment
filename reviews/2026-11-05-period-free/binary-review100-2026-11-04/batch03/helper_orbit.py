import json,math
from pathlib import Path
B=Path(__file__).resolve().parent;g=json.loads((B.parent/'source-packets/113645244/sources.json').read_text())['target']['gaia'];v=[float(g[k]) for k in ('period','eccentricity','arg_periastron','t_periastron')];sig=[float(g[k]) for k in ('period_error','eccentricity_error','arg_periastron_error','t_periastron_error')];obs=1676.360967

def f(v,side,n):
 p,e,w,t=v;nu=side*math.pi/2-math.radians(w);E=2*math.atan2(math.sqrt(1-e)*math.sin(nu/2),math.sqrt(1+e)*math.cos(nu/2));return 389+t+((E-e*math.sin(E))%(2*math.pi))/(2*math.pi)*p+n*p
out=[]
for side in [1,3]:
 n=round((obs-f(v,side,0))/v[0]);pred=f(v,side,n);comp=[]
 for i,s in enumerate(sig):
  h=s/100;x=v.copy();y=v.copy();x[i]+=h;y[i]-=h;comp.append((f(x,side,n)-f(y,side,n))/(2*h)*s)
 out.append({'side':side,'cycle':n,'pred_btjd':pred,'observed_minus_pred_days':obs-pred,'independent_sigma_components':comp,'diagonal_only_sigma_days':sum(x*x for x in comp)**.5})
obj={'gaia':g,'results':out,'caveat':'edge-on conjunction; periastron time converted from Gaia epoch via +389; diagonal-only errors ignore covariance, not calibrated compatibility test; periastron omega convention may swap labels.'};(B/'helper-orbit.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(out,indent=2))
