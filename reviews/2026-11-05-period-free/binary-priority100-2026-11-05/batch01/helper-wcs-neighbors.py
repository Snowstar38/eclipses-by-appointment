import csv,json,math
from pathlib import Path
from astropy.io import fits
from astropy.wcs import WCS
B=Path(__file__).resolve().parent;rows={r['sample_id']:r for r in csv.DictReader((B/'queue.csv').open())};data=json.loads((B/'helper-neighbors-all.json').read_text());sp=json.loads((B/'helper-spatial-rest.json').read_text());sp={z['tic']:z for z in sp};out=[]
for sid in ['T005','T007','T009','T010']:
 r=rows[sid];a=next(z for z in data if z['sample_id']==sid);z=sp[r['tic']];h=fits.open(B/f'helper-{r["tic"]}-tesscut.fits');w=WCS(h[2].header);cx,cy=z['diff_centroid'];ns=[]
 for n in a['capable']:
  x,y=map(float,w.all_world2pix(float(n['ra']),float(n['dec']),0));ns.append({'id':n['source_id'],'xy':[x,y],'distance_from_diff_pix':math.hypot(x-cx,y-cy),'distance_from_target_pix':math.hypot(x-z['target_pixel'][0],y-z['target_pixel'][1])})
 out.append({'sample_id':sid,'diff_centroid':z['diff_centroid'],'target_pixel':z['target_pixel'],'neighbors':ns});print(sid,[(x['id'],round(x['distance_from_diff_pix'],2),round(x['distance_from_target_pix'],2)) for x in ns if x['distance_from_target_pix']<3])
(B/'helper-wcs-neighbors.json').write_text(json.dumps(out,indent=2))
