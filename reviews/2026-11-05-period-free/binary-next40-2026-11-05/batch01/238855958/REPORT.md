# F007 TIC 238855958: CONFIRMED

Selected stratum: repeat_sector_dip; original priority rank 117. Bounded physical review complete. Catalogue status: SCOPED_NONMATCH.

## Raw events and alternative extraction

Narrow, similar raw SAP eclipses occur in S1 1337.722, S67 3132.851, S68 3171.042, S94 3858.534 and S95 3896.731. The short 38.191-day consecutive spacing recurs after 18 cycles and again one cycle later, supporting ~38.193 days from measured centers; broad S103/S104 gap-edge features are excluded. The explicit shorter-period test finds four fully covered sensitive P/2 nulls, seven P/3 nulls and fourteen P/4 nulls in real q0 cadence windows. Representative visually inspected S94 P/2 BTJD3877.615 has 112 continuous core points, max gap 0.0023 d, -0.05 ppt local depth and 0.49-ppt sideband MAD noise; S67 P/3 BTJD3145.582 has 112 points, gap 0.0023 d, +0.06 ppt depth and 0.86-ppt noise, versus ~7-ppt real events. S1 target-centered TESSCut recovers a ~7.26-ppt resolved dip.

## Timing, source and Gaia geometry

S1 difference deficit is centered within ~0.20 pixel of target. The nearest nominally capable Gaia neighbor is 4.46 pixels away, so source location and aperture throughput strongly favor the target. Gaia SB1 P38.229 +/-0.040 days agrees with the measured clock within its period uncertainty; the S94 source-specific B/A conjunction comparison has a broad compatible A offset (-0.073 phase, -0.73 linear sigma).

## Limits and next check

S1 timing covariance is singular; reported period is rounded from multiple good later events with no formal uncertainty. Shorter-alias nulls assume similar same-kind ~7-ppt eclipses. Alternative extraction shares TESS photons. Next: A later resolved eclipse would tighten the ephemeris.

## Evidence and scope

Verified source FITS identities and hashes: `../../source-packets/238855958/sources.json`. Raw q0 context: `all-sectors.png`, `ranked-windows.png`, `screen.json`; provisional local fits: `fitted-windows.json` and plot. Hand-selected cycle arithmetic: `../review-clocks.json`. Source-specific Gaia diagnostics: `../gaia-geometry.json` and F002 `../abfg-geometry.json`. Independent same-photon TESSCut and WCS: `../helper-audit.md` plus helper-prefixed artifacts. Current sector availability: `../../root-availability.json`. Queue-scoped catalogue receipts: `../../shared-catalogues/TARGET-STATUS.csv` and `target-evidence.json`. F006 repeat morphology and invalid S65: `../f006-overlay.json`, `../f006-s65.json`; F007 shorter aliases and visual null comparison: `../f007-aliases.json`, `../f007-null-preview.png`; F008 partial-cycle coverage and two-kind interval arithmetic: `../helper-F008-coverage.json`, `../helper-F008-deep-coverage.json`, `../f008-cycle-intersection.json`; F010 raw overlay and unresolved aliases: `../f010-overlay.json`, `../f010-aliases.json`. Screening centers are predictions; fitted local centers with singular or bound-hitting covariance are not precision epochs. No source in another reduction supplies a new observing occasion.
