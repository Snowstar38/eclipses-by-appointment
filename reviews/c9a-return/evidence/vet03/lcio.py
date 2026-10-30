import numpy as np, glob
from astropy.io import fits
D='/tmp/claude-0/-home-user-eclipses-paper-review/55c92ff4-798a-544f-be03-9888c6804905/scratchpad/data/vet03'
def load(tic):
    """Return list of dicts: pipeline, sector, t, f (SAP/median, QUALITY==0, finite), cadence_days, bkg"""
    out=[]
    for fn in sorted(glob.glob(f'{D}/{tic}/mastDownload/HLSP/*/*.fits')):
        if 'tesscut' in fn: continue
        h=fits.open(fn); d=h[1].data
        pipe='QLP' if 'qlp' in fn else 'SPOC'
        sec=h[0].header['SECTOR']
        t=np.array(d['TIME'],float); f=np.array(d['SAP_FLUX'],float); q=np.array(d['QUALITY'])
        b=np.array(d['SAP_BKG'],float)
        m=(q==0)&np.isfinite(t)&np.isfinite(f)&(f>0)
        cad=np.nanmedian(np.diff(t))
        out.append(dict(pipe=pipe,sector=sec,t=t[m],f=f[m]/np.nanmedian(f[m]),bkg=b[m],cad=cad,ntot=len(t),ngood=m.sum(),tstart=np.nanmin(t),tend=np.nanmax(t)))
    return out
def trap(t,t0,D,T14,r,cad,ss=None):
    # trapezoid, depth D, total duration T14, flat-bottom T23=r*T14; supersampled over cadence
    if ss is None: ss=max(1,int(round(cad/0.0014)))
    ss=min(ss,15)
    off=(np.arange(ss)+0.5)/ss-0.5
    tt=(t[:,None]+off[None,:]*cad)
    x=np.abs(tt-t0); T23=r*T14
    s=np.clip((T14/2-x)/max((T14-T23)/2,1e-6),0,1)
    return (1-D*s).mean(1)
