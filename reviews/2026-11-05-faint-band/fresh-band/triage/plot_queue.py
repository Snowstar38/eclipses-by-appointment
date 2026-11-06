"""Render diagnostic raw windows and collect unfitted event-screen measurements."""
import csv
import json
from pathlib import Path
import numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

O=Path(__file__).resolve().parent
W=O.parent
queue=list(csv.DictReader((O/'review-queue.csv').open(newline='')))
measure=[]
for r in queue:
    tic=r['tic']
    bulk=json.loads((W/'bulk-results'/f'{tic}.json').read_text())
    wins=[dict(w,sector=f['sector'],path=f['path']) for f in bulk['files'] if f['status']=='ok' for w in f['windows'] if w['kind']=='dip']
    picks=[]
    for w in sorted(wins,key=lambda w:(w['flag'],w['contrast']),reverse=True):
        if w['sector'] not in {p['sector'] for p in picks}:picks.append(w)
        if len(picks)==min(4,len(bulk['files'])):break
    fig,axs=plt.subplots(len(picks),1,figsize=(11,2.7*len(picks)),squeeze=False)
    for i,w in enumerate(picks):
        ax=axs[i,0]
        with fits.open(w['path']) as hd:
            d=hd[1].data;t=np.asarray(d['TIME'],float);f=np.asarray(d['SAP_FLUX'],float);q=np.asarray(d['QUALITY'])
        m=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0)&(abs(t-w['time'])<max(4*w['duration'],1.5))
        ax.plot(t[m]-w['time'],f[m]/np.median(f[m]),'.',ms=2)
        ax.axvspan(-w['duration']/2,w['duration']/2,color='r',alpha=.10)
        ax.set_title(f"S{w['sector']} BTJD {w['time']:.4f} | scanned box {w['duration']:.2f} d | depth {w['depth']:.4f} | contrast {w['contrast']:.1f}")
        ax.set_xlabel('Days from selected window center');ax.set_ylabel('SAP / local median')
        ax.grid(alpha=.15)
        measure.append({'tic':tic,'sector':w['sector'],'screen_time_btjd':w['time'],'screen_box_d':w['duration'],'screen_depth_fraction':w['depth'],'screen_contrast':w['contrast'],'event_flag':w['flag'],'core_n':w['core_n'],'internal_gaps_ok':w['internal_gaps_ok'],'raw_fits':w['path']})
    fig.suptitle(f'TIC {tic}: raw quality=0 SAP; independently selected sector windows, no eclipse fit',fontsize=12)
    fig.tight_layout();fig.savefig(O/f'queue-{tic}.png',dpi=140);plt.close(fig)
with (O/'queue-window-measurements.csv').open('w',newline='') as f:
    wr=csv.DictWriter(f,fieldnames=list(measure[0]));wr.writeheader();wr.writerows(measure)
print(len(queue),'targets',len(measure),'windows')
