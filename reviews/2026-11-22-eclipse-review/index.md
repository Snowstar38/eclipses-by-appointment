# November 2026 eclipse review

**107 systems** are included in this release. The available measurements support a confirmed classification for **88** and a probable classification for **19**. The catalogue and literature checks found no earlier eclipse candidate for **20** systems. The other **87** are validations of earlier machine-selected candidates. Publication history and the physical classification are tracked separately.

| Earlier eclipse evidence | Confirmed | Probable | Total |
|---|---:|---:|---:|
| No earlier candidate in the sources checked | 15 | 5 | 20 |
| Prior machine-selected candidate | 73 | 14 | 87 |
| Total | 88 | 19 | 107 |

- [Host table, R839–R945](host-stars.csv) gives identifiers, sky coordinates, adopted periods, reference epochs, evidence summaries and limitations.
- [Host measurements](host-evidence.json) links each TIC to visit-level eclipse checks, source localization, catalogue comparisons and available archive identifiers and hashes.
- [Outcomes for all 352 selected fields](field-outcomes.csv) and [field measurements](field-evidence.json) include sources withheld for insufficient, contaminated or non-eclipsing evidence.
- [Methods and data dictionary](methods.md) explains the physical tiers, epochs, controls and evidence structure.

The 352 selected fields comprise 83 priority fields, 204 follow-up fields and 65 periodic radial-velocity variables. The eclipse evidence supports 106 of the originally selected stars. A separately localized eclipsing neighbor, [TIC 26427360](examples/TIC-26427360.md), completes the 107-host table. This distinction makes it possible to plan follow-up at the position of the star that actually fades.

## Additional analyses

- [TIC 34691042](examples/TIC-34691042.md) has three six-hour TESS eclipses, with six surviving period alternatives. The system remains outside the count while the eclipse clock and its relationship to a known spectroscopic binary are tested.
- [TGV-184 A observer note](examples/TGV-184.md) gives two observing windows for testing the proposed 90.36632-day clock and shows the partial 2007 SuperWASP egress. This is an orbital result for a published system.
- [Reproduce compact diagnostic plots](examples/plot-examples.py) uses the released phase, flux and difference-image data.
