import json,hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
B=Path(__file__).resolve().parent
out={}
for tic in ('351338696','320328447'):
 src=json.loads((B/tic/'raw-inspection.json').read_text())
 s=next(x for x in src['sectors'] if x.get('sector')==94)
 fp=Path(s['path']);assert hashlib.sha256(fp.read_bytes()).hexdigest()==s['sha256']
 with fits.open(fp,memmap=False) as h:
  a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
 good=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0)&(abs(t-3874.77)<2)
 t=t[good];f=f[good];base=np.median(f[(t<3873.5)|(t>3876)])
 out[tic]={'time':t,'flux':f/base,'n':len(t),'baseline':float(base)}
a,b=[out[x] for x in ('351338696','320328447')]
ix=(a['time']>=max(min(b['time']),3872.8))&(a['time']<=min(max(b['time']),3876.8))
times=a['time'][ix];av=a['flux'][ix];bv=np.interp(times,b['time'],b['flux'])
cor=float(np.corrcoef(av,bv)[0,1]);
bins=[]
for lo,hi in ((3873.5,3874.0),(3874.0,3874.5),(3874.5,3875.0),(3875.0,3875.5),(3875.5,3876.0)):
 m=(times>=lo)&(times<hi)
 bins.append({'lo':lo,'hi':hi,'n':int(sum(m)),'H031_ppt':float(1000*(np.median(av[m])-1)) if any(m) else None,'H040_ppt':float(1000*(np.median(bv[m])-1)) if any(m) else None})
res={'tic_pair':['351338696','320328447'],'sector':94,'window_btjd':[float(times.min()),float(times.max())],'n_overlap':len(times),'pearson_raw_normalized':cor,'half_day_bins':bins,'caution':'Two different targets share spacecraft times; raw correlation is diagnostic only and can include common trends. Coordinates are widely separated, and this does not itself identify the instrument mechanism.'}
(B/'common-event.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps(res,indent=2))
