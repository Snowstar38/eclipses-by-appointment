"""Inspect actual quality-zero coverage of TIC 331650047 half-period odd cycles."""
import json
from pathlib import Path
import numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

here=Path(__file__).resolve().parent;tic='331650047'
m=json.loads((here/tic/'measurements.json').read_text());fit=m['same_kind_fits']['A']
t0=fit['epoch_btjd'];half=fit['period_days']/2
files=sorted((here.parent/'search256'/'fresh-data').glob(f'{tic}_s*.fits'))
output=[]
for path in files:
    sector=int(path.stem.split('_s')[1])
    with fits.open(path) as h:
        a=h[1].data;t=np.array(a['TIME'],float);f=np.array(a['SAP_FLUX'],float);q=np.array(a['QUALITY'],int)
    ok=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[ok];f=f[ok]
    for n in range(int(np.floor((t.min()-t0)/half))-1,int(np.ceil((t.max()-t0)/half))+2):
        if n%2==0:continue
        center=t0+n*half
        core=abs(t-center)<.08;side=(abs(t-center)>.18)&(abs(t-center)<.45)
        before=side&(t<center);after=side&(t>center)
        if not (core.sum()>=5 and before.sum()>=5 and after.sum()>=5):
            output.append(dict(sector=sector,half_cycle=n,predicted_btjd=center,adequate=False,
                               n_core=int(core.sum()),n_before=int(before.sum()),n_after=int(after.sum())))
            continue
        base=.5*(np.median(f[before])+np.median(f[after]));depth=(base-np.median(f[core]))/base*1000
        noise=1.4826*np.median(abs(f[side]-np.median(f[side])))/base*1000
        output.append(dict(sector=sector,half_cycle=n,predicted_btjd=center,adequate=True,
                           n_core=int(core.sum()),n_before=int(before.sum()),n_after=int(after.sum()),
                           core_depth_ppt=float(depth),side_mad_ppt=float(noise)))
        fig,ax=plt.subplots(figsize=(7,3));win=abs(t-center)<.6
        ax.plot(t[win]-center,f[win]/base,'.',ms=2)
        ax.axvspan(-.08,.08,alpha=.15,color='red')
        ax.set_title(f'TIC {tic} s{sector} odd half-cycle {n}; depth {depth:.2f} ppt')
        ax.set_xlabel('Days from half-period prediction');ax.set_ylabel('raw Q0 SAP / local baseline')
        fig.tight_layout();fig.savefig(here/tic/f'half-alias-s{sector}-n{n}.png',dpi=130);plt.close(fig)
(here/tic/'half-alias-windows.json').write_text(json.dumps(output,indent=2))
print(json.dumps(output,indent=2))
