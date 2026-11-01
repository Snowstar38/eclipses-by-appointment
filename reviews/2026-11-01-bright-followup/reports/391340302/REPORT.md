# TIC 391340302: PROBABLE

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are separate.

1. **Raw repeated events: pass.** Quality-zero QLP SAP_FLUX contains 14 fitted representative eclipses in sectors [10, 11, 38, 90]; 14 enter the reported timing fit. Local trapezoids have free centers, depths, durations and baselines. Predicted times guided windows only; flagged or uncovered intervals are not clean nulls. See raw-events.png, raw-windows.csv and measurements.json.
2. **Measured timing and aliases: pass.** 14 same-kind actual midpoints yield P = 6.4566398472 ± 0.0000072175 d and reference epoch BTJD 1575.9846204 (Selected repeating eclipse; primary by convention; deeper/secondary identity not independently established). All timing-usable historical photometric cycles; representative parity shows no persistent unequal alternation. Same-sector repeats and parity are in ../alias-audit.json. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Half/double alias assessment is bounded by representative raw morphology, not an exhaustive blind period search.
3. **Source attribution: unresolved.** Historical sector 11 cutout places the deficit centroid 3.98 arcsec from the target; peak pixel [7, 7] versus target pixel [7, 7]. Image-model fractional residual 0.890 is not a calibrated localization error. Gaia neighbors capable under the approximate G-band flux budget: Gaia 5239465552568592768: 6.1 arcsec, G 13.331, approximate intrinsic eclipse requirement 0.087; Gaia 5239465518208831104: 35.1 arcsec, G 15.493, approximate intrinsic eclipse requirement 0.487; Gaia 5239453801538064640: 35.2 arcsec, G 15.421, approximate intrinsic eclipse requirement 0.457; Gaia 5239465518208825984: 46.9 arcsec, G 16.057, approximate intrinsic eclipse requirement 0.802; Gaia 5239453767178311808: 51.5 arcsec, G 15.422, approximate intrinsic eclipse requirement 0.457; Gaia 5239454175171527424: 56.3 arcsec, G 15.756, approximate intrinsic eclipse requirement 0.614. The neighbor intrinsic eclipse requirement is not directly comparable to blended pixel fractional loss.
4. **Alternative reduction: supports recurring loss with unresolved host.** Target-centered background-subtracted TESScut 1x1/3x3/5x5 aperture depths are 19.49/19.83/18.92 ppt over 4 stacked events, compared with median selected QLP raw fit depth 23.22 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Aperture dilution or mixed eclipse kinds limit depth equality. and aperture dilution or mixed eclipse kinds limit depth equality.
5. **Gaia geometry: consistent within descriptive limits.** Matched DR3 source 5239465548244669952 has P = 6.4572634522 d and e = 0.10891. The closest edge-on conjunction offset at the measured epoch is -0.08325 d (-0.01289 phase), with 0.16381 d linearly propagated full-SB1-covariance timing error. A rough central duration is 7.18 h versus observed median 7.04 h; TIC radius and minimum-mass companion are approximations, and impact parameter is not fitted.

**Deciding interpretation and limitation:** The S11 difference image centers on the target pixel, but a Gaia neighbor 6.1 arcsec away lies in that same TESS core and can produce the observed loss. TESS pixels cannot assign the eclipses uniquely.

**Next check:** Resolved eclipse photometry of the 6.1-arcsec pair.

Catalogue novelty is in the central seven-group ../../shared-catalogues/coverage-matrix.csv receipt; physical classification does not assert exhaustive priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Orbital timing status |
|---|---:|---:|---:|---:|---|
| 10 | 0 | 1575.9846232 | 0.010417 | 23.90 | used |
| 10 | 2 | 1588.8979173 | 0.010417 | 23.10 | used |
| 11 | 4 | 1601.8110937 | 0.010417 | 23.20 | used |
| 11 | 5 | 1608.2682354 | 0.010417 | 22.15 | used |
| 11 | 6 | 1614.7223332 | 0.010417 | 23.13 | used |
| 11 | 7 | 1621.1823670 | 0.010417 | 22.23 | used |
| 38 | 118 | 2337.8680384 | 0.003472 | 24.38 | used |
| 38 | 119 | 2344.3247065 | 0.003472 | 23.83 | used |
| 38 | 120 | 2350.7815131 | 0.003472 | 23.58 | used |
| 38 | 121 | 2357.2381694 | 0.003472 | 24.48 | used |
| 90 | 337 | 3751.8699430 | 0.001301 | 22.87 | used |
| 90 | 338 | 3758.3315202 | 0.001186 | 23.05 | used |
| 90 | 339 | 3764.7857257 | 0.001157 | 24.18 | used |
| 90 | 340 | 3771.2406614 | 0.001513 | 23.25 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../alias-audit.json, ../gaia-geometry.json, historical/diff_s11.json, historical/diff_s11.png, historical/gaia.json and ../helper-audit.md. Original TESScut binary: [local path omitted] (hash in ../source-hashes.json). All evidence and source files are in ../SHA256SUMS.json.


Stable review key: R500. Public evidence files: [diff_s11.json](../../evidence/391340302/historical/diff_s11.json), [diff_s11.png](../../evidence/391340302/historical/diff_s11.png), [gaia.json](../../evidence/391340302/historical/gaia.json), [measurements.json](../../evidence/391340302/measurements.json), [raw-events.png](../../evidence/391340302/raw-events.png), [raw-windows.csv](../../evidence/391340302/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch10/INDEX.md). 
