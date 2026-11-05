"""Check actual time coverage of integer subharmonics of the Q005 Gaia period."""
from pathlib import Path
import json
import numpy as np
from astropy.io import fits

B=Path(__file__).resolve().parent
tic='1535458'
packet=json.loads((B.parent/'source-packets'/tic/'sources.json').read_text())
data=[]
for receipt in packet['verified_files']:
    with fits.open(receipt['path']) as hd:
        a=hd[1].data
        t=np.asarray(a['TIME'],float)
        f=np.asarray(a['SAP_FLUX'],float)
        q=np.asarray(a['QUALITY'],int)
    ok=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0)
    data.append((int(receipt['sector']),t[ok],f[ok]))
epoch=2194.214
gaia_period=float(packet['queue_row']['gaia_period_days'])
rows=[]
for divisor in range(1,9):
    period=gaia_period/divisor
    for sector,t,f in data:
        for cycle in range(-100,101):
            center=epoch+cycle*period
            if center<t.min()-2 or center>t.max()+2:continue
            dt=t-center
            core=np.abs(dt)<.4
            left=(-1.4<dt)&(dt<-.6)
            right=(.6<dt)&(dt<1.4)
            near=np.abs(dt)<1.4
            gaps=np.diff(t[near]) if near.sum()>1 else np.array([])
            row=dict(divisor=divisor,conditional_period_days=period,sector=sector,cycle=cycle,
                     predicted_center_btjd=center,core_points=int(core.sum()),left_points=int(left.sum()),
                     right_points=int(right.sum()),max_internal_gap_days=float(gaps.max()) if len(gaps) else None,
                     core_vs_side_median_ppt=(float((1-np.median(f[core])/np.median(f[left|right]))*1000)
                                              if core.sum()>=10 and left.sum()>=10 and right.sum()>=10 else None),
                     interpretation='descriptive local window only; smooth baseline variability and intrinsic orbit can change this statistic')
            rows.append(row)
(B/tic/'lead-q005-alias-windows.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf8')
for r in rows:
    if r['divisor']>1 and r['core_points']>=10 and r['left_points']>=10 and r['right_points']>=10:
        print(r['divisor'],r['sector'],round(r['predicted_center_btjd'],3),round(r['core_vs_side_median_ppt'],1),round(r['max_internal_gap_days'],2))
