# s11: per-sector depths, identical method for every pipeline: QLP SAP (Q==0), own TESScut aperture photometry (s8, Q==0,
# own background), TASOC raw flux (s15, 195865529), GSFC-ELEANOR-LITE raw flux (s12/13, 468181994).
# Method: ephemeris and shape fixed (s7/s6), each event window |dt|<W normalised by a quadratic fitted to |dt|>0.6*T14,
# depth = least-squares amplitude of the exposure-supersampled trapezoid; error = max(formal, scatter of per-event depths/sqrt(n)).
import numpy as np, json, csv, glob
from astropy.io import fits
from lcio import load_qlp, trap
D='/tmp/claude-0/-home-user-eclipses-paper-review/55c92ff4-798a-544f-be03-9888c6804905/scratchpad/data/vet01'
EP=json.load(open('ephem.json'))
CFG={'195865529':dict(P=(0.0,0.2176,0.415),S=(0.5,0.2186,0.473),W=0.40),
     '468181994':dict(P=(0.0,0.1529,0.650),S=(EP['468181994_sec'][0],0.1529,0.650),W=0.40)}
def tmodel(t,tc,T14,f23,texp):
    k=np.linspace(-0.5,0.5,9)*texp
    return np.mean([trap(t+dk,tc,1.0,T14,f23) for dk in k],axis=0)
def depths(t,f,P,T0,phi,T14,f23,W,texp):
    n0=int(np.floor((t.min()-T0)/P))-1; n1=int(np.ceil((t.max()-T0)/P))+1
    ev=[]
    for n in range(n0,n1+1):
        tc=T0+(n+phi)*P; m=np.abs(t-tc)<W
        oot=m&(np.abs(t-tc)>0.6*T14); inn=m&(np.abs(t-tc)<0.35*T14)
        if (oot&(t<tc)).sum()<4 or (oot&(t>tc)).sum()<4 or inn.sum()<2: continue
        c=np.polyfit(t[oot]-tc,f[oot],2); y=f[m]/np.polyval(c,t[m]-tc)
        mm=tmodel(t[m],tc,T14,f23,texp); ev.append((tc,mm,1-y))
    if not ev: return None
    dd=[];ee=[]
    for tc,mm,r in ev:
        a=np.sum(mm*r)/np.sum(mm*mm); s=np.std(r-a*mm); dd.append(a); ee.append(s/np.sqrt(np.sum(mm*mm)))
    MM=np.concatenate([e[1] for e in ev]); RR=np.concatenate([e[2] for e in ev])
    A=np.sum(MM*RR)/np.sum(MM*MM); sA=np.std(RR-A*MM)/np.sqrt(np.sum(MM*MM))
    if len(dd)>2: sA=max(sA,np.std(dd,ddof=1)/np.sqrt(len(dd)))
    return A,sA,len(ev),np.array([e[0] for e in ev]),np.array(dd),np.array(ee)
def load_tc(tic,s):
    z=np.load(f'pix/ap_{tic}_s{s}.npz'); return z['t'],z['flux']/np.median(z['flux']),float(z['texp'])
res={}
for tic,c in CFG.items():
    P,T0=EP[tic]['P'],EP[tic]['T0']
    L=load_qlp(tic)
    srcs={}
    for s in L: srcs[('QLP-SAP',s)]=(L[s]['t'],L[s]['f'],L[s]['texp'])
    for f in glob.glob(f'pix/ap_{tic}_s*.npz'):
        s=int(f.split('_s')[1].split('.')[0]); srcs[('TESScut-ap',s)]=load_tc(tic,s)
    for f in glob.glob(f'{D}/{tic}/**/hlsp_tasoc*cbv-lc.fits',recursive=True)+glob.glob(f'{D}/{tic}/**/hlsp_gsfc-eleanor*.fits',recursive=True):
        h=fits.open(f); d=h[1].data; s=h[0].header['SECTOR']
        col='FLUX_RAW' if 'tasoc' in f else 'RAW_FLUX'; name='TASOC-raw' if 'tasoc' in f else 'ELEANOR-lite-raw'
        t=np.array(d['TIME'],float); y=np.array(d[col],float); q=np.array(d['QUALITY'])
        m=np.isfinite(t)&np.isfinite(y)&(q==0); srcs[(name,s)]=(t[m],y[m]/np.median(y[m]),float(np.median(np.diff(t[m]))))
        if name=='ELEANOR-lite-raw':
            y2=np.array(d['CORR_FLUX'],float); m2=np.isfinite(t)&np.isfinite(y2)&(q==0); srcs[('ELEANOR-lite-corr',s)]=(t[m2],y2[m2]/np.median(y2[m2]),float(np.median(np.diff(t[m2]))))
    print('='*25,tic,f'P={P:.7f} T0={T0:.5f}')
    for typ in ('P','S'):
        phi,T14,f23=c[typ]
        print(f'  {typ} (phase {phi:.4f}, T14 {T14*24:.2f} h fixed):')
        for (name,s) in sorted(srcs,key=lambda k:(k[1],k[0])):
            t,f,texp=srcs[(name,s)]
            r=depths(t,f,P,T0,phi,T14,f23,c['W'],texp)
            if r is None: print(f'    s{s:<3d} {name:18s} no covered events'); continue
            print(f'    s{s:<3d} {name:18s} depth {r[0]*1e3:7.2f} +- {r[1]*1e3:5.2f} ppt  (n_events {r[2]}, cadence {texp*1440:.1f} min)')
            res[f'{tic}_{typ}_{name}_{s}']=[r[0],r[1],r[2]]
            if name=='TESScut-ap' and ((tic=='468181994' and s==66) ):
                for tc,dd,ee in zip(r[3],r[4],r[5]): print(f'        event {tc:.4f}: depth {dd*1e3:6.2f} +- {ee*1e3:.2f} ppt')
json.dump(res,open('s11_depths.json','w'),indent=0)
