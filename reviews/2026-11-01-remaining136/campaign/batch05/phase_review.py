from pathlib import Path
import json,csv,numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).parent;geo=json.load(open(B/'gaia-geometry.json'));out={};fig,axs=plt.subplots(5,2,figsize=(16,18))
for ax,row in zip(axs.flat,csv.DictReader(open(B/'queue.csv'))):
 tic=row['tic'];m=json.load(open(B/tic/'measurements.json'));P=m['period_days'];T=m['primary_epoch_btjd'];dur=m['search_duration_days'];z=[]
 for k,rec in enumerate(m['sources']):
  with fits.open(rec['path']) as h:
   a=h[1].data;ok=(a['QUALITY']==0)&np.isfinite(a['SAP_FLUX'])&(a['SAP_FLUX']>0);t=np.array(a['TIME'][ok],float);f=np.array(a['SAP_FLUX'][ok],float);f/=np.median(f)
  ph=((t-T)/P)%1;ax.plot(ph,f+k*.06,'.',ms=.7,alpha=.55,label=str(rec['sector']))
  grid=np.arange(.05,.951,.002);vals=[]
  for phase in grid:
   dt=abs(((ph-phase+.5)%1)-.5)*P;core=dt<dur*.3;oot=(dt>dur*.75)&(dt<dur*1.75)
   vals.append(float((np.median(f[oot])-np.median(f[core]))*1000) if sum(core)>=3 and sum(oot)>=6 else -999)
  j=int(np.argmax(vals));z.append(dict(sector=rec['sector'],strongest_candidate_phase=float(grid[j]),contrast_ppt=vals[j]))
 ax.axvline(geo[tic]['other_conjunction_relative_phase'],color='r',ls='--');ax.set_title(tic);ax.set_xlabel('Phase, measured selected-kind ephemeris');ax.legend(fontsize=7)
 out[tic]=dict(sectors=z,gaia_other_phase=geo[tic]['other_conjunction_relative_phase'],note='Raw quality-zero per-sector median normalized flux, vertical offsets0.06. Heuristic local contrasts are candidate guides only; secondary claims require recurring morphology. Red line is source-specific eccentric other-conjunction phase, not fixed0.5.')
fig.tight_layout();fig.savefig(B/'phase-review.png',dpi=150);(B/'phase-review.json').write_text(json.dumps(out,indent=2))
