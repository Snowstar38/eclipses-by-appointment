# T067 / TIC 255761037 - PLAUSIBLE

Queue stratum: cross_method_dip. Gaia source 5501675122732638976; selection P=35.913561 d. Physical verdict and novelty are separate; shared catalogue status is UNKNOWN because four VizieR gates remain unavailable.

## Raw evidence

The s2 1364.43 flag is a ~1-3 ppt shallow local depression within irregular baseline motion. The same sector later develops much larger brightenings and edge excursions. Conditional Gaia-period phase checks from s7 through s89 look flat near their point predictions, but their accumulated timing uncertainty and local baseline validity make them insufficient to refute a small single event.

The original detector windows are predictions, not eclipse centers. The exploratory local trapezoid fits in `lead-numeric.json` do not define an orbital ephemeris. Representative raw plots are `lead-raw-01.png`; full-sector SAP/KSPSAP context is in the `lead-sector-*.png` plots. `lead-fold-coverage.json` records time-bin core coverage and local contrast for returns conditional on the Gaia period point estimate. Period uncertainty accumulates over cycles; these phase checks are not calibrated nulls across the whole timing allowance. A flagged or gapped window is not a clean null.

## Alternative reduction and attribution

KSPSAP attenuates the s2 fluctuation and later positive excursions. A noise/extraction explanation is credible, yet the raw local depression has no decisive positive artifact signature. The same-photon corrected series does not independently test recurrence.

## Orbital geometry

The s2 screen is 4.29 d from the nearest Gaia conjunction, about 2.06 linear sigma; its relation to that orbit is uncertain and no eclipse ephemeris is measured.

## Limits and next check

Low signal-to-noise single feature; source attribution and recurrence are unresolved.

Require a cleaner repeated raw deficit with a measured center and valid source pixels.

Source receipts: the batch `SOURCE-HASHES.json` includes this TIC source packet, original bulk-window JSON and every used QLP FITS SHA-256. The shared Gaia neighbor and NSS catalogues and current TESSCut sector response are recorded once for the batch. New-sector TESSCut receipts, if present, are in this TIC directory.
