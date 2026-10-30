# Event census: every predicted primary/secondary inside each light curve's span, with QUALITY==0 coverage,
# plus a look at the blind dips that are not at eclipse phases.
import numpy as np, glob
from astropy.io import fits
from lcio import load, D
E={'70665829':dict(T0=2576.73361,P=3.4657658,phi2=0.46049,T14=2.83/24),
   '331293467':dict(T0=4066.68168,P=5.2568187,phi2=0.5002,T14=4.07/24)}
for tic,c in E.items():
    print('='*10,tic)
    for lc in load(tic):
        t=lc['t']; lines=[]; nfull=0; npart=0; nlost=0
        for kind,ph in [('P',0),('S',c['phi2'])]:
            n0=int(np.floor((lc['tstart']-c['T0'])/c['P']))-1; n1=int(np.ceil((lc['tend']-c['T0'])/c['P']))+1
            for n in range(n0,n1+1):
                tc=c['T0']+(n+ph)*c['P']
                if tc<lc['tstart']-c['T14']/2 or tc>lc['tend']+c['T14']/2: continue
                cov=np.sum(np.abs(t-tc)<c['T14']/2)/(c['T14']/lc['cad'])
                if cov>0.9: nfull+=1
                elif cov>0.1: npart+=1; lines.append(f'{kind}@{tc:.3f}:partial({cov:.2f})')
                else: nlost+=1; lines.append(f'{kind}@{tc:.3f}:LOST')
        print(f"{lc['pipe']:4s} s{lc['sector']:<4d} {lc['tstart']:.2f}-{lc['tend']:.2f}: full {nfull}, partial {npart}, lost {nlost}  "+' '.join(lines))
# non-eclipse blind dips flagged by s3
def show(tic,pipe,sec,t1,t2):
    c=E[tic]
    for fn in glob.glob(f'{D}/{tic}/mastDownload/HLSP/*/*.fits'):
        h=fits.open(fn)
        if h[0].header['SECTOR']!=sec or (('qlp' in fn)!=(pipe=='QLP')): continue
        d=h[1].data; t=d['TIME']; f=d['SAP_FLUX']; q=d['QUALITY']; b=d['SAP_BKG']
        m=(t>t1)&(t<t2)&np.isfinite(f)
        med=np.nanmedian(f[(q==0)&np.isfinite(f)])
        ph=((t[m]-c['T0'])/c['P'])%1
        print(f'-- {tic} {pipe} s{sec} {t1}-{t2}: phase range {ph.min():.3f}-{ph.max():.3f}; points {m.sum()}, QUALITY==0 {np.sum(q[m]==0)}')
        tb=np.arange(t1,t2,0.05)
        for a in tb:
            k=m&(t>=a)&(t<a+0.05)&(q==0)
            k_all=m&(t>=a)&(t<a+0.05)
            if k_all.sum(): print(f'   {a:.2f}: flux(q0) {np.nanmedian(f[k])/med if k.sum() else np.nan:.4f} n_q0={k.sum()}/{k_all.sum()} bkg {np.nanmedian(b[k_all]):.1f} flags {sorted(set(int(x) for x in q[k_all]))}')
show('70665829','SPOC',1751,4058.9,4059.8)
show('70665829','QLP',48,2621.1,2621.7)
