# F018 — TIC 340638289: REFUTED

**Physical finding.** The early S34/S36 flags are shallow ramp/step valleys and are suppressed in KSPSAP. S64/S87/S90 are broad changes centered near data interruptions. S94 at 3875 is a deep common time that appears across several unrelated queue targets, while S95/S97 flags align with level breaks and monotonic recoveries. Local trapezoids repeatedly hit their width bound instead of measuring stable ingress and egress.

**Coverage and evidence.** Verified 22 source FITS and quality-zero positive SAP in cached sectors 4, 7, 8, 9, 10, 27, 30, 34, 35, 36, 37, 61, 63, 64, 67, 68, 87, 88, 90, 94, 95, 97. The current TESSCut sector service returned 200 and lists uncached sectors 89. The original bulk flags are screening windows, not fitted centers. Numeric timing/coverage and source SHA-256 receipts: `lead-measurements.json`; same-photon alternative reduction: `lead-alternative.json`; raw and alternative panels are adjacent. 

**Limits.** The selected windows have positive trend/gap/step evidence, with no secure same-kind raw eclipses; an unrelated signal remains possible. S89 is available but uncached.

**Next check.** Inspect S89 only if a fresh event away from discontinuities establishes an eclipse interpretation.

**Novelty.** SCOPED_NONMATCH; no target EB identification in checked tables. This bounded catalogue status is separate from the physical verdict and is not a new-system claim.
