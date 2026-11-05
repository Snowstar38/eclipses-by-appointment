import json, hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
B=Path(__file__).parent
cases=[('H066','368903210',19,1820.9536195,80.2672882703167,42.504337529512355,59),('H067','321154190',94,3874.9424757,347.4464648792403,-87.74560820123955,66)]
out=[]
for sid,tic,sec,c,ra,dec,cs in cases:
 p=Path(f'[local-path-redacted]')
 with fits.open(p) as h:
  a=h[1].data;t=np.array(a['TIME'],float);q=np.array(a['QUALITY']); f=np.array(a['SAP_FLUX'],float); x=np.array(a['SAP_X'],float);y=np.array(a['SAP_Y'],float);bg=np.array(a['SAP_BKG'],float)
  ok=(abs(t-c)<2)&(q==0)&np.isfinite(f)&np.isfinite(x)&np.isfinite(y)&np.isfinite(bg)
  corr={k:float(np.corrcoef(f[ok],v[ok])[0,1]) for k,v in [('time',t),('x',x),('y',y),('background',bg)]}
  # also remove linear time trend to distinguish slow pointing drift from co-variation
  detr=lambda z:z[ok]-np.polyval(np.polyfit(t[ok]-c,z[ok],1),t[ok]-c)
  partial={k:float(np.corrcoef(detr(f),detr(v))[0,1]) for k,v in [('x',x),('y',y),('background',bg)]}
 cut=B/tic/f's{cs}-tesscut.fits'
 with fits.open(cut) as h:
  print(sid,h[1].columns.names)
  w=WCS(h[2].header); pos=w.all_world2pix([[ra,dec]],0)[0]
  shape=h[1].data['FLUX'].shape
 out.append(dict(sample_id=sid,source_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),window_n=int(ok.sum()),correlations=corr,time_detrended_correlations=partial,cutout_sha256=hashlib.sha256(cut.read_bytes()).hexdigest(),cutout_sector=cs,target_xy_zero_index=pos.tolist(),flux_shape=shape))
(B/'helper-audit-numeric.json').write_text(json.dumps(out,indent=2)+'\n')
