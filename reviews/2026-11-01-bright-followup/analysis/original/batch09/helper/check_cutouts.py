import csv,json,pathlib,re
from astropy.io import fits
from astropy.coordinates import SkyCoord
import astropy.units as u
b=pathlib.Path(r'[local path omitted]'); g=json.loads((b/'gaia-geometry.json').read_text())
for row in csv.DictReader((b/'RESULTS.csv').open(encoding='utf-8-sig')):
 t=row['tic']; s=(b/t/'REPORT.md').read_text(encoding='utf-8-sig'); p=re.search(r'Original TESScut binary: (.+?) \(hash',s).group(1); h=fits.getheader(p); d=json.loads((b/t/'historical/gaia.json').read_text()); v=next(x for x in d['src'] if x['source_id']==g[t]['gaia_source_id']); sep=SkyCoord(h['RA_OBJ']*u.deg,h['DEC_OBJ']*u.deg).separation(SkyCoord(float(v['ra'])*u.deg,float(v['dec'])*u.deg)).arcsec; print(t,'sector',h['SECTOR'],'separation_arcsec',round(sep,3))
