# T064 / TIC 196423445 - REFUTED

Queue stratum: cross_method_dip. Gaia source 5647494347671741568; selection P=38.828913 d. Physical verdict and novelty are separate; shared catalogue status is UNKNOWN because four VizieR gates remain unavailable.

## Raw evidence

The s88 3703.16 flag is a shallow valley in a broad and rapidly changing baseline. Two large s88 brightenings near 3691 and 3706 bracket that sector; a 0.25 d gap near 3704 changes the raw level by ~32 ppt. The newly available s109 target-containing pixels likewise show two enormous brightenings near 4320 and 4333 with slow recovery. The predicted s109 phase 4324.42 lies in a quiet intervening stretch of a target-flux-valid 1x1 and 3x3 extraction.

The original detector windows are predictions, not eclipse centers. The exploratory local trapezoid fits in `lead-numeric.json` do not define an orbital ephemeris. Representative raw plots are `lead-raw-01.png`; full-sector SAP/KSPSAP context is in the `lead-sector-*.png` plots. `lead-fold-coverage.json` records time-bin core coverage and local contrast for returns conditional on the Gaia period point estimate. Period uncertainty accumulates over cycles; these phase checks are not calibrated nulls across the whole timing allowance. A flagged or gapped window is not a clean null.

## Alternative reduction and attribution

The s109 TESSCut target pixel has median ~3072 counts and zero median-valued edge pixels, so its aperture is meaningful. The recurring brightenings/ramps, not an isolated eclipse, explain the screened s88 valley. The s109 extraction uses later photons; the s88 QLP corrected light curve is an alternative reduction of the original photons.

## Orbital geometry

Gaia P=38.82891 d; s88 screen is 0.17 d from edge-on conjunction within 0.87 d linear allowance, but the flagged shape is not an eclipse.

## Limits and next check

The new-sector extraction has no local background correction; its very large positive excursions make the qualitative shape robust, but small-amplitude null depth is not calibrated.

Reopen only for an isolated target-centered raw deficit independent of the broad brightenings.

Source receipts: the batch `SOURCE-HASHES.json` includes this TIC source packet, original bulk-window JSON and every used QLP FITS SHA-256. The shared Gaia neighbor and NSS catalogues and current TESSCut sector response are recorded once for the batch. New-sector TESSCut receipts, if present, are in this TIC directory.
