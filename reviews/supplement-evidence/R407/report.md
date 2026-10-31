# TIC 348302938: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX contain 14 distinct eclipse events in selected sectors[61, 88]. The representative raw-event plot and numeric raw-windows.csv were inspected. The raw morphology, ingress/egress and local baselines were inspected independently of fitted curves; target-specific interpretation follows below. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 14 same-kind midtimes give P=3.6439561479 +/-0.0000165768d, reference eclipse epoch BTJD2966.8369124, kind: Selected repeating eclipse; deeper/secondary identity not independently established. Partial or singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S88 deficit peak[8, 8] vs target pixel[8, 7]; deficit-target separation5.678arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.501. Capable neighbours: Gaia 5724552009498100864: 23.97 arcsec, G15.762, required fractional eclipse0.105; Gaia 5724552211356494720: 25.07 arcsec, G16.345, required fractional eclipse0.178; Gaia 5724552005198026112: 45.97 arcsec, G17.629, required fractional eclipse0.573; Gaia 5724551940778622464: 56.93 arcsec, G17.131, required fractional eclipse0.364
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths2.496/2.706/2.806ppt, with 8 stacked events. QLP selected-kind fitted median4.557ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR35724552009498098432, P=3.6439522672+/-0.0003950777d, e=0.097407, omega=267.6439deg. Closest edge-on conjunction offset-0.047381d (-0.013003phase), full-SB1-covariance linear propagated Gaia uncertainty0.314984d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.050125d (photometric period projection allowance0.011720d). The approximate central duration4.73h vs observed median2.37h is a radius/minimum-mass illustration, not a detailed binary fit.  Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Fourteen shallow narrow V-shaped eclipses repeat in S61/88; individual depths scatter at several ppt noise. Deficit0.270pixel from target versus nearest capable neighbor1.107pixels. Consecutive cycles constrain recurrence; parity depths are consistent within noise. Nearly equal primary/secondary events could leave a doubled orbital alias photometrically ambiguous; Gaia supports the retained branch.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 61 | 404 | 2966.8241799 | 0.006847 | 4.757 | used in ephemeris |
| 61 | 405 | 2970.4831648 | 0.002995 | 4.088 | used in ephemeris |
| 61 | 406 | 2974.1250280 | 0.002526 | 5.125 | used in ephemeris |
| 61 | 407 | 2977.7748846 | 0.002680 | 4.731 | used in ephemeris |
| 61 | 408 | 2981.4141019 | 0.002771 | 4.682 | used in ephemeris |
| 61 | 409 | 2985.0509515 | 0.002354 | 6.305 | used in ephemeris |
| 88 | 603 | 3691.9795432 | 0.005384 | 3.563 | used in ephemeris |
| 88 | 604 | 3695.6226915 | 0.005366 | 4.432 | used in ephemeris |
| 88 | 605 | 3699.2769256 | 0.005225 | 4.080 | used in ephemeris |
| 88 | 606 | 3702.9116340 | 0.003064 | 3.874 | used in ephemeris |
| 88 | 607 | 3706.5554139 | 0.004973 | 6.227 | used in ephemeris |
| 88 | 608 | 3710.2084557 | 0.003975 | 4.014 | used in ephemeris |
| 88 | 609 | 3713.8504577 | 0.004090 | 2.649 | used in ephemeris |
| 88 | 610 | 3717.5198846 | 0.008513 | 4.999 | used in ephemeris |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s88.json, historical/diff_s88.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are [local path omitted] and [local path omitted] No historical evidence overwritten. Historical inventory G=12.0059; actual nested Gaia DR3 G=11.996688. All three are inside actual DR3 G11.5-12 despite inventory values above12; this preserves the inventory/DR3 distinction.


Stable review key: R407. [Deciding evidence](../../2026-10-31-bright73/evidence/348302938) and [catalogue coverage](../../2026-10-31-bright73/catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../2026-10-31-bright73/evidence/348302938/measurements.json), [raw eclipse plots](../../2026-10-31-bright73/evidence/348302938/raw-events.png), [raw flux windows](../../2026-10-31-bright73/evidence/348302938/raw-windows.csv), [Gaia geometry](../../2026-10-31-bright73/analysis/batch08/gaia-geometry.json), [independent audit](../../2026-10-31-bright73/analysis/batch08/helper-audit.md), [difference image](../../2026-10-31-bright73/evidence/348302938/historical/diff_s88.png).
