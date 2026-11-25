"""Test the edge-on prediction of the published SB2 orbit, independently of its absolute period."""
import csv,json,math
from pathlib import Path
D=Path(__file__).resolve().parent
def secondary_phase(e,wdeg):
    w=math.radians(wdeg)
    def mean_anomaly(f):
        E=2*math.atan2(math.sqrt(1-e)*math.sin(f/2),math.sqrt(1+e)*math.cos(f/2))
        return E-e*math.sin(E)
    return ((mean_anomaly(1.5*math.pi-w)-mean_anomaly(.5*math.pi-w))/(2*math.pi))%1
def main():
    with (D/"gaia/gaia_nss.csv").open(encoding="utf-8-sig") as f:r=next(csv.DictReader(f))
    e,w,se,sw=(float(r[k]) for k in ["eccentricity","arg_periastron","eccentricity_error","arg_periastron_error"])
    ph=secondary_phase(e,w)
    # Sensitivity over a rectangle of marginal parameters, not a joint confidence interval.
    trial=[secondary_phase(e+se*a/20,w+sw*b/20) for a in range(-60,61) for b in range(-60,61)]
    j=json.loads((D/"sol/ephemeris.json").read_bytes())
    result=dict(assumption="edge-on Keplerian orbit, two conjunctions at true longitude 90 and 270 degrees; neglect light travel and precession",eccentricity=e,argument_periastron_deg=w,phase=ph,phase_if_families_swapped=1-ph,
                photo_phase=j["secondary_phase"],range_three_marginal_errors=[min(trial),max(trial)],range_if_swapped=[1-max(trial),1-min(trial)])
    (D/"geometry.json").write_text(json.dumps(result,indent=1),encoding="utf8");print(result)
if __name__=="__main__":main()
