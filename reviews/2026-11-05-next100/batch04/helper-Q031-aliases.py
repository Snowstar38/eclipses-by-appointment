"""Test actual q0 cadence support for short same-kind aliases of Q031."""
import json
from pathlib import Path
import numpy as np
from astropy.io import fits
B=Path(__file__).resolve().parent;ROOT=B.parent
packet=json.loads((ROOT/'source-packets/209429773/sources.json').read_text())
events=[2123.0984085,2165.6409522,3952.2485526]
P=(events[2]-events[1])/42
sectors=[]
for s in packet['verified_files']:
    with fits.open(s['path'],memmap=False) as h:
        a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
    ok=(q==0)&np.isfinite(t)&np.isfinite(f)&(f>0)
    t,f=t[ok],f[ok]
    sectors.append((s['sector'],t,f,float(np.median(np.diff(t)))))
tests=[]
for div in (2,3,4):
    p=P/div
    for sec,t,f,cad in sectors:
        nlo=int(np.floor((t.min()-events[1])/p))-1;nhi=int(np.ceil((t.max()-events[1])/p))+1
        for n in range(nlo,nhi+1):
            if n%div==0:continue
            center=events[1]+n*p
            if center<t.min()+1.2 or center>t.max()-1.2:continue
            core=np.abs(t-center)<.22
            pre=(t>=center-1.1)&(t<=center-.65)
            post=(t>=center+.65)&(t<=center+1.1)
            if core.sum()<8 or pre.sum()<8 or post.sum()<8:continue
            coretime=t[core]
            full=(coretime.min()<=center-.18 and coretime.max()>=center+.18 and np.max(np.diff(coretime))<3*cad)
            if not full:continue
            baseline=(np.median(f[pre])+np.median(f[post]))/2
            loss=1000*(1-np.median(f[core])/baseline)
            tests.append(dict(divisor=div,sector=sec,cycle_n=n,predicted_btjd=center,core_n=int(core.sum()),
                              core_first_btjd=float(coretime.min()),core_last_btjd=float(coretime.max()),
                              core_max_gap_days=float(np.max(np.diff(coretime))),pre_n=int(pre.sum()),post_n=int(post.sum()),
                              local_sap_loss_ppt=float(loss)))
out=dict(candidate_same_kind_events_btjd=events,conditional_full_period_days=P,
         period_note='S31 to S97 assigned 42 cycles; S30 to S31 approx one cycle. Event centers are broad local Gaussian diagnostics, not precision timings.',
         null_definition='actual q0 positive cadence, full +/-0.18 d core, no >3-cadence internal gap, bilateral 0.65-1.1 d sidebands',
         extra_phase_windows=tests)
(B/'helper-Q031-aliases.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
for div in (2,3,4):
    z=[x for x in tests if x['divisor']==div]
    print(div,len(z),'min/max loss',min([x['local_sap_loss_ppt'] for x in z],default=None),max([x['local_sap_loss_ppt'] for x in z],default=None))
    print([(x['sector'],round(x['predicted_btjd'],2),round(x['local_sap_loss_ppt'],2)) for x in z])
