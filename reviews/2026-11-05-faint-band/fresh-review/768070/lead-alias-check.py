import json
from pathlib import Path
import numpy as np
from astropy.io import fits
B=Path(__file__).resolve().parent
period=4299.277462500361-4247.129649643252
tests=[('half',4247.129649643252+period/2),('third-1',4247.129649643252+period/3),('third-2',4247.129649643252+2*period/3)]
out=[]
for label,pred in tests:
 sec=107
 with fits.open(B/f'lead-extra-s{sec}.fits') as h:
  a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['FLUX'],float);q=np.asarray(a['QUALITY'],int)
 sky=np.nanmedian(f[:,[0,0,4,4],[0,4,0,4]],axis=1);y=np.nansum(f[:,1:4,1:4],axis=(1,2))-9*sky
 ok=np.isfinite(t)&np.isfinite(y)&(y>0)&(q==0);t=t[ok];y=y[ok]
 core=np.abs(t-pred)<.14;left=(t>pred-.6)&(t<pred-.25);right=(t>pred+.25)&(t<pred+.6)
 # linear baseline through left/right medians to remove S107 smooth trend
 tl=np.median(t[left]);tr=np.median(t[right]);fl=np.median(y[left]);fr=np.median(y[right]);baseline=fl+(fr-fl)*(t-tl)/(tr-tl)
 ratio=y/baseline
 d=dict(label=label,sector=sec,predicted_btjd=pred,core_n=int(core.sum()),left_n=int(left.sum()),right_n=int(right.sum()),first_core_btjd=float(t[core].min()),last_core_btjd=float(t[core].max()),max_core_gap_d=float(np.diff(t[core]).max()),median_core_depth_ppt=float((1-np.median(ratio[core]))*1000),min_core_depth_ppt=float((1-np.min(ratio[core]))*1000),local_scatter_ppt=float(1.4826*np.median(np.abs(ratio[left|right]-np.median(ratio[left|right])))*1000))
 out.append(d);print(label,round(pred,4),d['median_core_depth_ppt'],d['core_n'])
(B/'lead-alias-check.json').write_text(json.dumps(out,indent=2),encoding='utf8')
