from pathlib import Path
import hashlib,json
import numpy as np
from astropy.io import fits
from astropy.timeseries import LombScargle
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent
D=Path('[local-path-redacted]')
specs=[(41975422,69,[(3191.6,3192),(3193.15,3193.3),(3195.2,3195.3),(3204.8,3205.2),(3206.4,3206.55)]),(198279430,17,[(1773.5,1774),(1775.1,1775.5)]),(198279430,84,[(3584,3585),(3586,3586.3),(3597,3598),(3598.9,3599.2)]),(288157030,87,[(3676.243502617746,3676.4435026177457),(3676.6564644697473,3676.856464469747)]),(100938468,88,[(3703.692943343204,3703.892943343204),(3704.103593687798,3704.3035936877977)])]
out={'method':'quality==0 finite values; medians in BTJD intervals; QLP SAP_FLUX is already normalized. Background values in file units; association alone does not prove mechanism.','windows':[],'periodograms':[],'sources':[]}
for tic,sec,windows in specs:
 p=D/f'{tic}_s{sec:03}.fits';out['sources'].append({'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
 with fits.open(p,memmap=False) as h:
  d=h[1].data;t=np.array(d['TIME']);q=np.array(d['QUALITY'])
  for a,b in windows:
   s=(t>a)&(t<b)&(q==0);item={'tic':tic,'sector':sec,'start':a,'end':b,'n':int(sum(s))}
   for col in ['SAP_FLUX','SAP_X','SAP_Y','SAP_BKG']:item[col]=float(np.nanmedian(d[col][s]))
   out['windows'].append(item)
  if tic==41975422:
   f=np.array(d['SAP_FLUX']);good=np.isfinite(t)&np.isfinite(f)&(f>0);f=f/np.median(f[good&(q==0)]);fig,axs=plt.subplots(2,1,figsize=(12,6))
   for ax,c in zip(axs,[3193.3,3206.55]):
    s=good&(abs(t-c)<2);ax.plot(t[s],f[s],'.',ms=2);ax.plot(t[s&(q!=0)],f[s&(q!=0)],'rx',ms=2);ax.set_ylim(.85,1.08);ax.set_xlabel('BTJD');ax.set_ylabel('SAP / median');ax.grid()
   fig.tight_layout();fig.savefig(B/'helper-T052-gaps.png',dpi=150);plt.close(fig)
for sec in [11,37,64,99,100,101]:
 p=D/f'180177949_s{sec:03}.fits';out['sources'].append({'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
 with fits.open(p,memmap=False) as h:
  d=h[1].data;t=np.array(d['TIME']);f=np.array(d['SAP_FLUX']);q=np.array(d['QUALITY']);s=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[s];f=f[s];freq,power=LombScargle(t,f/np.median(f)).autopower(minimum_frequency=.2,maximum_frequency=5,samples_per_peak=8);k=np.argmax(power)
  out['periodograms'].append({'sector':sec,'n':len(t),'start':float(t.min()),'end':float(t.max()),'period_days_grid_peak':float(1/freq[k]),'power':float(power[k])})
(B/'helper-audit-numerics.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
