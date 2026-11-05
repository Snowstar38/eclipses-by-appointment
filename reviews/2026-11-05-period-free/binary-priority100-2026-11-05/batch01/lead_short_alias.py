"""Actual SAP coverage/nulls at selected shorter integer aliases for T003/T004."""
import json,hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent
choices=[('T003','123365080',97,3953.4326,48.527672,.32),('T004','241629469',65,3070.0045,38.115712,.34)]
out=[]
for sid,tic,sector,anchor,p,duration in choices:
    m=json.loads((B/tic/'lead-numeric.json').read_text());src=next(x for x in m['sources'] if x['sector']==sector)
    fp=Path(src['path']);assert hashlib.sha256(fp.read_bytes()).hexdigest()==src['sha256']
    with fits.open(fp,memmap=False) as h:
        a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
    valid=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[valid];f=f[valid];cad=float(np.median(np.diff(t)))
    fig,axs=plt.subplots(3,1,figsize=(9,7),squeeze=False)
    for ax,k in zip(axs[:,0],(2,3,4)):
        pred=anchor+p/k;dt=t-pred;core=np.abs(dt)<duration/2;left=(dt>-.8)&(dt<-.35);right=(dt>.35)&(dt<.8);local=np.abs(dt)<.8
        core_t=t[core];core_f=f[core];lt=t[left];rt=t[right]
        edge_start=pred-duration/2;edge_end=pred+duration/2
        expected=duration/cad
        present=(len(core_t)>=.8*expected and len(lt)>=.8*(.45/cad) and len(rt)>=.8*(.45/cad) and len(core_t)>2 and core_t.min()-edge_start<1.6*cad and edge_end-core_t.max()<1.6*cad and np.max(np.diff(core_t))<2*cad)
        baseline=np.median(np.r_[f[left],f[right]]) if sum(left)+sum(right)>2 else float('nan')
        deficit=(1-np.median(core_f)/baseline)*1000 if len(core_f)>0 else None
        noise=1.4826*np.median(np.abs(np.r_[f[left],f[right]]/baseline-1))*1000 if np.isfinite(baseline) else None
        coarse=(len(core_t)>=.75*expected and len(lt)>=.5*(.45/cad) and len(rt)>=.5*(.45/cad) and len(core_t)>2 and core_t.min()-edge_start<2*cad and edge_end-core_t.max()<2*cad and np.max(np.diff(core_t))<.03)
        rec=dict(sample_id=sid,tic=tic,sector=sector,alias_divisor=k,period_days=p/k,predicted_deep_btjd=pred,source_sha256=src['sha256'],duration_days=duration,cadence_days=cad,expected_core_n=expected,quality0_core_n=int(sum(core)),quality0_left_n=int(sum(left)),quality0_right_n=int(sum(right)),core_first_btjd=float(core_t.min()) if len(core_t) else None,core_last_btjd=float(core_t.max()) if len(core_t) else None,core_max_internal_gap_days=float(np.max(np.diff(core_t))) if len(core_t)>1 else None,window_start_btjd=edge_start,window_end_btjd=edge_end,sensitive_coverage=bool(present),sensitive_to_100ppt_deep=bool(coarse),core_median_deficit_ppt=float(deficit) if deficit is not None else None,side_scatter_ppt=float(noise) if noise is not None else None)
        out.append(rec)
        ax.plot(dt[local],f[local]/baseline,'.',ms=2);ax.axvspan(-duration/2,duration/2,color='orange',alpha=.2);ax.set_xlim(-.8,.8)
        ax.set_title(f'{sid} P/{k} @ {pred:.4f}: coverage {present}, core deficit {deficit:.2f} ppt, n={sum(core)}',fontsize=10)
        ax.set_ylabel('raw SAP / side')
        print(sid,k,'sensitive',present,'gross',coarse,'core',sum(core),'flanks',sum(left),sum(right),'gap',rec['core_max_internal_gap_days'],'deficit',round(deficit,3) if deficit is not None else None,'noise',round(noise,3) if noise is not None else None)
    fig.tight_layout();fig.savefig(B/tic/'lead-short-alias.png',dpi=125);plt.close(fig)
(B/'lead-short-alias.json').write_text(json.dumps(out,indent=2)+'\n')
