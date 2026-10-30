import json,pathlib,numpy as np
r=pathlib.Path(r'C:\Home\Astra\made\binary-handoff-2026-10-30\local-batch-b\full-vet')
for tic in ['295945076','372376841','416525506','451493289','348737250']:
 s=json.loads((r/f'{tic}_secondary_timing.json').read_text());m=json.loads((r/f'{tic}_measurements.json').read_text());ep=m['ephemeris'];a=[e for e in s['events'] if not e['center_edge']];ph=np.array([(e['tc']-ep['T0'])/ep['P']-e['cycle'] for e in a]);w=np.array([1/e['error_d']**2 for e in a]);jk=[]
 for sec in set(e['sector'] for e in a):
  keep=np.array([e['sector']!=sec for e in a]);jk.append(float(np.average(ph[keep],weights=w[keep])))
 phases=[]
 for mult in ['0.7','1','1.3']:
  candidates=[]
  for p in r.glob(tic+'_secondary_phase*.json'):
   x=json.loads(p.read_text());phase=float(p.stem.split('phase')[-1]);z=x.get('combined_'+mult)
   if .49<=phase<=.55 and z:candidates.append((z['depth'],phase))
  if candidates:phases.append(max(candidates)[1])
 scatter=float(np.std(jk,ddof=1)) if len(jk)>1 else 0;shape=max(abs(x-s['weighted_phase']) for x in phases);conservative=max(scatter,shape,.0025,s['formal_phase_error']);out={'weighted_phase':s['weighted_phase'],'formal_error':s['formal_phase_error'],'leave_one_sector_phase_scatter':scatter,'peak_phase_width_alternatives':phases,'max_width_phase_shift':shape,'conservative_phase_uncertainty':conservative,'caveat':'Grid peak quantization 0.005 cycles; envelope is heuristic and not calibrated coverage, includes lower bound 0.0025 cycles.'};(r/f'{tic}_secondary_phase_sensitivity.json').write_text(json.dumps(out,indent=2));print(tic,out)
