"""B-eclipse scan over B-A phase separation: for each sep, B centres at T_A(s55)+(sep-1)P and T_A(s82)+(sep-1)P;
fit a box of duration D (6.5 h, also 5 h) with a local linear baseline (+-0.7 d) to raw SAP q==0 (QLP and TESS-SPOC separately),
requiring >=60% in-box coverage; combine sectors by inverse variance. Errors scaled by red-noise beta from 6.5-h binned rms.
-> bnull.txt, bnull.png. python bnull.py"""
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from astropy.io import fits
D='[local path omitted]'; V=D+'vet466336052/'
P=32.13919; TA={55:2818.4830,82:3557.6843}
F={('QLP',55):D+'466336052_s055.fits',('QLP',82):D+'466336052_s082.fits',
   ('TSPOC',55):V+'hlsp_tess-spoc_tess_phot_0000000466336052-s0055_tess_v1_lc.fits',('TSPOC',82):V+'hlsp_tess-spoc_tess_phot_0000000466336052-s0082_tess_v1_lc.fits'}
L={}
for k,fn in F.items():
    d=fits.open(fn)[1].data; t=np.array(d['TIME'],float); f=np.array(d['SAP_FLUX'],float); q=np.array(d['QUALITY'],int)
    ok=np.isfinite(t)&np.isfinite(f)&(q==0); t,f=t[ok],f[ok]; f/=np.median(f)
    A=np.abs(t-TA[k[1]])<0.3; L[k]=(t[~A],f[~A])
seps=np.arange(0.40,0.80,0.0015)
fig,axs=plt.subplots(2,1,figsize=(12,8))
for j,Dh in enumerate((6.5,5.0)):
    Dd=Dh/24; print(f'--- box {Dh} h')
    for pipe in ('QLP','TSPOC'):
        res=[]
        for s in seps:
            num=den=0; per=[]
            for sec in (55,82):
                t,f=L[(pipe,sec)]; tb=TA[sec]+(s-1)*P
                w=np.abs(t-tb)<0.7; inb=np.abs(t-tb)<Dd/2
                cad=np.median(np.diff(t)); 
                if inb.sum()<0.6*Dd/cad or (w&~inb).sum()<0.3*1.4/cad: per.append(None); continue
                X=np.vstack([np.ones(w.sum()),t[w]-tb,-inb[w].astype(float)]).T
                c,_,_,_=np.linalg.lstsq(X,f[w],rcond=None); r=f[w]-X@c; sig=np.std(r)
                cov=np.linalg.inv(X.T@X)*sig**2; e=np.sqrt(cov[2,2])
                nb=max(1,int(Dd/cad)); beta=1.0
                rr=r[:len(r)//nb*nb].reshape(-1,nb).mean(1) if len(r)//nb>=3 else None
                if rr is not None: beta=max(1,np.std(rr)/(sig/np.sqrt(nb)))
                e*=beta; per.append((c[2],e)); num+=c[2]/e**2; den+=1/e**2
            if den: res.append((s,num/den,1/np.sqrt(den),per))
            else: res.append((s,np.nan,np.nan,per))
        a=np.array([(r[0],r[1],r[2]) for r in res])
        axs[j].errorbar(a[:,0],a[:,1]*100,a[:,2]*100,fmt='.',label=pipe,alpha=0.6)
        cov_=np.isfinite(a[:,1]); ex=cov_&(a[:,1]+3*a[:,2]<0.0020)
        print(f'{pipe}: sep covered (either sector) fraction of 0.40-0.80: {cov_.mean():.2f}; covered ranges:')
        # contiguous ranges
        def rng(m):
            out=[];st=None
            for s,mm in zip(a[:,0],m):
                if mm and st is None: st=s
                if not mm and st is not None: out.append((round(st,4),round(prev,4))); st=None
                prev=s
            if st is not None: out.append((round(st,4),round(prev,4)))
            return out
        print('   covered:',rng(cov_)); print('   B depth >=0.20% excluded at 3 sigma for sep in:',rng(ex))
        big=a[cov_&(a[:,1]>3*a[:,2])&(a[:,1]>0.001)]
        print('   >3 sigma positive dips (sep, depth%, err%):',[(round(x[0],4),round(x[1]*100,3),round(x[2]*100,3)) for x in big][:40])
    axs[j].axvspan(0.6012-0.0335,0.6012+0.0335,color='gold',alpha=0.3); axs[j].axhline(0.25,color='r',ls=':'); axs[j].set_title(f'box {Dh} h'); axs[j].legend(); axs[j].set_ylim(-0.5,0.8)
plt.savefig('bnull.png',dpi=60)
