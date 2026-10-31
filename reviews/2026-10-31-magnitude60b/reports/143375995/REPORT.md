# TIC 143375995: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 9 distinct eclipse events in selected sectors[7, 34, 88]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 9 same-kind midtimes give P=8.3596843935 ±0.0000123196d, reference eclipse epoch BTJD1492.9984843, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Unreliable fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S88 deficit peak[7, 8] vs target pixel[7, 8]; deficit-target separation1.472arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.856. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths107.960/102.672/81.871ppt, with 4 stacked events. Historical event coordinates guide these stacks and are not newly measured midtimes. QLP selected-kind fitted median113.726ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR35700400927358983168, P=8.3599586040±0.0006591686d, e=0.210170, omega=8.4067deg. Closest edge-on conjunction offset0.060141d (0.007194phase), full-SB1-covariance linear propagated Gaia uncertainty0.114884d at the measured epoch. Near-Gaia-reference projected eclipse offset0.096337d (photometric period projection allowance0.001626d). The approximate central duration8.53h vs observed median6.22h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Deep isolated eclipses recur across three sectors. Aperture depths vary with dilution; no capable catalogued neighbor within60arcsec under approximate Gaia G brightness test. PSF-scaled residual0.856 warns against interpreting this simple PSF fit quantitatively; deficit core is centered on target.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 7 | 0 | 1492.9980107 | 0.010417 | 112.398 | usable; same-kind selection applies |
| 7 | 1 | 1501.3580369 | 0.010417 | 110.266 | usable; same-kind selection applies |
| 7 | 2 | 1509.7179946 | 0.010417 | 112.749 | usable; same-kind selection applies |
| 34 | 89 | 2237.0105695 | 0.003472 | 117.121 | usable; same-kind selection applies |
| 34 | 90 | 2245.3699671 | 0.003472 | 115.447 | usable; same-kind selection applies |
| 88 | 263 | 3691.5953460 | 0.001157 | 114.711 | usable; same-kind selection applies |
| 88 | 264 | 3699.9555267 | 0.001157 | 113.726 | usable; same-kind selection applies |
| 88 | 265 | 3708.3148285 | 0.001157 | 113.351 | usable; same-kind selection applies |
| 88 | 266 | 3716.6743233 | 0.001157 | 113.901 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s88.json, historical/diff_s88.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R287. [Deciding evidence](../../evidence/143375995/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
