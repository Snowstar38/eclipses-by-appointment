# TIC 283862049 (TYC 2263-89-1, Gaia DR3 2873905966582180864): per-object vet
Opus-model subagent for Fable 5, 2026-10-18 (saved by Fable from the agent's final message; the write tool refused in-agent). Batch row: G 11.09, P 10.14437 d, 7.9 ppt, 4 events, dphi +0.000.

**Verdict: CONFIRMED.** The F8 dwarf (M 1.15, R 1.16 Rsun) is grazed by its Gaia SB1 companion, an M dwarf of about 0.5 Msun.

**Archives**
- `cats.py --r 60`: no VSX, ASAS-SN, Prša, IJspeert or Kostov entry. SIMBAD: SB* at 0".
- Gaia: no `vari_summary` or `vari_eclipsing_binary` entry.
- Gaia NSS SB1: P 10.144581 ± 0.000635 d, e 0.080 ± 0.013, ω 168.2 ± 7.4°, K1 35.68 ± 0.46 km/s, significance 78, RUWE 1.90, ipd_frac_multi_peak 0.
- SB9, WDS and J/AJ/160/111: none. ExoFOP: no TOI or CTOI. Web search: no hits.
- **New as an eclipsing binary.**

**Light curve** (QLP SAP, QUALITY==0, no trimming; `vet-out.txt`)
- Trapezoid fit: depth 7.98 ppt, T14 1.92 h, ingress T12 0.77 h. A V shape is disfavoured by only Δχ² 14 (near-V).
- **6 events, not 4** — sector 17 (30-min cadence) holds two the batch missed. Per-event depths: 8.22, 7.64, 8.63, 8.18, 7.87, 7.83 ppt, S/N 17–26. Weighted depth 8.10 ± 0.14 ppt; depth-constancy χ² 5.0/5 across s17, s57, s84.
- Systematics: no bit-32 cadences in any window, none near the known systematic times. Control phases null, all within ±0.43 ppt. Blind dip census finds 6 dips, all on the ephemeris. Background regression could fake at most 0.03 ppt per sector.

**Ephemeris**
- P = 10.144315 ± 0.000004 d; T0 = 2997.87878 ± 0.00029 BTJD; χ² 0.4/4.
- Jackknife: leaving out one event or one sector, the dropped events are predicted to ≤ 1.6 min.
- Gaia: ΔP = −0.42σ. Conjunction A matched at −0.09 to −0.19σ in each sector.
- Gaia's e cos ω −0.078 ± 0.013 and e sin ω +0.016 ± 0.010 predict secondary phase 0.4503 ± 0.0083.

**Secondary eclipse**
- Not detected. Best point in the Gaia window: 0.51 ± 0.15 ppt at phase 0.442 (7% false-alarm rate); at 0.4503 it is −0.37 ± 0.17 ppt. TESS cannot measure e cos ω here.

**Independence**

| Pipeline | s17 (ppt) | s57 (ppt) | s84 (ppt) |
|---|---|---|---|
| TESS-SPOC PDCSAP | 8.01 ± 0.23 | 8.27 ± 0.21 | 7.60 ± 0.22 |
| TARS | 9.17 ± 0.43 | 7.99 ± 0.40 | 8.39 ± 0.38 |

- SPOC TPF difference images (s57, s84): the loss's position minus the light's position is −0.006 and +0.021 px along the axis to the G 14.0 star at 78"; a neighbour host would give +3.56 px. A PSF fit puts the loss on the target at 7.95 and 7.75 ppt.
- No star brighter than G 17 within 60"; the brightest within 60" is G 19.2, which would need an impossible dip.

**Physics**
- f(M) = 0.047 Msun, so m2 = 0.46–0.55 Msun. a = 23.3 Rsun, a/R1 = 20.2.
- A central transit would last 5.6 h; the observed 1.9 h requires a grazing chord.
- Limb-darkened two-sphere fit with k = 0.44 (R2 0.51 Rsun): b = 1.34, dilution scale 1.09 — fits depth, duration and shape with no third light (TIC contratio 0.001), χ² equal to the trapezoid's.
- Predicted secondary: b_B ≈ 1.38, depth 0.3–0.5 ppt, duration ≈ 1.6 h — matches the non-detection.
- No heartbeat: e = 0.08 and a 1.9 h V-shaped event rule it out.
- The companion is in front at conjunction A, where all six events fall.

**Next predicted eclipses (BTJD)**
- Primary (±1 min): 4407.9386, 4418.0829, 4428.2272.
- Secondary (Gaia phase, ±2.0 h): 4412.507, 4422.651, 4432.795.

**Paper row changes:** n_events 4 → 6; depth 8.1 ppt; mark as grazing. Nothing to strike or demote.
