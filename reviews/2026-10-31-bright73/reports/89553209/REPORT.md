# TIC 89553209: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX contain 6 distinct eclipse events in selected sectors[14, 54, 81]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 5 same-kind midtimes give P=11.8658638287 Ã‚+/-0.0000359636d, reference eclipse epoch BTJD1695.6867422, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Partial or singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S14 deficit peak[8, 7] vs target pixel[7, 8]; deficit-target separation0.970arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.476. Capable neighbours: Gaia 2024239325242611072: 53.46 arcsec, G14.018, required fractional eclipse0.461
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths10.283/12.097/12.528ppt, with 2 stacked events. QLP selected-kind fitted median51.272ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR32024239325242612736, P=11.8678248503Ã‚+/-0.0035823200d, e=0.375346, omega=266.7319deg. Closest edge-on conjunction offset-0.231422d (-0.019500phase), full-SB1-covariance linear propagated Gaia uncertainty0.480204d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.015709d (photometric period projection allowance0.003956d). The approximate central duration12.04h vs observed median11.52h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Sector14 cycle-1 lacks ingress coverage and is excluded from timing. Remaining five measured events include successive sector54/81 pairs and a full sector14 event. Historical prediction drift is fitted freely; partial raw event is not a precise timing. Broad eclipse duration and radius-based central estimate agree approximately.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 14 | -1 | 1683.8202443 | 0.010417 | 50.113 | Partially covered eclipse lacks ingress baseline; retained raw morphology but excluded timing. |
| 14 | 0 | 1695.6905685 | 0.010417 | 51.272 | used in ephemeris |
| 54 | 91 | 2775.4780234 | 0.003472 | 52.415 | used in ephemeris |
| 54 | 92 | 2787.3475254 | 0.003472 | 51.847 | used in ephemeris |
| 81 | 153 | 3511.1638934 | 0.001157 | 51.095 | used in ephemeris |
| 81 | 154 | 3523.0298522 | 0.001157 | 50.557 | used in ephemeris |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s14.json, historical/diff_s14.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R346. [Deciding evidence](../../evidence/89553209/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../evidence/89553209/measurements.json), [raw eclipse plots](../../evidence/89553209/raw-events.png), [raw flux windows](../../evidence/89553209/raw-windows.csv), [Gaia geometry](../../analysis/batch01/gaia-geometry.json), [independent audit](../../analysis/batch01/helper-audit.md), [difference image](../../evidence/89553209/historical/diff_s14.png).
