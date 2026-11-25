# TIC 160193535 eclipse timings

The shortest orbital clock that fits two recurring eclipse families is **17.1488321 days**. The deeper minimum follows BTJD = 2944.6101382 + 17.1488321 × E. The shallower minimum follows 8.6482104 days later, at phase 0.5043032. The following deeper minimum is 8.5006218 days after the shallower one. BTJD is BJD in TDB minus 2457000.

The fit uses 27 complete eclipse windows from all 13 indexed TESS-SPOC sectors. The 4 additional partial eclipses were fitted independently and evaluated against the ephemeris. The complete-event residual scatter is 0.167 minutes. Removing one sector at a time gives periods from 17.14883165 to 17.14883279 days and secondary lags from 8.64817161 to 8.64824592 days. These ranges describe sensitivity to sector removal. SAP and PDCSAP reductions share the same pixels. Their complete-event centers differ by a median 0.030 minutes.

## Eclipse families

| Family | Complete | Partial | Complete PDCSAP minimum depth, median (range) | Complete SAP median depth |
| --- | ---: | ---: | --- | ---: |
| Deeper | 17 | 2 | 198.3 ppt (195.2–201.2) | 195.8 ppt |
| Shallower | 10 | 2 | 162.9 ppt (160.8–164.0) | 161.3 ppt |

Centers were found before folding through a sector-normalized PDCSAP dip search, requiring at least two points deeper than 45 ppt. Fits use an exposure-integrated symmetric eclipse profile and a linear local baseline. Separate SAP and PDCSAP center fits share empirical family profile shapes and are averaged for the timing fit. Complete-event coverage requires at least 78% sampling in the central ±0.10 d and both 0.13–0.28 d shoulder windows, with a central gap less than 2.1 times local cadence.

## Alternative clocks and coverage

| Trial | Result |
| --- | --- |
| 17.1488321 d, two families | 27 complete matches, 4 partial matches, 7 predicted centers with no core data, and zero covered blanks. |
| 12.13261 d, independently rephased families | Zero of 31 centers match within 0.012 d. One lies within 0.11 d. The fit predicts 45 fully covered blank windows. |
| 8.5744161 d, one family | Predicted centers are displaced by about 53 minutes from each eclipse. Depth and spacing alternate at the observed centers. |
| 8.5744161 d, two families | Fits the centers arithmetically by predicting two minima separated by 0.0737943 d at every repeat. Where both are covered, one minimum is observed in the approximately five-hour event profile. The extra predicted center lands on the flank, without a separate eclipse. |
| 4.2872, 5.7163 and 3.4298 d two-family subharmonics | These match centers arithmetically but respectively predict 65, 63 and 125 fully covered blank windows. |
| 34.2976642 d | A two-family fit misses the observed adjacent same-family repeats. A four-phase model reproduces every 17.15 d prediction by construction. Even and odd median depths differ by 0.65 ppt for deeper eclipses and 0.39 ppt for shallower eclipses, within the respective depth ranges. Photometry disfavors adding a longer cycle without further evidence. |

The seven unobserved prediction centers fall between the neighboring quality-zero cadences listed below. The partial events in sectors 52, 53 and 79 lost their right shoulder, and sector 86 lost its left shoulder.

| Sector | Prediction BTJD | Last prior cadence | First following cadence |
| --- | ---: | ---: | ---: |
| 20 | 1855.733093 | 1854.846050 | 1856.429371 |
| 40 | 2404.495721 | 2404.383576 | 2405.334971 |
| 47 | 2593.132874 | 2592.956750 | 2595.838650 |
| 60 | 2953.258349 | 2949.766851 | 2955.044573 |
| 73 | 3287.586781 | 3286.093040 | 3289.238893 |
| 73 | 3304.735613 | 3299.493578 | 3306.194959 |
| 86 | 3656.360466 | 3650.605364 | 3658.332270 |

Archive provenance and checksums are in ephemeris.json and archive.json. Events, every predicted window for the tested clocks, and the timing figure are in events.csv, coverage.csv and timing.png. All sectors in the local index were included. The two-minute SPOC index has no matching entry.
