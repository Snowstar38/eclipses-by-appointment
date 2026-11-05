# Q027 / TIC 94255849

**Physical verdict:** PLAUSIBLE. **Novelty:** UNKNOWN.

## Raw result

S10 BTJD 1588.414 and S100 4075.502 contain narrow, fully sampled raw dips of roughly 4-5 ppt, with the S10 feature retained in KSPSAP. Independent TESSCut difference images place the loss at the target position in both sectors. S101 BTJD 4119.39 contains a dip-like excursion amid dense quality gaps and an abrupt baseline change; its local center is not precise enough to prove another same-kind occasion. Explicit cycle counts 50-64 were projected into all cached sectors: n=56 and 58 predict complete S64 cores at BTJD 3054.020 and 3046.362, with local detrended depths -0.17 and -0.06 ppt rather than a 4-ppt dip. These are useful nulls for those two aliases. Several other counts lack discriminating coverage, and n=57 (43.6331 d) remains conditional; the Gaia period is not an adopted photometric clock.

Selected detector windows (BTJD predictions, not adopted event centers): S10 1588.411, S100 4075.507, S101 4119.324. Full measured local windows, fits, actual sector coverage and SHA-256 source receipts are in `lead-measurements.json`; raw plots in `lead-event-panels.png`. Actual core/wing endpoints and gaps are in `lead-window-checks.json`. Same-photon KSPSAP comparison, where available, is in `lead-alternative.json` and its plot.

## Orbit, source and limits

Frozen Gaia DR3 source 5368647379859461504 has spectroscopic period 43.594943 d. This is a selection prior, not a measured eclipse period or a source-specific conjunction match.

Two clean target-position occasions and a compromised third leave unresolved subpixel neighbors, remaining integer aliases and orbital conjunction geometry.

Independent difference images/WCS for S10 and S100: `../helper-q027-difference.json` and associated PNG; TESSCut source ZIP hashes are recorded there. Conditional cycle counts, actual cadence coverage and bounded S64 nulls: `lead-alias-checks.json` and `lead-alias-nulls.png`.

This is a bounded verdict on the selected bulk lead, not a global statement that the star has no binary or transit signal. A same-photon reduction is a processing comparison, not a new observing occasion.

## Next check

Obtain a third complete target-localized dip or further sensitive alias nulls, then test Gaia conjunction geometry.
