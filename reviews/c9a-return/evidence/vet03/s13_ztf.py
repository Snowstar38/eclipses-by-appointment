# ZTF light curves (IRSA API) at the targets (2.0" radius = 0.00056 deg); fold at the TESS ephemeris.
import requests, io, numpy as np, pandas as pd
from astropy.time import Time
D='/tmp/claude-0/-home-user-eclipses-paper-review/55c92ff4-798a-544f-be03-9888c6804905/scratchpad/data/vet03/ztf'
S={'70665829':(155.384788090706,17.2035145893056,2791.61111,3.4657654,0.46048),'331293467':(212.403511923353,-60.1143106920448,3467.40446,5.2568199,0.50013)}
for tic,(ra,dec,T0,P,ph2) in S.items():
    u=f'https://irsa.ipac.caltech.edu/cgi-bin/ZTF/nph_light_curves?POS=CIRCLE%20{ra}%20{dec}%200.00056&BANDNAME=g,r&FORMAT=csv'
    try: r=requests.get(u,timeout=180); txt=r.text
    except Exception as e: print(tic,'request failed',e); continue
    open(f'{D}/ztf_{tic}.csv','w').write(txt)
    df=pd.read_csv(io.StringIO(txt)) if txt.strip() else pd.DataFrame()
    print(f'== TIC {tic} (Dec {dec:+.1f}): HTTP {r.status_code}, {len(df)} rows')
    if len(df)==0: continue
    df=df[(df.catflags==0)]
    print('   oids:',dict(df.groupby(['oid','filtercode']).size()))
    # hjd is heliocentric; barycentric-heliocentric difference < 4 s, ignored
    t=df.hjd.values-2457000; ph=((t-T0)/P+0.5)%1-0.5; df=df.assign(ph=ph)
    for (oid,fc),g in df.groupby(['oid','filtercode']):
        if len(g)<30: continue
        oot=g[(np.abs(g.ph)>0.03)&(np.abs(g.ph-(ph2-1 if ph2>0.5 else ph2))>0.03)&(np.abs(g.ph-ph2)>0.03)]
        m0=np.median(oot.mag)
        for lab,c in [('primary',0.0),('secondary',ph2 if ph2<0.5 else ph2-1)]:
            ii=g[np.abs(((g.ph-c)+0.5)%1-0.5)<0.006]   # within ~ +-T23/2.. core of eclipse
            if len(ii)>=2:
                dm=np.median(ii.mag)-m0; print(f'   {oid} {fc}: N={len(g)} OOT median {m0:.3f} mag (scatter {np.std(oot.mag):.3f}); {lab}: {len(ii)} points within +-0.006 phase, median +{dm:.3f} mag = {(1-10**(-0.4*dm))*1e3:.0f} ppt, at HJD-2457000 {", ".join(f"{x:.3f}" for x in ii.hjd.values[:6]-2457000)}')
            else: print(f'   {oid} {fc}: N={len(g)}; {lab}: {len(ii)} points in core')
        print(f'   {oid} {fc}: time span {g.hjd.min()-2457000:.1f}-{g.hjd.max()-2457000:.1f}')
