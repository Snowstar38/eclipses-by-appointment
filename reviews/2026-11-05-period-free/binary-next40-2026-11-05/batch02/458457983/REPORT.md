# F013 — TIC 458457983: PLAUSIBLE

**Physical finding.** Narrow raw SAP deficits at 1950.849 in S23 and 2685.513 in S50 are each represented by very few cadences and survive KSPSAP at about 5.5 and 2.2 ppt local core depth. Their 734.664-day separation allows many integer aliases; N=27 gives about 27.2098 d, close to but not identical with the Gaia 27.2175-day SB1 period. S23 fresh TESSCut has only three core cadences but places its difference peak near the target; the S50 cutout has no valid core at the narrow event. The broad 1934.5 flag is a trend, not a secure third event.

**Coverage and evidence.** Verified 2 source FITS and quality-zero positive SAP in cached sectors 23, 50. The current TESSCut sector service returned 200 and lists uncached sectors none. The original bulk flags are screening windows, not fitted centers. Numeric timing/coverage and source SHA-256 receipts: `lead-measurements.json`; same-photon alternative reduction: `lead-alternative.json`; raw and alternative panels are adjacent. Fresh WCS difference measurements and download hashes: `cutouts/pixel-evidence.json`. 

**Limits.** Two sparse events do not fix a cycle count; S50 source attribution and precise centers remain insecure.

**Next check.** Capture another narrow event with high-cadence target and neighbor photometry, then test adjacent integer aliases.

**Novelty.** SCOPED_NONMATCH; no target EB identification in checked tables. This bounded catalogue status is separate from the physical verdict and is not a new-system claim.
