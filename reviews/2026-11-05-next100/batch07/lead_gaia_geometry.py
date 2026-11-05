"""Illustrative edge-on conjunction from source-specific Gaia SB1 elements."""
import csv,json
from pathlib import Path
import numpy as np
B=Path(__file__).resolve().parent;R=B.parent
queue=list(csv.DictReader((B/'queue.csv').open(encoding='utf8')))
ids={r['gaia_dr3']:r for r in queue}
out=[]
for g in csv.DictReader((R/'shared-catalogues'/'gaia_nss.csv').open(encoding='utf8')):
    if g['source_id'] not in ids:continue
    if not all(g.get(k) for k in ('eccentricity','arg_periastron','t_periastron','period')):continue
    q=ids[g['source_id']];e=float(g['eccentricity']);w=float(g['arg_periastron']);p=float(g['period']);tp=float(g['t_periastron'])
    for kind,fdeg in [('inferior_approx',90-w),('superior_approx',270-w)]:
        f=np.deg2rad(fdeg);E=2*np.arctan2(np.sqrt(1-e)*np.sin(f/2),np.sqrt(1+e)*np.cos(f/2));M=(E-e*np.sin(E))%(2*np.pi)
        out.append(dict(sample_id=q['sample_id'],tic=q['tic'],source_id=g['source_id'],kind=kind,period_days=p,period_error_days=g.get('period_error'),
            eccentricity=e,omega_deg=w,omega_error_deg=g.get('arg_periastron_error'),t_periastron_gaia_days=tp,t_periastron_error_days=g.get('t_periastron_error'),
            approx_conjunction_btjd_cycle0=float(389+tp+p*M/(2*np.pi)),phase_fraction=float(M/(2*np.pi)),
            note='Edge-on f=90/270-omega approximation, not measured eclipse timing; Gaia epoch conversion BTJD=Gaia days+389.'))
(B/'lead-gaia-geometry.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print([(z['sample_id'],z['kind'],round(z['phase_fraction'],4)) for z in out])
