# TIC 67300566: PROBABLE

Full bounded review COMPLETE under current paper section2.7. Historical screened status was not an admission. Catalogue novelty is separate; central seven-group coverage applies, see ../../catalogues/coverage-matrix.csv. No exhaustive priority claim.

1. **Raw repeated eclipses: pass.** 6 directly measured raw QLP SAP events in sectors[73, 86]. Representative raw-event plots and numeric windows inspected. A local linear baseline plus free trapezoid was fitted to quality-zero cadences. Predicted centers only guide windows. Flagged/uncovered windows are not clean non-detections. At most three spread QLP sectors used; no mandatory all-event/all-sector fitting.
2. **Timing: pass with limitations below.** 6 same-kind measured times give P=4.42341934165 +/-0.00002389186d, reference eclipse epoch BTJD3288.44495593; epoch kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Historical photometric cycle branch guides association, not a fixed Gaia period fit. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. SparseS21 TIC20176241 instead uses duration/2 conservative allowance. Zero/singular timing fits are excluded; their real raw detections remain evidence. This is not a blind all-alias search.
3. **Attribution: unresolved after performed check.** DecidingS59 image peak[7, 7] matches target pixel[7, 7]; target-deficit offset0.051pixel, light-deficit offset6.735arcsec; PSF total-light scaled residual0.272. Gaia identifiers/WCS validated in identity-check.json (zero pixel mismatch). Capable neighbors listed below; required eclipse is approximate Gaia-G flux budget and pixel fractional losses are blended, not intrinsic source eclipses.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut yields1x1/3x3/5x5 depths6.926/6.929/6.498ppt, 5 stacked events, versus selected-kind raw QLP median12.142ppt. Aperture dilution and mixed primary/secondary stacks may change depth. Reused numeric image and plots, cutout identity and source algorithm checked; same TESS photons test reduction robustness, not independent observing occasions.
5. **Gaia geometry: consistent within stated model limitations.** DR3189461074831319680; P=4.4238367396 +/-0.0002841869d, e=0.083592, omega=61.1479deg. Closest edge-on conjunction offset-0.147851d (-0.033421phase), full-SB1-covariance linear Gaia uncertainty0.180326d at measured epoch. Approximate central duration3.99h vs measured median1.51h permits noncentral eclipses. Mass function0.076596solar, assumed primary mass1.145, minimum companion0.620solar. This is not a detailed binary fit or an arbitrary sigma veto; correlation convention and near-reference sensitivity recorded in ../gaia-geometry.json.

**Deciding limitations:** Real repeated raw dips; capable G12.84 neighbor18.26arcsec away lies0.84pixel from deficit versus0.05pixel target offset. Uncalibrated close-source localization prevents definitive attribution; completed review retains probable.

**Next check:** Resolved eclipse photometry or calibrated multisource PRF localization.

|Sector|Historical photometric cycle|Measured midpoint BTJD|Input timing error d|Depth ppt|Usable timing before same-kind selection|
|---|---|---|---|---|---|
|73|332|3288.44445394|0.0052524|12.584|True|
|73|333|3292.86640317|0.0012004|10.033|True|
|73|334|3297.29498816|0.0013114|11.699|True|
|73|337|3310.56119791|0.0013023|13.865|True|
|86|413|3646.74348143|0.0013213|13.087|True|
|86|416|3660.01103005|0.0011574|11.173|True|

|Capable Gaia neighbor|Separation arcsec|G|Required intrinsic fractional eclipse|Distance from deficit pixel|
|---|---|---|---|---|
|189461044769259648|18.262|12.839|0.0336|0.836|
|189461010409521408|41.798|16.454|0.6516|2.058|
|189461109191746432|49.582|16.879|0.9583|2.432|
|189461044769263232|51.897|14.831|0.1544|2.462|
|189461006112498688|53.184|14.006|0.0779|2.644|

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, historical/diff_s59.json, historical/diff_s59.png, historical/gaia.json; ../identity-check.json, ../gaia-geometry.json, ../helper-audit.md and ../SHA256SUMS.json. Original cutout: [local path omitted] QLP FITS and source paths with hashes retained in manifest. Difference events' JSON coordinates are predictions, never timing measurements. Interpretation uses bounded representative evidence rather than automatic historical screening.


Stable review key: R274. [Deciding evidence](../../evidence/67300566/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
