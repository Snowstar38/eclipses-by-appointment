import csv,json,hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent
for q in csv.DictReader((B/'queue.csv').open()):
 tic=q['tic'];r=json.loads((B/tic/'raw-inspection.json').read_text());wins=r['representative_flagged_windows'];
 if not wins:continue
 w=next((x for x in wins if x['kind']=='dip'),wins[0]);sector=w['sector'];mid=w['screen_center_btjd'];span=max(3,2*w['screen_duration_days'])
 s=next(x for x in r['sectors'] if x['sector']==sector);p=Path(s['path']);assert hashlib.sha256(p.read_bytes()).hexdigest()==s['sha256']
 with fits.open(p,memmap=False) as h:
  a=h[1].data;t=np.asarray(a['TIME'],float);Q=np.asarray(a['QUALITY'],int);names=a.names
  cols={k:np.asarray(a[k],float) for k in ['SAP_FLUX','KSPSAP_FLUX','SAP_BKG','SAP_X','SAP_Y'] if k in names}
 ok=np.isfinite(t)&(Q==0)&(abs(t-mid)<span)
 fig,axes=plt.subplots(len(cols),1,figsize=(9,1.7*len(cols)),sharex=True)
 out={'tic':tic,'sector':sector,'screen_center_btjd':mid,'fits_sha256':s['sha256'],'columns':list(cols),'bins':[]}
 for ax,(name,f) in zip(axes,cols.items()):
  m=ok&np.isfinite(f);norm=np.median(f[m&((t<mid-.8)|(t>mid+.8))]) if 'FLUX' in name else 1
  ax.plot(t[m],f[m]/norm,'.',ms=2);ax.set_ylabel(name)
 axes[-1].set_xlabel('BTJD');fig.tight_layout();fig.savefig(B/tic/'qlp-alternate.png',dpi=120);plt.close(fig)
 for lo,hi in [(mid-2,mid-1),(mid-1,mid-.5),(mid-.5,mid),(mid,mid+.5),(mid+.5,mid+1),(mid+1,mid+2)]:
  m=ok&(t>=lo)&(t<hi);out['bins'].append({'start':lo,'end':hi,'n':int(sum(m)),**{k:float(np.median(v[m])) if m.any() else None for k,v in cols.items()}})
 (B/tic/'qlp-alternate.json').write_text(json.dumps(out,indent=2)+'\n')
 print(tic,sector,','.join(cols),flush=True)
