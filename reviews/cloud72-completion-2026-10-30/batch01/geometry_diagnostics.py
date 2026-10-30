"""Near-reference phase check and one targeted nonlinearity sensitivity test."""
import csv, json, math
from pathlib import Path
import numpy as np
B = Path(__file__).parent
G = json.loads((B/'gaia-geometry.json').read_text())
R = json.loads((B/'raw-evidence/raw-events.json').read_text())
N = {r['source_id']: r for r in csv.DictReader((B.parent/'shared-catalogues/gaia-nss_two_body_orbit.csv').open())}
def conj(v, kind):
    P,e,w,tp=v
    nu=(math.pi/2 if kind=='A' else 3*math.pi/2)-w
    E=2*math.atan2(math.sqrt(1-e)*math.sin(nu/2),math.sqrt(1+e)*math.cos(nu/2))
    return tp+((E-e*math.sin(E))%(2*math.pi))/(2*math.pi)*P
for tic,g in G.items():
    if g.get('status')=='unresolved': continue
    n=N[g['gaia_source_id']]
    v=np.array([float(n['period']),float(n['eccentricity']),math.radians(float(n['arg_periastron'])),float(n['t_periastron'])+389])
    e=np.array([float(n['period_error']),float(n['eccentricity_error']),math.radians(float(n['arg_periastron_error'])),float(n['t_periastron_error'])])
    C=np.eye(6); vals=[float(x) for x in n['corr_vec'].strip('{}[]()').split(',')]; z=0
    for ii in range(1,6):
        for jj in range(ii): C[ii,jj]=C[jj,ii]=vals[z]; z+=1
    sub=C[np.ix_([0,3,4,5],[0,3,4,5])]
    ep=R[tic]['representative_ephemeris']; tc=ep['epoch_btjd']+round((389-ep['epoch_btjd'])/ep['period_d'])*ep['period_d']
    k=g['closest_kind']; nominal=conj(v,k); cyc=round((tc-nominal)/v[0]); deriv=[]
    for j in range(4):
        vv=v.copy(); step=e[j]*.001 or 1e-7; vv[j]+=step
        deriv.append((conj(vv,k)+cyc*vv[0]-nominal-cyc*v[0])/step*e[j])
    error=float(np.sqrt(max(0,np.asarray(deriv)@sub@np.asarray(deriv))))
    delta=float((tc-nominal-cyc*v[0]+v[0]/2)%v[0]-v[0]/2)
    g['near_gaia_reference']=dict(projected_eclipse_btjd=tc,offset_d=delta,covariance_linear_error_d=error,note='Photometric period projected back; measured period uncertainty unestimated; linear Gaia covariance only.')
    if tic=='23112764':
        x=np.random.default_rng(20261030).multivariate_normal(v,sub*e[:,None]*e[None,:],10000)
        x=x[(x[:,0]>0)&(x[:,1]>=0)&(x[:,1]<1)]
        P,ec,w,tp=x.T; nu=math.pi/2-w
        E=2*np.arctan2(np.sqrt(1-ec)*np.sin(nu/2),np.sqrt(1+ec)*np.cos(nu/2))
        pred=tp+((E-ec*np.sin(E))%(2*math.pi))*P/(2*math.pi)
        offsets=tc-(pred+np.round((tc-pred)/P)*P)
        q=np.quantile(offsets,[.00135,.025,.15865,.5,.84135,.975,.99865])
        out=dict(tic=tic,seed=20261030,n_draws=10000,n_physical=len(x),offset_quantiles_d=dict(zip(['0.135%','2.5%','15.865%','50%','84.135%','97.5%','99.865%'],q.tolist())),fraction_same_sign=float(np.mean(offsets>0)),method='Targeted nonlinearity diagnostic using full Gaia P,e,omega,Tp covariance; Gaussian errors, rejects e outside[0,1); photometric ephemeris fixed. Not a recalibration of Gaia uncertainty.')
        (B/'23112764-geometry-sensitivity.json').write_text(json.dumps(out,indent=2))
(B/'gaia-geometry.json').write_text(json.dumps(G,indent=2))
