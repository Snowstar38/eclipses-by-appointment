from pathlib import Path
import csv,json,hashlib,math
B=Path(__file__).parent;D=B.parent
ids=list(json.loads((B/'targets-selected.json').read_text()));C=[r for r in csv.DictReader((D/'shared-catalogues/coverage-matrix.csv').open()) if r['tic'] in ids]
(B/'catalogue-review.json').write_text(json.dumps(C,indent=2))
S=json.loads((B/'source-review.json').read_text())
for t,v in S.items():
 v['lead_visual_inspection']=t in ['29741740','417917895','162075402']
 v['source_assessment']=f"Cached eclipse deficit peaks at the target pixel, offset {v['target_distance_arcsec']:.3f} arcsec. "
 if t=='29741740':v['source_assessment']+='The G-band flux-capable neighbour is 43.24 arcsec from the target and 50.58 arcsec from the eclipse deficit; the disappearing source is localized near the target rather than that neighbour. The field is crowded; faint neighbours and colour-dependent flux limits remain caveats. '
 elif t=='417917895':
  v['source_assessment']+='The flux-capable neighbour is 12.43 arcsec away, 14.35 arcsec from the stacked deficit. A bounded repeatability check using the two separate cached sector-15 events gives target offsets 3.02 and 3.17 arcsec versus neighbour offsets 13.90 and 14.81 arcsec. Shifting the empirical blended out-of-eclipse template to target versus neighbour gives fractional residuals 0.128 versus 0.595; this descriptive shape diagnostic favours the target. Own-pixel losses are mixed and do not alone exclude the neighbour. This supports target attribution without assigning a calibrated centroid significance. See raw-evidence/417917895/source_repeatability.json. '
 else:v['source_assessment']+='No Gaia G-band flux-capable neighbour is recorded within 60 arcsec. '
 if t=='162075402':
  d=json.loads((B/'raw-evidence'/t/'diff_s80.json').read_text());ns={x['source_id']:x for x in d['neighbours_60']};vs=[]
  for sid in ['4251816451161098880','4251816554240317568','4251813599322538112']:
   if sid in ns:vs.append(ns[sid])
  v['nearby_catalogued_eb_checks']=vs
  v['source_assessment']+='The exact ASAS-SN ROT: identity and 0.80 arcsec VSX VAR entry are not prior-EB types. Nearby VSX E entries at 14.92, 40.16 and 58.55 arcsec identify distinct Gaia sources with periods 1.29114, 0.307656 and 6.9854 d; none is G-band flux-capable in the cached 60-arcsec source check, and their periods differ from the target primary eclipse period. '
 v['source_assessment']+='Centroid displacements are descriptive; G/TESS band differences, uncatalogued or unresolved blends and PSF modelling limit the test. '
 if v['lead_visual_inspection']:v['source_assessment']+='The lead inspected the cached difference-image panel. '
(B/'source-review.json').write_text(json.dumps(S,indent=2))
inputs=[D/'queue.csv',D/'targets-selected.json',D/'shared-catalogues/coverage-matrix.csv',D/'shared-catalogues/gaia-nss_two_body_orbit.csv']+list((B/'raw-evidence').glob('*/*.json'))+list((B/'raw-evidence').glob('*/*.png'))
(B/'lead-input-provenance.json').write_text(json.dumps([dict(path=str(p),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in inputs],indent=2))
print([(t,[(x['source_id'],x['G'],x['depth_needed']) for x in v.get('nearby_catalogued_eb_checks',[])]) for t,v in S.items() if t=='162075402'])
