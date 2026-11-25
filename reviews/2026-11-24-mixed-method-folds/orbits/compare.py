"""Compare each archived TESS fold epoch to the two edge-on Gaia conjunctions."""
import csv
from pathlib import Path

from astropy.time import Time
import numpy as np

HERE = Path(__file__).resolve().parent


def read(path):
    with path.open(newline="") as f:
        return list(csv.DictReader(f))


def compare(row, clock, orbit):
    fields = ["period", "eccentricity", "arg_periastron", "t_periastron"]
    par = np.array([float(orbit[k]) for k in fields])
    sig = np.array([float(orbit[k+"_error"]) for k in fields])
    assert orbit["nss_solution_type"] == "SB1" and orbit["bit_index"] == "127"
    # Gaia SB1 field order: P, systemic velocity, K1, e, omega, Tperi.
    full = np.eye(6)
    i,j = np.tril_indices(6,-1)
    full[i,j] = np.fromstring(orbit["corr_vec"].strip("(){}[]"),sep=",")
    full[j,i] = full[i,j]
    idx = [0,3,4,5]
    cov = full[np.ix_(idx,idx)] * np.outer(sig,sig)
    draws = np.random.default_rng(int(row["tic"])).multivariate_normal(par,cov,20000)
    draws = draws[(draws[:,0]>0)&(draws[:,1]>=0)&(draws[:,1]<1)]
    t = Time(2457000+float(clock["epoch_btjd"]),format="jd",scale="tdb").tcb.jd
    dt = t-Time(2016,format="jyear",scale="tcb").jd
    out = []
    for branch in (90,270):
        def difference(vals):
            p,e,omega,tp = np.asarray(vals).T
            halfnu = np.deg2rad(branch-omega)/2
            E = 2*np.arctan2(np.sqrt(1-e)*np.sin(halfnu), np.sqrt(1+e)*np.cos(halfnu))
            offset = (E-e*np.sin(E))*p/(2*np.pi)
            return (dt-tp-offset+p/2)%p-p/2
        nom = difference(par)
        oc = difference(draws)
        # Unwrap about the nominal residual before taking the quantiles.
        oc = nom+(oc-nom+par[0]/2)%par[0]-par[0]/2
        lo,md,hi = np.quantile(oc,[.025,.5,.975])
        w = float(clock["duration_d"])
        out.append(dict(tic=row["tic"],gaia_dr3=row["gaia_dr3"],angle_deg=branch,archive_epoch_btjd=clock["epoch_btjd"],
                        nominal_offset_days=nom,lower95_days=lo,median_days=md,upper95_days=hi,physical_draws=len(draws),
                        overlaps_core=bool(lo<=w/2 and hi>=-w/2)))
    return out


if __name__ == "__main__":
    orbits = {r["source_id"]:r for r in read(HERE/"gaia.csv")}
    clocks = {r["tic"]:r for r in read(HERE.parent/"ground/archived-clocks.csv")}
    rows = [x for r in read(HERE.parent/"batch.csv") for x in compare(r,clocks[r["tic"]],orbits[r["gaia_dr3"]])]
    with (HERE/"comparison.csv").open("w",newline="") as f:
        w = csv.DictWriter(f, rows[0],lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
