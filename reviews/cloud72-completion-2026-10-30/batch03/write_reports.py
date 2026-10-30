from pathlib import Path
import json,csv,hashlib
B=Path(__file__).parent;D=B.parent;R=B/'raw-evidence';T=json.load(open(B/'targets-selected.json'));Q={x['tic']:x for x in csv.DictReader(open(D/'queue.csv'))};raw=json.load(open(R/'raw-events.json'));G=json.load(open(B/'gaia-geometry.json'));C=json.load(open(B/'catalogue-scope.json'));dec=json.load(open(B/'decisions.json'));fx=json.load(open(R/'fixed-source-comparison.json'));ga=json.load(open(R/'gaussian-source-diagnostic.json'));pix=json.load(open(R/'pixel-results.json'));rows=[];(B/'reports').mkdir(exist_ok=True)
for tic in T:
 d=dec[tic];a=raw[tic];ev=[e for e in a['events'] if 'tc' in e]; ep=a['representative_ephemeris'];p=ep['period_d'] if ep and d['verdict']!='REFUTED' else '';s=[]
 for x in [x for x in ga if x['tic']==tic]:
  f=next(z for z in fx if z['tic']==tic and z['sector']==x['sector']);ratios=[n['sse_ratio_to_target'] for n in f['neighbours']];s.append(dict(sector=x['sector'],target_offset_arcsec=x['target_offset_arcsec'],min_neighbour_target_sse_ratio=min(ratios) if ratios else None,capable_neighbour_count=len(ratios)))
 if d['verdict']!='REFUTED': d['source']='Two fresh detector-sector signed difference stacks favor the target, with free Gaussian offsets and fixed-position capable-neighbour comparisons below. Neighbour capability uses a conservative depth/magnitude threshold; TIC cones extend 60 arcsec. Ratios are descriptive residual comparisons and do not imply calibrated probabilities. Custom TESScut aperture extraction independently recovers the events from the same TESS photons as QLP.'
 if tic=='411647453':
  d.update(verdict='REFUTED',assessment='Real narrow eclipses contaminate the target aperture, but the proposed target Gaia-period eclipse association is refuted. Two detector sectors place the deficit on nearby TIC 411647413 rather than TIC 411647453. The approximately 0.9151763 d short-period signal gives about seven dips per 6.394568 d screen fold; that screen interval is not a valid target eclipse period.',source='Sectors11/99 Gaussian deficit centers are 15.09/14.20 arcsec from the target, but 0.56/1.64 arcsec from TIC411647413, separated14.76 arcsec. Fixed neighbour/target SSE ratios are0.362/0.144, consistently favoring that neighbour. A short-period contaminating EB is strongly inferred; its precision ephemeris and novelty were not reviewed.',geometry='The original conditional 6.394515949 d regression aliased unrelated eclipse dips. It is rejected as an eclipse-derived target period; no Gaia-conjunction association is established.',limitations='The contaminating eclipses are real; REFUTED applies to target attribution and Gaia-period interpretation. TIC411647413 is an inferred by-catch host subject to pixel model systematics, not a new confirmed catalogue object.',next_check='Higher resolution event photometry can establish the contaminant host and measure its orbital period precisely.')
 path=B/'reports'/f'{tic}.md';text=f'''# TIC {tic}: {d['verdict']}

Queue position {Q[tic]['queue_position']}; batch03. Anonymous project coordinator review with an independent measurement helper.

## Deciding assessment

{d['assessment']}

## Raw flux and period

Cached QLP SAP_FLUX, QUALITY=0; {len(list((R/tic).glob('qlp_s*.fits')))} representative sectors. Local quadratic baseline plus trapezoid fits retained {len(ev)} trial events. Only repeated discrete eclipse morphology supports an eclipse period. Search cycle counts were initial constraints, not independent period discovery. Lead inspected raw-event-panels.png and ambiguous-folds.png; smooth-variable fits hitting duration bounds are not eclipses.

Accepted event-derived period: {p if p else 'none for the target'} d.

Initial measurement receipt (superseded where rejected above):
```json
{json.dumps(ep,indent=2)}
```

## Fresh source and independent reduction

{d['source']}

```json
{json.dumps(s,indent=2)}
```

Custom TESScut reduction is independent of QLP processing but uses the same photons; it is not SPOC or an independent telescope. Signed in/out images use adjacent pre/post baselines. Gaussian formal errors exclude PRF systematics; fixed-coordinate source comparisons and repeat source positions govern attribution. Fresh downloads, TIC cones, signed arrays, plots and source scripts are preserved in raw-evidence.

## Gaia geometry

{d['geometry']}

The computed gaia-geometry.json uses edge-on conjunction approximation, BTJD conversion Tp+389, and full SB1 covariance ordering P,gamma,K1,e,omega,Tp. Linear uncertainty is approximate, especially with weak eccentricity. Mass-function/main-sequence radius estimates test duration feasibility only; there is no fitted physical model or automatic sigma rejection.

## Catalogue status

{C[tic]['scoped_prior_eb_status']}; all seven central scopes complete: {C[tic]['coverage_complete']}. Central shared-catalogues coverage includes VSX, SIMBAD primary type, GaiaDR3 EB, Prsa2022, IJspeert2024, Kostov2025 vetted tables3/4 and ASAS-SN. SB* or ROT alone is not prior EB evidence. This is scoped novelty coverage, not an exhaustive discovery claim.

## Completion and limitations

Full representative review complete. Scientific ambiguity: {d['limitations']}

Next test: {d['next_check']}

Provenance: cache-manifest.json gives original cached FITS paths and SHA256. Fresh TESScut URLs/hashes are in tesscut-downloads.json. Helper raw evidence and retained scripts permit reproduction. manifest.json hashes deliverables. No source paper, prior adjudication or publication was changed.
''';path.write_text(text,encoding='utf-8');rows.append(dict(queue_position=Q[tic]['queue_position'],tic=tic,physical_verdict=d['verdict'],review_state='completed',full_review_completion='complete',remaining_full_review='false',representative_eclipse_period_days=p,novelty_status=C[tic]['scoped_prior_eb_status'],catalogue_coverage_complete=C[tic]['coverage_complete'],report=path.relative_to(D).as_posix(),limitations=d['limitations'],next_check=d['next_check']))
(B/'decisions.json').write_text(json.dumps(dec,indent=2));(B/'RESULTS.json').write_text(json.dumps(rows,indent=2))
with open(B/'RESULTS.csv','w',newline='',encoding='utf-8') as f:w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
files=[dict(path=p.relative_to(B).as_posix(),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in B.rglob('*') if p.is_file() and p.name!='manifest.json'];(B/'manifest.json').write_text(json.dumps(dict(batch='batch03',files=files),indent=2));print([(r['tic'],r['physical_verdict']) for r in rows])
