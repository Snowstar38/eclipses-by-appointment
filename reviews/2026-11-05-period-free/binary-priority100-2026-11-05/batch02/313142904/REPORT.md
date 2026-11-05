# T014  -  TIC 313142904

**Verdict:** CONFIRMED; bounded review COMPLETE. **Catalogue novelty:** UNKNOWN (shared catalogue review has four unavailable VizieR gates; see `../../shared-catalogues/REPORT.md`). The selection stratum is cross_method_dip; queue rank is not physical evidence.

## Deciding evidence

Five clean, symmetric raw SAP eclipses in S19/26/52/59/79 have measured centers 1832.6659, 2029.9716, 2720.5524, 2917.8669 and 3460.4681 BTJD. Same-kind cycles 0,4,18,22,33 fit P=49.327372+/-0.000108 d with maximum residual 0.00375 d; diverse intervals constrain cycle aliases. Conditional P/2 interstitial windows S40/53/60 have fully covered +/-0.10 d cores and both baselines, with 0.00/-0.36/+0.09 ppt deficits, rejecting a comparable missing eclipse at half cycles. The reported epoch names this observed kind; it is not assumed to be a deeper primary. Raw SAP S19 depth is 8.08 ppt; independent TESSCut target-centered raw pixels give 7.56 ppt and QLP corrected versions 7.90-8.18 ppt. Difference centroid is 0.127 px from target WCS. Nearest ideal-G capable Gaia neighbor is 42.95 arcsec away, 2.07 px from the deficit, requiring >=36% disappearance before aperture loss. Measured conjunction phase offsets are +0.0054 to +0.0066 versus the selected Gaia orbit, compatible in the bounded edge-on model.

Raw SAP quality-zero local plots are `lead-raw-*.png`; the independent full-data diagnostic is `lead-fold.png`. `lead-numeric.json` records all screened flags and file/cadence hashes, `lead-timing.json` records curated same-kind clocks, `lead-coverage.json` records tested actual windows where applicable, and `lead-geometry.json` records the approximate Gaia conjunction comparison. Source-packet and shared-catalogue receipts are outside this batch folder; `../helper-audit.md` and helper artifacts document alternative reduction and source attribution where material. A corrected QLP flux and a custom TESSCut aperture share the same TESS photons.

## Limits and next check

Formal timing error uses fit residual/cadence floor and is uncalibrated for pipeline offsets; Gaia orbit conjunction comparison is an edge-on approximation without full covariance propagation.

Observe another eclipse with higher spatial resolution to strengthen attribution and the ephemeris.
