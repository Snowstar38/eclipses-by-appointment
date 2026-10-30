# s5b = s5_roche.py with the M2(i) bracket widened (s5 crashed at i=5 deg) and i=10,5 replaced by 25,15 deg. Output s5b_roche.txt.
# Physical check: Roche-model ellipsoidal light curve of the Gaia RV star (no eclipses, dark companion),
# vs inclination, with M2(i) from Gaia's mass function. Reports A1..A3 (ppt), min depths at conj A/B,
# and whether the companion would eclipse the primary at that inclination.
import numpy as np, sys
sys.path.insert(0,'[local path omitted]')
from common import targets
from scipy.optimize import brentq
G=6.674e-11; Msun=1.989e30; Rsun=6.957e8
def omega(x,y,z,q):
    r=np.sqrt(x*x+y*y+z*z); r2=np.sqrt((x-1)**2+y*y+z*z)
    return 1/r+q*(1/r2-x)+(1+q)/2*(x*x+y*y)
def grad(x,y,z,q):
    r=np.sqrt(x*x+y*y+z*z); r2=np.sqrt((x-1)**2+y*y+z*z)
    gx=-x/r**3+q*(-(x-1)/r2**3-1)+(1+q)*x; gy=-y/r**3-q*y/r2**3+(1+q)*y; gz=-z/r**3-q*z/r2**3
    return gx,gy,gz
def L1(q):
    f=lambda x: -1/x**2+q/(1-x)**2-q+(1+q)*x   # d omega/dx on axis, 0<x<1 (sign convention)
    return brentq(lambda x: 1/x**2-q/(1-x)**2-(1+q)*x+q,1e-3,1-1e-3)
def surface(q,Om,nt=60,nph=120):
    th=(np.arange(nt)+0.5)/nt*np.pi; ph=(np.arange(nph)+0.5)/nph*2*np.pi
    TH,PH=np.meshgrid(th,ph,indexing='ij'); l=np.sin(TH)*np.cos(PH); m=np.sin(TH)*np.sin(PH); n=np.cos(TH)
    xl1=L1(q); R=np.zeros_like(TH)
    for i in range(nt):
        for j in range(nph):
            fr=lambda r: omega(r*l[i,j],r*m[i,j],r*n[i,j],q)-Om
            hi=xl1*0.999 if l[i,j]>0 else xl1
            # find first crossing outward
            rr=np.linspace(1e-3,hi,200); v=fr(rr); k=np.where(v<0)[0]
            R[i,j]=brentq(fr,rr[k[0]-1],rr[k[0]]) if len(k) else hi
    x,y,z=R*l,R*m,R*n; gx,gy,gz=grad(x,y,z,q); g=np.sqrt(gx**2+gy**2+gz**2)
    nx_,ny_,nz_=-gx/g,-gy/g,-gz/g   # outward normal
    cosb=np.clip(nx_*l+ny_*m+nz_*n,0.05,1)
    dA=R**2*np.sin(TH)*(np.pi/nt)*(2*np.pi/nph)/cosb
    vol=np.sum(R**3/3*np.sin(TH))*(np.pi/nt)*(2*np.pi/nph)
    return dict(x=x,y=y,z=z,n=(nx_,ny_,nz_),g=g,dA=dA,req=(3*vol/(4*np.pi))**(1/3))
def lc(S,inc,Teff,beta,u,nphase=200,lam=0.8e-6):
    gp=np.max(S['g'])  # pole ~ max gravity
    T=Teff*(S['g']/np.mean(S['g']))**beta
    I=1/(np.exp(6.626e-34*3e8/(lam*1.381e-23*T))-1)
    ph=np.arange(nphase)/nphase; F=[]
    for p in ph:
        o=np.array([np.sin(inc)*np.cos(2*np.pi*p),np.sin(inc)*np.sin(2*np.pi*p),np.cos(inc)])
        mu=S['n'][0]*o[0]+S['n'][1]*o[1]+S['n'][2]*o[2]; v=mu>0
        F.append(np.sum((I*(1-u*(1-mu))*mu*S['dA'])[v]))
    F=np.array(F); F=F/np.mean(F)-1
    a=[2*np.mean(F*np.exp(-2j*np.pi*k*ph)) for k in (1,2,3,4)]
    return ph,F,[abs(x)*1e3 for x in a]
def m2_of_i(fm,M1,i):
    return brentq(lambda M2:(M2*np.sin(i))**3/(M1+M2)**2-fm,1e-4,1e4)
def run(tic,M1,R1,Teff,beta,u=0.5,obsA2=None,label=''):
    T=targets()[tic]; P=float(T['gaia_Per']); K=float(T['gaia_K1']); e=float(T['gaia_ecc'])
    fm=1.0361e-7*K**3*P*(1-e*e)**1.5
    print(f'--- TIC {tic} {label}: P={P:.4f} d K1={K:.1f} km/s e={e:.3f} f(m)={fm:.4f} Msun; M1={M1} R1={R1} Teff={Teff} beta={beta} u={u}; observed A2 {obsA2} ppt')
    print('  i(deg)  M2   q     a(Rsun) R1/a  RL/a(Egg) fill(R1/RL)  A1    A2    A3   (ppt, model, no eclipse)  min@A-min@B(ppt)  eclipse?(cos i<(Rpol+R2)/a)')
    for ideg in (90,75,60,50,40,30,25,20,15):
        i=np.radians(ideg); M2=m2_of_i(fm,M1,i); q=M2/M1
        a=(G*(M1+M2)*Msun*(P*86400)**2/(4*np.pi**2))**(1/3)/Rsun
        rL=0.49*(1/q)**(2/3)/(0.6*(1/q)**(2/3)+np.log(1+(1/q)**(1/3)))
        r=R1/a
        note=''
        try:
            if r>=rL*0.995: raise ValueError
            Om=brentq(lambda Om: surface(q,Om,20,40)['req']-r, omega(L1(q),0,0,q)*1.0005, 200)
        except ValueError:
            Om=omega(L1(q),0,0,q)*1.0005; note='FILLS(capped)'
        S=surface(q,Om); ph,F,A=lc(S,i,Teff,beta,u)
        dAB=(F[0]-F[len(F)//2])*1e3   # negative => deeper at A
        R2=M2**0.8 if M2<1.4 else M2**0.57
        rpol=np.max(S['z']); ecl=np.cos(i)<(rpol*a+R2)/a
        print(f'  {ideg:5d} {M2:5.2f} {q:5.2f} {a:7.2f} {r:5.3f} {rL:6.3f} {r/rL:6.2f} {note:15s} {A[0]:6.2f} {A[1]:6.2f} {A[2]:5.2f}  {dAB:7.2f}  {"YES" if ecl else "no"}')
if __name__=='__main__':
    run('372683900',1.61,2.91,7189,0.25,obsA2='14.8 QLP (20.2 if x(1+0.37)); TESScut-PSF 13.7')
    run('13106408',2.5,5.95,7192,0.25,obsA2='21.5 QLP; TESScut-PSF 21.1',label='(TIC mass missing; M1=2.5 assumed)')
    run('13106408',2.0,5.95,7192,0.25,obsA2='21.5',label='(M1=2.0)')
    run('13106408',3.0,5.95,7192,0.25,obsA2='21.5',label='(M1=3.0)')
    run('372683622',1.19,3.28,6196,0.08,obsA2='3.21 QLP (3.46 x(1+0.078)); TESScut-PSF 3.3')
    run('319185391',1.42,2.66,6696,0.08,obsA2='3.62 QLP (4.09 x(1+0.129)); TESScut-PSF 3.6')
    run('62328710',1.51,4.58,6913,0.25,obsA2='<0.16 (2 sigma) QLP; <0.37 x(1+1.3)',label='(TIC R1)')
    run('62328710',1.51,1.8,6913,0.25,obsA2='<0.16; <0.37',label='(hypothetical MS R1=1.8)')
