from pathlib import Path
import numpy as np,pandas as pd
from astropy.io import fits
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
p=Path(__file__).resolve().parent
specs=[('52157743',44,(2505.5,2509.5),[(2505.5,2506.1),(2506.87,2506.96),(2508.7,2509.4)]),('218233922',42,(2454,2464),[(2454.5,2455.1),(2456.85,2457.0),(2461.3,2461.8),(2463.3,2463.9)])]
results=[]
for tic,sec,interval,wins in specs:
 a=fits.getdata(p/f'{tic}-{sec}.fits',1);t=a['TIME'];sap=a['SAP_FLUX'];bkg=a['SAP_BKG'];raw=sap+bkg;q=a['QUALITY'];m=np.isfinite(t)&np.isfinite(sap)&np.isfinite(bkg)&(t>interval[0])&(t<interval[1]);
 fig,ax=plt.subplots(3,1,figsize=(12,8),sharex=True,layout='constrained');
 for k,(y,label) in enumerate([(sap,'SAP_FLUX'),(bkg,'SAP_BKG'),(raw,'SAP_FLUX + SAP_BKG')]):
  good=m&(q==0);bad=m&(q!=0);ax[k].scatter(t[good],y[good],s=7,c='navy',label='QUALITY = 0');ax[k].scatter(t[bad],y[bad],s=7,c='darkorange',label='QUALITY != 0');ax[k].set_ylabel(label+'\n(e-/s)');ax[k].grid(alpha=.2)
  if tic=='218233922':ax[k].set_ylim(*[(-3000,2000),(-1000,9000),(-500,9000)][k])
  for x1,x2 in wins:ax[k].axvspan(x1,x2,color='gray',alpha=.12)
 ax[0].legend(loc='upper left');ax[0].set_title(f'TIC {tic}, sector {sec}: signed light-curve values; shaded measurement windows');ax[-1].set_xlabel('BTJD (days)');fig.savefig(p/f'{tic}-signed.png',dpi=150);plt.close(fig)
 for j,(lo,hi) in enumerate(wins):
  z=m&(t>=lo)&(t<=hi);results.append(dict(tic=tic,sector=sec,window=j+1,start_btjd=lo,end_btjd=hi,n=int(z.sum()),quality_nonzero=int(np.count_nonzero(q[z])),sap_median=float(np.median(sap[z])),bkg_median=float(np.median(bkg[z])),restored_median=float(np.median(raw[z]))))
 pd.DataFrame(dict(time=t[m],sap=sap[m],sap_bkg=bkg[m],restored=raw[m],quality=q[m])).to_csv(p/f'{tic}-signed.csv',index=False)
pd.DataFrame(results).to_csv(p/'measurements.csv',index=False);print(pd.DataFrame(results).to_string(index=False))
