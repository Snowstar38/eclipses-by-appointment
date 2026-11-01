# TIC 102052526: CONFIRMED

Full bounded review: **COMPLETE**. This physical outcome is separate from catalogue novelty and from the historical screening label.

1. **Raw repeat:** 8 measured same-kind eclipses in representative QLP SAP_FLUX sectors [9, 63, 99]; raw flux, quality filtering, fitted windows and plots are retained. Fitted periodic depressions alone would be insufficient: the inspected windows have recurring eclipse morphology. Predicted centers were search guides, never timing points. Flagged or unresolved windows are not clean nulls.
2. **Timing and aliases:** measured midpoints give P = 7.4120614461 ± 0.0000108580 d and reference BTJD 1548.6197006 (Deeper repeating eclipse; even half-period cycles). Same-kind within-sector counts and parity are in ../alias-audit.json. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check rather than a blind exhaustive search.
3. **Attribution:** historical S63 TESScut deficit lies 2.66 arcsec from the target coordinate; peak pixel [7, 8] and target pixel [7, 7]. Image-model fractional residual 0.997 is not a calibrated position error. Capable Gaia neighbors: None within 60 arcsec under the approximate G-band flux budget. The intrinsic neighbor requirement is not the same as the blended pixel loss.
4. **Alternative reduction:** independent target-centered background-subtracted TESScut 1x1/3x3/5x5 aperture extraction gives 59.76/24.22/6.56 ppt in 6 stacked events; selected QLP raw depth is 195.82 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Aperture dilution, event-kind mixing and temporal changes limit a direct depth comparison.
5. **Gaia geometry:** matched DR3 source 5416772041726772864 has SB1 period 7.4112548348 d, e = 0.01800. The closest edge-on conjunction differs from the measured eclipse epoch by 0.14870 d (0.02006 phase); the linear propagated timing scale from source-specific full SB1 covariance is 0.05727 d. Rough central duration 8.59 h versus measured median 6.72 h uses TIC radius and a minimum-mass main-sequence companion; it is not a physical fit or a sigma veto.

**Deciding interpretation and limitations:** Deep and shallow events alternate in S9/63/99. The 3.706-day photometric half-period is not the orbital period: the deeper even parity recurs at 7.412 days. The historical S63 aperture depths are strongly diluted and its image-model residual is high, but the deficit core is on the target and no capable Gaia neighbor is found.

**Next check:** Optional resolved photometry or spectroscopy for precision binary parameters; no bounded admission check remains missing.

Catalogue novelty: the central seven-group check in ../../shared-catalogues/coverage-matrix.csv reports complete scoped coverage and no identified prior eclipsing-binary match for this exact target. This is not exhaustive priority and does not resolve embargoed identities.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 9 | 0 | 1548.6186004 | 0.010417 | 199.47 | used |
| 9 | 3 | 1559.7334572 | 0.010417 | 147.91 | excluded from primary timing |
| 9 | 4 | 1563.4400284 | 0.010417 | 200.76 | used |
| 9 | 5 | 1567.1466206 | 0.010417 | 122.32 | excluded from primary timing |
| 63 | 396 | 3016.2076632 | 0.001257 | 196.25 | used |
| 63 | 397 | 3019.9129756 | 0.002086 | 151.54 | excluded from primary timing |
| 63 | 398 | 3023.6202250 | 0.001414 | 207.16 | used |
| 63 | 399 | 3027.3144753 | 0.007049 | 118.26 | excluded from primary timing |
| 63 | 400 | 3031.0310660 | 0.001157 | 195.39 | used |
| 63 | 401 | 3034.7348220 | 0.002138 | 155.44 | excluded from primary timing |
| 63 | 402 | 3038.4460476 | 0.001594 | 186.63 | used |
| 99 | 675 | 4050.1876910 | 0.002411 | 116.43 | excluded from primary timing |
| 99 | 676 | 4053.8959706 | 0.003968 | 150.78 | used |
| 99 | 679 | 4065.0094469 | 0.001528 | 158.59 | excluded from primary timing |
| 99 | 680 | 4068.7204943 | 0.001582 | 145.49 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../gaia-geometry.json, ../alias-audit.json, historical/diff_s63.json, historical/diff_s63.png and historical/gaia.json. Original TESScut binary: [local path omitted] (hash in ../source-hashes.json). Source code and retained evidence are covered by ../SHA256SUMS.json.


Stable review key: R461. Public evidence files: [diff_s63.json](../../evidence/102052526/historical/diff_s63.json), [diff_s63.png](../../evidence/102052526/historical/diff_s63.png), [gaia.json](../../evidence/102052526/historical/gaia.json), [measurements.json](../../evidence/102052526/measurements.json), [raw-events.png](../../evidence/102052526/raw-events.png), [raw-windows.csv](../../evidence/102052526/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch06/INDEX.md). 
