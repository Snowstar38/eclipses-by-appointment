import pathlib,numpy as np,pandas as pd,json,hashlib
from astropy.io import fits
from astropy.wcs import WCS
from scipy.ndimage import gaussian_filter1d
from scipy.signal import find_peaks
from scipy.optimize import least_squares
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
p=pathlib.Path(__file__).parent
with fits.open(p/'tp.fits') as h:
 t=h[1].data['TIME'].copy(); q=h[1].data['QUALITY'].copy(); cube=h[1].data['FLUX'].copy(); bg=h[1].data['FLUX_BKG'].copy(); mask=h[2].data.copy();w=WCS(h[2].header)
with fits.open(p/'lc.fits') as h:
 d=h[1].data; y=d['PDCSAP_FLUX'].copy(); b=d['SAP_BKG'].copy(); cx=d['MOM_CENTR1'].copy();cy=d['MOM_CENTR2'].copy();pc1=d['POS_CORR1'].copy();pc2=d['POS_CORR2'].copy()
valid=(q==0)&np.isfinite(t)&np.isfinite(y); yy=y/np.nanmedian(y[valid])-1
# Find dips from lightly smoothed flux, clean cadences only, ignore deep complex event.
z=np.where(valid,yy,np.nan); z=pd.Series(z).interpolate(limit_direction='both').to_numpy(); sm=gaussian_filter1d(z,3)
idx,_=find_peaks(-sm,height=.018,distance=400,prominence=.015)
centers=[float(t[i]) for i in idx if not (2916.9<t[i]<2918.5) and abs(yy[i])<.10]
print('centers',centers)
ra,dec=72.6639595885975,40.85798381916; tx,ty=w.world_to_pixel_values(ra,dec); print('targetxy',tx,ty)
g=pd.read_csv(p/'gaia.csv',dtype={'source_id':str}).sort_values('sep'); print(g.head(8).to_string(index=False))
# shallow samples: mean local adjacent baseline to suppress variability; each event same window.
shallow=[]; counts=[]
for c in centers:
 dtime=t-c; inside=valid&(abs(dtime)<.035); left=valid&(dtime>-.15)&(dtime<-.09); right=valid&(dtime>.09)&(dtime<.15)
 if min(inside.sum(),left.sum(),right.sum())<12:continue
 shallow.append((np.nanmedian(cube[left],axis=0)+np.nanmedian(cube[right],axis=0))/2-np.nanmedian(cube[inside],axis=0));counts.append(c)
inside=valid&(t>2917.54)&(t<2917.93); left=valid&(t>2917.0)&(t<2917.25); right=valid&(t>2918.25)&(t<2918.5)
deep=(np.nanmedian(cube[left],axis=0)+np.nanmedian(cube[right],axis=0))/2-np.nanmedian(cube[inside],axis=0)
sh=np.nanmedian(shallow,axis=0)
Y,X=np.indices(sh.shape)
def fit(im):
 # weighted Gaussian template with free circular scale + constant; descriptive not calibrated PRF
 z=np.nan_to_num(im,nan=0); a=np.unravel_index(np.argmax(z),z.shape); init=[z.max(),float(a[1]),float(a[0]),1.,0.]
 def resid(v):
  A,x,y,s,b=v; return (A*np.exp(-((X-x)**2+(Y-y)**2)/(2*s*s))+b-z).ravel()
 r=least_squares(resid,init,bounds=([0,-1,-1,.2,-np.inf],[np.inf,12,12,5,np.inf])); return r.x.tolist()
fits_={'shallow':fit(sh),'deep':fit(deep)};print('fits',fits_)
fig,axes=plt.subplots(1,3,figsize=(14,4.6)); ref=np.nanmedian(cube[valid],axis=0)
for ax,im,name in zip(axes,[ref,sh,deep],['Median calibrated flux','Shallow local difference','Deep event difference']):
 v=ax.imshow(im,origin='lower',cmap='viridis'); fig.colorbar(v,ax=ax,shrink=.8);ax.plot(tx,ty,'r+',ms=12,mew=2,label='TIC position')
 for r in g[g.sep<70].itertuples():
  x,y0=w.world_to_pixel_values(r.ra,r.dec)
  if 0<=x<11 and 0<=y0<11:ax.plot(x,y0,'wx',ms=5);ax.text(x+.1,y0+.1,f'{r.phot_g_mean_mag:.1f}',color='white',fontsize=7)
 ax.set_title(name);ax.set_xlabel('column');ax.set_ylabel('row')
fig.tight_layout();fig.savefig(p/'difference.png',dpi=180)
for name,ins,base in [('deep',inside,left|right)]:
 print(name,'quality',np.unique(q[(t>2917.3)&(t<2918.2)],return_counts=True));
 for k,v in [('background',b),('centroid_x',cx),('centroid_y',cy),('pos1',pc1),('pos2',pc2)]:print(k,float(np.nanmedian(v[ins])-np.nanmedian(v[base])))
summary={'sha256':{fn:hashlib.sha256((p/fn).read_bytes()).hexdigest() for fn in ['tp.fits','lc.fits']},'shallow_centers':counts,'target_xy':[float(tx),float(ty)],'gaussian_fit_amp_x_y_sigma_offset':fits_,'deep_windows':{'in':[2917.54,2917.93],'out':[[2917,2917.25],[2918.25,2918.5]]},'deep_cadences':int(inside.sum()),'quality_zero_only_images':True,'warning':'Gaussian descriptive centroid is not an empirical PRF fit; systematic and centroid uncertainty not computed.'}
(p/'evidence.json').write_text(json.dumps(summary,indent=2))
