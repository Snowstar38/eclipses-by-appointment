# TIC 195206508: CONFIRMED

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are separate.

1. **Raw repeated events: pass.** Quality-zero QLP SAP_FLUX contains 10 fitted representative eclipses in sectors [15, 55, 82]; 6 enter the reported timing fit. Local trapezoids have free centers, depths, durations and baselines. Predicted times guided windows only; flagged or uncovered intervals are not clean nulls. See raw-events.png, raw-windows.csv and measurements.json.
2. **Measured timing and aliases: pass.** 6 same-kind actual midpoints yield P = 13.4074536487 ± 0.0000554388 d and reference epoch BTJD 1718.7700294 (Deeper repeating eclipse, odd half-period cycles; primary by convention). Odd historical half-period cycles only; deeper repeating eclipse. Even cycles show a shallower secondary. Same-sector repeats and parity are in ../alias-audit.json. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Half/double alias assessment is bounded by representative raw morphology, not an exhaustive blind period search.
3. **Source attribution: favors target at TESS pixel resolution.** Historical sector 55 cutout places the deficit centroid 4.32 arcsec from the target; peak pixel [7, 7] versus target pixel [7, 7]. Image-model fractional residual 0.998 is not a calibrated localization error. Gaia neighbors capable under the approximate G-band flux budget: Gaia 1870085389842887808: 18.2 arcsec, G 16.013, approximate intrinsic eclipse requirement 0.405; Gaia 1870085389842888192: 24.0 arcsec, G 16.168, approximate intrinsic eclipse requirement 0.465; Gaia 1870085419893612288: 32.0 arcsec, G 14.661, approximate intrinsic eclipse requirement 0.125; Gaia 1870084801418161920: 40.4 arcsec, G 14.623, approximate intrinsic eclipse requirement 0.122; Gaia 1870085183684446336: 42.6 arcsec, G 16.907, approximate intrinsic eclipse requirement 0.906; Gaia 1870085389842895488: 43.0 arcsec, G 14.507, approximate intrinsic eclipse requirement 0.110; Gaia 1870085389842896384: 47.0 arcsec, G 16.029, approximate intrinsic eclipse requirement 0.411; Gaia 1870085149324698624: 49.8 arcsec, G 14.891, approximate intrinsic eclipse requirement 0.152; Gaia 1870085218044179712: 52.3 arcsec, G 16.164, approximate intrinsic eclipse requirement 0.463; Gaia 1870085149324696192: 55.0 arcsec, G 16.678, approximate intrinsic eclipse requirement 0.736; Gaia 1870085011885771648: 55.4 arcsec, G 14.453, approximate intrinsic eclipse requirement 0.106; Gaia 1870085114964960384: 55.6 arcsec, G 15.774, approximate intrinsic eclipse requirement 0.327; Gaia 1870085218044179584: 55.8 arcsec, G 13.824, approximate intrinsic eclipse requirement 0.065; Gaia 1870085458562377600: 57.3 arcsec, G 14.222, approximate intrinsic eclipse requirement 0.088; Gaia 1870085424202627712: 59.9 arcsec, G 16.159, approximate intrinsic eclipse requirement 0.461. The neighbor intrinsic eclipse requirement is not directly comparable to blended pixel fractional loss.
4. **Alternative reduction: pass.** Target-centered background-subtracted TESScut 1x1/3x3/5x5 aperture depths are 13.13/11.62/3.32 ppt over 4 stacked events, compared with median selected QLP raw fit depth 15.78 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Aperture dilution or mixed eclipse kinds limit depth equality. and aperture dilution or mixed eclipse kinds limit depth equality.
5. **Gaia geometry: consistent within descriptive limits.** Matched DR3 source 1870085183684452864 has P = 13.4086220195 d and e = 0.03442. The closest edge-on conjunction offset at the measured epoch is -0.14065 d (-0.01049 phase), with 0.23479 d linearly propagated full-SB1-covariance timing error. A rough central duration is 27.40 h versus observed median 10.86 h; TIC radius and minimum-mass companion are approximations, and impact parameter is not fitted.

**Deciding interpretation and limitation:** Alternating shallow even and deeper odd eclipses across S15/55/82 set a 13.407-day orbital period. The deeper odd cycles alone define the reported epoch and timing fit. The S55 cutout has a central target deficit, but high image-model residual and neighboring field stars limit subpixel localization.

**Next check:** Optional resolved eclipse imaging and refined primary/secondary modeling.

Catalogue novelty is in the central seven-group ../../shared-catalogues/coverage-matrix.csv receipt; physical classification does not assert exhaustive priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Orbital timing status |
|---|---:|---:|---:|---:|---|
| 15 | 0 | 1712.0546966 | 0.012570 | 10.16 | excluded from orbital fit (secondary) |
| 15 | 1 | 1718.7691468 | 0.010417 | 15.70 | used |
| 15 | 3 | 1732.1783285 | 0.010417 | 16.58 | used |
| 55 | 162 | 2798.0873194 | 0.004654 | 10.69 | excluded from orbital fit (secondary) |
| 55 | 163 | 2804.7689867 | 0.014417 | 20.51 | used |
| 55 | 165 | 2818.1830818 | 0.008534 | 15.26 | used |
| 82 | 272 | 3535.4816843 | 0.006814 | 12.26 | excluded from orbital fit (secondary) |
| 82 | 273 | 3542.1829509 | 0.003761 | 15.52 | used |
| 82 | 274 | 3548.8921402 | 0.004545 | 12.21 | excluded from orbital fit (secondary) |
| 82 | 275 | 3555.5919677 | 0.003868 | 15.85 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../alias-audit.json, ../gaia-geometry.json, historical/diff_s55.json, historical/diff_s55.png, historical/gaia.json and ../helper-audit.md. Original TESScut binary: [local path omitted] (hash in ../source-hashes.json). All evidence and source files are in ../SHA256SUMS.json.


Stable review key: R509. Public evidence files: [diff_s55.json](../../evidence/195206508/historical/diff_s55.json), [diff_s55.png](../../evidence/195206508/historical/diff_s55.png), [gaia.json](../../evidence/195206508/historical/gaia.json), [measurements.json](../../evidence/195206508/measurements.json), [raw-events.png](../../evidence/195206508/raw-events.png), [raw-windows.csv](../../evidence/195206508/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch10/INDEX.md). 
