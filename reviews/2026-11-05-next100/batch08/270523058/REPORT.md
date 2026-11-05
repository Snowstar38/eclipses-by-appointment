# Q077 TIC 270523058

Physical verdict: **REFUTED**. Review completion: **COMPLETE**. EB novelty: **UNKNOWN**.

Raw S82 has 39 deep minima at BTJD 3533.807–3558.17 with a same-kind interval 0.641193 d and alternating shallow minima halfway between; S14/S40/S54/S74 show the same sharp morphology. SAP, DET_FLUX and SYS_RM_FLUX retain the pattern. Yet TESSCut S14 eclipse difference peaks at pixel (4,4), 2.54 pixels from the target WCS (5.84,5.81). Gaia 2126300770519521024, G=12.12, lies 5.05 arcsec from the loss centroid and is capable; the target is 52.33 arcsec away. VSX ASASSN-V J193328.10+440008.5 is an EW with P=0.641235 d at the displaced neighbor position. This is a real off-target EB lead, not evidence that the queued Gaia 30.03-d SB1 eclipses.

The raw SAP sector plot is `lead-raw-context.png`; every selected dip has raw cadence values in `lead-local-series.json` and actual endpoints/gaps in `lead-flag-diagnostics.json`. Source file hashes are in `../LEAD-SOURCE-HASHES.json`; sectors reviewed: 14,15,40,41,54,55,74,75,81,82. The screening centers are predictions, not fitted centers. VSX direct receipt: `[local-path-redacted]` (queried 2026-11-05; exact identity assessed separately from physical verdict).

Limitations: The target may be binary spectroscopically; this refutes assignment of the short-period eclipses to it.

Next check: Preserve the neighbor as a separate known EB and seek target-only photometry for the 30.03-d orbit.
