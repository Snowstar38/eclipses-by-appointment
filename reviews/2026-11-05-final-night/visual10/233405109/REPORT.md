# X003 / TIC 233405109

Gaia DR3 2186340015269024768; frozen visual10 queue, M271.

Completion: COMPLETE_BOUNDED. Physical tier: **CONFIRMED**. Association: GAIA_ASSOCIATED.

Five representative same-kind resolved raw events in S55/56/76/81/83 give P48.58726285 d and epoch 2802.44939 BTJD, cycles 0,1,12,15,16, descriptive residuals within 0.034 d. Covered intermediate predictions reject shorter integer aliases 2-10, including seven P/2 windows; the selected 24.2948 d screen cue had mixed absent opposite windows. S76 custom aperture retains 2.61 ppt; difference peak(4,5) coincides with target(4.12,4.80). The actual Gaia conjunction B has median offset-0.091 d,95%[-0.877,+0.663]d under full published SB1 covariance. Seven conservatively capable Gaia neighbors inside 108 arcsec start 55.82 arcsec away and do not explain the target-centered deficit.

Limitations: Period is a representative centroid fit, with no calibrated total timing error. Covariance MC rejects unphysical eccentricity draws; edge-on conjunction is an approximation. Independent custom reduction shares photons, and unresolved companions are not excluded at TESS resolution.

Next check: Obtain higher angular resolution eclipse photometry or a precision timing model if characterization is desired.

## Scope and provenance

Raw QLP SAP was read with finite positive flux and QUALITY=0; source SHA256 and FITS TICID were checked before use. 13 cached sectors were inspected; exact sample membership and queue hash are unchanged. Representative full-sector context and ranked windows are in `all-sectors.png` and `ranked-windows.png`; raw coverage and selected screen windows are in `screen.json`. Detector contrast is a maximized ordering statistic, not calibrated eclipse significance. Event-kind assignments come from raw morphology, not the selection cue.

Alternative TESScut extractions test processing/source location using the same photons, not an independent observing occasion. The bounded review does not require all-event/all-sector precision characterization. Completion means the deciding bounded review is finished and limitations are explicitly adjudicated; it does not mean every possible observation or catalogue has succeeded. Physical tier is independent of catalogue novelty and publication eligibility. Central scoped catalogue receipts are under `../shared-catalogues/`; failed requests are unknown, and no claim of exhaustive priority is made. Parent owns final catalogue/novelty eligibility.

Numeric evidence: `../lead-source-receipts.json`, `../lead-clocks.json`, `../initial-minima-diagnostics.json` (superseded fits explicitly not used), `../lead-deciding-checks.json`, `../lead-gaia-covariance.json`, and helper artifacts where present.
