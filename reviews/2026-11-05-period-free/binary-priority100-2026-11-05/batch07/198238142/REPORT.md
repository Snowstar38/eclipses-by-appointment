# T068 / TIC 198238142 - REFUTED

Queue stratum: cross_method_dip. Gaia source 1636006889053061888; selection P=59.304946 d. Physical verdict and novelty are separate; shared catalogue status is UNKNOWN because four VizieR gates remain unavailable.

## Raw evidence

The s17 retained dip screen at 1788.36 is actually on a sharp raw brightening/ramp: the measured core is about +12 ppt relative to its baseline. The same sector has strong positive end-of-interval ramps. Sixteen other sectors sample approximately flat flux at the Gaia-period point predictions, conditional on that period and their local coverage.

The original detector windows are predictions, not eclipse centers. The exploratory local trapezoid fits in `lead-numeric.json` do not define an orbital ephemeris. Representative raw plots are `lead-raw-01.png`; full-sector SAP/KSPSAP context is in the `lead-sector-*.png` plots. `lead-fold-coverage.json` records time-bin core coverage and local contrast for returns conditional on the Gaia period point estimate. Period uncertainty accumulates over cycles; these phase checks are not calibrated nulls across the whole timing allowance. A flagged or gapped window is not a clean null.

## Alternative reduction and attribution

KSPSAP largely removes the s17 ramp. The sign of the raw event and its asymmetric rising shape positively refute an eclipse interpretation for this flag; the conditional phase checks are secondary context.

## Orbital geometry

The s17 screen is ~15.83 d from the nearest Gaia conjunction versus 3.09 d linear allowance.

## Limits and next check

The raw positive excursion could have a separate source or astrophysical cause; it is not an eclipse.

No eclipse follow-up from this flag; inspect any future independent dip on its own merits.

Source receipts: the batch `SOURCE-HASHES.json` includes this TIC source packet, original bulk-window JSON and every used QLP FITS SHA-256. The shared Gaia neighbor and NSS catalogues and current TESSCut sector response are recorded once for the batch. New-sector TESSCut receipts, if present, are in this TIC directory.
