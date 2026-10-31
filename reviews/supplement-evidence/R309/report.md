# TIC 21295315: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free eclipse-core fits to quality-zero raw QLP SAP_FLUX show 5 distinct eclipse events in selected sectors[20, 47, 60]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local baseline, free depth, center, duration and ingress were fitted with a linear baseline; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 5 same-kind midtimes give P=11.6068097551 +/-0.0000652497d, reference eclipse epoch BTJD1861.1294409, kind: Selected repeating eclipse; primary/secondary depth identity not established. No center-covariance fits were excluded. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Saved S47 deficit peak[7, 7] vs target pixel[8, 7]; deficit-target separation0.471arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.288. Capable neighbours: Gaia 895666127653255552: 58.00 arcsec, G13.835, required fractional eclipse0.428
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths84.424/81.615/70.247ppt, with 3 stacked events (quality-zero data). QLP selected-kind fitted median87.584ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR3895666402531207936, P=11.6050108508+/-0.0044449065d, e=0.299861, omega=90.5800deg. Closest edge-on conjunction offset0.251296d (0.021654phase), full-SB1-covariance linear propagated Gaia uncertainty0.732493d at the measured epoch. Near-Gaia-reference projected eclipse offset0.022835d (photometric period projection allowance0.008287d). The approximate central duration3.85h vs observed median3.24h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Five raw eclipses include consecutive cycles63/64/65 in sector47, testing recurrence. Target deficit0.022pixel versus capable neighbor2.73pixels. Gaia conjunction linear uncertainty0.73d limits phase inference.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 20 | 1 | 1861.1296303 | 0.010417 | 90.311 | selected |
| 47 | 63 | 2580.7518230 | 0.003472 | 87.584 | selected |
| 47 | 64 | 2592.3581302 | 0.003472 | 86.818 | selected |
| 47 | 65 | 2603.9653446 | 0.003472 | 88.603 | selected |
| 60 | 94 | 2940.5627534 | 0.001157 | 85.522 | selected |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv; shared-qlp QLP FITS; historical/diff_s47.json, historical/diff_s47.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R309. [Deciding evidence](../../2026-10-31-magnitude60b/evidence/21295315) and [catalogue coverage](../../2026-10-31-magnitude60b/catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
