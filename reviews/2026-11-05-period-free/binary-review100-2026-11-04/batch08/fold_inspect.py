import csv, hashlib, json
from pathlib import Path
import numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

B=Path(__file__).resolve().parent
Q=list(csv.DictReader((B/'queue.csv').open(newline='',encoding='utf-8')))
for row in Q:
    tic=row['tic']; out=B/tic; out.mkdir(exist_ok=True)
    src=json.loads((B.parent/'source-packets'/tic/'sources.json').read_text())
    fold=src['fold']; files=[]; windows=[]; light={}
    for f in fold['files']:
        if 'path' not in f: continue
        p=Path(f['path']); digest=hashlib.sha256(p.read_bytes()).hexdigest()
        assert digest==f['sha256'],p
        with fits.open(p,memmap=False) as h:
            a=h[1].data; names=a.names
            t=np.asarray(a['TIME'],float); q=np.asarray(a['QUALITY'],int)
            flux={k:np.asarray(a[k],float) for k in ('SAP_FLUX','KSPSAP_FLUX','SAP_BKG','SAP_X','SAP_Y') if k in names}
        good=np.isfinite(t)&(q==0)&np.isfinite(flux['SAP_FLUX'])&(flux['SAP_FLUX']>0)
        t=t[good]; flux={k:v[good] for k,v in flux.items()}; s=int(f['sector'])
        files.append({'sector':s,'path':str(p),'sha256':digest,'start':float(t.min()),'end':float(t.max()),'n':len(t),'median_cadence_d':float(np.median(np.diff(t)))})
        light[s]=(t,flux)
        for typ in ('P','P2'):
            ep=fold[typ]; P=ep['P']; t0=ep['t0']; dur=ep['dur']
            for k in range(int(np.floor((t.min()-t0)/P))-1,int(np.ceil((t.max()-t0)/P))+2):
                center=t0+k*P
                if not t.min()-1.3<center<t.max()+1.3:continue
                x=t-center; win=np.abs(x)<1.2; core=np.abs(x)<max(.12,dur/2); side=(np.abs(x)>.65)&(np.abs(x)<1.2)
                left=side&(x<0);right=side&(x>0)
                if side.sum()<5:baseline=float('nan')
                else:baseline=float(np.median(flux['SAP_FLUX'][side]))
                def med(mask,key):return float(np.median(flux[key][mask])) if mask.sum() else None
                def maxgap(mask):return float(np.max(np.diff(t[mask]))) if mask.sum()>1 else None
                delta=lambda key: 1000*(med(core,key)/med(side,key)-1) if core.sum() and side.sum()>5 and med(side,key) else None
                windows.append({'sector':s,'trial':typ,'cycle':k,'predicted_btjd':center,'duration_days':dur,'n_core':int(core.sum()),'n_left':int(left.sum()),'n_right':int(right.sum()),'core_max_gap_days':maxgap(core),'side_max_gap_days':maxgap(side),'sap_core_delta_ppt':delta('SAP_FLUX'),'kspsap_core_delta_ppt':delta('KSPSAP_FLUX') if 'KSPSAP_FLUX' in flux else None,'sap_baseline':baseline,'nearest_cadence_days':float(np.min(np.abs(x)))})
    selected=sorted(windows,key=lambda w:(w['trial'],w['predicted_btjd']))
    fig,ax=plt.subplots(max(1,len(selected)),1,figsize=(10,max(2,2.05*len(selected))),squeeze=False)
    for a,w in zip(ax[:,0],selected):
        t,fl=light[w['sector']]; x=t-w['predicted_btjd']; m=np.abs(x)<1.2
        y=fl['SAP_FLUX'][m]/w['sap_baseline'] if np.isfinite(w['sap_baseline']) else fl['SAP_FLUX'][m]/np.median(fl['SAP_FLUX'][m])
        a.plot(x[m],y,'.',ms=2);a.axvline(0,color='r',lw=.6);a.axhline(1,color='k',lw=.5)
        a.set_xlim(-1.2,1.2)
        a.set_title(f"{w['trial']} s{w['sector']} k{w['cycle']} {w['predicted_btjd']:.3f} core={w['sap_core_delta_ppt']} ppt n={w['n_core']}",fontsize=8)
    ax[-1,0].set_xlabel('Days from fold prediction');fig.tight_layout();fig.savefig(out/'fold-predicted-windows.png',dpi=110);plt.close(fig)
    result={'sample_id':row['sample_id'],'tic':tic,'gaia_period_days':row['gaia_period_days'],'fold_trials':{x:fold[x] for x in ('P','P2')},'files':files,'windows':selected,'method':'QUALITY=0 SAP and KSPSAP local median core ±max(0.12,duration/2) d versus side 0.65–1.2 d; predicted times, not measured centers. Missing cadences excluded; n and max gap reported.'}
    (out/'fold-inspection.json').write_text(json.dumps(result,indent=2)+'\n')
    print(row['sample_id'],tic,len(selected),flush=True)
