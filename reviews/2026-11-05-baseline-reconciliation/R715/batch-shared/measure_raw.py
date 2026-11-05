"""Bounded same-kind raw QLP SAP event extraction from the sealed review9 queue."""
import csv, hashlib, json, math, sys
from pathlib import Path
import numpy as np
from astropy.io import fits
from scipy.optimize import curve_fit
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

B=Path(__file__).resolve().parent
D=json.loads((B/'SOURCE-SNAPSHOT.json').read_text(encoding='utf-8'))
Q=list(csv.DictReader((B/'queue.csv').open(encoding='utf-8',newline='')))

def model(x,b,s,d,c,w,k):
    return b+s*x-d*np.clip((w/2-np.abs(x-c))/k,0,1)

for row in Q:
    if len(sys.argv)>1 and row['tic'] not in sys.argv[1:]:continue
    tic=row['tic']; o=B/tic; o.mkdir(exist_ok=True)
    src=D[tic]; seed=src['screen']['P']; P=float(seed['P']); t0=float(seed['t0']); dur=float(seed['dur'])
    if tic=='449012335': dur=1.8
    if tic=='25320385': P=P/3
    events=[]; panels=[]; cover=[]
    receipts=src['target']['file_receipts']; selected=[receipts[i] for i in sorted(set(np.linspace(0,len(receipts)-1,min(6,len(receipts))).astype(int)))]
    for receipt in selected:
        fp=Path(receipt['path']); actual=hashlib.sha256(fp.read_bytes()).hexdigest()
        if actual!=receipt['sha256']: raise RuntimeError(f'source hash mismatch {fp}')
        with fits.open(fp,memmap=False) as h:
            a=h[1].data; t=np.asarray(a['TIME'],float); f=np.asarray(a['SAP_FLUX'],float); qual=np.asarray(a['QUALITY'],int)
        good=np.isfinite(t)&np.isfinite(f)&(f>0)&(qual==0); t=t[good];f=f[good]
        if len(t)<20: continue
        cadence=float(np.median(np.diff(t))); cover.append(dict(sector=receipt['sector'],first_btjd=float(t.min()),last_btjd=float(t.max()),cadence_days=cadence,n=len(t)))
        for n in range(math.ceil((t.min()-t0)/P),math.floor((t.max()-t0)/P)+1):
            pred=t0+n*P; half=max(4*dur,0.65); ix=np.abs(t-pred)<half
            x=t[ix]-pred;y=f[ix]
            if len(x)<15: continue
            oot=np.abs(x)>max(1.7*dur,0.25)
            if sum(oot&(x<0))<4 or sum(oot&(x>0))<4: continue
            y=y/np.median(y[oot]); noise=max(1.4826*np.median(abs(y[oot]-np.median(y[oot]))),1e-6)
            # Fit only if there is a local deficit above noise in the predicted eclipse neighborhood.
            core=np.abs(x)<max(1.2*dur,.12)
            if sum(core)<2:continue
            signal=float(1-np.median(np.sort(y[core])[:max(2,sum(core)//3)]))
            if signal<max(3*noise,.001):continue
            try:
                pars,cov=curve_fit(model,x,y,p0=[1,0,min(max(signal,.001),.8),0,max(dur,.08),max(dur*.2,.015)],bounds=([.7,-.5,0,-max(.5,2*dur),.03,.005],[1.3,.5,.95,max(.5,2*dur),min(5.0,8*dur),1.0]),sigma=np.full(len(x),noise),absolute_sigma=True,maxfev=30000)
                formal=float(np.sqrt(cov[3,3])) if cov[3,3]>0 else float('nan')
                depth=float(pars[2]*min(1,pars[4]/(2*pars[5]))*1000)
                usable=bool(np.isfinite(formal) and formal<max(dur,.15) and depth>max(3*noise*1000,1))
                e=dict(sector=receipt['sector'],cycle=n,predicted_btjd=pred,mid_btjd=float(pred+pars[3]),formal_timing_error_days=formal,timing_error_days=max(formal,cadence/2) if usable else None,timing_usable=usable,depth_ppt=depth,model_amplitude_ppt=float(pars[2]*1000),duration_days=float(pars[4]),ingress_parameter_days=float(pars[5]),oot_scatter_ppt=float(noise*1000),n=len(x),cadence_days=cadence,source_sha256=actual)
                events.append(e);panels.append((e,x,y,model(x,*pars)))
            except Exception as exc: events.append(dict(sector=receipt['sector'],cycle=n,fit_error=str(exc)))
    good=[e for e in events if e.get('timing_usable')]
    summary=dict(tic=tic,gaia_source_id=src['target']['gaia']['source_id'],screen_period_days=P,screen_epoch_btjd=t0,screen_duration_days=dur,source_receipts=src['target']['file_receipts'],coverage=cover,events=events,timing_event_count=len(good),epoch_kind='Selected repeating eclipse; primary/secondary identity assessed separately',depth_meaning='Median realized central loss of fitted trapezoid d*min(1,w/(2*k)); model amplitude separately retained.')
    if len(good)>=2:
        n=np.array([e['cycle'] for e in good]);tt=np.array([e['mid_btjd'] for e in good]);er=np.array([e['timing_error_days'] for e in good]);X=np.column_stack([np.ones(len(n)),n-n.min()]);A=X/er[:,None];C=np.linalg.inv(A.T@A);beta=C@(A.T@(tt/er));res=tt-X@beta;red=float(np.sum((res/er)**2)/(len(n)-2)) if len(n)>2 else None;C*=max(red or 1,1)
        summary.update(period_days=float(beta[1]),period_error_days=float(np.sqrt(C[1,1])),reference_epoch_btjd=float(beta[0]),epoch_error_days=float(np.sqrt(C[0,0])),reference_cycle=int(n.min()),reduced_chi_square=red,timing_residual_days=res.tolist(),depth_ppt=float(np.median([e['depth_ppt'] for e in good])),timing_error_meaning='Linear same-kind event fit, individual max(formal center covariance, half cadence), scatter-inflated covariance if reduced chi square > 1; excludes uncalibrated model/pipeline systematics.')
    (o/'measurements.json').write_text(json.dumps(summary,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    if panels:
        picks=np.linspace(0,len(panels)-1,min(9,len(panels))).astype(int);fig,axs=plt.subplots(len(picks),1,figsize=(9,2.1*len(picks)),squeeze=False)
        for ax,i in zip(axs[:,0],picks):
            e,x,y,fit=panels[i];ax.plot(x,y,'.',ms=2);ax.plot(x,fit,'r-',lw=1);ax.set_title(f"s{e['sector']} cycle {e['cycle']} depth {e['depth_ppt']:.2f} ppt at {e['mid_btjd']:.5f}",fontsize=9);ax.set_xlim(-max(3*dur,.4),max(3*dur,.4));ax.set_ylabel('raw SAP / OOT')
        fig.tight_layout();fig.savefig(o/'raw-events.png',dpi=110);plt.close(fig)
    print(tic,len(good),summary.get('period_days'),summary.get('depth_ppt'),flush=True)
