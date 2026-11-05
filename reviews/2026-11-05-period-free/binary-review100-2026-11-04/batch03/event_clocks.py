"""Fit selected same-kind event clocks and compare with Gaia conjunction geometry."""
import json,math
from pathlib import Path
import numpy as np
B=Path(__file__).resolve().parent
groups={
 '294257329':{'primary':[(9,1548.745,0),(36,2285.3133,23),(89,3726.3222,68),(100,4078.5793,79)],'secondary':[(9,1564.811,0),(36,2301.2915,23),(62,3005.8163,45),(89,3742.3679,68)]},
 '224631871':{'primary':[(14,1699.9899,0),(55,2821.7915,25),(82,3539.7622,41)],'secondary':[(15,1715.9279,0),(82,3555.6715,41)]},
}
for tic,kinds in groups.items():
 g=json.loads((B.parent/'source-packets'/tic/'sources.json').read_text())['target']['gaia'];gp=float(g['period']);e=float(g['eccentricity']);w=math.radians(float(g['arg_periastron']));tp=389+float(g['t_periastron']);conj=[]
 for kind,nu in [('A',math.pi/2-w),('B',3*math.pi/2-w)]:
  E=2*math.atan2(math.sqrt(1-e)*math.sin(nu/2),math.sqrt(1+e)*math.cos(nu/2));base=tp+((E-e*math.sin(E))%(2*math.pi))/(2*math.pi)*gp;conj.append((kind,base))
 out={'tic':tic,'gaia_period_days':gp,'gaia_period_error_days':float(g['period_error']),'gaia_eccentricity':e,'gaia_conjunction_bases_btjd':dict(conj),'kinds':{}}
 for name,items in kinds.items():
  y=np.array([x[1] for x in items]);n=np.array([x[2] for x in items]);coef=np.polyfit(n,y,1) if len(items)>2 else [(y[-1]-y[0])/(n[-1]-n[0]),y[0]];period,epoch=coef
  residual=(y-(epoch+period*n)).tolist();offsets=[]
  for ck,base in conj:
   k=round((epoch-base)/gp);pred=base+k*gp;offsets.append({'conjunction_kind':ck,'predicted_at_epoch_btjd':pred,'offset_days':epoch-pred,'offset_phase':(epoch-pred)/gp})
  out['kinds'][name]={'events': [{'sector':s,'center_btjd':t,'cycle':k} for s,t,k in items],'period_days':float(period),'epoch_btjd':float(epoch),'residual_days':residual,'gaia_period_difference_sigma':float((period-gp)/float(g['period_error'])),'gaia_conjunction_offsets':offsets,'caution':'Clock centers from local model fits; this is not a calibrated period uncertainty. Integer cycles use Gaia-compatible assignments and are checked against additional observing occasions.'}
 (B/tic/'event-clock.json').write_text(json.dumps(out,indent=2)+'\n')
 print(tic,[(k,round(v['period_days'],6),round(v['epoch_btjd'],4),round(v['gaia_period_difference_sigma'],2),[(x['conjunction_kind'],round(x['offset_phase'],4)) for x in v['gaia_conjunction_offsets']]) for k,v in out['kinds'].items()])
