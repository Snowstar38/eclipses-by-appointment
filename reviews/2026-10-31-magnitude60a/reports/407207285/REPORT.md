# TIC 407207285: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 6 distinct eclipse events in selected sectors[17, 25, 85]. The raw-event plot and numeric raw-windows.csv were inspected. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 6 same-kind midtimes give P=12.8149004912 +/-0.0000392303d, reference eclipse epoch BTJD1767.6750368, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Deciding S17 deficit peak[7, 8] vs target pixel[7, 8]; deficit-target separation2.991arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.606. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths69.282/68.374/67.489ppt, with 2 stacked events. QLP selected-kind fitted median67.187ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR3529579745461206016, P=12.8145405975+/-0.0008878672d, e=0.052468, omega=134.5472deg. Closest edge-on conjunction offset0.164534d (0.012840phase), full-SB1-covariance linear propagated Gaia uncertainty0.104311d at the measured epoch. Near-Gaia-reference projected eclipse offset0.125665d (photometric period projection allowance0.004237d). The approximate central duration36.58h vs observed median21.65h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Historical0.18d duration placed out-of-eclipse windows inside the approximately0.90d eclipse and suppressed cutout depth to6ppt. Revised21.6h extraction yields69/68/67ppt versus raw median67ppt. Updated flux budget makes all neighbors incapable (closest18.27arcsec requires253percent intrinsic eclipse). Target-centered revised deficit passes attribution; original extraction preserved. Raw fit uses0.65d baseline exclusion and free duration; no unperformed check is hidden.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 17 | 0 | 1767.6723916 | 0.010417 | 65.533 | usable; same-kind selection applies |
| 17 | 1 | 1780.4852109 | 0.010417 | 65.367 | usable; same-kind selection applies |
| 25 | 17 | 1985.5303882 | 0.010417 | 71.993 | usable; same-kind selection applies |
| 25 | 18 | 1998.3490303 | 0.010417 | 67.967 | usable; same-kind selection applies |
| 85 | 144 | 3613.0217424 | 0.001285 | 71.986 | usable; same-kind selection applies |
| 85 | 145 | 3625.8330986 | 0.001994 | 66.407 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, ../identity-check.json, shared-qlp QLP FITS; historical/diff_s17.json, historical/diff_s17.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] For TIC407207285 the deciding revised cutout is revised-cutout/diff_revised-long-window.json and .png; historical extraction remains for comparison. Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R262. [Deciding evidence](../../evidence/407207285/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
