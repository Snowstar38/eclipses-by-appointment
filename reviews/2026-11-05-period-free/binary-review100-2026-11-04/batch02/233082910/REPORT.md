# H020 — TIC 233082910

**Physical verdict:** REFUTED. **Bounded review:** COMPLETE. **Novelty:** UNKNOWN; four shared VizieR gates were unqueried after a positive-control timeout.

Selected as `cross_method_dip` from the sealed queue. Gaia DR3 source 2158639297271985920 has a spectroscopic period 52.66087411162764 d; that is a selection orbit, not an eclipse period.

Forty raw sectors contain a persistent smooth short-timescale oscillation, with repeated crests and troughs every few days. The many bulk dip and brightening flags select extrema of this oscillation and sector trends; they do not form a 52.66-day eclipse train. This is positive evidence for non-eclipse variability.

**Limitations:** No eclipse ephemeris from this screen. The full available cached raw SAP sectors and representative flagged windows are documented in [raw-inspection.json](raw-inspection.json) and [orbit-context.json](orbit-context.json). The panel centers are screening predictions, not measured eclipse times. The [source packet](../../source-packets/233082910/sources.json) records Gaia metadata and FITS hashes; `inspect_raw.py` independently checked every used FITS hash.

**Next check:** Study the short-period oscillation separately if desired; suppress its harmonics before any new long-period eclipse search.
