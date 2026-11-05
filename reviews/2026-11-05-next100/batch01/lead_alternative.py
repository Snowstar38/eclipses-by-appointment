"""Compare the same observed photons in raw SAP and QLP KSPSAP near flagged events."""
import csv, hashlib, json
from pathlib import Path
import numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

B=Path(__file__).resolve().parent
for row in csv.DictReader((B/'queue.csv').open(newline='',encoding='utf-8')):
    tic=row['tic']; d=json.loads((B/tic/'lead-measurements.json').read_text(encoding='utf-8'))
    bysector={int(v['sector']):v for v in d['coverage']}
    source={int(Path(v['path']).stem.split('_s')[-1]):v for v in d['source_receipts']}
    result=[]; panels=[]
    for ev in d['screen_flagged_dips']:
        sec=int(ev['sector']); fp=Path(source[sec]['path']); assert hashlib.sha256(fp.read_bytes()).hexdigest()==source[sec]['sha256']
        center=ev.get('measured_center_btjd',ev['screen_center_btjd'])
        with fits.open(fp,memmap=False) as h:
            a=h[1].data
            if 'KSPSAP_FLUX' not in h[1].columns.names:
                result.append(dict(sector=sec,center_btjd=float(center),alternative_status='KSPSAP_FLUX absent',source_sha256=source[sec]['sha256']))
                continue
            t=np.asarray(a['TIME'],float);raw=np.asarray(a['SAP_FLUX'],float);alt=np.asarray(a['KSPSAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
        center=ev.get('measured_center_btjd',ev['screen_center_btjd']); radius=max(.4,min(1.5,ev.get('fit_width_days',.15)*3))
        ok=np.isfinite(t)&np.isfinite(raw)&np.isfinite(alt)&(raw>0)&(alt>0)&(q==0)&(abs(t-center)<radius)
        t=t[ok];raw=raw[ok];alt=alt[ok]
        if len(t)<12:continue
        oot=(abs(t-center)>max(.17,ev.get('fit_width_days',.1)*.8)); oot=oot if sum(oot)>10 else abs(t-center)>radius*.55
        entry=dict(sector=sec,center_btjd=float(center),points=len(t),source_sha256=source[sec]['sha256'],aperture_independence='same photons; alternative QLP reduction')
        plot=[]
        for name,flux in [('SAP',raw),('KSPSAP',alt)]:
            baseline=np.polyfit(t[oot]-center,flux[oot],1);norm=flux/np.polyval(baseline,t-center)
            core=abs(t-center)<max(.06,min(.16,ev.get('fit_width_days',.1)*.3))
            entry[name.lower()+'_core_depth_ppt']=float((1-np.median(norm[core]))*1000) if core.sum()>1 else None
            plot.append(norm)
        result.append(entry);panels.append((entry,t-center,plot))
    (B/tic/'lead-alternative.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    if panels:
        fig,axs=plt.subplots(len(panels),1,figsize=(9,2.2*len(panels)),squeeze=False)
        for ax,(entry,x,ys) in zip(axs[:,0],panels):
            ax.plot(x,ys[0],'.',ms=2,label='SAP');ax.plot(x,ys[1],'.',ms=2,label='KSPSAP')
            ax.set_title(f"S{entry['sector']} at {entry['center_btjd']:.4f}; SAP {entry['sap_core_depth_ppt']:.1f} ppt, KSPSAP {entry['kspsap_core_depth_ppt']:.1f} ppt",fontsize=9)
            ax.legend(fontsize=7)
        fig.tight_layout();fig.savefig(B/tic/'lead-alternative.png',dpi=115);plt.close(fig)
    print(row['sample_id'],len(result),flush=True)
