# X004 / TIC 378411251

Gaia DR3 5253057062489834240; frozen visual10 queue, M524.

Completion: COMPLETE_BOUNDED. Physical tier: **PROBABLE**. Association: SHORT_PERIOD_BY_CATCH.

Sharp repeatable dips in S63/64 yield local consecutive sharp-minimum spacing 3.19139 d from the first six clean S64 events, vastly different from the 58.97741 d Gaia orbit. Stacked TESScut deficit centroid is only 0.19 pixel (~4 arcsec) from target, with a target-centered deficit at TESS resolution (no PSF fit performed). Disappearance in other apertures alone does not refute target attribution. Real repeated eclipse-like events are probable short-period by-catch rather than an established eclipse of the selected Gaia orbit.

Limitations: Unresolved neighbor remains possible because complete capable-neighbor cone queries failed. Same-kind versus opposite-kind doubling and long-baseline ephemeris have not been resolved. DSCT/GDOR/SXPHE catalogue variability does not itself explain these sharp deficits.

Next check: Resolve close blends and obtain repeated independent source photometry; fit both eclipse kinds before assigning orbital period.

## Scope and provenance

Raw QLP SAP was read with finite positive flux and QUALITY=0; source SHA256 and FITS TICID were checked before use. 7 cached sectors were inspected; exact sample membership and queue hash are unchanged. Representative full-sector context and ranked windows are in `all-sectors.png` and `ranked-windows.png`; raw coverage and selected screen windows are in `screen.json`. Detector contrast is a maximized ordering statistic, not calibrated eclipse significance. Event-kind assignments come from raw morphology, not the selection cue.

Alternative TESScut extractions test processing/source location using the same photons, not an independent observing occasion. The bounded review does not require all-event/all-sector precision characterization. Completion means the deciding bounded review is finished and limitations are explicitly adjudicated; it does not mean every possible observation or catalogue has succeeded. Physical tier is independent of catalogue novelty and publication eligibility. Central scoped catalogue receipts are under `../shared-catalogues/`; failed requests are unknown, and no claim of exhaustive priority is made. Parent owns final catalogue/novelty eligibility.

Numeric evidence: `../lead-source-receipts.json`, `../lead-clocks.json`, `../initial-minima-diagnostics.json` (superseded fits explicitly not used), `../lead-deciding-checks.json`, `../lead-gaia-covariance.json`, and helper artifacts where present.
