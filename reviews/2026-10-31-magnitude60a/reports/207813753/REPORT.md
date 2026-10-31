# TIC 207813753: PROBABLE

Full bounded review COMPLETE under current paper section2.7. Historical screened status was not an admission. Catalogue novelty is separate; central seven-group coverage applies, see ../../catalogues/coverage-matrix.csv. No exhaustive priority claim.

1. **Raw repeated eclipses: pass.** 9 directly measured raw QLP SAP events in sectors[12, 93, 103]. Representative raw-event plots and numeric windows inspected. A local linear baseline plus free trapezoid was fitted to quality-zero cadences. Predicted centers only guide windows. Flagged/uncovered windows are not clean non-detections. At most three spread QLP sectors used; no mandatory all-event/all-sector fitting.
2. **Timing: pass with limitations below.** 9 same-kind measured times give P=5.40796620007 +/-0.00005411377d, reference eclipse epoch BTJD1648.61982916; epoch kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Historical photometric cycle branch guides association, not a fixed Gaia period fit. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. SparseS21 TIC20176241 instead uses duration/2 conservative allowance. Zero/singular timing fits are excluded; their real raw detections remain evidence. This is not a blind all-alias search.
3. **Attribution: unresolved after performed check.** DecidingS39 image peak[7, 7] matches target pixel[7, 7]; target-deficit offset0.057pixel, light-deficit offset19.218arcsec; PSF total-light scaled residual0.994. Gaia identifiers/WCS validated in identity-check.json (zero pixel mismatch). Capable neighbors listed below; required eclipse is approximate Gaia-G flux budget and pixel fractional losses are blended, not intrinsic source eclipses.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut yields1x1/3x3/5x5 depths29.314/16.217/3.548ppt, 5 stacked events, versus selected-kind raw QLP median32.832ppt. Aperture dilution and mixed primary/secondary stacks may change depth. Reused numeric image and plots, cutout identity and source algorithm checked; same TESS photons test reduction robustness, not independent observing occasions.
5. **Gaia geometry: consistent within stated model limitations.** DR35835218954421837824; P=5.4075148223 +/-0.0012803780d, e=0.091258, omega=234.4079deg. Closest edge-on conjunction offset-0.005827d (-0.001078phase), full-SB1-covariance linear Gaia uncertainty0.330001d at measured epoch. Approximate central duration8.60h vs measured median5.26h permits noncentral eclipses. Mass function0.025727solar, assumed primary mass1.03, minimum companion0.369solar. This is not a detailed binary fit or an arbitrary sigma veto; correlation convention and near-reference sensitivity recorded in ../gaia-geometry.json.

**Deciding limitations:** Completed attribution check remains unresolved:16 capable neighbors, including12.72–18.90arcsec sources. Target-centered deficit favors target but lacks calibrated multistar localization to rule out close sources. Aperture depths differ strongly in crowded field. Real repeating eclipses retained probable.

**Next check:** Resolved eclipse photometry or calibrated multisource PRF localization.

|Sector|Historical photometric cycle|Measured midpoint BTJD|Input timing error d|Depth ppt|Usable timing before same-kind selection|
|---|---|---|---|---|---|
|12|4|1648.61467421|0.0104166|32.832|True|
|93|408|3833.44014443|0.0018734|37.764|True|
|93|409|3838.85041011|0.0019785|36.879|True|
|93|410|3844.25892757|0.0021579|38.382|True|
|93|411|3849.64276890|0.0028419|30.033|True|
|103|468|4157.91521042|0.0029628|28.652|True|
|103|469|4163.32256182|0.0042963|38.422|True|
|103|470|4168.73180569|0.0019699|31.421|True|
|103|471|4174.14024031|0.0042243|32.124|True|

|Capable Gaia neighbor|Separation arcsec|G|Required intrinsic fractional eclipse|Distance from deficit pixel|
|---|---|---|---|---|
|5835218920062098176|12.720|15.251|0.4643|0.623|
|5835218954421849472|17.561|14.998|0.3747|0.899|
|5835218920062083456|18.497|15.926|0.8368|0.849|
|5835218920062093440|18.902|14.770|0.3098|0.905|
|5835218920062078080|26.681|15.336|0.4998|1.251|
|5835218920062107904|27.183|13.722|0.1382|1.339|
|5835218920029036544|28.032|15.993|0.8885|1.386|
|5835219121848729088|35.372|14.990|0.3722|1.751|
|5835220363171449344|45.581|15.547|0.5997|2.174|
|5835219126220540672|48.304|9.754|0.0352|2.347|
|5835219160580307712|48.550|14.465|0.2420|2.429|
|5835218816982865024|51.062|15.970|0.8698|2.459|
|5835218816982888832|51.759|13.948|0.1626|2.503|
|5835220431896165376|53.212|12.547|0.0683|2.623|
|5835220431896233728|54.327|15.011|0.3788|2.630|
|5835218954421880192|57.862|15.895|0.8141|2.873|

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, historical/diff_s39.json, historical/diff_s39.png, historical/gaia.json; ../identity-check.json, ../gaia-geometry.json, ../helper-audit.md and ../SHA256SUMS.json. Original cutout: [local path omitted] QLP FITS and source paths with hashes retained in manifest. Difference events' JSON coordinates are predictions, never timing measurements. Interpretation uses bounded representative evidence rather than automatic historical screening.


Stable review key: R272. [Deciding evidence](../../evidence/207813753/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
