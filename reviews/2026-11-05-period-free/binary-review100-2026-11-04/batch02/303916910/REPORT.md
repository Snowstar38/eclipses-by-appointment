# H017 — TIC 303916910

**Physical verdict:** REFUTED. **Bounded review:** COMPLETE. **Novelty:** UNKNOWN; four shared VizieR gates were unqueried after a positive-control timeout.

Selected as `cross_method_dip` from the sealed queue. Gaia DR3 source 6437492253937494528 has a spectroscopic period 58.097882229597154 d; that is a selection orbit, not an eclipse period.

The only flagged s101 dip at 4112.908 is a monotonic descent cut off by a multi-day gap and followed by a shifted baseline. Eight other raw sectors do not show an analogous isolated trough. The plot supports a gap/baseline artifact interpretation for this screening window.

**Limitations:** No eclipse ephemeris. The full available cached raw SAP sectors and representative flagged windows are documented in [raw-inspection.json](raw-inspection.json) and [orbit-context.json](orbit-context.json). The panel centers are screening predictions, not measured eclipse times. The [source packet](../../source-packets/303916910/sources.json) records Gaia metadata and FITS hashes; `inspect_raw.py` independently checked every used FITS hash.

**Next check:** No eclipse follow-up warranted from this event alone; reassess if a new independent occasion appears.
