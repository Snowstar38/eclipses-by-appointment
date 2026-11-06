import json,hashlib,csv
from pathlib import Path
import numpy as np
from astropy.io import fits
b=Path(__file__).resolve().parent;out={};hashes=[]
for row in csv.DictReader((b/'queue.csv').open()):
 tic=row['tic'];p=b/tic;ct=json.loads((p/'lead-context.json').read_text());loc=json.loads((p/'helper-localization.json').read_text());h=hashlib.sha256((p/'helper-tesscut.fits').read_bytes()).hexdigest();hashes.append(dict(path=str(p/'helper-tesscut.fits'),expected=loc['fits_sha256'],actual=h,match=h==loc['fits_sha256']))
 for src in ct['source']:
  h=hashlib.sha256(Path(src['path']).read_bytes()).hexdigest();hashes.append(dict(path=src['path'],expected=src['sha256'],actual=h,match=h==src['sha256']))
 if tic=='55662895':
  with fits.open(p/'helper-tesscut.fits') as f:
   t=np.array(f[1].data['TIME']);q=np.array(f[1].data['QUALITY']);cube=np.array(f[1].data['FLUX'])
  c=1371.3646711929484;dur=1.218734;good=(q==0)&np.isfinite(t);core=good&(abs(t-c)<dur*.25);side=good&(abs(t-c)>dur*.75)&(abs(t-c)<dur*2);diff=np.nanmedian(cube[side],axis=0)-np.nanmedian(cube[core],axis=0);base=np.nanmedian(cube[side],axis=0);out[tic]=dict(core_n=int(core.sum()),side_n=int(side.sum()),target_pixel_xy=[4,4],neighbor_pixel_xy=[2,5],target_pixel_absolute_loss=float(diff[4,4]),neighbor_pixel_absolute_loss=float(diff[5,2]),target_pixel_fractional_loss=float(diff[4,4]/base[4,4]),neighbor_pixel_fractional_loss=float(diff[5,2]/base[5,2]),note='Different dilution in pixels; signed absolute losses show target deficit and neighbor brightening. A pixel fractional loss is not an intrinsic source eclipse depth.')
(b/'helper-independent-hash-audit.json').write_text(json.dumps(dict(n=len(hashes),all_match=all(x['match'] for x in hashes),items=hashes),indent=2));(b/'helper-pixel-source-check.json').write_text(json.dumps(out,indent=2));print(len(hashes),all(x['match'] for x in hashes));print(out)
