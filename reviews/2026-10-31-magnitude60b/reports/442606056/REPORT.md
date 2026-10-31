# TIC 442606056: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free eclipse-core fits to quality-zero raw QLP SAP_FLUX show 8 distinct eclipse events in selected sectors[12, 65, 103]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local baseline, free depth, center, duration and ingress were fitted with a linear baseline; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 8 same-kind midtimes give P=5.3867042118 +/-0.0000046689d, reference eclipse epoch BTJD1651.0703266, kind: Selected repeating eclipse; primary/secondary depth identity not established. No center-covariance fits were excluded. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Saved S65 deficit peak[8, 8] vs target pixel[8, 8]; deficit-target separation3.973arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.905. Capable neighbours: Gaia 6015192755661126144: 8.81 arcsec, G12.576, required fractional eclipse0.165; Gaia 6015192790020864256: 50.94 arcsec, G13.336, required fractional eclipse0.259; Gaia 6015192790020865024: 56.30 arcsec, G14.423, required fractional eclipse0.581
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths51.676/42.364/34.810ppt, with 4 stacked events (quality-zero data). QLP selected-kind fitted median75.874ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR36015192755661126400, P=5.3867234906+/-0.0003950484d, e=0.026677, omega=105.4305deg. Closest edge-on conjunction offset-0.034817d (-0.006463phase), full-SB1-covariance linear propagated Gaia uncertainty0.107917d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.030306d (photometric period projection allowance0.001093d). The approximate central duration5.75h vs observed median3.81h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Crowded unresolved field: deficit0.189pixel from target versus closest capable G12.6neighbor0.62pixel. Deficit maximum is target pixel and centroid is displaced away from this neighbor, favoring target. No calibrated localization uncertainty, so resolved photometry remains useful. Intrinsic neighbor requirement is not compared directly to blended pixel loss.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 12 | 3 | 1651.0662448 | 0.010416 | 64.269 | selected |
| 65 | 267 | 3073.1604315 | 0.001157 | 81.142 | selected |
| 65 | 268 | 3078.5469895 | 0.001157 | 81.633 | selected |
| 65 | 269 | 3083.9336036 | 0.001157 | 80.791 | selected |
| 65 | 270 | 3089.3202674 | 0.001157 | 81.189 | selected |
| 103 | 468 | 4155.8877713 | 0.001157 | 69.463 | selected |
| 103 | 469 | 4161.2748774 | 0.001157 | 70.957 | selected |
| 103 | 470 | 4166.6600791 | 0.001849 | 69.807 | selected |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv; shared-qlp QLP FITS; historical/diff_s65.json, historical/diff_s65.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R314. [Deciding evidence](../../evidence/442606056/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
