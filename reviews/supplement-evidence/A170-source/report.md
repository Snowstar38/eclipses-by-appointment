# TIC 88457347 (TYC 4114-604-1, Gaia DR3 1099411576514297728): per-object vet

Opus 5.5 subagent, wave 5, 2026-10-21. No earlier session had worked this star. (Saved by the parent session; the file-write tool refused REPORT.md for the subagent.)

## Verdict: **CONFIRMED**. An eccentric F + M-dwarf EB. The eclipse is on target, and the 6.4″ batch offset is a centroiding artefact.

**The numbers that decide it:**
- **Period:** 14 primary eclipses (the batch had 10; s020 adds 4) give P = 5.4689808 ± 0.0000012 d. That is +0.04σ from Gaia's period.
- **Gaia epoch:** the TESS primary, extrapolated back to BTJD ~389, lands **−0.10 h (−0.10σ) from Gaia's conjunction A**.
- **Periastron brightening:** a ~0.8 ppt brightening appears in all four sectors at phase 0.15. Gaia puts periastron at 0.127 ± 0.008.
- **Occultation hint:** 0.33 ± 0.08 ppt at Gaia's conjunction-B phase (0.362, well away from 0.5).
- **Localization:** the PSF-fit deficit is 0.4–1.7″ from the target in 6 pixel products.

## 1. Archives
- cats.py (r = 60″): nothing in VSX, ASAS-SN, Prša, IJspeert or Kostov. SIMBAD lists it as SB*.
- Gaia vari_summary and vari_eclipsing_binary: no rows.
- SB9, WDS, J/AJ/160/111: nothing. ExoFOP: no TOI, CTOI, imaging or spectroscopy.
- Web search on all three ids found nothing.
- Gaia NSS: SB1, e 0.233 ± 0.021, ω 159.2 ± 3.7°, K1 26.41 km/s.
- **RUWE 9.08.**
- Not previously catalogued as eclipsing.

## 2. Light curve (raw QLP SAP, Q0, no trimming)
- **Primary:** 20.57 ± 0.07 ppt, T14 3.30 h, T12 1.15 h, flat bottom 1.0 h. A V shape is worse by Δχ² +573.
- **Per-sector depths:** 20.8 / 20.1 / 20.7 / 20.6 ppt. Odd and even agree (20.44 vs 20.69).
- **Control phases:** all 0 within ±0.13 ppt.
- **Background:** the unit-free regression gives fake dips ≤ 0.7% of the depth in 13 events.
  - E264 (BTJD 3288.06) sits on a +3475 e⁻/s scattered-light ramp. It still fakes only 3%, and its depth is unchanged with background as a regressor.
- **Flags and systematics:** 3 events have a bit-32 cadence, with no depth effect. E201 is 0.3 d from the listed 2943.2 systematic, and its depth is normal.
- **Blind census:** every off-ephemeris dip is either the s060 sector-start scattered light (2939.2–2939.5) or a sidelobe.
- **TESS-SPOC (independent pipeline):** s060 PDCSAP 20.43 / SAP 20.35 ppt, and s073 20.62 / 20.33 ppt, at the same ephemeris.

## 3. Ephemeris, secondary, e cos ω
- **Ephemeris:** T0 = 2730.21937 ± 0.00008 BTJD. χ²/dof 12.6/12, O−C rms 0.5 min.
- **Conjunction A per sector:** within ±0.02 h of every sector's eclipse.
- **Phase 0.5:** nothing (+0.12 ± 0.07 ppt), which is correct for e cos ω = −0.22.
- **Fixed-shape test at Gaia's B phase:** +0.33 ± 0.08 ppt (S/N 4.3).
  - All four sectors are positive.
  - The look-elsewhere controls have rms 1.25σ and a maximum of +2.44σ.
  - The best phase in the scan is 0.3612.
- **e cos ω:** about −0.218, against Gaia's −0.2175 ± 0.022.
- **e sin ω:** not measurable from a 4σ hint. The preferred occultation (2.5 h, shorter than the transit) fits Gaia's more distant conjunction B (r_B/r_A = 1.18).

## 4. Localization
- **Batch hypothesis confirmed:**
  - In diff_s47.json the light centroid (8.051, 7.267) and the deficit centroid (8.039, 7.319) agree to 1.1″.
  - Both sit about 0.30 px from the uncalibrated catalogue x = 7.734, inside a box centred on the rounded pixel 8.
- **A correction to the wave-4 explanation:** boxbias.py shows that a pure box-centring bias on a Gaussian PSF is only 0.00–0.02 px.
  - The remainder comes from the uncalibrated WCS (+0.16 px, 3.5″, in s047) plus the PSF wings or a residual pedestal pulling toward the box centre.
  - So it is the same family of artefact as wave 4, but box-centring alone doesn't account for its size.
- **Own PSF fit at calibrated positions** puts the deficit this far from the target:

| Product | Offset from target |
|---|---|
| TESScut s020 | 1.5″ |
| TESScut s047 | 0.8″ |
| TESScut s060 | 0.4″ (errors over-estimated, as in 449475961's s101) |
| TESScut s073 | 0.4″ (errors over-estimated) |
| SPOC TPF s060 | 1.7″ |
| SPOC TPF s073 | 0.4″ |

- In every product the missing flux is 1.93–2.05% of the target's own flux.
- **Neighbours:** there is no G < 17 neighbour within 54″. The G 14.46 star at 54″ would need a 47% dip and loses its fixed-position fit everywhere.
- **Caveat:** RUWE 9 means an unresolved companion within about 1″, so "on target" means on the Gaia source.

## 5. Physics
- **Companion:** f(m) = 0.0096 M☉. With M1 ≈ 1.3, m2 ≈ 0.29 M☉ (an M dwarf, R about 0.31 R☉), and a ≈ 15.3 R☉.
- **Shape fit:** the limb-darkened model wants k = 0.16–0.18 at b ≈ 0.85, so R1 ≈ 1.7 R☉. k ≥ 0.35 is excluded.
- **Duration:** a predicted T14 of about 3.1–3.4 h matches the 3.30 h observed.
- **Occultation:** the predicted occultation at B for Gaia's e sin ω is 0.24–0.47 ppt, which fits the 0.33 ppt hint.
- One geometry fits everything.

## Next predicted eclipses (BTJD)

| Kind | Times | Uncertainty |
|---|---|---|
| Primary | 4403.7275, 4409.1965, 4414.6655, 4420.1345 (then +5.4689808 d) | ±0.5 min |
| Secondary (~0.3 ppt, phase 0.3612) | 4405.703, 4411.172, 4416.641, 4422.110 | ±~1.8 h |

## What would settle it further
More sectors stacked at phase 0.36 to turn the occultation into a detection; imaging or Gaia DR4 for the RUWE-9 companion; RVs for M1.

**Row fixes:** P 5.4689808(12); depth 20.6 ppt; 14 events; the 6.4″ offset is not real.
