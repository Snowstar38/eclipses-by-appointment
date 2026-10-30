import json,numpy as np,matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
r=Path(__file__).parent;P=json.load(open(r/'pixel-results.json'));N=json.load(open(r/'neighbour-results.json'));fig,axs=plt.subplots(1,4,figsize=(16,4))
for ax,(tic,sec) in zip(axs,[('431762229',58),('222498305',39),('9396327',80),('183994341',91)]):
 p=next(x for x in P if x['tic']==tic and x['sector']==sec);n=next(x for x in N if x['tic']==tic and x['sector']==sec);z=np.load(r/tic/f'pixel_s{sec:03d}.npz')['deficit'];v=np.percentile(abs(z),98);ax.imshow(z,origin='lower',cmap='RdBu_r',vmin=-v,vmax=v);ax.plot(*p['target_px'],'x',c='lime',ms=12); 
 for c in n['capable_neighbours']:
  x,y=c['px'];ax.plot(x,y,'o',mfc='none',mec='orange',ms=6)
 ax.set_title(f'TIC{tic} S{sec}');ax.set_xlim(1,9);ax.set_ylim(1,9)
fig.suptitle('Signed eclipse deficit; green target, orange capable TIC neighbours');fig.tight_layout();fig.savefig(r/'lead-source-panels.png',dpi=150)
