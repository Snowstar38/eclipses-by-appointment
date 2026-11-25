from pathlib import Path
import json, numpy as np
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
D=Path(__file__).resolve().parent
meta=json.loads((D/'dips.json').read_bytes())
fig,ax=plt.subplots(5,2,figsize=(12,11),constrained_layout=True)
for panel,(tic,ss) in zip(ax.flat,meta.items()):
 for s in ss:
  z=np.load(D/'cadences'/f"{tic}-{s['sector']}.npz");t=z['t'];y=z['pdc'];sel=np.isfinite(y);t=t[sel];y=y[sel];y=1000*(y/np.median(y)-1)
  panel.scatter(t-t.min(),y,s=.08,alpha=.4,label=str(s['sector']))
 panel.legend(fontsize=6);panel.set_title(tic)
fig.savefig(D/'sector-overview.png',dpi=110);plt.close(fig)
for tic in ('187261476','356752132','167710','259514170','307907698'):
 ss=meta[tic];fig,axes=plt.subplots(1,2,figsize=(11,3.5),constrained_layout=True);a,b=axes
 ev=[(r,s) for s in ss for r in s['events'] if r.get('pdc') and r.get('sap')]
 ev.sort(key=lambda rs:-rs[0]['pdc']['depth'])
 if not ev:continue
 e,s=ev[0];t0=e['btjd'];z=np.load(D/'cadences'/f"{tic}-{s['sector']}.npz");t=z['t'];v=z['pdc'];ok=np.isfinite(v)&(v>0);t=t[ok];v=v[ok];v=1000*(v/np.median(v)-1)
 a.plot(t,v,'.',ms=.6);a.axvline(t0,c='r',lw=.5);b.plot(t-t0,v,'.',ms=1);b.set_xlim(-1.3,1.3);fig.suptitle(f'{tic} S{s["sector"]} peak {t0}');fig.savefig(D/f'{tic}-exam.png',dpi=120);plt.close(fig)
