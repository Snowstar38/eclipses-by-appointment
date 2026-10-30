import numpy as np, glob, os
from astropy.io import fits
D='/tmp/claude-0/-home-user-eclipses-paper-review/55c92ff4-798a-544f-be03-9888c6804905/scratchpad/data/vet04'
GAIA={'283532878':dict(P=17.42978669295818506,eP=8.8529550e-03,Tp=380.47053566681467,eTp=0.3199847300,e=0.3519805625291096973,ee=0.0390625520,w=345.769957761088,ew=7.29386230,K1=28.24378006708665367),
      '407877153':dict(P=17.09019815692232669,eP=6.2858580e-03,Tp=380.8190058663926,eTp=1.1854453000,e=0.1261253831345137411,ee=0.0880497100,w=319.743664536709,ew=23.89891400,K1=23.18874062242855061)}
def load(tic, author=None):
    """return list of dict(author, sector, t, f(normalised SAP), fe, qual-ok only)"""
    out=[]
    for fn in sorted(glob.glob(f'{D}/{tic}/mastDownload/HLSP/*/*.fits')):
        h=fits.open(fn); hd=h[0].header; d=h[1].data
        au='QLP' if 'qlp' in fn else 'TESS-SPOC'
        if author and au!=author: continue
        t=np.array(d['TIME'],float); q=np.array(d['QUALITY'])
        sap=np.array(d['SAP_FLUX'],float)
        if au=='QLP':
            fe=np.array(d['KSPSAP_FLUX_ERR'],float) if 'KSPSAP_FLUX_ERR' in d.columns.names else np.full_like(sap,np.nan)
        else:
            fe=np.array(d['SAP_FLUX_ERR'],float)
        m=(q==0)&np.isfinite(t)&np.isfinite(sap)
        med=np.nanmedian(sap[m])
        out.append(dict(author=au,sector=hd['SECTOR'],cam=hd.get('CAMERA'),ccd=hd.get('CCD'),t=t[m],f=sap[m]/med,fe=fe[m]/med if au!='QLP' else fe[m],
                        t_all=t, f_all=sap/np.nanmedian(sap[m]), q_all=q, fn=fn))
    return out
