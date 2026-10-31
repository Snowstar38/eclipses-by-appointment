"""Alias test: could the two dips belong to a shorter period (8.0 d single kind, or 16.0 d P/S alternation)?
Coverage and box depth (5.9 h, local quadratic baseline) at 3196.0997 +- n*8.0019 inside s69. python alias.py"""
import numpy as np
from astropy.io import fits
V='[local path omitted]'
for lab,fn in (('SPOC',V+'tess2023237165326-s0069-0000000012864953-0264-s_lc.fits'),('QLP','[local path omitted]')):
    d=fits.open(fn)[1].data; t=np.array(d['TIME'],float); f=np.array(d['SAP_FLUX'],float); q=np.array(d['QUALITY'],int)
    for qs in ('q0','allq'):
        ok=np.isfinite(t)&np.isfinite(f)&((q==0) if qs=='q0' else True); tt,ff=t[ok],f[ok]/np.median(f[ok])
        for tc in (3196.0997-8.0019, 3196.0997+2*8.0019, 3196.0997-4.001, 3196.0997+4.001, 3196.0997+3*4.001):
            w=np.abs(tt-tc)<0.12; b=(np.abs(tt-tc)<0.7)&(np.abs(tt-tc)>0.2)
            if w.sum()<5 or b.sum()<20: print(lab,qs,f'{tc:.3f}: not covered (in {w.sum()}, base {b.sum()})'); continue
            c=np.polyfit(tt[b]-tc,ff[b],2); r=ff-np.polyval(c,tt-tc)
            print(lab,qs,f'{tc:.3f}: n_in {w.sum()} depth {-r[w].mean()*100:+.3f}% +- {r[b].std()/np.sqrt(w.sum())*100:.3f}%  (span {tt[w].min():.3f}-{tt[w].max():.3f})')
