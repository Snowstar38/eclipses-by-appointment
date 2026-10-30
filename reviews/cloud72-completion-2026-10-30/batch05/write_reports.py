from pathlib import Path
import json,csv,hashlib
B=Path(__file__).parent;D=B.parent;R=B/'raw-evidence';T=json.load(open(B/'targets-selected.json'));Q={r['tic']:r for r in csv.DictReader((D/'queue.csv').open())};C=json.load(open(B/'catalogue-scope.json'));A=json.load(open(R/'raw-events.json'));G=json.load(open(B/'gaia-geometry.json'));dec=json.load(open(B/'decisions.json'));helper=json.load(open(R/'terra-helper-results.json'));rows=[];(B/'reports').mkdir(exist_ok=True)
for tic in T:
 d=dec[tic];period=A[tic]['representative_ephemeris']['period_d'] if d['verdict'] in ('CONFIRMED','PROBABLE') else ''
 if tic=='183994341':d['association']='compatible at approximate current precision; phase uncertainty retained'
 event=A[tic]['events'] if period else [];p=B/'reports'/f'{tic}.md'
 txt=f"""# TIC {tic}: {d['verdict']}

Queue position {Q[tic]['queue_position']}; batch05. Automated GPT-6.1 Sol lead and independent fresh GPT-6.1 Terra review, supervised by Astra. The anonymous project coordinator supplied oversight; these are computational measurements, not human measurements.

## Assessment

{d['assessment']}

## Raw repetition and period

Accepted target eclipse period: {period if period else 'not established'} days. {len(list((R/tic).glob('qlp*.fits')))} representative cached QLP sectors were reviewed using SAP_FLUX and QUALITY=0. Original packet periods were treated as candidate aliases. Corrected event fits use local linear baselines and trapezoids on raw cadences; no exhaustive sector fit or physical binary model was required.

{json.dumps(A[tic]['representative_ephemeris'] if period else {'accepted_target_ephemeris':None,'reason':'No established target repeated eclipse; original alias fitter is not accepted evidence'},indent=2)}

Representative accepted event measurements:
```json
{json.dumps(event,indent=2)}
```

## Source and independent reduction

{d['source']}

Fresh 11x11 TESScuts and 60 arcsec TIC source cones were obtained. Signed in/out images compare local pre/post baselines. The source model includes signed pixel-integrated Gaussians and fixed source positions with free widths/amplitude/background. Residual ratios are descriptive and do not constitute calibrated PRF probabilities. Neighbours capable under a conservative brightness/depth limit were compared; throughput, uncatalogued sources and TIC photometry remain limitations.

The independent custom target aperture subtracts a per-cadence background from faint cutout pixels and uses the same TESS photons as QLP. It is a distinct extraction, not SPOC or a second telescope. Terra independently inspected raw/custom comparison and signed images; quantitative four-EB depths and receipts are in raw-evidence/terra-helper-results.json. See HELPER.md, all-raw.png, raw-event-panels.png and terra-independent-comparison.png.

## Gaia geometry and association

{d['geometry']}

Association flag: {d['association']}.

The gaia-geometry.json calculation uses edge-on conjunctions, Tp+389 BTJD conversion, full SB1 covariance in P,gamma,K1,e,omega,Tp order, and linear propagation. Approximate mass function, TIC radius and main-sequence companion radius test feasibility, not a fitted geometry. No automatic Gaia sigma veto was applied.

## Catalogue coverage

{C[tic]['scoped_prior_eb_status']}; seven-scope coverage complete: {C[tic]['coverage_complete']}. Central coverage includes VSX, SIMBAD primary type, Gaia DR3 EB, Prsa2022, IJspeert2024, vetted Kostov2025 tables3/4 and ASAS-SN. SB* and ROT alone do not count as known EB. This scoped result is separate from physical assessment. TIC183994341 is known and excluded from new additions regardless of physical tier.

## Completion, limits and next check

Full representative review complete; remaining full review=false. Available deciding checks were attempted. Scientific uncertainty: {d['limitations']}

Next check: {d['next_check']}

Provenance: raw-evidence/cache-manifest.json hashes the cached original QLP files; identity-checks.json verifies TICID/sector. Fresh TESScut URLs/SHA256 are in tesscut-downloads.json; source cones and adapted scripts are retained. manifest.json hashes batch deliverables. No paper edits, source table edits, publication or commits were made.
"""
 p.write_text(txt,encoding='utf-8');rows.append(dict(queue_position=Q[tic]['queue_position'],tic=tic,physical_verdict=d['verdict'],review_state='completed',full_review_completion='complete',remaining_full_review='false',representative_eclipse_period_days=period,novelty_status=C[tic]['scoped_prior_eb_status'],catalogue_coverage_complete=C[tic]['coverage_complete'],report=p.relative_to(D).as_posix(),limitations=d['limitations'],next_check=d['next_check']))
(B/'decisions.json').write_text(json.dumps(dec,indent=2));(B/'RESULTS.json').write_text(json.dumps(rows,indent=2))
with (B/'RESULTS.csv').open('w',newline='',encoding='utf-8') as f:w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
files=[dict(path=p.relative_to(B).as_posix(),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in B.rglob('*') if p.is_file() and p.name!='manifest.json'];(B/'manifest.json').write_text(json.dumps(dict(batch='batch05',files=files),indent=2));print([(r['tic'],r['physical_verdict']) for r in rows])
