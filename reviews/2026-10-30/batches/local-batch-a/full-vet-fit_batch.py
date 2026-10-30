"""Independent raw-SAP fits. Grid trapezoids + polynomial baseline, numpy only.
No detrended QLP columns. Exposure integration, red-noise inflation, conservative
grid errors. Full outputs retain all coverage exclusions. Run from any cwd.
"""
from pathlib import Path
import json,sys
import numpy as np
from astropy.io import fits
ROOT=Path(__file__).parent; INPUT=ROOT.parent
targets=json.load(open(INPUT/'targets-selected.json'))
search={x['tic']:x['P'] for x in json.load(open(INPUT/'receipts.json'))['search.jsonl']}
def trap(x,T,fr,cad=0):
    # Seven sub-exposure samples suppress cadence-smearing bias.
    xx=np.abs(np.asarray(x)[:,None]+np.linspace(-.5,.5,7)[None,:]*cad)
    return np.mean(np.clip((T/2-xx)/max(fr*T,1e-6),0,1),axis=1)
def mad(x):return max(float(1.4826*np.median(abs(x-np.median(x)))),1e-7)
def linear(x,y,shape,deg=2,extra=None):
    A=np.column_stack([x**k for k in range(deg+1)]+[-shape]+([] if extra is None else [extra]))
    c=np.linalg.lstsq(A,y,rcond=None)[0];res=y-A@c
    dof=max(len(x)-A.shape[1],1); s2=np.sum(res**2)/dof
    cov=np.linalg.pinv(A.T@A)*s2
    return float(np.sum(res**2)),c,res,cov
def read(tic):
    out=[]
    for fn in sorted((INPUT/'data').glob(tic+'_s*.fits')):
        with fits.open(fn,memmap=False) as h:
            d=h[1].data; t=np.array(d['TIME'],float);f=np.array(d['SAP_FLUX'],float);q=np.array(d['QUALITY'],int)
            valid=np.isfinite(t)&np.isfinite(f)&(f>0)
            g=lambda n:np.array(d[n],float)[valid] if n in d.columns.names else np.full(valid.sum(),np.nan)
            t,f,q=t[valid],f[valid],q[valid];med=np.median(f[q==0]);f=f/med
            out.append(dict(t=t,f=f,q=q,b=g('SAP_BKG'),x=g('SAP_X'),y=g('SAP_Y'),sec=int(fn.stem[-3:]),cad=float(np.median(np.diff(t)))))
    return out
def cut(s,tc,w):
    m=(abs(s['t']-tc)<w)&(s['q']==0)
    return s['t'][m]-tc,s['f'][m],m
def shape_fit(secs,P,t0,d):
    cuts=[]
    for s in secs:
        phase=(s['t']-t0+P/2)%P-P/2
        m=(s['q']==0)&(abs(phase)<min(.36*P,max(.5,4*d)))
        # Local event polynomial is fitted per cycle, so low-frequency and orbital
        # modulation cannot be mistaken for a global baseline.
        for n in sorted(set(np.round((s['t'][m]-t0)/P).astype(int))):
            x,y,_=cut(s,t0+n*P,min(.30*P,max(.4,3*d)))
            if sum(abs(x)<d/2)<3 or sum(x<-d)<5 or sum(x>d)<5:continue
            cuts.append((x,y,s['cad']))
    best=None; scores=[]
    for T in np.linspace(.55*d,2.3*d,30):
      for fr in [.08,.15,.25,.35,.45,.5]:
       for shift in [-.01,0,.01]:
        chi=0;nd=0
        for x,y,cad in cuts:
            a=linear(x/max(.4,3*d),y,trap(x-shift,T,fr,cad));chi+=a[0];nd+=len(y)-4
        scores.append((chi,T,fr,shift,nd))
        if best is None or chi<best[0]:best=scores[-1]
    sig2=best[0]/max(best[4],1)
    allowed=[x for x in scores if (x[0]-best[0])/sig2<=3.53]
    step=(2.3-.55)*d/29
    return dict(T14=best[1],fr=best[2],shift=best[3],T14_range=[min(x[1] for x in allowed)-step/2,max(x[1] for x in allowed)+step/2],fr_range=[max(0,min(x[2] for x in allowed)-.04),min(.5,max(x[2] for x in allowed)+.04)],n_local_windows=len(cuts),error_note='profile likelihood plus half-grid resolution; conditional shape model')
def event(s,tc,T,fr,scan=True,deg=2):
    w=min(max(3*T,.32),.35*P);x,y,m=cut(s,tc,w)
    inn=abs(x)<T/2
    # QUALITY can select alternate cadences; coverage is relative to the
    # clean-cadence sampling, while integration retains native exposure length.
    expected=T/float(np.median(np.diff(s['t'][s['q']==0])))
    if sum(inn)<max(3,.6*expected) or sum(x<-T*.65)<5 or sum(x>T*.65)<5:return dict(status='insufficient',tc_nom=tc,sec=s['sec'],n_in=int(sum(inn)))
    grid=np.linspace(-.3*T,.3*T,101) if scan else np.array([0.])
    best=None;chis=[]
    for shift in grid:
        a=linear(x/w,y,trap(x-shift,T,fr,s['cad']),deg)
        chis.append(a[0])
        if best is None or a[0]<best[0]:best=(a[0],shift,*a[1:])
    chi,shift,c,res,cov=best; sigma2=chi/max(len(x)-deg-3,1)
    # Bin-residual beta over 20/40/60 min, with lower floor 1. No shuffling
    # of temporally correlated points or fictitiously precise timing errors.
    beta=1.
    for minutes in [20,40,60]:
        nb=max(2,int(minutes/1440/s['cad'])); nr=len(res)//nb
        if nr>=3:
            br=res[:nr*nb].reshape(nr,nb).mean(axis=1)
            beta=max(beta,float(np.std(br,ddof=1)/(max(np.std(res,ddof=1),1e-7)/np.sqrt(nb))*np.sqrt((nr-1)/nr)))
    dc=(np.array(chis)-chi)/max(sigma2,1e-14)/beta**2
    ok=grid[dc<=1]; terr=max((max(ok)-min(ok))/2 if len(ok) else 0, .003*T, s['cad']/np.sqrt(12*max(sum(inn),1)))
    # Native background regression projected through SAME template gives a
    # unit-free fake depth, and refit with normalized background checks stability.
    b=s['b'][m]; bg=np.isfinite(b); fake=None;dep_bg=None
    if sum(bg)>10 and np.std(b[bg])>0:
        xx=x[bg]/w; yy=y[bg]; bb=(b[bg]-np.median(b[bg]))/np.std(b[bg]);tt=trap(x[bg]-shift,T,fr,s['cad'])
        oot=tt==0
        if sum(oot)>10:
            X=np.column_stack([xx[oot]**k for k in range(deg+1)]+[bb[oot]])
            bc=np.linalg.lstsq(X,yy[oot],rcond=None)[0][-1]
            fake=float(linear(xx,bc*bb,tt,deg)[1][-1]);dep_bg=float(linear(xx,yy,tt,deg,bb)[1][deg+1])
    core=(abs(s['t']-tc-shift)<T/2);q=s['q'][core]
    cent={}
    for nm in ['x','y']:
        z=s[nm][m];zok=np.isfinite(z)
        if sum(zok)>10:
            zz=linear(x[zok]/w,z[zok],trap(x[zok]-shift,T,fr,s['cad']),1)
            cent[nm+'_template_shift_pix']=-float(zz[1][-1]);cent[nm+'_err_pix']=float(np.sqrt(zz[3][-1,-1])*beta)
    return dict(status='fit',sec=s['sec'],tc_nom=tc,tc=tc+shift,tc_error=terr,depth=float(c[deg+1]),depth_error=float(np.sqrt(cov[deg+1,deg+1])*beta),T14=T,T12=fr*T,T23=T*(1-2*fr),beta=beta,n_in=int(sum(inn)),flagged_core=int(sum(q!=0)),flag_bits_core=int(np.bitwise_or.reduce(q,initial=0)),background_fake_depth=fake,depth_with_background=dep_bg,scan_edge=bool(abs(shift)>=.299*T),**cent)
def ephemeris(rows,P0,t0):
    a=[r for r in rows if r['status']=='fit' and r['depth']>3*r['depth_error'] and not r['scan_edge']]
    E=np.array([r['cycle'] for r in a]);t=np.array([r['tc'] for r in a]);er=np.array([r['tc_error'] for r in a]);ref=int(np.round(np.mean(E)));x=E-ref
    A=np.column_stack([np.ones(len(x)),x]);w=1/er**2;cov=np.linalg.inv(A.T@(w[:,None]*A));c=cov@(A.T@(w*t));res=t-A@c;chi=float(sum((res/er)**2));scale=max(1,chi/max(len(t)-2,1));cov*=scale
    for r,oc in zip(a,res):r['oc_days']=float(oc)
    return dict(P=float(c[1]),P_error=float(np.sqrt(cov[1,1])),Tref=float(c[0]),Tref_error=float(np.sqrt(cov[0,0])),reference_cycle=ref,T0=float(c[0]-ref*c[1]),chi2=chi,dof=len(t)-2,n=len(t),oc_rms_minutes=float(np.std(res)*1440))
def census(secs,P,t0,T):
    # Blind sector-local rolling median; identify contiguous runs below a
    # threshold, retaining raw events and gaps. Not a narrow-template phase scan.
    out=[]
    for s in secs:
        good=s['q']==0;t=s['t'][good];f=s['f'][good];rr=np.empty(len(t));span=max(4*T,.5)
        for i,ti in enumerate(t):
            l=np.searchsorted(t,ti-span);r=np.searchsorted(t,ti+span);rr[i]=f[i]-np.median(f[l:r])
        noise=mad(np.diff(rr))/np.sqrt(2);threshold=max(4*noise,.003)
        hit=np.flatnonzero(rr<-threshold);groups=[]
        for i in hit:
            if not groups or t[i]-t[groups[-1][-1]]>max(2*s['cad'],T*.2):groups.append([i])
            else:groups[-1].append(i)
        for ids in groups:
            if len(ids)<2:continue
            weights=-rr[ids];tc=float(np.average(t[ids],weights=weights));phase=float(((tc-t0)/P)%1)
            out.append(dict(sec=s['sec'],tc=tc,depth=float(-min(rr[ids])),n=len(ids),phase=phase,threshold=threshold,duration=float(t[ids[-1]]-t[ids[0]]+s['cad'])))
    return out
if __name__=='__main__':
 for tic in (sys.argv[1:] or list(search)):
    dest=ROOT/tic;dest.mkdir(exist_ok=True);p=search[tic];P=p['P'];t0=p['t0'];secs=read(tic)
    shape=shape_fit(secs,P,t0,p['dur']);print(tic,'shape',shape,flush=True)
    rows=[]
    for s in secs:
      for n in range(int(np.ceil((s['t'].min()-t0)/P)),int(np.floor((s['t'].max()-t0)/P))+1):
        r=event(s,t0+n*P+shape['shift'],shape['T14'],shape['fr']);r['cycle']=n;rows.append(r)
    eph=ephemeris(rows,P,t0);print(tic,'ephemeris',eph,flush=True)
    out=dict(tic=tic,shape=shape,events=rows,ephemeris=eph,census=census(secs,eph['P'],eph['T0'],shape['T14']))
    json.dump(out,open(dest/'fit-results.json','w'),indent=2)
