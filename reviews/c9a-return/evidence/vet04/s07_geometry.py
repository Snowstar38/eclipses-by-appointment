# Monte Carlo: Gaia SB1 orbit -> conjunction A (nu=90-omega, companion in front of the RV primary) and B (nu=270-omega)
# compare (i) secondary-minus-primary phase (depends on e, omega only) and (ii) absolute phase of the TESS primary.
from common import *; import json
rng=np.random.default_rng(42); N=20000
def E_of_nu(nu,e): return 2*np.arctan2(np.sqrt(1-e)*np.sin(nu/2),np.sqrt(1+e)*np.cos(nu/2))
def M_of_nu(nu,e):
    E=E_of_nu(nu,e); return E-e*np.sin(E)
def circ_stats(ph):  # phase in [0,1): mean and std around circular mean
    a=2*np.pi*ph; m=np.arctan2(np.mean(np.sin(a)),np.mean(np.cos(a)))/(2*np.pi)%1
    d=(ph-m+0.5)%1-0.5; return m,np.std(d),np.percentile(d,[2.5,97.5])
rhos={'283532878':0.92670065,'407877153':0.9852944}  # last corr_vec element, assumed corr(arg_periastron,t_periastron) (see REPORT caveat)
for tic,g in GAIA.items():
    eph=json.load(open(f's05_ephem_{tic}.json'))
    for case in ('independent','rho_wTp'):
        e=g['e']+g['ee']*rng.standard_normal(N)
        z1=rng.standard_normal(N); z2=rng.standard_normal(N)
        rho=rhos[tic] if case=='rho_wTp' else 0.0
        w=g['w']+g['ew']*z1; Tp=g['Tp']+g['eTp']*(rho*z1+np.sqrt(1-rho**2)*z2)
        Pg=g['P']+g['eP']*rng.standard_normal(N)
        ok=(e>=0)&(e<0.95); e=np.abs(e)
        wr=np.radians(w)
        MA=M_of_nu(np.radians(90-w),e)%(2*np.pi); MB=M_of_nu(np.radians(270-w),e)%(2*np.pi)
        dph=((MB-MA)/(2*np.pi))%1     # phase of B after A
        tA=Tp+MA/(2*np.pi)*Pg; tB=Tp+MB/(2*np.pi)*Pg
        # absolute phase of conjunctions relative to TESS primary T0, propagated (a) with TESS P (precise), (b) with Gaia P draws
        P=eph['P']; T0=eph['T0P']
        phA_t=((tA-T0)/P)%1; phB_t=((tB-T0)/P)%1
        ncyc=np.round((T0-g['Tp'])/g['P'])
        phA_g=((tA+ncyc*Pg-T0)/P)%1; phB_g=((tB+ncyc*Pg-T0)/P)%1
        print('=====',tic,case,'rho=%.3f'%rho)
        m,s,ci=circ_stats(dph); print('  Gaia-predicted phase of B after A: %.4f ± %.4f (95%%: %+.4f %+.4f)'%(m,s,*ci))
        print('     -> phase of A after B: %.4f'%((1-m)%1))
        ms=eph['ph2']; print('  measured secondary phase (after primary): %.5f ± %.5f'%(ms,eph['eph2']))
        for lab,obs in (('primary=A (secondary=B)',ms),('primary=B (secondary=A)',(1-ms)%1)):
            dd=((obs-dph+0.5)%1-0.5) if lab.startswith('primary=A') else (((1-ms)%1-dph+0.5)%1-0.5)
            # fraction of MC draws within ±0.01 phase? and sigma
            mm,ss,_=circ_stats(dph)
            diff=((ms if lab.startswith('primary=A') else (1-ms)%1)-mm+0.5)%1-0.5
            print('  hypothesis %s: obs B-A sep=%.4f, pred %.4f±%.4f, diff=%+.4f = %.2f sigma'%(lab,(ms if lab.startswith('primary=A') else (1-ms)%1),mm,ss,diff,diff/ss))
        for lab,phA,phB in (('TESS-P propagation',phA_t,phB_t),('Gaia-P propagation',phA_g,phB_g)):
            mA,sA,_=circ_stats(phA); mB,sB,_=circ_stats(phB)
            dA=((0-mA+0.5)%1-0.5); dB=((0-mB+0.5)%1-0.5)
            print('  %s: conj A at TESS-primary phase %.4f±%.4f (primary off by %+.4f = %.2f sig, %+.2f d); conj B at %.4f±%.4f (primary off by %+.4f = %.2f sig, %+.2f d)'%(
                lab,mA,sA,dA,dA/sA,dA*P,mB,sB,dB,dB/sB,dB*P))
            # where does the measured secondary sit?
            dAs=((ms-mA+0.5)%1-0.5); dBs=((ms-mB+0.5)%1-0.5)
            print('      secondary (phase %.4f) vs A: %+.4f (%.2f sig); vs B: %+.4f (%.2f sig)'%(ms,dAs,dAs/sA,dBs,dBs/sB))
        # e cos w and e sin w
        print('  Gaia e cos w = %.4f ± %.4f ; e sin w = %.4f ± %.4f'%(np.mean(e*np.cos(wr)),np.std(e*np.cos(wr)),np.mean(e*np.sin(wr)),np.std(e*np.sin(wr))))
