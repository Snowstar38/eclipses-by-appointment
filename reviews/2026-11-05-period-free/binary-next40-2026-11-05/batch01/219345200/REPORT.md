# F002 TIC 219345200: PROBABLE

Selected stratum: repeat_sector_dip; original priority rank 112. Bounded physical review complete. Catalogue status: SCOPED_NONMATCH.

## Raw events and alternative extraction

Resolved short raw SAP dips in S4 1434.925, S31 2153.951, S97 3951.547 and S98 4011.467 repeat at ~59.919 days. Target-centered TESSCut 3x3 extraction independently recovers ~4.31 ppt in S4. The S97 detector fit at 3941.719 is a separate spurious/broad feature and is excluded from the clock.

## Timing, source and Gaia geometry

Gaia AstroSpectroSB1 ABFG gives inclination 87.18 degrees and omega 158.09 degrees, near C/H check 155.11 degrees. Source-specific full-covariance A conjunction predicts 1434.712 +/- 0.224 d; observed offset +0.213 d. The nearest Gaia neighbor lies just 0.475 pixel away, G ratio 0.00315 versus measured 0.00431 fractional loss; nominal G-band total disappearance falls short, but TESS bandpass and aperture contributions prevent decisive exclusion.

## Limits and next check

Real repeated eclipses and compatible Gaia geometry; close capable or near-capable neighbor prevents firm source ownership. Period is approximate from representative raw centers, not a calibrated ephemeris error. Next: Obtain higher-resolution eclipse photometry or a multi-pixel PSF fit across separate events.

## Evidence and scope

Verified source FITS identities and hashes: `../../source-packets/219345200/sources.json`. Raw q0 context: `all-sectors.png`, `ranked-windows.png`, `screen.json`; provisional local fits: `fitted-windows.json` and plot. Hand-selected cycle arithmetic: `../review-clocks.json`. Source-specific Gaia diagnostics: `../gaia-geometry.json` and F002 `../abfg-geometry.json`. Independent same-photon TESSCut and WCS: `../helper-audit.md` plus helper-prefixed artifacts. Current sector availability: `../../root-availability.json`. Queue-scoped catalogue receipts: `../../shared-catalogues/TARGET-STATUS.csv` and `target-evidence.json`. F006 repeat morphology and invalid S65: `../f006-overlay.json`, `../f006-s65.json`; F007 shorter aliases and visual null comparison: `../f007-aliases.json`, `../f007-null-preview.png`; F008 partial-cycle coverage and two-kind interval arithmetic: `../helper-F008-coverage.json`, `../helper-F008-deep-coverage.json`, `../f008-cycle-intersection.json`; F010 raw overlay and unresolved aliases: `../f010-overlay.json`, `../f010-aliases.json`. Screening centers are predictions; fitted local centers with singular or bound-hitting covariance are not precision epochs. No source in another reduction supplies a new observing occasion.
