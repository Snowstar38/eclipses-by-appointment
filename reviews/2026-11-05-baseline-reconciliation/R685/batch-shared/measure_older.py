import hashlib,json
from pathlib import Path
import numpy as np
from astropy.io import fits
from scipy.optimize import curve_fit
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

here=Path(__file__).resolve().parent
downloads=json.loads((here/'older-qlp-downloads.json').read_text())
def model(t,b,s,amp,c,w,k):return b+s*(t-c)-amp*np.clip((w/2-abs(t-c))/k,0,1)
out=[]
for receipt in downloads:
    if receipt['status']!='ok':continue
    tic=receipt['tic'];sec=receipt['sector'];p=Path(receipt['path'])
    assert hashlib.sha256(p.read_bytes()).hexdigest()==receipt['sha256']
    summary=json.loads((here/tic/'measurements.json').read_text())
    kind='B' if tic=='109560492' else 'A';fit=summary['same_kind_fits'][kind]
    with fits.open(p) as h:
        a=h[1].data;t=np.array(a['TIME'],float);f=np.array(a['SAP_FLUX'],float);q=np.array(a['QUALITY'],int)
    ok=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[ok];f=f[ok]
    P=fit['period_days'];T0=fit['epoch_btjd'];n=round((np.median(t)-T0)/P)
    for cycle in range(n-1,n+2):
        tc=T0+cycle*P
        if not t.min()+.4<tc<t.max()-.4:continue
        ix=abs(t-tc)<1.;x=t[ix];y=f[ix]
        if len(x)<30:continue
        baseline=abs(x-tc)>.3
        if baseline.sum()<12:continue
        y=y/np.median(y[baseline]);noise=max(1.4826*np.median(abs(y[baseline]-np.median(y[baseline]))),1e-6)
        p0=[1,0,.05,tc,.2,.08]
        try:
            par,cov=curve_fit(model,x,y,p0=p0,bounds=([.7,-1,0,tc-.35,.03,.01],[1.3,1,1,tc+.35,.7,.5]),
                              sigma=np.full(len(x),noise),absolute_sigma=True,maxfev=30000)
            depth=float(par[2]*min(1,par[4]/(2*par[5]))*1000)
            result=dict(tic=tic,sector=sec,kind=kind,cycle=cycle,predicted_btjd=tc,
                        center_btjd=float(par[3]),depth_ppt=depth,duration_hours=float(par[4]*24),
                        formal_timing_error_days=float(np.sqrt(cov[3,3])),
                        cadence_days=float(np.median(np.diff(t))),
                        conservative_timing_error_days=max(float(np.sqrt(cov[3,3])),float(np.median(np.diff(t)))/2),
                        n=len(x),q0_fits_sha256=receipt['sha256'])
            out.append(result)
            fig,ax=plt.subplots(figsize=(8,3.4));ax.plot(x,y,'.',ms=2);xx=np.linspace(x.min(),x.max(),1000)
            ax.plot(xx,model(xx,*par),'r-');ax.axvline(tc,color='green',ls=':')
            ax.set_xlim(tc-.7,tc+.7);ax.set_title(f'TIC {tic} older s{sec} {kind}, {depth:.1f} ppt')
            ax.set_xlabel('BTJD');ax.set_ylabel('raw Q0 SAP / local baseline')
            fig.tight_layout();fig.savefig(here/tic/f'older-event-s{sec}.png',dpi=140);plt.close(fig)
        except Exception as e:out.append(dict(tic=tic,sector=sec,kind=kind,cycle=cycle,predicted_btjd=tc,error=repr(e)))
(here/'older-events.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
