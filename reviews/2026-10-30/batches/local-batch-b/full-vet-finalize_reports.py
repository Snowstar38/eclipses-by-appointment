"""Lead adjudication and reproducible compact reports. No source catalogue writes."""
import pathlib,json,csv,numpy as np,math,hashlib,datetime
R=pathlib.Path(__file__).parent; shared=R.parent.parent/'shared-full-review';sel=json.loads((R.parent/'selected.json').read_text());phys=json.loads((R/'physics-initial.json').read_text());vsx={x['tic']:x for x in json.loads((shared/'vsx70-receipts.json').read_text())}
def load(t,s):return json.loads((R/f'{t}_{s}.json').read_text())
def med(a,k):return float(np.median([x[k] for x in a]))
rows=[]
for tic,t in sel['targets'].items():
 m=load(tic,'measurements'); ep=m['ephemeris'];a=[x for x in m['events'] if x['coverage_ok'] and x['depth']/x['depth_error']>4];st=load(tic,'secondary_timing');se=load(tic,'secondary_ephemeris');ss=load(tic,'secondary_phase_sensitivity');mc=load(tic,'gaia_mc');ind=load(tic,'independent_comparison');census=load(tic,'blind_census');cov=load(tic,'coverage_sensitivity');ld=load(tic,'limbdark_refined' if tic=='451493289' else 'limbdark_grid');p=phys[tic]
 sb=list(csv.DictReader((R/f'{tic}_simbad_harvard.txt').open()));name=min(sb,key=lambda x:(float(x['ra'])-t['ra'])**2+(float(x['dec'])-t['dec'])**2)['main_id']
 def ranges(k):return f'{min(x[k] for x in ind)*1000:.1f} to {max(x[k] for x in ind)*1000:.1f}'
 frac=ss['weighted_phase'];ferr=ss['conservative_phase_uncertainty'];ec=math.pi/2*(frac-.5);ecoserr=math.pi/2*ferr
 best=ld['best'];chi=best['chi2'];notes={
 '295945076':'The secondary is at phase 0.52192, not the Gaia median 0.53683. The difference is about 1.7 sigma after the heuristic timing envelope; the Gaia orbit is not contradicted. Sector 87 has baseline/depth shifts. The grazing solution has no securely measured totality.',
 '372376841':'The independent SAP/PDCSAP depth difference is substantial. The 16-arcsec neighbour could mimic the depth in a large aperture, but the new pixel test selects the target. A separate known EB 58 arcsec away has period 1.78258 d and is too faint to explain the depth under the G-band proxy.',
 '416525506':'S55 cycle 232 is background-sensitive: raw 32.55 versus background-regressed 37.23 ppt. Excluding it changes P by only 0.0048 seconds. It is retained as an affected event, not pristine evidence.',
 '451493289':'The joint model fits poorly near the catalog dimensions. A refined illustrative fit needs R1 about 2.52 Rsun, 0.75 times TIC 3.355 +/- 0.144 Rsun. This is a large unresolved stellar-dimension/model tension, not a measured correction to the catalogue. S93/S101 have extreme flagged excursions and S100/S102 depth/baseline changes.',
 '348737250':'At the catalog radius the simple R2=M2min relation underpredicts depth. Allowing radius/model freedom provides an illustrative binary geometry. The nearby 33-arcsec source would need about a 96% G-band dip under equal-throughput assumptions; prior target-centered difference imaging supports attribution.'}[tic]
 if tic in ['295945076','372376841']:
  px=load(tic,'pixel_template');local=f"Fresh TESScut template fitting in sector {px['sector']} uses two events. The target is preferred to all listed neighbours; free and split-event PSF centroids lie within about 0.07 pixel of the catalogue position. These are unweighted Gaussian-PSF/WCS diagnostics, not calibrated localization sigma."
 else:local='The valid prior difference-image receipt is reused, with on-target peak and small deficit-to-target offset (0.87 arcsec for 416525506, 1.63 for 451493289, 2.50 for 348737250). No new pixel cube was needed; this is explicitly prior attribution evidence.'
 nbg=max(abs(x['background_fractional_change']) for x in a);depth=med(a,'depth')*1000;sdepth=med(st['events'],'depth')*1000
 secp=se['secondary_P'];sperr=math.sqrt(se['covariance'][1][1]);sP=math.sqrt(ep['covariance'][1][1]);sT=math.sqrt(ep['covariance'][0][0]);secrms=float(np.std(se['oc_d']))*1440
 primarynext=', '.join(f'{x:.5f}' for x in se['next_primary_BTJD'][:3]);secondarynext=', '.join(f'{x:.5f}' for x in se['next_secondary_BTJD'][:3]);secbound=ferr*ep['P']*1440
 off=sum(x.get('classification')=='off_ephemeris' for x in census['peaks']);gaia=mc['primary_comparisons'][0]
 text=f'''# TIC {tic} ({name}): full attempted and adjudicated review

Verdict: CONFIRMED physical eclipsing target/system associated with the Gaia SB1. Repeated primary and secondary eclipses, orbital timing, independent photometry and localization support this classification. Exact component properties remain uncertain; this is not a catalogue edit or publication action.

## Deciding light-curve evidence

{len(a)} primary event fits pass the stated basic fit/coverage screen; the stricter cadence/gap screen retains {cov['strict_n']}. Median fitted primary depth is {depth:.2f} ppt, with median conditional per-event depth error {med(a,'depth_error')*1000:.2f} ppt. Median T14/T12/T23 are {med(a,'T14_d')*24:.2f}/{med(a,'T12_d')*24:.2f}/{med(a,'T23_d')*24:.2f} hours. These are fitted trapezoid descriptors; partial eclipses do not imply physical totality. Individual profile ranges, counts and gaps are in {tic}_measurements.json. Shape grids and baseline systematics limit errors, especially at profile boundaries.

{len(st['events'])} secondary timing fits give median depth {sdepth:.2f} ppt and phase {frac:.6f} +/- {ferr:.5f} cycles. The latter is a conservative heuristic envelope from phase-grid resolution, width alternatives and leave-one-sector scatter, not a calibrated confidence interval. Fixed-phase/alternate-width controls and covered windows are preserved in secondary JSONs. Approximate small-e e*cos(omega) = {ec:+.4f} +/- {ecoserr:.4f}; no trapezoid duration-ratio estimate of e*sin(omega) is claimed.

## Timing and Gaia

Primary T0 = {ep['T0']:.8f} +/- {sT:.8f} BTJD, P = {ep['P']:.9f} +/- {sP:.9f} d. Primary O-C rms {ep['oc_rms_d']*1440:.2f} min. Covariance is scaled by max(1, chi-square/dof); stricter-mask P = {cov['P']:.9f} d. Secondary P = {secp:.9f} +/- {sperr:.9f} d, O-C rms {secrms:.2f} min; primary-secondary difference {se['period_difference_d']*86400:+.2f} +/- {se['period_difference_formal_error_d']*86400:.2f} seconds/cycle. Covariances and all O-C values remain in JSON.

The Gaia comparison uses this source's full SB1 row, bit_index 127, its own 15-element correlation vector and the documented six-parameter order. The primary is {gaia['A_offset_sigma']:+.2f} sigma from conjunction A near the Gaia epoch; photometric-Gaia period difference is {mc['period_difference_sigma']:+.2f} sigma. Per-sector A/B timing comparisons are saved. Physical-e rejection fraction {mc['physical_e_rejection_fraction']:.1%} means the Gaussian orbit approximation is conditional and small-e priors remain soft.

## Independence, systematics and attribution

TESS-SPOC sector {ind[0]['sector']} independently recovers time-aligned dips: SAP {ranges('SAP_FLUX')} ppt and PDCSAP {ranges('PDCSAP_FLUX')} ppt. Their difference is a dilution/detrending uncertainty, not evidence of absent eclipses. Raw QLP SAP with QUALITY=0 is the primary source; no post-gap trim was used. Flags, raw centroids, native-unit background excursions and gap coverage were examined. Background regression changes primary depths by at most {nbg:.1%}; this is a unit-free sensitivity check and does not convert SAP_BKG to fractional stellar flux. {notes}

The blind coarse-box census retains {len(census['peaks'])} peaks, {sum(x['gap_flag'] for x in census['peaks'])} gap-flagged, and {off} classified off the two eclipse ephemerides. Its max(3 ppt, three flank-MAD) threshold is not a significance calibration or exhaustive shallow-event census. {local} Fresh 60-arcsec Gaia neighbours and G-proxy dilution requirements are in neighbours-dilution.csv; aperture throughput, colour and unresolved companions remain limitations.

## Physics and archives

RV mass function {p['mass_function_msun']:.4f} Msun; using catalog M1={p['M1_catalogue']:.3f}, edge-on M2min={p['M2_min_msun']:.3f} Msun and a={p['a_Rsun']:.2f} Rsun. A shared limb-darkened two-disc model was actually tested against both eclipse shapes, with finite-exposure sampling, radius/impact/e*sin(omega)/light-ratio freedom. Illustrative best k={best['radius_ratio_k']:.3f}, b_A={best['impact_parameter_A']:.2f}, R1 scale={best['R1_scale']:.2f}, R2={best['R2_solar']:.3f} Rsun; diagnostic score {chi:.1f} for {ld['number_bins']} bins. Correlated bins, fixed limb darkening, local trends, no third light and coarse bounds prevent precision physical inference. This is a plausible geometry family, not independently measured masses/radii.

Fresh SIMBAD identifies the target SB*. ExoFOP has no TOI/CTOI. Successful IDIA cones find no target entry in ASAS-SN, SB9, WDS, Prsa, IJspeert or vetted Kostov table3/4. Kostov table2 is unvetted and is not prior confirmation; 372376841 appears there. Root's successful 60-arcsec VSX sweep returns {len(vsx[tic]['rows'])} rows here: no eclipsing entry at this target. The 372 cone's known EB is the different 58-arcsec neighbour. Gaia vari_eclipsing_binary has no target row in the successful shared query. Exact TIC/main-name web searches found no relevant prior eclipsing record; 416's KIC11418931 is absent from the Kepler EB catalogue. This supports novelty only within the queried sources. Initial failed CDS queries were superseded by working mirrors, not treated as null results.

## Next eclipses and follow-up

After 2026-10-30: primary BTJD {primarynext}; secondary {secondarynext}. Linear-covariance prediction errors can be optimistic; secondary scheduling allowance is at least about {secbound:.0f} minutes from the heuristic phase envelope, plus accumulated ephemeris uncertainty. Primary covariance propagation and sampling sensitivity are retained in the ephemeris files. Follow-up priorities are robust component radii/light ratios, baseline-sensitive events and calibrated multi-sector localization; they do not negate the repeated attributed eclipses.

Provenance: parent acquisition.csv/selected.json/prior-receipts.txt; full-vet scripts and per-target JSONs; successful archive response hashes; shared Gaia/VSX receipts. Sol lead reviewed code and compact evidence plus exactly two new pixel maps; Terra performed bulk extraction/model attempts. Original catalogue and work directories remain unchanged.
'''
 (R/f'{tic}_REPORT.md').write_text(text,encoding='ascii')
 rows.append(dict(tic=tic,verdict='CONFIRMED',review_status='full attempted and adjudicated; bounded methods and residual limitations explicit',primary_events=len(a),strict_primary_events=cov['strict_n'],secondary_events=len(st['events']),P_d=ep['P'],P_error_d=sP,primary_depth_ppt=round(depth,3),secondary_depth_ppt=round(sdepth,3),secondary_phase=frac,secondary_phase_heuristic_error=ferr,Gaia_A_offset_sigma=gaia['A_offset_sigma'],independent_pipeline='TESS-SPOC SAP+PDCSAP',attribution='fresh TESScut target template+split/freePSF' if tic in ['295945076','372376841'] else 'valid prior target-centered diffimg plus fresh neighbour/dilution check',physical_gate='bounded limb-darkened joint family; catalog-dimension tension explicit' if tic=='451493289' else 'bounded limb-darkened joint family; parameters not precise',residual_limitations='coarse census; approximate red-noise/profile errors; PSF/WCS model; stellar dimensions/light/dilution degenerate',next_primary_BTJD=se['next_primary_BTJD'][0],next_secondary_BTJD=se['next_secondary_BTJD'][0],physical_verdict='CONFIRMED',full_review_completion='full_attempted_and_adjudicated',novelty_status='no prior target eclipsing classification in successfully queried vetted sources; unvetted flags separate',next_check={'451493289':'Resolve catalog radius versus joint eclipse geometry; sector baseline variation','416525506':'Inspect S55 cycle232 background-sensitive event; refine component geometry','295945076':'Refine secondary timing and Gaia small-e orbit; multi-sector calibrated pixels','372376841':'Resolve SAP/PDCSAP dilution difference and component radii','348737250':'Refine component radius/light ratio and calibrated localization'}[tic],report=str(R/f'{tic}_REPORT.md')))
with (R/'RESULTS.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
assert len(rows)==5
manifest=[]
for f in (R/'data').glob('*'):
 if f.is_file():manifest.append(dict(file=f.name,bytes=f.stat().st_size,sha256=hashlib.sha256(f.read_bytes()).hexdigest()))
(R/'data-hashes.json').write_text(json.dumps(manifest,indent=2))
print([(x['tic'],x['verdict'],len(pathlib.Path(x['report']).read_text().split())) for x in rows])
