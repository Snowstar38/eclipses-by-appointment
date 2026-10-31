# TIC 399868192: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. Current section 2.7 five-check standard applied; historical screening is not itself admission evidence.

1. **Raw flux: pass.** 7 fitted event windows in sectors [5, 71, 98] were examined in raw-events.png and numeric raw-windows.csv. Repeated localized ingress/egress depressions and surrounding baseline were visually inspected; trapezoid fits alone are not the eclipse interpretation. QLP raw SAP_FLUX with quality zero is used for these measurements. Coverage requirements are in review_measure.py; uncovered/flagged windows are not clean nulls. At most three spread available sectors were initially selected; no mandatory all-event or all-sector analysis is implied.
2. **Measured timing: pass.** 6 same-kind measured centers give P = 6.4834644669 +/- 0.0000125529 d and reference epoch BTJD 1457.0655796. Epoch kind: Selected repeating eclipse; deeper/secondary identity not independently established. Predicted historical centers only seed windows and cycle counts, not measured timings. Within-sector recurrence/parity tests are retained in alias-audit.json; this is not an exhaustive blind alias scan. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Partial/singular fits remain documented and excluded; the epoch may denote a selected repeating eclipse rather than an independently established deeper primary.
3. **Source attribution: pass at TESS resolution.** Original cutout WCS/Gaia identity audited in pixel-audit.json. Saved sector 98 deficit-target distance 0.057 pixel; full deficit image examined against every flux-capable listed source. Capable neighbors: Gaia 3291551648758099840: separation 37.753 arcsec, required intrinsic fractional eclipse 0.1130, deficit distance 1.860 pixel; Gaia 3291551614399361152: separation 42.464 arcsec, required intrinsic fractional eclipse 0.0417, deficit distance 2.031 pixel Required intrinsic fractional eclipse and observed blended pixel fractional loss have different dilution and are not directly compared to exclude neighbors. The approximate G-band budget and saved 60 arcsec cone limit this check.
4. **Alternative reduction: pass.** Separately extracted background-subtracted target-centered TESScut 1x1/3x3/5x5 apertures show depths 29.732/24.057/11.964 ppt from 6 stacked events; current selected-kind QLP median 29.230 ppt. These are reductions of the same TESS photons, not independent observing occasions. Dilution, aperture differences and mixed primary/secondary stacks can change depth; no claim of equal intrinsic depths is made.
5. **Gaia orbital geometry: pass with limitations.** DR3 3291551648758101248, P = 6.4836906195 +/- 0.0007693937 d, e = 0.248840, omega = 343.5160 deg. Closest edge-on conjunction is offset 0.204507 d (0.031542 phase), with full SB1 covariance linear propagated uncertainty 0.176224 d at measured epoch. Projection near Gaia reference gives offset 0.241823 d; photometric period projection allowance 0.002071 d excludes covariance and model systematics. Approximate central duration 5.40 h versus fitted median 4.88 h is an illustration using TIC radius/mass and a minimum-mass main-sequence companion, not a fitted geometry. No arbitrary sigma veto; gaia-geometry.json preserves all assumptions and both conjunctions.

**Deciding interpretation and limitations:** Repeated flat-bottom eclipses across sectors 5/71/98. Sector 98 cycle 398 lacks ingress and has singular center covariance, so it is excluded from timing. Other consecutive events anchor the recurrence. Capable neighbors are at least 1.86 pixels from deficit versus target 0.057 pixel.

**Next check:** Optional resolved photometry or spectroscopy for precision characterization.

Catalogue novelty: see central ../../catalogues/coverage-matrix.csv; this report does not establish exhaustive literature priority. Current observed repeats remove a single-cycle availability question; the short-baseline cases explicitly state their evidence.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing input error d | Depth ppt | Timing status |
|---|---|---|---|---|---|
| 5 | 2 | 1457.0459022 | 0.0104168 | 32.896 | used |
| 71 | 277 | 3240.0193501 | 0.0013255 | 37.051 | used |
| 98 | 394 | 3998.5827791 | 0.0014039 | 29.239 | used |
| 98 | 396 | 4011.5511436 | 0.0011574 | 28.515 | used |
| 98 | 398 | 4024.5243308 | 304938.5784592 | 28.421 | Partially covered eclipse lacks ingress baseline; retained raw morphology but excluded timing. |
| 98 | 399 | 4031.0005506 | 0.0020469 | 29.221 | used |
| 98 | 401 | 4043.9675139 | 0.0011574 | 26.397 | used |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, historical/diff_s98.json, historical/diff_s98.png, historical/gaia.json; batch ../pixel-audit.json, ../alias-audit.json, ../gaia-geometry.json, ../helper-audit.md and ../SHA256SUMS.json. Raw cutout: [local path omitted] Historical extraction definitions: [local path omitted] and c3_sapdepth.py. Reused source hashes in source-hashes.json; no historical evidence overwritten.


Stable review key: R390. [Deciding evidence](../../2026-10-31-bright73/evidence/399868192) and [catalogue coverage](../../2026-10-31-bright73/catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../2026-10-31-bright73/evidence/399868192/measurements.json), [raw eclipse plots](../../2026-10-31-bright73/evidence/399868192/raw-events.png), [raw flux windows](../../2026-10-31-bright73/evidence/399868192/raw-windows.csv), [Gaia geometry](../../2026-10-31-bright73/analysis/batch06/gaia-geometry.json), [independent audit](../../2026-10-31-bright73/analysis/batch06/helper-audit.md), [difference image](../../2026-10-31-bright73/evidence/399868192/historical/diff_s98.png).
