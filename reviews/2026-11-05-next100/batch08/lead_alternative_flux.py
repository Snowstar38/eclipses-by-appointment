import json
from pathlib import Path
import numpy as np
from astropy.io import fits
B=Path(__file__).resolve().parent
spec=[('270523058',82,3538.29584,.10,.12,.27),('295351347',99,4067.94,.10,.14,.28),('280051953',67,3137.07516,.65,1.4,2.4)]
out=[]
for tic,sec,c,hw,bl,bu in spec:
 s=next(x for x in json.loads((B/tic/'lead-context.json').read_text())['sectors'] if x['sector']==sec)
 with fits.open(s['source_path'],memmap=False) as h:
  a=h[1].data;t=np.array(a['TIME'],float);q=np.array(a['QUALITY'],int);names=h[1].columns.names
  for name in ['SAP_FLUX','DET_FLUX','DET_FLUX_SML','SYS_RM_FLUX','KSPSAP_FLUX']:
   if name not in names:continue
   f=np.array(a[name],float);g=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);tt=t[g];ff=f[g]
   core=abs(tt-c)<=hw;base=(abs(tt-c)>=bl)&(abs(tt-c)<=bu)
   if core.sum()<4 or base.sum()<4:continue
   baseline=np.median(ff[base]);depth=1000*(1-np.median(ff[core])/baseline)
   out.append(dict(tic=tic,sector=sec,center_btjd=c,flux_column=name,core_count=int(core.sum()),baseline_count=int(base.sum()),core_half_width_days=hw,baseline_inner_days=bl,baseline_outer_days=bu,median_core_deficit_ppt=float(depth),source_sha256=s['source_sha256']))
(B/'lead-alternative-flux.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
