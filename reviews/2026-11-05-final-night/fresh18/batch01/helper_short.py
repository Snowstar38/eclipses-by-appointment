import requests,zipfile,io,json,hashlib,csv
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent; pop=json.loads((B.parent.parent/'fresh-band-next400'/'population.json').read_text())['targets']; out=[]
for tic,sec,epoch,period,nid in [('65684549',59,2935.3667933,1.137190622,'476202682177725184'),('122766753',59,1821.3013817,2.209276574,'201206302856438528')]:
 p=pop[tic]; path=B/tic/f'helper-short-cut-s{sec}.fits'
 if not path.exists():
  r=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/astrocut',params={'ra':p['ra'],'dec':p['dec'],'x':7,'y':7,'units':'px','sector':sec},timeout=100);r.raise_for_status(); z=zipfile.ZipFile(io.BytesIO(r.content));path.write_bytes(z.read(z.namelist()[0])); url=r.url
 else:url='cached'
 rows=list(csv.DictReader((B/tic/'gaia-neighbors.csv').open())); nb=next(r for r in rows if r['source_id']==nid)
 with fits.open(path) as h:
  a=h[1].data;t=np.array(a['TIME']);q=np.array(a['QUALITY']); f=np.array(a['FLUX']);w=WCS(h[2].header);target=w.all_world2pix([[p['ra'],p['dec']]],0)[0]; neighbor=w.all_world2pix([[float(nb['ra']),float(nb['dec'])]],0)[0]
 phase=(t-epoch+period/2)%period-period/2;ok=(q==0)&np.isfinite(t);inside=ok&(abs(phase)<.035);base=ok&(abs(phase)>.12)&(abs(phase)<.30)
 diff=np.nanmedian(f[base],axis=0)-np.nanmedian(f[inside],axis=0);med=np.nanmedian(f[base],axis=0);border=np.concatenate([diff[0],diff[-1],diff[1:-1,0],diff[1:-1,-1]]); diff-=np.nanmedian(border)
 fig,ax=plt.subplots(1,2,figsize=(9,4));
 for a,img,title in zip(ax,[med,diff],['baseline','phase-folded difference, border-subtracted']):
  im=a.imshow(img,origin='lower');fig.colorbar(im,ax=a);a.plot(*target,'rx',ms=12,mew=2);a.plot(*neighbor,'c+',ms=12,mew=2);a.grid(alpha=.3);a.set_title(title)
 fig.suptitle(f'{tic} S{sec}, red target, cyan neighbor');fig.tight_layout();fig.savefig(B/tic/f'helper-short-diff-s{sec}.png',dpi=150);plt.close(fig)
 cut=diff[1:6,1:6]; yy,xx=np.indices(diff.shape);ww=np.maximum(diff,0);ww[:1]=0;ww[6:]=0;ww[:,:1]=0;ww[:,6:]=0;centroid=[float((ww*xx).sum()/ww.sum()),float((ww*yy).sum()/ww.sum())]
 out.append(dict(tic=tic,sector=sec,url=url,sha256=hashlib.sha256(path.read_bytes()).hexdigest(),target_xy=target.tolist(),neighbor_xy=neighbor.tolist(),centroid_positive_5x5=centroid,peak_xy=list(map(int,np.unravel_index(np.nanargmax(diff),diff.shape)[::-1])),inside=int(inside.sum()),baseline=int(base.sum()),period=period,epoch=epoch,border_subtracted_difference=diff.tolist(),note='Median phase-stack spans multiple same-sector events; same photons. Centroid heuristic, not PRF fit. Gaia G ratio does not equal TESS aperture response.'))
(B/'helper-short-receipts.json').write_text(json.dumps(out,indent=2));print(json.dumps([{k:v for k,v in o.items() if k!='border_subtracted_difference'} for o in out],indent=2))
