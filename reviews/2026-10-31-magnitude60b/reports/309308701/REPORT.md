# TIC 309308701: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 4 distinct eclipse events in selected sectors[73, 86]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 4 same-kind midtimes give P=18.3848616420 ±0.0001132702d, reference eclipse epoch BTJD3291.8509571, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Unreliable fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S73 deficit peak[7, 7] vs target pixel[7, 7]; deficit-target separation3.247arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.312. Capable neighbours: Gaia 261872853348447872: 27.98 arcsec, G15.831, required fractional eclipse0.708
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths20.421/18.408/17.309ppt, with 2 stacked events. Historical event coordinates guide these stacks and are not newly measured midtimes. QLP selected-kind fitted median20.689ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR3261872780332852736, P=18.3808647997±0.0048918530d, e=0.311976, omega=136.7904deg. Closest edge-on conjunction offset0.655409d (0.035657phase), full-SB1-covariance linear propagated Gaia uncertainty0.842000d at the measured epoch. Near-Gaia-reference projected eclipse offset0.023907d (photometric period projection allowance0.017897d). The approximate central duration11.27h vs observed median5.50h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Four shallow isolated eclipses in sectors73/86, including adjacent-cycle pairs, test recurrence. Target-deficit0.155pixel vs nearest capable neighbor1.50pixels favors target; no calibrated centroid errors. Gaia nominal conjunction offset0.6554d but full-covariance linear allowance0.8420d and near-reference offset0.0239d support compatible geometry.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 73 | 80 | 3291.8516219 | 0.001157 | 21.044 | usable; same-kind selection applies |
| 73 | 81 | 3310.2347606 | 0.001487 | 20.239 | usable; same-kind selection applies |
| 86 | 99 | 3641.1600099 | 0.001993 | 20.748 | usable; same-kind selection applies |
| 86 | 100 | 3659.5495792 | 0.001303 | 20.629 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s73.json, historical/diff_s73.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R293. [Deciding evidence](../../evidence/309308701/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
