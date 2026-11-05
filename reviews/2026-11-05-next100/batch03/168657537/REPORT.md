# Q029 / TIC 168657537

**Physical verdict:** REFUTED. **Novelty:** UNKNOWN.

## Raw result

There are many real short raw dips in S4, S5 and S31. Twelve selected local centers give a conditional 1.9634497-d dip clock with 0.00615-d RMS; the ±1 long-baseline cycle aliases smear the narrow cores. Full-cycle extraction finds 22 complete predicted cores. However, independent TESSCut difference images in all three sectors localize the loss at nearby Gaia DR3 4883892013333719680 (G=12.8691), several pixels from the selected Gaia DR3 4883891772815552000. Thus the repeated aperture dips are real but do not belong to the selected Gaia SB1 source, whose spectroscopic period is also incompatible at 46.08764 d.

Selected detector windows (BTJD predictions, not adopted event centers): S4 1433.077, S4 1413.452, S4 1429.160, S4 1411.494, S5 1444.869, S5 1448.806, S5 1462.535, S5 1452.723, S31 2151.709, S31 2153.674, S31 2163.486, S31 2147.778. Full measured local windows, fits, actual sector coverage and SHA-256 source receipts are in `lead-measurements.json`; raw plots in `lead-event-panels.png`. Actual core/wing endpoints and gaps are in `lead-window-checks.json`. Same-photon KSPSAP comparison, where available, is in `lead-alternative.json` and its plot.

## Orbit, source and limits

Frozen Gaia DR3 source 4883891772815552000 has spectroscopic period 46.087636 d. This is a selection prior, not a measured eclipse period or a source-specific conjunction match.

The selected target-associated EB interpretation is refuted by positive spatial attribution to a different star. The neighbor may itself be an EB: odd/even depth differences of about 0.2-0.3 ppt recur in all three sectors, with exploratory sector-stratified permutation p≈0.016. A 1P transiting body remains possible, and aperture dilution limits companion sizing. The selected TIC radius is 2.294 solar radii, but it does not apply to the eclipsed neighbor.

Conditional timing and adjacent-cycle alias residuals: `lead-timing.json`; phase plot: `lead-phase.png`; every covered predicted event and odd/even depths: `lead-all-cycles.json`. Independent source-resolved WCS and difference-flux evidence: `../helper-q029-difference.json`, associated PNG, `../helper-q029-apertures.json` and helper audit. Neighbor-centered apertures have roughly 80-130-ppt dips, whereas target-centered apertures show no corresponding loss at the 0.1-ppt scale. The TIC radius metadata and hash are in `lead-timing.json`; that radius concerns the selected target, not the contaminating neighbor. The photometric dip clock is intentionally not placed in the orbital-period field.

This is a bounded verdict on the selected bulk lead, not a global statement that the star has no binary or transit signal. A same-photon reduction is a processing comparison, not a new observing occasion.

## Next check

Analyze source-resolved neighbor photometry to distinguish 1.96345-d transits from 3.9269-d alternating eclipses; review the selected Gaia SB1 separately for its own orbital eclipses.
