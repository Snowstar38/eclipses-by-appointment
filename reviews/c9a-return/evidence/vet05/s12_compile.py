# Master event table per star (QLP SAP, TESS-SPOC SAP from s7; own TESScut 3x3 / r2.5 from s11),
# eclipse-only ephemerides with all events, per-sector depths per pipeline, dilution-corrected depths, odd/even.
import json, glob, numpy as np
s7=json.load(open('s7_events.json'))
s11={}
for f in sorted(glob.glob('s11_*_s*.json')):
    d=json.load(open(f))
    if d['tic']=='15855794' and d['sector']==70 and 'exclE124' not in f:
        pass  # photometry identical in both s70 runs; diff image from the exclE124 run is used
    if 'exclE124' in f: continue
    s11[(d['tic'],d['sector'])]=d
gaia={'15855794':(5.89053844070554700,1.1329550e-03),'92881948':(8.80436043401770618,1.4405058e-03)}
out={}
def wmean(x,e):
    x=np.array(x);e=np.array(e);w=1/e**2;m=np.sum(w*x)/np.sum(w);em=1/np.sqrt(np.sum(w))
    chi2=np.sum(((x-m)/e)**2); return m,em,chi2,len(x)-1
def linfit(E,T,s,extra=None):
    cols=[np.ones_like(E),E]+([extra] if extra is not None else [])
    A=np.vstack(cols).T; W=np.diag(1/s**2); C=np.linalg.inv(A.T@W@A); b=C@A.T@W@T
    res=T-A@b; chi2=np.sum((res/s)**2); dof=len(T)-A.shape[1]; sc=max(1,np.sqrt(chi2/dof)) if dof>0 else 1
    return b,np.sqrt(np.diag(C))*sc,res,chi2,dof
for tic in ['15855794','92881948']:
    print('='*20,'TIC',tic)
    ev={}
    for r in s7:
        if r['tic']!=tic: continue
        k=(r['kind'],r['epoch']); ev.setdefault(k,dict(kind=r['kind'],epoch=r['epoch'],sector=r['sector'],tpred=r['tpred'],meas={},lost=[]))
        if 'tc' in r and r['status']=='OK': ev[k]['meas'][r['pipe']]=dict(tc=r['tc'],etc=r['etc'],dep=r['dep'],edep=r['edep'],cad=r['texp_min'])
        elif 'tc' in r: ev[k]['meas'][r['pipe']+'(partial)']=dict(tc=r['tc'],etc=r['etc'],dep=r['dep'],edep=r['edep'],cad=r['texp_min'])
        else: ev[k]['lost'].append(f"{r['pipe']}: {r['n_in_q0']}/{r['n_in_all']} Q0/any pts in T14")
    tfrac={}
    for (t_,sec),d in s11.items():
        if t_!=tic: continue
        tf={a:d['dilution'][a]['sig'][0]['frac_in_ap'] for a in ['3x3','r2.5']}
        tfrac[sec]=tf
        for e in d['events']:
            k=(e['kind'],e['epoch']); ev.setdefault(k,dict(kind=e['kind'],epoch=e['epoch'],sector=sec,tpred=e['tpred'],meas={},lost=[]))
            if e['status']=='OK':
                for a in ['3x3','r2.5']:
                    ev[k]['meas']['TESScut-'+a]=dict(tc=e[a]['tc'],etc=e[a]['etc'],dep=e[a]['dep'],edep=e[a]['edep'],cad=d['cad_min'],tfrac=tf[a])
            else: ev[k]['lost'].append(f"TESScut: {e['n_in']}/{e['n_in_expected']:.0f} Q0 pts in T14")
    keys=sorted(ev,key=lambda k:ev[k]['tpred'])
    print('# Event table. depth ppt (raw, not dilution-corrected); mid BTJD from best pipeline (TESS-SPOC > QLP > TESScut-3x3)')
    best=[]
    for k in keys:
        e=ev[k]; m=e['meas']
        pref=[p for p in ['TESS-SPOC','QLP','TESScut-3x3'] if p in m]
        line=f"{e['kind']} E{e['epoch']:<4d} s{e['sector']:<4d} pred {e['tpred']:.4f} | "
        if pref:
            b=m[pref[0]]; best.append(dict(kind=e['kind'],epoch=e['epoch'],tc=b['tc'],etc=b['etc'],pipe=pref[0],sector=e['sector']))
            line+=f"mid {b['tc']:.5f}±{b['etc']:.5f} [{pref[0]}] | "+' '.join(f"{p}={1e3*v['dep']:.2f}±{1e3*v['edep']:.2f}" for p,v in m.items())
        else: line+='NO USABLE DATA ('+'; '.join(e['lost'])+')'
        if pref and e['lost']: line+=' | lost in: '+'; '.join(e['lost'])
        print(line)
    # per-sector depths per pipeline (weighted means), and dilution-corrected TESScut depths
    print('# Per-sector weighted-mean depths (ppt); TESScut also divided by modelled target flux fraction in aperture')
    secs=sorted(set(ev[k]['sector'] for k in keys))
    persec={}
    for kind in 'PS':
        for sec in secs:
            row={}
            for p in ['QLP','TESS-SPOC','TESScut-3x3','TESScut-r2.5']:
                L=[ev[k]['meas'][p] for k in keys if ev[k]['kind']==kind and ev[k]['sector']==sec and p in ev[k]['meas']]
                if L:
                    m_,em,c2,dof=wmean([x['dep'] for x in L],[x['edep'] for x in L]); row[p]=(m_,em,len(L))
                    if p.startswith('TESScut'): row[p+'/frac']=(m_/L[0]['tfrac'],em/L[0]['tfrac'],len(L))
            if row:
                persec[f'{kind}_s{sec}']={p:list(v) for p,v in row.items()}
                print(f'  {kind} s{sec}: '+' | '.join(f'{p} {1e3*v[0]:.2f}±{1e3*v[1]:.2f} (n={v[2]})' for p,v in row.items()))
    out[tic+'_persector']=persec
    # all-pipeline consistency of the overall depth
    for kind in 'PS':
        for p in ['QLP','TESS-SPOC','TESScut-3x3','TESScut-r2.5']:
            L=[ev[k]['meas'][p] for k in keys if ev[k]['kind']==kind and p in ev[k]['meas']]
            if not L: continue
            m_,em,c2,dof=wmean([x['dep'] for x in L],[x['edep'] for x in L])
            line=f'  ALL {kind} {p}: {1e3*m_:.2f}±{1e3*em:.2f} ppt n={len(L)} chi2/dof={c2:.1f}/{dof}'
            if p.startswith('TESScut'):
                mc,emc,c2c,_=wmean([x['dep']/x['tfrac'] for x in L],[x['edep']/x['tfrac'] for x in L]); line+=f' ; /target-frac -> {1e3*mc:.2f}±{1e3*emc:.2f} ppt'
                out[f'{tic}_{kind}_{p}_corr']=[mc,emc]
            out[f'{tic}_{kind}_{p}']=[m_,em,len(L),c2,dof]
            print(line)
    # ephemerides: primaries only, secondaries only, joint; all best events
    Pg,ePg=gaia[tic]
    for lab,sel in [('P',lambda b:b['kind']=='P'),('S',lambda b:b['kind']=='S')]:
        L=[b for b in best if sel(b)]
        E=np.array([b['epoch'] for b in L],float);T=np.array([b['tc'] for b in L]);s=np.array([b['etc'] for b in L])
        bb,eb,res,chi2,dof=linfit(E,T,s)
        print(f'  EPHEM {lab}-only (all pipelines, n={len(L)}, epochs {int(E.min())}..{int(E.max())}): T0={bb[0]:.5f}±{eb[0]:.5f} P={bb[1]:.7f}±{eb[1]:.7f} chi2/dof={chi2:.1f}/{dof}; vs Gaia {(bb[1]-Pg)/np.hypot(eb[1],ePg):+.2f} sigma')
        print('     O-C min: '+' '.join(f"E{int(e_)}:{1440*r_:+.1f}±{1440*s_:.1f}[{b['pipe'][0:3]}]" for e_,r_,s_,b in zip(E,res,s,L)))
        out[f'{tic}_ephem_{lab}']=dict(T0=bb[0],eT0=eb[0],P=bb[1],eP=eb[1],chi2=chi2,dof=dof,n=len(L))
    E=np.array([b['epoch'] for b in best],float);T=np.array([b['tc'] for b in best]);s=np.array([b['etc'] for b in best]);isS=np.array([b['kind']=='S' for b in best],float)
    # choose reference epoch near the weighted centre of the primaries to decorrelate T0 and P
    Ep=E[isS==0]; Eref=float(np.round(np.sum(Ep/s[isS==0]**2)/np.sum(1/s[isS==0]**2)))
    bb,eb,res,chi2,dof=linfit(E-Eref,T,s,extra=isS)
    phS=bb[2]/bb[1]; ephS=np.hypot(eb[2]/bb[1],bb[2]*eb[1]/bb[1]**2)
    T0e=bb[0]-Eref*bb[1]
    print(f'  EPHEM joint (n={len(best)}): Tref(E={Eref:.0f})={bb[0]:.5f}±{eb[0]:.5f}  P={bb[1]:.7f}±{eb[1]:.7f}  T0(E=0)={T0e:.5f}  S offset {bb[2]:.5f}±{eb[2]:.5f} d  phase_S={phS:.5f}±{ephS:.5f} chi2/dof={chi2:.1f}/{dof}; P vs Gaia {(bb[1]-Pg)/np.hypot(eb[1],ePg):+.2f} sigma')
    out[f'{tic}_ephem_joint']=dict(Eref=Eref,Tref=bb[0],eTref=eb[0],P=bb[1],eP=eb[1],T0_E0=T0e,dtS=bb[2],edtS=eb[2],phaseS=phS,ephaseS=ephS,chi2=chi2,dof=dof,n=len(best))
    # TESScut-only period (independent pipeline)
    L=[(k,ev[k]['meas']['TESScut-3x3']) for k in keys if ev[k]['kind']=='P' and 'TESScut-3x3' in ev[k]['meas']]
    E_=np.array([k[1] for k,_ in L],float);T_=np.array([v['tc'] for _,v in L]);s_=np.array([v['etc'] for _,v in L])
    bb,eb,res,chi2,dof=linfit(E_,T_,s_)
    print(f'  EPHEM primaries TESScut-3x3 only (n={len(L)}): P={bb[1]:.7f}±{eb[1]:.7f} chi2/dof={chi2:.1f}/{dof}; vs Gaia {(bb[1]-Pg)/np.hypot(eb[1],ePg):+.2f} sigma')
    out[f'{tic}_ephem_P_tesscut']=dict(P=bb[1],eP=eb[1],chi2=chi2,dof=dof,n=len(L))
    # odd/even (at P_ecl: odd vs even primaries == the two halves of a 2P orbit), per pipeline
    for p in ['TESS-SPOC','QLP','TESScut-3x3']:
        for kind in 'PS':
            L=[(k[1],ev[k]['meas'][p]) for k in keys if ev[k]['kind']==kind and p in ev[k]['meas']]
            if len(L)<2: continue
            o=[(v['dep'],v['edep']) for e_,v in L if e_%2]; ee=[(v['dep'],v['edep']) for e_,v in L if not e_%2]
            if not o or not ee: continue
            mo,eo,_,_=wmean(*zip(*o)); me,eE,_,_=wmean(*zip(*ee))
            print(f'  ODD/EVEN {p} {kind}: odd {1e3*mo:.2f}±{1e3*eo:.2f} (n={len(o)})  even {1e3*me:.2f}±{1e3*eE:.2f} (n={len(ee)})  diff {(mo-me)/np.hypot(eo,eE):+.2f} sigma')
            out[f'{tic}_oddeven_{p}_{kind}']=dict(odd=mo,eodd=eo,even=me,eeven=eE,nsig=(mo-me)/np.hypot(eo,eE))
    out[tic+'_events']=[dict(kind=ev[k]['kind'],epoch=ev[k]['epoch'],sector=ev[k]['sector'],tpred=ev[k]['tpred'],meas=ev[k]['meas'],lost=ev[k]['lost']) for k in keys]
json.dump(out,open('s12_compile.json','w'),indent=1,default=float)
