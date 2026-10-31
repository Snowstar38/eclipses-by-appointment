# TIC 387275908: CONFIRMED

Full bounded review COMPLETE under current paper section2.7. Historical screened status was not an admission. Catalogue novelty is separate; central seven-group coverage applies, see ../../catalogues/coverage-matrix.csv. No exhaustive priority claim.

1. **Raw repeated eclipses: pass.** 10 directly measured raw QLP SAP events in sectors[46, 87]. Representative raw-event plots and numeric windows inspected. A local linear baseline plus free trapezoid was fitted to quality-zero cadences. Predicted centers only guide windows. Flagged/uncovered windows are not clean non-detections. At most three spread QLP sectors used; no mandatory all-event/all-sector fitting.
2. **Timing: pass with limitations below.** 10 same-kind measured times give P=4.39055204155 +/-0.00001165698d, reference eclipse epoch BTJD2556.19633037; epoch kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Historical photometric cycle branch guides association, not a fixed Gaia period fit. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. SparseS21 TIC20176241 instead uses duration/2 conservative allowance. Zero/singular timing fits are excluded; their real raw detections remain evidence. This is not a blind all-alias search.
3. **Attribution: pass at TESS image resolution with limitations below.** DecidingS72 image peak[8, 8] matches target pixel[8, 8]; target-deficit offset0.097pixel, light-deficit offset6.110arcsec; PSF total-light scaled residual0.823. Gaia identifiers/WCS validated in identity-check.json (zero pixel mismatch). Capable neighbors listed below; required eclipse is approximate Gaia-G flux budget and pixel fractional losses are blended, not intrinsic source eclipses.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut yields1x1/3x3/5x5 depths7.102/7.464/6.359ppt, 6 stacked events, versus selected-kind raw QLP median8.059ppt. Aperture dilution and mixed primary/secondary stacks may change depth. Reused numeric image and plots, cutout identity and source algorithm checked; same TESS photons test reduction robustness, not independent observing occasions.
5. **Gaia geometry: consistent within stated model limitations.** DR33166138805578006016; P=4.3913179458 +/-0.0006353543d, e=0.075001, omega=354.8170deg. Closest edge-on conjunction offset-0.257200d (-0.058570phase), full-SB1-covariance linear Gaia uncertainty0.254946d at measured epoch. Approximate central duration6.45h vs measured median2.15h permits noncentral eclipses. Mass function0.058270solar, assumed primary mass1.17, minimum companion0.558solar. This is not a detailed binary fit or an arbitrary sigma veto; correlation convention and near-reference sensitivity recorded in ../gaia-geometry.json.

**Deciding limitations:** Capable neighbors27.34 and36.11arcsec are spatially separated from deficit0.10pixel from target. High total-light PSF residual0.823 reflects crowding and is not used alone as attribution evidence. Gaia phase offset-0.059 has covariance uncertainty0.255d; duration can be noncentral.

**Next check:** Optional precision characterization; no missing bounded admission check.

|Sector|Historical photometric cycle|Measured midpoint BTJD|Input timing error d|Depth ppt|Usable timing before same-kind selection|
|---|---|---|---|---|---|
|46|242|2556.19705006|0.0034724|7.880|True|
|46|243|2560.58516895|0.0034724|8.081|True|
|46|245|2569.37245514|0.0034724|7.755|True|
|46|246|2573.75689717|0.0034724|6.815|True|
|46|247|2578.14744976|0.0034724|8.541|True|
|87|495|3667.00062154|0.0016082|8.037|True|
|87|496|3671.39959704|0.0018368|8.965|True|
|87|497|3675.78973554|0.0017435|8.526|True|
|87|498|3680.17549709|0.0020934|7.428|True|
|87|499|3684.57163960|0.0020927|8.546|True|

|Capable Gaia neighbor|Separation arcsec|G|Required intrinsic fractional eclipse|Distance from deficit pixel|
|---|---|---|---|---|
|3166139119111943424|27.344|16.766|0.5694|1.397|
|3166138741154825728|36.107|15.699|0.2177|1.758|

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, historical/diff_s72.json, historical/diff_s72.png, historical/gaia.json; ../identity-check.json, ../gaia-geometry.json, ../helper-audit.md and ../SHA256SUMS.json. Original cutout: [local path omitted] QLP FITS and source paths with hashes retained in manifest. Difference events' JSON coordinates are predictions, never timing measurements. Interpretation uses bounded representative evidence rather than automatic historical screening.


Stable review key: R276. [Deciding evidence](../../evidence/387275908/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
