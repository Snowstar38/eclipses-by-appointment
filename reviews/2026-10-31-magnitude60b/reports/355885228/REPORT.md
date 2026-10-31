# TIC 355885228: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 6 distinct eclipse events in selected sectors[24, 51, 78]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 3 same-kind midtimes give P=12.2236227521 ±0.0000760471d, reference eclipse epoch BTJD1959.6132243, kind: Deeper repeating eclipse; even half-period cycles. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S24 deficit peak[7, 7] vs target pixel[7, 7]; deficit-target separation2.151arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.060. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths21.673/20.791/20.470ppt, with 4 stacked events. QLP selected-kind fitted median26.934ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR31214467114648223616, P=12.2241552395±0.0009737126d, e=0.003387, omega=37.0094deg. Closest edge-on conjunction offset-0.119695d (-0.009792phase), full-SB1-covariance linear propagated Gaia uncertainty0.140237d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.051537d (photometric period projection allowance0.009734d). The approximate central duration16.72h vs observed median10.74h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Unequal alternating eclipses support doubled orbital period; three deeper even-half-period events include a sector24 same-kind repeat and sector78 recurrence. Historical cutout mixes kinds.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 24 | 0 | 1959.6145829 | 0.010417 | 25.806 | usable; same-kind selection applies |
| 24 | 1 | 1965.7098686 | 0.016196 | 20.182 | usable; same-kind selection applies |
| 24 | 2 | 1971.8324839 | 0.018590 | 26.934 | usable; same-kind selection applies |
| 24 | 3 | 1977.9430294 | 0.014045 | 14.810 | usable; same-kind selection applies |
| 51 | 121 | 2699.1303431 | 0.003472 | 12.696 | usable; same-kind selection applies |
| 78 | 242 | 3438.6715775 | 0.001327 | 27.086 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s24.json, historical/diff_s24.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R282. [Deciding evidence](../../evidence/355885228/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
