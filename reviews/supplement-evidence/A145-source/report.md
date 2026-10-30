# TIC 260789413 (TYC 3344-341-1, Gaia DR3 206662904185592704) — per-object vet

Opus 5.5 subagent, wave 3 relaunch, 2026-10-19. Ledger row: G 10.69 | P 4.74683 | 12.2 ppt | 16 events | dphi +0.009.

## Verdict: CONFIRMED (eclipsing SB1, detached and grazing, with both eclipses detected; circular orbit)

Deciding numbers:
- 18/18 primaries detected individually (S/N 29–50), depth 14.28 ± 0.08 ppt, T14 3.30 h, V/U-shaped (T12/T14 0.4).
- Secondary eclipse detected: 4.90 ppt, S/N 39 on the fold, 14 individual events; same duration as the primary.
- Photometric P = 4.746808 ± 0.000003 d vs Gaia 4.746792 ± 0.000199 (+0.09σ).
- Primary is +1.1–1.3 h (+0.010 phase) from Gaia conjunction A (0.4–0.8σ); secondary −1.4 h from conjunction B (0.4–1.2σ).
- Difference images (TESS-SPOC TPFs, s019/s059/s073) put the loss on the target. In s059 the target-PSF fit has χ² 1082 and the G 10.97 neighbour at 38.5″ has χ² 44311. The secondary-phase difference image (s059) is also on the target: χ² 302 vs 2691.
- Another pipeline (TESS-SPOC PDCSAP) sees the same eclipse: 14.4 / 14.0 / 13.5 ppt in s019 / s059 / s073.
- A heartbeat is excluded. The most generous tidal (Kumar-family) superset fit is worse than the eclipse model by Δχ² = +6141. With Gaia's e and ω fixed it is worse by +20939.

## 1. Archives
- `cats.py 260789413 --r 60` (APPOINTMENTS_DATA = $TEMP\hunt-sb1-scale): VSX none; ASAS-SN none; SIMBAD TYC 3344-341-1 [SB*] at 0.0″ only. Not in Prša+2022, IJspeert+2024, or Kostov t2/t3/t4 (batch ebcats: "none of the vetted/unvetted EB tables").
- VizieR: SB9 none; WDS none; J/AJ/160/111 none.
- Gaia DR3: vari_summary, vari_eclipsing_binary and vari_classifier_result are empty. RUWE 1.06; phot_variable_flag NOT_AVAILABLE.
- ExoFOP: no TOI, CTOI, imaging, spectroscopy or companions.
- Web search on "TYC 3344-341-1" / "TIC 260789413": nothing relevant.
- **New eclipsing binary; no prior art.**

Full Gaia NSS SB1 row (TAP, with corr_vec): P 4.746792(199), e 0.039(8), ω 346.4(18.2)°, Tp 1.711(236) d after J2016, K1 55.52(56) km/s, significance 99.5.

## 2. Eclipse measurements
Inputs: QLP SAP_FLUX with QUALITY==0, no trimming; sectors s019 (30 min), s059, s073 and s086 (200 s). Detrending: a 3-d moving median plus 3 orbital harmonics, with the eclipses masked.

- **Primary (global trapezoid):** depth 14.37 ppt, T14 3.30 h, T12 1.32 h, flat bottom 0.66 h.
- **Primary, per event:** 18 events with timing errors of 0.7–1.8 min. Depth constancy χ² 61/17. Per-sector depths are 14.64 / 14.61 / 13.78 / 14.01 ppt; the spread is consistent with QLP aperture dilution changing between sectors. Odd 14.14 ± 0.10 vs even 14.44 ± 0.11 ppt.
- **Secondary:** at phase 0.49996 ± 0.00018, depth 4.90 ppt, T14 3.30 h [3.23–3.37]. 14 events, depths 3.7–6.1 ppt.
- **Background:**
  - Median in–out SAP_BKG over events is −0.42 ppt-equivalent; a fake dip would need +175 e⁻/s.
  - bkgreg: the flux change the background could imprint is ≤0.04 ppt in every sector.
  - Two s086 events (E386/387) have background jumps of +6 / +23 ppt-equivalent, but their depths are normal.
- **Centroids:** dX −0.5 ± 0.2 mpix, dY +1.9 ± 0.4 mpix.
- **Quality and systematics:** no QUALITY bit 32 in any event window; no event within 0.5 d of a listed sector-wide systematic.
- **Control phases** (0.125–0.875 excluding 0.5): all |depth| ≤ 0.15 ppt, n(S/N > 3) = 0.
- **Blind dip census:** 40 dips with S/N ≥ 4 — 18 are primaries and 13 are secondaries at phase ±0.500. The other 9 are low-S/N s086 features (S/N 4–9). Three are ≥ 7 ppt (3652.909, 3657.679 and 3641.469); the first two sit 0.2 d before the primary eclipses E386/387 in the high-background stretch (the +6 / +23 ppt jumps). No unexplained eclipse-like dips elsewhere.

## 3. Ephemerides and orbit shape
- Primary: P 4.746808 ± 0.000003 d, T0 = 3126.22496 ± 0.00027 BTJD; χ²/dof 48/16; O−C rms 1.6 min.
- Secondary: P 4.746810 ± 0.000006, T0 = 2971.95351 ± 0.00081; O−C rms 5.5 min.
- Δφ(sec − pri) = 0.49996 ± 0.00018 → **e cos ω = −0.0001 ± 0.0003**. Gaia gives +0.036 ± 0.008, which predicts Δφ = 0.5231 ± 0.0051: a **4.5σ tension**.
- Duration ratio 1.00 [0.97–1.02] → **e sin ω = 0.000 [−0.015, +0.010]**. Gaia gives −0.009 ± 0.012, which is consistent.
- The orbit is photometrically circular, as expected for a 4.7-d binary with a subgiant primary. Gaia's e = 0.039 (5σ from zero) is very probably spurious (Lucy–Sweeney-type bias or spot RV jitter). Gaia's conjunction times are still met because the conjunctions do not depend strongly on e at this level.

## 4. Independence and dilution
- **TESS-SPOC (FFI, crowding-corrected PDCSAP):** s019 14.42 ± 0.13 ppt; s059 14.03 ± 0.09; s073 13.48 ± 0.13. SPOC-SAP (not deblended) is 10.9–12.4 ppt.
- **Difference images (TESS-SPOC TPFs, stacked in-eclipse vs local out-of-eclipse):** the max-loss pixel and the loss-weighted centroid coincide with the target in all three sectors. Single-star PSF-fit χ² (target vs G 10.97 neighbour): s019 1168 vs 5470; s059 1082 vs 44311; s073 3385 vs 12717. The secondary (s059) is also on target: 302 vs 2691.
- **Batch diffrun (s059):** deficit 2.5″ from the target. The "14″ from the light centroid" receipt is the light centroid being pulled by the neighbour of nearly equal brightness, not an off-target deficit.
- **Neighbour table** (Gaia DR3, within 60″, G < 15), with the fractional dip each would need = 14.3 ppt × 10^(0.4ΔG):

| Gaia DR3 | G | sep | needed dip | diff-image χ² (s059) |
|---|---|---|---|---|
| 206662835466118400 | 10.97 | 38.5″ | 18.4 ppt | 44311 (target 1082) |
| 206662526228474880 | 14.25 | 49.6″ | 380 ppt | 47241 |
| 206662904185592448 | 14.97 | 22.3″ | 740 ppt | 36097 |

  The G 10.97 neighbour is the only one that could physically host the signal. The pixels exclude it, and so does the period match: P agrees with Gaia's SB1 to 0.09σ and the conjunction phase agrees to 0.01.

## 5. Physics
- f(M) = 0.0842 M☉. With M1 = 1.13 ± 0.15 (TIC): m2(i = 90°) = 0.64 (0.59–0.69) M☉, a = 14.4 R☉.
- Central-eclipse T14 would be 7.6 h; the observed 3.3 h means a grazing geometry (i ≈ 79°, b ≈ 1.1 R1 for R1 = 2.36).
- **Which star is in front:** at A (primary, the deeper eclipse) the cooler companion is in front of the F/G primary. At B the primary occults the companion.
- Depth ratio sec/pri = 0.34. Expected TESS-band surface-brightness ratio for a ~0.65 M☉ dwarf (~4300 K) on a 6050 K primary is ≈ 0.29. Consistent.
- **Mild tensions, both pointing the same way (not a vet issue):**
  - The limb-darkened grazing fit only gives a physical, s ≤ 1 solution for a/R1 ≳ 7, i.e. R1 ≲ 2.05 R☉ vs TIC 2.36 ± 0.22.
  - Observed ellipsoidal A2 is ≈ 1.35 ppt (sector range 0.5–2.35, spot-contaminated; PDCSAP 1.4–1.6) vs 3.1 ppt predicted for R1 = 2.36. A2 ∝ R1³, so this also favours R1 ≈ 1.8–2.0 R☉.
- The A1/A2 harmonics change between sectors, which suggests spots.
- Shape: the LD grazing model beats the trapezoid (χ² 321 vs 350 on 360 2-min bins).
- **Heartbeat check:**
  - The conjunctions are not near periastron (Gaia periastron at phase 0.715), and the photometric e is ≈ 0.
  - Free Kumar-family superset (e, Tp grid; free C, 1/r³, cos2ν/r³, sin2ν/r³): χ² 7238 vs the eclipse model's 1097 on 1367 5-min bins (Δχ² +6141). With 3 harmonics added it is still +2475.
  - A heartbeat cannot produce two flat-bottomed 3.3-h dips 0.5 apart in phase.

## 6. Row fixes for the paper table
- P: 4.74683 → **4.746808 ± 0.000003 d**
- depth: 12.2 → **14.3 ppt** (QLP SAP; PDCSAP 13.5–14.4)
- n events: 16 → **18 primaries + 14 secondaries**
- dphi: +0.009 → +0.0096–0.0111 (fine as is)
- offset: 2.51″ (s059 deficit−target), unchanged
- Add a secondary eclipse: 4.9 ppt at phase 0.49996.
- Note: e cos ω = 0.0000 ± 0.0003 (Gaia e = 0.039 is 4.5σ discrepant; the orbit is circular).

## 7. Next predicted eclipses (BTJD; linear ephemeris)
- **Primary** (T0 3126.22496 + 4.746808 E): 4403.1163, 4407.8631, 4412.6099 (± 1 min).
- **Secondary** (T0 2971.95351 + 4.746808 E): 4400.7427, 4405.4895, 4410.2363 (± 2 min).

## What would settle it further
It is already settled as an EB on this star. Still useful:
- A double-lined spectrum (K2) for masses.
- A light-curve model with free R1 to resolve the radius tension.
- An RV re-reduction to test Gaia's e.

Files: vet.py / vet-out.txt, sec.py / sec-out.txt / sec.png, heartbeat.py / heartbeat-out.txt / heartbeat.png, tpfdiff*.png, indep.py, physics-out.txt, grazing-out.txt, grazing-aR-scan.txt, secratio.py, bkgreg-out.txt, gaia.json, cats-out.txt, morecats-out.txt, nbvari-out.txt. Downloads are in C:\Home\sky\data\qlp-sb-p20-60\pervet260789413\.
