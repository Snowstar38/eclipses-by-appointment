# TIC 62867537: PROBABLE

Full bounded physical review: COMPLETE. Catalogue novelty is separate from this verdict.

Raw QLP SAP_FLUX contains 16 complete free-center fitted eclipses in representative sectors[56, 83]. Predicted historical centers guided extraction, not timing points. Fits use local linear baselines and trapezoid shapes; quality-zero cadences only. Flagged, partial and uncovered windows are not clean nulls. raw-events.png, raw-sector-fold.png and raw-windows.csv show the actual observations.

Measured recurrence P=2.8372050009 +/- 0.0000035438d. Named reference epoch BTJD2827.2764461: selected eclipse kind at phase zero, not an assumed deeper primary. The legacy primary_epoch_btjd column carries this epoch. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when positive-degree-of-freedom reduced chi square exceeds one. With only two centers, no reduced chi square or measured residual scatter exists; covariance propagates input timing allowances. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Consecutive same-kind measured pairs: 12. Same-sector parity and actual coverage are in alias-coverage.json. No persistent deep alternating-depth pattern in the same-sector parity arrays. Covered half-phase windows lack an eclipse comparable to the selected kind. A perfectly identical two-eclipse2P harmonic is not mathematically excluded by single-kind morphology alone; Gaia orbital association and the lack of a second comparable sequence support the reported recurrence. This is a bounded alias check, not a blind exhaustive search. Two separated sectors are distinct observing occasions on the same instrument.

Fresh raw TESScut pixel identity agrees with Gaia DR3 2164885691563277824 to 0.00000arcsec by saved WCS; all source bytes are hashed. In sector56, 9 separately recomputed event deficits average0.029px from the target. Event-scatter vector is[0.0951169563249573, 0.10623889582676811]; this is descriptive sampling scatter, not calibrated positional confidence or pixel-response systematics. Lead visually inspected the historical full-field and freshly recomputed core images. Every capable neighbor in the saved60arcsec Gaia list: Gaia 2164885687254026880: separation8.79arcsec, G16.033, intrinsic required fraction0.407, deficit distance0.402px; Gaia 2164885691563276928: separation25.37arcsec, G16.305, intrinsic required fraction0.520, deficit distance1.252px; Gaia 2164885691563276160: separation26.40arcsec, G16.235, intrinsic required fraction0.488, deficit distance1.308px; Gaia 2164879816048014848: separation31.98arcsec, G15.562, intrinsic required fraction0.269, deficit distance1.546px; Gaia 2164885897721704576: separation34.20arcsec, G16.191, intrinsic required fraction0.469, deficit distance1.696px; Gaia 2164879816048016512: separation35.38arcsec, G13.400, intrinsic required fraction0.049, deficit distance1.693px; Gaia 2164885622832174976: separation42.60arcsec, G11.017, intrinsic required fraction0.018, deficit distance2.065px; Gaia 2164885657192541824: separation43.26arcsec, G16.146, intrinsic required fraction0.451, deficit distance2.085px; Gaia 2164879816048019328: separation54.05arcsec, G13.404, intrinsic required fraction0.049, deficit distance2.594px Intrinsic source loss requirements and diluted fractional pixel losses are different quantities and are never compared as a veto. The G-band flux screen is approximate and does not exclude unknown unresolved companions.

Alternative extraction: background-subtracted raw TESScut1x1/3x3/5x5 median event depths are8.66/3.47/2.17ppt; selected QLP raw median fit depth14.00ppt. Details, windows, individual centroids, count and depths are in pixel-evidence.json. This separately extracted reduction shares the same TESS photons as QLP and is not an independent instrument or independent observing occasion. Aperture dilution, cadence and event-core averaging explain differing apparent depths; no intrinsic binary depth is inferred.

Gaia orbit and physical plausibility: source-specific NSS P=2.8372544030d, e=0.03049, omega=250.7928deg, periastron BTJD388.57332. Closest edge-on conjunction offset at the measured epoch=-0.07767d (-0.02738phase); descriptive linear full-SB1-covariance timing error=0.20597d. The covariance uses source-specific P/e/omega/Tp correlations, not only diagonal errors. Mass function=0.0027229solar; assumed primary mass=1.922solar gives minimum companion mass=0.233solar. Approximate central duration=3.79h versus observed2.32h. TIC radius/main-sequence companion assumptions and edge-on conjunction are approximations, not a fitted stellar model or arbitrary sigma admission rule. Orbit/geometry are consistent at this descriptive precision and do not establish the identity of an unresolved eclipse source.

Deciding interpretation: Real raw eclipses repeat in S15/56/83, with16 usable midpoints and12 consecutive pairs. Nine fresh S56 deficit centers average0.029px from target, so target is favored. A capable G16.03 neighbor8.79arcsec away shares the central TESS resolution element (separation0.42px); a calibrated two-source pixel response/localization uncertainty is unavailable. Deficit event scatter~0.10px and severe aperture dilution do not uniquely exclude that source. Attribution remains unresolved after completed check, so probable rather than confirmed.

Next check: Resolved eclipse photometry or calibrated two-source PRF localization of8.8arcsec pair.

Seven scoped catalogue groups were checked centrally for this identity; see ../../shared-catalogues/coverage-matrix.csv and verification receipts. A nearby catalogue source is not an exact target match, and the scoped result does not assert exhaustive publication priority.

|Sector|Photometric cycle|Measured midpoint BTJD|Input timing allowance d|Fitted depth ppt|
|---|---:|---:|---:|---:|
|56|393|2827.2736150|0.001838|15.12|
|56|394|2830.1129900|0.002239|20.62|
|56|395|2832.9516742|0.001189|14.86|
|56|396|2835.7893179|0.001204|15.21|
|56|398|2841.4617981|0.002294|13.41|
|56|399|2844.2980121|0.002187|12.93|
|56|400|2847.1358365|0.001650|14.27|
|56|401|2849.9746955|0.002059|11.88|
|56|402|2852.8129364|0.002478|12.49|
|83|652|3562.1128513|0.002827|12.78|
|83|654|3567.7842873|0.001702|13.73|
|83|655|3570.6222924|0.001810|15.32|
|83|656|3573.4614912|0.002189|15.80|
|83|657|3576.2991845|0.001643|13.63|
|83|658|3579.1380268|0.002092|15.50|
|83|659|3581.9748491|0.001696|13.58|

Evidence and provenance: measurements.json, raw-windows.csv, raw-events.png, raw-sector-fold.png, alias-coverage.json, pixel-evidence.json, pixel-recomputed.png, historical/diff_s*.json/png, historical/gaia.json; batch ../gaia-geometry.json, ../alias-audit.json, ../secondary-audit.json, ../measurement-source-receipts.json, ../download-receipts.json, ../source-hashes.json, ../LEAD-AUDIT.md and ../helper-audit.md. SHA256SUMS.json covers reports, scripts, raw FITS and original cutouts. Current availability receipt for246857844 is in shared-catalogues and copied locally with its hash. No canonical/public files were edited by this batch.
