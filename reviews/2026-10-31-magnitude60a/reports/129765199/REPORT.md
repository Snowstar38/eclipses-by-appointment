# TIC 129765199: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 5 distinct eclipse events in selected sectors[3, 97, 104]. The raw-event plot and numeric raw-windows.csv were inspected. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass with disclosed cycle assumptions.** 5 same-kind midtimes give P=18.2494315475 ±0.0000459899d, reference eclipse epoch BTJD1385.4630846, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S3 deficit peak[7, 7] vs target pixel[7, 7]; deficit-target separation3.721arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.152. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths124.676/125.418/125.076ppt, with 2 stacked events. Historical outputs are retained as measured pipeline evidence. QLP selected-kind fitted median108.159ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR34963994287275259008, P=18.2510587758±0.0033978994d, e=0.275285, omega=357.8710deg. Closest edge-on conjunction offset0.029584d (0.001621phase), full-SB1-covariance linear propagated Gaia uncertainty0.275262d at the measured epoch. Near-Gaia-reference projected eclipse offset0.119082d (photometric period projection allowance0.002529d). The approximate central duration10.13h vs observed median8.54h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Deep repeating eclipses, target-centered deficit, no capable catalogued neighbor. Sector-dependent depth is dilution or extraction dependent.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 3 | 0 | 1385.4673363 | 0.010417 | 116.516 | usable; same-kind selection applies |
| 3 | 1 | 1403.7164435 | 0.010417 | 116.116 | usable; same-kind selection applies |
| 97 | 140 | 3940.3829309 | 0.001157 | 103.742 | usable; same-kind selection applies |
| 97 | 141 | 3958.6323546 | 0.001157 | 102.892 | usable; same-kind selection applies |
| 104 | 154 | 4195.8765905 | 0.001157 | 108.159 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): ../helper/pixel-identity-audit.json, ../helper/same-sector-refits.json, ../helper/314047448-measured-diff.json, ../helper/48108063-measured-diff.json; measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s03.json, historical/diff_s03.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R251. [Deciding evidence](../../evidence/129765199/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
