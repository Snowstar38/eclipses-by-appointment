# Q095 - TIC 3299934

**Physical verdict:** PROBABLE. **Review completion:** COMPLETE. **Catalogue novelty:** UNKNOWN.

## Raw morphology and coverage

S8, S9, S62 and S89 show matching flat-bottom dips at measured centers 1528.1410, 1549.1704, 3000.0675 and 3736.0319 BTJD; independent trapezoids give 3.85, 3.97, 4.69 and 4.69 ppt depths. S99 is an extreme gap/baseline step, not an event.

## Timing and interpretation

A linear fit with cycles 0, 1, 70, 105 gives P=21.0275198 d and residuals under 0.0011 d. Tested P/2, P/3 and P/4 same-kind aliases predict well-covered nulls; S62 at 3010.582 has 172 core, 64+64 baseline points, maximum internal gap 0.00232 d and 0.276 ppt measured depth versus 3.686 ppt at the actual S62 event. See lead-alias.json for others. These are bounded tests, not an exhaustive alias proof. Gaia SB1 P=21.0288706 d; a source-specific edge-on approximation gives S8 conjunction 1528.873 versus measured 1528.141, phase offset -0.0348, without propagated covariance. This is not a full orbital-geometry test.

## Source and reduction

For Q095, TESSCut S62 and S89 deficit peaks lie on the WCS target pixel, with positive target-region baseline and 3x3 depths 5.95 and 4.31 ppt. MAST TIC identifies capable neighbors 23.42, 29.94 and 30.11 arcsec away with approximate T-band flux ratios 0.0338, 0.00627 and 0.182. Coarse pixels do not uniquely exclude blended origins. See the independent helper audit for image and attribution checks. SAP and, where available, KSPSAP are displayed in the zoom plots; detrending may suppress long events, so suppression alone is not a refutation. Same photons in different reductions do not create another occasion. Screening centers are predictions rather than measurements.

## Limits and next check

Repeated real eclipses are supported; definitive source attribution and Gaia association remain unresolved.

Obtain spatially resolved eclipse photometry and a covariance-aware Gaia conjunction test.

## Provenance

The batch lead-context script verifies source-packet, bulk-result and FITS hashes. Numeric `lead-context.json`, `lead-local-series.json` and `lead-flag-diagnostics.json` record raw times, fluxes, endpoints and gaps across 6 sectors; `lead-raw-context.png` and `lead-dip-zooms.png` show raw morphology. See batch `LEAD-SOURCE-HASHES.json`, `helper-audit.md`, and exact direct VSX receipt `../../tap-recovery/vsx-Q095.json`. Other required catalogue scopes remain unavailable, so novelty is UNKNOWN; a generic variability type is not an eclipsing-binary classification.
