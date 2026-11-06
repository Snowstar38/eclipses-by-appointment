"""Independent local raw SAP fits of flagged dip windows; provisional timing diagnostics."""
from pathlib import Path
import csv,json,hashlib,math
import numpy as np
from astropy.io import fits
from scipy.optimize import least_squares
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent
H=B.parent.parent/'binary-exploration-2026-11-04'/'bulk-results'
def model(x,p):
    b,s,d,c,w,k=p
    return b+s*x-d*np.clip((w/2-np.abs(x-c))/k,0,1)
for row in csv.DictReader((B/'queue.csv').open(newline='',encoding='utf8')):
    tic=row['tic'];o=B/tic;bulk=json.loads((H/f'{tic}.json').read_text())
    events=[];panels=[]
    for rec in bulk['files']:
        flags=sorted((w for w in rec['windows'] if w['kind']=='dip' and w['flag']),key=lambda w:w['time'])
        if not flags:continue
        p=Path(rec['path']);assert hashlib.sha256(p.read_bytes()).hexdigest()==rec['sha256']
        with fits.open(p,memmap=False) as hd:
            a=hd[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
        z=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[z];f=f[z]
        cadence=float(np.median(np.diff(t)));f=f/np.median(f)
        for w in flags:
            duration=float(w['duration']);pred=float(w['time']); half=max(3*duration,.55)
            idx=abs(t-pred)<half;x=t[idx]-pred;y=f[idx]
            if len(x)<16:continue
            outer=abs(x)>max(.75*duration,.16)
            if sum(outer&(x<0))<4 or sum(outer&(x>0))<4:continue
            base=np.median(y[outer]);yn=y/base
            noise=max(1.4826*np.median(abs(yn[outer]-np.median(yn[outer]))),.0001)
            depth=min(max(1-np.quantile(yn[abs(x)<duration/2],.15),.001),.5)
            p0=[1,0,depth,0,max(duration,.1),max(duration*.2,.02)]
            lb=[.7,-.3,0,-duration,.02,.004];ub=[1.3,.3,.6,duration,min(3.,3*duration),max(1,2*duration)]
            fit=least_squares(lambda p:(model(x,p)-yn)/noise,p0,bounds=(lb,ub),max_nfev=3000,loss='soft_l1')
            pars=fit.x; depth_ppt=1000*pars[2]*min(1,pars[4]/(2*pars[5]))
            # Formal covariance only; model/systematic allowance reported separately.
            try: cov=np.linalg.inv(fit.jac.T@fit.jac);formal=float(np.sqrt(cov[3,3]))
            except:formal=None
            e={'sector':int(rec['sector']),'screen_btjd':pred,'screen_duration_days':duration,'mid_btjd':float(pred+pars[3]),'depth_ppt':float(depth_ppt),'duration_days':float(pars[4]),'ingress_parameter_days':float(pars[5]),'formal_center_error_days':formal,'cadence_days':cadence,'local_noise_ppt':float(noise*1000),'fit_cost':float(fit.cost),'n':len(x),'source_sha256':rec['sha256']}
            events.append(e);panels.append((e,x,yn,model(x,pars)))
    events.sort(key=lambda e:e['mid_btjd'])
    # Duplicate detector windows around one physical event are explicitly retained but marked.
    for i,e in enumerate(events): e['near_previous_same_event']=bool(i and e['mid_btjd']-events[i-1]['mid_btjd']<max(e['duration_days'],events[i-1]['duration_days']))
    (o/'fitted-windows.json').write_text(json.dumps({'tic':tic,'fit_scope':'flagged detector windows only; inspect raw plots and aliases before adoption','events':events},indent=2)+'\n')
    if panels:
        fig,ax=plt.subplots(len(panels),1,figsize=(10,max(3,2*len(panels))),squeeze=False)
        for a,(e,x,y,fit) in zip(ax[:,0],panels):
            a.plot(x,y,'.',ms=2);a.plot(x,fit,'r-',lw=1)
            a.set_title(f"S{e['sector']} fitted {e['mid_btjd']:.5f} depth {e['depth_ppt']:.1f} ppt; detector {e['screen_btjd']:.3f}",fontsize=8)
        fig.tight_layout();fig.savefig(o/'fitted-windows.png',dpi=110);plt.close(fig)
    print(tic,len(events),[(e['sector'],round(e['mid_btjd'],3),round(e['depth_ppt'],1)) for e in events],flush=True)
