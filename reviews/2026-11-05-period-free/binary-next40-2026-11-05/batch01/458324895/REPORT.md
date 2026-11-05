# F010 TIC 458324895: PROBABLE

Selected stratum: repeat_sector_dip; original priority rank 120. Bounded physical review complete. Catalogue status: SCOPED_NONMATCH.

## Raw events and alternative extraction

Broad flat-bottom raw losses repeat in S12 ~1649.35, S39 ~2377.50, S66 ~3105.50 and S93 ~3833.89. Independent local sideband overlays show similar ~21-24-ppt core losses in each sector; S39 lacks most pre-baseline and S66 lacks post-baseline, so those depth figures are diagnostic only. A second, shallower kind appears around S12 1632.86 and S93 3850.35. S93 target-centered extraction retains a ~25-ppt broad trough.

## Timing, source and Gaia geometry

If the four deep events span 66 cycles, the conditional period is ~33.099 days; 63 and 69 cycles over the same baseline (~34.675 and ~31.660 days) also align the three ~728-day gaps, while bounded cache coverage has no strong null to reject them. The other-kind pair is too sparse to determine its cycle count independently. Gaia SB1 P33.089 days favors the 66-cycle alias and near-circular geometry predicts a B conjunction ~0.027 phase from S93 (1.8 linear sigma), but Gaia agreement is not a measured unique eclipse clock. Difference flux is within ~0.30 pixel of target; nominally capable Gaia neighbors are 3.7-4.4 pixels away and aperture throughput favors the target.

## Limits and next check

Real repeated broad eclipses have unresolved integer aliases; no measured orbital period is adopted. S39/S66 incomplete baselines and same-photon alternative extraction limit depth and source precision. Next: Observe a deep eclipse at a discriminating intermediate cycle and repeat target-centered pixels.

## Evidence and scope

Verified source FITS identities and hashes: `../../source-packets/458324895/sources.json`. Raw q0 context: `all-sectors.png`, `ranked-windows.png`, `screen.json`; provisional local fits: `fitted-windows.json` and plot. Hand-selected cycle arithmetic: `../review-clocks.json`. Source-specific Gaia diagnostics: `../gaia-geometry.json` and F002 `../abfg-geometry.json`. Independent same-photon TESSCut and WCS: `../helper-audit.md` plus helper-prefixed artifacts. Current sector availability: `../../root-availability.json`. Queue-scoped catalogue receipts: `../../shared-catalogues/TARGET-STATUS.csv` and `target-evidence.json`. F006 repeat morphology and invalid S65: `../f006-overlay.json`, `../f006-s65.json`; F007 shorter aliases and visual null comparison: `../f007-aliases.json`, `../f007-null-preview.png`; F008 partial-cycle coverage and two-kind interval arithmetic: `../helper-F008-coverage.json`, `../helper-F008-deep-coverage.json`, `../f008-cycle-intersection.json`; F010 raw overlay and unresolved aliases: `../f010-overlay.json`, `../f010-aliases.json`. Screening centers are predictions; fitted local centers with singular or bound-hitting covariance are not precision epochs. No source in another reduction supplies a new observing occasion.
