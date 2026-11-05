# Q025 / TIC 70887357

**Physical verdict:** PLAUSIBLE. **Novelty:** KNOWN.

## Raw result

S5 BTJD 1454.341 and S32 BTJD 2178.169 show similar short, approximately 3-ppt raw dips, also present in KSPSAP on the same photons. Independent TESSCut difference loss peaks within about 0.2 pixel of the Gaia target in both sectors, supporting target attribution at TESS resolution. The S5 egress is followed by a 0.146-d cadence gap, but the dip and immediate egress are observed; S32 is complete. Their 723.828-d separation allows many integer cycle counts. A bounded check of counts 10-20 (36.19-72.38 d) finds no additional predicted event inside either cached sector to discriminate them. Fourteen cycles give 51.7020 d, only conditionally close to the Gaia 51.62784-d spectroscopic period; source-specific conjunction timing remains untested.

Selected detector windows (BTJD predictions, not adopted event centers): S5 1454.453, S32 2178.154. Full measured local windows, fits, actual sector coverage and SHA-256 source receipts are in `lead-measurements.json`; raw plots in `lead-event-panels.png`. Actual core/wing endpoints and gaps are in `lead-window-checks.json`. Same-photon KSPSAP comparison, where available, is in `lead-alternative.json` and its plot.

## Orbit, source and limits

Frozen Gaia DR3 source 5096613016130459136 has spectroscopic period 51.627842 d. This is a selection prior, not a measured eclipse period or a source-specific conjunction match.

Exact Gaia identity is already a published EB alert (Tarrants and Mendes Table 2) and appears in Chopard v1.2.0; novelty is known. This bounded two-occasion review does not by itself validate the selected dips as that published eclipse clock. Unresolved close neighbors remain possible.

Catalogue receipts: `../../shared-catalogues/TARGET-STATUS.csv`, `../../shared-catalogues/tarrants-mendes-overlaps.json` and `../../shared-catalogues/chopard-overlaps.json`. Independent difference images/WCS: `../helper-q025-difference.json` and associated PNG; TESSCut source ZIP hashes are recorded there. Conditional cycle calculations and cached-sector availability: `lead-alias-checks.json`. Publication identity and physical interpretation of these two particular dips are separate claims.

This is a bounded verdict on the selected bulk lead, not a global statement that the star has no binary or transit signal. A same-photon reduction is a processing comparison, not a new observing occasion.

## Next check

Recover the published ephemeris and a third target-localized event; check Gaia conjunction geometry and cycle aliases.
