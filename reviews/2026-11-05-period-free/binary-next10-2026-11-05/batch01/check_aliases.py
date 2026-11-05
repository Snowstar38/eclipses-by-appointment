"""Bounded neighboring integer-cycle tests with actual q0 time coverage."""
from pathlib import Path
import csv,json,hashlib,math
import numpy as np
from astropy.io import fits
B=Path(__file__).resolve().parent
Q={r['sample_id']:r for r in csv.DictReader((B/'queue.csv').open(newline='',encoding='utf8'))}
H=B.parent.parent/'binary-exploration-2026-11-04'/'bulk-results'
CASES={'N001':(1959.089,2685.012,.24,40.5,18,24),'N006':(1891.863,2603.626,.12,20.6,26,35),'N007':(2712.682,3454.354,.24,17.7,16,23),'N008':(2046.070,3131.710,.96,11.3,16,24)}
result={}
for sid,(t0,t1,dur,depth,k0,k1) in CASES.items():
    tic=Q[sid]['tic']; bulk=json.loads((H/f'{tic}.json').read_text());data=[]
    for rec in bulk['files']:
        p=Path(rec['path']);assert hashlib.sha256(p.read_bytes()).hexdigest()==rec['sha256']
        with fits.open(p,memmap=False) as hd:
            a=hd[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
        z=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[z];f=f[z];f=f/np.median(f)
        data.append((int(rec['sector']),t,f,float(np.median(np.diff(t)))))
    trials=[]
    for k in range(k0,k1+1):
        P=(t1-t0)/k; occasions=[]
        for s,t,f,cadence in data:
            for n in range(math.ceil((t.min()-t0)/P),math.floor((t.max()-t0)/P)+1):
                if n in (0,k):continue
                mid=t0+n*P
                core=abs(t-mid)<dur/2
                left=(t>mid-2*dur)&(t<mid-.75*dur)
                right=(t>mid+.75*dur)&(t<mid+2*dur)
                expected=max(1,dur/cadence)
                core_n=int(sum(core));frac=core_n/expected
                gaps=float(max(np.diff(t[core]))) if core_n>1 else None
                full=bool(core_n>=max(4,.75*expected) and gaps is not None and gaps<2.5*cadence and sum(left)>=4 and sum(right)>=4 and t[core].min()<mid-.3*dur and t[core].max()>mid+.3*dur)
                if core_n:
                    base=np.median(np.r_[f[left],f[right]]) if sum(left)+sum(right)>8 else None
                    obs=float((base-np.median(f[core]))/base*1000) if base is not None else None
                else:obs=None
                if core_n>0 or abs(mid-t.min())<dur or abs(mid-t.max())<dur:
                    occasions.append({'sector':s,'cycle':n,'predicted_mid':mid,'core_n':core_n,'expected_core_n':expected,'core_fraction':frac,'max_core_gap_days':gaps,'left_n':int(sum(left)),'right_n':int(sum(right)),'full_coverage':full,'observed_core_depth_ppt':obs,'strong_null':bool(full and obs is not None and obs<.25*depth)})
        trials.append({'cycles_between_events':k,'conditional_period_days':P,'occasions':occasions,'strong_null_count':sum(v['strong_null'] for v in occasions)})
    result[sid]={'tic':tic,'anchor_centers_btjd':[t0,t1],'anchor_centers_are':'provisional local raw fits','nominal_duration_days':dur,'nominal_depth_ppt':depth,'trials':trials}
(B/'alias-tests.json').write_text(json.dumps(result,indent=2)+'\n')
for sid,v in result.items():
    print(sid,[(x['cycles_between_events'],x['strong_null_count'],len(x['occasions'])) for x in v['trials']],flush=True)
