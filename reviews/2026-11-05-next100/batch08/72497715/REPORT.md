# Q075 TIC 72497715

Physical verdict: **PLAUSIBLE**. Review completion: **COMPLETE**. EB novelty: **UNKNOWN**.

S99 has two broad raw SAP V-shaped depressions at about 4053.25 and 4068.06 BTJD, 14.81 d apart, with good FFI core/comparison counts. A MAST TIC cone finds a 3.51-times-target T-band source at 49 arcsec, WCS (6.93,2.98), near both difference peaks (6,3), plus a 0.37-times-target neighbor at 19.7 arcsec; these are capable alternatives. S101 has a further dip near 4120.04 but its center is split by a gap; S10 flags are much weaker in KSPSAP. The two clean S99 events are the same observing sector, and no unique integer-cycle clock is established across S101. Helper difference images of the S99 pair both peak one to two pixels below the target, with centroids about one pixel away, so source ownership remains open.

The raw SAP sector plot is `lead-raw-context.png`; every selected dip has raw cadence values in `lead-local-series.json` and actual endpoints/gaps in `lead-flag-diagnostics.json`. Source file hashes are in `../LEAD-SOURCE-HASHES.json`; sectors reviewed: 10,37,64,99,100,101. The screening centers are predictions, not fitted centers. VSX direct receipt: `[local-path-redacted]` (queried 2026-11-05; exact identity assessed separately from physical verdict).

Limitations: These could be eclipses from a nearby source or structured/systematic variability; same-sector recurrence and fractional-pixel centroids do not settle that.

Next check: Resolve the bright TIC neighbors with higher-resolution time-series photometry and obtain a second-sector target-centered difference image at a predicted same-kind event.
