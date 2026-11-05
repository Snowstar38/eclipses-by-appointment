# F032 / TIC 51321183

**Physical verdict:** PROBABLE; **bounded review:** COMPLETE; **catalogue status:** SCOPED_NONMATCH.

## Raw observation and interpretation

Sharp 4-6 ppt raw SAP eclipses at BTJD 2237.4566 (S34), 2980.6394 (S61), and 3706.9308 (S88) have matching narrow morphology. Their successive separations give 44 and 43 cycles at 16.890517 and 16.890499 d. Adjacent 43/42 and 45/44 cycle models miss the middle center by 0.198 and 0.190 d, larger than the 0.15-0.19 d event widths. P/2 through P/5 predict covered extra flat cores. The P=16.890508 d prediction at S99 BTJD 4061.631 lies in an actual 7.31-d data gap; the broad S99 detector window is a separate baseline structure.

Detector windows and diagnostic local centers: S34 2237.4566, S61 2980.6394, S88 3706.9308, S99 4068.1025. These are not all accepted eclipse centers. Source: `lead-measurements.json` and `lead-event-panels.png`; alternative QLP check: `lead-alternative.json`. Raw QLP FITS SHA256 receipts are in `lead-measurements.json` and the sealed source packet.

## Timing, source and prior identity

Gaia DR3 source 5755352452627474176, selection SB1/SB2 period 38.46864949433853 d. Selection orbit is not itself an eclipse timing measurement. Shared catalogue: `[local-path-redacted]`. SCOPED_NONMATCH; no target EB identification in checked tables.

Adopted measured photometric period: 16.8905 d. Reference measured center: 2237.4566 BTJD. Representative raw depth: 4.7 ppt.

## Limits and next check

The photometric clock is a rounded blended-aperture recurrence, not an established orbit of the Gaia target. Fresh WCS pixels have valid target flux but a capable G13.015 neighbor only 0.36 pixel from the target; local drift moves the difference centroid off both positions. Source ownership is unresolved. Gaia SB1 P38.46865 d is incompatible with the observed 16.89-d clock; no source-specific conjunction tie is claimed. Local formal timing errors omit systematics, so no period error is supplied.

Obtain resolved target and neighbor photometry at another predicted sharp eclipse, then establish source ownership and orbital association.

This review is a bounded assessment of the selected bulk lead. Same-photon QLP reductions are processing checks, not another observing occasion. Gaia G-band neighbor flux is approximate. No exhaustive all-sector physical fit or publication claim is implied.

Numeric cycle and coverage receipts: `lead-alias-null.json`, `lead-alias-grid.json`, `lead-adjacent-cycle-check.json`; source attribution: `helper-pixels.json`.
