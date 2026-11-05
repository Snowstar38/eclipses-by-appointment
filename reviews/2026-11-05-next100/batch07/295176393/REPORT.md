# Q061 — TIC 295176393

**Physical verdict:** CONFIRMED. **EB novelty:** UNKNOWN. **Review completion:** COMPLETE.

## Raw evidence

Six sharp, symmetric SAP dips with ingress and egress occur at measured BTJD 2365.9714 (S39), 3101.8450 (S66), 3837.7177 (S93), 4083.0084 (S100), 4110.2602 (S101), and 4137.5179 (S102). A local Gaussian plus linear baseline fit gives 5.2–6.3 ppt depth and a 27.25454 d spacing for cycles 0,27,54,63,64,65; O–C is at most 0.0023 d. The actual 0.06 d cores have 9/10 to 26/27 expected quality-zero cadences. The screen-selected S12 1630.035 dip is partly gapped, while the measured clock predicts about 1630.10; it is not used. S101 4112.915 and S102 4145.071 are broad gap/step features unrelated to the narrow clock.

## Timing, physics and source

The repeated short duration and stable depth favor eclipses over the broad baseline waves. Bounded half-phase checks at the revised measured 27.25454 d clock find fully covered S39/S66/S93/S100/S101 midpoints without a comparable narrow dip; this argues against a shorter equal-event alias. Gaia SB1 P27.24860±0.00443 d is close but is not adopted as the photometric period. Its source-specific e=0.430, omega=46.5 deg and t_periastron=13.419 Gaia days give an illustrative edge-on inferior conjunction about 0.40 d before the first observed center when propagated to that cycle; period and orbital-element uncertainty across the long baseline make this compatible, not an exact geometry measurement. Independent S39 TESSCut has positive target flux, a target-pixel deficit peak and clipped centroid 7.0 arcsec from target. A MAST TIC cone finds all stars within 38 arcsec at approximate T-flux ratio below 0.002 versus the target, too faint to produce the 0.0055 observed depth by complete disappearance; brighter capable stars start at 62 arcsec, about three TESS pixels away. Raw and alternate reductions recover representative events.

## Limits and next check

No formal timing error is assigned from a local shape model. TIC flux ratios and TESS difference centroids are approximate, with bandpass and aperture uncertainty; the distant capable neighbors are disfavored rather than mathematically excluded. Novelty gates remain unresolved for this exact queue.

Obtain higher-angular-resolution time series or independent aperture localization to tighten source ownership and refine the orbital geometry.

## Reproduction

`lead_context.py` verifies source-packet, bulk-result and FITS SHA-256 values, then plots raw SAP for all 9 cached sectors. `lead-context.json` and `lead-local-series.json` retain numeric time/flux, actual quality-zero coverage and gaps. `lead-flag-diagnostics.json` records core endpoints for 11 selected dip windows. `lead-alternate.png/json` compare reductions of the same photons. `lead-gaia-geometry.json` records source-specific orbital elements where used. `lead-neighbors.json` records MAST TIC cone data for Q061/Q068; `lead-timing.json` and `lead-extended-timing.json` contain measured eclipse centers. `lead-halfphase.json` records revised-clock shorter-alias checks; `lead-sector-availability.json` documents the Q062 availability discrepancy. The independent helper audit supplies pixel and WCS evidence. Screening centers are predictions, not measured eclipse times.
