# TIC 53256660 (TYC 4952-149-1, Gaia DR3 3682572652570849792) — per-object vet

Opus 5.5 subagent, wave 3 relaunch, 2026-10-19. Ledger row: G 11.15 | P 5.16016 | 12.2 ppt | 7 events | dphi +0.015.

## Verdict: CONFIRMED (grazing eclipsing SB1; primary secure, secondary marginal)

Deciding numbers:
- 8/8 primaries detected individually (S/N 22–35). Depth 12.87 ± 0.16 ppt, constant: χ² 4.5/7; s046 12.73 vs s091 12.97 ppt. T14 2.23–2.28 h, V/U-shaped.
- Photometric P = 5.160140 ± 0.000004 d vs Gaia 5.160018 ± 0.000234 (+0.54σ).
- The primary is +1.9 h / +2.6 h (+0.015 / +0.021 phase) from Gaia conjunction A, i.e. 0.75σ / 0.69σ.
- Difference image (TESS-SPOC TPF, s046): the loss is on the target pixel, centroid (5.18, 5.19) vs target (5.26, 5.03). The batch diffrun-c4 (s091) has the deficit 1.7″ from the target and 0.18″ from the light centroid.
- No Gaia source with G < 17 within 90″. The brightest within 60″ is G 17.9 at 37.5″, which would need a dip larger than its whole flux (~6.5×).
- Another pipeline (TESS-SPOC PDCSAP, s046) gives 12.43 ± 0.19 ppt.
- A heartbeat is excluded: Δχ² = +2371 for the most generous tidal superset.

## 1. Archives
- `cats.py 53256660 --r 60`: VSX has "Gaia DR3 3682572652570849792" type ROT at 0″. **This is a type revision (ROT → EA + spots), not prior art.** ASAS-SN none; SIMBAD TYC 4952-149-1 [SB*] only. Not in Prša, IJspeert or Kostov t2/t3/t4 (batch ebcats: none).
- VizieR: SB9 none; WDS none; J/AJ/160/111 none.
- Gaia DR3:
  - vari_summary is present (G range 0.043 mag over 57 epochs, in_vari_eclipsing_binary false).
  - vari_classifier_result: SOLAR_LIKE (score 0.07).
  - vari_rotation_modulation: no row (re-queried with SELECT *).
  - vari_eclipsing_binary: none. RUWE 1.10.
- ExoFOP: no TOI, CTOI, imaging, spectroscopy or companions.
- Web search on "TYC 4952-149-1" / "TIC 53256660": nothing relevant.
- **New eclipsing binary.**

Full Gaia NSS SB1 row (TAP, with corr_vec): P 5.160018(234), e 0.022(12), ω 292.9(36.6)°, Tp 1.067(529) d after J2016, K1 34.29(48) km/s, significance 70.8.

## 2. Eclipse measurements
Inputs: QLP SAP_FLUX with QUALITY==0, no trimming; s046 (10 min) and s091 (200 s). Detrending: a 3-d moving median plus 3 orbital harmonics, with the eclipses masked.

- **Primary (global trapezoid):** 13.01 ppt, T14 2.28 h [2.22–2.28], T12 0.91 h, flat bottom 0.46 h.
- **Primary, per event:** timing errors 0.7–1.4 min. Odd 12.85 ± 0.20 vs even 12.90 ± 0.26 ppt.
- **Background:**
  - The per-event in–out SAP_BKG varies a lot: +28 / +16 / +3 / −10 ppt-equivalent in s046, and +210 at E239 in s091. The depths stay constant regardless.
  - bkgreg: the background-induced flux change is −0.004 ppt (s046) and −0.12 ppt (s091).
- **Centroids:** dX 0.0 ± 0.5, dY −1.9 ± 1.7 mpix.
- **Quality and systematics:** one event window contains a QUALITY bit-32 cadence (E1, s046), and its depth is normal. No event near a listed sector-wide systematic.
- **Control phases:** |depth| ≤ 0.21 ppt except phase 0.5 (+0.92 ± 0.16, the secondary).
- **Blind dip census:** 8 dips with S/N ≥ 4, all 8 on the primary ephemeris; nothing off-ephemeris.
- **Secondary:** 0.85 ppt at phase 0.4986 ± 0.0007 (best-fit shape). With the primary shape fixed at phase 0.500 it is 0.92 ± 0.27 ppt (3.5σ). Per event it is only 1–3σ. Treat it as **marginal**: its timing and its duration ratio (0.69) are not reliable.

## 3. Ephemerides and orbit shape
- Primary: P 5.160140 ± 0.000004 d, T0 = 3411.01065 ± 0.00041 BTJD; χ²/dof 35/6 (errors scaled); O−C rms 1.8 min.
- Secondary (marginal): Δφ = 0.4986 ± 0.0007 (formal error, realistically ≳ 2× larger) → e cos ω ≈ −0.002 ± 0.002. Gaia gives +0.007 ± 0.013 and predicts Δφ = 0.5045 ± 0.0085; consistent (−0.7σ).
- e sin ω: not measurable (secondary S/N too low). Gaia gives −0.016 ± 0.011.
- The secondary ephemeris lands +1.0 h / +1.7 h from Gaia conjunction B (0.4σ / 0.5σ).

## 4. Independence and dilution
- **TESS-SPOC s046:** PDCSAP 12.43 ± 0.19 ppt, SPOC-SAP 12.36 ± 0.19 ppt (4 events).
- **SPOC TPF difference image (s046, 4 events):** the max-loss pixel is the target pixel (S/N 76). Target-PSF fit implied dip 10.4 ppt (crude G→T scaling).
- **Neighbour table:** no Gaia DR3 source with G < 17 within 90″. The batch run lists 3 sources within 60″, the brightest G 17.9 at 37.5″. Needed dip = 12.9 ppt × 10^(0.4 × 6.75) ≈ 6.5× its flux: impossible.
- TIC contratio is 0.002, so dilution is negligible.

## 5. Physics
- f(M) = 0.0216 M☉. With M1 = 1.00 ± 0.12: m2(i = 90°) = 0.34 (0.31–0.36) M☉, an M dwarf; a = 13.9 R☉.
- Central-eclipse T14 would be 5.0 h; the observed 2.23 h means grazing (i ≈ 83.5°, b ≈ 1.13 R1 with R1 = 1.39). The V-like shape fits this.
- **Which star is in front:** at A (primary eclipse) the M dwarf is in front of the G primary. At B the primary occults the M dwarf.
- Expected secondary/primary ≈ the TESS-band surface-brightness ratio (3400 K / 5620 K) ≈ 0.12 → ~1.5 ppt. Observed 0.85–0.92 ppt; same order (grazing and limb-darkening details matter).
- The LD grazing fit is physical (s ≤ 1) only for a/R1 ≳ 11, i.e. R1 ≲ 1.26 vs TIC 1.39 ± 0.07. This is weak (56 bins) and not a vet issue.
- Ellipsoidal amplitude: predicted 0.43 ppt; not measurable, because the out-of-eclipse harmonics are spot-dominated and change between sectors (s046 A1c +3.9 ppt, s091 A2c −3.5 ppt). This is consistent with Gaia's 0.043-mag G range and the VSX ROT label.
- **Heartbeat check:**
  - e ≈ 0.02 and Gaia periastron is at phase 0.56, not at the primary.
  - Free Kumar-family superset: χ² 4217 vs 1846 for the eclipse model on 1103 5-min bins (Δχ² +2371). With harmonics added it is still +1895. Gaia-fixed: χ² 8608.

## 6. Row fixes for the paper table
- P: 5.16016 → **5.160140 ± 0.000004 d**
- depth: 12.2 → **12.9 ppt** (PDCSAP 12.4)
- n events: 7 → **8 primaries** (s046: 4, s091: 4)
- dphi: +0.015 (s046) / +0.021 (s091), fine as is
- offset: 1.7″, unchanged
- Note: VSX ROT → EB type revision; marginal secondary of 0.9 ppt at phase 0.4986.

## 7. Next predicted eclipses (BTJD; linear ephemeris)
- **Primary** (T0 3411.01065 + 5.160140 E): 4401.7575, 4406.9176, 4412.0777 (± 1 min).
- **Secondary** (marginal; T0 3501.3058 + 5.160140 E): 4404.330, 4409.490, 4414.651. The formal error is ± 5 min; ± 15 min is realistic. The primary + 0.5 P gives 4404.338, 4409.498.

## What would settle it further
The primary is settled. Still useful:
- More TESS sectors at 200 s, to firm up the secondary and measure e sin ω.
- Spectroscopy, to check the M-dwarf companion via K2 or IR lines.

Files: vet.py / vet-out.txt, sec.py / sec-out.txt / sec.png, heartbeat.py / heartbeat-out.txt / heartbeat.png, tpfdiff_46.png, indep.py, physics-out.txt, grazing-out.txt, secratio.py, bkgreg-out.txt, gaia.json, gaia-rot-out.txt, cats-out.txt, morecats-out.txt, nbvari-out.txt. Downloads are in C:\Home\sky\data\qlp-sb-p20-60\pervet53256660\.
