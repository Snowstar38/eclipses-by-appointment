# N008 TIC 62374377: PROBABLE

Selected stratum: repeat_sector_dip; original priority rank 108. Bounded full review complete. Novelty: UNKNOWN.

## Raw signal and source

S27 2046.07 and S67 3131.71 have matching ~10–13 ppt rounded raw dips. Newly available S105 target-centered raw TESSCut shows a third ~9.5 ppt dip near 4217.35; its 3x3 flux is positive across all 9290 quality-zero cadences and the difference peak is the target pixel (6,6), with valid core/pre/post counts 259/216/201. S67 independent cutout also centers near target. These are three observing occasions.

## Timing and physics

The two long gaps are each ~1085.64 d. Any integer k cycles per gap reproduces all three times, so equal spacing does not select an orbital period. k=19 or 20 would imply ~57.14 or 54.28 d, both discrepant from Gaia SB2 55.5332 d. A long-period event train or bycatch relative to Gaia is possible. Gaia SB2 e=0.115 does not yet explain a secure eclipse clock at these times; target association and repeating dip are stronger than the Gaia-orbit association.

## Limits and next check

Orbital cycle count and Gaia association unresolved; S105 is a raw TESSCut reduction of new photons, not a QLP light curve. Next: Targeted fourth occasion or intervening eclipse to resolve integer clock and Gaia relationship.

## Reproducibility

Raw q0 SAP sectors, detector windows and coverage are in `screen.json`, `all-sectors.png`, `ranked-windows.png`; local provisional fits in `fitted-windows.json` and `fitted-windows.png`. The verified original paths and SHA256 hashes are in `[local-path-redacted]`. Pixel checks and source hashes are in `../helper-audit.md` and helper-prefixed artifacts. The sector availability receipt is `../../root-availability.json`. Sparse pair alias diagnostics: `../alias-tests.json`. S105 new cutout hash, actual coverage and plot: `s105-check.json`, `s105-event.png`. Source-specific Gaia conjunction diagnostic: `../gaia-geometry.json`. Catalogues: shared-catalogues/TARGET-STATUS.csv and target-evidence.json. Per-target VSX/ASAS-SN/Kostov gates unavailable; primary-table nonmatches are not novelty clearance.
