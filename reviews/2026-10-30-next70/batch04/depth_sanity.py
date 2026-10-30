from pathlib import Path
import json,numpy as np,urllib.request,urllib.parse,hashlib
from astropy.io import fits
from astropy.wcs import WCS
B=Path(__file__).parent;R=B/'raw-evidence';tic='364120441';T=json.loads((B/'targets-selected.json').read_text())[tic];ep=json.loads((R/'raw-events.json').read_text())[tic]['representative_ephemeris'];events=json.loads((R/'independent-results.json').read_text());rec=next(x for x in events if x['tic']==tic)
uri=next(x[1] for x in T['qlp'] if x[0]==20);p=R/tic/'qlp_s020.fits'
if not p.exists():p.write_bytes(urllib.request.urlopen('https://mast.stsci.edu/api/v0.1/Download/file?'+urllib.parse.urlencode({'uri':uri}),timeout=60).read())
dur=np.median([x['duration_d'] for x in json.loads((R/'raw-events.json').read_text())[tic]['events'] if 'tc'in x])
def measure(t,f):
 out=[]
 for e in rec['measurements']:
  dt=t-e['tc'];mi=abs(dt)<.3*dur;pre=(dt<-.75*dur)&(dt>-1.75*dur);post=(dt>.75*dur)&(dt<1.75*dur);base=(np.median(f[pre])+np.median(f[post]))/2
  out.append(dict(tc=e['tc'],baseline=float(base),depth_core=float(1-np.median(f[mi])/base),depth_deepest3=float(1-np.median(np.sort(f[mi])[:3])/base),core_samples=int(mi.sum())))
 return out
with fits.open(p) as h:
 assert str(h[0].header['TICID'])==tic and h[0].header['SECTOR']==20
 a=h[1].data;m=(a['QUALITY']==0)&np.isfinite(a['SAP_FLUX']);qlp=measure(a['TIME'][m],a['SAP_FLUX'][m]);cols=h[1].columns.names
with fits.open(rec['source_path']) as h:
 a=h[1].data;F=np.array(a['FLUX']);t=np.array(a['TIME']);m=(a['QUALITY']==0)&np.isfinite(t)&np.all(np.isfinite(F.reshape(len(t),-1)),axis=1);F=F[m];t=t[m];bg=np.median(np.sort(F.reshape(len(t),-1),axis=1)[:,:90],axis=1);x,y=WCS(h[2].header).all_world2pix(float(T['gaia']['ra']),float(T['gaia']['dec']),0);ix,iy=round(float(x)),round(float(y));aps={}
 for half in [0,1,2]:
  f=F[:,iy-half:iy+half+1,ix-half:ix+half+1].sum(axis=(1,2))-(2*half+1)**2*bg;aps[str(2*half+1)+'x'+str(2*half+1)]=measure(t,f)
d=json.loads((R/tic/'diff_s20.json').read_text());result=dict(tic=tic,sector=20,qlp_uri=uri,qlp_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),qlp_columns=cols,qlp_same_epoch=qlp,pixel_same_epoch=aps,primary_period=ep['period_d'],duration_d=dur,source_target_px=d['target_px'],deficit_centroid=d['deficit_centroid'],capable_neighbour=d['brightest_neighbour_60'],target_Tmag=T['Tmag'],target_G=T['gaia'].get('phot_g_mean_mag'))
(B/'depth-sanity-364120441.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
