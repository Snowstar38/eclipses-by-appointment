import json,pathlib,hashlib,numpy as np,matplotlib
matplotlib.use('Agg');import matplotlib.pyplot as plt
from astropy.io import fits
B=pathlib.Path(r'[local-path-redacted]')
for tic,sec in [('317718737','033'),('317718737','087'),('390853987','086')]:
 d=json.loads((B/tic/'raw-fold.json').read_text());w=next(x for x in d['windows'] if x['kind']=='P' and x['sector']==sec);s=next(x for x in d['sectors'] if x['sector']==sec);p=pathlib.Path(s['path']);assert hashlib.sha256(p.read_bytes()).hexdigest()==s['sha256']
 with fits.open(p) as h:
  a=h[1].data; t=np.array(a['TIME']);q=np.array(a['QUALITY']);m=np.isfinite(t)&(q==0)&(abs(t-w['predicted_btjd'])<.5);t=t[m]; a=a[m]; cols=[c for c in ['SAP_FLUX','KSPSAP_FLUX','DET_FLUX','SYS_RM_FLUX','SAP_BKG','SAP_X','SAP_Y'] if c in a.names]
  fig,axs=plt.subplots(len(cols),1,figsize=(11,1.8*len(cols)),sharex=True)
  for ax,c in zip(axs,cols):
   y=np.asarray(a[c],float); good=np.isfinite(y);v=y[good];x=t[good]-w['predicted_btjd'];ax.plot(x,v,'.',ms=2);ax.axvspan(-w['duration']/2,w['duration']/2,alpha=.2,color='red');ax.set_ylabel(c)
  axs[0].set_title(f'{tic} sector {sec} BTJD {w["predicted_btjd"]:.5f}');fig.tight_layout();fig.savefig(B/tic/f'helper-detail-{sec}.png',dpi=140);plt.close(fig)
  print(tic,sec,s['sha256'])
