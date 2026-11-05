# Q002 / TIC 72747845

**Physical verdict:** PLAUSIBLE; **bounded review:** COMPLETE; **catalogue status:** UNKNOWN.

## Raw evidence

Several shallow S3 minima and short S30/S97 features are present in raw SAP at about 1-2 ppt, embedded in similar-amplitude short-timescale variability. The S3 BTJD 1404.5 and S30 BTJD 2120.1 features happen to lie near twelve Gaia-period cycles, but the S3 center is not a measured eclipse center and the shapes do not establish same-kind recurrence. The projected S97 BTJD 3968.21 window has many quality-zero cadences yet a 0.308-d left-baseline gap and similar intrinsic modulation, so it is not a sensitive exclusion.

Selected screen windows: S3 1404.557, S3 1392.515, S3 1385.682, S3 1397.349, S30 2120.112, S97 3944.388. These are detector predictions, not adopted eclipse centers. Lead numeric and original source receipts: `lead-measurements.json`; raw plots: `lead-event-panels.png`; same-photon QLP reduction: `lead-alternative.json`. Independent visual and TESSCut checks: `../helper-audit.md` and helper-prefixed artifacts.

## Timing, identity and limits

Frozen Gaia DR3 source 5116265446446549120; selection spectroscopic period 59.621102 d. This is an orbital prior, not a photometric clock or source-specific conjunction match.

Novelty remains UNKNOWN: the queue-wide catalogue audit has no successful fresh VSX/ASAS-SN/Kostov gate for this target; a failed query is not a nonmatch. Physical classification is independent of novelty.

The eclipse interpretation, clock and target-specific geometry remain insecure. KSPSAP strongly suppresses several S3 minima on the same photons, which alone cannot refute raw variability.

No unsupported photometric period, precision error, primary epoch or depth is adopted. Same-photon reductions are processing comparisons, not independent observing occasions. This bounded verdict concerns the selected bulk lead, not every possible signal from this star.

## Next check

Acquire a distinct source-centered eclipse with stable morphology and a measured clock; test actual aliases and capable neighbors.

Actual projected S97 coverage and baseline limitation: `../helper-Q002-null.json`.
