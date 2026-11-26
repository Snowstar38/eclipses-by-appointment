# fresh60 dwarfs: appointment search for shallow eclipses

Group: `shallow (<60 ppt)` rows of `fresh60_gaia.csv` (30 stars, G 11.6-12.0, P 20-50 d). Data: QLP FFI light curves, all 30 stars, 232 files (`C:\Home\sky\data\fresh60-qlp`, `sectors.json`). No TESS-SPOC fallback was needed.

## Method

- Conjunctions A (nu = 90 - omega) and B (nu = 270 - omega) from the Gaia NSS elements, t_periastron + 389 = BTJD; sigma_T from a 4000-draw MC over t_peri, e, omega errors, combined in quadrature with |n| sigma_P for cycle n. Window half-width max(3 sigma_T, 0.25 d) capped at 7 d. One prediction cross-checked by hand (394589749: A 397.207 vs 397.221 BTJD, cycle 72 at 3083.23 vs 3083.244, sigma_T 1.662 identical).
- Flux: KSPSAP_FLUX (main pass) and SAP_FLUX (second pass), QUALITY == 0, 10-min bins, 0.25 d trimmed at every gap edge, positive outliers clipped at 4 sigma from a 1-d running median.
- Box grid 1, 1.5, 2, 3, 4, 6, 8, 11, 14 h; centre step min(dur/4, 20 min). Baseline for each trial box: straight line least-squares fitted to the points 0.5-2.0 durations either side (a 4x-box window with the box masked), so a box the size of the trial is never flattened. SNR = depth / (sigma_pt sqrt(1/n_in + 1/n_side)) with sigma_pt the point-to-point scatter. Box, left and right sidebands each need 60% coverage; both halves of the box must dip.
- Null: the same best-box statistic in max(24, n_windows) random windows of the same width drawn from the star's own sectors with every predicted-window point removed. z = (best - median) / max(MAD, 0.5); the MAD is floored because overlapping null windows repeat one maximum. Depth floor 5 ppt.
- Verdict (automatic): eclipser = depth >= 5 ppt, no null window reaches the on-window SNR, SNR >= null max + 3, z >= 5, and (repeat at the same phase in another cycle or SNR >= 15); candidate = same with SNR >= null max + 1, z >= 3; else null. Every automatic eclipser/candidate and every on-window SNR >= 15 was inspected by eye; overrides are stated in the table notes.
- Repeat: the best box duration searched at the same phase in every other covered window of the same conjunction, within 3 |dn| sigma_P of the drifted time; y if any shows >= half the depth at SNR >= 4.
- Sectors >= 100: QLP TIME is not barycentric; events there are marked `time uncorrected`.

## Table

| tic | G | sectors (QLP) | windows A/B | best on-window box: sector, mid BTJD, dur, depth ppt, SNR | null med / max SNR | z | repeat | SAP pass best | verdict |
|---|---|---|---|---|---|---|---|---|---|
| 394589749 | 11.88 | 8: 11,12,38,39,64,65,66,93 | 7/8 | s066 3121.95 14h 1.1 8.0 | 3.8 / 5.2 (n=24) | 6.9 | n | 1.1 ppt SNR 8.0, null | null |
| 42452437 | 11.81 | 8: 14,40,41,53,54,74,80,81 | 7/8 | s080 3492.05 14h 9.8 46.2 | 4.6 / 9.6 (n=24) | 43.9 | n | 9.8 ppt SNR 46.2, eclipser | null |
| 393554921 | 11.97 | 7: 8,34,35,61,62,88,89 | 7/6 | s089 3744.46 14h 3.4 18.4 | 6.7 / 13.9 (n=24) | 3.6 | n | 3.4 ppt SNR 18.4, null | null |
| 260637515 | 11.64 | 41: 1..98 | 56/51 | s069 3205.17 14h 7.4 63.5 | 3.7 / 66.5 (n=107) | 74.7 | n | 7.4 ppt SNR 63.5, null | null |
| 403114300 | 11.78 | 30: 15..86 | 31/39 | s059 2914.70 14h 5.9 52.0 | 5.0 / 9.3 (n=70) | 28.7 | y | 5.9 ppt SNR 52.0, eclipser | eclipser |
| 405075519 | 11.73 | 10: 12..94 | 10/10 | s066 3123.35 8h 3.2 14.9 | 5.5 / 19.1 (n=24) | 3.1 | n | 3.2 ppt SNR 14.9, null | null |
| 195525295 | 11.66 | 7: 15,55,56,75,76,82,83 | 9/9 | s056 2844.48 14h 1.7 14.1 | 3.5 / 5.6 (n=24) | 21.2 | y | 1.9 ppt SNR 15.0, null | null |
| 323002495 | 11.89 | 10: 11..93 | 9/8 | s087 3679.99 3h 3.3 10.2 | 4.5 / 5.8 (n=24) | 3.2 | n | 3.3 ppt SNR 10.2, null | null |
| 380537052 | 11.96 | 9: 13..104 | 9/8 | s101 4111.83 14h 4.8 45.8 (time uncorrected) | 4.7 / 11.7 (n=24) | 26.9 | n | 4.8 ppt SNR 45.8, null | null |
| 56523308 | 11.72 | 7: 8,34,35,61,62,88,89 | 4/5 | s034 2231.15 2h 14.9 7.4 | 4.0 / 6.6 (n=24) | 6.7 | n | 5.2 ppt SNR 7.8, candidate | null |
| 427243341 | 11.93 | 8: 16,17,24,56,76,77,83,85 | 13/14 | s085 3611.96 14h 3.6 15.3 | none | - | n | 3.6 ppt SNR 15.3, null | null |
| 234291344 | 11.69 | 8: 1,28,68,95,96,102,103,104 | 5/6 | s102 4132.68 14h 2.5 28.6 (time uncorrected) | 7.8 / 23.6 (n=24) | 5.4 | n | 2.5 ppt SNR 28.6, null | null |
| 273793659 | 11.89 | 7: 15,16,55,56,76,82,83 | 8/9 | s082 3534.55 14h 2.0 7.8 | 4.5 / 9.0 (n=24) | 2.6 | n | 3.0 ppt SNR 8.8, null | null |
| 123630300 | 11.76 | 4: 6,33,87,98 | 3/4 | s087 3666.64 14h 4.2 30.6 | 4.1 / 12.3 (n=24) | 32.5 | na | 4.2 ppt SNR 30.6, null | null |
| 146478224 | 11.74 | 6: 7,8,34,35,61,88 | 5/6 | s088 3706.03 14h 2.1 9.2 | 4.5 / 6.9 (n=24) | 4.9 | n | 2.1 ppt SNR 9.2, null | null |
| 301654619 | 11.74 | 2: 55,82 | 3/3 | s082 3541.70 14h 0.8 6.1 | none | - | na | 0.8 ppt SNR 6.1, null | null |
| 248060132 | 11.61 | 5: 15,55,56,82,83 | 7/6 | s083 3570.56 14h 1.6 14.3 | 3.5 / 3.5 (n=24) | 21.5 | y | 1.6 ppt SNR 14.3, null | null |
| 82129560 | 11.70 | 8: 8,9,34,35,61,62,88,89 | 9/8 | s089 3731.93 11h 3.1 10.6 | 8.0 / 12.9 (n=24) | 4.1 | y | 5.1 ppt SNR 7.9, null | null |
| 24697689 | 11.76 | 4: 5,6,32,98 | 3/2 | s098 4030.26 14h 0.6 6.9 | 5.2 / 5.3 (n=24) | 3.6 | na | 0.9 ppt SNR 8.8, null | null |
| 266696841 | 11.65 | 4: 12,39,66,93 | 5/5 | s066 3116.71 8h 1.2 4.8 | none | - | n | 1.2 ppt SNR 4.8, null | null |
| 8545463 | 12.00 | 6: 24,25,51,52,78,79 | 4/6 | s078 3435.59 14h 3.8 19.9 | 4.3 / 4.4 (n=24) | 31.1 | na | 3.8 ppt SNR 19.9, null | null |
| 375061556 | 11.84 | 2: 55,81 | 3/4 | s081 3530.27 14h 2.1 15.1 | none | - | n | 2.1 ppt SNR 15.1, null | null |
| 149360830 | 11.77 | 2: 38,65 | 3/2 | s038 2344.43 6h 1.4 5.5 | 3.4 / 3.6 (n=24) | 4.1 | na | 1.6 ppt SNR 5.2, null | null |
| 328032108 | 11.93 | 3: 42,43,70 | 5/4 | s070 3222.14 8h 6.5 26.3 | none | - | n | 6.5 ppt SNR 26.3, null | null |
| 13494699 | 11.80 | 3: 54,81,92 | 3/4 | s081 3530.87 14h 1.0 7.6 | 6.6 / 6.6 (n=24) | 2.0 | n | 1.0 ppt SNR 7.6, null | null |
| 313202027 | 11.90 | 3: 19,59,73 | 4/5 | s073 3310.17 14h 1.0 6.0 | 3.8 / 4.0 (n=24) | 4.4 | na | 1.0 ppt SNR 6.0, null | null |
| 437254512 | 11.57 | 6: 9,36,63,90,100,101 | 10/9 | s100 4089.98 14h 1.9 23.5 (time uncorrected) | none | - | n | 1.9 ppt SNR 23.5, null | null |
| 398571726 | 11.78 | 5: 3,30,42,43,97 | 7/6 | s097 3983.10 14h 2.6 29.1 | none | - | n | 5.8 ppt SNR 41.7, null | eclipser |
| 283945234 | 12.00 | 6: 17,18,24,58,78,85 | 5/4 | s085 3633.20 14h 1.1 6.1 | 3.9 / 4.9 (n=24) | 4.5 | n | 1.1 ppt SNR 6.1, null | null |
| 284469305 | 11.69 | 2: 25,79 | 2/2 | s079 3467.55 14h 1.4 11.8 | 4.1 / 4.5 (n=24) | 15.4 | na | 1.4 ppt SNR 11.8, null | null |

`windows A/B`: predicted conjunction windows with data. `null med / max`: median and maximum best-box SNR over the off-window null windows. `SAP pass best`: the same on-window search on SAP_FLUX (depth, SNR, automatic verdict).

## Notes on individual stars

- 403114300: 5-6 ppt, 14 h flat-bottomed dip at conjunction A (1.3 sigma_T) repeating at the same phase in 8 sectors in KSPSAP (s056, s058, s059, s075, s076, s079, s083, s086; SNR 31-52) and 11 in SAP (adds s048, s049, s051, s055 at 3.8-5.4 ppt, which KSPSAP had flattened to 0.1 ppt). Linear ephemeris from 8 KSPSAP detections: P 28.4298 d (Gaia 28.4561 +- 0.0153, 1.7 sigma), T0 BTJD 384.462, rms 0.04 d. Nothing at B (< 2 ppt). Year-1 sectors (30-min cadence) show nothing in KSPSAP; not checked in SAP.
- 398571726: SAP pass only (KSPSAP flattened it): 5.8 ppt, 14 h flat-bottomed dip in s030 at BTJD 2132.83, 1.2 d before conjunction A (0.5 sigma_T); same phase in s042 at 4.7 ppt SNR 32 (0.04 d from the drifted prediction) and s097 at 2.6 ppt SNR 29 (1.0 d off, within 3 |dn| sigma_P). No off-window null sample (windows cover the whole sectors), so no z; the depth, shape and two-sector repeat carry it. Period needs a refit before quoting times.
- 42452437: automatic eclipser in both passes rejected by eye: 10 ppt, 14 h trough inside 50-100 ppt systematics in s080; nothing at the same phase in s040, s041, s081.
- 56523308: SAP-pass automatic candidate rejected by eye: 5.2 ppt, 14 h box at the end of s034, whose scatter is 10 ppt per 10-min bin; nothing in s035, s062, s088 (predicted 48 ppt, 9 h).
- First pass (no gap trimming, 40% sideband coverage) flagged 393554921, 195525295, 380537052, 82129560, 284469305 and 42452437 as eclipsers; every one was a 14-h box on a ramp or step beside a data gap. The 0.25-d trim and 60% sideband rule removed all but 42452437, rejected by eye.
- Strong on-window SNR (15-65) with depth under the 5 ppt floor or failing the null: 260637515 (41 sectors, variable; null max 66), 123630300, 8545463, 328032108, 437254512, 234291344, 380537052: all post-gap ramps or stellar variability on inspection.
- 8 stars had no off-window data for a null (windows of 10-14 d cover whole sectors): 427243341, 301654619, 266696841, 375061556, 328032108, 437254512, 398571726, 13494699 (partly). Their verdicts rest on depth floor and inspection.
- Caution for the whole test: KSPSAP flattened the 14-h, 5-ppt eclipses of both eclipsers in some sectors (403114300 s048/s055: 0.1 ppt in KSPSAP, 4.2-4.7 ppt in SAP; 398571726 s030: 0.3 vs 5.8 ppt). A KSPSAP-only search under-counts 10-20 h shallow eclipses; the SAP pass is the one to trust for this group, at the price of more ramp false positives (all caught by the null or by eye here).

## Off-window dips (SNR >= 15, depth >= 5 ppt, not at a predicted conjunction)

- 260637515: s069 t=3191.82 14 h 7.7 ppt SNR 66.5
- (260637515 is a rotational/variability trough in a 20-ppt modulated light curve, not a box dip)

## Counts

- eclipser: 2
- null: 28
- stars with at least one covered conjunction window: 30 of 30; no data: 0

Plots: `plots\<tic>.png` (window and fold) for the eclipser and for every star inspected; `_sap` suffix for the SAP pass.

Not done here: TIC 428785041 has no row in the CSV; its Gaia orbit was fetched from AIP (`orbit_428785041.csv`: SB1, P 50.789 d, sigma_tp 4.6 d) but the TIC lists R = 17.6 Rsun, lumclass GIANT, so it belongs to the giant group and was not searched.
