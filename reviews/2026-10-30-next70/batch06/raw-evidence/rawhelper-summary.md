# Independent raw-evidence review

QLP event fits and conditional cycle-count linear ephemerides are in raw-events.json. Pixel extractions in pixel-independent-results.json use the same TESS photons, with an independent 3x3 aperture, local faint-pixel background, and core-median depths. Their centers are predicted from the QLP ephemeris: these verify repeated dips, not an independent period fit. Hashes, sector and WCS identity are recorded in the result. Archive reductions and product identity/hash are in independent-results.json; five archive inventories timed out and do not establish absence.

| TIC | QLP period (d) | QLP median fitted depth | TESScut median core depth | depth flag |
|---|---:|---:|---:|---|
| 417917895 | 15.975834 | 0.1456 | 0.1035 | Difference >20% relative |
| 162075402 | 5.327672 | 0.1420 | 0.0988 | Difference >20% relative |
| 29741740 | 11.027858 | 0.1313 | 0.1128 | No >20% difference |
| 48829357 | 17.894784 | 0.1389 | 0.1483 | No >20% difference |
| 115549556 | 6.582222 | 0.1486 | 0.1270 | No >20% difference |
| 90563464 | 15.234219 | 0.1260 | 0.1249 | No >20% difference |
| 156851362 | 4.033257 | 0.1273 | 0.1179 | No >20% difference |
| 273177449 | 5.288131 | 0.1356 | 0.1191 | No >20% difference |
| 144500102 | 5.242787 | 0.1387 | 0.1270 | No >20% difference |
| 177285916 | 6.429546 | 0.1299 | 0.1274 | No >20% difference |

The depth comparison is a screening flag, not a significance test: trapezoid-model depths and aperture core medians differ in weighting, cadence, dilution, and sometimes sector. TIC 417917895 differs by about 29% and 162075402 by 30%; inspect dilution and extraction before equating depths. For 273177449, the 3513.419 event has only 11 in-core points and a shallower core estimate; other events are near 0.117?0.120.

TIC 417917895 TESScut sector 15 is distinct from QLP sectors 14, 22, 75 and recovers two events at predicted cycles. TIC 156851362 has two fitted QLP events in sector 72, so its 4.033257 d value depends on assigned cycles; five TESScut dips support the approximately 4.03 d repetition. TIC 162075402 primary repetition is 5.327672 d; a half-period alias can arise from secondary eclipses and is not adjudicated by this extraction.

Archive reductions: TARS sector 80 for TIC 162075402; TESS-SPOC for 29741740, 48829357, 115549556; SPOC for 156851362. All matched TIC and sector headers. TARS has no QUALITY column; its two fixed-shape depths differ (0.132 and 0.118), while the TESScut core depths are stable near 0.099. Formal fit errors do not include systematic or shape uncertainty.

Period fits assume the search-derived integer cycle assignments; they are descriptive, not uncertainties or proof that all possible aliases are excluded. No source attribution or physical verdict is made here.
