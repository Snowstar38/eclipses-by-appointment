"""Render explicit lead adjudications; not an automatic classifier."""
from pathlib import Path
import json,csv,math,hashlib,datetime
import numpy as np
from astropy.time import Time
F=Path(__file__).parent;D=F.parent;T=json.load(open(D/'targets-selected.json'));A=json.load(open(F/'archive-shared-gates.json'));N=json.load(open(F/'neighbors-summary.json'));I=json.load(open(F/'independent-summary.json'));DG=json.load(open(F/'review-diagnostics.json'));TC=json.load(open(F/'timing-covariance.json'))
notes={
'240360239':'CONFIRMED target EB. Both eclipse kinds repeat over many cycles and agree with the SB1 ephemeris. Own sector56 pixel fits resolve the capable neighbor44.8arcsec away. Absolute depth depends on baseline: independent aperture quadratic43.5–47.4ppt versus linear54.8–61.1ppt; use the timing and source attribution more strongly than exact radius/depth inference.',
'341735257':'CONFIRMED target EB. Seven primary and eight secondary measurements, independent reduction and own sector79 localization support target over the capable neighbor18.53arcsec away. Primary geometry touches the low-impact-parameter grid boundary; dimensions are not uniquely measured.',
'306553279':'CONFIRMED target eclipsing system with one observed eclipse kind. It matches Gaia B, not A; the resolved11.9604d period is used. The opposite conjunction is genuinely covered and null under the tested widths/phases. Eccentric geometry can hide that eclipse. Narrow events survive the smooth tide+harmonics adversary. Which luminous component is being eclipsed remains a characterization issue, particularly because the deeper event is at B; no unique temperature/radius solution is claimed.',
'56534111':'CONFIRMED target EB. Both kinds repeat, independent TARS confirms the narrow primary and own sector88 per-pixel regression favors target over all six capable neighbors. Nearby VSX pulsator and IJspeert entries belong to different Gaia/TIC sources. Difference-light centroid bias and aperture dilution explain why the original offset alone was insufficient. TARS depths35.6–38.5ppt versus QLP40.8–44.5ppt are a dilution/baseline caveat.',
'31357336':'CONFIRMED target EB. Primary/secondary timing is essentially circular; Gaia relative-phase tension is2.87sigma and primary epoch389 timing differs2.9sigma, suggesting refinement of its low-e RV orbit. It does not erase the repeatable target-localized eclipses. The capable neighbor48.6arcsec away is a VSX pulsator, distinct from target; original deficit/light separation1.16arcsec strongly favors target. Grazing geometry means trapezoid flat duration cannot measure e sin omega.',
'342454977':'CONFIRMED target EB. Over100 independently timed events per kind, alternate TARS reduction, and original near-target difference image support target. Simple geometry has chi2/dof~7.1, indicating stellar dimensions, dilution or baseline/model mismatch; its grid intervals are not calibrated orbital constraints. TARS baseline changes depth by2.3–7.3ppt. Physical confirmation rests on the attributed repeat eclipses and SB1 match.',
'455214882':'CONFIRMED target eclipsing system with one observed kind at Gaia A. Six repeat events, independent TESS-SPOC, no capable Gaia neighbor and original deficit-light separation0.28arcsec establish attribution. Covered opposite windows remain null; eccentric grazing geometry provides a feasible missed B eclipse. A narrow eclipse is required beyond smooth tide+five harmonics. Component light/radii remain uncertain.',
'140477577':'CONFIRMED target EB. Nine primary and seven secondary timings, independent TESS-SPOC, no capable neighbor and original deficit-target0.13arcsec support attribution. Both kinds agree with a shared period and Gaia conjunctions; radius ratio/impact parameter remain degenerate.',
'190972398':'CONFIRMED eccentric target EB. Five primary and four secondary timings establish the strongly non-half-cycle secondary, phase0.71817, agreeing with Gaia exact eccentric timing. A first-order e cos omega approximation is inadequate at e~0.35. Original deficit-light0.33arcsec and no capable neighbors support source attribution. The simplified chord geometry has residual tension and is only a feasibility exploration.',
'349273287':'CONFIRMED target EB.147primary and127 individually significant secondary timings plus TARS establish recurrence. Own sector97 pixel regression favors target over the flagged27.85arcsec neighbor after including a bright source outside the60arcsec Gaia cone. Moving that empirical nuisance source±0.2pixel keeps target preferred; exact centroid errors are not calibrated. Blind-census extra features in sectors62/65/69 are broad quality-contaminated ramps, not repeat eclipse-shaped events. Sector65 feature coincides with the known3082.8 common-mode interval and its fitted depth drops35.6 to16.5ppt on background regression. These features limit baseline purity, not the well-localized5.54727d eclipses.'}
nexts={x:'Obtain joint RV/eclipse and stellar-radius constraints for characterization.' for x in T}
nexts['31357336']='Refit the Gaia small-e orbit jointly with both eclipse ephemerides.'
nexts['349273287']='Calibrate a multi-source empirical PSF and obtain less diluted eclipse photometry.'
nexts['306553279']='Characterize temperatures/component assignment and test the covered null secondary with resolved multiband photometry.'
nexts['455214882']='Constrain grazing geometry and component light with resolved multiband photometry.'
diff={}
for name in ['diffrun.jsonl','diffrun-c4.jsonl']:
 for l in (D/name).read_text().splitlines():
  if l: r=json.loads(l);diff[r['tic']]=r
now=float(Time('2026-10-30T20:00:00',scale='utc').jd-2457000);res=[]
for tic,t in T.items():
 p=F/tic;r=json.load(open(p/'fit-results.json'));o=json.load(open(p/'orbit-gates.json'));s=json.load(open(p/'secondary-fit.json'));g=json.load(open(p/'geometry.json'));n=json.load(open(p/'gaia-nss.json'));ep=r['ephemeris'];diag=DG[tic];tc=TC[tic];depth=diag['primary_depth_median'];good=[e for e in r['events'] if e['status']=='fit'];bg=diag['background_largest_fake_depth'];sec=s['statistic'];pr=o['primary_conjunction'];other='B' if pr=='A' else 'A';pp=ep['T0']+math.ceil((now-ep['T0'])/ep['P'])*ep['P'];se=s['ephemeris'];sp=(se['T0']+math.ceil((now-se['T0'])/se['P'])*se['P']) if se else ep['T0']+o['predicted_secondary_phase']*ep['P']+math.ceil((now-ep['T0']-o['predicted_secondary_phase']*ep['P'])/ep['P'])*ep['P']
 fields=sorted(set(k for e in r['events']+s['events'] for k in e))
 with (p/'event-measurements.csv').open('w',newline='') as h:
  w=csv.DictWriter(h,fieldnames=['kind']+fields);w.writeheader()
  for kind,rows in [('primary',r['events']),('secondary',s['events'])]:
   for e in rows:w.writerow({'kind':kind,**e})
 capable=[x for x in N[tic] if x['capable']]
 text=f'''# TIC {tic}: CONFIRMED

Full review completed; all applicable gates attempted/adjudicated, with limitations below. Reviewed2026-10-30 by Sol lead with fresh Terra independent photometry/localization helper. Original candidate status and absence of original vet directory checked before work; original files unchanged.

{notes[tic]}

## Raw SAP measurements and timing

QUALITY==0 raw SAP, no post-gap trimming or detrended QLP flux. All flagged cadences inspected numerically; {diag['flagged_core_events']} fitted event cores contain some flagged points, excluded from fits. Exposure-integrated trapezoids with local quadratic baselines, residual-bin red-noise inflation and grid floors; timing errors and chi2-scaled ephemeris retained. No primary timing scan reaches an edge. Individual mid-times, errors, depths/errors, total/ingress/flat durations, O-C, quality, background and centroid statistics are in [event-measurements.csv](event-measurements.csv), including explicit insufficient-coverage windows. Shared-shape duration uncertainties are conditional; individual CSV durations are not separately fitted shape posteriors.

Primary median depth {depth*1000:.3f}ppt; fitted total duration {r['shape']['T14']*24:.3f}h, grid/profile interval {np.array(r['shape']['T14_range'])*24}h; ingress {r['shape']['fr']*r['shape']['T14']*24:.3f}h and flat {r['shape']['T14']*(1-2*r['shape']['fr'])*24:.3f}h. The fitted flat in a partial eclipse does not imply physical totality.

P={ep['P']:.10f}±{ep['P_error']:.2g}d; Tref={ep['Tref']:.7f}±{ep['Tref_error']:.2g}BTJD at cycle{ep['reference_cycle']}; T0={ep['T0']:.7f}. {ep['n']}timings; O-C RMS{ep['oc_rms_minutes']:.2f}min; chi2/dof={ep['chi2']:.2f}/{ep['dof']}. Sector depths: `{json.dumps(diag['sector_depths'])}`.

Secondary conditional fit: phase{ s['profile_phase']:.7f}; depth{sec.get('depth',0)*1000:.3f}ppt; formal error{sec.get('error',0)*1000:.3f}ppt; empirical error{sec.get('empirical_error',0)*1000:.3f}ppt; {sec.get('n',0)}covered fitted windows, {sec.get('n_individual_gt3sigma',0)}individual >3sigma detections. Phase optimization is not a blind significance claim; repeat event detections, fixed Gaia/control tests and full coverage exclusions remain in secondary-fit.json/orbit-gates.json. Secondary ephemeris: `{json.dumps(se)}`.

Largest background-projected fake primary depth{bg*1000:.3f}ppt, median depth change on background regression{diag['background_median_depth_change']*1000:.3f}ppt. Native SAP_BKG is never divided by normalized flux. Blind rolling-median census has{diag['blind_census_count']}runs and{len(diag['offphase_deep'])}deep off-eclipse-phase runs; flags/gaps and broad ramps are retained rather than counted as astrophysical eclipses. See review-diagnostics.json and any offphase-controls/context products.

## Gaia covariance, geometry and physics

Exact source{t['gaia']['source_id']}; SB1, bit_index127,15lower-triangle correlations verified independently for this source. Covariance order P,gamma,K1,e,omega,Tp, with angular units converted. Own20000/40000draw checks; no copied correlation. Primary matches{pr}; delta P={o['period_delta_sigma']:.3f}sigma. Conjunction comparisons at every event and Gaia epoch389 are in orbit-gates.json. Epoch389(primary) offset/error: {next(x for x in o['gaia_comparison'] if x['kind']==pr)['epoch389_offset']:.5f}/{next(x for x in o['gaia_comparison'] if x['kind']==pr)['epoch389_gaia_error']:.5f}d.

Exact Gaia relative-phase and e-components: `{json.dumps(tc)}`. Photometric phase diagnostic: `{json.dumps(diag['timing'])}`. When e is small, timing can refine a biased small-e RV solution; phase matching and source localization establish system identity. The first-order e cos omega diagnostic is explicitly not used for precise high-e inference.

RV mass function and conditional dimensions/central durations: `{json.dumps(o['physics'])}`. Minimum companion masses are stellar under the listed M1 assumptions. Companion radius uses an explicit main-sequence approximation, not a measurement. Limb-darkened two-disk shape exploration: `{json.dumps(g)}`. Its coarse fixed-TIC dimensions, depth/dilution freedom and simplified chord speeds limit parameter inference; profile ranges are not calibrated uncertainties. In the standard primary-RV convention A has the companion in front and B has the primary in front; observed depth alone cannot identify which component is hotter, and unresolved multiplicity/stellar dimensions remain characterization caveats.
'''
 if (p/'null-secondary.json').exists():
  nu=json.load(open(p/'null-secondary.json'));ti=json.load(open(p/'tide-test.json'));text+=f'''\nCovered null opposite-kind test:45conditional phase/shape tests across5durations and±2sigma Gaia phase covariance; phase sigma{nu['phase_sigma_covariance']:.6f}. Pointwise3sigma upper limits range{np.array(nu['upper_limit_range'])*1000}ppt. Each test preserves its individual windows and exclusions in null-secondary.json; no assertion that uncovered/flagged windows are null. Feasible eccentric missing-eclipse geometry: `{json.dumps(nu['geometry'])}`. Smooth equilibrium tide+five harmonics versus same+narrow primary yields deltaBIC={ti['delta_BIC_tide_only_minus_plus_eclipse']:.1f}, RSS{ti['rss']}; sector narrow depths{ti['eclipse_depths']}. This is an adversarial smooth-variability test, not calibrated false-alarm probability.\n'''
 text+=f'''
## Independence, dilution and source

Own alternate photometry: `{json.dumps(I[tic])}`. Detailed individual baseline/error/quality/product identity and hashes are in independent-summary.json and independent-manifest.json. These are independently reduced TESS pixels, not independent observatory data. Independent products use their own available quality cuts; TARS has no quality column.

GaiaG<15 neighbor cone: {len(N[tic])}non-target sources, {len(capable)}capable by the G-band total-flux upper-bound approximation depth×10^(0.4deltaG). Exact neighbor table in neighbors-summary.json; aperture throughput/color can change dilution. Capable rows: `{json.dumps(capable)}`. Previously verified difference-image receipt: `{json.dumps(diff[tic])}`. Duplicate schemas are one measurement. New per-pixel localization where required is in this folder's pixel-localization.json and nuisance variants; model residuals and event consistency matter more than uncalibrated formal chi2. No unresolved source ambiguity remains in the tested target-versus-neighbor comparisons.

## Archives and novelty

Fresh2026-10-30 VizieRIDIA60arcsec cones returned all9catalog sections: VSX, ASAS-SNII/366, SB9, WDS, Kostovtable2/3/4, IJspeert and Prsa. Raw response {tic}_idia.tsv; URLs/response hashes in idia-receipts.json. Parsed exact rows in catalogue-rows.json. Target-vs-neighbor IDs checked; Kostovtable2 is unvetted and not published EB classification. Cone row counts: `{json.dumps(A[tic]['catalog_counts'])}`. Current shared Gaia variability exact-source and ExoFOP checks: `{json.dumps(A[tic])}`. TIC349273287 ExoFOP was retried successfully; its receipt is retained.

No target prior EB entry established by these catalogs. SIMBAD exact Gaia match is SB*, already known spectroscopic binarity, not a complete bibliography. Name web searches returned no reliable target-specific EB result; search non-detection is weak and not an exhaustive literature clearance. Nearby VSX/IJspeert flags do not establish target novelty or prior EB status. Novelty status is limited prior-art coverage/no target EB match, separate from physical CONFIRMED.

## Prediction and next check

Using epochs after2026-10-30T20UTC (BTJD{now:.5f}), next primary-kind({pr}) center {pp:.6f}BTJD; next opposite-kind({other}) center {sp:.6f}BTJD. Repeated secondary uses its own fitted ephemeris; null opposite kind uses Gaia phase with sigma{tc['phase_error']*ep['P']:.4f}d before future-period uncertainty, so it may geometrically miss. Ephemeris errors are conditional and future checks should include O-C scatter.

{nexts[tic]}
'''
 (p/'REPORT.md').write_text(text,encoding='utf-8')
 res.append(dict(tic=tic,physical_verdict='CONFIRMED',full_review_completion='all applicable gates attempted/adjudicated; limitations retained',novelty_status='limited: no target prior EB match in fresh nine-catalog cones; not exhaustive bibliography',report=str(p/'REPORT.md'),next_check=nexts[tic]))
with (D/'RESULTS.csv').open('w',newline='') as h:w=csv.DictWriter(h,fieldnames=list(res[0]));w.writeheader();w.writerows(res)
json.dump(res,open(D/'RESULTS.json','w'),indent=2)
json.dump(res,open(F/'RESULTS.json','w'),indent=2)
print('Rendered',len(res),'explicit reviewed verdicts, next epoch',now)
