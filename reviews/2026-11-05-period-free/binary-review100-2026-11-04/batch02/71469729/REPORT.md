# H018 — TIC 71469729

**Physical verdict:** REFUTED. **Bounded review:** COMPLETE. **Novelty:** UNKNOWN; four shared VizieR gates were unqueried after a positive-control timeout.

Selected as `cross_method_dip` from the sealed queue. Gaia DR3 source 2998862100122116224 has a spectroscopic period 57.501197479246 d; that is a selection orbit, not an eclipse period.

The s6 flags around 1483.8 and 1486.5 are embedded in irregular broad fluctuations; the s98 4010.061 dip is an abrupt discontinuity at a gap with sloping shoulders. s87 and s98 also contain bright humps with no stable eclipse profile. The repeated screening labels mix different physical shapes and do not establish same-kind recurrence.

**Limitations:** No eclipse period, epoch, or depth. The full available cached raw SAP sectors and representative flagged windows are documented in [raw-inspection.json](raw-inspection.json) and [orbit-context.json](orbit-context.json). The panel centers are screening predictions, not measured eclipse times. The [source packet](../../source-packets/71469729/sources.json) records Gaia metadata and FITS hashes; `inspect_raw.py` independently checked every used FITS hash.

**Next check:** Inspect the irregular variability as a separate source if of interest; seek independent raw events before an eclipse claim.
