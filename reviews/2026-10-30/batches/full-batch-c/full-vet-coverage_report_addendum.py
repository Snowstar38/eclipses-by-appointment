from pathlib import Path
import json,collections
F=Path(__file__).parent
for p in F.glob('*/REPORT.md'):
 o=json.load(open(p.parent/'orbit-gates.json'));s=json.load(open(p.parent/'secondary-fit.json'));sh=s['shape'];a=o['secondary'];wins=o['secondary_windows']['gaia_other_windows'];counts=dict(collections.Counter(x['status'] for x in wins));sc=dict(collections.Counter(x['status'] for x in s['events']));txt=p.read_text(encoding='utf-8');txt+=f"\nFixed Gaia-phase other-conjunction coverage: {len(wins)} windows; {counts}; depth {a.get('depth',float('nan'))*1000:.4f}ppt; control-inflated conditional3sigma upper value {a.get('upper_3sigma',float('nan'))*1000:.4f}ppt. Optimized windows{sc}; secondaryT14={sh['T14']*24:.4f}h,T12={sh['T14']*sh['fr']*24:.4f}h,T23={sh['T14']*(1-2*sh['fr'])*24:.4f}h. Uncovered windows are not nulls; secondary status is adjudicated above.\n";p.write_text(txt,encoding='utf-8')
