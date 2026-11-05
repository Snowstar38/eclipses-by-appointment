"""Conditional timing and phase coherence of Q029's raw, repeated narrow dips."""
from pathlib import Path
import json, hashlib
import numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

B=Path(__file__).resolve().parent
T=B/'168657537'
d=json.loads((T/'lead-measurements.json').read_text(encoding='utf8'))
e=d['screen_flagged_dips']
times=np.array([x['measured_center_btjd'] for x in e])
# The preliminary 1.96345-day clock is determined from within-sector spacing.
# Integer cycles are explicit; test the adjacent long-baseline counts below.
anchor=min(times)
out={}
for offset in [-2,-1,0,1,2]:
    p0=1.96345
    cycles=np.rint((times-anchor)/p0).astype(int)
    cycles=np.where(times>2000,cycles+offset,cycles)
    a=np.column_stack([np.ones(len(times)),cycles])
    epoch,period=np.linalg.lstsq(a,times,rcond=None)[0]
    residual=times-a@np.array([epoch,period])
    out[str(offset)]={'period_days':float(period),'epoch_btjd':float(epoch),'rms_days':float(np.sqrt(np.mean(residual**2))),'max_abs_residual_days':float(np.max(abs(residual))),'event_residuals_days':list(map(float,residual)),'cycle_numbers':list(map(int,cycles))}
best=out['0']; epoch=best['epoch_btjd']; period=best['period_days']
fig,axs=plt.subplots(3,1,figsize=(9,8),sharex=True)
for ax,src in zip(axs,d['source_receipts']):
    fp=Path(src['path'])
    if int(fp.stem.split('_s')[-1]) not in [4,5,31]:continue
    assert hashlib.sha256(fp.read_bytes()).hexdigest()==src['sha256']
    with fits.open(fp,memmap=False) as h:
        a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
    ok=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0)
    t=t[ok];f=f[ok]/np.median(f[ok])
    phase=((t-epoch+period/2)%period)-period/2
    ax.plot(phase,f,'.',ms=2,alpha=.4)
    ax.set_ylabel(f"S{int(fp.stem.split('_s')[-1])} SAP")
    ax.set_ylim(np.percentile(f,0.1)-.001,np.percentile(f,99.9)+.001)
axs[-1].set_xlabel('days from predicted recurrent narrow dip')
fig.suptitle(f'Q029 conditional dip clock: {period:.8f} d; Gaia SB1 is 46.08764 d')
fig.tight_layout();fig.savefig(T/'lead-phase.png',dpi=150);plt.close(fig)
tic_catalog=Path(r'[local-path-redacted]')
assert hashlib.sha256(tic_catalog.read_bytes()).hexdigest()=='9434777b195e9f7f7538b4ebe057d3926c4e8651b37f4ee2702ba3010726290c'
tic_record=json.loads(tic_catalog.read_text(encoding='utf8'))['168657537']
result={'scope':'Fit to 12 preselected local trapezoid centers, several singular. Conditional coherent dip timing, not an orbital SB1 assignment or formal precision period error.','gaia_period_days':46.087635974491675,'aliases_by_late_epoch_cycle_offset':out,'source_sha256_by_sector':{int(Path(x['path']).stem.split('_s')[-1]):x['sha256'] for x in d['source_receipts']},'tic_stellar_metadata':{'radius_solar':tic_record['rad'],'teff_K':tic_record['Teff'],'source':str(tic_catalog),'sha256':hashlib.sha256(tic_catalog.read_bytes()).hexdigest()}}
(T/'lead-timing.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:{f:round(v[f],7) for f in ['period_days','rms_days','max_abs_residual_days']} for k,v in out.items()},indent=2))
