# Q068 — TIC 341419787

**Physical verdict:** CONFIRMED. **EB novelty:** KNOWN. **Review completion:** COMPLETE.

## Raw evidence

Two narrow S7 raw SAP dips near BTJD 1493.4366 and 1514.5071 were selected, but the same shape also occurs in unflagged S34/S35/S61/S62/S63/S88/S89/S90 data. Thirteen locally fitted centers spanning cycles 0–108 yield P21.069015 d and an epoch 1493.43634; O–C rms is 0.0034 d, with depths about 3.4–4.6 ppt. Representative S61 and S88/S89 events are fully covered at roughly 2-minute cadence. The first two event spacing alone (21.0716 d) drifts by 0.28 d over 105 cycles and thus produces false later nulls if held exact. S35 2256.561 is a separate abrupt level change with isolated deep outliers, not the eclipse series.

## Timing, physics and source

The multi-epoch narrow clock is eclipse-like and close to Gaia SB1 P21.05714±0.00615 d. Bounded half-phase windows at the revised measured P21.069015 d in S35/S36/S61–S63/S88–S90 are well covered and show no comparable narrow dip, arguing against a shorter equal-event alias. The source-specific Gaia e=0.0585, omega=3.7±30.3 deg and t_periastron uncertainty 1.74 d permit the observed conjunction phase, but do not precisely predict it. Independent S7 and S61 TESSCut difference peaks land on the target pixel, with clipped deficit centroids 2.1 and 6.3 arcsec away and positive target-aperture baselines. MAST TIC neighbors at 18.8 arcsec have only 0.0017 approximate T-flux ratio; the 26.9 arcsec neighbor is marginally capable at ratio 0.0041, but the deficit is closer to the target in both orientations. More distant bright stars are capable in principle but several pixels away. Tarrants–Mendes Table 2 has an exact Gaia DR3 source-ID match labelled EB/New EB, so EB novelty is KNOWN regardless of the physical re-review.

## Limits and next check

The local Gaussian is descriptive and yields no formal period error. TIC flux ratios and clipped difference centroids are approximate; higher-resolution data could tighten ownership.

Refine high-resolution source attribution and compare the observed eclipse epoch against a joint orbital fit.

## Reproduction

`lead_context.py` verifies source-packet, bulk-result and FITS SHA-256 values, then plots raw SAP for all 12 cached sectors. `lead-context.json` and `lead-local-series.json` retain numeric time/flux, actual quality-zero coverage and gaps. `lead-flag-diagnostics.json` records core endpoints for 3 selected dip windows. `lead-alternate.png/json` compare reductions of the same photons. `lead-gaia-geometry.json` records source-specific orbital elements where used. `lead-neighbors.json` records MAST TIC cone data for Q061/Q068; `lead-timing.json` and `lead-extended-timing.json` contain measured eclipse centers. `lead-halfphase.json` records revised-clock shorter-alias checks; `lead-sector-availability.json` documents the Q062 availability discrepancy. The independent helper audit supplies pixel and WCS evidence. Screening centers are predictions, not measured eclipse times.
