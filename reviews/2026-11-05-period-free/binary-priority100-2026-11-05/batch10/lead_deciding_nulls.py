"""Visual context for the alias nulls that decide shorter harmonics."""
import csv,json,hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent
spec={'T091':[(26,2025.2678,.27)],'T093':[(11,1619.2133,2.44),(64,3062.9925,2.44)],'T095':[(48,2631.0388,1.8)],'T096':[(43,2495.6249,.34)],'T097':[],'T098':[(18,1812.8054,1.14)]}
# T097 chooses the first actual sensitive null for its 36-cycle shorter alias.
a=json.loads((B/'lead-alias.json').read_text())
z=next(v for v in a['T097']['trials'] if v['cycles_between']==36)
spec['T097']=[(x['sector'],x['center'],1.5) for x in z['checks'] if x['sensitive'] and x['observed_depth']<.077][:1]
rows={r['sample_id']:r for r in csv.DictReader((B/'queue.csv').open())}
for sid,events in spec.items():
 m=json.loads((B/rows[sid]['tic']/'lead-numeric.json').read_text());fig,axs=plt.subplots(len(events),1,figsize=(8,2.8*len(events)),squeeze=False)
 for ax,(sec,center,dur) in zip(axs[:,0],events):
  src=next(x for x in m['sources'] if x['sector']==sec);p=Path(src['path']);assert hashlib.sha256(p.read_bytes()).hexdigest()==src['sha256']
  with fits.open(p,memmap=False) as h:
   f=h[1].data;t=np.array(f['TIME'],float);v=np.array(f['SAP_FLUX'],float);q=np.array(f['QUALITY'],int)
  sel=np.isfinite(t)&np.isfinite(v)&(v>0)&(q==0)&(abs(t-center)<2.5*dur);t=t[sel];v=v[sel];base=np.median(v)
  ax.plot(t-center,v/base,'.',ms=2);ax.axvspan(-dur/2,dur/2,color='salmon',alpha=.2);ax.axvline(0,color='gray');ax.set_title(f'{sid} s{sec} predicted alias at BTJD {center:.4f}');ax.set_xlabel('days from prediction');ax.set_ylabel('raw SAP / local median')
 fig.tight_layout();fig.savefig(B/f'lead-deciding-null-{sid}.png',dpi=130);plt.close(fig)
