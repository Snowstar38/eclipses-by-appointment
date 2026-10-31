# TIC 168917716: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX contain 7 distinct eclipse events in selected sectors[14, 74, 82]. The representative raw-event plot and numeric raw-windows.csv were inspected. The raw morphology, ingress/egress and local baselines were inspected independently of fitted curves; target-specific interpretation follows below. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 5 same-kind midtimes give P=13.4024383530 +/-0.0000718553d, reference eclipse epoch BTJD1699.2149087, kind: Selected alternating eclipse; even half-period cycles; depth parity nearly equal, orbital identity informed by Gaia. Partial or singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S41 deficit peak[7, 7] vs target pixel[7, 7]; deficit-target separation1.800arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.666. Capable neighbours: Gaia 2072042036374420736: 16.82 arcsec, G15.817, required fractional eclipse0.581; Gaia 2072040558905683072: 41.98 arcsec, G16.071, required fractional eclipse0.730; Gaia 2072040352747228672: 44.54 arcsec, G14.587, required fractional eclipse0.198; Gaia 2072042105093927936: 52.14 arcsec, G15.474, required fractional eclipse0.428; Gaia 2072040558905685632: 54.35 arcsec, G15.169, required fractional eclipse0.327; Gaia 2072040348430214784: 56.78 arcsec, G13.458, required fractional eclipse0.081; Gaia 2072040558905691648: 58.77 arcsec, G15.239, required fractional eclipse0.348
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths17.954/18.356/16.103ppt, with 4 stacked events. QLP selected-kind fitted median16.506ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR32072041830215983360, P=13.4010756298+/-0.0017605164d, e=0.043450, omega=234.1643deg. Closest edge-on conjunction offset0.196176d (0.014639phase), full-SB1-covariance linear propagated Gaia uncertainty0.189543d at the measured epoch. Near-Gaia-reference projected eclipse offset0.062630d (photometric period projection allowance0.007042d). The approximate central duration12.09h vs observed median4.68h is a radius/minimum-mass illustration, not a detailed binary fit.  Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Shallow repeating eclipses across S14/74/82 with nearly equal alternating depths. Photometry supports6.701d repetition; selected even cycles give13.40244d consistent with Gaia orbit. Equal depths alone cannot reject half-period orbital identity; retained doubled branch explicitly uses Gaia and eclipse parity, with primary identity unresolved. Deficit0.086pixel versus nearest capable neighbor0.859pixel.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 14 | 2 | 1699.2085569 | 0.010417 | 14.696 | used in ephemeris |
| 74 | 244 | 3320.9122083 | 0.002050 | 16.506 | used in ephemeris |
| 74 | 246 | 3334.3119945 | 0.002017 | 17.610 | used in ephemeris |
| 82 | 276 | 3535.3499738 | 0.001446 | 15.270 | used in ephemeris |
| 82 | 277 | 3542.0554081 | 0.001394 | 17.804 | measured; excluded opposite parity (identity unresolved) |
| 82 | 278 | 3548.7495208 | 0.001473 | 16.810 | used in ephemeris |
| 82 | 279 | 3555.4557456 | 0.001531 | 17.083 | measured; excluded opposite parity (identity unresolved) |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s41.json, historical/diff_s41.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are [local path omitted] and [local path omitted] No historical evidence overwritten.


Stable review key: R402. [Deciding evidence](../../evidence/168917716/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../evidence/168917716/measurements.json), [raw eclipse plots](../../evidence/168917716/raw-events.png), [raw flux windows](../../evidence/168917716/raw-windows.csv), [Gaia geometry](../../analysis/batch07/gaia-geometry.json), [independent audit](../../analysis/batch07/helper-audit.md), [difference image](../../evidence/168917716/historical/diff_s41.png).
