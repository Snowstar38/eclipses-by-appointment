from astropy.io.votable import parse_single_table
from astropy.coordinates import SkyCoord
from astropy import units as u
import numpy as np,json,pathlib
b=pathlib.Path('[local-path-redacted]');z=json.load(open(b.parent/'source-packets/454228598/sources.json'))['queue_row'];T=parse_single_table(b/'helper-pixels/454228598/gaia.raw').to_table();p=SkyCoord(float(z['ra_deg'])*u.deg,float(z['dec_deg'])*u.deg); c=SkyCoord(np.array(T['ra'],float)*u.deg,np.array(T['dec'],float)*u.deg);s=c.separation(p).arcsec; out=[]
for i in np.where(s<60)[0]:
 a=T[i];sid=str(a['datalinkID']); m=a['phot_g_mean_mag'];
 if sid==z['gaia_dr3'] or np.ma.is_masked(m):continue
 ratio=10**(-.4*(float(m)-float(z['gaia_G'])));
 if ratio>.01:out.append({'gaia':sid,'sep_arcsec':float(s[i]),'G':float(m),'flux_ratio_G':ratio})
(b/'helper-h039-neighbors.json').write_text(json.dumps(out,indent=2));print(out)
