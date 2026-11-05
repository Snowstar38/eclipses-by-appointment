# Q051 - TIC 373314632

**Physical verdict:** PLAUSIBLE. **Novelty:** UNKNOWN. **Review completion:** COMPLETE.

## Evidence and interpretation

S98 has a sharp raw SAP descent near BTJD 4028.5, a low at about 4029.6, and a fast recovery near 4029.9 superposed on large stellar or instrumental trends. The nominal 4028.67-4029.63 core has 409/416 expected quality-zero cadences, so the trough is not a core-gap artifact. A final same-kind phase check found an unflagged raw rise at the S32 opening, approximately 2174.68-2174.91, which could be a partial egress related to the S98 rise around 4029.73-4030.00. S32 starts at 2174.287, so ingress and left baseline are absent; KSPSAP suppresses its rise to near flat. Two same-camera/CCD controls do not show the same large rise, so shared detector timing alone does not dismiss it. S98 DET_FLUX largely removes the raw shape while SYS_RM_FLUX preserves it; suppression alone is not proof of artifact. The selected S98 4010.620 window starts after a gap and rises into a level change, while S5 1451.746 is a slope beside a gap.

The illustrative mid-egress separation across S32/S98 is about 1855.07 d; conditional 49/50/51-cycle periods are about 37.86/37.10/36.37 d. Gaia SB1 P37.0862 d is compatible with the 50-cycle interpretation within its accumulated uncertainty, but this agreement cannot establish cycle uniqueness or even same-kind identity from one incomplete S32 occasion. The selected 4010.620 and 4029.150 windows are about half a Gaia period apart, but they are screen predictions, not two measured conjunction centers. S32 at the opposite-kind Gaia-projected BTJD 2193.396 has a 0.167 d central gap and is no sensitive narrow-event null. An independent S98 15x15 TESSCut WCS difference places the positive-loss centroid (7.777,7.667) near the queued source (7.796,7.921) in cutout pixels. Gaia DR3 3289139217167840000, G14.65 at 37.5 arcsec (pixel 6.82,6.43), has approximate G flux ratio 0.0309 and remains a capable blended source. The difference map on a sloping baseline does not uniquely assign ownership.

## Limits and next check

The S32 partial rise and S98 full raw trough are not established as a repeating eclipse kind; integer aliases remain unresolved, and target/neighbor ownership is uncertain. Neither depth nor adopted period is assigned. The official MAST TESSCut coordinate coverage endpoint, queried on 2026-11-05 and saved in lead-sector-availability.json, lists only S5/S32/S98, all already cached; this is availability, not a null. `lead-phase-followup.json/png` gives the projected phase and approximate egress intervals; `lead-startup-controls.json/png` records the same-CCD comparison and hashes. The helper WCS/Gaia artifacts give independent source details. Catalogue gates for this exact queue failed; the cached primary nonmatch does not establish novelty. The verdict is about the selected eclipse interpretation, not a claim that the Gaia source cannot be binary.

Obtain a later full event with resolved target/neighbor difference photometry and test the 49/50/51-cycle alternatives.

## Reproduction

`lead_context.py` verifies source-packet, bulk-result, and used FITS SHA-256 before plotting raw SAP for all 3 cached sectors. `lead-context.json` and `lead-local-series.json` record the numeric source series, actual quality-zero positive-flux coverage, gaps, and screen windows. `lead-flag-diagnostics.json` records actual core endpoints and gaps for 3 flagged dip windows. `lead-alternate.png` and `lead-alternate.json` compare the same-photon pipeline reductions around deciding windows. Screening centers are not measured eclipse times. The independent helper audit supplies a separate review.
