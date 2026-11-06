import numpy as np,json,hashlib
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
B=Path(__file__).resolve().parent;pop=json.loads((B.parent.parent/'fresh-band-next400'/'population.json').read_text())['targets']
items=[('159860053',28,2066.022,.07,.3,.6),('159860053',106,4246.76,.06,.3,.6),('162437782',90,3768.785,.10,.3,.6),('167461087',82,3549.07,.025,.15,.3),('277772867',95,3902.152,.10,.3,.6),('332686088',58,2890.333,.035,.2,.4),('436205524',41,2421.210,.07,.3,.6),('440995465',64,3053.788,.07,.3,.6),('440995465',64,3062.822,.07,.3,.6),('440995465',64,3058.099,.07,.3,.6)]
nb={};out=[]
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
(B/'lead-pixels-results.json').write_text(json.dumps(out,indent=2));print(json.dumps([{k:v for k,v in r.items() if k not in ('difference','source_sha256')} for r in out],indent=2))
