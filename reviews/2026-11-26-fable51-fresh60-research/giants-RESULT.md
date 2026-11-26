# Giants re-search: long-box appointment test on the fresh60 long-eclipse group

29 of the 30 giant-group targets have a Gaia row (TIC 428785041 has none and was not searched). All 29
have QLP FFI light curves on MAST (193 sector files, no TESS-SPOC fallback needed); data in
`sky\data\fresh60-qlp\` (shared with the rest of fresh60), sectors per star in `files.json` there.
Code: `fetch_giants.py`, `search_giants.py`, `plot_giants.py`, `fold278.py`, `report.py`; raw numbers in
`results.json`, log in `search.log`.

## Method

- Flux: QLP `SAP_FLUX`, `QUALITY == 0`, finite, per-sector median-normalised; bins with |f-1| > 0.3
  dropped; a sector is discarded if the median absolute deviation of its flux exceeds 5% (QLP aperture
  failures). Per-orbit (gap > 0.5 d) robust linear fit divided out (3 passes of 3-sigma clipping), then
  30-min bins.
- Conjunctions A (nu = 90 - omega) and B (270 - omega) from the Gaia SB1 elements, t_peri + 389.0 = BTJD;
  the Kepler-equation step-through check agrees with the closed form to 1e-4 d. sigma_T per cycle =
  hypot(MC sigma from t_peri, e, omega errors; n_cycles x period_error); window half-width
  max(3 sigma_T, 0.25 d) capped at 7 d. Every window hit the 7-d cap: Gaia t_peri errors are 1-2 d
  for these orbits and 60-150 cycles separate J2016 from the TESS data. A +-7 d window on a 20-58 d
  period is 25-70% of the orbit per conjunction, so the appointment constrains little.
- Box grid 12, 18, 24, 36, 48, 72, 96 h; box deficit against side windows 0.75-2.5 durations either
  side (one side suffices); SNR from point-to-point scatter. Depth floor 2 ppt.
- Null: same-width windows at random off-window centres on the same star, 40 per star (more than the
  on-window count, for a usable median/MAD); exclusion relaxed in steps when the windows cover most of
  the data (column `null` mode in `results.json`). z = (best - null median) / null MAD.
- Repeat check: other windows of the same conjunction with >= 50% coverage must show at least half
  the best depth. Verdicts were then checked by eye on `plots\<tic>.png` (every flagged star); overrides
  and reasons are in the note column and in `report.py`.
- Sensitivity column: rms of the box depth at the grid duration nearest the predicted one over random
  positions in all usable sectors. Where it exceeds half the predicted depth the star is reported as
  `null (variability-limited)`: a single eclipse of the predicted depth would not stand out.
- `*` on a mid-time: sector >= 100, QLP TIME not barycentric, time uncorrected.

## Table

| tic | G | P d | sectors | win A/B | best on-window: sec, mid BTJD, dur h, depth ppt, SNR | null med / max SNR | z | depth rms at pred dur (ppt) / pred depth | verdict | note |
|---|---|---|---|---|---|---|---|---|---|---|
| 13970600 | 11.96 | 26.05 | 14,15,41,55,81,82 | 9/6 | s82, 3536.25, 96, 57.5, 1035 (A+1.4 d) | 497 / 1035 (n=40) | 1.1 | 24.4 / 2.2 | null (variability-limited) | box-depth rms at the predicted duration exceeds half the predicted depth |
| 425356231 | 11.83 | 40.38 | 11,37,38,64,99,100,101 | 6/7 | s37, 2326.90, 96, 25.0, 316 (A-1.9 d) | 266 / 316 (n=40) | 1.4 | 9.3 / 3.0 | null (variability-limited) | box-depth rms at the predicted duration exceeds half the predicted depth |
| 341698647 | 11.62 | 39.21 | 11,12,38,65,100,101 | 5/6 | s65, 3082.45, 96, 15.6, 193 (A+0.1 d) | 76 / 123 (n=40) | 3.5 | 11.7 / 2.9 | null (variability-limited) | 44 ppt 6-d dip at A in s12 not repeated in s38 or s101 (flat at A); s11-s12 variability 2-8% |
| 278774793 | 11.64 | 58.12 | 1,2,5,6,7,8,9,11,12,28,29,32,33,34,35,36,38,39,61,62,65,66,67,68,69,87,88,89,93,94,95,96,98 | 21/20 | s88, 3702.61, 96, 33.6, 761 (B+3.0 d) | 144 / 339 (n=41) | 6.6 | 10.2 / 2.8 | candidate | 33-sector fold dips ~10 ppt for ~5 d at B+0.03 phase; 96-h box at B+1.7 d gives 23-31 ppt in 6 of 12 covered cycles, <6 ppt in the other 6; random 96-h boxes reach 20 ppt 4.7% of the time (binomial p~1e-5 before look-elsewhere). Depth 9x predicted; not in every cycle |
| 50929975 | 11.85 | 27.31 | 7,34,61,88,99 | 6/5 | s88, 3696.06, 96, 77.2, 928 (A-0.5 d) | 152 / 484 (n=40) | 17.6 | 14.6 / 3.9 | null (variability-limited) | 1.5-d quasi-periodic 2% oscillations plus trends; best box is a trend |
| 57663508 | 12.00 | 40.22 | 44,45,71,72 | 4/3 | s71, 3237.30, 72, 23.2, 140 (A+1.3 d) | 285 / 285 (n=40) | - | 11.6 / 2.8 | null (variability-limited) | box-depth rms at the predicted duration exceeds half the predicted depth |
| 144449849 | 11.91 | 26.18 | 10,37,64,101 | 7/5 | s101, 4115.68*, 48, 17.4, 309 (A+2.5 d) | 226 / 309 (n=40) | 0.8 | 8.7 / 3.6 | null (variability-limited) | box-depth rms at the predicted duration exceeds half the predicted depth |
| 306838524 | 11.97 | 49.68 | 10,37,63,64,90,99,100 | 6/4 | s99, 4054.71, 48, 14.0, 197 (A-1.3 d) | 140 / 289 (n=40) | 0.5 | 11.2 / 2.0 | null (variability-limited) | box-depth rms at the predicted duration exceeds half the predicted depth |
| 68063539 | 11.62 | 30.27 | 34,61,88 | 3/3 | s88, 3702.36, 72, 8.4, 128 (A+4.8 d) | 82 / 128 (n=40) | 1.7 | 3.7 / 3.3 | null (variability-limited) | box-depth rms at the predicted duration exceeds half the predicted depth |
| 284764266 | 11.67 | 26.08 | 44,45,46,71,72 | 5/8 | s46, 2578.65, 72, 38.4, 436 (B+3.3 d) | 347 / 434 (n=40) | 1.0 | 14.7 / 7.2 | null (variability-limited) | box-depth rms at the predicted duration exceeds half the predicted depth |
| 449307530 | 11.68 | 42.73 | 32,98 | 3/2 | s32, 2179.12, 96, 7.5, 158 (B+1.9 d) | 53 / 158 (n=40) | 9.4 | 2.7 / 2.6 | null (variability-limited) | U-shaped 7.5 ppt 4-d dip at B in s32; B in s98 flat to 0.5 ppt |
| 241700271 | 11.94 | 20.50 | 38,65,101,102 | 7/7 | s65, 3074.70, 96, 39.8, 501 (A-6.8 d) | 228 / 501 (n=40) | 3.5 | 13.1 / 12.9 | null (variability-limited) | box-depth rms at the predicted duration exceeds half the predicted depth |
| 169469440 | 11.85 | 26.59 | 11,37,38,99,100,101 | 8/10 | s38, 2354.56, 96, 39.2, 546 (A-0.8 d) | 365 / 546 (n=40) | 2.7 | 14.6 / 7.2 | null (variability-limited) | box-depth rms at the predicted duration exceeds half the predicted depth |
| 64375542 | 11.99 | 21.05 | 16,17,57,77,83,84 | 11/11 | s17, 1776.20, 48, 55.9, 394 (A-0.3 d) | 169 / 394 (n=40) | 1.2 | 8.5 / 4.0 | null (variability-limited) | box-depth rms at the predicted duration exceeds half the predicted depth |
| 354707476 | 11.90 | 43.11 | 18,59,86 | 3/3 | s18, 1792.06, 48, 8.0, 60 (B+4.3 d) | 48 / 59 (n=40) | 404.4 | 2.3 / 2.6 | null (variability-limited) | best box is the s18 start-of-sector ramp; null MAD degenerate |
| 341076867 | 11.96 | 27.81 | 13,27,101,102,103,104 | 12/6 | s103, 4164.80*, 72, 19.5, 342 (B-1.4 d) | 200 / 342 (n=40) | 8.8 | 6.3 / 3.1 | null (variability-limited) | best boxes are s101-s104 end-of-segment drops (scattered light) |
| 250837804 | 11.73 | 31.36 | 58,85 | 3/2 | s58, 2886.33, 96, 15.6, 179 (A-3.8 d) | 79 / 179 (n=40) | 1.0 | 4.7 / 3.2 | null (variability-limited) | box-depth rms at the predicted duration exceeds half the predicted depth |
| 248124207 | 11.94 | 23.50 | 54,81 | 4/3 | s81, 3529.63, 72, 37.2, 495 (A-0.0 d) | 438 / 495 (n=40) | 0.7 | 14.2 / 5.0 | null (variability-limited) | box-depth rms at the predicted duration exceeds half the predicted depth |
| 157587214 | 11.98 | 22.13 | 14,26,40,53,54,74,80,81 (1 usable) | 2/2 | s14, 1690.80, 96, 24.6, 112 (A-0.5 d) | 111 / 112 (n=40) | 0.7 | 12.0 / 10.2 | no data | 7 of 8 QLP sectors unusable (flux swings 0-250%, spikes); only s14 kept |
| 235986365 | 11.82 | 26.33 | 18,19,20,24,25,26,40,47,52,53,58,59,60,73,74,78,79,85,86 | 30/28 | s79, 3459.56, 96, 24.4, 445 (A+3.3 d) | 207 / 445 (n=58) | 2.5 | 8.7 / 4.3 | null (variability-limited) | box-depth rms at the predicted duration exceeds half the predicted depth |
| 430088489 | 11.76 | 34.48 | 43,44,45,71,72 | 7/6 | s72, 3284.95, 48, 4.1, 39 (B+4.7 d) | 19 / 28 (n=40) | - | 1.1 / 2.8 | null |  |
| 118724088 | 11.82 | 44.87 | 13,39,66,93,103,104 | 5/4 | s103, 4152.92*, 12, 11.4, 72 (A+1.8 d) | 9 / 135 (n=40) | 40.4 | 1.5 / 2.3 | null (variability-limited) | best boxes are s103/s104 start-of-segment ramps (time uncorrected sectors) |
| 3576168 | 11.98 | 20.50 | 44,45,46,47,71,72 | 10/8 | s72, 3267.65, 96, 44.5, 724 (B-3.0 d) | 243 / 724 (n=40) | 3.8 | 14.2 / 20.1 | null (variability-limited) | box-depth rms at the predicted duration exceeds half the predicted depth |
| 92201673 | 11.62 | 40.89 | 14,15,41,54,55,75,81,82 | 8/7 | s75, 3363.29, 96, 4.4, 78 (B+1.2 d) | 11 / 59 (n=40) | 9.7 | 1.2 / 3.2 | null | s75 4.4 ppt 96-h deficit at B is a slow hump; fold of 8 sectors flat to 0.5 ppt at both conjunctions, predicted 3.2 ppt would show |
| 171006861 | 11.99 | 43.57 | 19,43,44,59,70,71,86 | 5/6 | s59, 2936.50, 72, 11.1, 148 (A-5.7 d) | 40 / 148 (n=40) | 4.4 | 3.3 / 2.2 | null (variability-limited) | box-depth rms at the predicted duration exceeds half the predicted depth |
| 308091169 | 11.64 | 25.50 | 26,53,79,80 | 5/7 | s80, 3490.44, 72, 17.5, 253 (A+0.5 d) | 200 / 253 (n=40) | 0.7 | 6.1 / 3.0 | null (variability-limited) | box-depth rms at the predicted duration exceeds half the predicted depth |
| 303104461 | 11.80 | 28.81 | 9,10,36,37,63,90,99,100 | 11/8 | s63, 3018.95, 96, 44.2, 377 (B-1.2 d) | 134 / 377 (n=40) | 4.9 | 11.8 / 8.9 | null (variability-limited) | box-depth rms at the predicted duration exceeds half the predicted depth |
| 403188500 | 11.62 | 32.66 | 40,54,80,81 (3 usable) | 4/4 | s80, 3495.34, 96, 66.4, 346 (B+6.7 d) | 346 / 346 (n=40) | - | 21.4 / 3.7 | null (variability-limited) | box-depth rms at the predicted duration exceeds half the predicted depth |
| 72273851 | 11.96 | 32.58 | 14,41,54,55,74,75,81 | 8/11 | s55, 2822.80, 72, 23.6, 161 (B+4.6 d) | 30 / 129 (n=39) | 7.3 | 6.0 / 5.4 | null (variability-limited) | single flat-bottomed 10 ppt 4-d dip at A in s74 (3320-3325); A covered in s55 and s41 without it; fold flat at A |

## Summary

- Eclipses at a Gaia conjunction: **0 secure**. **1 candidate**, TIC 278774793 (58.1 d, 33 sectors):
  the stacked fold dips ~10 ppt for ~5 d just after conjunction B, and a 96-h box at B + 1.7 d gives
  23-31 ppt in 6 of the 12 covered cycles but < 6 ppt in the other 6. Random 96-h boxes on this star
  reach 20 ppt 4.7% of the time, so 6 of 12 at one phase is p ~ 1e-5 before a look-elsewhere factor of
  ~15. It is 9x the predicted 2.8 ppt and not present every cycle, which an eclipse must be; the
  absent cycles are not explained by the +-7 d ephemeris uncertainty (their windows hold nothing
  deeper than 19 ppt in any box). Treat as a target for a dedicated look, not a detection.
  `plots\278774793.png`, `plots\278774793_fold.png`.
- Clean nulls with coverage: **2** (TIC 92201673: 8 sectors, 8 A + 7 B windows, fold flat to 0.5 ppt
  against 3.2 ppt predicted; TIC 430088489: 5 sectors, box-depth rms 1.1 ppt against 2.8 predicted).
- Variability-limited nulls: **25**. These giants show 10-70 ppt deficits at 2-4 d timescales
  everywhere (semi-regular variability, sector-edge ramps), which is why the raw box SNRs run to
  hundreds and the null z is the only meaningful statistic; nothing beats its own null with a repeat
  at the same conjunction. Five of them had a single-event dip at a conjunction that failed the
  repeat test (341698647, 449307530, 72273851, and the code's two ramp/trend flags 50929975,
  354707476); a 2-13 ppt eclipse could hide under the variability in most of the rest.
- No data: **1** (TIC 157587214: 7 of 8 QLP sectors unusable) plus 1 target with no Gaia row.

Caveats: windows all at the 7-d cap, so this is closer to a "dip anywhere near the right half-orbit"
test than an appointment; the null is degenerate (MAD ~ 0, z blank) for three stars whose predicted
windows cover nearly all their data; sector >= 100 mid-times are uncorrected. Diagnostic plots for the
other flagged stars are also in `plots\`.
