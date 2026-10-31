# TIC 20176241: CONFIRMED

Full bounded review COMPLETE under current paper section2.7. Historical screened status was not an admission. Catalogue novelty is separate; central seven-group coverage applies, see ../../catalogues/coverage-matrix.csv. No exhaustive priority claim.

1. **Raw repeated eclipses: pass.** 3 directly measured raw QLP SAP events in sectors[21, 48]. Representative raw-event plots and numeric windows inspected. A local linear baseline plus free trapezoid was fitted to quality-zero cadences. Predicted centers only guide windows. Flagged/uncovered windows are not clean non-detections. At most three spread QLP sectors used; no mandatory all-event/all-sector fitting.
2. **Timing: pass with limitations below.** 3 same-kind measured times give P=13.51921255715 +/-0.00106281621d, reference eclipse epoch BTJD1890.22784388; epoch kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Historical photometric cycle branch guides association, not a fixed Gaia period fit. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. SparseS21 TIC20176241 instead uses duration/2 conservative allowance. Zero/singular timing fits are excluded; their real raw detections remain evidence. This is not a blind all-alias search.
3. **Attribution: pass at TESS image resolution with limitations below.** DecidingS48 image peak[8, 7] matches target pixel[8, 7]; target-deficit offset0.095pixel, light-deficit offset1.009arcsec; PSF total-light scaled residual0.045. Gaia identifiers/WCS validated in identity-check.json (zero pixel mismatch). Capable neighbors listed below; required eclipse is approximate Gaia-G flux budget and pixel fractional losses are blended, not intrinsic source eclipses.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut yields1x1/3x3/5x5 depths80.163/80.642/79.239ppt, 2 stacked events, versus selected-kind raw QLP median85.111ppt. Aperture dilution and mixed primary/secondary stacks may change depth. Reused numeric image and plots, cutout identity and source algorithm checked; same TESS photons test reduction robustness, not independent observing occasions.
5. **Gaia geometry: consistent within stated model limitations.** DR3819970107903053312; P=13.5172019155 +/-0.0032729947d, e=0.059889, omega=16.4528deg. Closest edge-on conjunction offset0.152987d (0.011318phase), full-SB1-covariance linear Gaia uncertainty0.321871d at measured epoch. Approximate central duration6.98h vs measured median3.89h permits noncentral eclipses. Mass function0.115116solar, assumed primary mass1.08, minimum companion0.720solar. This is not a detailed binary fit or an arbitrary sigma veto; correlation convention and near-reference sensitivity recorded in ../gaia-geometry.json.

**Deciding limitations:** Two well-sampledS48 events and third clear sparseS21 recurrence test period across55cycles. S21 missing egress/sparse core gets duration/2 conservative timing allowance, not calibrated confidence. Current MAST query finds only21/48, no newer sector.

**Next check:** Optional precision characterization; no missing bounded admission check.

|Sector|Historical photometric cycle|Measured midpoint BTJD|Input timing error d|Depth ppt|Usable timing before same-kind selection|
|---|---|---|---|---|---|
|21|1|1890.22823249|0.0592790|79.842|True|
|48|55|2620.26524864|0.0034722|85.301|True|
|48|56|2633.78460652|0.0034722|85.111|True|

|Capable Gaia neighbor|Separation arcsec|G|Required intrinsic fractional eclipse|Distance from deficit pixel|
|---|---|---|---|---|
|None|||||

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, historical/diff_s48.json, historical/diff_s48.png, historical/gaia.json; ../identity-check.json, ../gaia-geometry.json, ../helper-audit.md and ../SHA256SUMS.json. Original cutout: [local path omitted] QLP FITS and source paths with hashes retained in manifest. Difference events' JSON coordinates are predictions, never timing measurements. Interpretation uses bounded representative evidence rather than automatic historical screening.


Stable review key: R275. [Deciding evidence](../../evidence/20176241/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
