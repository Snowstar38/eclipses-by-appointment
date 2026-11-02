# TIC 314040568: CONFIRMED

Full bounded physical review: **COMPLETE**. Physical classification is separate from catalogue recovery/novelty; historical screening was not an admission verdict.

1. **Raw events.** 14 free-center trapezoid measurements from quality-zero QLP SAP_FLUX in sectors [17, 77, 85]; 7 enter the reported ephemeris. Representative raw light curves and numerical windows show repeated eclipse morphology. Predictions guided the windows and are not measurements. Flagged or uncovered windows are not clean nulls.
2. **Timing and aliases.** Measured recurring-eclipse timing supported. Deeper odd half-period cycles only; shallow even cycles establish secondary near phase 0.5. P=9.1805146651 +/- 0.0000287051 d; reference BTJD=1771.3939484. Epoch kind: Deeper repeating eclipse, odd historical half-period parity. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. The formal error column is the local free-center model covariance; the input error adds a half-cadence floor. Singular/unidentifiable centers are excluded. Cycle/parity counts are in [../alias-audit.json](../../campaign/batch06/alias-audit.json). The epoch kind above states whether the fitted events are identified as deeper primary or selected eclipse by convention. The bounded half/double check does not prove all possible aliases absent.
3. **Attribution.** Fresh difference stack in sector 85 has 2 events; target coordinate [7.5895062275439145, 7.700943838622596], deficit [7.580766136291378, 7.829906458814922]; offset 0.129 pixel. The image-model fractional residual 0.777 is not a localization uncertainty. Every capable Gaia neighbor in the retained 60-arcsec table was inspected: Gaia 2013347867977153152: 57.49 arcsec, G=12.410, intrinsic required loss proxy=0.365. The intrinsic loss proxy uses a pairwise G-band flux budget and cannot be directly compared with diluted pixel fractional loss. Close blends and passband/aperture response limit exclusion claims. Persistent unequal alternating 120/190 ppt dips reject the historical half-period as an orbital period. The quoted 9.180514665 d ephemeris uses seven deeper odd-parity measured eclipses; shallow even-parity events form the phase 0.500 secondary. Fresh pixel stack uses only deeper events and favors target over the 57.49 arcsec capable neighbor.
4. **Alternative reduction.** Fresh TESScut background-subtracted target-centered 1x1/3x3/5x5 depths are 191.13/178.63/143.19 ppt; selected QLP fitted median 190.32 ppt. This reruns the historical extraction primitive using the fresh ephemeris and measured duration, with identity and source hashes checked. The alternative extraction and the QLP data for this sector share the same TESS photons; they test processing robustness and are not independent observations. Distinct sectors are distinct observing occasions on one instrument. Depth differences can reflect dilution, aperture and background response; intrinsic binary depth is not inferred.
5. **Gaia geometry/physical plausibility.** Exact DR3 source 2013348112800055808, orbital P=9.1811034987 d, e=0.01268. Closest edge-on conjunction offset=-0.14075 d (-0.01533 phase), full source-specific covariance linear timing allowance=0.17439 d. Mass function=0.14611 solar masses; adopted primary mass=1.13, minimum secondary mass=0.823. Rough central duration=10.31 h versus observed median=8.31 h. Radius and main-sequence companion assumptions make this a plausibility calculation, not a fitted geometry or calibrated significance veto. Shorter observed duration can reflect impact parameter and model assumptions. Orbit agreement does not establish ownership among unresolved sources.

**Secondary phase check:** Pooled raw-window free-center phase=0.5000975746392974, depth=124.56105240297056ppt. Formal pooled trapezoid covariance only; sector normalization, red noise and shape systematics uncalibrated. Weak secondary fits (especially314713331) describe inspected narrow dips and are not independent primary-eclipse evidence or calibrated detection significances. See [../secondary-phases.json](../../campaign/batch06/secondary-phases.json) and [../secondary-contact.png](../../campaign/batch06/secondary-contact.png).

**Deciding limit:** Persistent unequal alternating 120/190 ppt dips reject the historical half-period as an orbital period. The quoted 9.180514665 d ephemeris uses seven deeper odd-parity measured eclipses; shallow even-parity events form the phase 0.500 secondary. Fresh pixel stack uses only deeper events and favors target over the 57.49 arcsec capable neighbor.

**Next check:** Optional resolved photometry and spectroscopy for precision physical parameters.

Catalogue recovery is recorded centrally in [../../shared-catalogues/coverage-matrix.csv](../../campaign/shared-catalogues/coverage-matrix.csv). A successful cone with no exact eclipsing target classification is distinct from a failed query; known recoveries must not count as new additions. No exhaustive literature priority claim is made.

| Sector | Search cycle | Measured midpoint BTJD | Formal center error d | Timing input error d | Depth ppt | Timing status |
|---|---:|---:|---:|---:|---:|---|
| 17 | 0 | 1766.8040475 | 0.000239269 | 0.0104167 | 120.02 | other parity |
| 17 | 1 | 1771.3943669 | 0.000164893 | 0.0104167 | 185.55 | selected |
| 17 | 3 | 1780.5753217 | 0.000278147 | 0.0104167 | 184.46 | selected |
| 17 | 4 | 1785.1660010 | 0.000319738 | 0.0104167 | 121.14 | other parity |
| 77 | 355 | 3396.3448717 | 0.000235171 | 0.0011574 | 195.64 | selected |
| 77 | 356 | 3400.9359518 | 0.000419352 | 0.0011574 | 125.85 | other parity |
| 77 | 357 | 3405.5256323 | 0.00026901 | 0.0011574 | 194.63 | selected |
| 77 | 360 | 3419.2972904 | 0.000388438 | 0.0011574 | 126.87 | other parity |
| 85 | 402 | 3612.0877771 | 0.000364141 | 0.00115738 | 124.07 | other parity |
| 85 | 403 | 3616.6769356 | 0.000269006 | 0.00115738 | 190.11 | selected |
| 85 | 404 | 3621.2690180 | 0.000312457 | 0.00115738 | 124.22 | other parity |
| 85 | 405 | 3625.8582844 | 0.000245969 | 0.00115738 | 190.32 | selected |
| 85 | 406 | 3630.4489996 | 0.000339954 | 0.00115738 | 123.33 | other parity |
| 85 | 407 | 3635.0385951 | 0.000198994 | 0.00115738 | 190.54 | selected |

Evidence: [measurements.json](../../campaign/batch06/314040568/measurements.json), [raw-windows.csv](../../campaign/batch06/314040568/raw-windows.csv), [raw-events.png](../../campaign/batch06/314040568/raw-events.png), [fresh-pixels/diff_fresh.json](../../campaign/batch06/314040568/fresh-pixels/diff_fresh.json)/png, historical original receipts, [../download-receipts.json](../../campaign/batch06/download-receipts.json), [../identity-check.json](../../campaign/batch06/identity-check.json), [../alias-audit.json](../../campaign/batch06/alias-audit.json), [../gaia-geometry.json](../../campaign/batch06/gaia-geometry.json) and [../helper-audit.md](../../campaign/batch06/helper-audit.md). Original inputs and fresh outputs are covered by [../SHA256SUMS.json](../../campaign/batch06/SHA256SUMS.json) and [../source-hashes.json](../../campaign/batch06/source-hashes.json).


Stable review key: R597.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](../../campaign/batch06/314040568/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](../../campaign/batch06/314040568/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](../../campaign/batch06/314040568/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](../../campaign/batch06/314040568/fresh-pixels/run.log)
- [historical/diff_s85.json](../../campaign/batch06/314040568/historical/diff_s85.json)
- [historical/diff_s85.png](../../campaign/batch06/314040568/historical/diff_s85.png)
- [historical/gaia.json](../../campaign/batch06/314040568/historical/gaia.json)
- [measurements.json](../../campaign/batch06/314040568/measurements.json)
- [phase-check.json](../../campaign/batch06/314040568/phase-check.json)
- [raw-events.png](../../campaign/batch06/314040568/raw-events.png)
- [raw-windows.csv](../../campaign/batch06/314040568/raw-windows.csv)

[Batch audits and scripts](../../campaign/batch06/INDEX.md). [Depth correction provenance](../../campaign/depth-audit/README.md).
