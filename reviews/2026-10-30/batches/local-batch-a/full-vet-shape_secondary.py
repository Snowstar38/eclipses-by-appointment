"""Refine each secondary shape from a preliminary secondary_fit.py run."""
import json
import fit_batch as f
for tic in f.targets:
 p=f.ROOT/tic;r=json.load(open(p/'fit-results.json'));s=json.load(open(p/'secondary-fit.json'));e=r['ephemeris'];f.P=e['P'];ss=s['ephemeris']
 tsec=ss['T0'] if ss else e['T0']+s['profile_phase']*e['P']
 shape=f.shape_fit(f.read(tic),e['P'],tsec,f.search[tic]['dur'])
 json.dump(shape,open(p/'secondary-shape.json','w'),indent=2)
