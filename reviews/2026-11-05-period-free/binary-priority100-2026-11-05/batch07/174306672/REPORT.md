# T061 / TIC 174306672 - REFUTED

Queue stratum: cross_method_dip. Gaia source 1937604302944104704; selection P=29.013877 d. Physical verdict and novelty are separate; shared catalogue status is UNKNOWN because four VizieR gates remain unavailable.

## Raw evidence

Sector 84 QLP SAP contains two extraordinary asymmetric drops near BTJD 3585.8 and 3599.3, separated by about 13.5 d. The screened 3599.55 box samples a ~208 ppt core deficit. At the same Gaia-period phase, s16, s17 and s57 have 1.00, 0.97 and 0.87 time-bin core coverage with ~0, +0.6 and -1.6 ppt local contrast. Those are informative historical non-repeats under the assumed phase. The two s84 troughs are same-sector features and cannot establish same-kind orbital recurrence.

The original detector windows are predictions, not eclipse centers. The exploratory local trapezoid fits in `lead-numeric.json` do not define an orbital ephemeris. Representative raw plots are `lead-raw-01.png`; full-sector SAP/KSPSAP context is in the `lead-sector-*.png` plots. `lead-fold-coverage.json` records time-bin core coverage and local contrast for returns conditional on the Gaia period point estimate. Period uncertainty accumulates over cycles; these phase checks are not calibrated nulls across the whole timing allowance. A flagged or gapped window is not a clean null.

## Alternative reduction and attribution

The independent TESSCut pixel cube has the G=11.3058 target at (5.17,5.94) and a brighter G=10.5737 neighbor 23.72 arcsec away at (6.22,6.34), both at the active edge. Its 11x11 cutout contains 44 zero edge pixels, invalidating a lowest-pixel background estimator. Terra used active-sky pixels instead: background rises about 50.6 and 88.6 counts per pixel at the two QLP troughs, while raw target and neighbor pixels rise too. A target-plus-neighbor 4x3 extraction after valid sky correction shows only 0.042% and 0.408% deficits, versus QLP SAP 15.07% and 24.11% in the same windows. This direct same-photon pixel contradiction and sky correlation positively identify the huge QLP dips as extraction/background artifacts. The small pixel residuals cannot be localized because both PSFs are truncated at the edge.

## Orbital geometry

Gaia SB1 P=29.01388 d; the 3599.55 screening time is 1.69 d before the nearest edge-on Gaia conjunction with linear covariance allowance 2.82 d. Geometry cannot rescue QLP troughs contradicted by the raw pixels.

## Limits and next check

The edge-truncated TESSCut aperture cannot establish whether a much smaller physical signal belongs to either star. The selected 15-24% QLP eclipse interpretation is refuted.

Only a target-flux-valid, fully captured aperture or independent photometry showing a repeated isolated deficit would reopen the eclipse claim.

Source receipts: the batch `SOURCE-HASHES.json` includes this TIC source packet, original bulk-window JSON and every used QLP FITS SHA-256. The shared Gaia neighbor and NSS catalogues and current TESSCut sector response are recorded once for the batch. New-sector TESSCut receipts, if present, are in this TIC directory.

Independent helper pixel audit: `helper-audit.txt`, its `helper-*-numeric.json`/`helper-pixel-numeric.json` measurements, image plots, retrieval receipts and reproducible helper scripts in the batch folder.
