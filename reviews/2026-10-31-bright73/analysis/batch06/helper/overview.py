import json
from pathlib import Path
b=Path(r'[local path omitted]')
p=json.loads((b/'pixel-audit.json').read_text());g=json.loads((b/'gaia-geometry.json').read_text())
for t,x in p.items():
 print(t,'target',round(x['target_deficit_distance_px'],3),'capable',[(round(n['separation_arcsec'],2),round(n['deficit_distance_px'],3),round(n['intrinsic_fractional_eclipse_required'],2)) for n in x['capable']], 'phase',round(g[t]['closest']['offset_phase'],4),'dur',round(g[t]['observed_duration_hours'],2),round(g[t]['central_duration_hours_approx'],2))
