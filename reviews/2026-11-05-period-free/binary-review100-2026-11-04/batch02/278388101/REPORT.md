# H015 — TIC 278388101

**Physical verdict:** REFUTED. **Bounded review:** COMPLETE. **Novelty:** UNKNOWN; four shared VizieR gates were unqueried after a positive-control timeout.

Selected as `cross_method_dip` from the sealed queue. Gaia DR3 source 4518693040111462400 has a spectroscopic period 48.1466138019085 d; that is a selection orbit, not an eclipse period.

The s80 flagged dip at 3492.604 is an asymmetric broad descent into a flat low state near an internal gap; the flagged brightening at 3504.320 is an irregular broad hump. s26/s40/s53/s54 do not show a matching shape. The raw profile supplies positive evidence for slow variability or reduction artifacts rather than an isolated eclipse.

**Limitations:** No eclipse ephemeris. The full available cached raw SAP sectors and representative flagged windows are documented in [raw-inspection.json](raw-inspection.json) and [orbit-context.json](orbit-context.json). The panel centers are screening predictions, not measured eclipse times. The [source packet](../../source-packets/278388101/sources.json) records Gaia metadata and FITS hashes; `inspect_raw.py` independently checked every used FITS hash.

**Next check:** If pursuing the variable, compare custom pixel extraction across the s80 state changes.
