# X008 / TIC 381548065

Gaia DR3 5944937948374623744; frozen visual10 queue, M526.

Completion: COMPLETE_BOUNDED. Physical tier: **PLAUSIBLE**. Association: SINGLE_AMBIGUOUS_EVENT.

S39 BTJD2367.88 has a credible dip-like feature but its egress is interrupted by a data gap. S1044197.4 is an asymmetric ramp into a gap; S1034159.9 is a gap-related step. These do not establish same-kind recurrence or the 28.5863 d screening cue. A current TESScut sector query returns exactly cached sectors 13,39,66,93,103,104, with no newer science sector available.

Limitations: No secure clock, source attribution, second extraction or Gaia geometry exists for the possible singleton. Missing checks remain limitations of a plausible signal; gap windows are not clean nulls.

Next check: Obtain another well-covered event and source localization before assigning an EB period.

## Scope and provenance

Raw QLP SAP was read with finite positive flux and QUALITY=0; source SHA256 and FITS TICID were checked before use. 6 cached sectors were inspected; exact sample membership and queue hash are unchanged. Representative full-sector context and ranked windows are in `all-sectors.png` and `ranked-windows.png`; raw coverage and selected screen windows are in `screen.json`. Detector contrast is a maximized ordering statistic, not calibrated eclipse significance. Event-kind assignments come from raw morphology, not the selection cue.

Alternative TESScut extractions test processing/source location using the same photons, not an independent observing occasion. The bounded review does not require all-event/all-sector precision characterization. Completion means the deciding bounded review is finished and limitations are explicitly adjudicated; it does not mean every possible observation or catalogue has succeeded. Physical tier is independent of catalogue novelty and publication eligibility. Central scoped catalogue receipts are under `../shared-catalogues/`; failed requests are unknown, and no claim of exhaustive priority is made. Parent owns final catalogue/novelty eligibility.

Numeric evidence: `../lead-source-receipts.json`, `../lead-clocks.json`, `../initial-minima-diagnostics.json` (superseded fits explicitly not used), `../lead-deciding-checks.json`, `../lead-gaia-covariance.json`, and helper artifacts where present.
