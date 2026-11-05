# H013 — TIC 231694897

**Physical verdict:** PLAUSIBLE. **Bounded review:** COMPLETE. **Novelty:** UNKNOWN; four shared VizieR gates were unqueried after a positive-control timeout.

Selected as `cross_method_dip` from the sealed queue. Gaia DR3 source 6458496052761193856 has a spectroscopic period 57.96837228122208 d; that is a selection orbit, not an eclipse period.

The one s94 candidate near BTJD 3875.114 is a shallow ~5 ppt asymmetric depression followed by a ~1-day gap and different post-gap baseline. Seven cached QLP sectors show no comparable secure event. The live MAST TESSCut inventory adds s1, s103 and s105. s105 has measurable target flux and quality-zero cadence at conditional BTJD 4222.924 (s94 event plus six Gaia periods) without a comparable dip, though a slow local slope and the unmeasured s94 center limit that null. s103 cutout has only near-zero net target counts, so its central coverage cannot be counted as a null; s1 cutout returned no usable FFIs. These additional outcomes do not positively refute a one-off eclipse.

**Limitations:** Single insecure event; no period, epoch, or depth fit. Missing-sector receipts and local-background TESSCut measurements in missing-cutout-review.json; s103/s1 unusable. The full available cached raw SAP sectors and representative flagged windows are documented in [raw-inspection.json](raw-inspection.json) and [orbit-context.json](orbit-context.json). The panel centers are screening predictions, not measured eclipse times. The [source packet](../../source-packets/231694897/sources.json) records Gaia metadata and FITS hashes; `inspect_raw.py` independently checked every used FITS hash.

**Next check:** Obtain an independent s94 pixel extraction and a new raw observing occasion if the source remains of interest.
