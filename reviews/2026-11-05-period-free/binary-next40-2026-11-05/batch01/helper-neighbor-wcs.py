import json,csv,math
from astropy.io import fits
from astropy.wcs import WCS
from pathlib import Path
B=Path(__file__).resolve().parent;Q=list(csv.DictReader((B/'queue.csv').open()));n=json.loads((B.parent/'shared-catalogues/gaia-neighbors.json').read_text())['targets'];sp={x['tic']:x for x in json.loads((B/'helper-spatial.json').read_text())};out={}
for r in Q:
 t=r['tic'];f=B/f'helper-{t}-tesscut.fits';p=sp[t]
 with fits.open(f) as h:w=WCS(h[2].header)
 rows=[]
 for x in n[r['sample_id']]:
  if not x['phot_g_mean_mag']:continue
  x0,y0=map(float,w.all_world2pix(float(x['ra']),float(x['dec']),0));ratio=10**(-.4*(float(x['phot_g_mean_mag'])-float(r['gaia_G']))); off=math.hypot(x0-p['target_pixel'][0],y0-p['target_pixel'][1]);depth=(p.get('depth_ppt') or 0)/1000
  if ratio>=max(depth*.5,.001) and not x['is_queue_gaia_source'] and 0<=x0<=10 and 0<=y0<=10:rows.append({'source_id':x['source_id'],'mag':float(x['phot_g_mean_mag']),'separation_arcsec':x['separation_arcsec'],'xy':[x0,y0],'offset_pixels':off,'G_flux_ratio':ratio,'nominal_fully_disappearing_ratio_over_observed_loss':ratio/depth if depth>0 else None})
 out[t]={'sample_id':r['sample_id'],'target_xy':p['target_pixel'],'depth_ppt':p.get('depth_ppt'),'neighbors_in_cutout':rows,'caveat':'G ratios approximate, bandpass and aperture throughput differ; ratio over observed loss is a rough capability diagnostic, not an exclusion or source ownership proof.'}
 print(r['sample_id'], 'depth',round(depth*1000,2),'neighbors',[(x['source_id'],round(x['offset_pixels'],2),round(x['G_flux_ratio'],3)) for x in rows])
(B/'helper-neighbor-wcs.json').write_text(json.dumps(out,indent=2))
