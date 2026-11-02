from pathlib import Path
import csv,json,numpy as np
B=Path(__file__).parent;geo=json.load(open(B/'gaia-geometry.json'));sec=json.load(open(B/'secondary-phases.json'));rows=[]
notes={
'370138999':'Shallow repeated narrow raw eclipses; compact deficit near target. Three capable neighbors at31-59 arcsec are spatially separated from the deficit core. No secure secondary.',
'176048490':'Four deep, flat-bottomed raw eclipses and an unequal secondary near phase0.3683 support eccentric binary morphology. The capable neighbor at56.6 arcsec is separated from the deficit.',
'76177367':'Six narrow raw eclipses and another eclipse near phase0.5930; two capable neighbors at35 and57 arcsec lie away from the deficit. Very bright field light shifts the full-light centroid and dilutes aperture photometry; the compact lost flux remains near target. No deeper-primary assignment is claimed; baseline/extraction differences limit the depth comparison.',
'101259338':'Sixteen repeated narrow eclipses and an unequal secondary near0.5004. No capable Gaia neighbor within60 arcsec; compact lost flux favors target.',
'157367278':'Sixteen deep flat-bottomed eclipses, shallower secondary near0.5000. No capable Gaia neighbor within60 arcsec. Bright displaced field light shifts the light centroid; target-centered deficit remains distinct.',
'264485594':'Eight repeated shallow narrow raw eclipses. Target-centered compact deficit; no capable Gaia neighbor within60 arcsec. No secure secondary; baseline variability limits null claims.',
'202442866':'Nine deep repeated raw eclipses plus a broad shallower secondary near0.4988. Target-centered deficit; no capable Gaia neighbor within60 arcsec.',
'297956126':'Five measured deep eclipses after adding S66 QLP. Consecutive same-kind S66 eclipses resolve the long-baseline cycle-count ambiguity. Unequal eccentric secondary near0.7244; three capable neighbors are spatially separated from compact deficit.',
'216024097':'Nine repeated flat-bottomed raw eclipses and shallower secondary near0.5051. Three capable neighbors at38-56 arcsec are displaced from target deficit core.',
'380616368':'Six deep repeated raw eclipses and unequal secondary near0.5185 are real. A capable Gaia neighbor only13.06 arcsec away overlaps the TESS footprint; target ownership remains unresolved. Five farther capable neighbors were also inspected.'}
for q in csv.DictReader(open(B/'queue.csv')):
 tic=q['tic'];out=B/tic;m=json.load(open(out/'measurements.json'));d=json.load(open(out/'fresh-pixels/diff_fresh.json'));g=geo[tic];v='PROBABLE' if tic=='380616368' else 'CONFIRMED';s=sec[tic];ev=[x for x in m['events'] if x.get('timing_usable')];nbs=[x for x in d['neighbours_60'] if x['possible']]
 nb='\n'.join(f"| {n['source_id']} | {n['sep']:.3f} | {n['G']:.3f} | {n['depth_needed']:.4f} | {n['px']} | {n['frac_loss_at_pixel']} |" for n in nbs) or '| None | | | | | |'
 times='\n'.join(f"| {e['sector']} | {e['cycle']} | {e['mid_btjd']:.8f} | {e['formal_timing_error_days']:.8g} | {e['timing_error_days']:.8g} | {e['depth_ppt']:.3f} |" for e in ev)
 prov='Same-sector QLP and cutout extraction share TESS photons and test processing robustness.' if d['sector'] in [x['sector'] for x in m['sources']] else 'Cutout sector is a distinct observing occasion on the same TESS instrument relative to retained QLP sectors. This alternative reduction shares the FFI photons of that sector; no same-sector QLP comparison claimed.'
 secondary=f"{s['visual_status']}. "+(f"Depth is the realized center deficit of the fitted shape, with its amplitude parameter retained separately in the JSON. Measured pooled secondary phase={s['phase']:.7f}, formal phase covariance error={s['formal_phase_error']:.5g}; depth={s['depth_ppt']:.3f} ppt. {s['error_meaning']} Search-guide provenance: {s['search_guess_provenance']}." if s['secure_secondary'] else 'A fitted low-amplitude pooled model is not evidence of a secondary; flagged and missing coverage are not clean nulls.')
 nextcheck='Resolved eclipse photometry or multi-source PRF localization for target and13.06-arcsec neighbor.' if v=='PROBABLE' else 'Optional resolved photometry and spectroscopy to refine physical parameters.'
 text=f'''# TIC {tic}: {v}

Full bounded physical review: **COMPLETE**. {notes[tic]}

Raw morphology was inspected in raw-events.png and phase-review.png, including P and2P parity views. {len(ev)} free-center trapezoid timings survive finite, identifiable center-covariance checks. Quality-zero raw QLP SAP_FLUX was used; predictions only guide fitting windows. This is representative available evidence, not an all-event/all-sector census.

Measured same-kind eclipse ephemeris: P={m['period_days']:.11f} +/- {m['period_error_days']:.11f} d; reference BTJD={m['primary_epoch_btjd']:.8f}. Epoch kind: {m['epoch_kind']}. {m['error_meaning']} Reduced timing chi-square={m['reduced_chi_square']}; zero degrees of freedom would be null. All selected timings follow the selected repeating eclipse family. The epoch is conventional and does not assert that this is the deeper primary; pooled alternate-event depths may differ with baseline/extraction. Within-sector cycle recurrence and parity depths are in ../alias-audit.json. Unequal secondary depths exclude mixing eclipse kinds into P/2; the P/2 and2P raw views were inspected. No exhaustive blind alias search is asserted.

{secondary}

Fresh difference image: sector{d['sector']}, {d['n_events']} complete core/sideband events. Target pixel={d['target_px']}; deficit centroid={d['deficit_centroid']}; deficit-target distance={np.hypot(*d['deficit_minus_target_px']):.4f} pixel. Deficit-light offset={d['deficit_minus_light_arcsec']:.3f} arcsec is a descriptive field-light displacement, not an arbitrary veto. Fractional PSF-model residual={d['psf_fit_frac_resid']:.4f} is not a calibrated localization uncertainty. Every flux-capable Gaia source in the60-arcsec list was inspected against the image. Attribution conclusion: {notes[tic]}

| Capable Gaia source | Separation arcsec | G | Intrinsic required eclipse proxy | Pixel coordinate | Diluted loss at pixel |
|---|---:|---:|---:|---|---:|
{nb}

The pairwise G-band required intrinsic loss is an approximate brightness screen, with passband, aperture and blend assumptions. It cannot be directly compared to the diluted fractional loss in a pixel. Noncapable neighbors and all coordinates remain in fresh-pixels/diff_fresh.json and gaia.json. TESS resolution does not exclude unlisted unresolved companions.

Alternative reduction: fresh background-subtracted TESScut1x1/3x3/5x5 target apertures have depths {d['depth_ap1']*1000:.3f}/{d['depth_ap3']*1000:.3f}/{d['depth_ap5']*1000:.3f} ppt versus fitted raw QLP median{m['depth_ppt']:.3f} ppt. Individual cutout event depths are retained in the pixel JSON. {prov} Distinct sectors are observing occasions on one instrument. Aperture/depth differences reflect dilution, background and extraction response; no intrinsic depth inferred.

Gaia DR3 source{g['gaia_source_id']}: P={g['period_days']:.8f} +/-{g['period_error_days']:.8f} d, e={g['eccentricity']:.6f}, omega={g['omega_deg']:.5f} degrees, periastron BTJD={g['t_periastron_btjd']:.7f}. Closest edge-on conjunction offset={g['closest']['offset_days']:.6f} d ({g['closest']['offset_phase']:.6f} phase), source-specific full-covariance linear uncertainty={g['closest']['gaia_covariance_linear_error_days']:.6f} d. Full correlation ordering P,gamma,K,e,omega,Tp, selected indices0,3,4,5. This linear approximation is descriptive, not a sigma veto. Both conjunctions and near-reference projection are retained in ../gaia-geometry.json. Mass function={g['mass_function_solar']:.6g} solar masses, assumed M1={g['assumed_m1_solar']:.5g}, minimum M2={g['minimum_m2_solar']:.5g}; approximate central duration={g['central_duration_hours_approx']:.3f} h versus observed{g['observed_duration_hours']:.3f} h. TIC radius and main-sequence companion scaling are assumptions, not a geometry fit; impact parameter and stellar evolution affect duration. Agreement cannot establish ownership among unresolved sources.

| Sector | Same-kind cycle | Measured midpoint BTJD | Formal center error d | Input error d | Depth ppt |
|---|---:|---:|---:|---:|---:|
{times}

Next check: {nextcheck}

Catalogue status is separate from physical verdict; shared-catalogues/coverage-matrix.csv retains the seven scoped groups. Known recoveries are not new additions; no exhaustive priority claim. Sources and identity are checked in ../identity-check.json and ../source-hashes.json. Numeric artifacts, original receipts and outputs are frozen in ../SHA256SUMS.json; independent helper review is ../helper-audit.md.
'''
 (out/'REPORT.md').write_text(text,encoding='utf8');rows.append(dict(tic=tic,physical_verdict=v,full_review_completion='COMPLETE',period_days=m['period_days'],period_error_days=m['period_error_days'],primary_epoch_btjd=m['primary_epoch_btjd'],depth_ppt=m['depth_ppt'],limitations=notes[tic],next_check=nextcheck,source_report=str(out/'measurements.json'),report=str(out/'REPORT.md')))
with open(B/'RESULTS.csv','w',newline='',encoding='utf8') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
