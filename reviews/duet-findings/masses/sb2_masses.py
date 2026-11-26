"""Dynamical masses of the eclipsing Gaia DR3 SB2 systems, and a luminosity test of Gaia's semi-amplitudes.
Inputs (all in the repository): Fable 5.1's NSS export for the A systems, sb2-eclipsing.csv (collect_sb2.py) for
the R systems, CHECKCARD.csv and gaia-errors/a-epoch-test.csv for eclipse periods, tic-records.csv (collect_tic.py)
for TIC v8.2 luminosities. Writes masses/sb2-masses.csv. Run from the repository root."""
import numpy as np, pandas as pd
D='reviews/duet-findings/'
num=lambda s: pd.to_numeric(s,errors='coerce')
f=pd.read_csv(D+'gaia-errors/fable51-nss-appointments.csv',dtype=str)
f=f[f.nss_solution_type.str.startswith('SB2')]
A=pd.DataFrame(dict(review_id=f.review_id,source_id=f.source_id,type=f.nss_solution_type,P=num(f.period),e=num(f.eccentricity).fillna(0),
    omega=num(f.arg_periastron),K1=num(f.semi_amplitude_primary),K1_err=num(f.semi_amplitude_primary_error),
    K2=num(f.semi_amplitude_secondary),K2_err=num(f.semi_amplitude_secondary_error)))
r=pd.read_csv(D+'masses/sb2-eclipsing.csv',dtype=str); r=r[r.review_id.str.startswith('R')]
R=pd.DataFrame(dict(review_id=r.review_id,source_id=r.source_id,type=r.type,P=num(r.P),e=num(r.e).fillna(0),omega=num(r.omega),
    K1=num(r.K1),K1_err=num(r.K1_err),K2=num(r.K2),K2_err=num(r.K2_err),P_ecl=num(r.eclipse_P)))
cc=pd.read_csv('CHECKCARD.csv',dtype=str).set_index('label')
ae=pd.read_csv(D+'gaia-errors/a-epoch-test.csv',dtype=str).set_index('review_id')
A['P_ecl']=[num(pd.Series([ae.P_ecl.get(i, cc.P_days.get(i))])).iloc[0] for i in A.review_id]
m=pd.concat([A,R],ignore_index=True)
m['P_ratio']=m.P/m.P_ecl
m['same_period']=(abs(m.P_ratio-1)<0.01)
m['accepted']=m.review_id.isin(set(pd.read_csv('accepted-systems.csv').review_id))
acc=pd.read_csv('accepted-systems.csv',dtype=str)[['review_id','tic','tier']]
tic=pd.read_csv(D+'masses/tic-records.csv',dtype=str)
m=m.merge(acc,on='review_id',how='left').merge(tic[['ID','Teff','lum','rad','mass','lumclass']].rename(columns={'mass':'M_tic'}),left_on='tic',right_on='ID',how='left')
go=pd.read_csv('reviews/2026-11-24-gaia-epoch-review/gaia-orbits.csv',dtype=str)[['source_id','phot_g_mean_mag','bp_rp','parallax']].drop_duplicates('source_id')
m=m.merge(go,on='source_id',how='left')
for c in ['Teff','lum','rad','M_tic','phot_g_mean_mag','bp_rp','parallax']: m[c]=num(m[c])
m['M_G']=m.phot_g_mean_mag+5*np.log10(m.parallax/100)
K1,K2,P,e=m.K1,m.K2,m.P,m.e
fac=1.0361e-7*(1-e**2)**1.5*(K1+K2)**2*P
m['M1sin3i']=fac*K2; m['M2sin3i']=fac*K1
# errors: M1 ~ (K1+K2)^2 K2 ; independent K errors
s=K1+K2
m['M1_err']=m.M1sin3i*np.sqrt((2*m.K1_err/s)**2+(m.K2_err*(2/s+1/K2))**2)
m['M2_err']=m.M2sin3i*np.sqrt((2*m.K2_err/s)**2+(m.K1_err*(2/s+1/K1))**2)
m['q']=K1/K2
m['asini_Rsun']=1.9758e-2*np.sqrt(1-e**2)*(K1+K2)*P
# eclipse => cos i < (R1+R2)/r ; r >= a(1-e). R1+R2 ~ sqrt(2) R_TIC (two similar stars), floor 2 Rsun
Rsum=np.where(m.rad.notna(),np.sqrt(2)*m.rad,2.0)
m['sin3i_min']=np.clip(1-(Rsum/(m.asini_Rsun*(1-e)))**2,0,1)**1.5
def L_ms(M):  # Eker et al. 2018 main-sequence mass-luminosity relation (detached eclipsing binaries)
    lm=np.log10(M)
    return 10**np.select([M<=0.45,M<=0.72,M<=1.05,M<=2.4],[2.028*lm-0.976,4.572*lm-0.102,5.743*lm-0.007,4.329*lm+0.010],3.967*lm+0.093)
m['L_pred']=L_ms(m.M1sin3i)+L_ms(m.M2sin3i)
m['logL_obs_over_pred']=np.log10(m.lum/m.L_pred)
m['Mdyn_max_over_Mtic']=m[['M1sin3i','M2sin3i']].max(axis=1)/m.M_tic
cols=['review_id','accepted','tier','type','P','P_ecl','P_ratio','same_period','e','K1','K1_err','K2','K2_err','q','M1sin3i','M1_err','M2sin3i','M2_err','asini_Rsun','sin3i_min','Teff','rad','lum','lumclass','M_tic','Mdyn_max_over_Mtic','L_pred','logL_obs_over_pred','bp_rp','M_G']
m=m[cols].sort_values('review_id',key=lambda s:s.str[0]+s.str[1:].str.zfill(5))
m.round(4).to_csv(D+'masses/sb2-masses.csv',index=False)
g=m[m.same_period&m.accepted]
print('Gaia SB2 orbits on A and R labels:',len(m),'; on accepted systems:',int(m.accepted.sum()),'; accepted and at the eclipse period (within 1%):',len(g))
print('not accepted (not counted):',', '.join(m.review_id[~m.accepted]))
print('not at the eclipse period:',', '.join(f'{a} ({b:.3f})' for a,b in zip(m[~m.same_period].review_id,m[~m.same_period].P_ratio)))
print('M1 sin^3 i: median %.2f, range %.2f-%.2f Msun; M2: median %.2f, range %.2f-%.2f'%(g.M1sin3i.median(),g.M1sin3i.min(),g.M1sin3i.max(),g.M2sin3i.median(),g.M2sin3i.min(),g.M2sin3i.max()))
print('median fractional mass error %.1f%% (M1), %.1f%% (M2)'%(100*(g.M1_err/g.M1sin3i).median(),100*(g.M2_err/g.M2sin3i).median()))
print('sin^3 i lower bound from the eclipse: median %.3f, min %.3f'%(g.sin3i_min.median(),g.sin3i_min.min()))
d=g[(g.lumclass=='DWARF')&~g.review_id.isin(['R729','R1819'])]
d=d.dropna(subset=['logL_obs_over_pred'])
print('excluded as contradicted Gaia orbits: R729, R1819')
print('dwarfs with a TIC luminosity:',len(d))
print('log L_obs/L_pred(Eker MLR): median %+.3f, mean %+.3f, sd %.3f, 16-84%% %+.2f..%+.2f'%(d.logL_obs_over_pred.median(),d.logL_obs_over_pred.mean(),d.logL_obs_over_pred.std(),*d.logL_obs_over_pred.quantile([.16,.84])))
print('fraction with L_obs < L_pred: %d/%d'%((d.logL_obs_over_pred<0).sum(),len(d)))
x=d.dropna(subset=['Mdyn_max_over_Mtic'])
print('dynamical/TIC mass, %d dwarfs: median %.3f, robust sd %.3f (implied K scale %.3f)'%(len(x),x.Mdyn_max_over_Mtic.median(),1.4826*np.median(abs(x.Mdyn_max_over_Mtic-x.Mdyn_max_over_Mtic.median())),x.Mdyn_max_over_Mtic.median()**(1/3)))
q=g.q.where(g.q<=1,1/g.q); print('mass ratios (<=1): median %.3f; below 0.8: %s'%(q.median(),', '.join(f'{a} {b:.3f}' for a,b in zip(g.review_id[q<0.8],q[q<0.8]))))
pd.set_option('display.width',250)
print(g[['review_id','tier','P','e','q','M1sin3i','M1_err','M2sin3i','M2_err','sin3i_min','Teff','rad','lum','lumclass','M_tic','Mdyn_max_over_Mtic','logL_obs_over_pred','bp_rp','M_G']].round(3).to_string(index=False))
