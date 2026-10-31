# TIC 144113939: CONFIRMED

Full bounded review COMPLETE under current paper section2.7. Historical screened status was not an admission. Catalogue novelty is separate; central seven-group coverage applies, see ../../catalogues/coverage-matrix.csv. No exhaustive priority claim.

1. **Raw repeated eclipses: pass.** 4 directly measured raw QLP SAP events in sectors[64, 101]. Representative raw-event plots and numeric windows inspected. A local linear baseline plus free trapezoid was fitted to quality-zero cadences. Predicted centers only guide windows. Flagged/uncovered windows are not clean non-detections. At most three spread QLP sectors used; no mandatory all-event/all-sector fitting.
2. **Timing: pass with limitations below.** 4 same-kind measured times give P=11.78879640721 +/-0.00001285928d, reference eclipse epoch BTJD3046.67692883; epoch kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Historical photometric cycle branch guides association, not a fixed Gaia period fit. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. SparseS21 TIC20176241 instead uses duration/2 conservative allowance. Zero/singular timing fits are excluded; their real raw detections remain evidence. This is not a blind all-alias search.
3. **Attribution: pass at TESS image resolution with limitations below.** DecidingS37 image peak[8, 7] matches target pixel[8, 7]; target-deficit offset0.135pixel, light-deficit offset2.607arcsec; PSF total-light scaled residual0.442. Gaia identifiers/WCS validated in identity-check.json (zero pixel mismatch). Capable neighbors listed below; required eclipse is approximate Gaia-G flux budget and pixel fractional losses are blended, not intrinsic source eclipses.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut yields1x1/3x3/5x5 depths36.457/35.553/33.835ppt, 2 stacked events, versus selected-kind raw QLP median35.558ppt. Aperture dilution and mixed primary/secondary stacks may change depth. Reused numeric image and plots, cutout identity and source algorithm checked; same TESS photons test reduction robustness, not independent observing occasions.
5. **Gaia geometry: consistent within stated model limitations.** DR36146876276851999104; P=11.7889746135 +/-0.0024534753d, e=0.061265, omega=283.7125deg. Closest edge-on conjunction offset-0.011443d (-0.000971phase), full-SB1-covariance linear Gaia uncertainty0.581526d at measured epoch. Approximate central duration5.96h vs measured median3.13h permits noncentral eclipses. Mass function0.108096solar, assumed primary mass0.96, minimum companion0.656solar. This is not a detailed binary fit or an arbitrary sigma veto; correlation convention and near-reference sensitivity recorded in ../gaia-geometry.json.

**Deciding limitations:** One capable neighbor38.54arcsec away is separated from target-centered deficit. Four raw repeated events span sectors64/101; alternative historicalS37 provides earlier reduction evidence.

**Next check:** Optional precision characterization; no missing bounded admission check.

|Sector|Historical photometric cycle|Measured midpoint BTJD|Input timing error d|Depth ppt|Usable timing before same-kind selection|
|---|---|---|---|---|---|
|64|125|3046.67659151|0.0011574|36.741|True|
|64|126|3058.46606543|0.0011574|36.006|True|
|101|215|4107.66868332|0.0011574|35.110|True|
|101|216|4119.45732116|0.0011574|32.241|True|

|Capable Gaia neighbor|Separation arcsec|G|Required intrinsic fractional eclipse|Distance from deficit pixel|
|---|---|---|---|---|
|6146876242492663808|38.543|15.351|0.5114|1.787|

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, historical/diff_s37.json, historical/diff_s37.png, historical/gaia.json; ../identity-check.json, ../gaia-geometry.json, ../helper-audit.md and ../SHA256SUMS.json. Original cutout: [local path omitted] QLP FITS and source paths with hashes retained in manifest. Difference events' JSON coordinates are predictions, never timing measurements. Interpretation uses bounded representative evidence rather than automatic historical screening.


Stable review key: R270. [Deciding evidence](../../evidence/144113939/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
