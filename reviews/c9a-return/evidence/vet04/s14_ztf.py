# ZTF (IRSA) light curves of TIC 283532878 and of every neighbour that the dilution arithmetic cannot exclude for the
# secondary (needs < 100% intrinsic depth in some aperture: 26.3" G16.38, 28.1" G17.47, 28.3" G14.93, 29.5" G15.74, 37.0" G14.50).
# Fold on the TESS ephemeris (s05) and measure the mean flux deficit inside the inner part of primary and secondary windows.
import requests, io, json, csv, numpy as np, os
D='/tmp/claude-0/-home-user-eclipses-paper-review/55c92ff4-798a-544f-be03-9888c6804905/scratchpad/data/vet04/283532878/ztf'
os.makedirs(D,exist_ok=True)
eph=json.load(open('s05_ephem_283532878.json')); sh=json.load(open('s08_shape_oddeven.json'))['283532878']['shape']
P=eph['P']; T0={'P':eph['T0P'],'S':eph['T0S']}
nb=[r for r in csv.DictReader(open('../neighbours_90as.csv')) if r['tic']=='283532878']
pick=[r for r in nb if float(r['sep_arcsec'])<1 or (float(r['sep_arcsec'])<40 and float(r['Gmag'])<17.6)]
res={}
for r in pick:
    ra,dec=float(r['ra']),float(r['dec']); lab='%.1f"/G%.2f'%(float(r['sep_arcsec']),float(r['Gmag']))
    fn=f'{D}/ztf_{r["source_id"]}.csv'
    if not os.path.exists(fn):
        u=f'https://irsa.ipac.caltech.edu/cgi-bin/ZTF/nph_light_curves?POS=CIRCLE%20{ra}%20{dec}%200.0004&BANDNAME=g,r&FORMAT=csv'
        txt=requests.get(u,timeout=180).text; open(fn,'w').write(txt)
    T=np.genfromtxt(fn,delimiter=',',names=True,dtype=None,encoding=None)
    if T.size==0: print(lab,'no ZTF rows'); continue
    T=np.atleast_1d(T)
    print('=====',lab,'source',r['source_id'],'rows',T.size,'oids',len(set(T['oid'])))
    out={}
    for oid in sorted(set(T['oid'])):
        m=(T['oid']==oid)&(T['catflags']==0)
        if m.sum()<50: continue
        band=T['filtercode'][m][0]
        # hjd is heliocentric JD; BTJD approx = hjd-2457000 (HJD vs BJD differ by < 4 s here)
        t=T['hjd'][m]-2457000; mag=T['mag'][m]; f=10**(-0.4*(mag-np.median(mag)))
        sel={}
        for k in 'PS':
            ph=((t-T0[k])/P+0.5)%1-0.5; dt=ph*P
            hin=0.5*sh[k]['r23']*sh[k]['T14']+0.25*(1-sh[k]['r23'])*sh[k]['T14']
            sel[k]=np.abs(dt)<hin
        oot=np.ones_like(t,bool)
        for k in 'PS':
            ph=((t-T0[k])/P+0.5)%1-0.5; oot&=np.abs(ph*P)>sh[k]['T14']/2+0.05
        base=np.median(f[oot]); sd=1.4826*np.median(np.abs(f[oot]-base))
        line=f'  oid {oid} {band} N={m.sum()} oot rms {1e3*sd:.1f} ppt'
        for k in 'PS':
            n=sel[k].sum()
            if n==0: line+=f' | {k}: no points'; continue
            dep=base-np.mean(f[sel[k]]); e=sd/np.sqrt(n)
            line+=f' | {k}: N_in={n} deficit {1e3*dep:.1f}±{1e3*e:.1f} ppt'
            out[f'{oid}_{band}_{k}']=dict(n=int(n),dep=float(dep),e=float(e))
        print(line)
    res[lab]=out
json.dump(res,open('s14_ztf.json','w'),indent=1)
