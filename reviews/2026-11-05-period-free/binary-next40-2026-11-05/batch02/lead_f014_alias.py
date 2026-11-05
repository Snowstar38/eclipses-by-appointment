"""Test bounded integer subharmonics of the recurring F014 A dips in actual SAP."""
import hashlib,json,math
from pathlib import Path
import numpy as np
from astropy.io import fits
B=Path(__file__).resolve().parent;tic='236223193'
d=json.loads((B/tic/'lead-measurements.json').read_text())
source={int(Path(s['path']).stem.split('_s')[-1]):s for s in d['source_receipts']}
observed=[2424.6169,2431.2596,2812.2604,2818.8631,3340.8387,3347.4436]
P=35.239;t0=2424.6169;out=[]
for sec in (41,55,75):
    s=source[sec];p=Path(s['path']);assert hashlib.sha256(p.read_bytes()).hexdigest()==s['sha256']
    with fits.open(p,memmap=False) as h:
        a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
    good=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[good];f=f[good]
    for divisor in (2,3,4):
        per=P/divisor
        for n in range(math.ceil((t.min()-t0)/per),math.floor((t.max()-t0)/per)+1):
            center=t0+n*per
            if min(abs(center-x) for x in observed)<.6:continue
            core=abs(t-center)<.1;side=(abs(t-center)>.3)&(abs(t-center)<.7)
            if core.sum()<2 or side.sum()<8:continue
            left=t[core].min()-center;right=t[core].max()-center
            coverage=min(1,max(0,(right-left+.002)/.2))
            x=t[side]-center;coef=np.polyfit(x,f[side],1);norm=f/np.polyval(coef,t-center)
            depth=float((1-np.median(norm[core]))*1000)
            out.append(dict(sector=sec,divisor=divisor,cycle=n,predicted_center_btjd=center,core_n=int(core.sum()),core_left_offset=float(left),core_right_offset=float(right),core_coverage_fraction=float(coverage),baseline_n=int(side.sum()),local_depth_ppt=depth,source_sha256=s['sha256']))
(B/tic/'lead-alias.json').write_text(json.dumps(dict(method='A-kind arithmetic subharmonic predictions, actual quality0 positive SAP core +/-0.1 d and linear side baseline 0.3-0.7 d; local depths are not global vetoes',nominal_period_days=P,rows=out),indent=2)+'\n',encoding='utf-8')
print([(x['sector'],x['divisor'],round(x['predicted_center_btjd'],3),round(x['local_depth_ppt'],2),round(x['core_coverage_fraction'],2)) for x in out])
