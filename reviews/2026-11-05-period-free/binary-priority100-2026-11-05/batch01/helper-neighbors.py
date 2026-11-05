import csv,json,math,hashlib
from pathlib import Path
from astropy.coordinates import SkyCoord
from astropy import units as u
B=Path(__file__).resolve().parent;p=B.parent/'shared-catalogues/gaia-neighbors-first4.csv';tab=list(csv.DictReader(p.open()));q=list(csv.DictReader((B/'queue.csv').open()))[:4];sp=json.loads((B/'helper-spatial.json').read_text());out=[]
for row,o in zip(q,sp):
 pos=SkyCoord(float(row['ra_deg'])*u.deg,float(row['dec_deg'])*u.deg);depth=o['qlp_depths_ppt']['SAP_FLUX']/1000;alln=[]
 for x in tab:
  if x['source_id']==row['gaia_dr3'] or not x['phot_g_mean_mag']:continue
  sep=pos.separation(SkyCoord(float(x['ra'])*u.deg,float(x['dec'])*u.deg)).arcsec
  if sep>120:continue
  G=float(x['phot_g_mean_mag']);r=10**(-.4*(G-float(row['gaia_G'])));need=depth*(1+r)/r
  if need<=1:alln.append({'source_id':x['source_id'],'ra':float(x['ra']),'dec':float(x['dec']),'sep_arcsec':float(sep),'G':G,'ratio_G':r,'required_fraction_ideal':need})
 out.append({'tic':row['tic'],'depth_ppt':depth*1000,'capable_within_120_arcsec':sorted(alln,key=lambda z:z['sep_arcsec']),'gaia_csv_sha256':hashlib.sha256(p.read_bytes()).hexdigest()});print(row['tic'],out[-1]['capable_within_120_arcsec'])
(B/'helper-neighbors.json').write_text(json.dumps(out,indent=2))
