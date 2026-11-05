# H016 — TIC 467963921

**Physical verdict:** PROBABLE. **Bounded review:** COMPLETE. **Novelty:** UNKNOWN; four shared VizieR gates were unqueried after a positive-control timeout.

Selected as `cross_method_dip` from the sealed queue. Gaia DR3 source 6438459789808462592 has a spectroscopic period 49.7807524998903 d; that is a selection orbit, not an eclipse period.

Three clean narrow raw SAP dips occur in s66, s94 and s103 at BTJD 3119.898, 3865.640 and 4163.932. The 15- and 6-cycle spacings each give about 49.716 d; quality-zero coverage excludes a 24.858-day half-period alias at s67, s93 and s104. Independent TESSCut extraction of s94 retains ~13.5 ppt depth; its difference centroid is 0.094 pixel from the WCS target. The brightest listed Gaia neighbor in 60 arcsec is far too faint under an approximate G/full-inclusion disappearance bound. Simple Gaia conjunction predictions are 4–5 days later; covariance-aware orbital compatibility has not been established.

**Limitations:** Descriptive raw Gaussian centers and depths in measured-events.json; no formal timing error. The full available cached raw SAP sectors and representative flagged windows are documented in [raw-inspection.json](raw-inspection.json) and [orbit-context.json](orbit-context.json). The panel centers are screening predictions, not measured eclipse times. The [source packet](../../source-packets/467963921/sources.json) records Gaia metadata and FITS hashes; `inspect_raw.py` independently checked every used FITS hash.

**Next check:** Resolve Gaia phase/covariance and test other plausible orbital geometry; retain the measured eclipse period separate from Gaia P.
