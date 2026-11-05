import json
from pathlib import Path
import numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).parent;d=json.loads(Path('[local-path-redacted]').read_text());p=59.621102295409855;t0=1404.5;c=t0+43*p;print('prediction',c)
f=next(x for x in d['files'] if x['sector']==97)
with fits.open(f['path']) as h:
 a=h[1].data;t=np.array(a['TIME']);y=np.array(a['SAP_FLUX']);q=np.array(a['QUALITY']);ok=np.isfinite(t)&np.isfinite(y)&(y>0)&(q==0);t=t[ok];y=y[ok];ix=abs(t-c)<2;x=t[ix]-c;y=y[ix]; out={'prediction':c,'n':len(x),'first':float(x.min()) if len(x) else None,'last':float(x.max()) if len(x) else None,'core_n':int(sum(abs(x)<.2)),'left_n':int(sum((x>-.8)&(x<-.3))),'right_n':int(sum((x>.3)&(x<.8))),'maxgap':float(max(np.diff(x))) if len(x)>1 else None};print(out);(B/'helper-Q002-null.json').write_text(json.dumps(out,indent=2));fig,ax=plt.subplots(figsize=(9,3));ax.plot(x,y/np.median(y),'.',ms=2);ax.axvline(0,color='r');ax.grid();fig.tight_layout();fig.savefig(B/'helper-Q002-null.png')
