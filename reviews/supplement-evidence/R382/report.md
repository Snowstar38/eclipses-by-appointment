# TIC 128825695: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX contain 21 distinct eclipse events in selected sectors[56, 83]. The representative raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 11 same-kind midtimes give P=4.8028045149 +/-0.0000048724d, reference eclipse epoch BTJD2826.0721681, kind: Deeper eclipse; even historical half-period cycles. Partial or singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S56 deficit peak[8, 7] vs target pixel[8, 7]; deficit-target separation1.753arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.408. Capable neighbours: Gaia 1904568750234102400: 51.23 arcsec, G12.586, required fractional eclipse0.043
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths13.142/12.399/10.344ppt, with 12 stacked events. QLP selected-kind fitted median17.106ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR31904568715874364160, P=4.8031801465+/-0.0002357494d, e=0.067203, omega=233.4166deg. Closest edge-on conjunction offset-0.165546d (-0.034466phase), full-SB1-covariance linear propagated Gaia uncertainty0.124919d at the measured epoch. Near-Gaia-reference projected eclipse offset0.024899d (photometric period projection allowance0.002470d). The approximate central duration6.52h vs observed median3.05h is a radius/minimum-mass illustration, not a detailed binary fit.  Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Unequal alternating eclipses establish doubled orbital period relative to historical SAP half branch. Even11 deeper events define ephemeris; odd secondary timings excluded. Target deficit0.083pixel versus capable neighbor2.531pixels.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 56 | 452 | 2826.0724916 | 0.001157 | 17.106 | used in ephemeris |
| 56 | 453 | 2828.4942892 | 0.001352 | 10.922 | measured; excluded from primary fit (secondary event) |
| 56 | 454 | 2830.8743699 | 0.001157 | 16.895 | used in ephemeris |
| 56 | 455 | 2833.2930554 | 0.001578 | 12.377 | measured; excluded from primary fit (secondary event) |
| 56 | 456 | 2835.6776301 | 0.001249 | 18.272 | used in ephemeris |
| 56 | 458 | 2840.4807618 | 0.001157 | 15.987 | used in ephemeris |
| 56 | 459 | 2842.9021433 | 0.001198 | 11.381 | measured; excluded from primary fit (secondary event) |
| 56 | 460 | 2845.2829200 | 0.001157 | 17.889 | used in ephemeris |
| 56 | 461 | 2847.7023979 | 0.001479 | 12.048 | measured; excluded from primary fit (secondary event) |
| 56 | 462 | 2850.0877416 | 0.001722 | 18.482 | used in ephemeris |
| 56 | 463 | 2852.5049818 | 0.001716 | 7.258 | measured; excluded from primary fit (secondary event) |
| 83 | 758 | 3560.9028777 | 0.001157 | 16.620 | used in ephemeris |
| 83 | 759 | 3563.3188879 | 0.001538 | 10.988 | measured; excluded from primary fit (secondary event) |
| 83 | 760 | 3565.7020372 | 0.001157 | 17.010 | used in ephemeris |
| 83 | 761 | 3568.1223736 | 0.001157 | 9.544 | measured; excluded from primary fit (secondary event) |
| 83 | 762 | 3570.5065417 | 0.001157 | 15.349 | used in ephemeris |
| 83 | 763 | 3572.9253431 | 0.001345 | 9.593 | measured; excluded from primary fit (secondary event) |
| 83 | 764 | 3575.3101004 | 0.001724 | 19.003 | used in ephemeris |
| 83 | 765 | 3577.7288782 | 0.001240 | 11.536 | measured; excluded from primary fit (secondary event) |
| 83 | 766 | 3580.1130087 | 0.001157 | 19.051 | used in ephemeris |
| 83 | 767 | 3582.5320671 | 0.001262 | 11.906 | measured; excluded from primary fit (secondary event) |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s56.json, historical/diff_s56.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R382. [Deciding evidence](../../2026-10-31-bright73/evidence/128825695) and [catalogue coverage](../../2026-10-31-bright73/catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../2026-10-31-bright73/evidence/128825695/measurements.json), [raw eclipse plots](../../2026-10-31-bright73/evidence/128825695/raw-events.png), [raw flux windows](../../2026-10-31-bright73/evidence/128825695/raw-windows.csv), [Gaia geometry](../../2026-10-31-bright73/analysis/batch05/gaia-geometry.json), [independent audit](../../2026-10-31-bright73/analysis/batch05/helper-audit.md), [difference image](../../2026-10-31-bright73/evidence/128825695/historical/diff_s56.png).
