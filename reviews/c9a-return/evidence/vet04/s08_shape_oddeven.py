# (a) stacked shape (T14, T23) of primary and secondary from 200-s/600-s data, local quadratic baselines removed per event
# (b) fixed-shape refits of every event, every pipeline (t0, depth, quadratic baseline free) -> depth table
# (c) odd/even primary depths; depth at phase 0.5 (should be nothing for star 1)
from common import *; from fitlib import *; import json
rows=json.load(open('s04_events.json')); res={}
for tic in GAIA:
    eph=json.load(open(f's05_ephem_{tic}.json')); P=eph['P']
    win=0.7 if tic=='283532878' else 0.8
    S=load(tic)
    shape={}
    for kind,T0,T14g,dg in (('P',eph['T0P'],0.29,0.07 if tic=='283532878' else 0.027),('S',eph['T0S'],0.29 if tic=='283532878' else 0.38,0.01 if tic=='283532878' else 0.003)):
        X=[];Y=[]
        for s in S:
            if s['author']!='QLP': continue
            te=np.median(np.diff(s['t']))
            if te>0.005: continue   # 200-s sectors only for the shape
            t,f=s['t'],s['f']
            n=np.round((t-T0)/P); 
            for k in np.unique(n):
                tc=T0+k*P; m=np.abs(t-tc)<win
                if m.sum()<100: continue
                oot=m&(np.abs(t-tc)>T14g/2+0.06)
                if oot[m].sum()<50 or np.sum(m&(np.abs(t-tc)<T14g/2))<30: continue
                c=np.polyfit(t[oot]-tc,f[oot],2); X.append(t[m]-tc); Y.append(f[m]/np.polyval(c,t[m]-tc))
        X=np.concatenate(X);Y=np.concatenate(Y)
        r=fit_event(X,Y,0.0,0.0,dg,T14g,win,fix={'c1':0,'c2':0})
        p,e=r['p'],r['e']
        print(tic,kind,'STACK(200s QLP) t0off=%.4f±%.4f d=%.2f±%.2fppt T14=%.3f±%.3fh T23=%.3f±%.3fh (T23/T14=%.3f) npts=%d rms=%.2fppt'%(p['t0'],e['t0'],1e3*p['d'],1e3*e['d'],24*p['T14'],24*e['T14'],24*p['T14']*p['r23'],24*np.hypot(e['T14']*p['r23'],p['T14']*e['r23']),p['r23'],len(X),1e3*r['rms']))
        shape[kind]=dict(T14=p['T14'],r23=p['r23'],d=p['d'],ed=e['d'],eT14=e['T14'])
        np.savez(f's08_stack_{tic}_{kind}.npz',x=X,y=Y)
    res[tic]=dict(shape=shape)
    # (b) fixed-shape refits
    out=[]
    for s in S:
        te=float(np.median(np.diff(s['t']))); t,f=s['t'],s['f']
        for kind,T0 in (('P',eph['T0P']),('S',eph['T0S'])):
            sh=shape[kind]
            for k in range(int((t.min()-T0)/P)-1,int((t.max()-T0)/P)+2):
                tc=T0+k*P
                if tc<t.min()-0.1 or tc>t.max()+0.1: continue
                inn=np.abs(t-tc)<sh['T14']/2; pre=np.sum((t<tc-sh['T14']/2)&(t>tc-win)); post=np.sum((t>tc+sh['T14']/2)&(t<tc+win))
                if inn.sum()*te/sh['T14']<0.6 or pre<5 or post<5: 
                    if inn.sum()>0: print('  skip partial',tic,s['author'],s['sector'],kind,k,'cov=%.2f pre=%d post=%d'%(inn.sum()*te/sh['T14'],pre,post))
                    continue
                r=fit_event(t,f,te,tc,sh['d'],sh['T14'],win,fix={'T14':sh['T14'],'r23':sh['r23']})
                p,e=r['p'],r['e']
                out.append(dict(author=s['author'],sector=int(s['sector']),kind=kind,n=k,t0=p['t0'],et0=e['t0'],d=p['d'],ed=e['d'],rms=r['rms'],beta=r['beta'],texp=te))
                print('  FIX',tic,s['author'],'s%d'%s['sector'],kind,k,'t0=%.4f±%.4f depth=%.2f±%.2f ppt (beta %.2f)'%(p['t0'],e['t0'],1e3*p['d'],1e3*e['d'],r['beta']))
            # phase 0.5 test (primary-relative) for star 1, phase 0.5 nothing expected
        if tic=='283532878':
            for k in range(int((t.min()-eph['T0P'])/P)-1,int((t.max()-eph['T0P'])/P)+2):
                tc=eph['T0P']+(k+0.5)*P
                if np.sum(np.abs(t-tc)<0.15)<10 or np.sum(np.abs(t-tc)<0.7)<60: continue
                r=fit_event(t,f,te,tc,0.001,shape['P']['T14'],0.7,fix={'T14':shape['P']['T14'],'r23':shape['P']['r23'],'t0':tc})
                print('  PH0.5',tic,s['author'],'s%d'%s['sector'],k,'depth at phase 0.5 (primary shape, fixed time) = %.2f±%.2f ppt'%(1e3*r['p']['d'],1e3*r['e']['d']))
    res[tic]['fixed']=out
    # (c) odd/even on primaries; one measurement per event (TESS-SPOC preferred for depth? report both)
    for au in ('QLP','TESS-SPOC'):
        E=[o for o in out if o['kind']=='P' and o['author']==au]
        if len(E)<2: continue
        for par,lab in ((0,'even'),(1,'odd')):
            Z=[o for o in E if o['n']%2==par]
            if not Z: continue
            d=np.array([o['d'] for o in Z]); ed=np.array([o['ed'] for o in Z]); w=1/ed**2
            mu=np.sum(w*d)/np.sum(w); emu=1/np.sqrt(np.sum(w)); chi=np.sum(w*(d-mu)**2)
            print('ODDEVEN',tic,au,lab,'N=%d mean depth=%.2f±%.2f ppt (chi2=%.1f/%d; scatter %.2f ppt)'%(len(Z),1e3*mu,1e3*emu,chi,len(Z)-1,1e3*np.std(d)))
json.dump(res,open('s08_shape_oddeven.json','w'),indent=1)
