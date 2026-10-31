# TIC 29114881: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 6 distinct eclipse events in selected sectors[43, 45, 72]. The raw-event plot and numeric raw-windows.csv were inspected. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 6 same-kind midtimes give P=12.6025319623 +/-0.0000314390d, reference eclipse epoch BTJD2478.4844056, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Deciding S43 deficit peak[8, 8] vs target pixel[8, 8]; deficit-target separation2.217arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.315. Capable neighbours: Gaia 3403151219984383616: 53.54 arcsec, G14.899, required fractional eclipse0.579, pixel fractional loss0.010934079114229483
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths57.519/56.424/51.492ppt, with 2 stacked events. QLP selected-kind fitted median57.390ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR33403145344469126784, P=12.5997639477+/-0.0076575857d, e=0.081743, omega=206.9858deg. Closest edge-on conjunction offset0.028161d (0.002235phase), full-SB1-covariance linear propagated Gaia uncertainty1.025084d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.431329d (photometric period projection allowance0.005219d). The approximate central duration6.14h vs observed median5.33h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Six raw events across three sectors. Capable neighbor53.54arcsec is distinct from target-centered deficit. Raw56-59ppt and cutout57/56/51ppt depend on aperture.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 43 | 0 | 2478.4845644 | 0.003473 | 58.767 | usable; same-kind selection applies |
| 43 | 1 | 2491.0866878 | 0.003473 | 58.407 | usable; same-kind selection applies |
| 45 | 4 | 2528.8946730 | 0.003472 | 58.122 | usable; same-kind selection applies |
| 45 | 5 | 2541.4970666 | 0.003472 | 56.659 | usable; same-kind selection applies |
| 72 | 63 | 3272.4436002 | 0.001157 | 55.969 | usable; same-kind selection applies |
| 72 | 64 | 3285.0467647 | 0.001157 | 56.204 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, ../identity-check.json, shared-qlp QLP FITS; historical/diff_s43.json, historical/diff_s43.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] For TIC407207285 the deciding revised cutout is revised-cutout/diff_revised-long-window.json and .png; historical extraction remains for comparison. Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R264. [Deciding evidence](../../evidence/29114881/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
