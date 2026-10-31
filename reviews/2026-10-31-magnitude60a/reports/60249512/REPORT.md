# TIC 60249512: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 10 distinct eclipse events in selected sectors[7, 61, 88]. The raw-event plot and numeric raw-windows.csv were inspected. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 6 same-kind midtimes give P=15.3007645492 ±0.0000224480d, reference eclipse epoch BTJD1497.6542271, kind: Selected conjunction, even half-period cycles; primary/secondary depth identity ambiguous. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S88 deficit peak[7, 8] vs target pixel[7, 8]; deficit-target separation1.783arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.113. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths273.940/271.050/261.562ppt, with 4 stacked events. QLP selected-kind fitted median309.258ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR35512369488219087744, P=15.2997416314±0.0023368048d, e=0.023463, omega=147.8744deg. Closest edge-on conjunction offset0.070489d (0.004607phase), full-SB1-covariance linear propagated Gaia uncertainty0.159401d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.003161d (photometric period projection allowance0.001616d). The approximate central duration10.68h vs observed median8.42h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Similar eclipse depths do not establish half orbital period. Consecutive sector88 spacings7.682814/7.617839/7.682757d alternate; same-kind spacings15.300653/15.300596d support full orbital period. Even half-period cycles define selected-conjunction epoch; deeper-primary identity is not claimed. Historical cutout mixes eclipse kinds.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 7 | 0 | 1497.6546055 | 0.010417 | 295.120 | usable; same-kind selection applies |
| 7 | 1 | 1505.2723818 | 0.010417 | 300.513 | usable; same-kind selection applies |
| 7 | 2 | 1512.9545493 | 0.010417 | 294.334 | usable; same-kind selection applies |
| 61 | 192 | 2966.5277090 | 0.001157 | 310.399 | usable; same-kind selection applies |
| 61 | 193 | 2974.1458765 | 0.001157 | 312.867 | usable; same-kind selection applies |
| 61 | 194 | 2981.8283020 | 0.001157 | 309.391 | usable; same-kind selection applies |
| 88 | 287 | 3693.2815932 | 0.001157 | 314.161 | usable; same-kind selection applies |
| 88 | 288 | 3700.9644077 | 0.001157 | 310.212 | usable; same-kind selection applies |
| 88 | 289 | 3708.5822465 | 0.001157 | 314.693 | usable; same-kind selection applies |
| 88 | 290 | 3716.2650033 | 0.001157 | 309.125 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s88.json, historical/diff_s88.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R223. [Deciding evidence](../../evidence/60249512/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
