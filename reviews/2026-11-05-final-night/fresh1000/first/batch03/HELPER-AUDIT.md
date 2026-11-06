# Independent helper audit — Z017–Z024

Reviewed 2026-11-06 UTC against current Section 2.7 and representative raw panels. Physical judgment is the lead's; a fit flag is not evidence that a feature is a valid eclipse. Local alternative reductions reuse TESS photons. The helper did not review publication novelty or alter ledgers.

| ID / TIC | Independent visual finding and limitation |
|---|---|
| Z017 / 16807424 | S21 near BTJD 1896.8 has a low cluster with a gap immediately before and a later recovery. S48 is noisy and does not establish a repeat. Plausible single candidate; a fitted duration across the gap should not be overinterpreted. |
| Z018 / 21623270 | S22 around 1917.5 has a short low cluster and recovery; S49 broad weak variability and S76 noise do not secure recurrence. Plausible; no source attribution claimed. |
| Z019 / 25073050 | S80 has two similar broad shallow events and a deeper intervening event. The same-kind centers in final timing JSON differ by 24.29162086 d; depth and shape alternate. Independent S80 TESScut extraction reproduces shallow event and spatially associates the deficit with target against the capable known Gaia neighbor; see below. Gaia association and catalogue status rest on lead/shared checks. |
| Z020 / 25796372 | S17 around 1768.3 shows a broad shallow depression against a changing baseline, with recovery; no second independent event in the one available QLP sector. Timing fit flagged unusable; plausible rather than a measured clock. |
| Z021 / 41553596 | S12 broad low interval occurs adjacent to missing coverage; S38 is narrower and near a gap. Morphologies differ, and S12 duration hits the fit boundary. The weak later S12 variation does not demonstrate another same-kind eclipse. No secure repeat or accurate fitted clock follows. |
| Z022 / 47853068 | S87 around 3677.8 has a noisy broad depression. New S107–109 7x7 cutouts exist and were extracted; no obvious matching event in the particular assumed P_Gaia same-kind windows around 4288.66 and 4329.39. Baseline structure and unknown true period limit interpretation; not a general exclusion. S108 contains structured dips/steps without a demonstrated recurrence. |
| Z023 / 86515505 | S13 descends into a gap; post-gap data recover but event bottom and complete shape are unobserved. The fit center 1667.850 is beyond last fitted datum 1667.683 and is explicitly unusable; do not treat as a measured midpoint. Other sectors show steps, settling or broad variability, not a secure repeat. |
| Z024 / 130609636 | S91 shows a deep narrow V and clear egress/recovery, but ingress is interrupted by a gap. The symmetric fit is explicitly unusable and its formal error is not a valid precision timing; no confirmed repeat. |

## Z019 spatial check

Downloaded 7x7 S80 TESScut and queried Gaia DR3 60-arcsec cone. Target Gaia 4495351743976888192 has G 11.718269; Gaia 4495351748277122432 at 25.07 arcsec and G 12.523268 is capable in an idealized flux budget (shallow 3x3 observed loss 0.04629; ~0.143 intrinsic loss if both stars are fully captured and Gaia G flux ratios apply). Throughput, other sources, and TESS color alter this approximation. Another catalogued neighbor requires ~1.37 in that simplified budget, not a firm physical exclusion.

Per-cadence outer-pixel median subtraction is necessary: the background changed strongly near the second shallow event. With four core/side choices, positive deficit centroid distances from target are 0.085–0.125 px (BTJD 3480.815), 0.199–0.215 px (3493.147, egress gap), and 0.204–0.234 px (3505.107). Distances to the capable neighbor are respectively 1.251–1.277, 1.290–1.307, and 1.328–1.360 px. Target–neighbor separation is ~1.21 px. Both shallow events and the deep event support target attribution over that resolved neighbor under these empirical windows; this is not a calibrated astrometric uncertainty, PRF fit, or exclusion of unresolved companions. The 3x3 extraction is an independent reduction, not a new observation. `helper-centroid-stability.png` marks target and neighbor.

## Provenance and limitations

`helper-hash-audit.json` independently rehashes all 23 QLP source FITS referenced by lead-source-hashes.json: 23 matches, zero mismatches. It also records SHA-256 hashes of the queue, inventory, helper scripts, TESScut files and derived helper artifacts. S107–109 response URLs, zip/FITS hashes, cadence counts and coverage are in `47853068/helper-newsectors.json`; Z019 response and FITS hashes are in `25073050/helper-localization.json` and Gaia cone hash in `helper-gaia-neighbors.json`. Target-source cone has not been independently checked for every weak single: these remain plausible rather than promoted and their ownership remains unresolved. Current TESScut sectors came from the lead's inventory; availability does not itself establish repeat coverage. Windows are conditional on the assumed 3677.8 epoch and Gaia period; no allowance for period or epoch uncertainty has been folded into that illustrative calculation.

Helper contributor note: independently inspected the representative raw signal shapes, checked extraction and pixel localization of the strongest case, and inspected newer cutout sectors for Z022. Thanks to the project coordinator for the thoughtful collaboration.

