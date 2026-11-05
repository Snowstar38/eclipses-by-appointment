import json,math
from pathlib import Path
import numpy as np
B=Path(__file__).resolve().parent;S=json.loads((B/'SOURCE-SNAPSHOT.json').read_text(encoding='utf8'));G=json.loads((B/'gaia-geometry.json').read_text(encoding='utf8'));out=[]
for tic,s in S.items():
 g=s['target']['gaia'];m=json.loads((B/tic/'measurements.json').read_text(encoding='utf8'));P=float(g['period']);e=float(g['eccentricity']);w=math.radians(float(g['arg_periastron']));tp=389+float(g['t_periastron']);ep=m['reference_epoch_btjd'];cs=[]
 for L in [math.pi/2,3*math.pi/2]:
  nu=(L-w)%(2*math.pi);E=2*math.atan2(math.sqrt(1-e)*math.sin(nu/2),math.sqrt(1+e)*math.cos(nu/2));t=tp+P*((E-e*math.sin(E))%(2*math.pi))/(2*math.pi);cs.append(t+round((ep-t)/P)*P)
 ev=[x for x in m['events'] if x.get('timing_usable')];n=np.array([x['cycle'] for x in ev]);tt=np.array([x['mid_btjd'] for x in ev]);err=np.array([x['timing_error_days'] for x in ev]);A=np.column_stack([np.ones(len(n)),n-n.min()])/err[:,None];beta=np.linalg.lstsq(A,tt/err,rcond=None)[0];depths=[x['model_amplitude_ppt']*min(1,x['duration_days']/(2*x['ingress_parameter_days']))-x['depth_ppt'] for x in ev];out.append({'tic':tic,'gaia_conjunction_differences_days':[cs[i]-G[tic]['conjunctions'][i]['gaia_conjunction_btjd'] for i in range(2)],'period_difference_days':beta[1]-m['period_days'],'epoch_difference_days':beta[0]-m['reference_epoch_btjd'],'max_event_depth_error_ppt':max(map(abs,depths)),'median_depth_difference_ppt':float(np.median([x['depth_ppt'] for x in ev])-m['depth_ppt'])})
print(json.dumps(out,indent=2));(B/'helper-numeric-geometry-audit.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
