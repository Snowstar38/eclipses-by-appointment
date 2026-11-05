import json,math
from pathlib import Path
import numpy as np
from scipy.optimize import brentq
B=Path(__file__).resolve().parent;src=json.loads((B/'SOURCE-SNAPSHOT.json').read_text(encoding='utf8')); lead=json.loads((B/'gaia-geometry.json').read_text(encoding='utf8'));out={}
for tic in ['184398115','95623701','342060048','284613090']:
 g=src[tic]['target']['gaia'];m=json.loads((B/tic/'measurements.json').read_text(encoding='utf8'));P=float(g['period']);e=float(g['eccentricity']);w=math.radians(float(g['arg_periastron']));tp=389+float(g['t_periastron']);ep=m['reference_epoch_btjd'];c=[]
 for L in [math.pi/2,3*math.pi/2]:
  nu=(L-w)%(2*math.pi); E=2*math.atan2(math.sqrt(1-e)*math.sin(nu/2),math.sqrt(1+e)*math.cos(nu/2));M=(E-e*math.sin(E))%(2*math.pi); t=tp+P*M/(2*math.pi);cycle=round((ep-t)/P);c.append(t+cycle*P)
 ev=[x for x in m['events'] if x.get('timing_usable')];res=[(x['mid_btjd']-ev[0]['mid_btjd'])-(x['cycle']-ev[0]['cycle'])*P for x in ev];out[tic]={'gaia_period':P,'phot_period':m['period_days'],'phot_period_error':m['period_error_days'],'gaia_period_error':float(g['period_error']),'phot_minus_gaia_days':m['period_days']-P,'conjunction_btjd':c,'difference_vs_lead_days':[c[i]-lead[tic]['conjunctions'][i]['gaia_conjunction_btjd'] for i in [0,1]],'event_residual_days_relative_first_gaia_period':res,'cycles':[x['cycle'] for x in ev],'solution_type':g['nss_solution_type']}
print(json.dumps(out,indent=2));(B/'helper-geometry.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
