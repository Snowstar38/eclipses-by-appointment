"""Bounded observed-window test for F023 long-baseline cycles and half/third aliases."""
from pathlib import Path
import json,hashlib,math
import numpy as np
from astropy.io import fits
B=Path(__file__).resolve().parent;tic='286094277';m=json.loads((B/tic/'lead-measurements.json').read_text(encoding='utf8'))
ev=[x for x in m['screen_flagged_dips'] if 'measured_center_btjd' in x and not x['fit_singular'] and not x['fit_boundary']]
t=np.array(sorted(x['measured_center_btjd'] for x in ev));P=27.37165736;ep=1747.3806
n=np.rint((t-ep)/P).astype(int);res=t-(ep+n*P)
out=dict(tic=tic,measured_centers_btjd=t.tolist(),cycles=n.tolist(),residual_days=res.tolist(),rms_residual_days=float(np.sqrt(np.mean(res**2))),gaia_period_days=27.388301314923662,aliases=[])
for divisor in [1,2,3]:
    period=P/divisor;wins=[]
    for r in m['source_receipts']:
        p=Path(r['path']);assert hashlib.sha256(p.read_bytes()).hexdigest()==r['sha256']
        with fits.open(p,memmap=False) as h:
            a=h[1].data;tt=np.array(a['TIME'],float);f=np.array(a['SAP_FLUX'],float);q=np.array(a['QUALITY'],int)
        good=np.isfinite(tt)&np.isfinite(f)&(f>0)&(q==0);tt=tt[good];f=f[good]
        if len(tt)<30:continue
        dt=float(np.median(np.diff(tt)))
        for j in range(math.ceil((tt.min()-ep)/period),math.floor((tt.max()-ep)/period)+1):
            pred=ep+j*period;u=tt-pred;core=np.abs(u)<.15;left=(u>-.7)&(u<-.3);right=(u>.3)&(u<.7);tc=tt[core]
            gap=float(max(np.diff(tc),default=1))
            full=bool(len(tc)>3 and tc.min()<pred-.15+dt and tc.max()>pred+.15-dt and gap<max(.07,2.5*dt))
            baseline=bool(left.sum()>3 and right.sum()>3)
            depth=float((1-np.median(f[core])/np.median(f[left|right]))*1000) if full and baseline else None
            bas=f[left|right];scatter=float(1.4826*np.median(np.abs(bas/np.median(bas)-1))*1000) if baseline else None
            wins.append(dict(sector=int(r['sector']),trial_cycle=j,predicted_btjd=float(pred),full=full,bilateral_baseline=baseline,depth_ppt=depth,core_q0_positive=int(core.sum()),core_first_btjd=float(tc.min()) if len(tc) else None,core_last_btjd=float(tc.max()) if len(tc) else None,core_max_gap_days=gap if len(tc)>1 else None,left_baseline_q0=int(left.sum()),right_baseline_q0=int(right.sum()),baseline_scatter_ppt=scatter,source_sha256=r['sha256']))
    extra=[x for x in wins if x['full'] and x['bilateral_baseline'] and (x['trial_cycle']%divisor)!=0]
    out['aliases'].append(dict(trial_period_days=period,divisor=divisor,all_covered=sum(x['full'] and x['bilateral_baseline'] for x in wins),additional_phase_covered=len(extra),additional_phase_median_depth_ppt=float(np.median([x['depth_ppt'] for x in extra])) if extra else None,additional_phase_max_depth_ppt=max([x['depth_ppt'] for x in extra],default=None),additional_phase_windows=extra))
out['caveat']='Full actual quality-zero core and bilateral baseline required. Testing no comparably deep same-kind dips at half/third clock; a shallow secondary at another orbital phase is allowed.'
(B/tic/'lead-alias.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print([(a['divisor'],a['all_covered'],a['additional_phase_covered'],a['additional_phase_median_depth_ppt'],a['additional_phase_max_depth_ppt']) for a in out['aliases']])
