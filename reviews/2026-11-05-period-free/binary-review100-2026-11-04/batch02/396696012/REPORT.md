# H014 — TIC 396696012

**Physical verdict:** REFUTED. **Bounded review:** COMPLETE. **Novelty:** UNKNOWN; four shared VizieR gates were unqueried after a positive-control timeout.

Selected as `cross_method_dip` from the sealed queue. Gaia DR3 source 4779324987198360448 has a spectroscopic period 37.323869475322155 d; that is a selection orbit, not an eclipse period.

All eight raw sectors show repeated smooth waves with characteristic spacing of several days, including alternating bright crests and broad troughs. The s31/s97/s98 flagged dips are pieces of this changing waveform; the s97/s98 recurrence does not identify a 37.32-day eclipse kind. Full-sector context provides positive evidence for quasi-periodic non-eclipse variability.

**Limitations:** No eclipse period, epoch, or depth. The full available cached raw SAP sectors and representative flagged windows are documented in [raw-inspection.json](raw-inspection.json) and [orbit-context.json](orbit-context.json). The panel centers are screening predictions, not measured eclipse times. The [source packet](../../source-packets/396696012/sources.json) records Gaia metadata and FITS hashes; `inspect_raw.py` independently checked every used FITS hash.

**Next check:** Characterize the shorter-period variability separately if desired; do not infer an eclipse period from these screening windows.
