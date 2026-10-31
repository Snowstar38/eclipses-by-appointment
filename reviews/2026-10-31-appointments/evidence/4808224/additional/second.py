"""Other pipelines: TESS-SPOC (s8,9,35) and TGLC (s8,9) at primary and secondary times. Same trapezoid shape as QLP,
fit tc, depth and quadratic baseline only."""
import numpy as np, glob, json
from astropy.io import fits
src=open('ecl.py').read(); exec(src[src.index('def trap'):src.index('res=[]')])
ep=json.load(open('ephem.json')); T0,P=ep['T0'],ep['P']; sf=json.load(open('secfit.json'))
C='[local path omitted]'
for fn in sorted(glob.glob(C+'*lc.fits')):
    h=fits.open(fn); d=h[1].data; cols=d.columns.names
    t=d['TIME']; 
    fc=[c for c in ('SAP_FLUX','cal_aper_flux','aperture_flux','PDCSAP_FLUX') if c in cols]
    qc=[c for c in ('QUALITY','TESS_flags','TGLC_flags') if c in cols]
    for fcol in fc[:2]:
        f=d[fcol]; q=d[qc[0]] if qc else np.zeros(len(t))
        for lab,ph,dep,T14,T12 in (('pri',0,0.051,7.7/24,2.9/24),('sec',sf['phase'],sf['depth'],sf['T14'],sf['T12'])):
            for k in range(-1,120):
                tg=T0+(k+ph)*P
                g=np.isfinite(t)&np.isfinite(f)&(np.abs(t-tg)<0.8)
                if g.sum()<15 or not ((t[g]<tg-0.2).sum()>3 and (t[g]>tg+0.2).sum()>3): continue
                tt,ff,qq=t[g],f[g]/np.nanmedian(f[g]),q[g]; cad=np.median(np.diff(tt))
                def c2(x):
                    if x[1]<-0.02: return 1e9
                    u=tt-tg; return np.sum((ff-trap(tt,x[0],x[1],T14,T12,cad)*(x[2]+x[3]*u+x[4]*u*u))**2)
                x=nm(c2,[tg,dep,1,0,0],[0.02,0.002,0.001,0.001,0.001],2000)
                r=ff-trap(tt,x[0],x[1],T14,T12,cad)*(x[2]+x[3]*(tt-tg)+x[4]*(tt-tg)**2)
                print(f"{fn.split('/')[-1][:40]:40s} {fcol:14s} {lab} E{k}: tc {x[0]:.4f} (O-C {(x[0]-tg)*24:+.2f} h) depth {x[1]*100:.2f}% rms {np.std(r)*100:.2f}% n={g.sum()} flagged={(qq!=0).sum()}")
