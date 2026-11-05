# Q079 TIC 280051953

Physical verdict: **CONFIRMED**. Review completion: **COMPLETE**. EB novelty: **KNOWN**.

Twelve raw flat-bottomed eclipses from S2 through S96 fit 1379.83394+28.34273608*n BTJD, n=0–90, with 0.0585-d center RMS. Consecutive n=62,63,64 and n=88,89,90 break sparse long-baseline aliases. Local trapezoids are ~1.4–2.0 d wide and ~26–43 ppt deep; independent sector overlays preserve ingress/flat core/egress. SYS_RM_FLUX retains the S67 36.5-ppt dip while DET_FLUX suppresses it, a detrending limitation rather than a raw refutation. S13 TESSCut loss centroid is 0.064 pixel from target WCS; exact-position VSX ASAS J030241-7332.9 is ESD|EC, catalog period 28.27 d. Gaia SB1 P=28.341827 d agrees; nominal edge-on conjunction is 0.10 d from S13 measured center, subject to correlated orbital uncertainties. Fully covered half-phase windows in S63/S94/S96 have broad ~12-18 ppt minima, unlike the ~35-ppt flat-bottom primary; the 14.17-d identical-event alias fails this morphology test. A 56.69-d alternating-kind photometric interpretation is not excluded by primary times alone, but is disfavored by the Gaia spectroscopic period.

The raw SAP sector plot is `lead-raw-context.png`; every selected dip has raw cadence values in `lead-local-series.json` and actual endpoints/gaps in `lead-flag-diagnostics.json`. Source file hashes are in `../LEAD-SOURCE-HASHES.json`; sectors reviewed: 2,13,27,28,29,36,63,67,68,69,87,90,94,95,96. The screening centers are predictions, not fitted centers. VSX direct receipt: `[local-path-redacted]` (queried 2026-11-05; exact identity assessed separately from physical verdict).

Limitations: The Gaia neighbor cone timed out, but a MAST TIC cone finds the nearest catalogued sources at 24.0/25.2 arcsec with T-band flux ratios 0.0004/0.0007, incapable of a ~35-ppt target-aperture loss even at full disappearance. Unresolved sources remain a small residual caveat. The fitted period has no formal error because event shapes and baseline differ by sector.

Next check: Refine orbital geometry jointly with radial velocities and obtain high-resolution eclipse photometry to tighten source ownership.
