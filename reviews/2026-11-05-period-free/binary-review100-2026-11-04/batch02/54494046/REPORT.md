# H012 — TIC 54494046

**Physical verdict:** PROBABLE. **Bounded review:** COMPLETE. **Novelty:** UNKNOWN; four shared VizieR gates were unqueried after a positive-control timeout.

Selected as `cross_method_dip` from the sealed queue. Gaia DR3 source 3373132589745512704 has a spectroscopic period 58.95458539010055 d; that is a selection orbit, not an eclipse period.

Raw s45 BTJD 2527.768 and s72 BTJD 3264.431 show deep, smooth, roughly 2-day troughs. The s43 ending near 2498 and s71 beginning near 3235 show partial analogous troughs. Across three flux thresholds, s43 ingress to s72 ingress spans 13 cycles at 58.926–58.931 d, while s45 egress to s71 egress spans 12 cycles at 58.928–58.929 d. Adjacent integer aliases give incompatible clocks (about 54.4–54.7 or 63.8–64.3 d); thus four independent occasions support two alternating eclipse kinds. The two full minima alone are opposite kinds and cannot set the clock. The s72 TESSCut alternate extraction retains the broad trough (42.5 ppt core-to-side statistic, biased low by in-event side baseline) and difference centroid lies 0.067 pixel from target, but two Gaia neighbors at 12.67 and 18.00 arcsec are capable under approximate G-band bounds; attribution remains unresolved.

**Limitations:** Contact threshold alias diagnostics in partial-contact-aliases.json are not a formal ephemeris; Gaussian descriptive minima and QLP SAP depth in measured-events.json; no secure period error or primary epoch. The full available cached raw SAP sectors and representative flagged windows are documented in [raw-inspection.json](raw-inspection.json) and [orbit-context.json](orbit-context.json). The panel centers are screening predictions, not measured eclipse times. The [source packet](../../source-packets/54494046/sources.json) records Gaia metadata and FITS hashes; `inspect_raw.py` independently checked every used FITS hash.

**Next check:** Resolve capable neighbors with multi-aperture/difference-image modeling and measure an additional complete same-kind eclipse.
