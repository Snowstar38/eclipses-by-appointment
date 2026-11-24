# November 23 review of pipeline detections and ground-survey binaries

**855 systems** are included in this release from three searches. The measurements support a confirmed classification for **506** and a probable classification for **349**. The catalogue and literature checks found no earlier eclipse candidate for **113** systems. The other **742** are validations of earlier machine-selected candidates: the unvetted machine-learning list of Kostov et al. (2025, table 2) and/or the Gaia DR3 variability classifier. Publication history and the physical classification are tracked separately.

| Earlier eclipse evidence | Confirmed | Probable | Total |
|---|---:|---:|---:|
| No earlier candidate in the sources checked | 39 | 74 | 113 |
| Prior machine-selected candidate | 467 | 275 | 742 |
| Total | 506 | 349 | 855 |

| Search | Stars reviewed | Confirmed | Probable | No earlier candidate | Prior machine candidate | Added |
|---|---:|---:|---:|---:|---:|---:|
| SPOC two-minute threshold-crossing events not promoted to objects of interest | 299 | 132 | 79 | 36 | 175 | **211** |
| TESS-SPOC full-frame threshold-crossing events not promoted to objects of interest | 348 | 246 | 56 | 16 | 286 | **302** |
| Spectroscopic binaries from ground-based surveys (LAMOST, APOGEE, GALAH, RAVE, Gaia-ESO) | 923 | 128 | 214 | 61 | 281 | **342** |

Three stars were reviewed in two searches, so the column sums to 1,570.

- [Host table, R946–R1802](host-stars.csv) gives identifiers, sky coordinates, the search that found each system, adopted periods and reference epochs, depths, attribution, ground-survey detections, the reason for the tier and its limitation.
- [All 1,567 reviewed stars](reviewed-stars.csv) with the outcome of each review, including stars not added.
- [Methods and data dictionary](methods.md) explains the three searches, the criteria and the limitations.
- Summary figures: [periods](figures/periods.png), [depths](figures/depths.png) and [systems by search and earlier evidence](figures/flag-split.png); [plotting code](figures/plot-summary.py).
- [Diagnostic sheets](sheets/index.md) for 167 of the 855 systems, including every system whose tier was decided by adjudication.

This review replaces the dated proposal of the same day, which listed 654 systems before the visual review described in the methods. An independent audit (dated November 24) checked the 756 systems first published on November 23 against these criteria. Following it, four confirmed systems were moved to probable (R1053, R1337, R1431, R1501), two systems with two equal minima per orbit below 0.5 d were withdrawn and their numbers retired (R988, R1008), and period, depth, event-count and secondary-eclipse columns were corrected for rows whose period had been refitted. Where the secondary eclipse was the deeper, the epoch now marks the deeper eclipse. The systems were selected from searches, not from a defined population, so the counts are not occurrence rates.

![Systems added by search, tier and earlier eclipse evidence](figures/flag-split.png)
