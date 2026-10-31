# TIC 345406164: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 7 distinct eclipse events in selected sectors[54, 81]. The lead inspected raw-event plots and numeric fitting summaries. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 5 same-kind midtimes give P=7.4405907450 ±0.0000495074d, reference primary epoch BTJD2771.4040073. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using quadrature-free conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage.
3. **Target attribution: pass at TESS image resolution.** Historical S81 deficit peak[7, 7] vs target pixel[7, 7]; deficit-target separation1.076arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.319. Capable neighbours: Gaia 4237461433423122688: 7.77 arcsec, G12.987, required fractional eclipse0.337, pixel fractional loss0.039804052005913027; Gaia 4237461639581556992: 39.85 arcsec, G14.229, required fractional eclipse0.903, pixel fractional loss0.012143463390351002; Gaia 4237462910891870720: 46.38 arcsec, G13.638, required fractional eclipse0.554, pixel fractional loss0.005077976710626553
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths39.804/40.512/36.074ppt, with 5 stacked events. QLP primary fitted median74.892ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR34237461433423121536, P=7.4404803638±0.0003387583d, e=0.018421, omega=297.4883deg. Closest edge-on conjunction offset0.055481d (0.007457phase), full-SB1-covariance linear propagated Gaia uncertainty0.115704d at the measured epoch. Near-Gaia-reference projected eclipse offset0.020159d (photometric period projection allowance0.015842d). The approximate central duration9.03h vs observed median5.08h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Deeper even cycles near75ppt alternate with47ppt odd eclipses in sector81, establishing doubled orbital period. Primary-only ephemeris used. Historical stack mixes eclipse kinds. Three capable neighbours are away from compact target deficit.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt |
|---|---|---|---|---|
| 54 | 0 | 2771.4036377 | 0.006944 | 67.387 |
| 54 | 4 | 2786.2853908 | 0.006944 | 75.268 |
| 81 | 198 | 3508.0226679 | 0.001157 | 75.143 |
| 81 | 199 | 3511.7407693 | 0.001157 | 47.168 |
| 81 | 202 | 3522.9036282 | 0.001157 | 74.889 |
| 81 | 203 | 3526.6219133 | 0.001157 | 47.305 |
| 81 | 204 | 3530.3441355 | 0.001157 | 74.892 |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, ../../shared-qlp/QLP FITS; historical/diff_s81.json, historical/diff_s81.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R189. [Deciding evidence](../../evidence/345406164/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
