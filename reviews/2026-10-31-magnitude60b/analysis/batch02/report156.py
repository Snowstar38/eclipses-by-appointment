import json,csv
from pathlib import Path
B=Path(__file__).parent;t='156985493';D=B/t;m=json.load(open(D/'measurements.json'));g=json.load(open(B/'gaia-geometry.json'))[t]
lim='Narrow eclipses at30minute cadence in sector22 have only3-4 trough samples. Mixed quadratic/Gaussian timing model and cadence floors are descriptive allowances, not total uncertainty. Sector49 cycle75 and sector22 half-period midpoint are flagged/gaps, not clean nulls; other sector49 half-period windows have usable flat samples. Same photons, aperture dilution and uncalibrated centroid uncertainty remain. Approximate1.2h observed FWHM differs from modeled central duration; grazing geometry possible, no detailed binary fit.'
table='\n'.join(f"| {e['sector']} | {e['cycle']} | {e['mid_btjd']:.8f} | {e['timing_error_days']:.8f} | {e['depth_ppt']:.3f} | {e['method']} |" for e in m['events'])
s=f'''# TIC156985493: CONFIRMED

Full bounded review: COMPLETE. Physical classification is separate from central catalogue novelty. Root scientific acceptance is required before integration.

1. **Raw repeats: pass.** Two actual unflagged narrow sector22 SAP eclipses and two sector49 eclipses are measured. The generic25-point fit gate missed short events at30minute cadence; its empty result remains pipeline_measurements.json. Independent helper examined actual SAP samples and plots, measuring quadratic trough centers from3-4 samples in sector22 and free Gaussian plus linear baseline centers in sector49. Historical predicted epochs drifted and were not used as measured timings. See helper/independent_raw.png and helper/156-alias-windows.png.
2. **Measured same-kind timing and aliases: pass.** Four measured centers at cycles0,1,74,76 give P={m['period_days']:.10f} +/-{m['period_error_days']:.10f}d and selected-eclipse epoch BTJD{m['primary_epoch_btjd']:.8f}. Kind: {m['epoch_kind']}. Sector22 adjacent spacing9.94631d and sector49 two-cycle spacing19.89509d test recurrence across the gap. Half-period alternatives at BTJD2649.223 and2659.171 have15/17 and14/17 unflagged cadences and minima0.99764/0.99915 of baseline, excluding comparable12ppt intermediate eclipses. A separate shallower secondary remains possible. This is a bounded alias check, not exhaustive all-period search. Error meaning: {m['error_meaning']}
3. **Target attribution: pass at TESS resolution.** Newly fetched sector22 TESScut difference has positive-deficit5x5 centroid(7.7458,7.7067) vs WCS target(7.797,7.723), separation0.054pixel. No calibrated centroid uncertainty. Successful current MAST TIC60arcsec cone finds two Gaia-linked neighbors at39.92/54.44arcsec, G20.231/20.323. Producing11ppt target loss would require approximately26/28 times their entire Gaia G flux, so neither is capable under that approximate color/aperture brightness proxy. This is not proof against uncatalogued unresolved companions. Receipt helper/156-tic-cone.json; cutout image helper/156-cutout-difference.png.
4. **Alternative reduction: pass.** Independently extracted TESScut pixel-aperture flux reproduces both sector22 dips. Event1 1x1/3x3/5x5 average depths5.93/6.66/4.95ppt; event2 9.39/5.42/2.93ppt. Apertures center on brightest pixel(8,8), without background subtraction, in-event +/-0.027d and out-of-event0.065-0.17d. These smeared average depths differ from QLP trough/model depths, as expected from cadence, extraction and dilution. Same TESS photons, not independent observations. Source FITS, script and hash in helper/156-independent.json and helper/tesscut156.
5. **Full NSS Gaia geometry: pass with limitations.** DR3{g['gaia_source_id']}; GaiaP={g['period_days']:.10f}+/-{g['period_error_days']:.10f}d, e={g['eccentricity']:.6f}, omega={g['omega_deg']:.4f}deg. Closest edge-on conjunction offset{g['closest']['offset_days']:.6f}d ({g['closest']['offset_phase']:.6f}phase), full SB1 covariance linear allowance{g['closest']['gaia_covariance_linear_error_days']:.6f}d at measured epoch. Mass function{g['mass_function_solar']:.6f}solar masses, assumed primary{g['assumed_m1_solar']:.3f}, minimum companion{g['minimum_m2_solar']:.3f}. Approximate central duration{g['central_duration_hours_approx']:.2f}h vs observed approximate sector22 cutout FWHM1.2h allows grazing/noncentral geometry. This is descriptive edge-on/minimum-mass comparison, not detailed binary modeling; no arbitrary sigma veto. Full inputs/covariance assumptions in gaia-geometry.json.

Queue-preparation QLP availability product list (targets-selected.json, hashed in helper/156-checks.json) contains sectors22 and49, both investigated. This reuses the campaign product list rather than asserting an independent fresh helper query. Sector49 previously flagged predicted windows were not clean nulls; shifted actual eclipse windows reveal repeats. No replacement or denominator exclusion.

**Limitations:** {lim}

**Next check:** Optional short-cadence resolved photometry and revised spectroscopy for sharper eclipse morphology/geometry; no missing bounded admission check.

Catalogue novelty is supplied separately by ../../shared-catalogues/coverage-matrix.csv. This physical report does not claim exhaustive literature priority.

| Sector | Cycle | Measured midpoint BTJD | Timing input d | Depth ppt | Method |
|---|---|---|---|---|---|
{table}

Evidence: measurements.json; pipeline_measurements.json; ../helper/156-independent.json; ../helper/156-independent.py; ../helper/156-sector49.py; ../helper/156-alias-windows.png; ../helper/156-cutout-difference.png; ../helper/156-tic-cone.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Shared QLP source hashes in ../download-receipts.json. Public identity boundary respected.
'''
(D/'REPORT.md').write_text(s,encoding='utf-8')
rows=list(csv.DictReader(open(B/'RESULTS.csv',encoding='utf-8')));rows=[r for r in rows if r['tic']!=t];rows.append(dict(tic=t,physical_verdict='CONFIRMED',full_review_completion='COMPLETE',period_days=m['period_days'],period_error_days=m['period_error_days'],primary_epoch_btjd=m['primary_epoch_btjd'],depth_ppt=m['depth_ppt'],limitations=lim,next_check='Optional short-cadence resolved photometry and revised spectroscopy',source_report=str(B/'helper/156-independent.json'),report=str(D/'REPORT.md')))
order={r['tic']:i for i,r in enumerate(csv.DictReader(open(B/'queue.csv')))};rows.sort(key=lambda r:order[r['tic']])
with open(B/'RESULTS.csv','w',newline='',encoding='utf-8') as f:w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
