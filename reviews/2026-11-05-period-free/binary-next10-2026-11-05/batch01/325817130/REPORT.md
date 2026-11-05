# N010 TIC 325817130: PROBABLE

Selected stratum: repeat_sector_dip; original priority rank 110. Bounded full review complete. Novelty: UNKNOWN.

## Raw signal and source

Deep S12 1635.896 and S100 4079.290 eclipses repeat over ~43 Gaia cycles. Shallower S11 1607.486, S65 3084.901, S99 4050.924 and S101 4107.660 events alternate at ~half the orbital interval, consistent with two eclipse kinds. S12 and S100 TESSCut differences peak near target; target-center pixel drops 2.51/2.84%, while capable G12.04 neighbor-center drops 1.30/1.17%, favoring target spillover to neighbor but not uniquely deblending their PSFs.

## Timing and physics

S12→S100 deep interval /43 gives conditional 56.8231 d. Shallower S11→S101 has k=44 favored by S65/S99 timing over k=43/45; slope-limited shallow centers differ by ~0.04–0.09 d. Reported 56.823 d is rounded same-kind clock, not a precision fit. Gaia SB1 e≈0.002 and P=56.8227 d. Source-specific covariance puts S12 −0.0028 phase (−0.53 linear sigma) from Gaia B conjunction. Orbital geometry is supportive, but close-source ambiguity remains.

## Limits and next check

Capable G12.04 neighbor not fully PRF-deblended; corrected columns suppress long raw events. S102 new cutout has no finite target-flux cadences and cannot yield a null. Next: PSF deblending and joint two-kind fit for secure ownership and depth.

## Reproducibility

Raw q0 SAP sectors, detector windows and coverage are in `screen.json`, `all-sectors.png`, `ranked-windows.png`; local provisional fits in `fitted-windows.json` and `fitted-windows.png`. The verified original paths and SHA256 hashes are in `[local-path-redacted]`. Pixel checks and source hashes are in `../helper-audit.md` and helper-prefixed artifacts. The sector availability receipt is `../../root-availability.json`. New sector validity checks: `../latest-check.json`. Source-specific Gaia conjunction diagnostic: `../gaia-geometry.json`. Catalogues: shared-catalogues/TARGET-STATUS.csv and target-evidence.json. Per-target VSX/ASAS-SN/Kostov gates unavailable; primary-table nonmatches are not novelty clearance.
