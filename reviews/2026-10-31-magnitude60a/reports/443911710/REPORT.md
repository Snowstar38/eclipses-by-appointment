# TIC 443911710: CONFIRMED

Full bounded review COMPLETE under current paper section2.7. Historical screened status was not an admission. Catalogue novelty is separate; central seven-group coverage applies, see ../../catalogues/coverage-matrix.csv. No exhaustive priority claim.

1. **Raw repeated eclipses: pass.** 9 directly measured raw QLP SAP events in sectors[7, 46, 88]. Representative raw-event plots and numeric windows inspected. A local linear baseline plus free trapezoid was fitted to quality-zero cadences. Predicted centers only guide windows. Flagged/uncovered windows are not clean non-detections. At most three spread QLP sectors used; no mandatory all-event/all-sector fitting.
2. **Timing: pass with limitations below.** 9 same-kind measured times give P=8.34083548141 +/-0.00001306561d, reference eclipse epoch BTJD1492.60574892; epoch kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Historical photometric cycle branch guides association, not a fixed Gaia period fit. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. SparseS21 TIC20176241 instead uses duration/2 conservative allowance. Zero/singular timing fits are excluded; their real raw detections remain evidence. This is not a blind all-alias search.
3. **Attribution: pass at TESS image resolution with limitations below.** DecidingS7 image peak[8, 8] matches target pixel[8, 8]; target-deficit offset0.253pixel, light-deficit offset0.485arcsec; PSF total-light scaled residual0.355. Gaia identifiers/WCS validated in identity-check.json (zero pixel mismatch). Capable neighbors listed below; required eclipse is approximate Gaia-G flux budget and pixel fractional losses are blended, not intrinsic source eclipses.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut yields1x1/3x3/5x5 depths41.234/39.862/39.295ppt, 3 stacked events, versus selected-kind raw QLP median40.506ppt. Aperture dilution and mixed primary/secondary stacks may change depth. Reused numeric image and plots, cutout identity and source algorithm checked; same TESS photons test reduction robustness, not independent observing occasions.
5. **Gaia geometry: consistent within stated model limitations.** DR3649656340876678272; P=8.3417793302 +/-0.0013516296d, e=0.051939, omega=330.7882deg. Closest edge-on conjunction offset0.029366d (0.003520phase), full-SB1-covariance linear Gaia uncertainty0.210879d at measured epoch. Approximate central duration8.65h vs measured median5.97h permits noncentral eclipses. Mass function0.024608solar, assumed primary mass1.24, minimum companion0.405solar. This is not a detailed binary fit or an arbitrary sigma veto; correlation convention and near-reference sensitivity recorded in ../gaia-geometry.json.

**Deciding limitations:** Close2.88arcsec neighbor G16.14 requires129percent intrinsic loss under approximate Gaia-G flux budget; excluded as sole source under that assumption. TESS/G color differences are not modeled. Nine measured repeats, consistent target-centered cutout.

**Next check:** Optional precision characterization; no missing bounded admission check.

|Sector|Historical photometric cycle|Measured midpoint BTJD|Input timing error d|Depth ppt|Usable timing before same-kind selection|
|---|---|---|---|---|---|
|7|0|1492.59791575|0.0104167|40.481|True|
|7|1|1500.94079005|0.0104167|40.506|True|
|7|2|1509.28073502|0.0104167|39.159|True|
|46|128|2560.23450630|0.0034724|42.814|True|
|46|129|2568.57535963|0.0034724|42.410|True|
|46|130|2576.91510282|0.0034724|42.053|True|
|88|264|3694.58637853|0.0011574|40.061|True|
|88|265|3702.92654723|0.0011574|39.902|True|
|88|266|3711.26829171|0.0011574|40.997|True|

|Capable Gaia neighbor|Separation arcsec|G|Required intrinsic fractional eclipse|Distance from deficit pixel|
|---|---|---|---|---|
|None|||||

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, historical/diff_s07.json, historical/diff_s07.png, historical/gaia.json; ../identity-check.json, ../gaia-geometry.json, ../helper-audit.md and ../SHA256SUMS.json. Original cutout: [local path omitted] QLP FITS and source paths with hashes retained in manifest. Difference events' JSON coordinates are predictions, never timing measurements. Interpretation uses bounded representative evidence rather than automatic historical screening.


Stable review key: R269. [Deciding evidence](../../evidence/443911710/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
