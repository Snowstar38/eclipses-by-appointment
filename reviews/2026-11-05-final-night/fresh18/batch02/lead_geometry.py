"""Source-specific edge-on Gaia conjunction phase check; descriptive only."""
import json,math
from pathlib import Path
B=Path(__file__).resolve().parent
P=json.loads((B.parent.parent/'fresh-band-next400'/'population.json').read_text())['targets']
cl=json.loads((B/'lead-clocks.json').read_text())
out={}
def conj(period,e,w,tp,k):
 nu=(math.pi/2 if k==0 else 3*math.pi/2)-w
 E=2*math.atan2(math.sqrt(1-e)*math.sin(nu/2),math.sqrt(1+e)*math.cos(nu/2))
 return tp+((E-e*math.sin(E))%(2*math.pi))*period/(2*math.pi)
for tic in P:
 if tic not in cl:continue
 g=P[tic]['gaia'];p=float(g['period']);pe=float(g['period_error']);e=float(g['eccentricity']);w=math.radians(float(g['arg_periastron']));tp=float(g['t_periastron'])+389
 t=cl[tic]['epoch_btjd'];vv=[]
 for kind in (0,1):
  c=conj(p,e,w,tp,kind);cy=round((t-c)/p);offset=t-c-cy*p
  vv.append(dict(conjunction_kind=kind,reference_conjunction_btjd=c,cycle_at_photometric_epoch=cy,offset_d=offset,phase_offset=offset/p,period_accumulation_allowance_d=abs(cy)*pe))
 out[tic]=dict(gaia_p_d=p,gaia_p_error_d=pe,gaia_e=e,gaia_omega_deg=math.degrees(w),gaia_tp_btjd=tp,measured_epoch_btjd=t,conjunctions=vv,note='Approximate edge-on ν=90°−ω or 270°−ω conjunction from Gaia SB1 means. Period accumulation is abs(cycle)*formal period error only, not full covariance or calibrated geometry uncertainty. Interpreting association requires source localization and orbit consistency.')
 print(tic,[(x['conjunction_kind'],round(x['phase_offset'],4),round(x['period_accumulation_allowance_d'],2)) for x in vv])
(B/'lead-geometry.json').write_text(json.dumps(out,indent=2),encoding='utf8')
