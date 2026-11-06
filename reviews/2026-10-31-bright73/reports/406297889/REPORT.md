# TIC 406297889: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX contain 23 distinct eclipse events in selected sectors[14, 55, 82]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 23 same-kind midtimes give P=2.8227799299 ±0.0000039347d, reference eclipse epoch BTJD1685.8956770, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Partial or singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S55 deficit peak[8, 8] vs target pixel[8, 8]; deficit-target separation2.266arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.408. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths87.296/81.926/78.810ppt, with 10 stacked events. QLP selected-kind fitted median95.040ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR31860669069176556160, P=2.8228180213±0.0000945775d, e=0.034549, omega=126.9402deg. Closest edge-on conjunction offset-0.025598d (-0.009068phase), full-SB1-covariance linear propagated Gaia uncertainty0.046441d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.008114d (photometric period projection allowance0.001806d). The approximate central duration4.60h vs observed median4.16h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Repeated raw events across sectors14/55/82 with stable isolated morphology; no capable listed neighbor.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 14 | 0 | 1685.8917905 | 0.010417 | 95.040 | used in ephemeris |
| 14 | 1 | 1688.7135021 | 0.010417 | 96.145 | used in ephemeris |
| 14 | 5 | 1700.0051986 | 0.010417 | 93.668 | used in ephemeris |
| 14 | 6 | 1702.8279558 | 0.010417 | 95.062 | used in ephemeris |
| 55 | 394 | 2798.0717778 | 0.003472 | 96.535 | used in ephemeris |
| 55 | 395 | 2800.8942891 | 0.003472 | 96.278 | used in ephemeris |
| 55 | 396 | 2803.7169761 | 0.003472 | 95.099 | used in ephemeris |
| 55 | 397 | 2806.5398949 | 0.003472 | 97.329 | used in ephemeris |
| 55 | 398 | 2809.3628982 | 0.003472 | 98.674 | used in ephemeris |
| 55 | 399 | 2812.1855604 | 0.003472 | 96.196 | used in ephemeris |
| 55 | 400 | 2815.0081985 | 0.003472 | 96.954 | used in ephemeris |
| 55 | 401 | 2817.8306117 | 0.003472 | 95.109 | used in ephemeris |
| 55 | 402 | 2820.6534237 | 0.003472 | 92.253 | used in ephemeris |
| 55 | 403 | 2823.4761498 | 0.003472 | 99.577 | used in ephemeris |
| 82 | 655 | 3534.8161824 | 0.001157 | 93.909 | used in ephemeris |
| 82 | 656 | 3537.6390350 | 0.001157 | 93.036 | used in ephemeris |
| 82 | 657 | 3540.4625039 | 0.001157 | 93.587 | used in ephemeris |
| 82 | 658 | 3543.2846434 | 0.001157 | 94.343 | used in ephemeris |
| 82 | 659 | 3546.1075581 | 0.001157 | 92.950 | used in ephemeris |
| 82 | 660 | 3548.9305805 | 0.001157 | 94.080 | used in ephemeris |
| 82 | 661 | 3551.7530043 | 0.001157 | 94.672 | used in ephemeris |
| 82 | 662 | 3554.5760892 | 0.001157 | 93.599 | used in ephemeris |
| 82 | 663 | 3557.3989236 | 0.001157 | 93.538 | used in ephemeris |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s55.json, historical/diff_s55.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R363. [Deciding evidence](../../evidence/406297889/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../evidence/406297889/measurements.json), [raw eclipse plots](../../evidence/406297889/raw-events.png), [raw flux windows](../../evidence/406297889/raw-windows.csv), [Gaia geometry](../../analysis/batch03/gaia-geometry.json), [independent audit](../../analysis/batch03/helper-audit.md), [difference image](../../evidence/406297889/historical/diff_s55.png).
