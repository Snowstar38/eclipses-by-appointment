from pathlib import Path
import json,numpy as np,matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from astropy.io import fits
R=Path(__file__).parent;D=json.load(open(R/'tesscut-downloads.json'));fig,axs=plt.subplots(5,2,figsize=(15,14));out=[]
for i,d in enumerate(D):
 p=R/d['tic']/d['members'][0]
 with fits.open(p) as h:
  a=h[1].data;t=np.array(a['TIME']);f=np.array(a['FLUX']);q=np.array(a['QUALITY']);b=np.nanmedian(np.sort(f.reshape(len(t),-1),axis=1)[:,:30],axis=1);f=f-b[:,None,None];y=np.sum(f[:,4:7,4:7],axis=(1,2));m=np.isfinite(t)&np.isfinite(y)&(q==0)&(y>0);t=t[m];y=y[m]/np.median(y[m])
 np.savez_compressed(R/d['tic']/('custom_s%03d.npz'%d['sector']),time=t,flux=y);ax=axs.flat[i];ax.plot(t,y,'.',ms=1);ax.set_title(d['tic']+' S'+str(d['sector']));ax.set_ylim(np.percentile(y,.2)-.005,np.percentile(y,99.8)+.005);out.append({'tic':d['tic'],'sector':d['sector'],'points':len(t),'method':'TESS FFI cutout; frame background lowest 30 pixel median; central 3x3 sum; QUALITY=0; independent extraction, same photons'})
fig.tight_layout();fig.savefig(R/'custom-morphology.png',dpi=120);json.dump(out,open(R/'custom-extraction.json','w'),indent=2)
