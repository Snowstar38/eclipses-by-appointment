from pathlib import Path
import json,csv,hashlib
B=Path('[local working path omitted; see provenance receipts]');R=json.loads((B/'raw-evidence/raw-events.json').read_text())
for p in B.glob('TIC-*.md'):
 t=p.stem[4:];text=p.read_text(encoding='utf-8')
 if t=='311918550':
  e=R[t]['events'];pairs=[(e[j+1]['tc']-e[j]['tc'])/(e[j+1]['cycle']-e[j]['cycle']) for j in [0,2,4]]
  text+='\nGaia orbit caveat: the eclipse-derived period differs from Gaia by 0.011414624 d (8.56 quoted Gaia period errors). Consecutive events within sectors 19,45,72 independently give '+', '.join(f'{x:.9f}' for x in pairs)+' d, so the discrepancy is not caused only by long-baseline cycle assignments. Accumulated drift is about 1.15 d across 101 cycles. Gaia conjunction at the representative epoch is nevertheless compatible within its 0.528 d propagated covariance scale and the duration is geometrically feasible. The target EB is confirmed from localized repeated eclipses and the independent extraction; precise Gaia orbit agreement and orbit association are unresolved, not asserted. Next test: obtain or refit RVs to test the Gaia period against the eclipse period, and check for orbit complexity.\n'
 elif t=='101779765':text+='\nNext test: resolved eclipse-time imaging or a calibrated multi-source pixel model that can distinguish the 3.63 arcsec pair. Complete execution of the five checks does not remove source ambiguity.\n'
 else:text+='\nNext tests for characterization: exposure-integrated eclipse modelling and stellar/RV constraints; refine dilution with resolved photometry where needed. These are follow-up opportunities rather than missing execution steps.\n'
 p.write_text(text,encoding='utf-8')
(B/'README.md').write_text('''# Batch 07 review

Positions 61–70 only: nine CONFIRMED target EBs and one PLAUSIBLE (TIC 101779765, unresolved 3.63 arcsec capable neighbour). All ten full reviews complete. TIC 311918550 is a confirmed target EB with a significant Gaia-period contradiction retained explicitly; its Gaia orbit association needs follow-up.

Representative QLP raw events, eclipse-derived periods, cached difference imaging, independent custom TESScut extraction and Gaia geometry were reviewed. TESScut uses the same photons through an independent pipeline, not SPOC or independent observations. The helper and lead reviewed raw panels; the lead viewed targeted difference images for 101779765, 233269866, 287032105, 122024194. A bounded split-stack/template test supports 233269866 attribution. No Monte Carlo, exhaustive fitting or formal new centroid calibration was required.

Catalogue matrix and Gaia NSS receipts are reused from ../shared-catalogues without repeated queries. No identified prior EB in the seven checked scopes for these ten; this is scoped coverage, not proof of novelty. Reports contain limitations and next tests. manifest.json hashes all deliverables except itself. Public wording is anonymous. No source-paper edits or commits.
''',encoding='utf-8')
p=B/'validate.py';s=p.read_text().replace("queue_positions='41-50'","queue_positions='61-70'").replace('targeted cached difference images140802498,293946483,4374712; bounded140802498repeatability and template comparison','raw panel all ten; targeted cached difference images101779765,233269866,287032105,122024194; bounded233269866repeatability and template comparison');p.write_text(s)
inputs=[B.parent/'queue.csv',B.parent/'targets-selected.json',B.parent/'shared-catalogues/coverage-matrix.csv',B.parent/'shared-catalogues/gaia-nss_two_body_orbit.csv']+list((B/'raw-evidence').glob('*/*.json'))+list((B/'raw-evidence').glob('*/*.png'))
(B/'lead-input-provenance.json').write_text(json.dumps([dict(path=str(p),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in inputs],indent=2))

