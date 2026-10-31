# TIC 115106052: CONFIRMED

Full bounded review COMPLETE under current paper section2.7. Historical screened status was not an admission. Catalogue novelty is separate; central seven-group coverage applies, see ../../catalogues/coverage-matrix.csv. No exhaustive priority claim.

1. **Raw repeated eclipses: pass.** 15 directly measured raw QLP SAP events in sectors[1, 68, 95]. Representative raw-event plots and numeric windows inspected. A local linear baseline plus free trapezoid was fitted to quality-zero cadences. Predicted centers only guide windows. Flagged/uncovered windows are not clean non-detections. At most three spread QLP sectors used; no mandatory all-event/all-sector fitting.
2. **Timing: pass with limitations below.** 10 same-kind measured times give P=7.64111642841 +/-0.00000850037d, reference eclipse epoch BTJD1329.80183865; epoch kind: Deeper primary: odd half-period cycles. Historical photometric cycle branch guides association, not a fixed Gaia period fit. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. SparseS21 TIC20176241 instead uses duration/2 conservative allowance. Zero/singular timing fits are excluded; their real raw detections remain evidence. This is not a blind all-alias search.
3. **Attribution: pass at TESS image resolution with limitations below.** DecidingS27 image peak[7, 8] matches target pixel[7, 8]; target-deficit offset0.199pixel, light-deficit offset0.464arcsec; PSF total-light scaled residual0.237. Gaia identifiers/WCS validated in identity-check.json (zero pixel mismatch). Capable neighbors listed below; required eclipse is approximate Gaia-G flux budget and pixel fractional losses are blended, not intrinsic source eclipses.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut yields1x1/3x3/5x5 depths64.129/63.115/61.825ppt, 5 stacked events, versus selected-kind raw QLP median69.362ppt. Aperture dilution and mixed primary/secondary stacks may change depth. Reused numeric image and plots, cutout identity and source algorithm checked; same TESS photons test reduction robustness, not independent observing occasions.
5. **Gaia geometry: consistent within stated model limitations.** DR36774432193491335040; P=7.6419883813 +/-0.0004853004d, e=0.050448, omega=186.4256deg. Closest edge-on conjunction offset0.054355d (0.007113phase), full-SB1-covariance linear Gaia uncertainty0.075422d at measured epoch. Approximate central duration9.39h vs measured median5.84h permits noncentral eclipses. Mass function0.174560solar, assumed primary mass1.1, minimum companion0.882solar. This is not a detailed binary fit or an arbitrary sigma veto; correlation convention and near-reference sensitivity recorded in ../gaia-geometry.json.

**Deciding limitations:** Deeper odd half-period cycles selected:10 primary times, with independent even-cycle timing agreement. Alternating depth and center residuals support doubled orbital period; historical half-period stack mixes unequal eclipses.

**Next check:** Optional precision characterization; no missing bounded admission check.

|Sector|Historical photometric cycle|Measured midpoint BTJD|Input timing error d|Depth ppt|Usable timing before same-kind selection|
|---|---|---|---|---|---|
|1|0|1326.00783212|0.0104166|64.792|True|
|1|1|1329.80077528|0.0104166|69.532|True|
|1|2|1333.65053740|0.0104166|64.734|True|
|1|3|1337.44218674|0.0104166|69.191|True|
|1|5|1345.08288030|0.0104166|68.195|True|
|68|479|3156.02850104|0.0011574|74.991|True|
|68|480|3159.87771782|0.0011574|67.889|True|
|68|481|3163.67014168|0.0011574|73.933|True|
|68|483|3171.31072552|0.0011574|73.858|True|
|68|485|3178.95212182|0.0011574|76.796|True|
|95|670|3885.78441073|0.0011574|57.862|True|
|95|671|3889.57577389|0.0011574|64.850|True|
|95|672|3893.42574517|0.0011574|57.533|True|
|95|673|3897.21709914|0.0011574|61.629|True|
|95|675|3904.85790871|0.0011574|61.732|True|

|Capable Gaia neighbor|Separation arcsec|G|Required intrinsic fractional eclipse|Distance from deficit pixel|
|---|---|---|---|---|
|None|||||

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, historical/diff_s27.json, historical/diff_s27.png, historical/gaia.json; ../identity-check.json, ../gaia-geometry.json, ../helper-audit.md and ../SHA256SUMS.json. Original cutout: [local path omitted] QLP FITS and source paths with hashes retained in manifest. Difference events' JSON coordinates are predictions, never timing measurements. Interpretation uses bounded representative evidence rather than automatic historical screening.


Stable review key: R268. [Deciding evidence](../../evidence/115106052/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
