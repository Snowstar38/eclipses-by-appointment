# H011 — TIC 158965683

**Physical verdict:** REFUTED. **Bounded review:** COMPLETE. **Novelty:** UNKNOWN; four shared VizieR gates were unqueried after a positive-control timeout.

Selected as `cross_method_dip` from the sealed queue. Gaia DR3 source 4583348069026129920 has a spectroscopic period 56.45654481260243 d; that is a selection orbit, not an eclipse period.

The s80 flagged dip at BTJD 3506.014 is the end of a monotonic ~25 ppt ramp and lies at the sector endpoint; the s80 brightening at 3491.139 is a broad ~42 ppt hump. The earlier s40/s53/s79 raw sectors show no comparable event. These are positive non-eclipse morphology, with the local side-window statistic distorted by the ramp.

**Limitations:** No isolated eclipse center; no physical period or depth reported. The full available cached raw SAP sectors and representative flagged windows are documented in [raw-inspection.json](raw-inspection.json) and [orbit-context.json](orbit-context.json). The panel centers are screening predictions, not measured eclipse times. The [source packet](../../source-packets/158965683/sources.json) records Gaia metadata and FITS hashes; `inspect_raw.py` independently checked every used FITS hash.

**Next check:** No secure eclipse ephemeris. If astrophysical variability is of interest, obtain an independently extracted light curve and inspect the broad hump.
