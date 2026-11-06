# TIC 436092743: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 8 distinct eclipse events in selected sectors[55, 82]. The raw-event plot and numeric raw-windows.csv were inspected. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 4 same-kind midtimes give P=13.1290724046 ±0.0000461943d, reference eclipse epoch BTJD2799.7762801, kind: Deeper primary (odd half-period cycles). Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S55 deficit peak[8, 7] vs target pixel[8, 7]; deficit-target separation2.240arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.238. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths118.232/111.779/104.775ppt, with 4 stacked events. QLP selected-kind fitted median152.348ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR31860331033765994880, P=13.1281268605±0.0022765186d, e=0.011420, omega=39.9211deg. Closest edge-on conjunction offset0.178987d (0.013634phase), full-SB1-covariance linear propagated Gaia uncertainty0.443548d at the measured epoch. Near-Gaia-reference projected eclipse offset0.005007d (photometric period projection allowance0.008500d). The approximate central duration17.53h vs observed median13.88h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Unequal alternating eclipses approximately153/100ppt establish full orbital period13.12907d, twice historical SAP branch. Odd half-period cycles are deeper primary eclipses and alone define ephemeris. Historical cutout stack mixes eclipse kinds; no capable neighbor.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 55 | 169 | 2799.7763956 | 0.003472 | 153.464 | usable; same-kind selection applies |
| 55 | 170 | 2806.3419285 | 0.003472 | 100.211 | usable; same-kind selection applies |
| 55 | 171 | 2812.9052776 | 0.003472 | 153.246 | usable; same-kind selection applies |
| 55 | 172 | 2819.4696319 | 0.003472 | 101.964 | usable; same-kind selection applies |
| 82 | 281 | 3535.0040697 | 0.001157 | 151.450 | usable; same-kind selection applies |
| 82 | 282 | 3541.5703121 | 0.001157 | 99.967 | usable; same-kind selection applies |
| 82 | 283 | 3548.1336678 | 0.001157 | 151.281 | usable; same-kind selection applies |
| 82 | 284 | 3554.6980615 | 0.001157 | 100.703 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, ../identity-check.json, shared-qlp QLP FITS; historical/diff_s55.json, historical/diff_s55.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R243. [Deciding evidence](../../evidence/436092743/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
