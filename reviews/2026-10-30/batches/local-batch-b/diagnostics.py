import os,glob,json,numpy as np,matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from astropy.io import fits
r=os.path.dirname(__file__); s=json.load(open(r+'/selected.json')); search={str(x['tic']):x['P'] for x in s['search']}
for tic in ['295945076','451493289']:
 files=sorted(glob.glob(f'{r}/data/{tic}_s*.fits')); e=search[tic]; h=e['dur']/2; fig,ax=plt.subplots(len(files),1,figsize=(8,1.6*len(files)),sharex=True,squeeze=False)
 for a,path in zip(ax[:,0],files):
  with fits.open(path,memmap=False) as hd:
   d=hd[1].data;t=np.array(d['TIME'],float);f=np.array(d['SAP_FLUX'],float);q=np.array(d['QUALITY'])
  phase=(t-e['t0']+e['P']/2)%e['P']-e['P']/2; good=np.isfinite(t)&np.isfinite(f); norm=np.nanmedian(f[good&(abs(phase)>h)&(abs(phase)<5*h)&(q==0)]); sel=good&(abs(phase)<5*h)
  a.axvspan(-h,h,color='gold',alpha=.22); a.axvspan(-3*h,-h,color='skyblue',alpha=.15);a.axvspan(h,3*h,color='skyblue',alpha=.15);a.axvspan(-5*h,-3*h,color='grey',alpha=.12);a.axvspan(3*h,5*h,color='grey',alpha=.12)
  a.scatter(phase[sel&(q==0)],1000*(f[sel&(q==0)]/norm-1),s=3,c='black',alpha=.35);a.scatter(phase[sel&(q!=0)],1000*(f[sel&(q!=0)]/norm-1),s=7,c='red',alpha=.6); a.set_ylabel(os.path.basename(path).split('_s')[1][:3]+'\nppt');a.grid(alpha=.15)
 ax[-1,0].set_xlabel('Time from search center (days); gold box, blue near, grey wide; red flagged'); fig.suptitle('TIC '+tic+' raw SAP, normalized per sector'); fig.tight_layout();fig.savefig(f'{r}/diagnostic_{tic}.png',dpi=130);plt.close(fig)
