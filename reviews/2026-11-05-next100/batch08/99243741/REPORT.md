# Q080 TIC 99243741

Physical verdict: **PROBABLE**. Review completion: **COMPLETE**. EB novelty: **KNOWN**.

Measured S7 and S34 raw SAP centers near 1501.440 and 2235.630 BTJD anchor two broad troughs with covered cores and visible ingress/egress. The S87 3670.09 and S88 3703.56 screening windows show further broad depressions on a repeated ~33.38-d branch; S33 2218.97 and S87 3687.31 may belong to the opposite branch. The S7–S34 separation of ~734.19 d is compatible with 22 Gaia 33.3822-d cycles or 11 cycles at twice that period, but S87/S88 are affected by gaps or strong waves and KSPSAP suppresses the broad raw structure. S7 and S34 have continuously sampled troughs, and independent 3x3 sky-subtracted FFI reductions preserve 8.58 and 5.52 ppt losses. Their loss centroids lie within about half a pixel of the target; capable Gaia neighbors are ~2.5–2.8 pixels from the difference centroids. VSX ASAS J071145-2226.6 is an exact-position ESD|ED EB with historical P65.8 d, which does not resolve the raw cycle count or confirm each window.

The raw SAP sector plot is `lead-raw-context.png`; every selected dip has raw cadence values in `lead-local-series.json` and actual endpoints/gaps in `lead-flag-diagnostics.json`. Source file hashes are in `../LEAD-SOURCE-HASHES.json`; sectors reviewed: 7,33,34,87,88. The screening centers are predictions, not fitted centers. VSX direct receipt: `[local-path-redacted]` (queried 2026-11-05; exact identity assessed separately from physical verdict).

Limitations: S7/S34 centers are approximate local fits, with shape and baseline systematics rather than formal timing errors. S87 ingress and S88 egress are gapped, and their timing cannot resolve P versus 2P. The VSX 65.8-d and Gaia 33.38-d clocks differ, and an orbital harmonic remains possible. Difference images are not a formal PRF fit.

Next check: Fit complete target-centered eclipses over independent sectors and test both 33.38-d and 65.8-d alias families.
