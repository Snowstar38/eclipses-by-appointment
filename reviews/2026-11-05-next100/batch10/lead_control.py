import json,numpy as np,matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from astropy.io import fits
from pathlib import Path
B=Path(__file__).parent; fig,ax=plt.subplots(figsize=(12,5));out=[]
for tic in ['311461544','341005134','340968888']:
 s=next(x for x in json.loads((B/tic/'lead-context.json').read_text())['sectors'] if x['sector']==101)
 with fits.open(s['source_path']) as h:
  a=h[1].data;t=np.array(a['TIME']);f=np.array(a['SAP_FLUX']);q=np.array(a['QUALITY']);m=(t>4111.3)&(t<4113.3)&(q==0)&np.isfinite(f)&(f>0);t=t[m];f=f[m];f=f/np.median(f[(t>4111.4)&(t<4111.7)])
 ax.plot(t,f,'.',ms=2,label=tic);out.append({'tic':tic,'time':t.tolist(),'normalized':f.tolist()})
ax.legend();ax.set_xlabel('BTJD');ax.set_ylabel('SAP / early median');fig.savefig(B/'lead-S101-control.png',dpi=140);(B/'lead-S101-control.json').write_text(json.dumps(out,separators=(',',':')))
