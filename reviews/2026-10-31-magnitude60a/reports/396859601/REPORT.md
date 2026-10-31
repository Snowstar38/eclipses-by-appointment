# TIC 396859601: CONFIRMED

Full bounded review COMPLETE under current paper section2.7. Historical screened status was not an admission. Catalogue novelty is separate; central seven-group coverage applies, see ../../catalogues/coverage-matrix.csv. No exhaustive priority claim.

1. **Raw repeated eclipses: pass.** 3 directly measured raw QLP SAP events in sectors[5, 32]. Representative raw-event plots and numeric windows inspected. A local linear baseline plus free trapezoid was fitted to quality-zero cadences. Predicted centers only guide windows. Flagged/uncovered windows are not clean non-detections. At most three spread QLP sectors used; no mandatory all-event/all-sector fitting.
2. **Timing: pass with limitations below.** 2 same-kind measured times give P=16.77770105414 +/-0.00491037467d, reference eclipse epoch BTJD2179.72210646; epoch kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Historical photometric cycle branch guides association, not a fixed Gaia period fit. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. SparseS21 TIC20176241 instead uses duration/2 conservative allowance. Zero/singular timing fits are excluded; their real raw detections remain evidence. This is not a blind all-alias search.
3. **Attribution: pass at TESS image resolution with limitations below.** DecidingS32 image peak[7, 8] matches target pixel[7, 8]; target-deficit offset0.112pixel, light-deficit offset1.611arcsec; PSF total-light scaled residual0.138. Gaia identifiers/WCS validated in identity-check.json (zero pixel mismatch). Capable neighbors listed below; required eclipse is approximate Gaia-G flux budget and pixel fractional losses are blended, not intrinsic source eclipses.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut yields1x1/3x3/5x5 depths18.583/18.905/18.782ppt, 2 stacked events, versus selected-kind raw QLP median18.238ppt. Aperture dilution and mixed primary/secondary stacks may change depth. Reused numeric image and plots, cutout identity and source algorithm checked; same TESS photons test reduction robustness, not independent observing occasions.
5. **Gaia geometry: consistent within stated model limitations.** DR33258578909949773056; P=16.7849273877 +/-0.0081647730d, e=0.285924, omega=191.4077deg. Closest edge-on conjunction offset-0.376136d (-0.022409phase), full-SB1-covariance linear Gaia uncertainty1.029050d at measured epoch. Approximate central duration7.28h vs measured median2.24h permits noncentral eclipses. Mass function0.027170solar, assumed primary mass1.05, minimum companion0.382solar. This is not a detailed binary fit or an arbitrary sigma veto; correlation convention and near-reference sensitivity recorded in ../gaia-geometry.json.

**Deciding limitations:** Two S32 well-sampled events determine the reported period. A third real S5 eclipse tests recurrence across 44 cycles; its zero/singular covariance is excluded from timing. No newer timeseries sectors in current MAST query beyond5/32. Period error remains short-baseline and conditional on tested cycle branch, not precision long-baseline characterization.

**Next check:** Optional precision characterization; no missing bounded admission check.

|Sector|Historical photometric cycle|Measured midpoint BTJD|Input timing error d|Depth ppt|Usable timing before same-kind selection|
|---|---|---|---|---|---|
|5|1|1458.23946377|0.0104166|14.162|False|
|32|44|2179.72210646|0.0034722|17.486|True|
|32|45|2196.49980751|0.0034722|18.990|True|

|Capable Gaia neighbor|Separation arcsec|G|Required intrinsic fractional eclipse|Distance from deficit pixel|
|---|---|---|---|---|
|None|||||

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, historical/diff_s32.json, historical/diff_s32.png, historical/gaia.json; ../identity-check.json, ../gaia-geometry.json, ../helper-audit.md and ../SHA256SUMS.json. Original cutout: [local path omitted] QLP FITS and source paths with hashes retained in manifest. Difference events' JSON coordinates are predictions, never timing measurements. Interpretation uses bounded representative evidence rather than automatic historical screening.


Stable review key: R267. [Deciding evidence](../../evidence/396859601/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
