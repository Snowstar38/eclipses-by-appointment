import numpy as np,json,hashlib
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
B=Path(__file__).resolve().parent;pop=json.loads((B.parent/'fresh-band'/'population.json').read_text())['targets']
items=[('259614821',38,2339.507,.06,.25,.48),('371856921',23,1951.953,.04,.20,.45),('412521418',34,2231.994,.035,.20,.33),('86182628',49,2662.044,.04,.25,.45),('26486304',81,3527.585,.10,.35,.60),('26486304',81,3514.460,.10,.35,.60),('356801225',81,3526.698,.07,.25,.45),('331643517',56,2829.840,.025,.12,.22),('343187602',24,1970.092,.025,.15,.30)]
nb={'412521418':(110.76825,-22.27438),'356801225':(286.48935,16.76372)};out=[]
for tic,sec,c,iw,b0,b1 in items:
 p=B/tic/f'helper-cut-s{sec}.fits';d=pop[tic]
 if not p.exists(): continue
 with fits.open(p) as h:
  a=h[1].data;t=np.array(a['TIME']);q=np.array(a['QUALITY']);f=np.array(a['FLUX']);w=WCS(h[2].header);xy=w.all_world2pix([[d['ra'],d['dec']]],0)[0];nxy=w.all_world2pix([nb[tic]],0)[0] if tic in nb else None
 ok=(q==0)&np.isfinite(t); inn=ok&(abs(t-c)<iw); base=ok&(abs(t-c)>b0)&(abs(t-c)<b1)
 diff=np.nanmedian(f[base],axis=0)-np.nanmedian(f[inn],axis=0); med=np.nanmedian(f[base],axis=0)
 fig,ax=plt.subplots(1,2,figsize=(9,4)); im=ax[0].imshow(med,origin='lower');fig.colorbar(im,ax=ax[0]); im=ax[1].imshow(diff,origin='lower');fig.colorbar(im,ax=ax[1]);
 for a in ax:
  a.plot(*xy,'rx',ms=12,mew=2)
  if nxy is not None:a.plot(*nxy,'c+',ms=12,mew=2)
  a.set_xticks(range(7));a.set_yticks(range(7));a.grid(alpha=.3)
 ax[0].set_title('baseline; red target, cyan EA');ax[1].set_title('baseline minus event');fig.suptitle(f'{tic} S{sec} BTJD {c}');fig.tight_layout();img=B/tic/f'helper-diff-s{sec}-{c:.0f}.png';fig.savefig(img,dpi=140);plt.close(fig)
 r=dict(tic=tic,sector=sec,center_btjd=c,n_in=int(inn.sum()),n_baseline=int(base.sum()),target_xy=xy.tolist(),neighbor_xy=nxy.tolist() if nxy is not None else None,peak_diff_xy=list(map(int,np.unravel_index(np.nanargmax(diff),diff.shape)[::-1])),peak_diff=float(np.nanmax(diff)),target_baseline=float(med[round(xy[1]),round(xy[0])]),image=str(img),source_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),difference=diff.tolist());out.append(r)
(B/'helper-pixels-results.json').write_text(json.dumps(out,indent=2));print(json.dumps([{k:v for k,v in r.items() if k not in ('difference','source_sha256')} for r in out],indent=2))
