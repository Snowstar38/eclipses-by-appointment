# TIC 399285183: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. Current section 2.7 five-check standard applied; historical screening is not itself admission evidence.

1. **Raw flux: pass.** 7 fitted event windows in sectors [54, 81] were examined in raw-events.png and numeric raw-windows.csv. Repeated localized ingress/egress depressions and surrounding baseline were visually inspected; trapezoid fits alone are not the eclipse interpretation. QLP raw SAP_FLUX with quality zero is used for these measurements. Coverage requirements are in review_measure.py; uncovered/flagged windows are not clean nulls. At most three spread available sectors were initially selected; no mandatory all-event or all-sector analysis is implied.
2. **Measured timing: pass.** 7 same-kind measured centers give P = 3.8060033593 +/- 0.0000370371 d and reference epoch BTJD 2771.5481179. Epoch kind: Selected repeating eclipse; deeper/secondary identity not independently established. Predicted historical centers only seed windows and cycle counts, not measured timings. Within-sector recurrence/parity tests are retained in alias-audit.json; this is not an exhaustive blind alias scan. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Partial/singular fits remain documented and excluded; the epoch may denote a selected repeating eclipse rather than an independently established deeper primary.
3. **Source attribution: pass at TESS resolution.** Original cutout WCS/Gaia identity audited in pixel-audit.json. Saved sector 81 deficit-target distance 0.142 pixel; full deficit image examined against every flux-capable listed source. Capable neighbors: Gaia 4242940643455267968: separation 26.034 arcsec, required intrinsic fractional eclipse 0.3477, deficit distance 1.135 pixel; Gaia 4242937654158029312: separation 38.743 arcsec, required intrinsic fractional eclipse 0.2899, deficit distance 1.942 pixel Required intrinsic fractional eclipse and observed blended pixel fractional loss have different dilution and are not directly compared to exclude neighbors. The approximate G-band budget and saved 60 arcsec cone limit this check.
4. **Alternative reduction: pass.** Separately extracted background-subtracted target-centered TESScut 1x1/3x3/5x5 apertures show depths 12.498/11.543/10.458 ppt from 6 stacked events; current selected-kind QLP median 13.833 ppt. These are reductions of the same TESS photons, not independent observing occasions. Dilution, aperture differences and mixed primary/secondary stacks can change depth; no claim of equal intrinsic depths is made.
5. **Gaia orbital geometry: pass with limitations.** DR3 4242940643455270144, P = 3.8059045398 +/- 0.0002783071 d, e = 0.147943, omega = 124.5770 deg. Closest edge-on conjunction is offset 0.034084 d (0.008956 phase), with full SB1 covariance linear propagated uncertainty 0.161791 d at measured epoch. Projection near Gaia reference gives offset -0.027777 d; photometric period projection allowance 0.023185 d excludes covariance and model systematics. Approximate central duration 5.16 h versus fitted median 3.05 h is an illustration using TIC radius/mass and a minimum-mass main-sequence companion, not a fitted geometry. No arbitrary sigma veto; gaia-geometry.json preserves all assumptions and both conjunctions.

**Deciding interpretation and limitations:** Seven repeated localized shallow eclipses, with clean flat surrounding baseline in sector 81 and consecutive measured cycles. Capable neighbors are at least 1.135 pixels from the deficit versus target 0.142 pixel.

**Next check:** Optional resolved photometry or spectroscopy for precision characterization.

Catalogue novelty: see central ../../catalogues/coverage-matrix.csv; this report does not establish exhaustive literature priority. Current observed repeats remove a single-cycle availability question; the short-baseline cases explicitly state their evidence.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing input error d | Depth ppt | Timing status |
|---|---|---|---|---|---|
| 54 | 0 | 2771.5475403 | 0.0069444 | 15.721 | used |
| 81 | 194 | 3509.9142646 | 0.0011574 | 13.839 | used |
| 81 | 195 | 3513.7191080 | 0.0014885 | 13.833 | used |
| 81 | 197 | 3521.3289178 | 0.0011574 | 13.503 | used |
| 81 | 198 | 3525.1358128 | 0.0014356 | 13.468 | used |
| 81 | 199 | 3528.9429709 | 0.0018431 | 14.612 | used |
| 81 | 200 | 3532.7502021 | 0.0016008 | 13.555 | used |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, historical/diff_s81.json, historical/diff_s81.png, historical/gaia.json; batch ../pixel-audit.json, ../alias-audit.json, ../gaia-geometry.json, ../helper-audit.md and ../SHA256SUMS.json. Raw cutout: [local path omitted] Historical extraction definitions: [local path omitted] and c3_sapdepth.py. Reused source hashes in source-hashes.json; no historical evidence overwritten.


Stable review key: R389. [Deciding evidence](../../evidence/399285183/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../evidence/399285183/measurements.json), [raw eclipse plots](../../evidence/399285183/raw-events.png), [raw flux windows](../../evidence/399285183/raw-windows.csv), [Gaia geometry](../../analysis/batch06/gaia-geometry.json), [independent audit](../../analysis/batch06/helper-audit.md), [difference image](../../evidence/399285183/historical/diff_s81.png).
