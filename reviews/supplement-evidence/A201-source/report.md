# TIC 70465753 (TYC 1365-707-1, Gaia DR3 671534461902678784): per-object vet

Opus subagent, sb1-scale pervet wave 6, 2026-10-21. No earlier session had worked this star. (Saved by the parent session; the file-write tool refused REPORT.md for the subagent.)

## Verdict: **CONFIRMED**. A grazing eclipsing G dwarf + M dwarf on a circular 6.4476-d orbit. Both eclipses are detected, both are on target, and the 3.87″ batch diffimg offset is a WCS artefact.

**The numbers that decide it:**
- **Primary eclipse:** 18 events, 26.56 ± 0.08 ppt deep, all at S/N 56–86.
- **Occultation:** 2.35 ± 0.14 ppt (S/N 16) at phase 0.5001 ± 0.0002. It is seen in every sector that covers it.
- **Period:** P = 6.4475682 ± 0.0000015 d, which is +1.7σ from Gaia's period.
- **Gaia conjunctions:** the primary lands 1.1–2.7 h after Gaia's conjunction A in every sector (0.4–0.7σ). At the Gaia epoch it is −2.2σ from A, and the secondary is −1.0σ from B.
- **Localization:** the PSF-fit deficit is 0.4–1.2″ from the WCS-calibrated target in three TESScut sectors. A fixed-position fit on the target beats every neighbour by Δχ² > 1900.
- **Independent pipeline:** TESS-SPOC PDCSAP gives 26.2–26.8 ppt in all 5 sectors.
- **Physics:** the mass function gives m2 ≈ 0.39 M☉. A grazing chord (b ≈ 1.1–1.2) predicts T14 = 2.1–2.5 h against 2.16 h observed. The secondary/primary depth ratio of 0.081 implies a T_eff2 of about 3300 K (blackbody).

## 1. Archives
- **cats.py (r = 60″, APPOINTMENTS_DATA set):**
  - VSX has Gaia DR3 671534461902678784 as **ROT** with no period. That is a type revision to EA/EB, not prior art.
  - ASAS-SN: none. SIMBAD: TYC 1365-707-1 as **SB\***.
- **SIMBAD bibliography:** the only bibcode is 2023A&A...674A..34G, the Gaia DR3 NSS paper.
- **morecats.py:** nothing in B/sb9, B/wds or J/AJ/160/111.
- **ExoFOP:** returned HTTP 503 for both the JSON and the page (Retry-After 3600), so I could not check it this session. The batch sweep (Opus 5.5's TOI/CTOI review) had no entry for it.
- **Batch ebcats (c3/c4):** none of the vetted or unvetted EB tables.
- **Web search** for "TYC 1365-707-1", "TIC 70465753" and the Gaia id: no relevant hits.
- **Gaia DR3:**
  - vari_eclipsing_binary has no row. vari_summary has a row (in_vari_classification_result = true, but no EB and no rotation-modulation class). G range is 0.031 mag over 23 epochs, phot_variable_flag VARIABLE.
  - NSS SB1: P 6.446975 ± 0.000342, e 0.040 ± 0.027, ω 219 ± 23°, K1 34.84 ± 0.51 km/s, significance 68. RUWE 1.11, ipd_frac_multi_peak 0.
  - TIC: T_eff 5810 K, R 1.00 R☉, M 1.05 M☉, d 174 pc.
- **Conclusion:** not previously catalogued as eclipsing.

## 2. Light curve (raw QLP SAP, QUALITY == 0, no trimming)
Files: `vet-out.txt`, `events.png`, `fold_oc.png`, `bkgfake-out.txt`, `sec2-out.txt`.
- **Primary shape:** depth 26.56 ± 0.08 ppt, T14 2.16 h, T12 0.86 h, flat part 0.43 h — nearly V-shaped. A flat-bottomed trapezoid (T12/T14 = 0.1) is worse by Δχ² +7123, and a pure V by +201.
- **Per-sector depths:** 27.16 / 26.24 / 26.50 / 27.15 / 25.98 ppt. The constancy χ² is 44/17, a sector-to-sector scatter of ±0.5 ppt that is plausibly aperture/dilution. Odd and even agree (26.62 vs 26.48).
- **Control phases (0.125–0.875 except 0.5):** all 0 within ±0.08 ppt. Phase 0.5 is the occultation.
- **Background gate (unit-free regression):** the fake dip is ≤ 1.8% of the depth in all 18 events.
  - The worst case is E6 (s045, BTJD 2541.01), which sits on a +2788 e⁻/s ramp. Its depth is unchanged with background as a regressor.
- **Flags and systematics:** no bit-32 cadence inside any eclipse window, and no event within 0.5 d of a listed sector-wide systematic time. Centroid shifts in eclipse are dX +0.07 ± 0.11 mpix and dY −0.25 ± 0.15 mpix.
- **Blind census:** 30 dips at S/N ≥ 4. Eighteen are the primaries. Eleven are occultations at phase ±0.500, each 1.9–3.1 ppt.
  - The one "15-ppt" off-ephemeris peak (BTJD 3266.38, S/N 4.1) is an occultation that falls inside a 0.22-d momentum-dump data gap in s072. It is a fit to the gap edges, not an event.
- **Occultation:** 2.16–2.35 ppt depending on the shape, at phase 0.50000 (±1.4 min on the fold).
  - Per sector: s044 2.50 ± 0.33, s045 2.36 ± 0.25, s046 2.21 ± 0.19, s072 2.01 ± 0.27 ppt. s071 has no coverage of it.
  - It leads the vet.py phase scan at S/N 16.4; the scan's 99th percentile is 5.2.
- **Rotational modulation:** about 1 ppt. The first harmonic amplitude is about 1.2 ppt, consistent with the ROT classification (a spotted, probably tidally synchronised G dwarf).

## 3. Ephemeris and orbit
Files: `timing-out.txt`, `gaiaepoch-out.txt`.
- **Primary ephemeris:** P = 6.4475682 ± 0.0000015 d, T0 = 2831.15209 ± 0.00009 BTJD. χ²/dof 38/15; O−C rms 0.5 min; per-sector mean O−C within ±0.33 min.
- **Secondary:** 11 events, P_sec = 6.4475952 ± 0.0000340. P_sec − P_prim = 2.3 ± 2.9 s per cycle, so no apsidal motion is detected.
- **Secondary phase:** 0.50020 ± 0.00018 from per-event timing, and 0.50000 from the fold. So **e cos ω = +0.0003 ± 0.0003**. Gaia's −0.028 ± 0.019 is 1.5σ away, in the circular direction — the Lucy–Sweeney sign again, as in the wave-4 list.
- **e sin ω:**
  - A trapezoid duration ratio of 0.78 would imply −0.12. But both eclipses are grazing, and the occultation's contacts sink into the noise, so that number means nothing.
  - The limb-darkened two-sphere joint fit (`twosphere.py`, one geometry for both eclipses) leaves e sin ω **unconstrained over −0.10…+0.10** (Δχ² < 1 everywhere, because of the k–b degeneracy at this occultation S/N).
  - So: no tension with Gaia's −0.024 ± 0.022, and no measurement either.
- **Comparison with Gaia** (MC with this star's own corr_vec; ω–T_p correlation +0.996):
  - **Per TESS sector:** the primary is +1.08, +1.13, +1.19, +2.68 and +2.74 h from conjunction A (+0.37 to +0.73σ).
  - **At the Gaia epoch (BTJD ~389):**
    - The primary is −3.56 h from A (−2.2σ).
    - The secondary is −0.68 h from B (−1.0σ).
    - Gaia's A→B separation is 0.482 ± 0.012 in phase, against 0.5001 measured. Most of the −2.2σ is Gaia's small spurious e pulling A and B apart.
  - The deep eclipse is at A (companion in front), as it should be for an M dwarf transiting the G star.

## 4. Localization: the 3.87″ batch offset is an artefact
Files: `locate-s044-out.txt`, `locate-s046-out.txt`, `locate-s072-out.txt`, `locate_s0*.png`.
- **Batch receipt, diff_s44.json:**
  - The light centroid (7.876, 7.362) and the deficit centroid (7.879, 7.371) agree to **0.19″** (0.003, 0.008 px).
  - Both sit (+0.156, +0.098) px from the uncalibrated catalogue spot. That is exactly the wave-4/5 artefact family.
  - The peak-deficit pixel is the target pixel.
- **Own pass** (21×21 TESScut cubes; WCS calibrated by a Gaussian-PSF model of all G < 16.5 stars on the out-of-eclipse image; free single-PSF fit to the difference image):

| Sector | WCS shift needed | Deficit vs calibrated target | 1σ radius | Target fixed-fit Δχ² to next star | Deficit / target flux |
|---|---|---|---|---|---|
| s044 | 3.0″ | 1.2″ | 1.2″ | 9226 | 2.36% |
| s046 | 1.9″ | 0.4″ | 0.8″ | 1949 | 2.45% |
| s072 | 2.5″ | 0.6″ | 0.6″ | 3110 | 2.41% |

- **Stability:** half-sample fits are 0.4–2.4″ from the target.
- **Mechanism:** the uncalibrated WCS alone is off by 1.9–3.0″. That, plus the moment-centroid box pull, accounts for the batch's 3.87″.
- **s044 caveat:** it has reduced χ² 13.5. The Gaussian PSF is imperfect, but no neighbour comes close.
- **Neighbours** (`neighbours-out.txt`; T from Gaia colours): the dip each would need is
  - G 14.75 at 41.7″: 94%
  - G 13.66 at 64.8″: 35%
  - G 15.15 at 71.1″: 149%

  All of them lose the fixed-position fit by Δχ² ≥ 1949 in every sector.
- **TESS-SPOC (independent pipeline):** at the same ephemeris PDCSAP gives s044 26.42, s045 26.33, s046 26.16, s071 26.78, s072 26.43 ppt. SPOC-SAP gives 25.45–26.44 ppt (`indep-out.txt`).
- **Caveat:** RUWE 1.11 and ipd_frac_multi_peak 0, so no sign of an unresolved third light.

## 5. Physics
File: `physics-out.txt`.
- **Companion:** f(m) = 0.0283 M☉. With M1 = 1.045, m2 = 0.39 M☉ (i ≈ 86°) — an M dwarf with R2 ≈ 0.40 R☉. a = 16.4 R☉ (16.4 R1).
- **Chord:** a central transit would be about 180 ppt deep. The observed 26.6 ppt needs a grazing chord, b_A ≈ 1.13–1.22 R1 (for R1 0.9–1.1). The predicted T14 is 2.07–2.50 h against 2.16 h observed, and the V shape fits a grazing chord.
- **Occultation depth:**
  - The ms() relation (T2 3634 K, blackbody J 0.146) predicts about 4.3 ppt at e sin ω = 0.
  - The observed ratio 0.081 means a blackbody J of about 0.08, i.e. T_eff2 ≈ 3300 K. That is cooler than the crude relation but within normal scatter for a 0.35–0.4 M☉ M dwarf, whose TESS-band flux a blackbody overestimates.
  - Alternatively, a small |e sin ω| ≈ 0.03 at the relation's temperature. The light curve cannot distinguish the two.
- **Companion light:** about 1.5–2.5%, negligible for the depth.
- One geometry (circular, grazing, k ≈ 0.35–0.45) accounts for both eclipses, the duration, the depth ratio and the RV mass function.

## Row fixes
- **P:** 6.4475682 ± 0.0000015 d (the batch's 6.44759 is fine to 5 decimals).
- **T0:** 2831.15209 ± 0.00009 BTJD (primary).
- **Depth:** 26.6 ppt (trapezoid fit; the batch's 25.5 is a median of core points in sapdepth; TESS-SPOC PDCSAP gives 26.4). Occultation 2.3 ppt at phase 0.5001.
- **Events:** 18 primaries (unchanged) plus 11 occultations.
- **dphi:** +0.007 to +0.018 vs Gaia A per sector, as the batch had. At the Gaia epoch it is −0.023 (−2.2σ), driven by Gaia's spurious e.
- **Offset:** the 3.87″ is not real; the deficit is 0.4–1.2″ from the target.

## Next predicted eclipses (BTJD)

| Kind | Times | Uncertainty |
|---|---|---|
| Primary (~26.6 ppt) | 4404.3587, 4410.8063, 4417.2539, 4423.7014 (then +6.4475682 d) | ±0.5 min |
| Secondary (~2.3 ppt, phase 0.5001) | 4407.5832, 4414.0307, 4420.4783, 4426.9259 | ±2 min |

## What would settle it further
- **e sin ω:** more 200-s sectors through the occultation, with ingress and egress resolved.
- **Masses and radii:** one RV epoch plus a spectroscopic T_eff for star 1 would turn the system into a mass–radius point for the M dwarf. The grazing geometry limits R2 precision.
- **Archive:** re-check ExoFOP when it is back up (it was 503 tonight).
