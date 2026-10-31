# TIC 445438807: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free eclipse-core fits to quality-zero raw QLP SAP_FLUX show 12 distinct eclipse events in selected sectors[18, 58, 85]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local baseline, free depth, center, duration and ingress were fitted with a linear baseline; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 12 same-kind midtimes give P=3.6681590097 +/-0.0000037951d, reference eclipse epoch BTJD1795.6720263, kind: Selected repeating eclipse; primary/secondary depth identity not established. No center-covariance fits were excluded. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Saved S58 deficit peak[7, 8] vs target pixel[7, 8]; deficit-target separation3.948arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.712. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths84.862/73.669/64.838ppt, with 5 stacked events (quality-zero data). QLP selected-kind fitted median92.316ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR3505891592075928320, P=3.6680210933+/-0.0002846168d, e=0.007003, omega=146.5116deg. Closest edge-on conjunction offset0.043915d (0.011973phase), full-SB1-covariance linear propagated Gaia uncertainty0.122864d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.008907d (photometric period projection allowance0.001454d). The approximate central duration3.83h vs observed median3.18h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Twelve quality-zero measured raw events over three sectors test recurrence. No capable neighbor within60arcsec under approximate Gaia flux budget; target deficit0.188pixel. Finite-cadence trapezoid and aperture dilution limit precision.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 18 | 0 | 1795.6719555 | 0.010417 | 87.415 | selected |
| 18 | 1 | 1799.3391082 | 0.010417 | 88.036 | selected |
| 18 | 4 | 1810.3453508 | 0.010417 | 92.246 | selected |
| 58 | 297 | 2885.1151565 | 0.001157 | 93.175 | selected |
| 58 | 298 | 2888.7832647 | 0.001157 | 93.054 | selected |
| 58 | 299 | 2892.4516689 | 0.001157 | 92.363 | selected |
| 58 | 301 | 2899.7877145 | 0.001157 | 92.278 | selected |
| 58 | 303 | 2907.1245149 | 0.001157 | 92.354 | selected |
| 85 | 496 | 3615.0796458 | 0.001157 | 91.341 | selected |
| 85 | 497 | 3618.7471859 | 0.001157 | 92.723 | selected |
| 85 | 498 | 3622.4157207 | 0.001157 | 92.426 | selected |
| 85 | 501 | 3633.4183143 | 0.001157 | 91.382 | selected |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv; shared-qlp QLP FITS; historical/diff_s58.json, historical/diff_s58.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R310. [Deciding evidence](../../evidence/445438807/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
