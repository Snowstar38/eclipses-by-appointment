"""RV mass function and edge-on lower-mass/central-duration scales, not a geometry fit."""
import json, pathlib, math
R=pathlib.Path(__file__).parent
d=json.loads((R.parent/'selected.json').read_text()); out={}
for tic,t in d['targets'].items():
 g=t['gaia']; P=float(g['period']); e=float(g['eccentricity']); K=float(g['semi_amplitude_primary']); m1=float(t['mass']); r1=float(t['rad'])
 fm=1.036149e-7*K**3*P*(1-e*e)**1.5
 lo,hi=0.,20.
 for _ in range(100):
  m=(lo+hi)/2
  if m**3/(m1+m)**2 <fm:lo=m
  else:hi=m
 m2=(lo+hi)/2; a=4.208278*(m1+m2)**(1/3)*P**(2/3)
 # illustrative MS R2=M2 solar radii; not valid as final stellar inference.
 r2=m2; duration=P/math.pi*math.asin(min(1,(r1+r2)/a))*24
 out[tic]=dict(P_d=P,e=e,K1_kms=K,mass_function_msun=fm,M1_catalogue=m1,R1_catalogue=r1,M2_min_msun=m2,a_Rsun=a,illustrative_R2=m2,circular_central_T14_h=duration,depth_min_radius_ratio=math.sqrt(float(next(x for x in d['rows'] if x['tic']==tic).get('depth_ppt',30))/1000) if False else None)
(R/'physics-initial.json').write_text(json.dumps(out,indent=2))
for k,v in out.items():print(k, 'f=',round(v['mass_function_msun'],4),'M2min=',round(v['M2_min_msun'],3),'a=',round(v['a_Rsun'],2),'central circular h=',round(v['circular_central_T14_h'],2))
