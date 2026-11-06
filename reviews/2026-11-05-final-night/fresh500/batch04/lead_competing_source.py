import numpy as np,json
from pathlib import Path
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
b=Path(__file__).resolve().parent;d=b/'309259409';r=json.load(open(d/'helper-localization.json'));c=r['event']['center_btjd'];dur=r['event']['duration_d']
with fits.open(d/'helper-tesscut.fits') as h:t=np.array(h[1].data['TIME']);q=np.array(h[1].data['QUALITY']);cube=np.array(h[1].data['FLUX'])
g=(q==0)&np.isfinite(t)&(abs(t-c)<2);x=t[g]-c;cube=cube[g];core=abs(x)<dur*.25;side=(abs(x)>dur*.75)&(abs(x)<dur*2)
fig,axs=plt.subplots(3,1,figsize=(10,7));out=[]
for ax,(label,px,py) in zip(axs,[('target peak',3,4),('north deficit',2,6),('north neighbor lower pixel',2,5)]):
 y=cube[:,py,px];base=np.median(y[side]);z=y/base;loss=1-np.median(z[core]);out.append(dict(label=label,xy=[px,py],baseline_e_s=float(base),loss=float(loss)));ax.plot(x,z,'.',ms=2);ax.set_title(f'{label} fractional loss{loss:.4f}');ax.grid(alpha=.2)
fig.tight_layout();fig.savefig(d/'lead-competing-source.png',dpi=120);(d/'lead-competing-source.json').write_text(json.dumps(out,indent=2));print(out)
