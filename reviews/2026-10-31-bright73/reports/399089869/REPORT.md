# TIC 399089869: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. Current section 2.7 five-check standard applied; historical screening is not itself admission evidence.

1. **Raw flux: pass.** 5 fitted event windows in sectors [23, 46, 91] were examined in raw-events.png and numeric raw-windows.csv. Repeated localized ingress/egress depressions and surrounding baseline were visually inspected; trapezoid fits alone are not the eclipse interpretation. QLP raw SAP_FLUX with quality zero is used for these measurements. Coverage requirements are in review_measure.py; uncovered/flagged windows are not clean nulls. At most three spread available sectors were initially selected; no mandatory all-event or all-sector analysis is implied.
2. **Measured timing: pass.** 5 same-kind measured centers give P = 8.8537610758 +/- 0.0000176369 d and reference epoch BTJD 1937.8424876. Epoch kind: Selected repeating eclipse; deeper/secondary identity not independently established. Predicted historical centers only seed windows and cycle counts, not measured timings. Within-sector recurrence/parity tests are retained in alias-audit.json; this is not an exhaustive blind alias scan. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Partial/singular fits remain documented and excluded; the epoch may denote a selected repeating eclipse rather than an independently established deeper primary.
3. **Source attribution: pass at TESS resolution.** Original cutout WCS/Gaia identity audited in pixel-audit.json. Saved sector 46 deficit-target distance 0.221 pixel; full deficit image examined against every flux-capable listed source. Capable neighbors: No capable listed source within the saved 60 arcsec cone. Required intrinsic fractional eclipse and observed blended pixel fractional loss have different dilution and are not directly compared to exclude neighbors. The approximate G-band budget and saved 60 arcsec cone limit this check.
4. **Alternative reduction: pass.** Separately extracted background-subtracted target-centered TESScut 1x1/3x3/5x5 apertures show depths 106.328/108.693/103.991 ppt from 2 stacked events; current selected-kind QLP median 119.002 ppt. These are reductions of the same TESS photons, not independent observing occasions. Dilution, aperture differences and mixed primary/secondary stacks can change depth; no claim of equal intrinsic depths is made.
5. **Gaia orbital geometry: pass with limitations.** DR3 3902848326747296000, P = 8.8536629216 +/- 0.0012623065 d, e = 0.154456, omega = 84.8249 deg. Closest edge-on conjunction is offset 0.064106 d (0.007241 phase), with full SB1 covariance linear propagated uncertainty 0.229109 d at measured epoch. Projection near Gaia reference gives offset 0.046929 d; photometric period projection allowance 0.003086 d excludes covariance and model systematics. Approximate central duration 5.54 h versus fitted median 3.68 h is an illustration using TIC radius/mass and a minimum-mass main-sequence companion, not a fitted geometry. No arbitrary sigma veto; gaia-geometry.json preserves all assumptions and both conjunctions.

**Deciding interpretation and limitations:** Deep repeated isolated eclipses across sectors 23/46/91; sector 46 consecutive cycles 70/71 test recurrence. No capable neighbor in the saved 60 arcsec cone. Aperture-dependent dilution limits intrinsic depth.

**Next check:** Optional resolved photometry or spectroscopy for precision characterization.

Catalogue novelty: see central ../../catalogues/coverage-matrix.csv; this report does not establish exhaustive literature priority. Current observed repeats remove a single-cycle availability question; the short-baseline cases explicitly state their evidence.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing input error d | Depth ppt | Timing status |
|---|---|---|---|---|---|
| 23 | 0 | 1937.8436528 | 0.0104166 | 123.249 | used |
| 46 | 70 | 2557.6054165 | 0.0034726 | 120.642 | used |
| 46 | 72 | 2575.3134408 | 0.0034726 | 116.801 | used |
| 91 | 209 | 3788.2785328 | 0.0011573 | 116.881 | used |
| 91 | 210 | 3797.1323400 | 0.0011573 | 119.002 | used |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, historical/diff_s46.json, historical/diff_s46.png, historical/gaia.json; batch ../pixel-audit.json, ../alias-audit.json, ../gaia-geometry.json, ../helper-audit.md and ../SHA256SUMS.json. Raw cutout: [local path omitted] Historical extraction definitions: [local path omitted] and c3_sapdepth.py. Reused source hashes in source-hashes.json; no historical evidence overwritten.


Stable review key: R395. [Deciding evidence](../../evidence/399089869/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../evidence/399089869/measurements.json), [raw eclipse plots](../../evidence/399089869/raw-events.png), [raw flux windows](../../evidence/399089869/raw-windows.csv), [Gaia geometry](../../analysis/batch06/gaia-geometry.json), [independent audit](../../analysis/batch06/helper-audit.md), [difference image](../../evidence/399089869/historical/diff_s46.png).
