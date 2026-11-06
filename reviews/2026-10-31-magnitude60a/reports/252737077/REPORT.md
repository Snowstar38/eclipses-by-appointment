# TIC 252737077: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 6 distinct eclipse events in selected sectors[16, 57, 84]. The raw-event plot and numeric raw-windows.csv were inspected. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 6 same-kind midtimes give P=10.2034445887 ±0.0000145011d, reference eclipse epoch BTJD1757.7979046, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S57 deficit peak[8, 8] vs target pixel[8, 8]; deficit-target separation4.251arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.943. Capable neighbours: Gaia 1995327181638998016: 42.69 arcsec, G12.539, required fractional eclipse0.653, pixel fractional loss0.013331207987805165; Gaia 1995327525236380800: 53.79 arcsec, G9.660, required fractional eclipse0.237, pixel fractional loss0.00028959663111898507
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths160.420/95.526/43.208ppt, with 3 stacked events. QLP selected-kind fitted median208.935ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR31995327254658341888, P=10.2047428233±0.0012404385d, e=0.066845, omega=343.3919deg. Closest edge-on conjunction offset-0.047365d (-0.004641phase), full-SB1-covariance linear propagated Gaia uncertainty0.203135d at the measured epoch. Near-Gaia-reference projected eclipse offset0.126599d (photometric period projection allowance0.001943d). The approximate central duration6.54h vs observed median5.46h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Strong aperture dilution: raw QLP approximately209ppt versus cutout1/3/5 aperture160/96/43ppt. Deficit core is target-centered; capable neighbors42.7/53.8arcsec away are2.06/2.72pixels from the deficit centroid versus0.20pixel for target; blended local loss is not an intrinsic-source eclipse constraint. Poor total-light PSF residual0.943 reflects crowding; no intrinsic depth is inferred.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 16 | 1 | 1757.7984314 | 0.010417 | 211.716 | usable; same-kind selection applies |
| 57 | 109 | 2859.7700065 | 0.001157 | 209.782 | usable; same-kind selection applies |
| 57 | 110 | 2869.9730680 | 0.001157 | 204.648 | usable; same-kind selection applies |
| 57 | 111 | 2880.1770048 | 0.001157 | 208.907 | usable; same-kind selection applies |
| 84 | 181 | 3594.4179451 | 0.001157 | 208.229 | usable; same-kind selection applies |
| 84 | 182 | 3604.6213692 | 0.001157 | 208.963 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, ../identity-check.json, shared-qlp QLP FITS; historical/diff_s57.json, historical/diff_s57.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R237. [Deciding evidence](../../evidence/252737077/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
