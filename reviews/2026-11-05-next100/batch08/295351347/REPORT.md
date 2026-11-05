# Q078 TIC 295351347

Physical verdict: **PROBABLE**. Review completion: **COMPLETE**. EB novelty: **UNKNOWN**.

S99 shows eleven narrow V-shaped raw minima across consecutive ~0.693052-d intervals (4.7-minute RMS of minimum times), with similar recurring V morphology in earlier and later sectors. SAP, DET_FLUX and SYS_RM_FLUX preserve the S99 signal. TESSCut S11 difference centroid is 0.39 pixel from the target WCS, but a TIC neighbor at 13.1 arcsec and T-band flux ratio 0.050 is only 0.30 pixel from that centroid; another at 22.7 arcsec has ratio 0.34. The 4-ppt signal does not uniquely belong to the target. The Gaia 57.029-d SB1 period is not the measured short photometric clock. VSX has an exact-position GDS variable without EB type, plus more distant Gaia E entries; none alone establishes an exact-target known EB.

The raw SAP sector plot is `lead-raw-context.png`; every selected dip has raw cadence values in `lead-local-series.json` and actual endpoints/gaps in `lead-flag-diagnostics.json`. Source file hashes are in `../LEAD-SOURCE-HASHES.json`; sectors reviewed: 11,12,38,65,99,100,101,102. The screening centers are predictions, not fitted centers. VSX direct receipt: `[local-path-redacted]` (queried 2026-11-05; exact identity assessed separately from physical verdict).

Limitations: A repeated eclipse-like signal is real, but close-source ownership and orbital-cycle/harmonic interpretation remain unresolved.

Next check: Use higher-resolution or multi-aperture eclipse localization to separate the target from capable neighbors.
