# Q005 / TIC 1535458

**Physical verdict:** PLAUSIBLE; **bounded review:** COMPLETE; **catalogue status:** UNKNOWN.

## Raw evidence

Three broad raw troughs in S5, S32 and S98 near BTJD 1455.8, 2194.2 and 4039.5 have similar steep-drop, partial-rebound, second-low morphology. Their broad centers are compatible with sixteen and forty cycles of Gaia P=46.13747 d. Fresh target-vicinity apertures reproduce the S32 trough and an additional S98 feature near BTJD 4016.6, the Gaia P/2 phase from S32. The latter is a substantial pixel-level feature, not a clean subharmonic null, but its shape differs from 4039.5 and could be opposite-kind variation or orbital modulation. The troughs support recurring photometric variation, yet their double structure and asymmetric trends are not discrete eclipse morphology.

Selected screen windows: S5 1455.869, S32 2194.028, S98 4039.463. These are detector predictions, not adopted eclipse centers. Lead numeric and original source receipts: `lead-measurements.json`; raw plots: `lead-event-panels.png`; same-photon QLP reduction: `lead-alternative.json`. Independent visual and TESSCut checks: `../helper-audit.md` and helper-prefixed artifacts.

## Timing, identity and limits

Frozen Gaia DR3 source 4875254662302883712; selection spectroscopic period 46.137469 d. This is an orbital prior, not a photometric clock or source-specific conjunction match.

Novelty remains UNKNOWN: the queue-wide catalogue audit has no successful fresh VSX/ASAS-SN/Kostov gate for this target; a failed query is not a nonmatch. Physical classification is independent of novelty.

Broad center estimates and widths do not establish a unique same-kind clock. Orbital/periastron modulation and baseline effects remain alternatives. A brighter source about five pixels away and unresolved close neighbors limit ownership; S98 background varies sharply. Same-photon KSPSAP suppression is not an independent physical refutation.

No unsupported photometric period, precision error, primary epoch or depth is adopted. Same-photon reductions are processing comparisons, not independent observing occasions. This bounded verdict concerns the selected bulk lead, not every possible signal from this star.

## Next check

Obtain a clean full event with source-resolved pixels and test aliases and Gaia conjunction geometry.

Gaia-projected windows and actual cadence coverage: `../helper-Q005-predictions.json`; conditional subharmonic windows: `lead-q005-alias-windows.json`. The S98 4016.6 half-period feature and valid target-vicinity aperture are documented in `../helper-Q005-s98-alias.json` and `../helper-Q005-s98-diff.json`, with cutout receipt in `../helper-cut-receipts.json`. These do not prove an orbital eclipse or unique same-kind cycle.
