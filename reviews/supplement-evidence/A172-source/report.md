# REPORT — TIC 434263468 (TYC 4282-552-1, Gaia DR3 2207241593875197952)

Opus 5.5 subagent, 2026-10-21, wave 5. Fresh folder; no previous session worked this star. (Saved by the parent session; the file-write tool refused REPORT.md for the subagent.)

## Verdict: CONFIRMED. A detached, circular F-subgiant + M-dwarf SB1 with both eclipse kinds detected on target.

Deciding numbers:
- **Primary:** 23 events in 9 QLP sectors (s017–s085), each with S/N 22–136. Flat-bottomed transit, T14 8.04–8.10 h, T12/T14 0.15.
  - Depth is 23.85 ± 0.05 ppt in QLP. QLP depths scatter 17–28 ppt (χ²/dof 855/22).
  - TESS-SPOC PDCSAP gives 23.1–25.2 ppt in all 9 sectors, so the QLP scatter is a QLP dilution systematic.
- **Period:** P = 8.077758 ± 0.000004 d against Gaia's 8.078179 ± 0.000548 d, a difference of **−0.77σ**.
- **Timing:** the primary falls on Gaia conjunction A (companion in front) at −0.87σ to −0.99σ in every sector. Conjunction B is 17–35σ away.
- **Secondary eclipse:** 1.34–1.43 ppt in PDCSAP, present in 24 of 26 individual events.
  - S/N is 17.7 with red-noise-scaled errors; the control windows reach at most 5.5.
  - Phase is **0.50002 ± 0.00034** (PDCSAP jackknife) and 0.50069 ± 0.00082 (QLP).
  - That gives e cos ω = +0.0000 ± 0.0005, against Gaia's +0.0105 ± 0.0147 (0.7σ).
  - Duration ratio D2/D1 is 0.98–1.00, so e sin ω ≈ −0.002 ± 0.026, against Gaia's +0.001 ± 0.018.
- **On target:** both eclipse kinds are on target in the pixels.
  - Primary: the SPOC DV TIC offset is 0.65″ (s57) and 0.74″ (s58).
  - Own difference images over 9 sectors make the target the best fit. The G 9.19 neighbour at 67″ is worse by Σχ² ≈ 97,000.
  - At the secondary, the target is best, or within Δχ² ≤ 7 of a G 15.6 star at 10.5″ that would need a 12–54 ppt own dip. The G 9.19 star is worse by about 500.

## 1. Archives
- **cats.py --r 60:**
  - VSX has only a YSO 27″ away, fainter than G 17. It would need a dip of more than 9,000 ppt, so it cannot be the source.
  - No hits in ASAS-SN, Prša+2022, IJspeert+2024, or Kostov t2/t3/t4.
  - SIMBAD: TYC 4282-552-1 [SB*].
- **Gaia DR3:** vari_summary and vari_eclipsing_binary are empty. NSS is SB1, significance 44.6, flags 0, ruwe 1.02.
- **SB9, WDS, J/AJ/160/111:** none.
- **ExoFOP:** no TOI, CTOI, imaging, spectra or companions.
- **Extra VizieR cones at 30″** (ATLAS, ZTF, WISE, GCVS, ROSAT, 2RXS, 4XMM, ASAS-SN, LAMOST, APOGEE, Prša+2022): no rows. Each control cone returned rows, so the queries worked.
- **Web search** on "TYC 4282-552-1" and "TIC 434263468": nothing relevant.
- **New find, a TESS-SPOC DV report for s0056–s0069 on MAST** (`dv-out.txt`):
  - TCE 1 is the primary: P 8.077874 ± 0.000077 d, 25.4 ppt, 8.26 h, Rp/R* 0.149, a/R* 8.61.
  - TCE 2 is the secondary: epoch 2856.065 (phase 0.4993), 1.56 ± 0.10 ppt, 7.6 h, MES 15.
  - Neither became a TOI.
  - SPOC's s57 difference image for TCE 2 is offset 70″ toward the G 9.19 neighbour. The per-sector difference images here do not reproduce that offset (§4), so it is treated as a low-S/N centroid from a single sector.
- **Batch receipts:**
  - c3-vetsum: dphi −0.006/+0.483, ATTR.
  - diffrun s058: peak on target, deficit−target 2.23″. The 21.5″ deficit−light offset is the light centroid being pulled by the G 9.19 star.
  - ebcats: none.
- **No prior art** beyond the unpublished SPOC TCEs.

## 2. Measurements (vet-out.txt; QLP SAP, Q==0, no trimming)
- **Odd vs even:** 23.86 ± 0.08 vs 23.84 ± 0.06 ppt.
- **Background:** the unit-free regression (bkgreg-out.txt) implies a flux change of ≤ 0.11 ppt per sector. The exception is s077 at 1.4 ppt, against a 14 ppt dip in the same windows.
- **Quality flags:** 2 events touch a bit-32 cadence. None is within 0.5 d of a listed sector-wide systematic.
- **Centroids:** QLP dX is +4.8 ± 1.2 mpix and dY is −4.9 ± 1.3 mpix. That is the expected shift away from contaminating light (CROWDSAP 0.78–0.88).
- **Dip census:** the only off-ephemeris dip at half the eclipse depth or more is at 2867.637 (16 ppt).
  - It is the matched filter's window running into the primary 0.55 d later, and 26 cadences there are flagged.
  - Many 1–4 ppt red-noise dips are present.
- **Second eclipse kind:**
  - vet.py's free scan peaked at phase 0.4875. That was red noise; secA's control windows reach S/N 24.6.
  - With red-noise-scaled errors (secscan-out.txt), the scan peaks at exactly 0.5000 in both QLP (S/N 7.7) and PDCSAP (S/N 17.7).

## 3. Ephemeris
- **Primary:** T0 = 3199.37690 ± 0.00022 BTJD, P = 8.077758 ± 0.000004 d.
  - χ²/dof is 147/21 (errors scaled ×2.65); O−C rms 3.6 min.
- **Against Gaia's conjunction A:** −1.9 h at s017 to −4.8 h at s085. The drift is Gaia's P being 0.77σ long.
- **Phase separation:** Gaia's B−A is 0.5067 ± 0.0094; measured 0.50002 ± 0.00034.

## 4. Independence
- **TESS-SPOC light curves** (9 sectors): PDCSAP depth 23.1–25.2 ppt. SPOC-SAP, uncorrected for crowding, gives 19.3–20.7 ppt.
- **Difference images** (tpfdiff2.py on 11×11 TPFs):
  - Primary: the target pixel loses 20–22 ppt. The G 9.19 star's pixel changes by −0.5 to +1.7 ppt, so that star could only be contributing ≤ 2 ppt of its own dip.
  - Secondary: the target pixel loses 1.0–2.0 ppt (S/N up to 14). The neighbour's pixel averages about 0.
- **Neighbour table** (needed dip = 23.8 ppt × 10^(0.4ΔG)):

  | Neighbour | Needed dip | Verdict |
  |---|---|---|
  | G 9.19 at 66.9″ | 7.6 ppt | excluded by pixels (Σχ² +97,000) |
  | G 15.63 at 10.5″ | about 2,860 ppt | impossible |
  | G 15.25 at 13.7″ | about 2,000 ppt | impossible |

## 5. Physics
- **Mass function:** f(M) = 0.0125 M☉. With M1 = 1.30 M☉, m2(i = 90°) is 0.29–0.35 M☉ and a ≈ 19.9 R☉.
- **Duration:** the central-transit T14 would be 8.95 h. The observed 8.04–8.10 h gives b ≈ 0.4–0.5 and i ≈ 86.4°.
- **Radii:** SPOC's k = 0.149 gives R2 = 0.34–0.38 R☉ (using R1 = 2.31 R☉ from SPOC's a/R*, or 2.53 R☉ from TIC). That fits an M dwarf of the f(M) mass.
- **Which star is in front:**
  - At conjunction A the M dwarf transits the F star.
  - At conjunction B the M dwarf is totally occulted (flat bottom). The depth ratio 0.058 implies T2 ≈ 3200–3300 K.
  - The predicted occultation depth is 1.4–1.9 ppt; observed 1.34–1.43 ppt.
- **Ellipsoidal:** predicted 0.64 ppt; PDCSAP gives A2 = 0.35–0.57 ppt.
- **Heartbeat:** not an issue, because the orbit is circular.

## 6. Next predicted times (BTJD)
- **Primary** (conjunction A): **4338.3408, 4346.4185, 4354.4963** (± 0.0006 d), then every 8.077758 d.
- **Secondary** (conjunction B): **4342.3798, 4350.4576, 4358.5353** (± 0.003 d).

## What would settle it further
- RVs for a joint orbit fit.
- A spectroscopic log g to resolve the R1 question (TIC 2.53 R☉ vs SPOC 2.31 R☉).
- Reporting the SPOC TCE as a CTOI/EB.

## Files
- **Scripts:** vet.py (TMAX/T14G overrides), vetlib, bkgreg, secA, secscan, secphase, tpfdiff2, indep, dvparse, phys_ecc, physics, gaiatap, morecats, extracats, mastlc.
- **Outputs:** the matching *-out.txt files, plus vet-results.json, fold_oc.png and events.png.
- **Data:** `C:\Home\sky\data\qlp-sb-p20-60\pervet434263468\`.
