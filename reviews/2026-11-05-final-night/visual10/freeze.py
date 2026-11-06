from pathlib import Path
import csv,json,hashlib,collections
B=Path(__file__).resolve().parent
Q=list(csv.DictReader((B/'queue.csv').open()));R=list(csv.DictReader((B/'RESULTS.csv').open()));expected=json.loads((B/'selection.json').read_text())['queue_sha256'];assert hashlib.sha256((B/'queue.csv').read_bytes()).hexdigest()==expected;assert len(Q)==len(R)==10;assert [(r['sample_id'],r['tic'],r['gaia_dr3']) for r in Q]==[(r['sample_id'],r['tic'],r['gaia_dr3']) for r in R];assert R[6]['physical_tier']=='PLAUSIBLE' and R[6]['period_days']==''
receipts=json.loads((B/'lead-source-receipts.json').read_text())
for r in receipts:assert hashlib.sha256(Path(r['path']).read_bytes()).hexdigest()==r['sha256']
audit='''# Lead audit - frozen visual10

Completed bounded physical review of exact X001-X010, with no replacement or denominator change. Queue SHA-256 8ee3f338008260a44969d708029fbf7fe461e39f4c4bdec87e913b3a453dbbf1 matches selection.json. Every cached raw FITS input was hashed and its TICID checked before use. Output is confined to visual10; no ledger or public files were edited.

Final outcomes: 1 CONFIRMED (X003), 1 PROBABLE (X004, short-period by-catch), 2 PLAUSIBLE (X007, X008), 6 REFUTED selected patterns (X001/X002/X010 contaminated; X005/X006/X009 continuous variable structure). Physical tier, completion, association and publication eligibility remain separate. REFUTED never excludes a different hidden binary.

The lead viewed all ten all-sectors.png files and ranked windows for X003/X005/X006/X007/X008/X010, both lead-pixels.png files for X003/X007, all four helper-pixels.png maps for X001/X002/X004/X010, and X007 lead-gaia-repeat-windows.png. Helper independently reviewed the pixel maps and ambiguity windows (helper-audit.md). Lead owns final verdicts. Raw SAP was finite positive QUALITY=0; detector windows are guides, not measured event times or calibrated significances.

Deciding exceptions:

* X003: five raw same-kind events, 48.58726285 d recurrence, shorter integer aliases 2-10 tested against actual sampled intermediate windows; target-centered S76 difference and custom extraction; full Gaia SB1 covariance conjunction B passes. A successful 108-arcsec Gaia cone contains seven conservatively capable neighbors, nearest 55.82 arcsec; the observed deficit follows the target. Meets bounded confirmation checks. Independent extraction uses the same photons.
* X004: repeated sharp target-region loss, local consecutive minimum spacing 3.19139 d, target-centered 0.19-pixel diagnostic centroid. No PSF fit or close-blend exclusion. Orbital doubling unresolved; this is PROBABLE short-period by-catch, not an established 58.98 d Gaia eclipse.
* X007: two secure complete flat-bottomed events; S72 later notch is shorter and baseline dependent; S46 partial primary has singular timing covariance and is excluded from timing. Working 36.50930 d and P/2 remain alternatives. Explicit divisor-2 coverage audit does not reject P/2: S46 shows another notch and S71 is ramp dominated. Full Gaia covariance has ~2.46 d phase tension; neighbor inventory requests failed. Final PLAUSIBLE with blank adopted period. This retains the real eclipse-like variability without claiming a unique system/clock association. Updated from tentative probable after helper critique.
* X008: credible S39 singleton interrupted at egress; later S103/S104 flags are step/ramp/gap features, not secure repeats. Current TESScut query returns only the six cached science sectors. PLAUSIBLE, not an unperformed review.

Source and numerical provenance:

screen_raw.py creates the all-sector context and checks bulk SHA/TIC identities. measure.py creates initial local minima and centroid diagnostics; initial-minima-diagnostics.json is explicitly superseded where stated. seven_fit.py then reconcile_clocks.py establish working X007 alternatives; singular S46 is not timed. deciding.py records actual alias windows and source-specific mean conjunctions; geometry_mc.py propagates the full published SB1 corr_vec with seed 2026110507 and 20000 draws, rejecting unphysical eccentricities. These diagnostics do not assign precision errors to the representative clock or event-kind ambiguity. fetch_cuts.py and helper-fetch.py document MAST requests; custom reductions and difference images reuse TESS photons. neighbours.py / neighbours_retry.py record both success and failures. capable.py calculates conservative all-throughput G-proxy neighbor feasibility, separately from blended aperture fractions. write_reports.py creates all ten reports and RESULTS.csv. Central catalogue files and ROOT-CATALOGUE-SEAL.json are retained as supplied by root; root owns novelty eligibility.

Validation: exact identity/order and all ten reports checked; X007 adopted period blank; cached source hashes rechecked at final freeze. SHA256SUMS.json hashes every file inside visual10 except itself and validation.json; validation.json pins the manifest and the exact source count. No untested catalogue request is interpreted as a non-match.

Contributor note: The helper's independent localization and alias critique materially changed the conclusions, especially X004 and X007. Thank you to the project coordinator for supporting careful bounded review.
'''
(B/'LEAD-AUDIT.md').write_text(audit,encoding='utf8')
# Every report exists and final tiers sum to exact cohort.
for r in R:assert (B/r['report']).exists()
manifest={str(p.relative_to(B)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(B.rglob('*')) if p.is_file() and p.name not in ['SHA256SUMS.json','validation.json']}
(B/'SHA256SUMS.json').write_text(json.dumps(manifest,indent=2)+'\n')
val=dict(queue_sha256=expected,n_targets=len(R),n_source_receipts=len(receipts),tier_counts=dict(collections.Counter(r['physical_tier'] for r in R)),all_source_hashes_reverified=True,all_report_paths_exist=True,manifest_files=len(manifest),manifest_sha256=hashlib.sha256((B/'SHA256SUMS.json').read_bytes()).hexdigest(),results_sha256=hashlib.sha256((B/'RESULTS.csv').read_bytes()).hexdigest(),scope='exact selected patterns; root owns catalogue and publication decisions')
(B/'validation.json').write_text(json.dumps(val,indent=2)+'\n');print(json.dumps(val,indent=2))

