from astropy.io import fits
from astropy.wcs import WCS
import numpy as np, json, pathlib, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
p=pathlib.Path(r'[workspace]/Astra\made\final-night-2026-11-05\reserve500\batch04\394405964')
with fits.open(p/'helper-tesscut-102.fits') as h:
 d=h[1].data;t=np.array(d['TIME'],float);q=np.array(d['QUALITY'],int); f=np.array(d['FLUX'],float); x,y=WCS(h[2].header).world_to_pixel_values(218.711680937865,-63.1960011797097)
yy,xx=np.indices((7,7));ap=(abs(xx-round(float(x)))<=1)&(abs(yy-round(float(y)))<=1); sky=np.hypot(xx-x,yy-y)>2.8
b=np.nanmedian(f[:,sky],axis=1); flux=np.nansum(f[:,ap]-b[:,None],axis=1);good=np.isfinite(t)&np.isfinite(flux)&(q==0); center=1625.6796085096482+89*28.222390625629718;dur=1.1208382402987076
core=good&(abs(t-center)<dur*.3);left=good&(t>center-1.5*dur)&(t<center-.5*dur);right=good&(t>center+.5*dur)&(t<center+1.5*dur)
print(json.dumps(dict(x=float(x),y=float(y),tmin=float(np.nanmin(t)),tmax=float(np.nanmax(t)),center=center,good=int(good.sum()),core=int(core.sum()),left=int(left.sum()),right=int(right.sum()),flagged_core=int((np.isfinite(t)&(abs(t-center)<dur*.3)&(q!=0)).sum()),depth_ppt=float(1000*(1-np.nanmedian(flux[core])/np.nanmedian(flux[left|right]))) if core.sum() and left.sum() and right.sum() else None),indent=2))
fig,ax=plt.subplots(figsize=(12,3));ax.plot(t[good],flux[good]/np.nanmedian(flux[good]),'.',ms=1);ax.axvline(center,color='r');ax.axvspan(center-dur/2,center+dur/2,color='r',alpha=.15);ax.set(xlabel='BTJD',ylabel='3x3 background-subtracted relative flux',title='RS027 S102; red = assumed S12-anchored Gaia period');fig.tight_layout();fig.savefig(p/'helper-s102.png',dpi=140)
