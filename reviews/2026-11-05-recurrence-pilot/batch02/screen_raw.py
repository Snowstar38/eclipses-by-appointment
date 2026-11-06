"""Plot every raw sector and ranked detector windows for exact batch01."""
from pathlib import Path
import csv, json, hashlib
import numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

B=Path(__file__).resolve().parent
H=B.parent.parent/'binary-exploration-2026-11-04'/'bulk-results'
q=list(csv.DictReader((B/'queue.csv').open(newline='',encoding='utf8')))
for row in q:
    tic=row['tic']; out=B/tic; out.mkdir(exist_ok=True)
    bulk=json.loads((H/f'{tic}.json').read_text())
    series={}; windows=[]; coverage=[]
    for rec in bulk['files']:
        p=Path(rec['path']); sha=hashlib.sha256(p.read_bytes()).hexdigest()
        assert sha==rec['sha256']
        with fits.open(p,memmap=False) as hd:
            assert str(int(hd[0].header['TICID']))==tic
            d=hd[1].data
            t=np.asarray(d['TIME'],float); f=np.asarray(d['SAP_FLUX'],float)
            z=np.asarray(d['QUALITY'],int)
        ok=np.isfinite(t)&np.isfinite(f)&(f>0)&(z==0)
        t=t[ok];f=f[ok]; f=f/np.median(f)
        sector=int(rec['sector']);series[sector]=(t,f)
        coverage.append({'sector':sector,'first':float(t.min()),'last':float(t.max()),'n':len(t),'median_cadence':float(np.median(np.diff(t))),'largest_gap':float(max(np.diff(t)))})
        for w in rec['windows']:
            if w['kind']=='dip': windows.append(dict(w,sector=sector))
    windows.sort(key=lambda w:(w['flag'],w['contrast']),reverse=True)
    sectors=sorted(series)
    fig,ax=plt.subplots(len(sectors),1,figsize=(13,max(4,1.35*len(sectors))),squeeze=False)
    for a,s in zip(ax[:,0],sectors):
        t,f=series[s];a.plot(t,f,'.',ms=1.1,color='black')
        for w in windows:
            if w['sector']==s and w['flag']:
                a.axvline(w['time'],color='red',alpha=.5,lw=.6)
        a.set_ylabel(f'S{s}',rotation=0,labelpad=16)
        lo,hi=np.nanquantile(f,[.005,.995]);pad=max((hi-lo)*.15,.003)
        a.set_ylim(lo-pad,hi+pad)
    fig.suptitle(f"{row['sample_id']} TIC {tic} raw SAP q0, red = flagged dip predictions")
    fig.tight_layout();fig.savefig(out/'all-sectors.png',dpi=130);plt.close(fig)
    picks=[];seen=set()
    for w in windows:
        if w['sector'] not in seen:
            picks.append(w);seen.add(w['sector'])
        if len(picks)>=min(8,len(sectors)):break
    fig,ax=plt.subplots(len(picks),1,figsize=(12,max(3,2.3*len(picks))),squeeze=False)
    for a,w in zip(ax[:,0],picks):
        t,f=series[w['sector']]; m=np.abs(t-w['time'])<max(3*w['duration'],1)
        a.plot(t[m]-w['time'],f[m],'.',ms=2,color='black')
        a.axvspan(-w['duration']/2,w['duration']/2,color='red',alpha=.12)
        a.set_title(f"S{w['sector']} prediction {w['time']:.3f}, duration {w['duration']:.2f}, contrast {w['contrast']:.1f}, flagged {w['flag']}",fontsize=9)
    fig.tight_layout();fig.savefig(out/'ranked-windows.png',dpi=130);plt.close(fig)
    (out/'screen.json').write_text(json.dumps({'tic':tic,'coverage':coverage,'ranked_windows':windows},indent=2)+'\n')
    print(tic,len(sectors),len(windows),[(w['sector'],round(w['time'],2),round(w['contrast'],1)) for w in windows[:5]],flush=True)
