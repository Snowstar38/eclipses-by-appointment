import csv,json
from pathlib import Path
b=Path(__file__).resolve().parent;n={r['source_id']:r for r in csv.DictReader((b.parent/'shared-catalogues/gaia_nss-pending.csv').open())};q={r['tic']:r for r in csv.DictReader((b/'queue.csv').open())};a=json.load(open(b/'lead-alias-covered-windows.json'));out={}
for tic,rs in a.items():
 g=n[q[tic]['gaia_dr3']];gp=float(g['period']);se=float(g['period_error']);surv=[dict(label=r['label'],period_d=r['period_d'],gaia_period_offset_sigma=abs(r['period_d']-gp)/se,covered=r['covered']) for r in rs if r['timing_compatible'] and not r['nulls']];out[tic]=dict(gaia_period_d=gp,gaia_period_error_d=se,tested_integer_periods_d=[min(r['period_d'] for r in rs),max(r['period_d'] for r in rs)],survivors=surv,note=('Three measured times including adjacent later events leave only the measured clock among tested timing/coverage alternatives.' if tic=='48099288' else 'Gaia-assisted cycle selection is conditional; this is not independent validation or proof of photometric uniqueness.'))
(b/'lead-joint-alias-selection.json').write_text(json.dumps(out,indent=2));print(out)
