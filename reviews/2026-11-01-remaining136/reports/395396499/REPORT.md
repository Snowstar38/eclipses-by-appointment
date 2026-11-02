# TIC 395396499

Physical verdict: **confirmed**. Full bounded review: **complete**.

Crowded field: the large light-centroid displacement is caused by bright off-target flux and is not an attribution veto. The positive deficit core lies at the target, distinct from the brighter northeastern star and southwest capable cluster; target-centered alternative apertures retain the dip. Capable sources29-59.5 arcsec away and PSF overlap remain explicit limitations.

Measured period 2.13472589336 +/- 1.7530711e-06 d; named selected-eclipse epoch BTJD 1599.22690181; depth 17.11187 ppt (diluted raw QLP). Epoch is the selected recurring eclipse, not an assumed deeper primary. BTJD = BJD_TDB -2457000.

Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.

Timing samples: 26; sectors [11, 65, 101]; fitted same-kind cycle span 0 to 1183. Reduced chi square: 1.580164096963273. Actual centers, errors and local windows are in [measurements.json](../../campaign/batch07/395396499/measurements.json) and [raw-windows.csv](../../campaign/batch07/395396499/raw-windows.csv); predicted centers are labeled and never counted as measurements.

Aliases: within-sector adjacent same-kind pairs [[11, 0, 1], [11, 8, 9], [11, 9, 10], [11, 10, 11], [65, 689, 690], [65, 690, 691], [65, 691, 692], [65, 692, 693], [65, 693, 694], [65, 696, 697], [65, 697, 698], [65, 698, 699], [65, 699, 700], [101, 1173, 1174], [101, 1174, 1175], [101, 1175, 1176], [101, 1179, 1180], [101, 1182, 1183]]. Sector parity depths and nearby integer counts are in [../alias-audit.json](../../campaign/batch07/alias-audit.json) and [../integer-aliases.json](../../campaign/batch07/integer-aliases.json). Half-period extra windows are in [../coverage-alias-windows.json](../../campaign/batch07/coverage-alias-windows.json); flagged/empty windows are not nulls. No persistent unequal alternating primary depths support a doubled period. Gaia period is a consistency test, not a fixed photometric fit.

Secondary assessment: {'status': 'No secure secondary established by visual review of full raw phase and predicted-conjunction windows. Baseline variability/coverage limit a null claim; guess is Gaia-predicted separation, not a measured secondary phase.', 'guess_phase': 0.4772357068682392}

Attribution and alternative reduction: fresh TESScut S65 stacks 13 well-covered target-period eclipses. Target WCS pixel [7.961116056680671, 7.482100973027203]; deficit centroid [7.899055809335304, 7.515974381575997]. Read [fresh-pixels/diff_fresh.png](../../campaign/batch07/395396499/fresh-pixels/diff_fresh.png) against every capable neighbor below. No fixed centroid threshold applied. Target-centered custom background-subtracted1x1/3x3/5x5 extraction depths are 14.5450/9.9920/4.7739 ppt. This is a separate reduction of the same TESS photons, not independent observations; different sectors are different occasions on one instrument. Source FITS identities and SHA256 hashes are in [../identity-check.json](../../campaign/batch07/identity-check.json) and [../source-hashes.json](../../campaign/batch07/source-hashes.json).

All capable neighbors within60 arcsec (G-band flux-ratio proxy; intrinsic required depth is not directly compared to diluted pixel loss): [{"source_id": "5839906997056207872", "sep": 28.991768548491514, "G": 14.527749, "depth_needed": 0.12523499046901695, "possible": true, "px": [7.669671677458119, 6.0421327988523466], "frac_loss_at_pixel": 0.003890088099268314}, {"source_id": "5839907752970061184", "sep": 30.167358839238897, "G": 16.730427, "depth_needed": 0.8393351766660134, "possible": true, "px": [6.639910687639509, 6.821973862753561], "frac_loss_at_pixel": 0.013029986949728293}, {"source_id": "5839906997055815680", "sep": 33.994450456398006, "G": 13.824567, "depth_needed": 0.07368963122755694, "possible": true, "px": [7.518448407043566, 5.820476598680102], "frac_loss_at_pixel": 0.003890088099268314}, {"source_id": "5839907752970060928", "sep": 47.7690576152999, "G": 15.849694, "depth_needed": 0.3824513285700028, "possible": true, "px": [6.0322484129119305, 6.141352446880889], "frac_loss_at_pixel": 0.0034798911201436404}, {"source_id": "5839908130927585152", "sep": 53.33159216312645, "G": 14.634632, "depth_needed": 0.1364204762583442, "possible": true, "px": [6.73918181120282, 9.89160778453462], "frac_loss_at_pixel": 0.0036825051062978217}, {"source_id": "5839907306293855744", "sep": 55.704976634411146, "G": 16.107515, "depth_needed": 0.48037206077229516, "possible": true, "px": [10.657767817278128, 7.105521034384683], "frac_loss_at_pixel": -6.84631508196582e-05}, {"source_id": "5839907821689540352", "sep": 57.537778578956555, "G": 15.858967, "depth_needed": 0.38558496382563046, "possible": true, "px": [5.2078891406838625, 8.080582932402846], "frac_loss_at_pixel": 0.00023481691899460751}, {"source_id": "5839907301986821248", "sep": 59.49996509933243, "G": 11.449473, "depth_needed": 0.02345944658655942, "possible": true, "px": [10.862967528646882, 7.477289573326296], "frac_loss_at_pixel": -6.84631508196582e-05}]

Gaia source 5839907375013334144: source-specific NSS period 2.1348497552 d; eccentricity 0.32304; nearest edge-on conjunction offset -0.03716 d (phase -0.01741), linear full-covariance error 0.07790 d. Source-specific covariance, mass function, assumed masses/radii and approximate central duration are in [../gaia-geometry.json](../../campaign/batch07/gaia-geometry.json). This is not a hard phase veto or fitted inclination. Observed duration 2.818 h, approximate central duration 2.745 h; grazing geometry/dilution and radius assumptions can shorten the eclipse. No contradiction that invalidates repeated-eclipse interpretation is established.

Catalogue outcome: no identified prior EB; seven-group coverage yes. Shared coverage-matrix and catalogue receipts support scope only, not exhaustive priority. Physical verdict is separate from novelty.

Limitations: Representative sectors and simplified trapezoid/linear timing errors; shared TESS photons; approximate Gaia edge-on geometry and G-band neighbor flux budgets.

Next check: Additional clean eclipse timing and color-aware neighbor/PRF modeling would refine the bounded result.


Stable review key: R607.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](../../campaign/batch07/395396499/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](../../campaign/batch07/395396499/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](../../campaign/batch07/395396499/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](../../campaign/batch07/395396499/fresh-pixels/run.log)
- [historical/diff_s65.json](../../campaign/batch07/395396499/historical/diff_s65.json)
- [historical/diff_s65.png](../../campaign/batch07/395396499/historical/diff_s65.png)
- [historical/gaia.json](../../campaign/batch07/395396499/historical/gaia.json)
- [measurements.json](../../campaign/batch07/395396499/measurements.json)
- [phase.png](../../campaign/batch07/395396499/phase.png)
- [raw-events.png](../../campaign/batch07/395396499/raw-events.png)
- [raw-windows.csv](../../campaign/batch07/395396499/raw-windows.csv)

[Batch audits and scripts](../../campaign/batch07/INDEX.md). [Depth correction provenance](../../campaign/depth-audit/README.md).
