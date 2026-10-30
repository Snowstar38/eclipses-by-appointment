# REPORT — TIC 293844315 (BD−02 2880, Gaia DR3 3837326955675043456)

Opus 5.5 subagent, 2026-10-21, wave 5. Fresh folder. (Saved by the parent session; the file-write tool refused REPORT.md for the subagent.)

## Verdict: CONFIRMED. An eccentric (e ≈ 0.36) G-dwarf + M-dwarf SB1; the primary eclipse is solidly attributed and on target, and the second eclipse is only tentatively detected.

Deciding numbers:
- **Primary:** 7 events in 4 QLP sectors (s008, s035, s062, s099), each with S/N 69–177. Depth 22.5 ppt (QLP), T14 4.38 h, T12/T14 0.25.
  - QLP s099 is 21.2 ppt against about 24 ppt elsewhere.
  - SPOC 2-min PDCSAP gives 23.0–23.3 ppt in all 4 sectors, so the s099 value is a QLP dilution effect.
- **Period:** P = 14.774809 ± 0.000003 d against Gaia's 14.773343 ± 0.001224 d, a difference of **+1.20σ**.
- **Timing:** the eclipse falls on Gaia conjunction A at +1.34σ to +1.54σ in every sector. Conjunction B is 14–32σ away.
- **On target:**
  - SPOC DV TIC offsets are 0.16–0.53″ (s8, s35, s62).
  - Own difference images over 7 TPFs make the target the best fit. Every neighbour is worse by Σχ² of at least 60,000.
- **Second eclipse at B (tentative):**
  - SPOC 2-min PDCSAP shows **0.49 ± 0.08 ppt at phase 0.3309 (0.3303–0.3356)**, from 3 events. This is the top of the whole-phase scan; control windows reach at most 2.4.
  - Gaia predicts B−A = 0.3333 ± 0.0105, so this is −0.2σ.
  - Converted to e cos ω (at Gaia's e sin ω) it gives −0.260 (−0.264 to −0.256), against Gaia's −0.256 ± 0.017.
  - A free fit gives a V-shaped graze, 0.5–0.77 ppt and 9.8 h (8.9–11.8 h).
  - Per-event depths of 0.33, 0.70 and 1.14 ppt are not mutually consistent, and QLP (2 events) does not see it. **Treat it as tentative.** The CONFIRMED rests on the primary.

## 1. Archives
- **cats.py --r 60:** no hits in VSX, ASAS-SN, Prša+2022, IJspeert+2024 or Kostov. SIMBAD: BD−02 2880 [SB*].
- **Gaia DR3:** vari tables empty. NSS is SB1, significance 37.3, flags 0, ruwe 1.05.
- **SB9, WDS, J/AJ/160/111:** none.
- **ExoFOP:** no TOI, CTOI, imaging or spectra.
- **Extra VizieR cones:** none in any variable or X-ray table. LAMOST DR7 LRS has spectra at 2.2″, which could supply RVs.
- **Web search** on "BD-02 2880" and "TIC 293844315": nothing relevant.
- **MAST:** SPOC DV reports for s1–s36 and s1–s65 contain one TCE, the primary only. No TOI was made.
- **Batch receipts:**
  - c3-vetsum: dphi +0.011/−0.322, ATTR.
  - diffrun s008: peak on target, 1.95″.
  - ebcats: none.

## 2. Measurements (QLP SAP, Q==0, no trimming)
- **Odd vs even:** 22.61 ± 0.09 vs 22.29 ± 0.09 ppt. This tracks the s099 dilution, not a period problem.
- **Background:** the unit-free regression implies a flux change of ≤ 0.39 ppt per sector (s062), against a 16–18 ppt dip in the same windows.
- **Quality flags:** no event has a bit-32 cadence, and none is near a listed sector-wide systematic.
- **Centroids:** dX −0.3 mpix, dY −3.4 ± 1.0 mpix.
- **Control phases:** all |depth| ≤ 0.14 ppt.
- **Dip census:** no off-ephemeris dip of half the eclipse depth or more.
  - A 9.3 ppt feature at 4067.13 sits 0.32 d after a primary, where the window runs into the eclipse.
  - Phase 0.5 shows −0.03 ± 0.09 ppt; there is no circular-orbit secondary.
- **Second eclipse in QLP at B** (secA): 2 events, 0.0 ± 0.11 ppt; a weak S/N 3.1 peak at phase 0.329. Too thin to use on its own.

## 3. Ephemeris
- **Primary:** T0 = 2810.95109 ± 0.00021 BTJD, P = 14.774809 ± 0.000003 d.
  - χ²/dof is 22.5/5; O−C rms 0.6 min.
- **Against Gaia's conjunction A:** +3.7 h (s008) to +9.7 h (s099). The drift is Gaia's P being 1.2σ short.

## 4. Independence
- **SPOC 2-min and TESS-SPOC light curves:** PDCSAP depth 23.0–23.3 ppt in s008, s035, s062 and s099.
- **Difference images:**
  - Primary: the target pixel loses 22.7–23.9 ppt. The G 10.91 star at 69″ shows ≤ 1.4 ppt at its pixel.
  - Secondary candidate: the target pixel loses 1.78 ppt (S/N 7.9) in s062, but there is nothing in s099. Inconclusive.
- **Neighbour table** (needed dip = 23.8 ppt × 10^(0.4ΔG)):

  | Neighbour | Needed dip | Verdict |
  |---|---|---|
  | G 10.91 at 69″ | 42 ppt | excluded by pixels |
  | G 15.07 at 42.5″ | about 900 ppt | excluded |
  | G 14.35 at 62″ | about 1,700 ppt | excluded |

## 5. Physics
- **Mass function:** f(M) = 0.0063 M☉. With M1 = 1.10 M☉, m2 ≈ 0.22 M☉ (R2 ≈ 0.24 R☉) and a = 27.8 R☉.
- **Transit:** a 23 ppt transit across R1 = 1.55 R☉ gives k ≈ 0.15, so R2 ≈ 0.23 R☉. Consistent.
- **Conjunction A:** separation 0.695a, central T14 5.47 h. The observed 4.38 h gives a chord fraction of 0.80 and i ≈ 86.8°.
- **Conjunction B:** separation 1.164a, so the projected separation sits right at R1+R2 (marginal). That predicts at most a graze of an M dwarf whose total light is about 1.8 ppt, with a long chord (about 9.2 h central).
  - This is consistent with the tentative 0.5–0.7 ppt, roughly 9.8 h V-shaped feature.
  - It also explains why no clear secondary is seen.
- **Heartbeat:** the eclipse is near conjunction, not periastron, and is short and sharp. No heartbeat or tidal confusion.

## 6. Next predicted times (BTJD)
- **Primary** (M dwarf transits the G star, conjunction A): **4347.5312, 4362.3060, 4377.0808** (± 0.0004 d), then every 14.774809 d.
- **Secondary** (grazing occultation, conjunction B, tentative): **4352.4195, 4367.1943, 4381.9691** (± 0.04 d).

## What would settle it further
- More 2-min sectors covering phase 0.331 to confirm the graze.
- LAMOST or new RVs to tighten e and ω.

## Files
- **Scripts:** vet.py, vetlib, bkgreg, secA, secscan, secB, tpfdiff2, indep, dvparse, phys_ecc, gaiatap, morecats, extracats, mastlc.
- **Outputs:** the matching *-out.txt files, plus vet-results.json, fold_oc.png and events.png.
- **Data:** `C:\Home\sky\data\qlp-sb-p20-60\pervet293844315\`.
