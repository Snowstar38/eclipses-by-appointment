# Physical sanity check: mass function -> minimum companion mass; MS radius/Teff for it; separation; central T14;
# uniform-disc grazing geometry that reproduces the observed primary T14; predicted primary and secondary depths;
# observed depth ratio vs Planck surface-brightness ratio at 800 nm. Also TESS-SPOC CROWDSAP/FLFRCSAP keywords.
import numpy as np, json, glob, csv
from scipy.optimize import brentq
from astropy.io import fits
G=6.674e-11; Msun=1.989e30; Rsun=6.957e8; day=86400.
T=list(csv.DictReader(open('../targets.csv'))); T={r['tic']:r for r in T}
SH=json.load(open('s6_shape.json')); C=json.load(open('s12_compile.json'))
# rough main-sequence relations for M/K dwarfs (Pecaut & Mamajek 2013 table, interpolated): mass -> (R, Teff)
MS=np.array([[0.10,0.12,2800],[0.16,0.19,3050],[0.23,0.27,3200],[0.37,0.38,3400],[0.44,0.44,3550],[0.50,0.49,3650],[0.57,0.56,3800],[0.64,0.62,4000],[0.70,0.68,4300],[0.78,0.76,4700]])
def ms(m): return np.interp(m,MS[:,0],MS[:,1]),np.interp(m,MS[:,0],MS[:,2])
def overlap(d,r1,r2):
    if d>=r1+r2: return 0.0
    if d<=abs(r1-r2): return np.pi*min(r1,r2)**2
    a=r1*r1*np.arccos((d*d+r1*r1-r2*r2)/(2*d*r1)); b=r2*r2*np.arccos((d*d+r2*r2-r1*r1)/(2*d*r2))
    c=0.5*np.sqrt((-d+r1+r2)*(d+r1-r2)*(d-r1+r2)*(d+r1+r2)); return a+b-c
def planck(T,lam=800e-9):
    return 1/(np.exp(6.626e-34*2.998e8/(lam*1.381e-23*T))-1)
out={}
for tic in ['15855794','92881948']:
    r=T[tic]; P=float(r['gaia_Per']); K=float(r['gaia_K1']); e=float(r['gaia_ecc'])
    M1=float(r['tic_mass']); R1=float(r['tic_rad']); T1=float(r['tic_Teff'])
    fm=P*day*(K*1e3)**3*(1-e*e)**1.5/(2*np.pi*G)/Msun
    m2=brentq(lambda m:m**3/(M1+m)**2-fm,1e-3,5)
    R2,T2=ms(m2)
    a=(G*(M1+m2)*Msun*(P*day/(2*np.pi))**2)**(1/3)/Rsun
    T14c=P/np.pi*np.arcsin((R1+R2)/a)*24
    T14o=SH[f'{tic}_P']['T14_d']*24
    # impact parameter (in units of R1, on sky) that gives the observed T14 (circular, i from b)
    def t14(b):
        i=np.arccos(b*R1/a); x=np.sqrt(max((R1+R2)**2-(b*R1)**2,0))/a/np.sin(i)
        return P/np.pi*np.arcsin(min(x,1))*24
    b=brentq(lambda b:t14(b)-T14o,0,(R1+R2)/R1-1e-6); inc=np.degrees(np.arccos(b*R1/a))
    S1,S2=planck(T1),planck(T2); L1=S1*np.pi*R1**2; L2=S2*np.pi*R2**2
    A=overlap(b*R1,R1,R2)
    dP=A*S1/(L1+L2); dS=A*S2/(L1+L2)
    J=S2/S1
    dPo=C[f'{tic}_P_TESScut-3x3_corr'][0]; dSo=C[f'{tic}_S_TESScut-3x3_corr'][0]
    rat=dSo/dPo
    T2fromJ=brentq(lambda t:planck(t)/S1-rat,1500,T1*1.5)
    out[tic]=dict(fm=fm,m2min=m2,R2=R2,T2=T2,a_Rsun=a,T14_central_h=T14c,T14_obs_h=T14o,b=b,inc=inc,depthP_pred=dP,depthS_pred=dS,
                  depthP_obs=dPo,depthS_obs=dSo,J_planck=J,ratio_obs=rat,T2_from_ratio=T2fromJ,maxdepth_full=(R2/R1)**2*S1*np.pi*R1**2/(L1+L2))
    print(f'TIC {tic}: P={P:.4f} d K1={K:.2f} km/s e={e:.3f} -> f(m)={fm:.4f} Msun; with M1(TIC)={M1} Msun, R1={R1} Rsun, Teff1={T1:.0f} K: m2 sin^3i-equivalent minimum m2={m2:.3f} Msun')
    print(f'   MS companion: R2~{R2:.2f} Rsun, Teff2~{T2:.0f} K; a={a:.2f} Rsun; central T14={T14c:.2f} h vs observed {T14o:.2f} h -> uniform-disc b={b:.3f} (R1 units), i={inc:.2f} deg (grazing: b*R1 vs R1-R2 = {b*R1:.2f} vs {R1-R2:.2f})')
    print(f'   predicted (uniform discs, Planck 800 nm, no limb darkening): primary {1e3*dP:.1f} ppt, secondary {1e3*dS:.1f} ppt; observed (TESScut 3x3 / target fraction) {1e3*dPo:.1f} / {1e3*dSo:.2f} ppt')
    print(f'   depth ratio S/P observed {rat:.3f} vs Planck J(Teff2~{T2:.0f}) {J:.3f}; ratio implies Teff2 ~ {T2fromJ:.0f} K')
for f in sorted(glob.glob('/tmp/claude-0/-home-user-eclipses-paper-review/55c92ff4-798a-544f-be03-9888c6804905/scratchpad/data/vet05/*/mastDownload/HLSP/hlsp_tess-spoc*/*.fits')):
    h=fits.open(f)
    print('TESS-SPOC',f.split('/')[-1][:60],'CROWDSAP=',h[1].header.get('CROWDSAP'),'FLFRCSAP=',h[1].header.get('FLFRCSAP'),'NPIX_AP=',int((h[2].data & 2 >0).sum()))
for f in sorted(glob.glob('/tmp/claude-0/-home-user-eclipses-paper-review/55c92ff4-798a-544f-be03-9888c6804905/scratchpad/data/vet05/*/mastDownload/HLSP/hlsp_qlp*/*.fits')):
    h=fits.open(f); hh=h[1].header
    print('QLP',f.split('/')[-1][:50],'CROWDSAP=',hh.get('CROWDSAP'),'apertures:',{k:hh[k] for k in hh if k.startswith(('APRAD','BESTAP','NUM_AP','AP'))})
json.dump(out,open('s14_physics.json','w'),indent=1)
