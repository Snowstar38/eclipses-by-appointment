"""Test nearby integer-cycle alternatives against clean raw SAP coverage."""
import json, math
from pathlib import Path
import numpy as np
from astropy.io import fits
B=Path(__file__).resolve().parent
for tic,t1,t2,ns,half,depth in [('352438536',2040.0819,4106.0797,range(32,39),1.0,36),('322217134',3232.1065,3815.162,range(15,22),.35,77)]:
    src=json.loads((B/tic/'raw-inspection.json').read_text());series=[]
    for r in src['sectors']:
        if 'path' not in r:continue
        with fits.open(r['path'],memmap=False) as h:
            a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
        v=np.isfinite(t)&np.isfinite(f)&(f>0);series.append((r['sector'],t[v],f[v],q[v],r['cadence_days']))
    alternatives=[]
    for N in ns:
        P=(t2-t1)/N;ws=[]
        for sector,t,f,q,cad in series:
            for n in range(math.ceil((min(t)-t1-half)/P),math.floor((max(t)-t1+half)/P)+1):
                pred=t1+n*P;x=t-pred;core=abs(x)<half
                left=(x>-2.4*half)&(x<-1.4*half);right=(x<2.4*half)&(x>1.4*half)
                clean=core&(q==0);lc=left&(q==0);rc=right&(q==0)
                expected_n=2*half/cad
                core_times=np.sort(t[clean])
                max_gap=float(max(np.diff(core_times))) if len(core_times)>1 else float('inf')
                bin_counts=np.histogram(x[clean],bins=np.linspace(-half,half,7))[0]
                sensitive=bool(sum(clean)>=.75*expected_n and sum(lc)>=8 and sum(rc)>=8
                               and max_gap<max(3*cad,.15*half) and np.all(bin_counts>0))
                w={'sector':sector,'cycle':n,'predicted_btjd':pred,'quality0_core':int(sum(clean)),
                   'expected_core':float(expected_n),'left_quality0':int(sum(lc)),
                   'right_quality0':int(sum(rc)),'max_internal_core_gap_days':max_gap,
                   'core_six_bin_counts':bin_counts.tolist(),'sensitive':sensitive}
                if sensitive:
                    base=(np.median(f[lc])+np.median(f[rc]))/2
                    oot=np.concatenate([f[lc],f[rc]])/base
                    loss=1000*(1-np.median(f[clean])/base)
                    noise=1482.6*np.median(abs(oot-np.median(oot)))
                    w.update(core_loss_ppt=float(loss),side_mad_ppt=float(noise),
                             clean_null=bool(loss<.3*depth and noise<.2*depth))
                ws.append(w)
        gp=float(src['gaia_period_days']); ge=float(json.loads((B.parent/'source-packets'/tic/'sources.json').read_text())['target']['gaia']['period_error'])
        alternatives.append({'cycles_between_two_events':N,'period_days':P,'difference_from_gaia_days':P-gp,
                             'difference_in_gaia_formal_sigma':(P-gp)/ge,'clean_null_count':sum(w.get('clean_null',False) for w in ws),
                             'sensitive_window_count':sum(w['sensitive'] for w in ws),'windows':ws})
    (B/tic/'alias-tests.json').write_text(json.dumps({'tic':tic,'first_center_btjd':t1,'later_center_btjd':t2,'second_center_caveat':'H008 later center from partial quality-censored event; provisional','alternatives':alternatives,'method':'Same-kind two-event integer-cycle alternatives; clean null needs >=75% cadence-expected core sampling, all six core bins covered, max internal core gap <15% half-width, >=8 clean samples each side, core loss <30% representative depth and side MAD <20% depth. Gaia comparison uses formal period error only and is not a proof that eclipses belong to Gaia orbit. Adjacent real events contaminate some alternative windows and require visual adjudication.'},indent=2)+'\n')
    print(tic,[(a['cycles_between_two_events'],round(a['period_days'],3),round(a['difference_in_gaia_formal_sigma'],1),a['clean_null_count']) for a in alternatives])
