# T063 / TIC 220716821 - PLAUSIBLE

Queue stratum: cross_method_dip. Gaia source 5355830682067401344; selection P=47.621113 d. Physical verdict and novelty are separate; shared catalogue status is UNKNOWN because four VizieR gates remain unavailable.

## Raw evidence

The s64 3067.23 flag is a ~5 ppt local notch embedded in a sector-wide rise and later large brightenings. It lacks a clean stable baseline, but the local depression could be a small single event. Conditional Gaia-period checks in s10 and s63 are flat at their screened phases; they do not rule out other timing aliases or a signal of different depth.

The original detector windows are predictions, not eclipse centers. The exploratory local trapezoid fits in `lead-numeric.json` do not define an orbital ephemeris. Representative raw plots are `lead-raw-01.png`; full-sector SAP/KSPSAP context is in the `lead-sector-*.png` plots. `lead-fold-coverage.json` records time-bin core coverage and local contrast for returns conditional on the Gaia period point estimate. Period uncertainty accumulates over cycles; these phase checks are not calibrated nulls across the whole timing allowance. A flagged or gapped window is not a clean null.

## Alternative reduction and attribution

The notch and sector-wide excursion are suppressed in KSPSAP, an alternative reduction of the same photons. Suppression of a shallow feature is not decisive artifact evidence. No event difference image has established source position.

## Orbital geometry

The screen is 0.21 d from the nearest Gaia conjunction with 2.21 d linear allowance, compatible but not a measured event center or period.

## Limits and next check

Morphology is insecure against the brightening baseline; no repeat or source attribution is established.

Obtain a bracketed repeated raw dip and target-centered difference image.

Source receipts: the batch `SOURCE-HASHES.json` includes this TIC source packet, original bulk-window JSON and every used QLP FITS SHA-256. The shared Gaia neighbor and NSS catalogues and current TESSCut sector response are recorded once for the batch. New-sector TESSCut receipts, if present, are in this TIC directory.
