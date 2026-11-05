import json,csv,math
from astropy.io import fits
from astropy.wcs import WCS
from pathlib import Path
B=Path(__file__).resolve().parent; Q=list(csv.DictReader((B/'queue.csv').open())); n=json.loads((B.parent/'shared-catalogues/gaia-neighbors.json').read_text())['targets']; out={}
for r in Q:
 t=r['tic']; f=next(iter(B.glob(f'helper-{t}-s*-tesscut.fits')),B/'missing')
 if not f.exists():continue
 with fits.open(f) as h:w=WCS(h[2].header)
 rows=[]
 for x in n[r['sample_id']]:
  if not x['phot_g_mean_mag']:continue
  x0,y0=map(float,w.all_world2pix(float(x['ra']),float(x['dec']),0)); ratio=10**(-.4*(float(x['phot_g_mean_mag'])-float(r['gaia_G'])));rows.append({'source_id':x['source_id'],'mag':float(x['phot_g_mean_mag']),'separation_arcsec':x['separation_arcsec'],'xy':[x0,y0],'G_flux_ratio':ratio,'target':x['is_queue_gaia_source']})
 out[t]=rows
 print(t,[(v['source_id'],round(v['mag'],2),[round(c,2) for c in v['xy']],round(v['G_flux_ratio'],3)) for v in rows if v['G_flux_ratio']>.003])
(B/'helper-neighbor-wcs-extra.json').write_text(json.dumps(out,indent=2))

