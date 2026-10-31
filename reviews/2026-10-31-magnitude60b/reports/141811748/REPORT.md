# TIC 141811748: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 7 distinct eclipse events in selected sectors[1, 37, 98]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 7 same-kind midtimes give P=6.8389313923 ±0.0000094980d, reference eclipse epoch BTJD1334.0304484, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Unreliable fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S97 deficit peak[7, 8] vs target pixel[7, 8]; deficit-target separation3.935arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.218. Capable neighbours: Gaia 5260245291514395136: 38.08 arcsec, G14.242, required fractional eclipse0.394
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths37.325/34.581/32.925ppt, with 7 stacked events. Historical event coordinates guide these stacks and are not newly measured midtimes. QLP selected-kind fitted median31.682ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR35260245600752043648, P=6.8386133503±0.0007182882d, e=0.029587, omega=203.5107deg. Closest edge-on conjunction offset0.001233d (0.000180phase), full-SB1-covariance linear propagated Gaia uncertainty0.123473d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.042657d (photometric period projection allowance0.001311d). The approximate central duration8.07h vs observed median4.78h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Repeated isolated eclipses across three sectors; sector/aperture-dependent dilution retained. Target-deficit0.187pixel vs closest capable neighbor1.67pixels favors target; no calibrated centroid errors. Sector37 actual adjacent cycles144/145/146 show raw core depths38.52/37.30/37.68ppt (11/11/12 in-event cadences); cycle145 fails fit side-window threshold but tests recurrence. Missing even sector98 cycles have no raw coverage. Sparse sector1 cycles0/1/2 also recur. Thus apparent alternating-sector98 pattern is coverage, not doubled period; see coverage-alias.json.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 1 | 1 | 1334.0294197 | 0.010417 | 35.535 | usable; same-kind selection applies |
| 37 | 144 | 2311.9974617 | 0.003472 | 38.985 | usable; same-kind selection applies |
| 37 | 146 | 2325.6759452 | 0.003472 | 39.138 | usable; same-kind selection applies |
| 98 | 391 | 4001.2135603 | 0.001157 | 31.574 | usable; same-kind selection applies |
| 98 | 393 | 4014.8910898 | 0.001157 | 31.163 | usable; same-kind selection applies |
| 98 | 395 | 4028.5695202 | 0.001157 | 31.682 | usable; same-kind selection applies |
| 98 | 397 | 4042.2477547 | 0.001157 | 31.567 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s97.json, historical/diff_s97.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R294. [Deciding evidence](../../evidence/141811748/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
