# s9: combine s8 per-sector pixel results; dilution arithmetic with CATALOGUE fluxes (TIC Tmag, Gaia G->T fallback) for every
# Gaia G<18 neighbour within 90" (neighbours_90as.csv), PSF sigma fitted per sector in s8, aperture r=1.5 px around the target.
import json, csv, glob, numpy as np
from astropy.io import fits
from astropy.wcs import WCS
from scipy.special import erf
D='/tmp/claude-0/-home-user-eclipses-paper-review/55c92ff4-798a-544f-be03-9888c6804905/scratchpad/data/vet01'
NB=list(csv.DictReader(open('../neighbours_90as.csv')))
def gpsf(X,Y,x0,y0,s):
    a=lambda u,c:0.5*(erf((u+0.5-c)/(np.sqrt(2)*s))-erf((u-0.5-c)/(np.sqrt(2)*s)))
    return a(X,x0)*a(Y,y0)
depth={'195865529':(0.1827,0.0477),'468181994':(0.0224,0.00126)}  # QLP SAP primary / secondary depths (s7 odd-even raw means, s7b secondary)
for tic in ['195865529','468181994']:
    J=json.load(open(f'pix/pix_{tic}.json'))
    TIC={r['GAIA']:r for r in csv.DictReader(open(f'tic_neighbours_{tic}.csv')) if r['disposition']!='DUPLICATE'}
    nb=[r for r in NB if r['tic']==tic]
    print('='*25,tic)
    oE=np.array([J[s]['offE'] for s in J]); oN=np.array([J[s]['offN'] for s in J])
    print(f'diff-image centroid offsets over {len(J)} sectors: E {np.round(oE,2).tolist()}  N {np.round(oN,2).tolist()}')
    mE,mN=oE.mean(),oN.mean(); sE,sN=oE.std(ddof=1)/np.sqrt(len(oE)),oN.std(ddof=1)/np.sqrt(len(oN))
    print(f'  mean offset dE={mE:+.2f}+-{sE:.2f}" dN={mN:+.2f}+-{sN:.2f}" (error = sector scatter/sqrt(n)); |mean|={np.hypot(mE,mN):.2f}"; per-sector |off| median {np.median(np.hypot(oE,oN)):.2f}" max {np.hypot(oE,oN).max():.2f}"')
    print(f'  events in difference images: {sum(J[s]["nev"] for s in J)} primaries; sectors/cameras: {list(J)}')
    # per-neighbour arithmetic
    rows=[]
    for s in J:
        f=glob.glob(f'{D}/{tic}/tesscut/tess-s{int(s):04d}-*.fits')[0]
        w=WCS(fits.getheader(f,2)); img=np.load(f'pix/img_{tic}_s{s}.npz'); ap=img['ap']; xT,yT=float(img['xT']),float(img['yT'])
        x0,y0=w.world_to_pixel_values(float(nb[0]['ra']),float(nb[0]['dec'])); dx,dy=xT-x0,yT-y0
        Y,X=np.mgrid[0:ap.shape[0],0:ap.shape[1]]; sig=J[s]['sigma']
        fl={}
        # all TIC stars T<19 within 120" contribute to the aperture total
        for g,r in TIC.items():
            x,y=w.world_to_pixel_values(float(r['ra']),float(r['dec']))
            fl[g]=10**(-0.4*float(r['Tmag']))*gpsf(X,Y,x+dx,y+dy,sig)[ap].sum()
        tot=sum(fl.values())
        for r in nb:
            g=r['source_id']
            if g in fl: fr=fl[g]/tot; T=float(TIC[g]['Tmag'])
            else:
                x,y=w.world_to_pixel_values(float(r['ra']),float(r['dec'])); T=float(r['Gmag'])-0.5
                fr=10**(-0.4*T)*gpsf(X,Y,x+dx,y+dy,sig)[ap].sum()/tot
            rows.append((s,g,float(r['sep_arcsec']),float(r['Gmag']),T,fr))
    print(f'  {"Gaia DR3":>20s} {"sep":>6s} {"G":>6s} {"T":>6s}  frac_in_ap(max over sectors)  needed depth for primary / secondary (min over sectors)')
    for r in nb:
        g=r['source_id']; fr=np.array([x[5] for x in rows if x[1]==g]); T=[x[4] for x in rows if x[1]==g][0]
        need1=depth[tic][0]/fr.max(); need2=depth[tic][1]/fr.max()
        tag='TARGET' if float(r['sep_arcsec'])<1 else ('EXCLUDED (needs >100%)' if need1>1 else 'not excluded by arithmetic alone')
        print(f'  {g:>20s} {float(r["sep_arcsec"]):6.1f} {float(r["Gmag"]):6.2f} {T:6.2f}  {fr.max()*100:7.3f}% (min {fr.min()*100:.3f}%)   {min(need1,99)*100:7.1f}% / {min(need2,99)*100:6.1f}%   {tag}')
