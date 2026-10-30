from pathlib import Path
import json,csv,hashlib
B=Path(__file__).parent;D=B.parent;R=B/'raw-evidence';T=json.load(open(B/'targets-selected.json'));raw=json.load(open(R/'raw-events.json'));geo=json.load(open(B/'gaia-geometry.json'));cats=json.load(open(B/'catalogue-scope.json'));Q={r['tic']:r for r in csv.DictReader(open(D/'queue.csv'))};dec=json.load(open(B/'decisions.json'));reports=B/'reports';reports.mkdir(exist_ok=True);rows=[]
for tic,t in T.items():
 d=dec[tic];a=raw[tic];g=geo[tic];ev=[e for e in a['events'] if 'tc'in e];ep=a['representative_ephemeris'];p=ep.get('period_d',ep.get('candidate_binary_period_d','')) if ep else '';good=[e for e in ev if not e['edge']];deps=[e['depth'] for e in good];pix=[x for x in json.load(open(R/'pixel-results.json')) if x['tic']==tic];gaus=[x for x in json.load(open(R/'gaussian-source-diagnostic.json')) if x['tic']==tic];text=f'''# TIC {tic}: {d['verdict']}

Queue position {Q[tic]['queue_position']}; batch04. Review by GPT-6.1 Sol with a fresh GPT-6.1 Terra helper, supervised by Astra. Physical classification and prior-catalogue status are separate.

## Deciding assessment

{d['assessment']}

## Raw events and eclipse period

Two or three cached QLP SAP_FLUX sectors were checked with QUALITY=0. Representative events use local quadratic baselines plus trapezoid fits; TIC 60443793 instead uses the independently corrected alternating-minimum series, retained alongside the original search alias receipt. {len(ev)} representative fits were retained in raw-events.json, {len(good)} clear of fit bounds. {('Depth range '+str(round(min(deps)*100,3))+'–'+str(round(max(deps)*100,3))+' percent.') if deps else 'No detached event established.'} Period from representative event centers: {p if p else 'not established as an eclipse period'}. Search-cycle counts are conditional on the initial search except where the corrected alternating-minimum receipt explicitly supersedes that alias. No timing uncertainty or ephemeris prediction is claimed.

{json.dumps(ep,indent=2) if ep else 'Smooth-variable morphology is assessed in ambiguous-folds.json and helper receipts.'}

## Source imaging and independent reduction

{d['source']}

Fresh TESScut cutouts are a distinct custom aperture reduction of the same TESS photons as QLP; they are not SPOC and do not supply an independent telescope. No claim of a separate SPOC pipeline is made. Signed in/out images use adjacent pre/post windows. Positive-clipped centroids and Gaussian formal errors are diagnostics subject to PRF mismatch; target-specific repeat tests and capable-neighbour comparisons govern attribution.

## Gaia geometry

{d['geometry']}

Computed receipt: gaia-geometry.json. Linear covariance propagation uses SB1 correlation order P,gamma,K1,e,omega,Tp; conjunction uses edge-on approximation. The mass-function/MS-radius duration is a feasibility estimate, not a physical fit. Circular/low-eccentricity periastron phases may be weakly constrained.

## Prior EB coverage

{cats[tic]['scoped_prior_eb_status']}; seven-scope coverage complete: {cats[tic]['coverage_complete']}. Reused central coverage-matrix.csv and catalogue-scope.json: VSX, SIMBAD primary type, Gaia DR3 EB, Prsa2022, IJspeert2024, Kostov2025 vetted tables3/4, ASAS-SN. SB* or ROT alone are not EB identifications. This scoped result is not an exhaustive discovery claim.

## Completion, limitations and next check

Signal class: {d.get('signal_class','candidate variable')}; Gaia association: {d.get('gaia_association','assessed below')}.

Execution: completed representative full review; scientific ambiguity: {d['limitations']}

Next deciding check: {d['next_check']}

Provenance: cache-manifest.json preserves original cached FITS paths and SHA256; identity-checks.json matches TICID/SECTOR for all28 input QLP files. tesscut-downloads.json records fresh source URLs and zip hashes; signed images and helper evidence have hashes. manifest.json records deliverable checksums. Adapted scripts are retained. No source-paper edits or publication performed.
''';path=reports/f'{tic}.md';path.write_text(text,encoding='utf-8');rows.append(dict(queue_position=Q[tic]['queue_position'],tic=tic,physical_verdict=d['verdict'],review_state='completed',full_review_completion='complete',remaining_full_review='false',representative_eclipse_period_days=p,signal_class=d.get('signal_class',''),gaia_association=d.get('gaia_association',''),novelty_status=cats[tic]['scoped_prior_eb_status'],catalogue_coverage_complete=cats[tic]['coverage_complete'],report=str(path.relative_to(D)).replace('\\','/'),limitations=d['limitations'],next_check=d['next_check']))
with open(B/'RESULTS.csv','w',newline='',encoding='utf-8') as f:w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
(B/'RESULTS.json').write_text(json.dumps(rows,indent=2));files=[]
for p in B.rglob('*'):
 if p.is_file() and p.name!='manifest.json':files.append(dict(path=p.relative_to(B).as_posix(),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
(B/'manifest.json').write_text(json.dumps(dict(batch='batch04',files=files),indent=2));print(len(rows),len(files))
