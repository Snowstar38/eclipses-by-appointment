import json, pathlib, hashlib, math
root=pathlib.Path('[local path omitted] 5/made/sb1-scale/diffimg')
ids=['143375995','122506579','201598744','267094867','156985493','189664666','309308701','141811748','5781196','370329832']
out={}
for t in ids:
 files=list((root/t).glob('diff*.json'))
 if not files:
  out[t]={'available':False};continue
 p=files[0];d=json.loads(p.read_text()); ns=d['neighbours_60']; capable=[{'id':n['source_id'],'sep_arcsec':n['sep'],'required_intrinsic_fraction':n['depth_needed'],'distance_from_deficit_pixels':math.dist(n['px'],d['deficit_centroid'])} for n in ns if n['possible']]
 out[t]={'available':True,'file':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'image_sha256':hashlib.sha256(p.with_suffix('.png').read_bytes()).hexdigest(),'sector':d['sector'],'n_events':d['n_events'],'target_deficit_distance_px':math.dist(d['target_px'],d['deficit_centroid']),'aperture_depths':[d['depth_ap1'],d['depth_ap3'],d['depth_ap5']],'capable_neighbors':capable}
print(json.dumps(out,indent=2))
