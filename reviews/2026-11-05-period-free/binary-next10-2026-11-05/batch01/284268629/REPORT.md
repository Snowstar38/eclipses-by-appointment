# N001 TIC 284268629: PLAUSIBLE

Selected stratum: repeat_sector_dip; original priority rank 101. Bounded full review complete. Novelty: UNKNOWN.

## Raw signal and source

S24 and S50 contain nearly identical ~40 ppt flat eclipses at BTJD 1959.089 and 2685.012; a shallower S23 1936.757 dip may be another kind but does not fix the clock. S24 TESSCut loss is near the target (0.15 pixel), with 38.9 ppt in a 5x5 aperture; capable neighbors are projected in actual WCS.

## Timing and physics

The deep-event separation is 725.923 d. Conditional k=21 gives 34.568 d near Gaia 34.579 d, but k=19 and 23 also have no additional tested occasion in cached sectors. k=20 and 22 predict strong observed flat windows. The deeper-event cycle count is therefore not measured. Gaia SB1 P=34.57876 d, e=0.381; a shorter/shallow secondary phase is physically possible but not established. Two deep events and a possible other-kind event do not meet the repeating-clock criterion.

## Limits and next check

Integer aliases untested; second-sector pixel localization and independent pipeline remain limited. Next: Acquire a third primary eclipse or archival non-QLP event at a discriminating cycle.

## Reproducibility

Raw q0 SAP sectors, detector windows and coverage are in `screen.json`, `all-sectors.png`, `ranked-windows.png`; local provisional fits in `fitted-windows.json` and `fitted-windows.png`. The verified original paths and SHA256 hashes are in `[local-path-redacted]`. Pixel checks and source hashes are in `../helper-audit.md` and helper-prefixed artifacts. The sector availability receipt is `../../root-availability.json`. Sparse pair alias diagnostics: `../alias-tests.json`. Source-specific Gaia conjunction diagnostic: `../gaia-geometry.json`. Catalogues: shared-catalogues/TARGET-STATUS.csv and target-evidence.json. Per-target VSX/ASAS-SN/Kostov gates unavailable; primary-table nonmatches are not novelty clearance.
