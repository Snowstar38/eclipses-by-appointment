import json,csv,numpy as np
from pathlib import Path
b=Path(__file__).resolve().parent
for r in csv.DictReader((b/'queue.csv').open()):
 d=b/r['tic'];l=json.loads((d/'helper-localization.json').read_text());ns=json.loads((d/'lead-neighbors.json').read_text());g=json.loads((d/'lead-diff-gaussian.json').read_text()) if (d/'lead-diff-gaussian.json').exists() else None;out=[]
 for n in ns['neighbors']:
  f=n.get('relative_G_flux');sep=float(np.linalg.norm(np.array(n['pixel_xy'])-l['target_xy']))
  if f and f>.001 and sep<3:
   out.append(dict(source_id=n['source_id'],relative_G_flux=f,separation_pixels=sep,pixel_xy=n['pixel_xy'],difference_gaussian_distance_pixels=float(np.linalg.norm(np.array(n['pixel_xy'])-g['gaussian_xy'])) if g else None))
 (d/'lead-capability-audit.json').write_text(json.dumps({'note':'G-band flux is an approximate capability screen, not a calibrated TESS aperture throughput model. Source localization and raw depth must be interpreted together.','sources':out},indent=2))
 print(r['tic'],[(n['source_id'],round(n['relative_G_flux'],4),round(n['separation_pixels'],2),round(n['difference_gaussian_distance_pixels'],2) if n['difference_gaussian_distance_pixels'] else None) for n in sorted(out,key=lambda x:x['separation_pixels'])[:8]])
