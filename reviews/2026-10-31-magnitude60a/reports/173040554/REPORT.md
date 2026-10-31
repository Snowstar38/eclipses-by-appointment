# TIC 173040554: PROBABLE

Full bounded review COMPLETE under current paper section2.7. Historical screened status was not an admission. Catalogue novelty is separate; central seven-group coverage applies, see ../../catalogues/coverage-matrix.csv. No exhaustive priority claim.

1. **Raw repeated eclipses: pass.** 36 directly measured raw QLP SAP events in sectors[33, 87]. Representative raw-event plots and numeric windows inspected. A local linear baseline plus free trapezoid was fitted to quality-zero cadences. Predicted centers only guide windows. Flagged/uncovered windows are not clean non-detections. At most three spread QLP sectors used; no mandatory all-event/all-sector fitting.
2. **Timing: pass with limitations below.** 17 same-kind measured times give P=2.35330880019 +/-0.00000483332d, reference eclipse epoch BTJD2203.63257783; epoch kind: Selected even half-period conjunction; usually deeper, identity provisional. Historical photometric cycle branch guides association, not a fixed Gaia period fit. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. SparseS21 TIC20176241 instead uses duration/2 conservative allowance. Zero/singular timing fits are excluded; their real raw detections remain evidence. This is not a blind all-alias search.
3. **Attribution: unresolved after performed check.** DecidingS33 image peak[8, 8] matches target pixel[8, 8]; target-deficit offset0.369pixel, light-deficit offset17.224arcsec; PSF total-light scaled residual0.818. Gaia identifiers/WCS validated in identity-check.json (zero pixel mismatch). Capable neighbors listed below; required eclipse is approximate Gaia-G flux budget and pixel fractional losses are blended, not intrinsic source eclipses.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut yields1x1/3x3/5x5 depths3.864/2.872/1.354ppt, 20 stacked events, versus selected-kind raw QLP median6.434ppt. Aperture dilution and mixed primary/secondary stacks may change depth. Reused numeric image and plots, cutout identity and source algorithm checked; same TESS photons test reduction robustness, not independent observing occasions.
5. **Gaia geometry: consistent within stated model limitations.** DR32921782757306270080; P=2.3535060399 +/-0.0001121901d, e=0.044708, omega=342.5383deg. Closest edge-on conjunction offset-0.094204d (-0.040027phase), full-SB1-covariance linear Gaia uncertainty0.086885d at measured epoch. Approximate central duration6.29h vs measured median1.82h permits noncentral eclipses. Mass function0.115351solar, assumed primary mass1.77, minimum companion0.948solar. This is not a detailed binary fit or an arbitrary sigma veto; correlation convention and near-reference sensitivity recorded in ../gaia-geometry.json.

**Deciding limitations:** Seventeen selected even-half-cycle times; deeper ordering usually favors even but noisy shapes make primary identity provisional. Thirteen capable neighbors include13.75arcsec G13.70; centroid0.37pixel from target cannot exclude blended sources. Real raw alternating dips and orbital-period fit retained probable. Geometry phase offset-0.040 is discussed with Gaia covariance, not an automatic veto.

**Next check:** Resolved eclipse photometry or calibrated multisource PRF localization.

|Sector|Historical photometric cycle|Measured midpoint BTJD|Input timing error d|Depth ppt|Usable timing before same-kind selection|
|---|---|---|---|---|---|
|33|623|2202.45467722|0.0034723|3.536|True|
|33|624|2203.63153055|0.0034723|5.934|True|
|33|625|2204.80777236|0.0034723|5.208|True|
|33|626|2205.98544864|0.0042922|7.216|True|
|33|627|2207.16618782|0.0056696|5.103|True|
|33|628|2208.34073568|0.0034723|6.580|True|
|33|629|2209.50507888|0.0034723|4.916|True|
|33|630|2210.68565454|0.0051993|6.622|True|
|33|631|2211.86553740|0.0050984|4.987|True|
|33|632|2213.04956265|0.0034723|6.138|True|
|33|635|2216.57968852|0.0073950|5.106|True|
|33|636|2217.74892481|0.0034723|6.434|True|
|33|637|2218.93131282|0.0036913|3.924|True|
|33|638|2220.10382583|0.0064483|7.427|True|
|33|639|2221.27903720|0.0034723|4.483|True|
|33|640|2222.45910772|0.0042123|7.719|True|
|33|641|2223.63627837|0.0034723|3.959|True|
|33|642|2224.81109345|0.0069973|6.010|True|
|33|643|2225.99251302|0.0036874|7.494|True|
|33|644|2227.16911949|0.0034723|5.938|True|
|87|1867|3666.21007917|0.0060446|3.930|True|
|87|1868|3667.39163276|0.0032113|8.945|True|
|87|1869|3668.58315954|0.0102858|3.139|True|
|87|1871|3670.92014296|0.0047045|3.912|True|
|87|1872|3672.10710251|0.0020568|7.175|True|
|87|1873|3673.27522041|0.0060850|3.876|True|
|87|1874|3674.44442136|0.0015527|4.656|True|
|87|1875|3675.62415262|0.0034833|4.023|True|
|87|1879|3680.33141713|0.0063028|5.331|True|
|87|1880|3681.50391813|0.0039498|4.884|True|
|87|1881|3682.69630068|0.0050018|6.465|True|
|87|1882|3683.86279221|0.0019153|5.799|True|
|87|1883|3685.06527153|0.0056078|5.264|True|
|87|1884|3686.21837377|0.0033512|4.302|True|
|87|1885|3687.39761630|0.0029788|8.967|True|
|87|1886|3688.58147585|0.0039129|10.567|True|

|Capable Gaia neighbor|Separation arcsec|G|Required intrinsic fractional eclipse|Distance from deficit pixel|
|---|---|---|---|---|
|2921782761599913984|12.797|16.964|0.3031|0.954|
|2921782761604874368|13.754|13.698|0.0185|0.992|
|2921782692885397120|43.176|14.306|0.0296|2.471|
|2921782692885398016|44.143|17.230|0.3863|2.514|
|2921782795964604544|48.051|16.143|0.1443|2.341|
|2921782658525666944|49.379|17.681|0.5835|2.250|
|2921785613463163520|51.960|15.245|0.0652|2.199|
|2921782795964603392|54.451|17.694|0.5907|2.595|
|2921782727245128704|56.367|18.225|0.9606|2.946|
|2921782658525668736|56.924|18.166|0.9100|2.822|
|2921782795964603136|56.940|17.049|0.3277|2.878|
|2921785609164554752|57.993|12.077|0.0070|2.502|
|2921782692885396224|59.934|17.654|0.5691|3.287|

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, historical/diff_s33.json, historical/diff_s33.png, historical/gaia.json; ../identity-check.json, ../gaia-geometry.json, ../helper-audit.md and ../SHA256SUMS.json. Original cutout: [local path omitted] QLP FITS and source paths with hashes retained in manifest. Difference events' JSON coordinates are predictions, never timing measurements. Interpretation uses bounded representative evidence rather than automatic historical screening.


Stable review key: R273. [Deciding evidence](../../evidence/173040554/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
