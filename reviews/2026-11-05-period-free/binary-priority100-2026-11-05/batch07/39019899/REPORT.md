# T065 / TIC 39019899 - PLAUSIBLE

Queue stratum: cross_method_dip. Gaia source 4690111300916173184; selection P=50.886949 d. Physical verdict and novelty are separate; shared catalogue status is UNKNOWN because four VizieR gates remain unavailable.

## Raw evidence

The s96 3925.93 screened trough is ~5 ppt and broad, with a recovery interrupted by a 0.27 d gap and an ~6.6 ppt upward level change. This makes a secure center impossible, but the pre-gap depression might be a single physical event. The full-sector raw traces also show end-of-segment brightenings in s28 and s68. Conditional Gaia-phase samples in s27 and s68 are near zero contrast; they do not establish a period-independent exclusion.

The original detector windows are predictions, not eclipse centers. The exploratory local trapezoid fits in `lead-numeric.json` do not define an orbital ephemeris. Representative raw plots are `lead-raw-01.png`; full-sector SAP/KSPSAP context is in the `lead-sector-*.png` plots. `lead-fold-coverage.json` records time-bin core coverage and local contrast for returns conditional on the Gaia period point estimate. Period uncertainty accumulates over cycles; these phase checks are not calibrated nulls across the whole timing allowance. A flagged or gapped window is not a clean null.

## Alternative reduction and attribution

KSPSAP suppresses the broad drift; it shares the photons and cannot alone refute a possible long eclipse. The gap/step makes an extraction explanation credible but does not prove the entire depression is instrumental.

## Orbital geometry

The screen is ~7.41 d from nearest Gaia conjunction, within a broad 7.80 d linear uncertainty; neither this loose consistency nor the period fold establishes an eclipse.

## Limits and next check

One incompletely bracketed shallow event; center, recurrence and source attribution are unresolved.

Obtain a fully bracketed raw repeat and target-centered pixel deficit before fitting a period.

Source receipts: the batch `SOURCE-HASHES.json` includes this TIC source packet, original bulk-window JSON and every used QLP FITS SHA-256. The shared Gaia neighbor and NSS catalogues and current TESSCut sector response are recorded once for the batch. New-sector TESSCut receipts, if present, are in this TIC directory.
