"""Infer geometric conjunctions and propagate the Gaia NSS covariance."""
import argparse
import ast
import csv
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from astropy.time import Time

HERE=Path(__file__).resolve().parent
SOURCE="1906882711113246080"
p=argparse.ArgumentParser()
p.add_argument("--orbit",type=Path,default=HERE/"gaia-orbit.csv")
p.add_argument("--positions",type=Path,default=HERE/"gaia-source.csv")
p.add_argument("--eclipses",type=Path,default=HERE/"spoc-eclipses.csv")
p.add_argument("--draws",type=int,default=80000)
a=p.parse_args()


def read_row(path):
    with path.open(encoding="utf-8-sig",newline="") as f:
        return next(r for r in csv.DictReader(f) if r["source_id"]==SOURCE)


def pack(values):
    q=np.quantile(values,[.025,.16,.5,.84,.975])
    return {k:float(x) for k,x in zip(("q025","q16","median","q84","q975"),q)}


def btjd(ref,relative):
    return (Time(ref,relative,format="jd",scale="tcb").tdb-
            Time(2457000.,format="jd",scale="tdb")).to_value("day")


def geometry(values):
    """Return astrometric angular elements and signed separation minima."""
    A,B,F,G,C,H,e,P,tp=values.T
    x_norm=A*A+B*B
    y_norm=F*F+G*G
    cross=A*F+B*G
    a0=np.sqrt((x_norm+y_norm+np.hypot(x_norm-y_norm,2*cross))/2)
    cosi=(A*G-B*F)/a0**2
    i=np.arccos(np.clip(cosi,-1,1))
    omega_rv=np.arctan2(C,H)
    omega=np.arctan2(-2*cross,x_norm-y_norm)/2
    # Resolve the pi ambiguity of the sky-plane orientation with the RV branch.
    omega += np.pi*np.rint((omega_rv-omega)/np.pi)
    beta=np.sqrt(1-e**2)
    timing, radius, depth, anomalies = [], [], [], []
    for hemisphere in (1,-1):
        nu=hemisphere*np.pi/2-omega
        nu=(nu+np.pi)%(2*np.pi)-np.pi
        E=2*np.arctan2(np.sqrt(1-e)*np.sin(nu/2),np.sqrt(1+e)*np.cos(nu/2))
        for _ in range(8):
            c,s=np.cos(E),np.sin(E)
            x,y=c-e,beta*s
            X,Y=A*x+F*y,B*x+G*y
            XP,YP=-A*s+F*beta*c,-B*s+G*beta*c
            XPP,YPP=-A*c-F*beta*s,-B*c-G*beta*s
            curv=XP*XP+YP*YP+X*XPP+Y*YPP
            step=(X*XP+Y*YP)/curv
            E -= step
        if not (np.all(curv>0) and np.max(abs(step))<1e-9):
            raise RuntimeError("Separation minimum solve did not converge")
        xx=np.cos(E)-e
        yy=beta*np.sin(E)
        z=C*xx+H*yy
        if not np.all(hemisphere*z>0):
            raise RuntimeError("An orbital minimum left its expected line-of-sight hemisphere")
        radius.append(np.hypot(A*xx+F*yy,B*xx+G*yy)/a0)
        depth.append(z)
        timing.append(P*(E-e*np.sin(E))/(2*np.pi))
        anomalies.append(np.arctan2(beta*np.sin(E),np.cos(E)-e))
    return i,omega,omega_rv,a0,np.array(timing),np.array(radius),np.array(depth),np.array(anomalies)


row=read_row(a.orbit)
assert row["nss_solution_type"]=="AstroSpectroSB1" and int(row["bit_index"])==65535
order=("ra","dec","parallax","pmra","pmdec","a_thiele_innes","b_thiele_innes",
       "f_thiele_innes","g_thiele_innes","c_thiele_innes","h_thiele_innes",
       "center_of_mass_velocity","eccentricity","period","t_periastron")
v=ast.literal_eval(row["corr_vec"])
assert len(v)==len(order)*(len(order)-1)//2
corr=np.eye(len(order))
n=0
for j in range(1,len(order)):
    for k in range(j):
        corr[j,k]=corr[k,j]=v[n]
        n+=1
corr_min_eigen=float(np.linalg.eigvalsh(corr).min())
assert corr_min_eigen>0
idx=[5,6,7,8,9,10,12,13,14]
sigma=np.array([float(row[order[i]+"_error"]) for i in idx])
cov=corr[np.ix_(idx,idx)]*np.outer(sigma,sigma)
nom=np.array([float(row[order[i]]) for i in idx])
draw=np.random.default_rng(120239458).multivariate_normal(nom,cov,a.draws)
if not np.all((draw[:,6]>0)&(draw[:,6]<1)):
    raise RuntimeError("Draws include nonelliptical orbits")
ref=Time(float(read_row(a.positions)["ref_epoch"]),format="jyear",scale="tcb").jd
i,w,wr,a0,rel,r_proj,z,nu=geometry(draw)
i0,w0,wr0,a00,rel0,r_proj0,z0,nu0=geometry(nom[None,:])
with a.eclipses.open(encoding="utf-8-sig",newline="") as f:
    eclipses={(r["product"],r["eclipse"]):r for r in csv.DictReader(f)}
def measured(product,field):
    return np.array([float(eclipses[(product,k)][field]) for k in ("Primary","Secondary")])
obs=measured("PDCSAP_FLUX","center_btjd")
obs_sap=measured("SAP_FLUX","center_btjd")
pixel_window_centers=np.array([1741.14006,1747.89004])
# Each timestamp is paired with the same designated minimum in every draw.
integer=np.rint((obs-(ref-2457000+nom[-1]+rel0[:,0]))/nom[-2]).astype(int)
near=btjd(ref,draw[:,-1]+integer[:,None]*draw[:,-2]+rel)
near0=btjd(ref,nom[-1]+integer*nom[-2]+rel0[:,0])
earliest,latest=near
sep=latest-earliest
sep0=near0[1]-near0[0]
offset=obs[:,None]-near
res_time=(near.T-near0).T
covtime=np.cov(res_time)
common=(offset[0]+offset[1])/2
dsep=(obs[1]-obs[0])-sep
r1=np.hypot(draw[:,4],draw[:,5])/np.sin(i)
r1_rsun=r1*215.032
result={
    "source_id":SOURCE,"orbital_solution":row["solution_id"],"draws":a.draws,
    "corr_min_eigenvalue":corr_min_eigen,"full_correlation_order":order,
    "joint_epoch_correlation":float(np.corrcoef(near)[0,1]),
    "joint_epoch_covariance_d2":covtime.tolist(),
    "joint_gaia_timing_chi2_fixed_observed_centers":float((obs-near0)@np.linalg.solve(covtime,obs-near0)),
    "reference_epoch_tcb_jd":float(ref),"periastron_epoch_nominal_btjd":float(btjd(ref,nom[-1])),
    "period_days":float(nom[-2]),"eccentricity":float(nom[-3]),
    "inclination_deg_nominal":float(np.degrees(i0[0])),"inclination_deg":pack(np.degrees(i)),
    "omega_astrometric_deg_nominal":float(np.degrees(w0[0])%360),
    "omega_astrometric_deg":pack(np.degrees(w)%360),
    "omega_spectroscopic_deg_nominal":float(np.degrees(wr0[0])%360),
    "omega_spectroscopic_deg":pack(np.degrees(wr)%360),
    "omega_astrometric_minus_spectroscopic_deg":pack(np.degrees(w-wr)),
    "a_photocenter_mas":pack(a0),"a_primary_au":pack(r1),
    "predicted_separation_days_nominal":float(sep0),"predicted_separation_days":pack(sep),
    "observed_pdc_fit_btjd":obs.tolist(),"observed_sap_fit_btjd":obs_sap.tolist(),
    "observed_pdc_fit_depth_ppt":measured("PDCSAP_FLUX","fitted_depth_ppt").tolist(),
    "observed_sap_fit_depth_ppt":measured("SAP_FLUX","fitted_depth_ppt").tolist(),
    "observed_pdc_fwhm_days":measured("PDCSAP_FLUX","fwhm_days").tolist(),
    "adopted_pixel_window_centers_btjd":pixel_window_centers.tolist(),
    "observed_pdc_separation_days":float(np.diff(obs)[0]),
    "observed_sap_separation_days":float(np.diff(obs_sap)[0]),
    "observed_minus_predicted_separation_days":pack(dsep),
    "observed_mean_timing_offset_d":pack(common),
    "events":[],
}
for j in range(2):
    result["events"].append({
        "gaia_orbit_cycle":int(integer[j]),"z_sign_primary":1 if j==0 else -1,
        "nominal_btjd":float(near0[j]),"btjd":pack(near[j]),"obs_minus_predicted_d":pack(offset[j]),
        "true_anomaly_deg_nominal":float(np.degrees(nu0[j,0])),
        "nominal_offset_from_periastron_d":float(rel0[j,0]),
        "projected_separation_over_a":pack(r_proj[j]),
        "projected_relative_separation_lower_bound_rsun":pack(r_proj[j]*r1_rsun),
    })
with (HERE/"geometry.json").open("w",encoding="utf-8") as f:
    json.dump(result,f,indent=2)
    f.write("\n")
rows=[]
for cycle in range(20,93):
    tt=btjd(ref,draw[:,-1]+cycle*draw[:,-2]+rel)
    n0=btjd(ref,nom[-1]+cycle*nom[-2]+rel0[:,0])
    for j in range(2):
        if 1300<=n0[j]<=4220:
            rows.append(dict(cycle=cycle,z_sign_primary=1 if j==0 else -1,
                             nominal_btjd=n0[j],**pack(tt[j])))
with (HERE/"conjunctions.csv").open("w",encoding="utf-8",newline="") as f:
    wri=csv.DictWriter(f,rows[0].keys())
    wri.writeheader()
    wri.writerows(rows)

fig,ax=plt.subplots(1,2,figsize=(10.4,4.4),layout="constrained")
ax[0].hexbin(near[0],near[1],gridsize=70,cmap="Blues",mincnt=1)
ax[0].scatter(*obs,color="tab:red",s=35,label="S16 fitted dips",zorder=3)
ax[0].scatter(*near0,color="black",s=25,label="Nominal Gaia minima",zorder=3)
ax[0].set(xlabel="First conjunction (BTJD)",ylabel="Second conjunction (BTJD)")
ax[0].legend()
ax[1].hist(sep,bins=85,color="steelblue",alpha=.72)
ax[1].axvline(obs[1]-obs[0],color="tab:red",label="S16 separation")
ax[1].axvline(sep0,color="black",ls="--",label="Nominal Gaia")
ax[1].set(xlabel="Second minus first (d)",ylabel="Covariance draws")
ax[1].legend()
fig.suptitle("TIC 120239458 | Gaia DR3 AstroSpectroSB1 geometry")
fig.savefig(HERE/"conjunction-comparison.png",dpi=145)
plt.close(fig)
print(json.dumps(result,indent=2))
