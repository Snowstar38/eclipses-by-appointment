"""Reproducible bounded raw-SAP context for the frozen fresh-band queue."""
import csv, json, hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

B=Path(__file__).resolve().parent
S=B.parent.parent.parent/'fresh-band-next1000'
Q=list(csv.DictReader((B/'queue.csv').open(newline='',encoding='utf8')))

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
allout={}
for i,row in enumerate(Q,1):
    tic=row['tic'];sid=row['sample_id']; dest=B/tic;dest.mkdir(exist_ok=True)
    bulk=S/'bulk-results'/f'{tic}.json';d=json.loads(bulk.read_text())
    source=[];events=[];series=[]
    for ff in d['files']:
        p=Path(ff['path']); actual=sha(p)
        if actual!=ff['sha256']:raise ValueError((p,actual,ff['sha256']))
        source.append(dict(path=str(p),sha256=actual,sector=ff['sector']))
        with fits.open(p) as h:
            a=h[1].data;t=np.asarray(a['TIME'],float);y=np.asarray(a['SAP_FLUX'],float);k=np.asarray(a['KSPSAP_FLUX'],float) if 'KSPSAP_FLUX' in a.columns.names else np.full(len(a),np.nan);q=np.asarray(a['QUALITY'],int)
            hdr={key:h[0].header.get(key) for key in ('TICID','SECTOR','RA_OBJ','DEC_OBJ')}
        good=np.isfinite(t)&np.isfinite(y)&(y>0)&(q==0)
        t=t[good];y=y[good];k=k[good]
        if len(t)==0:continue
        secs=dict(sector=ff['sector'],first_btjd=float(t.min()),last_btjd=float(t.max()),n=len(t),median_cadence_d=float(np.median(np.diff(t))),header=hdr,flags=[])
        for win in ff['windows']:
            if win['kind']!='dip' or not win['flag']:continue
            c=win['time'];dur=win['duration'];span=max(.9,3*dur)
            sel=np.abs(t-c)<span; x=t[sel]; z=y[sel]; zk=k[sel]
            if len(x)<8:continue
            baseline=((x<c-dur*.7)|(x>c+dur*.7))
            med=float(np.median(z[baseline])) if baseline.sum()>4 else float(np.median(z))
            kn=np.isfinite(zk)&(zk>0);kmed=float(np.median(zk[baseline&kn])) if (baseline&kn).sum()>4 else None
            norm=z/med; minidx=int(np.argmin(norm));center=float(x[minidx]);depth=float(1-norm[minidx]);
            core=np.abs(x-c)<dur/2
            gaps=np.diff(x)
            ev=dict(sector=ff['sector'],screen_btjd=c,screen_duration_d=dur,screen_depth_ppt=win['depth']*1000,raw_minimum_btjd=center,raw_minimum_depth_ppt=depth*1000,raw_median_core_depth_ppt=float((1-np.median(norm[core]))*1000) if core.any() else None,n_window=len(x),n_core=int(core.sum()),first_btjd=float(x.min()),last_btjd=float(x.max()),max_gap_d=float(gaps.max()) if len(gaps) else None,baseline_sap=med,kspsap_baseline=kmed,source_sha256=actual)
            secs['flags'].append(ev);events.append(ev)
            series.append(dict(sector=ff['sector'],screen_btjd=c,time=x.tolist(),sap_norm=norm.tolist(),kspsap_norm=(zk/kmed).tolist() if kmed else None))
        allout.setdefault(tic,dict(sample_id=sid,tic=tic,gaia_period_d=float(row['gaia_period']),gaia_dr3=row['gaia_dr3'],bulk_result=str(bulk),bulk_sha256=sha(bulk),source=[],sectors=[],flag_events=[]))
        allout[tic]['sectors'].append(secs)
    allout[tic]['source']=source;allout[tic]['flag_events']=events
    (dest/'lead-context.json').write_text(json.dumps(allout[tic],indent=2),encoding='utf8')
    (dest/'lead-series.json').write_text(json.dumps(series),encoding='utf8')
    picks=[]
    for sec in sorted({e['sector'] for e in events}):
        ss=[(j,e) for j,e in enumerate(events) if e['sector']==sec]
        if ss:picks.append(max(ss,key=lambda je:je[1]['screen_depth_ppt'])[0])
    if picks:
        fig,axs=plt.subplots(len(picks),1,figsize=(10,2.4*len(picks)),squeeze=False)
        for ax,j in zip(axs[:,0],picks):
            e=events[j];s=series[j];x=np.asarray(s['time'])-e['screen_btjd'];ax.plot(x,s['sap_norm'],'.',ms=2,label='raw SAP')
            if s['kspsap_norm'] is not None:ax.plot(x,s['kspsap_norm'],'.',ms=1,alpha=.4,label='KSPSAP same photons')
            ax.set_title(f"{sid} TIC {tic} S{e['sector']} BTJD {e['screen_btjd']:.3f}, raw min {e['raw_minimum_btjd']:.3f}")
            ax.set_xlim(-max(.9,e['screen_duration_d']*3),max(.9,e['screen_duration_d']*3));ax.set_ylabel('normalized flux');ax.grid(alpha=.2)
        axs[-1,0].set_xlabel('days from screen window');fig.tight_layout();fig.savefig(dest/'lead-raw-context.png',dpi=130);plt.close(fig)
    print(sid,tic,len(source),len(events),flush=True)
(B/'lead-source-hashes.json').write_text(json.dumps({t:{'bulk_sha256':d['bulk_sha256'],'source':d['source']} for t,d in allout.items()},indent=2),encoding='utf8')
