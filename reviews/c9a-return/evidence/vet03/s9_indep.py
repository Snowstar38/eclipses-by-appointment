# Independence check: per-sector depths from QLP SAP, TESS-SPOC SAP (s3/s5 json) and own TESScut 3x3 aperture photometry
# (tesscut_ap3x3_*.txt written by s7/s7b). Same trapezoid + quadratic-baseline fit as s3, run at every predicted event.
import numpy as np, json, glob, re, sys
from scipy.optimize import least_squares
from lcio import trap
E={'70665829':dict(T0=2576.73361,P=3.4657658,phi2=0.46049,T14=0.118,win=0.30,pix=['s7_pixels_70665829.out']),
   '331293467':dict(T0=4066.68168,P=5.2568187,phi2=0.5002,T14=0.17,win=0.55,pix=['s7b_pixels_331293467.out'])}
def fit(tt,ff,cad,tc,T14g,win):
    m=np.abs(tt-tc)<win; t=tt[m]; f=ff[m]
    if m.sum()<15 or np.sum(np.abs(t-tc)<T14g/2)<0.6*T14g/cad or np.sum(t<tc-T14g/2)<5 or np.sum(t>tc+T14g/2)<5: return None
    def model(p): t0,D,T14,r,a0,a1,a2=p; x=t-tc; return (a0+a1*x+a2*x*x)*trap(t,t0,D,T14,r,cad)
    lb=[tc-0.05,0,0.02,0,0.5,-1,-10]; ub=[tc+0.05,1,win*1.6,0.95,1.5,1,10]; best=None
    for r0 in (0.05,0.4,0.8):
        p0=np.clip([tc,max(1-f.min()/np.median(f),1e-3),T14g,r0,np.median(f),0,0],np.array(lb)+1e-6,np.array(ub)-1e-6)
        s=least_squares(lambda p:model(p)-f,p0,bounds=(lb,ub))
        if best is None or s.cost<best.cost: best=s
    rms=np.std(best.fun)
    try: e=np.sqrt(np.diag(np.linalg.inv(best.jac.T@best.jac)))*rms
    except Exception: e=np.full(7,np.nan)
    return best.x[0],best.x[1],e[1],best.x[2]*24
out={}
for tic,c in E.items():
    print('='*10,tic)
    share={}; psf={}
    for fn in c['pix']:
        cur=None
        for l in open(fn):
            m=re.match(r's(\d+) (primary|secondary): .*A=(\d+)',l)
            if m: cur=(int(m.group(1)),m.group(2)); A=float(m.group(3))
            m=re.search(r'deficit amplitude ([\d.]+) e/s',l)
            if m and cur: psf[cur]=float(m.group(1))/A
            m=re.search(r'diff-image depth in aperture ([\d.]+) ppt; target model share of aperture = ([\d.]+)',l)
            if m and cur: share[cur]=(float(m.group(1)),float(m.group(2)))
    res={}
    for fn in sorted(glob.glob(f'tesscut_ap3x3_{tic}_s*.txt')):
        sec=int(re.search(r'_s(\d+)\.txt',fn).group(1)); t,f=np.loadtxt(fn,unpack=True); cad=np.median(np.diff(t))
        for kind,ph in [('primary',0),('secondary',c['phi2'])]:
            n0=int(np.floor((t.min()-c['T0'])/c['P']))-1; n1=int(np.ceil((t.max()-c['T0'])/c['P']))+1; rows=[]
            for n in range(n0,n1+1):
                r=fit(t,f,cad,c['T0']+(n+ph)*c['P'],c['T14'],c['win'])
                if r: rows.append(r)
            if rows:
                D=np.array([r[1] for r in rows]); res[(sec,kind)]=dict(n=len(rows),D=np.median(D),sD=np.std(D)/np.sqrt(len(D)),T14=np.median([r[3] for r in rows]))
    # pipeline per-sector medians
    ev=json.load(open(f's3_events_{tic}.json')); thr={'70665829':0.15,'331293467':0.03}[tic]
    pipe={}
    for e in ev:
        if e['D']<0.02 or e['eD']>0.01: continue
        k='primary' if e['D']>thr else 'secondary'; pipe.setdefault((e['pipe'],e['sector'],k),[]).append(e['D'])
    if tic=='331293467':
        for r in json.load(open('s5_secondary_331293467.json')):
            if r['kind']=='sec': pipe.setdefault(('QLP',r['sector'],'secondary'),[]).append(r['D'])
    secs=sorted(set([k[1] for k in pipe]+[k[0] for k in res]))
    print('sector | QLP SAP prim / sec (ppt) | SPOC SAP prim / sec | TESScut 3x3 raw prim / sec [n] | TESScut 3x3 / target share (scene model) | PSF-amplitude depth (deficit amp / target flux) | sec/prim ratio QLP, SPOC, TESScut')
    for s in secs:
        def g(p,k): v=pipe.get((p,s,k)); return (np.median(v)*1e3,len(v)) if v else (np.nan,0)
        q1,q2,s1,s2=g('QLP','primary'),g('QLP','secondary'),g('SPOC','primary'),g('SPOC','secondary')
        t1=res.get((s,'primary')); t2=res.get((s,'secondary'))
        tc1=t1['D']*1e3 if t1 else np.nan; tc2=t2['D']*1e3 if t2 else np.nan
        sh=share.get((s,'primary'),(np.nan,np.nan))[1]
        p1=psf.get((s,'primary'),np.nan)*1e3; p2=psf.get((s,'secondary'),np.nan)*1e3
        rat=lambda a,b: b/a if a==a and b==b else np.nan
        print(f"s{s} | {q1[0]:.1f} / {q2[0]:.1f} (n {q1[1]}/{q2[1]}) | {s1[0]:.1f} / {s2[0]:.1f} (n {s1[1]}/{s2[1]}) | {tc1:.1f}+-{(t1['sD']*1e3 if t1 else np.nan):.1f} / {tc2:.1f}+-{(t2['sD']*1e3 if t2 else np.nan):.1f} [{t1['n'] if t1 else 0}/{t2['n'] if t2 else 0}] | {tc1/sh:.1f} / {tc2/sh:.1f} (share {sh:.3f}) | {p1:.1f} / {p2:.1f} | {rat(q1[0],q2[0]):.3f}, {rat(s1[0],s2[0]):.3f}, {rat(tc1,tc2):.3f}")
    for k,v in sorted(res.items()): print(f'  TESScut s{k[0]} {k[1]}: n={v["n"]} median depth {v["D"]*1e3:.1f} ppt (+-{v["sD"]*1e3:.1f}) T14 {v["T14"]:.2f} h')
    out[tic]={f'{k[0]}_{k[1]}':v for k,v in res.items()}
json.dump(out,open('s9_indep.json','w'),indent=1,default=float)
