import numpy as np, json
G=6.674e-11; Ms=1.989e30; Rs=6.957e8; AU=1.496e11
P=25.083485; K=22.39; e=0.1096; sf=json.load(open('secfit.json')); E=json.load(open('ecl.json'))
f=1.0361e-7*(1-e*e)**1.5*K**3*P; print(f'mass function {f:.4f} Msun (K1 22.39+-1.69 -> +-{3*1.69/22.39*f:.4f})')
for M1 in (1.5,1.65,1.8):
    m=np.linspace(0.05,2,20000); m2=m[np.argmin(np.abs(m**3/(M1+m)**2-f))]
    a=((G*(M1+m2)*Ms*(P*86400)**2)/(4*np.pi**2))**(1/3); print(f' M1={M1}: m2(i=90)={m2:.3f} Msun, a={a/Rs:.1f} Rsun = {a/AU:.3f} AU')
M1,m2,R1=1.65,0.52,2.13
a=((G*(M1+m2)*Ms*(P*86400)**2)/(4*np.pi**2))**(1/3)/Rs
# phase separation -> e cos w (exact Kepler, i=90): solve over e,w grid
def conj(e,w,nu0):
    nu=nu0-w; Ee=2*np.arctan2(np.sqrt(1-e)*np.sin(nu/2),np.sqrt(1+e)*np.cos(nu/2)); return ((Ee-e*np.sin(Ee))/(2*np.pi))%1
dph=sf['phase']; dpe=sf['phase_err']
T1=np.mean([x['T14_h'] for x in E[2:]]); T1e=0.1; T2=sf['T14']*24; T2e=sf['T14_err']*24
# duration ratio T_B/T_A ~ (1 + e sin w)/(1 - e sin w) for Gaia primary w? sign: at A (nu=90-w) r=a(1-e^2)/(1+e cos(90-w))=a(1-e^2)/(1+e sin w)
# duration ∝ r / v_perp ∝ r^2 roughly... ratio T_B/T_A = r_B/r_A = (1+e sin w)/(1-e sin w)
ratio=T2/T1; rerr=ratio*np.hypot(T2e/T2,T1e/T1); esw=(ratio-1)/(ratio+1); eswe=rerr/(ratio+1)**2*2
print(f'durations: A {T1:.2f} h, B {T2:.2f}+-{T2e:.2f} h -> ratio {ratio:.3f}+-{rerr:.3f} -> e sin w = {esw:+.3f}+-{eswe:.3f}')
ee,ww=np.meshgrid(np.linspace(0,0.6,601),np.radians(np.linspace(0,360,721)))
sep=(conj(ee,ww,1.5*np.pi)-conj(ee,ww,0.5*np.pi))%1
best=np.abs(sep-dph)<3*dpe; ecw=(ee*np.cos(ww))[best]; print(f'phase sep {dph:.4f}+-{dpe:.4f} -> e cos w range (3sig) {ecw.min():.4f}..{ecw.max():.4f} (approx (pi/4)(dphi-0.5)={(np.pi/4)*(dph-0.5):.4f})')
# combine
ecw0=np.median(ecw); e_=np.hypot(ecw0,esw); w_=np.degrees(np.arctan2(esw,ecw0))%360
print(f'=> e cos w {ecw0:.4f}, e sin w {esw:+.3f}+-{eswe:.3f}, e {e_:.3f}, w {w_:.0f} deg  | Gaia e 0.110+-0.068, w 299+-55, ecosw 0.038+-0.081, esinw -0.061+-0.073')
print(f'   ecosw tension {(ecw0-0.038)/0.081:+.2f} sig; esinw tension {(esw+0.061)/np.hypot(0.073,eswe):+.2f} sig')
# predicted central durations at A, B
for lab,s in (('A',+1),('B',-1)):
    r=a*(1-e_**2)/(1+s*e_*np.sin(np.radians(w_)))  # primary-companion separation at conjunction
    v=2*np.pi*a/(P)*np.sqrt(1-e_**2)/(1-e_**2)*(1+s*e_*np.sin(np.radians(w_)))  # Rsun/day transverse
    for R2 in (0.5,):
        print(f' {lab}: sep {r:.1f} Rsun, central T14 (R1 {R1}+R2 {R2}) = {(2*(R1+R2)/v)*24:.1f} h')
# impact parameter from observed T14 ~7.75 h
v=2*np.pi*a/P*(1+e_*np.sin(np.radians(w_)))/np.sqrt(1-e_**2)
L=7.75/24*v/2; print(f' observed chord half-length {L:.2f} Rsun vs R1+R2={R1+0.5:.2f} -> b*(R1+R2)~{np.sqrt(max((R1+0.5)**2-L**2,0)):.2f} Rsun, i~{np.degrees(np.arccos(np.sqrt(max((R1+0.5)**2-L**2,0))/(a*(1-e_**2)/(1+e_*np.sin(np.radians(w_)))))):.2f} deg')
# surface brightness / temperature of companion from depth ratio (equal-area occulted approx)
d1=np.mean([x['depth'] for x in E[2:]]); d2=sf['depth']; sb=d2/d1
lam=0.8e-6; c=6.626e-34*2.998e8/(lam*1.381e-23)
for T1t in (7034,7308):
    B1=1/(np.exp(c/T1t)-1); T2t=c/np.log(1+1/(sb*B1)); print(f' depth ratio {sb:.3f}+-{sb*sf["depth_err"]/d2:.3f}; T1 {T1t} -> T2 ~{T2t:.0f} K (band 800 nm, equal-area)')
print(f' secondary light fraction in TESS ~ (R2/R1)^2 * sb = {(0.5/2.13)**2*sb:.4f}')
