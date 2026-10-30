import json,pathlib,numpy as np,matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.wcs import WCS
from astropy.coordinates import SkyCoord
import astropy.units as u
r=pathlib.Path(__file__).parent;T=json.load(open(r.parent/'targets-selected.json'));res=json.load(open(r/'pixel-results.json'));dl=json.load(open(r/'tesscut-downloads.json'));allres=[]
for x in res:
 if x.get('error'):continue
 tic=x['tic'];sec=x['sector'];target=T[tic];d=next(d for d in dl if d['tic']==tic and d['sector']==sec);h=fits.open(r/tic/d['members'][0]);w=WCS(h[2].header);h.close();arr=np.load(r/tic/f'pixel_s{sec:03d}.npz');O=arr['out'];Z=arr['deficit'];fig,ax=plt.subplots(1,2,figsize=(11,5));lims=np.nanpercentile(abs(Z),99);ax[0].imshow(O,origin='lower');im=ax[1].imshow(Z,origin='lower',cmap='RdBu_r',vmin=-lims,vmax=lims);fig.colorbar(im,ax=ax[1]);depth=x['depth_3x3']; nbs=[]
 for nb in json.load(open(r/tic/'tic-cone.json'))['data']:
  if str(nb['ID'])==tic or nb.get('Tmag') is None or target.get('Tmag') is None:continue
  fr=10**(-.4*(nb['Tmag']-target['Tmag']));need=depth*(1+fr)/fr;px,py=w.all_world2pix(nb['ra'],nb['dec'],0);px=float(px);py=float(py);sep=float(SkyCoord(target['ra']*u.deg,target['dec']*u.deg).separation(SkyCoord(nb['ra']*u.deg,nb['dec']*u.deg)).arcsec)
  if need>1:continue
  nbs.append(dict(tic=nb['ID'],gaia_dr2=nb['GAIA'],Tmag=nb['Tmag'],separation_arcsec=sep,depth_needed=need,px=[px,py]));
  for a in ax:a.plot(px,py,'wx',ms=8,mew=1.5);a.annotate(str(nb['ID']),[px,py],color='white',fontsize=6)
 for a in ax:a.plot(*x['target_px'],'g+',ms=15,mew=2);a.set_xlabel('pixel x');a.set_ylabel('pixel y');a.set_xlim(-.5,10.5);a.set_ylim(-.5,10.5)
 ax[0].set_title('Out of eclipse');ax[1].set_title('Signed out minus in');fig.suptitle(f'TIC {tic} sector {sec}; target green +; TIC capable neighbours white x');fig.tight_layout();fig.savefig(r/tic/f'terra_pixel_s{sec:03d}.png',dpi=120);plt.close(fig);allres.append(dict(tic=tic,sector=sec,depth_3x3=depth,capable_neighbours=nbs,note='TIC cone 60 arcsec; apparent Tmag-based ideal total-eclipse limit neglects aperture throughput and bandpass uncertainty. Uncatalogued sources possible.'))
json.dump(allres,open(r/'terra-neighbour-results.json','w'),indent=2);print([(x['tic'],x['sector'],len(x['capable_neighbours'])) for x in allres])

