import numpy as np, glob
from astropy.io import fits
D='/tmp/claude-0/-home-user-eclipses-paper-review/55c92ff4-798a-544f-be03-9888c6804905/scratchpad/data/vet05'
def load(tic, author, sector, col='sap_flux', q0=True):
    pat = {'QLP':f'{D}/{tic}/mastDownload/HLSP/hlsp_qlp_*s{sector:04d}-*/*.fits',
           'TESS-SPOC':f'{D}/{tic}/mastDownload/HLSP/hlsp_tess-spoc_*s{sector:04d}_*/*.fits'}[author]
    f=glob.glob(pat)
    if not f: return None
    h=fits.open(f[0]); d=h[1].data
    t=np.array(d['TIME'],float); fl=np.array(d[col.upper()],float)
    fe=np.array(d[col.upper()+'_ERR'],float) if col.upper()+'_ERR' in d.names else np.full_like(fl,np.nan)
    q=np.array(d['QUALITY'])
    m=np.isfinite(t)&np.isfinite(fl)
    if q0: m&=(q==0)
    med=np.nanmedian(fl[m])
    return t[m], fl[m]/med, fe[m]/med, q
