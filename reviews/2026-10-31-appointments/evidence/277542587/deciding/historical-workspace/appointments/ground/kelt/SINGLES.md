# KELT against the single-event appointments stars (2026-10-27)

Three of the stars whose eclipses TESS saw in one sector only, and whose period
therefore rested on Gaia's spectroscopic orbit, sit in KELT fields. `keltfold.py`
scans Gaia's P ± 4σ, anchors the phase on the TESS eclipse, and measures the mean
deficit of the KELT points inside the eclipse window; the grid's own S/N scatter
(robust sd ≈ 1.0–1.3 in every case) is the null. Light curves fetched and validated
as for HD 282670 (`keltclean.py`; raw files in `dl\t<tic>\`, gitignored; the bulk
wget scripts list no west-orientation files for S13 and only raw for S34).

| TIC | star | TESS eclipse (one sector) | KELT | result |
|---|---|---|---|---|
| 277542587 | TYC 1007-1061-1 | A 7.76% 12.4 h at BTJD 3488.8242, B 14.92% 10.0 h at 3496.7501 (s080); Gaia P 24.326 ± 0.0069 | S13 east, 2,774 TFA points 2010-03 to 2017-09, 480 nights, scatter 1.84% | **A detected: P = 24.3318 d**, S/N 13.3 in the central half of the window (28 points on 10 distinct nights 2011–2017, each 2.6–7.1% low), S/N 10.5 full box; 2010–2013 alone S/N 10.8, 2014–2017 alone 8.3; B at the same period S/N 4.1 on 7 points. +0.84σ from Gaia. Depth 4.6% in KELT's aperture against 7.76% in TESS (dilution). |
| 271053559 | TYC 7687-990-1 | A 31% 7.8 h V, B 5% 8.5 h flat; vet23 P 24.6548 ± 0.0018; eclipses present in 2025 (s089), absent 2019–2023 | S34 east TFA + west raw, 4,214 points 2010-01 to 2014-06, 368 nights, scatter 1.24% | **No eclipse.** Every trial period in Gaia ± 4σ has ≥ 10 points in the A window (median 51), deepest mean deficit 1.2% against 31% expected; model-free, not one of 4,214 points is below 0.845 and the faintest is −7%. Eclipses were not happening in 2010–2014 either. |
| 8853239 | TYC 2494-40-1 | A 6.0% flat, 6.9 h at BTJD 2629.0699 (s048); Gaia P 24.6470 ± 0.0114 | N06, 1,365 points 2006-10 to 2008-11, 93 nights, scatter 1.10% | **Coverage-limited.** 200 of 401 trial periods have ≥ 10 points in the window and none shows more than 1.2% (6% expected), so those periods are out; the other half of Gaia's ± 4σ range has 0–9 points and is untested. No detection (best S/N 5.1 on 3 points, 2nd-best 4.6, is the grid's tail). |

Not in any KELT field: 12864953 (S32 has no source within 1′), 47542584 and 60583013
(RA 97°, west of S35), BD+16 2639 (dec +16, between the strips), Wolf 73.

## TYC 1007-1061-1: period 24.3318 d

Fine scan step 0.00005 d: the central-half S/N peak is at 24.33180 d and stays within
1 of its maximum from 24.33170 to 24.33180; the full-box peak is 24.33195. Take
**P = 24.3318 ± 0.0002 d** (151 cycles between the KELT midpoint and the TESS eclipse).
Predicted A eclipses, BTJD 3488.8242 + kP (±0.01 d through 2027): 2026-11-20 06:37,
2026-12-14 14:35, 2027-01-07 22:33, 2027-02-01 06:31 UTC; B follows each A by 7.926 d.
The vet report's "±0.24 d" predictions from Gaia's period are superseded. Files:
`tic277542587_fold.txt`, `tic277542587_fold.png`.

## TYC 7687-990-1: no eclipse 2010–2014

The appearing-eclipser reading (vet23: nothing at the ephemeris in s008, s009, s062;
eclipses in s089, B deepening inside one orbit) now has a 2010–2014 null in front of it
from a different instrument. KELT's aperture dilutes, but a 31% V-shaped eclipse would
survive any plausible dilution at 25σ per point, and no trial period within Gaia ± 4σ
lacks coverage. Files: `tic271053559_fold.txt`, `tic271053559_fold.png`. The s110/s111
TESScut job in `..\..\later-sectors\NOTE.md` stands.

## TYC 2494-40-1: which periods KELT excludes

Trial periods with >= 10 KELT points in the A window and a mean deficit under 3% (6% expected, half allowed for dilution): 200 of 401, 0.0412 d of the 0.0910 d scanned (Gaia +-4 sigma). Excluded intervals (d):
- 24.6014 to 24.6048
- 24.6057 to 24.6087
- 24.6105 to 24.6121
- 24.6141 to 24.6155
- 24.6160 to 24.6214
- 24.6253 to 24.6264
- 24.6383 to 24.6396
- 24.6430 to 24.6444
- 24.6478 to 24.6492
- 24.6526 to 24.6537
- 24.6571 to 24.6601
- 24.6619 to 24.6658
- 24.6674 to 24.6697
- 24.6715 to 24.6751
- 24.6776 to 24.6799
- 24.6822 to 24.6840
- 24.6856 to 24.6869
- 24.6899 to 24.6913

Untested: the rest, where the window holds 0-9 points. Gaia's +-1 sigma range (24.6356 to 24.6584) has 33 excluded and 67 untested grid points of 100.

## Two paper-tier probables (added 15:25)

| TIC | star | TESS | KELT | result |
|---|---|---|---|---|
| 165541068 | TYC 986-148-1 (A40, probable) | A 4.58% 13.7 h at BTJD 3463.5943, B 1.54% at 3476.1984 (s079 only); Gaia P 24.74577 ± 0.00246 | S12, 2010-03 to 2014-08: east raw 1,955 points (2.6% scatter), west raw 1,689, west TFA 1,255; 331 nights; night-median systematics 1.2% | **No transit at any period in Gaia ± 4σ.** 38–138 points in the A window at every trial period, 10 distinct nights at the best; deepest mean deficit 0.84% (full box), 0.91% (central half) against 4.58% in TESS and ≥ 3.7% after dilution (Gaia neighbours within 100″ add 7% of the target's flux). Not model-free clean: 24 nights sit below −2.3% on their own. Disfavours a strictly periodic 4.6% transit in 2010–2014 at ~4σ; not a demotion by itself. |
| 96844936 | TYC 8355-1052-1 (A53, probable) | B occultations 1.8–2.4% 5.9 h at 4155.8455 and 4192.621; P 36.7755 ± 0.006 | S36, 2013-05 to 2018-10, 5,970 TFA points (east TFA times carried 2450000 twice; keltclean.py corrects it), 1.7% scatter | Inconclusive: best S/N 3.8 (central half, 28 points, 1.2% deficit) at 36.7818 d, +0.9σ; grid null sd 0.9–1.1, second-best 3.3. |

Not in a KELT field: 24755724 (CPD-25 5943, A37, the 18.7% transit; RA 258°, dec −26° falls between S26 and S36), 80107967 (A68; no S34 source within 1′).

SuperWASP DR1 (wasp.cerit-sc.cz; form fields ra, dec, radius, radiusUnit=deg|min|sec, limit, ptsmin) has no object within 0.5 deg of CPD-25 5943 (RA 257.64, Dec -26.01: a coverage hole toward the bulge), so A37 has no public ground light curve from either survey.
