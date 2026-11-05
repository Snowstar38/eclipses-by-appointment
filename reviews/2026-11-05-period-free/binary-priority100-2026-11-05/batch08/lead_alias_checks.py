"""Bounded P/2 interleaving-window check for sparse selected same-kind clocks."""
import json,hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
B=Path(__file__).resolve().parent
tim={x['sample_id']:x for x in json.loads((B/'lead-timing.json').read_text())}
out=[]
for sid in ('T073','T076','T078','T080'):
 r=tim[sid];P=r['period_days'];epoch=r['epoch_btjd'];m=json.loads((B/r['tic']/'lead-numeric.json').read_text())
 sampled=[]
 for src in m['sources']:
  fp=Path(src['path']);assert hashlib.sha256(fp.read_bytes()).hexdigest()==src['sha256']
  with fits.open(fp) as h:
   d=h[1].data;t=np.asarray(d['TIME'],float);f=np.asarray(d['SAP_FLUX'],float);q=np.asarray(d['QUALITY'],int)
  ok=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[ok];f=f[ok]
  if len(t)<10:continue
  cadence=float(np.median(np.diff(t)));n0=int(np.floor((t.min()-epoch)/P))-1;n1=int(np.ceil((t.max()-epoch)/P))+1
  for n in range(n0,n1+1):
   for denominator,phase in ((2,.5),(3,1/3),(3,2/3)):
    pred=epoch+(n+phase)*P
    if not(t.min()<=pred<=t.max()):continue
    half=.25;core=np.abs(t-pred)<half;left=(t>=pred-.9)&(t<pred-.45);right=(t>pred+.45)&(t<=pred+.9)
    bins=np.linspace(pred-half,pred+half,max(4,int(round(2*half/cadence))+1));counts=np.histogram(t[core],bins=bins)[0];cov=float(np.mean(counts>0));
    rec=dict(sector=src['sector'],alias_denominator=denominator,cycle_fraction=n+phase,pred_btjd=float(pred),core_time_bin_coverage=cov,core_first_btjd=float(t[core].min()) if core.any() else None,core_last_btjd=float(t[core].max()) if core.any() else None,core_n=int(core.sum()),left_n=int(left.sum()),right_n=int(right.sum()),largest_core_gap_days=float(np.max(np.diff(t[core]))) if sum(core)>1 else None)
    if core.sum()>2 and left.sum()>3 and right.sum()>3:
     base=np.median(f[left|right]);rec['core_deficit_ppt']=float(1000*(1-np.median(f[core])/base));rec['side_scatter_ppt']=float(1000*1.4826*np.median(abs(f[left|right]/base-1)))
    sampled.append(rec)
 out.append(dict(sample_id=sid,tic=r['tic'],measured_period_days=P,tested_shorter_alias_days=[P/2,P/3],method='P/2 and P/3 of selected same-kind clock predict equally deep intervening same-kind eclipses; actual quality-zero time-bin coverage and local side baseline are shown. Nearby opposite-kind events or broad trends require visual interpretation; absence alone is not a physical refutation.',windows=sampled))
 print(sid,[(x['alias_denominator'],x['sector'],round(x['pred_btjd'],2),round(x['core_time_bin_coverage'],2),round(x.get('core_deficit_ppt',float('nan')),1)) for x in sampled if x['core_time_bin_coverage']>.8 and 'core_deficit_ppt' in x][:20],flush=True)
(B/'lead-alias-checks.json').write_text(json.dumps(out,indent=2)+'\n')
