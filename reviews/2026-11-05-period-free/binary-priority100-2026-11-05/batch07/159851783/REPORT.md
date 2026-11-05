# T069 / TIC 159851783 - PLAUSIBLE

Queue stratum: cross_method_dip. Gaia source 4610838952095181952; selection P=30.117146 d. Physical verdict and novelty are separate; shared catalogue status is UNKNOWN because four VizieR gates remain unavailable.

## Raw evidence

There are broad ~4-6 ppt SAP depressions at the Gaia-period screened phases in s25 (1986.44), s26 (2016.56) and s52 (2739.37), including two consecutive sector occasions and a 24-cycle longer separation. They do not show secure ingress/flat core/egress of a detached eclipse. The s52 phase trough is one of several smooth oscillatory troughs across that sector (approximately 2724, 2729, 2734 and 2739), so it does not isolate an orbit. At the same predicted phase, s40 is a positive ~2.5 ppt hump, s79 a sloping positive baseline, and s80 a sloping ~1 ppt deficit. Thus the broad resemblance is suggestive but not a measured same-kind ephemeris.

The original detector windows are predictions, not eclipse centers. The exploratory local trapezoid fits in `lead-numeric.json` do not define an orbital ephemeris. Representative raw plots are `lead-raw-01.png`; full-sector SAP/KSPSAP context is in the `lead-sector-*.png` plots. `lead-fold-coverage.json` records time-bin core coverage and local contrast for returns conditional on the Gaia period point estimate. Period uncertainty accumulates over cycles; these phase checks are not calibrated nulls across the whole timing allowance. A flagged or gapped window is not a clean null.

## Alternative reduction and attribution

Terra independently extracted active-sky-corrected target-containing 3x3 apertures from valid 9x9 TESSCut cubes: the Gaia-phase +/-0.8 d cores versus 2-4 d sides show 4.38, 4.60 and 7.69 ppt deficits in s25, s26 and s52. QLP SAP gives 2.14, 5.37 and 7.91 ppt in those same windows. All three cutouts have positive target flux and no zero pixels. This supports a real aperture variation, but the same photons and a blended 3x3 extraction do not prove a target eclipse. KSPSAP strongly suppresses all three broad troughs, as expected for either long astrophysical events or raw extraction trends; suppression alone is not artifact proof.

## Orbital geometry

Gaia P=30.11715 d; the s26 screening time is 3.74 d from the nearest edge-on conjunction against a 1.37 d linear allowance. The conditional phase coherence of broad troughs is not a measured photometric period.

## Limits and next check

Aperture variation is supported; eclipse morphology, timing centers and source attribution are insecure. Broad sector trends can mimic phase agreement.

Locate s25/s26/s52 deficits with convincing target-versus-background difference pixels and obtain a clean, bracketed repeat.

Source receipts: the batch `SOURCE-HASHES.json` includes this TIC source packet, original bulk-window JSON and every used QLP FITS SHA-256. The shared Gaia neighbor and NSS catalogues and current TESSCut sector response are recorded once for the batch. New-sector TESSCut receipts, if present, are in this TIC directory.

Independent helper pixel audit: `helper-audit.txt`, its `helper-*-numeric.json`/`helper-pixel-numeric.json` measurements, image plots, retrieval receipts and reproducible helper scripts in the batch folder.
