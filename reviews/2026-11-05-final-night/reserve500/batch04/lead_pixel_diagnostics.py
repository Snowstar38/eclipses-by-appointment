import json,numpy as np
from pathlib import Path
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent
for tic,sec in [('352725084',81),('394405964',12)]:
 D=B/tic;r=json.loads((D/f'lead-localization-{sec}.json').read_text());c=r['event']['center_btjd'];dur=r['event']['duration_d'];x,y=r['target_xy'];ix,iy=round(x),round(y)
 with fits.open(D/f'lead-tesscut-{sec}.fits') as f:
  a=f[1].data;t=np.asarray(a['TIME'],float);q=np.asarray(a['QUALITY']);cube=np.asarray(a['FLUX'],float)
 yy,xx=np.indices(cube.shape[1:]);sky=np.hypot(xx-x,yy-y)>2.8;bg=np.nanmedian(cube[:,sky],axis=1);ap=(abs(xx-ix)<=1)&(abs(yy-iy)<=1)
 vals={'3x3 raw':np.nansum(cube[:,ap],axis=1),'3x3 minus outer median':np.nansum(cube[:,ap],axis=1)-ap.sum()*bg,'central pixel minus outer median':cube[:,iy,ix]-bg,'outer median':bg}
 good=(q==0)&np.isfinite(t);sel=good&(abs(t-c)<max(2.5*dur,1));side=good&(abs(t-c)>dur*.75)&(abs(t-c)<dur*2);core=good&(abs(t-c)<dur*.25);out={}
 fig,axs=plt.subplots(4,1,figsize=(10,8),sharex=True)
 for ax,(name,v) in zip(axs,vals.items()):
  scale=np.nanmedian(v[side]);z=v/scale;out[name]={'relative_core_loss_ppt':float((1-np.nanmedian(z[core]))*1000),'normalization':float(scale)};ax.plot(t[sel]-c,z[sel],'.',ms=2);ax.set_ylabel(name);ax.axvspan(-dur*.25,dur*.25,alpha=.15);ax.grid(alpha=.2)
 fig.suptitle(f'TIC{tic} S{sec} exact same photons; outer-pixel median background');fig.tight_layout();fig.savefig(D/'lead-pixel-diagnostics.png',dpi=120);plt.close(fig)
 (D/'lead-pixel-diagnostics.json').write_text(json.dumps(out,indent=2))
