import json,math
from pathlib import Path
import numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).parent;d=json.loads(Path('[local-path-redacted]').read_text());p=46.13746894094549;t0=2194.214;out=[];pan=[]
for f in d['files']:
 with fits.open(f['path']) as h:
  a=h[1].data;t=np.array(a['TIME']);flux=np.array(a['SAP_FLUX']);q=np.array(a['QUALITY']);good=np.isfinite(t)&np.isfinite(flux)&(flux>0)&(q==0);t=t[good];flux=flux[good];
  for n in range(math.ceil((t.min()-t0-2)/p),math.floor((t.max()-t0+2)/p)+1):
   c=t0+n*p; ix=abs(t-c)<2; x=t[ix]-c;y=flux[ix];
   if len(x)<3:continue
   gap=float(max(np.diff(x))) if len(x)>1 else None; med=np.median(y);pan.append((f['sector'],c,x,y/med));out.append({'sector':f['sector'],'cycle':n,'prediction':c,'n':len(x),'relative_first':float(x.min()),'relative_last':float(x.max()),'max_gap':gap,'left_n':int(sum((x>=-2)&(x<-.9))),'core_n':int(sum(abs(x)<.4)),'right_n':int(sum((x>.9)&(x<=2)))})
fig,axs=plt.subplots(len(pan),1,figsize=(9,2.5*len(pan)),squeeze=False)
for ax,(sec,c,x,y) in zip(axs[:,0],pan):ax.plot(x,y,'.',ms=2);ax.axvline(0,color='r');ax.set_title(f's{sec} predicted {c:.3f}');ax.grid()
fig.tight_layout();fig.savefig(B/'helper-Q005-predictions.png');(B/'helper-Q005-predictions.json').write_text(json.dumps(out,indent=2));print(out)
