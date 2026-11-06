import json,numpy as np
from pathlib import Path
b=Path(__file__).resolve().parent
for d in b.glob('*/lead-neighbors.json'):
 t=d.parent.name;o=json.loads(d.read_text());l=json.loads((d.parent/'helper-localization.json').read_text());xy=np.array(l['target_xy']);c=np.array(l['positive_diff_centroid_xy']); ns=o['neighbors']; near=[]
 for n in ns:
  z=np.array(n['pixel_xy']);sep=float(np.linalg.norm(z-xy));n['separation_pixels']=sep;n['difference_centroid_distance_pixels']=float(np.linalg.norm(z-c));
  if sep<6 and n['relative_G_flux'] and n['relative_G_flux']>.001: near.append(n)
 near.sort(key=lambda n:n['separation_pixels']);o['nearby_flux_sources']=near;d.write_text(json.dumps(o,indent=2));print(t,[(n['source_id'],round(n['relative_G_flux'],3),round(n['separation_pixels'],2),[round(x,2) for x in n['pixel_xy']],round(n['difference_centroid_distance_pixels'],2)) for n in near[:10]])
