"""Compact per-star evidence reports; no source catalogue writes."""
import json,csv
import numpy as np
from astropy.time import Time
from pathlib import Path
ROOT=Path(__file__).parent
ids=['373138363','270181578','298645930','362610608','399501645']
verdicts={'373138363':'CONFIRMED','270181578':'CONFIRMED','298645930':'PLAUSIBLE','362610608':'CONFIRMED','399501645':'CONFIRMED'}
reasons={
'373138363':'Repeated primary and secondary eclipses, matching SB1 period/conjunction, independent reduction, target-centered prior image and no capable resolved G<15 neighbor establish an eclipsing target. Stellar dimensions remain model dependent.',
'270181578':'Repeated primary and secondary eclipses match the SB1 ephemeris, an independent pipeline recovers the deficits, the historical deficit is centered on target and no capable resolved G<15 neighbor exists. RUWE 7.688 and conditional dilution limit stellar characterization, not the supported eclipsing-target classification.',
'298645930':'The target aperture contains repeated sharp primary deficits on strong variable modulation. Secondary amplitude changes materially with template; timing and blind census are contaminated. A real 24.78 arcsec neighbor and inadequate calibrated PSF fit leave target attribution/model unresolved.',
'362610608':'Repeated primary and secondary eclipses agree with the Gaia orbit and an independent pipeline. Own s63 pixel-template fitting places the calibrated deficit 0.23 arcsec from target and beats the capable 13.11 arcsec neighbor by delta chi2 about14709. This resolves the historical crowding concern for the eclipse source; precise astrometry still has PSF systematics.',
'399501645':'Three primaries and two repeated eccentric-phase secondary events, Gaia timing, an independent reduction and target-centered historical deficit support an eclipsing target. The sole capable resolved neighbor is 51.87 arcsec away; existing image has peak on target and 3.62 arcsec deficit-target offset.'}
nextchecks={'373138363':'Obtain stellar-radius constraints and joint RV/eclipse characterization.', '270181578':'Characterize high-RUWE multiplicity with high-resolution imaging and better primary mass/radius; then joint light/RV fit.', '298645930':'Calibrate a realistic PRF/multi-source pixel model and separate periodic modulation before assessing secondary/heartbeat alternatives; do not classify neighbor ROT as target prior art.', '362610608':'Compare per-sector apertures to explain s99 depth decrease; improve PRF and stellar characterization.', '399501645':'Improve weak secondary shape and stellar-radius/dilution characterization.'}
offsets={'373138363':.39,'270181578':1.47,'298645930':2.68,'362610608':3.92,'399501645':3.62}
rows=[];now=Time('2026-10-30T12:00:00').jd-2457000
for tic in ids:
 p=ROOT/tic;r=json.load(open(p/'fit-results.json'));s=json.load(open(p/'secondary-fit.json'));o=json.load(open(p/'orbit-gates.json'));g=json.load(open(p/'geometry.json'));n=json.load(open(p/'gaia-nss.json'));ep=r['ephemeris'];shape=r['shape'];events=[x for x in r['events'] if x['status']=='fit'];depth=np.array([x['depth']*1000 for x in events]);derr=np.array([x['depth_error']*1000 for x in events]);ss=s['shape'];ph=s['profile_phase'];beta=[x['beta'] for x in events];secstats=s['statistic'];secerr=secstats['empirical_error']*1000
 census=r['census'];off=[x for x in census if min(abs((x['phase']+.5)%1-.5),abs((x['phase']-ph+.5)%1-.5))*ep['P']>shape['T14']]
 primstats={}
 for sec in sorted(set(x['sec'] for x in events)):
  d=[x['depth']*1000 for x in events if x['sec']==sec];primstats[sec]=round(float(np.median(d)),2)
 primarygaia=next(x for x in o['gaia_comparison'] if x['kind']=='A');dt=primarygaia['epoch389_offset'];ge=primarygaia['epoch389_gaia_error']
 # A phase measurement from timing fits at the reference epoch; fixed-shape
 # phase profile otherwise. Approximate e cos omega is first-order only.
 if s['ephemeris']:
  se=s['ephemeris'];tcsec=se['T0']+round((ep['Tref']-se['T0'])/se['P'])*se['P'];phase=((tcsec-ep['Tref'])/ep['P'])%1
  cycles=abs((ep['Tref']-se['Tref'])/se['P']);pe=np.hypot(se['Tref_error'],cycles*se['P_error'])/ep['P']
 else:phase=ph;pe=max(x['tc_error'] for x in s['events'] if x['status']=='fit')/ep['P']
 ecos=np.pi/2*(phase-.5);ecoserr=np.pi/2*pe
 # Next two epochs of each observed kind; predictions use primary P and
 # measured secondary phase, not unsupported independent secondary ephemeris.
 predictions={}
 for label,offset in [('primary',0),('secondary',phase)]:
  k=np.ceil((now-ep['T0'])/ep['P']-offset);predictions[label]=[round(ep['T0']+(k+j+offset)*ep['P'],5) for j in range(2)]
 physics=o['physics'];fm=physics[0]['f_mass'];m2=[x['m2_min'] for x in physics];centers=[x['central_T14_hours']['A'] for x in physics];maxfake=max(abs(x.get('background_fake_depth') or 0) for x in events)*1000
 text=f'''# TIC {tic}: full adversarial review, 2026-10-30

**Physical verdict: {verdicts[tic]}.** {reasons[tic]}

**Review completion:** all required gates were attempted and adjudicated below; unavailable services and inconclusive models are explicit limitations. This is not automatic confirmation of novelty. No catalogue/paper edits or commits.

## Deciding measurements

- Raw QLP SAP, QUALITY=0, no gap trimming: {len(events)} primary fits. Median trapezoid depth {np.median(depth):.2f} ppt (event range {min(depth):.2f} to {max(depth):.2f}; median formal/red-noise error {np.median(derr):.2f} ppt). Sector medians: {primstats}.
- Primary T14 {shape['T14']*24:.2f} h, conditional profile/grid range {shape['T14_range'][0]*24:.2f} to {shape['T14_range'][1]*24:.2f} h; T12 {shape['T14']*shape['fr']*24:.2f} h; T23 {shape['T14']*(1-2*shape['fr'])*24:.2f} h. These are trapezoid shape summaries, not a claim of true totality in grazing events.
- P = {ep['P']:.9f} +/- {ep['P_error']:.9f} d; Tref = {ep['Tref']:.6f} +/- {ep['Tref_error']:.6f} BTJD at cycle {ep['reference_cycle']}. T0 = {ep['T0']:.6f} BTJD. Chi2/dof {ep['chi2']:.2f}/{ep['dof']}; O-C rms {ep['oc_rms_minutes']:.2f} min. Per-event timing/errors/O-C are in fit-results.json.
- Conditional secondary: {secstats['n']} fitted windows, {secstats['n_individual_gt3sigma']} individual >3-sigma fits; depth {secstats['depth']*1000:.2f} +/- {secerr:.2f} ppt after between-event scatter; phase {phase:.6f} +/- {pe:.6f}. T14 {ss['T14']*24:.2f} h (range {ss['T14_range'][0]*24:.2f} to {ss['T14_range'][1]*24:.2f}), T12 {ss['T14']*ss['fr']*24:.2f} h, T23 {ss['T14']*(1-2*ss['fr'])*24:.2f} h. Weak/modulated shape uncertainty can exceed these conditional errors.
- Gaia SB1 P offset {o['period_delta_sigma']:+.2f} sigma. At BTJD389, primary minus conjunction A = {dt*24:+.2f} h versus Gaia sigma {ge*24:.2f} h. Full per-event conjunction comparison uses this source's covariance. Bit index127 and 15 correlations asserted against [ESA's SB1 ordering](https://gea.esac.esa.int/archive/documentation/GDR3/Gaia_archive/chap_datamodel/sec_dm_non--single_stars_tables/ssec_dm_nss_two_body_orbit.html); omega-Tp correlation {o['w_tp_corr']:+.6f}.
- First-order e cos(omega) = {ecos:+.4f} +/- {ecoserr:.4f}; for eccentric systems compare exact Gaia conjunction separation rather than treating this expansion as exact. Gaia e={float(n['eccentricity']):.4f} +/- {float(n['eccentricity_error']):.4f}, omega={float(n['arg_periastron']):.2f} +/- {float(n['arg_periastron_error']):.2f} degrees.

## Gate adjudication

| Gate | Status | Evidence and limits |
|---|---|---|
| Own archives/prior art | completed; no target prior EB match | ExoFOP HTTP200, TOI=0/CTOI=0; SIMBAD CFA exact Gaia ID is SB*. Shared ARI Gaia variability cache has no EB rows among70 sources. CDS and Harvard timed out, then IDIA succeeded: fresh 60arcsec cones in VSX, ASAS-SN, SB9, WDS, Kostov table2/3/4, IJspeert and Prsa. All nine table sections returned; no target EB prior-art match. Neighbor ROT/unvetted table2 matches are distinct sources. Raw responses and hashes in *_idia.tsv/idia-receipts.json. Identifier web searches have no pertinent hit, not proof of novelty. |
| Individual events/ephemerides | measured | fit-results.json, secondary-fit.json: integrated-exposure trapezoids, local quadratic baselines, fixed shared shape per kind, profile timing error with cadence/grid floors; primary residual bin-beta range {min(beta):.2f} to {max(beta):.2f}; ephemeris errors inflated when chi2/dof>1. Secondary ephemeris stored when >=3 strong events; two-event cases use primary P. |
| Flags/background/centroids | tested; conditional | Each fit records flagged core counts, OR bits, template centroids/errors, background regression and refitted depth. Maximum predicted fake-background primary depth {maxfake:.2f} ppt. Native background units never treated as flux. Sparse flags/gaps remain exclusions, not clean nulls. |
| Blind census | measured; coverage limited | {len(census)} candidate dip groups at max(4 robust per-cadence sigma,3ppt), including {len(off)} away from measured eclipses. Thresholded rolling median can detect intrinsic modulation/gap edges. For straightforward objects the lone off-phase group lacks sufficient clean baseline for event fitting (offphase-checks.json); no claim it is an eclipse. |
| Other eclipse/controls | measured; conditional | Gaia-fixed-phase tests and off-phase controls in orbit-gates.json; optimized secondary timing/shape separately in secondary-fit.json. Any quoted null upper limit is primary-shape/Gaia-phase conditional, not general exclusion. |
| Independent pipeline | passed for aperture events | TESS-SPOC SAP/PDCSAP retrieval and QUALITY=0 core estimates in indep_measure.txt; different reduction of same TESS data, not a separate observatory. Amplitude differences include dilution/sampling. |
| Neighbors/localization | {'inconclusive' if tic=='298645930' else 'supports target'} | Fresh ARI G<15 cone within60arcsec; required fractional dip estimates in neighbors_summary.csv are G-band proxies without aperture throughput. Historical difference-image deficit-target offset {offsets[tic]:.2f}arcsec, peak on target. See star-specific verdict and limitations. |
| Physics/e sin(omega) | modeled; conditional | RV mass function {fm:.5f} Msun; minimum m2 {min(m2):.3f} to {max(m2):.3f} Msun for listed M1 hypotheses. Predicted central primary T14 {min(centers):.2f} to {max(centers):.2f} h versus observed {shape['T14']*24:.2f} h, compatible with a noncentral chord. Numerical limb-darkened two-disk fits in geometry.json explore both shapes with fixed TIC dimensions, free depth scales and physical scale<=1; degeneracies prevent a robust independent e sin(omega) measurement. Do not interpret the coarse-grid profile interval as a calibrated orbital confidence interval. |

Next predictions (BTJD, from 2026-10-30 noon): primary {predictions['primary']}; secondary {predictions['secondary']}. Timing extrapolations inherit ephemeris and secondary-shape systematics; no precise future uncertainty for the modulated system.

**Next deciding check:** {nextchecks[tic]}

Provenance: ../downloads.json and ../receipts.json; shared-full-review Gaia receipts; independent CAOM responses and indep_sha256.txt. Scripts fit_batch.py/orbit_gates.py/secondary_fit.py/geometry.py reproduce numeric results. Optional Terra personal note was not supplied; its scientific contribution is preserved verbatim in INDEPENDENT-NOTE.md. Lead: Sol batch A.
'''
 if tic=='362610608':text+='\nOwn pixel362.py uses the existing hashed s63 TESScut and three eclipse templates. Target fixed-source chi2=4556 versus nearest capable neighbor19265, free best0.23arcsec from calibrated target. Gaussian PSF shape is approximate and formal chi2 ignores PSF covariance; relative source discrimination is strong, precise centroid uncertainty is not claimed.\n'
 if tic=='298645930':text+='\nSpecific caution: source2123135139098776320 is a real G13.62 neighbor24.78arcsec away; its ROT classification is not the target2123135139098776448. Pixel298.py reused a hashed existing s41 cube: target beats neighbor by delta chi2 about22825, but free centroid~10arcsec and WCS shift at grid boundary make precise localization unreliable. Baseline sensitivity, broad secondary shape and large off-phase census preclude confirmation. Tide298.py compares equilibrium-tide plus five orbital harmonics per sector against the same plus a narrow primary: delta BIC17274 favors the eclipse component, with primary depths28.4 to30.8ppt. Correlations prohibit formal FAP; secondary and calibrated localization remain unresolved.\n'
 if tic=='270181578':text+='\nSpecific caution: no other G<15 resolved neighbor within60arcsec, but this does not exclude unresolved light. RUWE7.688 and conditional geometry primary scale~0.45 motivate multiplicity/dilution follow-up rather than a unique binary geometry.\n'
 # ASCII-safe text prevents PowerShell codepage corruption in artifacts.
 (p/'REPORT.md').write_text(text,encoding='utf-8')
 rows.append(dict(tic=tic,physical_verdict=verdicts[tic],novelty_status='limited: fresh nine-catalog IDIA cones: no target prior EB match; nearby unvetted flags separated',full_review_completion='all required gates attempted/adjudicated; limitations retained',primary_events=len(events),secondary_fitted_windows=secstats['n'],period_d=ep['P'],period_error_d=ep['P_error'],primary_median_depth_ppt=float(np.median(depth)),secondary_depth_ppt=secstats['depth']*1000,secondary_depth_error_ppt=secerr,primary_T14_h=shape['T14']*24,oc_rms_min=ep['oc_rms_minutes'],report=str(p/'REPORT.md'),next_check=nextchecks[tic]))
json.dump(rows,open(ROOT/'RESULTS.json','w'),indent=2)
with open(ROOT/'RESULTS.csv','w',newline='') as out:
 w=csv.DictWriter(out,list(rows[0]));w.writeheader();w.writerows(rows)
print([(x['tic'],x['physical_verdict']) for x in rows])
