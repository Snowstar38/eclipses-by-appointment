# TIC 403154475: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free eclipse-core fits to quality-zero raw QLP SAP_FLUX show 15 distinct eclipse events in selected sectors[102, 104]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local baseline, free depth, center, duration and ingress were fitted with a linear baseline; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 6 same-kind midtimes give P=5.0696716413 +/-0.0001354749d, reference eclipse epoch BTJD4132.0979108, kind: Even historical half-period eclipse parity; slightly deeper by sample median, physical primary unestablished. No center-covariance fits were excluded. Odd historical half-period cycles are omitted by event kind, not failed timing covariance. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Saved S95 deficit peak[8, 8] vs target pixel[8, 8]; deficit-target separation3.031arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.332. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths7.303/7.076/7.059ppt, with 10 stacked events (quality-zero data). QLP selected-kind fitted median7.954ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR36508306369040732928, P=5.0699604109+/-0.0003054710d, e=0.011145, omega=306.9271deg. Closest edge-on conjunction offset0.021105d (0.004163phase), full-SB1-covariance linear propagated Gaia uncertainty0.221143d at the measured epoch. Near-Gaia-reference projected eclipse offset0.234217d (photometric period projection allowance0.099981d). The approximate central duration6.00h vs observed median1.96h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Raw dips recur near2.535d, but Gaia orbit is5.06996d. Fit uses even half-period cycles1106,1108,1110,1112,1126,1128 as same-kind events; even median7.954ppt versus odd7.308ppt is not decisive physical-primary identification. Odd-only independent period5.0695421d agrees. Orbital5.0696716d interpretation uses same-kind parity and Gaia geometry; half-period dip recurrence is not silently called orbital period. No capable neighbor under flux-budget screen.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 102 | 1105 | 4129.5683846 | 0.001285 | 8.460 | usable, not selected (odd parity) |
| 102 | 1106 | 4132.0969361 | 0.001533 | 8.039 | selected (even parity) |
| 102 | 1107 | 4134.6360507 | 0.001819 | 7.003 | usable, not selected (odd parity) |
| 102 | 1108 | 4137.1682844 | 0.001325 | 7.527 | selected (even parity) |
| 102 | 1110 | 4142.2381538 | 0.001662 | 7.120 | selected (even parity) |
| 102 | 1111 | 4144.7767894 | 0.001526 | 7.857 | usable, not selected (odd parity) |
| 102 | 1112 | 4147.3060842 | 0.001587 | 8.399 | selected (even parity) |
| 102 | 1113 | 4149.8468381 | 0.001535 | 7.673 | usable, not selected (odd parity) |
| 104 | 1125 | 4180.2624123 | 0.001186 | 7.056 | usable, not selected (odd parity) |
| 104 | 1126 | 4182.7951689 | 0.001329 | 8.033 | selected (even parity) |
| 104 | 1127 | 4185.3338158 | 0.002088 | 6.968 | usable, not selected (odd parity) |
| 104 | 1128 | 4187.8636609 | 0.001501 | 7.876 | selected (even parity) |
| 104 | 1129 | 4190.4064294 | 0.001544 | 7.308 | usable, not selected (odd parity) |
| 104 | 1131 | 4195.4712426 | 0.001595 | 5.839 | usable, not selected (odd parity) |
| 104 | 1133 | 4200.5402226 | 0.001414 | 7.466 | usable, not selected (odd parity) |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv; shared-qlp QLP FITS; historical/diff_s95.json, historical/diff_s95.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R312. [Deciding evidence](../../evidence/403154475/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
