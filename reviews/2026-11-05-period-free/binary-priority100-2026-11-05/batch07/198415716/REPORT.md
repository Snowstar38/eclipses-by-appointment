# T062 / TIC 198415716 - PLAUSIBLE

Queue stratum: cross_method_dip. Gaia source 1434045294727818880; selection P=48.990104 d. Physical verdict and novelty are separate; shared catalogue status is UNKNOWN because four VizieR gates remain unavailable.

## Raw evidence

The s24 ~1971.41 window contains an ~7-9 ppt local notch on a strongly sloping raw baseline. Three other retained windows in the same sector have dissimilar irregular shapes; the 1957.45 window intersects a ~14.7 ppt local step and the 1970.39 window is a rising flank. Conditional Gaia-period checks elsewhere sample near-flat flux, but their endpoints, side baselines and accumulated timing error do not establish a comprehensive sensitive null. The 1971 notch might still be a single physical event.

The original detector windows are predictions, not eclipse centers. The exploratory local trapezoid fits in `lead-numeric.json` do not define an orbital ephemeris. Representative raw plots are `lead-raw-01.png`; full-sector SAP/KSPSAP context is in the `lead-sector-*.png` plots. `lead-fold-coverage.json` records time-bin core coverage and local contrast for returns conditional on the Gaia period point estimate. Period uncertainty accumulates over cycles; these phase checks are not calibrated nulls across the whole timing allowance. A flagged or gapped window is not a clean null.

## Alternative reduction and attribution

KSPSAP removes much of the s24 drift and the notch is less distinct. This same-photon alternative favors a trend explanation but does not by itself prove an artifact. No deciding difference pixel is available for the small s24 notch.

## Orbital geometry

Gaia P=48.99010 d. The 1971.41 screen is 5.00 d from the closest edge-on conjunction versus a 1.77 d linear covariance allowance, so association with that spectroscopic orbit is weak. A different eclipse period is untested.

## Limits and next check

The event center, source and repeat period are insecure; the s24 baseline is strongly variable.

Test a future clean raw notch and locate it in difference pixels before fitting an eclipse period.

Source receipts: the batch `SOURCE-HASHES.json` includes this TIC source packet, original bulk-window JSON and every used QLP FITS SHA-256. The shared Gaia neighbor and NSS catalogues and current TESSCut sector response are recorded once for the batch. New-sector TESSCut receipts, if present, are in this TIC directory.
