# F033 / TIC 355789639

**Physical verdict:** PLAUSIBLE; **bounded review:** COMPLETE; **catalogue status:** SCOPED_NONMATCH.

## Raw observation and interpretation

S28 shows a deep ingress immediately before a 2073.8117-2075.3881 BTJD gap and recovery after it; the eclipse center and full core are unobserved. The two S95 detector windows are broad baseline slopes and gap-adjacent steps with no matching deep eclipse morphology. A single partial event does not establish a repeat or clock.

Detector windows and diagnostic local centers: S28 2073.8336, S95 3899.5287, S95 3887.6222. These are not all accepted eclipse centers. Source: `lead-measurements.json` and `lead-event-panels.png`; alternative QLP check: `lead-alternative.json`. Raw QLP FITS SHA256 receipts are in `lead-measurements.json` and the sealed source packet.

## Timing, source and prior identity

Gaia DR3 source 4714307359954109696, selection SB1/SB2 period 46.37530159655366 d. Selection orbit is not itself an eclipse timing measurement. Shared catalogue: `[local-path-redacted]`. SCOPED_NONMATCH; no target EB identification in checked tables.

Adopted measured photometric period: none. Reference measured center: none. Representative raw depth: not robustly adopted.

## Limits and next check

The partial S28 signal may be an eclipse, but its depth and center are not securely measured and source attribution is untested for that event. KSPSAP attenuation on the same photons does not by itself refute it.

Inspect valid source-centered pixels or another complete deep event and then test integer-cycle aliases.

This review is a bounded assessment of the selected bulk lead. Same-photon QLP reductions are processing checks, not another observing occasion. Gaia G-band neighbor flux is approximate. No exhaustive all-sector physical fit or publication claim is implied.
