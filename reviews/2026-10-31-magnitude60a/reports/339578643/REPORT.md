# TIC 339578643: CONFIRMED

Full bounded review COMPLETE under current paper section2.7. Historical screened status was not an admission. Catalogue novelty is separate; central seven-group coverage applies, see ../../catalogues/coverage-matrix.csv. No exhaustive priority claim.

1. **Raw repeated eclipses: pass.** 4 directly measured raw QLP SAP events in sectors[95, 103]. Representative raw-event plots and numeric windows inspected. A local linear baseline plus free trapezoid was fitted to quality-zero cadences. Predicted centers only guide windows. Flagged/uncovered windows are not clean non-detections. At most three spread QLP sectors used; no mandatory all-event/all-sector fitting.
2. **Timing: pass with limitations below.** 4 same-kind measured times give P=7.13460231510 +/-0.00003044773d, reference eclipse epoch BTJD3886.00718979; epoch kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Historical photometric cycle branch guides association, not a fixed Gaia period fit. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. SparseS21 TIC20176241 instead uses duration/2 conservative allowance. Zero/singular timing fits are excluded; their real raw detections remain evidence. This is not a blind all-alias search.
3. **Attribution: pass at TESS image resolution with limitations below.** DecidingS102 image peak[8, 7] matches target pixel[8, 7]; target-deficit offset0.168pixel, light-deficit offset1.974arcsec; PSF total-light scaled residual0.382. Gaia identifiers/WCS validated in identity-check.json (zero pixel mismatch). Capable neighbors listed below; required eclipse is approximate Gaia-G flux budget and pixel fractional losses are blended, not intrinsic source eclipses.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut yields1x1/3x3/5x5 depths31.120/30.815/29.768ppt, 4 stacked events, versus selected-kind raw QLP median27.000ppt. Aperture dilution and mixed primary/secondary stacks may change depth. Reused numeric image and plots, cutout identity and source algorithm checked; same TESS photons test reduction robustness, not independent observing occasions.
5. **Gaia geometry: consistent within stated model limitations.** DR36494385074364232576; P=7.1343937492 +/-0.0007271545d, e=0.040070, omega=215.9747deg. Closest edge-on conjunction offset0.004981d (0.000698phase), full-SB1-covariance linear Gaia uncertainty0.330956d at measured epoch. Approximate central duration5.85h vs measured median2.83h permits noncentral eclipses. Mass function0.055553solar, assumed primary mass1.03, minimum companion0.509solar. This is not a detailed binary fit or an arbitrary sigma veto; correlation convention and near-reference sensitivity recorded in ../gaia-geometry.json.

**Deciding limitations:** Four raw events in sectors95/103; target-centeredS102 cutout supports separate reduction. No capable neighbor within60arcsec.

**Next check:** Optional precision characterization; no missing bounded admission check.

|Sector|Historical photometric cycle|Measured midpoint BTJD|Input timing error d|Depth ppt|Usable timing before same-kind selection|
|---|---|---|---|---|---|
|95|358|3886.00669743|0.0011574|24.460|True|
|95|359|3893.14230193|0.0011574|24.386|True|
|103|396|4157.12190663|0.0011574|30.801|True|
|103|397|4164.25683375|0.0011574|29.539|True|

|Capable Gaia neighbor|Separation arcsec|G|Required intrinsic fractional eclipse|Distance from deficit pixel|
|---|---|---|---|---|
|None|||||

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, historical/diff_s102.json, historical/diff_s102.png, historical/gaia.json; ../identity-check.json, ../gaia-geometry.json, ../helper-audit.md and ../SHA256SUMS.json. Original cutout: [local path omitted] QLP FITS and source paths with hashes retained in manifest. Difference events' JSON coordinates are predictions, never timing measurements. Interpretation uses bounded representative evidence rather than automatic historical screening.


Stable review key: R271. [Deciding evidence](../../evidence/339578643/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
