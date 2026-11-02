# TIC 374606776

Physical verdict: **probable**. Full bounded review: **complete**.

Repeated deep raw eclipses are secure, though individual noisy/gapped events have less reliable trapezoid centers. The target deficit overlaps capable neighbors at17.6/21.6 arcsec (less than or about one TESS pixel), plus the bright G10.8 neighbor22.2 arcsec away. Spatial morphology favors the target but does not decisively reject all capable close sources; retain probable attribution.

Measured period 8.85580116464 +/- 2.1865495e-05 d; named selected-eclipse epoch BTJD 1800.18062905; depth 26.59841 ppt (diluted raw QLP). Epoch is the selected recurring eclipse, not an assumed deeper primary. BTJD = BJD_TDB -2457000.

Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.

Timing samples: 8; sectors [18, 58, 85]; fitted same-kind cycle span 0 to 207. Reduced chi square: 1.1737374084112286. Actual centers, errors and local windows are in [measurements.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/374606776/measurements.json) and [raw-windows.csv](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/374606776/raw-windows.csv); predicted centers are labeled and never counted as measurements.

Aliases: within-sector adjacent same-kind pairs [[18, 0, 1], [58, 123, 124], [58, 124, 125], [85, 205, 206], [85, 206, 207]]. Sector parity depths and nearby integer counts are in [../alias-audit.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/alias-audit.json) and [../integer-aliases.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/integer-aliases.json). Half-period extra windows are in [../coverage-alias-windows.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/coverage-alias-windows.json); flagged/empty windows are not nulls. No persistent unequal alternating primary depths support a doubled period. Gaia period is a consistency test, not a fixed photometric fit.

Secondary assessment: {'status': 'No secure secondary established by visual review of full raw phase and predicted-conjunction windows. Baseline variability/coverage limit a null claim; guess is Gaia-predicted separation, not a measured secondary phase.', 'guess_phase': 0.5027542082545045}

Attribution and alternative reduction: fresh TESScut S58 stacks 2 well-covered target-period eclipses. Target WCS pixel [7.735897730512072, 7.911700008583637]; deficit centroid [7.893809124844426, 7.870893246386292]. Read [fresh-pixels/diff_fresh.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/374606776/fresh-pixels/diff_fresh.png) against every capable neighbor below. No fixed centroid threshold applied. Target-centered custom background-subtracted1x1/3x3/5x5 extraction depths are 12.0307/4.1228/3.5205 ppt. This is a separate reduction of the same TESS photons, not independent observations; different sectors are different occasions on one instrument. Source FITS identities and SHA256 hashes are in [../identity-check.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/identity-check.json) and [../source-hashes.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/source-hashes.json).

All capable neighbors within60 arcsec (G-band flux-ratio proxy; intrinsic required depth is not directly compared to diluted pixel loss): [{"source_id": "507046938282627584", "sep": 17.552827467644438, "G": 16.267841, "depth_needed": 0.8658359515900378, "possible": true, "px": [6.958882064915956, 8.209172249272271], "frac_loss_at_pixel": 0.014195749978632079}, {"source_id": "507046938281802112", "sep": 21.601346080805463, "G": 16.10722, "depth_needed": 0.7504282833904787, "possible": true, "px": [7.143570571996502, 8.745269859120807], "frac_loss_at_pixel": 0.010097954335560641}, {"source_id": "507043983344306048", "sep": 22.205015783194398, "G": 10.771246, "depth_needed": 0.031910275036079405, "possible": true, "px": [8.281313352623584, 7.013348811402841], "frac_loss_at_pixel": 0.0018805199116676006}, {"source_id": "507043983345129216", "sep": 26.310424040185577, "G": 15.426095, "depth_needed": 0.413131344515239, "possible": true, "px": [7.764886924965584, 6.668103493891229], "frac_loss_at_pixel": 0.0018805199116676006}, {"source_id": "507043983345129344", "sep": 27.78660520563944, "G": 15.761854, "depth_needed": 0.5532096244545974, "possible": true, "px": [8.148122803827341, 6.663638869266165], "frac_loss_at_pixel": 0.0018805199116676006}, {"source_id": "507046938282624384", "sep": 34.17244928482854, "G": 13.117002, "depth_needed": 0.07268231970877366, "possible": true, "px": [8.342912847039056, 9.409059578334325], "frac_loss_at_pixel": 0.006797815756623012}]

Gaia source 507046938281803392: source-specific NSS period 8.8541081525 d; eccentricity 0.02267; nearest edge-on conjunction offset 0.27115 d (phase 0.03062), linear full-covariance error 0.23434 d. Source-specific covariance, mass function, assumed masses/radii and approximate central duration are in [../gaia-geometry.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/gaia-geometry.json). This is not a hard phase veto or fitted inclination. Observed duration 2.766 h, approximate central duration 6.881 h; grazing geometry/dilution and radius assumptions can shorten the eclipse. No contradiction that invalidates repeated-eclipse interpretation is established.

Catalogue outcome: no identified prior EB; seven-group coverage yes. Shared coverage-matrix and catalogue receipts support scope only, not exhaustive priority. Physical verdict is separate from novelty.

Limitations: Representative sectors and simplified trapezoid/linear timing errors; shared TESS photons; approximate Gaia edge-on geometry and G-band neighbor flux budgets. Capable close neighbors prevent definitive source attribution.

Next check: Higher-resolution time-series localization or a second field orientation resolving capable close sources.

Depth correction audit (2026-11-02): realized trapezoid decrement replaces its unconstrained amplitude parameter. Original input windows, fitted centers/widths, timing selections and physical verdict are retained; capable-neighbor membership is unchanged. See [../../depth-audit/README.md](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/depth-audit/README.md).


Stable review key: R603.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/374606776/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/374606776/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/374606776/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/374606776/fresh-pixels/run.log)
- [historical/diff_s58.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/374606776/historical/diff_s58.json)
- [historical/diff_s58.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/374606776/historical/diff_s58.png)
- [historical/gaia.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/374606776/historical/gaia.json)
- [measurements.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/374606776/measurements.json)
- [phase.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/374606776/phase.png)
- [raw-events.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/374606776/raw-events.png)
- [raw-windows.csv](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/374606776/raw-windows.csv)

[Batch audits and scripts](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/INDEX.md). [Depth correction provenance](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/depth-audit/README.md).
