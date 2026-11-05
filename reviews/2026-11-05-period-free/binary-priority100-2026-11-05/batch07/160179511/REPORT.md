# T070 / TIC 160179511 - PLAUSIBLE

Queue stratum: cross_method_dip. Gaia source 4820577220362873728; selection P=55.622725 d. Physical verdict and novelty are separate; shared catalogue status is UNKNOWN because four VizieR gates remain unavailable.

## Raw evidence

The s6 1471.28 window contains a small ~1.5 ppt raw notch, with a 0.83 d gap shortly afterward. s32 at the Gaia-period phase is flat while s98 has a slow downward drift of about 1 ppt rather than a matching isolated dip. The newly available s107 has large positive pixel-flux excursions and no event-phase prediction in its time span. s108 covers the projected 4308.04 phase, but its WCS target pixel median is only ~0.15 counts and its extracted sums are noise dominated; it is not a sensitive null.

The original detector windows are predictions, not eclipse centers. The exploratory local trapezoid fits in `lead-numeric.json` do not define an orbital ephemeris. Representative raw plots are `lead-raw-01.png`; full-sector SAP/KSPSAP context is in the `lead-sector-*.png` plots. `lead-fold-coverage.json` records time-bin core coverage and local contrast for returns conditional on the Gaia period point estimate. Period uncertainty accumulates over cycles; these phase checks are not calibrated nulls across the whole timing allowance. A flagged or gapped window is not a clean null.

## Alternative reduction and attribution

KSPSAP removes the s6 shallow notch, but a detrending response alone cannot refute a small eclipse. The s107 valid target-containing extraction shows unrelated large brightenings; the s108 near-zero target flux invalidates a lowest-pixel background or target-aperture null.

## Orbital geometry

Gaia P=55.62273 d and the s6 screen is 0.27 d from predicted conjunction within 1.33 d linear allowance. Only one insecure event remains; no eclipse-based period is measured.

## Limits and next check

The original notch is shallow and only partially bracketed, with no established same-kind recurrence; s108 extraction cannot test the predicted phase.

Obtain target-flux-valid photometry at a future conjunction and difference pixels for a securely bracketed dip.

Source receipts: the batch `SOURCE-HASHES.json` includes this TIC source packet, original bulk-window JSON and every used QLP FITS SHA-256. The shared Gaia neighbor and NSS catalogues and current TESSCut sector response are recorded once for the batch. New-sector TESSCut receipts, if present, are in this TIC directory.
