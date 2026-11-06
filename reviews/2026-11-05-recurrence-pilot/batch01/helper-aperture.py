from pathlib import Path
import numpy as np,json,hashlib
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;tic='147413927';out=[]
for sec,c in [(37,2317.923),(90,3750.813)]:
 p=B/tic/f'helper-tesscut-s{sec:03}.fits'
 with fits.open(p,memmap=False) as h:
  d=h[1].data;t=np.array(d['TIME'],float);f=np.array(d['FLUX'],float);q=np.array(d['QUALITY'],int);w=WCS(h[2].header)
 x,y=w.world_to_pixel_values(163.21764583099278,-47.70130734349548);ix,iy=round(float(x)),round(float(y));ok=(q==0)&np.isfinite(t)&np.all(np.isfinite(f),axis=(1,2))
 sky=np.median(f[:,[0,0,-1,-1],[0,-1,0,-1]],axis=1);flux=np.sum(f[:,iy-1:iy+2,ix-1:ix+2],axis=(1,2))-9*sky
 core=ok&(abs(t-c)<.13);side=ok&(abs(t-c)>.48)&(abs(t-c)<.95);near=ok&(abs(t-c)<1.1);base=np.median(flux[side]);depth=1-np.median(flux[core])/base;tt=t[near]; cadence=np.median(np.diff(t[ok]));rec=dict(sector=sec,center_btjd=c,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),core_interval=[c-.13,c+.13],side_intervals=[[c-.95,c-.48],[c+.48,c+.95]],n_core=int(core.sum()),n_side=int(side.sum()),core_first=float(t[core].min()),core_last=float(t[core].max()),core_max_gap=float(np.max(np.diff(t[core]))),nominal_cadence_days=float(cadence),side_first=float(t[side].min()),side_last=float(t[side].max()),baseline_flux=float(base),sky_median=float(np.median(sky[side])),depth_ppt=float(depth*1000),same_photons=True);out.append(rec)
 plt.figure(figsize=(9,3));plt.plot(t[near]-c,1000*(flux[near]/base-1),'.',ms=2);plt.axvspan(-.13,.13,color='red',alpha=.1);plt.axhline(0,color='k',lw=.5);plt.title(f'V007 S{sec} 3x3 corner-sky same-photon extraction');plt.ylabel('relative flux (ppt)');plt.xlabel('BTJD - center (d)');plt.tight_layout();plt.savefig(B/tic/f'helper-aperture-s{sec:03}.png',dpi=130);plt.close()
(B/'helper-aperture.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
