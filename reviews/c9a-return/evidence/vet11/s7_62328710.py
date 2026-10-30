# TIC 62328710: (1) TESS QLP-SAP frequency analysis (prewhitening, relation to Gaia orbital frequency, per-sector
# amplitudes, Gaia-P ellipsoidal upper limit); (2) ZTF DR light curves (IRSA) of the target and the neighbours bright
# enough to supply the ~6.39 c/d signal; Lomb-Scargle amplitude at the TESS frequencies.
import sys, os, io, json, numpy as np, requests, csv
sys.path.insert(0,'[local path omitted]')
from common import *
from astropy.timeseries import LombScargle
VD='[local path omitted]'; tic='62328710'; T=targets()[tic]; P0=float(T['gaia_Per'])
out=open(f'{VD}/s7_{tic}.txt','w')
def Pr(*a):
    s=' '.join(str(x) for x in a); print(s,flush=True); out.write(s+'\n')
t,f,seg,sec=load_qlp(tic,'SAP_FLUX')
A=poly_cols(t,seg,3); m=np.ones(len(t),bool)
for _ in range(4):
    c,*_=np.linalg.lstsq(A[m],f[m],rcond=None); r=f-A@c; s=1.4826*np.median(np.abs(r[m])); m=np.abs(r)<5*s
tt,rr=t[m],r[m]; T0=np.round(np.median(tt))
freqs=[]; fr=np.arange(0.05,30,0.00005)
Pr(f'TESS QLP SAP, {len(tt)} 10-min bins, sectors {sorted(set(sec.tolist()))}; f_orb(Gaia)={1/P0:.6f} c/d')
res=rr.copy()
for k in range(6):
    pw=LombScargle(tt,res).power(fr); i=np.argmax(pw); f0=fr[i]
    # refine by least squares on fine grid
    fg=np.linspace(f0-0.0002,f0+0.0002,401); best=None
    for ff in fg:
        X=np.vstack([np.cos(2*np.pi*ff*(tt-T0)),np.sin(2*np.pi*ff*(tt-T0)),np.ones_like(tt)]).T; cc,*_=np.linalg.lstsq(X,res,rcond=None); ch=np.sum((res-X@cc)**2)
        if best is None or ch<best[0]: best=(ch,ff,cc)
    ch,ff,cc=best; amp=np.hypot(cc[0],cc[1]); sres=np.std(res-np.vstack([np.cos(2*np.pi*ff*(tt-T0)),np.sin(2*np.pi*ff*(tt-T0)),np.ones_like(tt)]).T@cc)
    ef=np.sqrt(6/len(tt))*sres/(np.pi*(tt.max()-tt.min())*amp)   # Montgomery & O'Donoghue
    freqs.append((ff,ef,amp*1e3))
    Pr(f'  f{k+1} = {ff:.6f} +- {ef:.6f} c/d (P={1/ff:.6f} d), semi-amp {amp*1e3:.3f} ppt; f/f_orb = {ff*P0:.4f} +- {ef*P0:.4f}; nearest integer {round(ff*P0)} -> ({ff*P0-round(ff*P0):+.4f}) = {(ff*P0-round(ff*P0))/(ef*P0):+.0f} sigma(f)')
    X=np.vstack([np.cos(2*np.pi*ff*(tt-T0)),np.sin(2*np.pi*ff*(tt-T0)),np.ones_like(tt)]).T; res=res-X@cc
# combination check
f1=freqs[0][0]; f2=[x[0] for x in freqs[1:] if x[0]>1][0]   # f2 = next prewhitened frequency above 1 c/d (lower ones are slow trends)
Pr(f'  f1-f2={f1-f2:.5f}, f1+f2={f1+f2:.5f}, 2f1={2*f1:.5f}; f2/f1={f2/f1:.5f}')
# per-sector amplitude of f1 and f2 (fixed frequencies)
Pr('per-sector semi-amplitudes (ppt) at f1, f2; QLP cadence:')
for s_ in sorted(set(sec[m].tolist())):
    q=sec[m]==s_; x=tt[q]; y=rr[q]
    X=np.vstack([np.cos(2*np.pi*f1*(x-T0)),np.sin(2*np.pi*f1*(x-T0)),np.cos(2*np.pi*f2*(x-T0)),np.sin(2*np.pi*f2*(x-T0)),np.ones_like(x)]).T
    cc,*_=np.linalg.lstsq(X,y,rcond=None); e=np.std(y-X@cc)*np.sqrt(2/len(x))
    Pr(f'  s{s_}: A(f1)={np.hypot(cc[0],cc[1])*1e3:.3f} A(f2)={np.hypot(cc[2],cc[3])*1e3:.3f} +- {e*1e3:.3f}; phase(f1)={np.degrees(np.arctan2(cc[1],cc[0])):.0f} deg')
# Gaia-period ellipsoidal limit after removing f1..f6
X=np.vstack([np.cos(2*np.pi*k*(tt-T0)/P0) for k in (1,2)]+[np.sin(2*np.pi*k*(tt-T0)/P0) for k in (1,2)]+[np.ones_like(tt)]).T
cc,*_=np.linalg.lstsq(X,res,rcond=None); e=np.std(res-X@cc)*np.sqrt(2/len(tt))
Pr(f'Gaia-P harmonics after prewhitening 6 frequencies: A1={np.hypot(cc[0],cc[2])*1e3:.3f}, A2={np.hypot(cc[1],cc[3])*1e3:.3f} +- {e*1e3:.3f} ppt (2-sigma upper limit on A2 ~ {np.hypot(cc[1],cc[3])*1e3+2*e*1e3:.3f} ppt)')
# ---- ZTF
D=f'/tmp/claude-0/-home-user-eclipses-paper-review/55c92ff4-798a-544f-be03-9888c6804905/scratchpad/data/vet11/{tic}/ztf'; os.makedirs(D,exist_ok=True)
src=[('target',float(T['tic_ra']),float(T['tic_dec']),float(T['gaia_Gmag']),0.0)]
for n in csv.DictReader(open('[local path omitted]')):
    if n['tic']==tic and float(n['sep_arcsec'])>0.5 and float(n['Gmag'])<15.6 and float(n['sep_arcsec'])<60: src.append((n['source_id'],float(n['ra']),float(n['dec']),float(n['Gmag']),float(n['sep_arcsec'])))
Pr('ZTF (IRSA, r=5"; catflags==0; per-field/filter median-subtracted): source, G, sep | band n | LS semi-amp (mmag) at f1, f2 | top LS peak 1-30 c/d (freq, amp) | FAP-ish: amp at f1 / median amp over 1-30 c/d')
for nm,ra,dec,G,sep in src:
    fn=f'{D}/{nm}.csv'
    if not os.path.exists(fn):
        u=f'https://irsa.ipac.caltech.edu/cgi-bin/ZTF/nph_light_curves?POS=CIRCLE%20{ra}%20{dec}%200.0014&BANDNAME=g,r&FORMAT=csv'
        try: txt=requests.get(u,timeout=300).text; open(fn,'w').write(txt)
        except Exception as ex: Pr(f'  {nm}: ZTF query failed {ex}'); continue
    import pandas as pd
    try: d=pd.read_csv(fn)
    except Exception: Pr(f'  {nm}: unreadable'); continue
    if len(d)==0: Pr(f'  {nm} G={G:.2f} sep={sep:.1f}: no ZTF rows'); continue
    # keep only the object nearest the position per field/filter
    d=d[(d.catflags==0)]
    for band in ('zg','zr'):
        x=d[d.filtercode==band]
        if len(x)<50: Pr(f'  {nm} G={G:.2f} sep={sep:.1f} | {band} n={len(x)} (too few)'); continue
        # one oid per field: pick the oid with most points within each field and subtract its median
        yy=[]; ttz=[]; ee=[]
        for (fid,oid),g in x.groupby(['field','oid']):
            if len(g)<20: continue
            yy.append(g.mag.values-np.median(g.mag.values)); ttz.append(g.hjd.values); ee.append(g.magerr.values)
        if not yy: continue
        yy=np.concatenate(yy); ttz=np.concatenate(ttz); ee=np.concatenate(ee)
        k=np.abs(yy-np.median(yy))<5*1.4826*np.median(np.abs(yy-np.median(yy))); yy,ttz,ee=yy[k],ttz[k],ee[k]
        frz=np.arange(1,30,0.0002); pw=LombScargle(ttz,yy).power(frz)
        def amp_at(ff):
            X=np.vstack([np.cos(2*np.pi*ff*ttz),np.sin(2*np.pi*ff*ttz),np.ones_like(ttz)]).T; cc,*_=np.linalg.lstsq(X,yy,rcond=None); return np.hypot(cc[0],cc[1])*1e3
        a1=amp_at(f1); a2=amp_at(f2); ip=np.argmax(pw); ap=amp_at(frz[ip])
        # noise: amplitudes at 300 random frequencies
        rs=np.random.default_rng(5).uniform(1,30,300); an=np.array([amp_at(v) for v in rs])
        Pr(f'  {nm} G={G:.2f} sep={sep:.1f} | {band} n={len(yy)} rms {np.std(yy)*1e3:.1f} mmag | A(f1)={a1:.2f} A(f2)={a2:.2f} mmag | top {frz[ip]:.5f} c/d A={ap:.2f} | noise amp median {np.median(an):.2f}, 99th pct {np.percentile(an,99):.2f} mmag')
json.dump(dict(freqs=freqs),open(f'{VD}/s7_{tic}.json','w'),indent=1)
