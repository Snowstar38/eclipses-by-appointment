import json,hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent
for tic,sector,mid,half in [('454228598',12,1625.85,2),('372989764',66,3114.25,2),('351338696',94,3874.77,2),('320328447',94,3874.77,2)]:
 rec=next(s for s in json.loads((B/tic/'raw-inspection.json').read_text())['sectors'] if s['sector']==sector)
 fp=Path(rec['path']);assert hashlib.sha256(fp.read_bytes()).hexdigest()==rec['sha256']
 with fits.open(fp,memmap=False) as h:
  a=h[1].data
  t=np.asarray(a['TIME'],float);q=np.asarray(a['QUALITY'],int)
  cols={k:np.asarray(a[k],float) for k in ('SAP_FLUX','KSPSAP_FLUX','SAP_BKG','SAP_X','SAP_Y') if k in a.names}
 ok=np.isfinite(t)&(q==0)&(abs(t-mid)<half)
 for k in cols:ok &= np.isfinite(cols[k])
 t=t[ok]
 for k in cols:cols[k]=cols[k][ok]
 fig,axes=plt.subplots(len(cols),1,figsize=(10,1.6*len(cols)),sharex=True)
 for ax,(k,y) in zip(axes,cols.items()):
  if 'FLUX' in k:y=y/np.median(y[(t<mid-1)|(t>mid+1)])
  ax.plot(t,y,'.',ms=2);ax.set_ylabel(k)
 axes[-1].set_xlabel('BTJD');fig.tight_layout();fig.savefig(B/tic/f'alternate-s{sector}.png',dpi=130);plt.close(fig)
 def med(k,lo,hi):
  y=cols[k];return float(np.median(y[(t>=lo)&(t<hi)]))
 bins=[(mid-1.2,mid-.7),(mid-.7,mid-.2),(mid-.2,mid+.3),(mid+.3,mid+.8),(mid+.8,mid+1.3)]
 out={'tic':tic,'sector':sector,'input_fits':str(fp),'fits_sha256':rec['sha256'],'bins':[{'start':x,'end':y,'n':int(sum((t>=x)&(t<y))),**{k:med(k,x,y) for k in cols}} for x,y in bins],'caution':'KSPSAP is a pipeline alternate reduction of the same TESS photons, not a separate observing occasion. Bin medians are descriptive, not eclipse fits.'}
 (B/tic/f'alternate-s{sector}.json').write_text(json.dumps(out,indent=2)+'\n')
 print(tic,sector,[(round(b['start'],2),b['n'],round(b['SAP_FLUX']/out['bins'][0]['SAP_FLUX']-1,4),round(b['KSPSAP_FLUX']/out['bins'][0]['KSPSAP_FLUX']-1,4) if 'KSPSAP_FLUX' in b else None) for b in out['bins']])
