"""Independent full-light-curve, cycle-by-cycle depth check for Q029."""
from pathlib import Path
import json,hashlib
import numpy as np
from astropy.io import fits
B=Path(__file__).resolve().parent;T=B/'168657537'
d=json.loads((T/'lead-measurements.json').read_text())
tim=json.loads((T/'lead-timing.json').read_text())['aliases_by_late_epoch_cycle_offset']['0']
epoch=tim['epoch_btjd'];period=tim['period_days']
events=[]
for src in d['source_receipts']:
    fp=Path(src['path']); sec=int(fp.stem.split('_s')[-1]);
    if sec not in (4,5,31):continue
    assert hashlib.sha256(fp.read_bytes()).hexdigest()==src['sha256']
    with fits.open(fp,memmap=False) as h:
        a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
    ok=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[ok];f=f[ok];cad=float(np.median(np.diff(t)))
    for n in range(int(np.floor((min(t)-epoch)/period)),int(np.ceil((max(t)-epoch)/period))+1):
        c=epoch+n*period
        if c<min(t)+.4 or c>max(t)-.4:continue
        x=t-c;core=np.abs(x)<.05;wing=(np.abs(x)>.18)&(np.abs(x)<.38)
        if core.sum()<.07/cad*.6 or wing.sum()<.4/cad*.6:continue
        # Actual endpoint and internal coverage, not row fraction alone.
        ct=t[core]; expected=int(round(.1/cad))+1
        complete=bool(ct.min()<c-.035 and ct.max()>c+.035 and np.max(np.diff(ct))<3*cad and core.sum()>=expected*.7)
        a,b=np.polyfit(x[wing],f[wing],1); norm=f/(a*x+b)
        depth=float((1-np.median(norm[core]))*1000)
        events.append({'sector':sec,'cycle':n,'parity':n%2,'predicted_center_btjd':float(c),'core_actual':int(core.sum()),'core_expected':expected,'core_complete':complete,'depth_ppt':depth,'source_sha256':src['sha256']})
summ={}
for sec in [4,5,31]:
    for parity in [0,1]:
        vals=[e['depth_ppt'] for e in events if e['sector']==sec and e['parity']==parity and e['core_complete']]
        summ[f'S{sec}_parity{parity}']={'n':len(vals),'median_depth_ppt':float(np.median(vals)) if vals else None,'values_ppt':vals}
result={'scope':'All predicted cycles in S4/S5/S31 with actual core and wing coverage. Parity is relative to conditional 1.96345-d dip clock, and cannot by itself distinguish 1P transits from a 2P binary.','events':events,'parity_summary':summ}
bysec={s:[e for e in events if e['sector']==s and e['core_complete']] for s in (4,5,31)}
def parity_contrast(items):
    return np.mean([np.mean([e['depth_ppt'] for e in items[s] if e['parity']==1])-np.mean([e['depth_ppt'] for e in items[s] if e['parity']==0]) for s in (4,5,31)])
observed=float(parity_contrast(bysec)); rng=np.random.default_rng(29); greater=0; N=50000
for _ in range(N):
    simulation={}
    for s,group in bysec.items():
        shuffled=rng.permutation([e['parity'] for e in group])
        simulation[s]=[dict(e,parity=int(p)) for e,p in zip(group,shuffled)]
    greater+=abs(parity_contrast(simulation))>=abs(observed)
result['parity_test']={'sector_stratified_mean_odd_minus_even_ppt':observed,'permutation_trials':N,'two_sided_randomization_p':float((greater+1)/(N+1)),'caveat':'Post-selection exploratory statistic. Cadence and aperture systematics, temporal dependence and source blending are not represented by this permutation.'}
(T/'lead-all-cycles.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps({'summary':summ,'test':result['parity_test']},indent=2))
