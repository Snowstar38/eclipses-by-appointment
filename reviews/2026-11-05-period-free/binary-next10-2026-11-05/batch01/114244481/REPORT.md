# N004 TIC 114244481: PROBABLE

Selected stratum: repeat_sector_dip; original priority rank 104. Bounded full review complete. Novelty: UNKNOWN.

## Raw signal and source

Deep, rounded raw SAP eclipses in S44 2510.814, S45 2531.264 and S72 3267.463 repeat at ~20.45 d; other shallower structures may be opposite-kind events. Independent S44 TESSCut loss is near target (0.24 pixel) with 110 ppt in 5x5 versus 124 ppt QLP SAP. Actual WCS includes a G10.13 neighbor displaced ~2.7 pixels; target-favored difference image and deep loss disfavor it.

## Timing and physics

S44→S45 is 20.44984 d and S45→S72 is 736.199 d (~36×20.45). S72 fit width and ingress are nonidentifiable, so its small formal center error is not used. Actual q0 S44 at BTJD2521.039 fully covers P/2 with −5.8 ppt local depth versus ~130 ppt primary; S44 2517.630 fully covers P/3 with −6.3 ppt; S44 2505.701 covers P/4 with only 8.8 ppt amid smooth variation. Local coverage/gaps, baseline counts, MAD and visual panels are in submultiple-tests.json/png. These reject the neighboring short same-kind clocks; rounded P≈20.450 d is adopted. Gaia SB2 e=0.343 and large RV amplitudes can permit deep eclipses, but Gaia P=20.46508±0.00355 d is ~4.3 nominal sigma from the photometric ~20.450 d. Source-specific covariance calculation puts S44 0.0678 phase early of nearest Gaia A conjunction (~3.95 linear sigma). Gaia-orbit association/geometry therefore remains unresolved.

## Limits and next check

Gaia conjunction and period tension; S72 nonidentifiable timing; crowded aperture depth. Next: Independent precise event centers and Gaia-orbit reconciliation.

## Reproducibility

Raw q0 SAP sectors, detector windows and coverage are in `screen.json`, `all-sectors.png`, `ranked-windows.png`; local provisional fits in `fitted-windows.json` and `fitted-windows.png`. The verified original paths and SHA256 hashes are in `[local-path-redacted]`. Pixel checks and source hashes are in `../helper-audit.md` and helper-prefixed artifacts. The sector availability receipt is `../../root-availability.json`. P/2–P/4 raw null checks: `submultiple-tests.json` and `submultiple-tests.png`. MAST label sector1751 has no validated light curve and was not used as science coverage. Source-specific Gaia conjunction diagnostic: `../gaia-geometry.json`. Catalogues: shared-catalogues/TARGET-STATUS.csv and target-evidence.json. Per-target VSX/ASAS-SN/Kostov gates unavailable; primary-table nonmatches are not novelty clearance.
