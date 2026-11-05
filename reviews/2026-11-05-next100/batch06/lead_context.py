"""Reproduce raw and alternate-flux context for sealed Q051-Q060."""
import csv, hashlib, json
from pathlib import Path
import numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

B=Path(__file__).resolve().parent
ROOT=B.parent
for row in csv.DictReader((B/'queue.csv').open(encoding='utf8',newline='')):
    tic=row['tic']; sid=row['sample_id']; D=B/tic;D.mkdir(exist_ok=True)
    packet_path=ROOT/'source-packets'/tic/'sources.json'
    packet=json.loads(packet_path.read_text(encoding='utf8'))
    assert packet['queue_row']['sample_id']==sid
    bulk=Path(packet['bulk_result'])
    assert hashlib.sha256(bulk.read_bytes()).hexdigest()==packet['bulk_result_sha256']
    detector=json.loads(bulk.read_text(encoding='utf8'))
    recs={str(Path(v['path']).stem.split('_s')[-1]).lstrip('0'):v for v in packet['verified_files']}
    assert hashlib.sha256(packet_path.read_bytes()).hexdigest()==json.loads((ROOT/'source-packet-index.json').read_text())['targets'][tic]['sha256']
    fig,axs=plt.subplots(len(detector['files']),1,figsize=(15,2.8*len(detector['files'])),squeeze=False)
    report=[]; zoom=[]
    for ax,item in zip(axs[:,0],detector['files']):
        sec=int(item['sector']); src=recs[str(sec)]; fp=Path(src['path'])
        assert hashlib.sha256(fp.read_bytes()).hexdigest()==src['sha256']
        with fits.open(fp,memmap=False) as h:
            a=h[1].data;t0=np.asarray(a['TIME'],float);f0=np.asarray(a['SAP_FLUX'],float);q0=np.asarray(a['QUALITY'],int)
            alt0=np.asarray(a['KSPSAP_FLUX'],float) if 'KSPSAP_FLUX' in h[1].columns.names else None
        good=np.isfinite(t0)&np.isfinite(f0)&(f0>0)&(q0==0)
        t=t0[good];f=f0[good];alt=alt0[good] if alt0 is not None else None
        if len(t)<2:continue
        cad=float(np.median(np.diff(t))); base=float(np.median(f))
        # 0.05 day bins retain sub-day occultations while exposing sector-wide context.
        bins=np.floor((t-t.min())/.05).astype(int); _,inv=np.unique(bins,return_inverse=True)
        bt=np.bincount(inv,weights=t)/np.bincount(inv)
        bf=np.array([np.median(f[inv==k]) for k in range(len(bt))])/base
        ax.plot(bt,bf,'.',ms=2,color='#222222')
        flags=[w for w in item.get('windows',[]) if w.get('flag')]
        for w in flags:
            c=float(w['time']);ax.axvline(c,color='tab:red' if w['kind']=='dip' else 'tab:blue',lw=.7,alpha=.7)
            rad=max(.35,min(1.5,1.5*float(w['duration'])))
            local=(t>=c-rad)&(t<=c+rad)
            tt=t[local];ff=f[local];aa=alt[local] if alt is not None else None
            z=dict(sector=sec,kind=w['kind'],screen_center_btjd=c,screen_duration_days=float(w['duration']),
                   raw_time=tt.tolist(),raw_sap_flux=ff.tolist(),raw_kspsap_flux=aa.tolist() if aa is not None else None,
                   local_points=int(local.sum()),local_first_btjd=float(tt.min()) if len(tt) else None,
                   local_last_btjd=float(tt.max()) if len(tt) else None,
                   local_gaps_over_3cadences=[[float(tt[i]),float(tt[i+1])] for i in np.where(np.diff(tt)>3*cad)[0]],
                   source_sha256=src['sha256'])
            zoom.append(z)
        gaps=np.where(np.diff(t)>3*cad)[0]
        report.append(dict(sector=sec,source_path=str(fp),source_sha256=src['sha256'],time_start_btjd=float(t.min()),time_end_btjd=float(t.max()),cadence_days=cad,
                           quality0_positive_points=len(t),all_rows=len(t0),raw_flux_median=base,
                           gaps_over_3cadences=[[float(t[i]),float(t[i+1])] for i in gaps],
                           flags=[dict(kind=w['kind'],screen_center_btjd=float(w['time']),duration_days=float(w['duration']),contrast=float(w['contrast']),depth_fraction=float(w['depth'])) for w in flags],
                           strongest_unflagged=[dict(kind=w['kind'],center_btjd=float(w['time']),duration_days=float(w['duration']),contrast=float(w['contrast'])) for w in sorted([w for w in item.get('windows',[]) if not w.get('flag')],key=lambda w:w.get('contrast',0),reverse=True)[:8]]))
        ax.set_title(f'{sid} TIC {tic} S{sec} SAP / median; red dip flags, blue bright flags',fontsize=10)
        ax.set_ylabel('normalized flux');ax.set_xlim(t.min(),t.max())
        p1,p99=np.percentile(bf,[1,99]);pad=max(.002,(p99-p1)*.25);ax.set_ylim(p1-pad,p99+pad)
    fig.tight_layout();fig.savefig(D/'lead-raw-context.png',dpi=120);plt.close(fig)
    (D/'lead-context.json').write_text(json.dumps(dict(sample_id=sid,tic=tic,packet_sha256=hashlib.sha256(packet_path.read_bytes()).hexdigest(),bulk_sha256=packet['bulk_result_sha256'],sectors=report),indent=2)+'\n',encoding='utf8')
    # Numeric local time series allows independent replotting and direct core/gap checks.
    (D/'lead-local-series.json').write_text(json.dumps(zoom,separators=(',',':'))+'\n',encoding='utf8')
    dip=[z for z in zoom if z['kind']=='dip']
    if dip:
        fig,axs=plt.subplots(len(dip),1,figsize=(10,2.25*len(dip)),squeeze=False)
        for ax,z in zip(axs[:,0],dip):
            t=np.array(z['raw_time']);raw=np.array(z['raw_sap_flux']);alt=np.array(z['raw_kspsap_flux']) if z['raw_kspsap_flux'] is not None else None
            c=z['screen_center_btjd']; x=t-c; outer=np.abs(x)>max(.15,z['screen_duration_days']*.55)
            if outer.sum()<5:outer=np.abs(x)>np.max(np.abs(x))*.6
            if outer.sum()>4:
                ax.plot(x,raw/np.median(raw[outer]),'.',ms=2,label='SAP')
                if alt is not None and np.count_nonzero(np.isfinite(alt)&(alt>0)&outer)>4:
                    ax.plot(x,alt/np.median(alt[outer]),'.',ms=2,alpha=.65,label='KSPSAP')
            ax.axvline(0,color='k',lw=.5);ax.set_title(f"{sid} S{z['sector']} predicted {c:.4f}; {z['local_points']} good points",fontsize=9);ax.legend(fontsize=7)
            ax.set_ylabel('flux / outer median')
        fig.tight_layout();fig.savefig(D/'lead-dip-zooms.png',dpi=120);plt.close(fig)
    print(sid,tic,len(report),'sectors',len(dip),'dip flags',flush=True)

