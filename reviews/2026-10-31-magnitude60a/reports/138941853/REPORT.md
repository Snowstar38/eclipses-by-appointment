# TIC 138941853: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 5 distinct eclipse events in selected sectors[6, 32, 98]. The raw-event plot and numeric raw-windows.csv were inspected. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 5 same-kind midtimes give P=11.5985912130 ±0.0000160827d, fitted ephemeris intercept at earliest retained cycle BTJD1475.6404802, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S98 deficit peak[8, 7] vs target pixel[8, 7]; deficit-target separation1.841arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.425. Capable neighbours: Gaia 3223511670208848896: 21.77 arcsec, G16.492, required fractional eclipse0.500, pixel fractional loss0.00821316823921336; Gaia 3223511734632170368: 33.94 arcsec, G16.100, required fractional eclipse0.351, pixel fractional loss0.005558516488320414; Gaia 3223511704568589952: 43.67 arcsec, G15.493, required fractional eclipse0.204, pixel fractional loss0.007256264006483505; Gaia 3223511429690683776: 44.80 arcsec, G13.282, required fractional eclipse0.033, pixel fractional loss0.0017700490677724006
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths9.200/8.300/6.809ppt, with 3 stacked events. QLP selected-kind fitted median9.255ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR33223511665912271232, P=11.6019567518±0.0050960393d, e=0.024700, omega=125.6521deg. Closest edge-on conjunction offset0.035580d (0.003067phase), full-SB1-covariance linear propagated Gaia uncertainty0.523683d at the measured epoch. Near-Gaia-reference projected eclipse offset0.351941d (photometric period projection allowance0.001512d). The approximate central duration7.90h vs observed median3.75h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Approximately8-10ppt eclipses repeat in sectors6/32/98. Deficit0.087pixel from target vs nearest capable source1.127pixel. Near-reference Gaia offset0.352d is descriptive; low-eccentricity orbit conjunction is poorly constrained. Actual epoch offset0.036d with0.524d propagated Gaia uncertainty is compatible.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 6 | 0 | 1475.6339074 | 0.010416 | 7.810 | usable; same-kind selection applies |
| 32 | 61 | 2183.1561435 | 0.003472 | 9.392 | usable; same-kind selection applies |
| 32 | 62 | 2194.7525984 | 0.003472 | 9.255 | usable; same-kind selection applies |
| 98 | 219 | 4015.7299466 | 0.001661 | 9.928 | usable; same-kind selection applies |
| 98 | 220 | 4027.3317908 | 0.001333 | 7.985 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s98.json, historical/diff_s98.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R234. [Deciding evidence](../../evidence/138941853/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
