"""Plot predicted occasions from raw SAP for visual validation of recurrence audit."""
import json,hashlib,math
from pathlib import Path
import numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent
for tic in ('398073873','143497778'):
 d=B/tic;rec=json.loads((d/'lead-recurrence.json').read_text());ctx=json.loads((d/'lead-context.json').read_text())
 rows=[x for x in rec['occasions'] if x['sensitive']]
 fig,axs=plt.subplots(math.ceil(len(rows)/2),2,figsize=(11,2.4*math.ceil(len(rows)/2)),squeeze=False)
 for ax,z in zip(axs.ravel(),rows):
  s=next(x for x in ctx['sectors'] if x['sector']==z['sector']);fp=Path(s['source_path']);assert hashlib.sha256(fp.read_bytes()).hexdigest()==s['source_sha256']
  with fits.open(fp,memmap=False) as h:
   a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
  good=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[good];f=f[good]
  c=z['predicted_btjd'];rad=.30 if tic=='398073873' else .75;win=np.abs(t-c)<rad;x=t[win]-c;y=f[win]/np.median(f[win]);ax.plot(x,y,'.',ms=2)
  ax.axvline(0,c='red',lw=.6);ax.set_title(f"S{z['sector']} n={z['cycle']} depth={z['local_depth_ppt']:.1f} ppt",fontsize=9)
  ax.set_ylabel('SAP / local median')
 for ax in axs.ravel()[len(rows):]:ax.axis('off')
 fig.tight_layout();fig.savefig(d/'lead-recurrence.png',dpi=130);plt.close(fig)
