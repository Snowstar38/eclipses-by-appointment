import csv,json,hashlib
from pathlib import Path
B=Path(__file__).resolve().parent;rows=list(csv.DictReader((B/'queue.csv').open()));out=[]
for r in rows:
 D=B/r['tic'];l=json.loads((D/'helper-localization.json').read_text());n=json.loads((D/'helper-gaia-neighbors.json').read_text());out.append(dict(sample_id=r['sample_id'],tic=r['tic'],sector=l['event']['sector'],target_xy=l['target_xy'],difference_peak=l['diff_peak_xy'],positive_centroid=l['positive_diff_centroid_xy'],offset_pixels=l['centroid_offset_pixels'],aperture_loss=l['aperture_loss'],neighbors=n['neighbors_sorted'],cone_sha256=n['response_sha256']))
(B/'helper-numeric-audit.json').write_text(json.dumps(out,indent=2),encoding='utf8')
files=[B/'helper_localization.py',B/'helper_neighbors.py',B/'helper_neighbors_retry.py',B/'helper_s109.py',B/'helper-numeric-audit.json',B/'helper-contact.png']
for r in rows:
 D=B/r['tic'];files.extend(D/x for x in ('helper-localization.json','helper-localization.png','helper-tesscut.fits','helper-gaia-cone.csv','helper-gaia-neighbors.json'))
files.extend(B/'34308477'/x for x in ('helper-s109.json','helper-s109.png','helper-s109-tesscut.fits'))
(B/'helper-hashes.json').write_text(json.dumps({str(p.relative_to(B)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files},indent=2),encoding='utf8')
