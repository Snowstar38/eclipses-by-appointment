import json
from pathlib import Path
B=Path(__file__).resolve().parent;A=json.loads((B/'coverage-alias.json').read_text());out={}
for tic,obs,tol,meaning in [('436013770',json.loads((B/'436013770'/'partial-third-event.json').read_text())['median_deep_time_btjd'],.25,'Median actual deep raw samples from third partial eclipse; 0.25d is a descriptive central-interval allowance, not a timing error.'),('449012335',4085.18444,.05,'Independently extracted same-photon s100 contact midpoint, with 0.05d descriptive comparison tolerance; custom formal error is not total uncertainty.')]:
 vals=[]
 for a in A[tic]['aliases']:
  P=a['period_days'];ep=A[tic]['epoch_btjd'];res=abs(((obs-ep+P/2)%P)-P/2);vals.append(dict(label=a['label'],period_days=P,third_observed_statistic_btjd=obs,nearest_recurrence_residual_days=res,rejected_by_third_occasion=res>tol))
 out[tic]=dict(comparison_tolerance_days=tol,meaning=meaning,alias_checks=vals)
# Orbital period remains unestablished for two sparse pairs and the harmonic crowded source.
for tic in ('349527829','95836684','25320385'):
 p=B/tic/'measurements.json';m=json.loads(p.read_text());m.update(generic_orbital_period_days=None,generic_orbital_period_error_days=None,generic_orbital_epoch_btjd=None,period_status=('Measured dip recurrence/harmonic ephemeris only; opposite eclipse kinds and orbital factor of two unresolved.' if tic=='25320385' else 'Conditional two-event cycle-count ephemeris only; alternative integer counts remain. Generic orbital ephemeris intentionally unestablished.'));p.write_text(json.dumps(m,indent=2)+'\n')
p=B/'449012335'/'measurements.json';m=json.loads(p.read_text());m['depth_meaning']='Fitted local linear-baseline trapezoid central loss, diluted and baseline dependent; refined fit events use saturated flat-bottom profiles.';p.write_text(json.dumps(m,indent=2)+'\n')
(B/'third-occasion-aliases.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
