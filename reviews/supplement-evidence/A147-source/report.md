# TIC 403936502: per-object vet
Opus 5.5 subagent for Fable 5, 2026-10-19 (wave 3b). Ledger row: G 10.26, P 14.80432 d, 12.7 ppt, 9 events, dphi +0.019.
Star: TYC 2136-2756-1, Gaia DR3 2038397358512598400. Gaia NSS **SB2**: P 14.801518 ± 0.000644 d, e 0.330 ± 0.007, ω 283.5 ± 1.2°, K1 59.4 ± 0.7 km/s, K2 66.0 ± 0.7 km/s.

## Verdict: CONFIRMED. A grazing eclipse at one conjunction of the Gaia SB2; no eclipse is possible at the other.

**Deciding numbers**
1. **The eclipse belongs to the Gaia binary.**
   - The eclipse falls on conjunction B, where the Gaia primary passes in front. Measured at Gaia's own epoch (Tp, BTJD 394), the TESS ephemeris lands **1.06 h (0.003 in phase, 2.4σ) after Gaia's predicted conjunction B**.
   - The ledger's +0.019, and the +5σ offsets at TESS epochs (+6.9 h in s014 growing to +15 h in s081), come entirely from Gaia's period being off by 0.0028 d (4.3σ_Gaia). At TESS epochs the error accumulates over about 88–212 cycles.
   - Conjunction A is 6.6 d away, so there is no ambiguity about which conjunction this is.
2. **It is an eclipse, not a heartbeat.**
   - Conjunction B is only 0.265 d before periastron, which is exactly the blind spot that caught 391918838.
   - Nine events, each in a ±1.5 d window with its own quadratic baseline and noise renormalised per event (N = 5563), were fitted with competing models:

     | Model | χ² |
     |---|---|
     | Free trapezoid | 5765 |
     | Kumar heartbeat, Gaia e and ω fixed (inclination and Tp scanned) | 28478 (Δχ² = **+22713**) |
     | Heartbeat with e free up to 0.97 | 6626 (Δχ² = +861) |

   - Adding a heartbeat term to the trapezoid takes only +0.31 (unit shape) and leaves the depth unchanged at 13.96 ppt (`shape_models.png`, `hb-out.txt`).
   - The dip is 2.8 h long and V-shaped. A Gaia-e tide would be about 1 d wide.
3. **On target, and in other pipelines.**
   - TESS-SPOC pixel difference images in s040, s041 and s074 peak on the target pixel (5,5). A PSF at the target's position fits best in every sector; the next-best star is G 16.48 at 5.8″, which would need a 2500–3100 ppt dip.
   - TESS-SPOC PDCSAP gives 14.2–14.4 ppt (s040/41/74/81), SPOC-SAP 13.3–13.4, TARS 14.0–14.5 (s040/41/74/80/81) and QLP SAP 14.0.
   - The batch diffimg "peak not on target" flag is overturned: its own deficit offset was 2.1″ (0.1 px).
4. **One consistent geometry.**
   - The SB2 gives M1 sin³i = 1.341 ± 0.033 M☉, M2 sin³i = 1.206 ± 0.030 M☉ and a sin i = 34.65 Rsun.
   - At conjunction B the stars are 23.4 Rsun apart with a transverse speed of 20.6 Rsun/d. The 2.82 h duration then gives a half-chord of 1.21 Rsun.
   - Splitting the TIC combined-light radius (2.18) by L ∝ M⁴ gives R1 ≈ 1.5 and R2 ≈ 1.25 Rsun at 0.9× scale. That predicts a QLP depth of **14.8 ppt (observed 14.0)** at i ≈ 83.9°, impact 0.90 (R1+R2): a grazing eclipse of the Gaia secondary. The masses are then 1.36 + 1.23 M☉.
   - At conjunction A the separation is 1.945× larger. An eclipse there would need R1 + R2 < 1.41 Rsun, which is impossible for these masses. So **no second eclipse is expected**.
   - The conjunction-A limit is consistent: a 3–12 h box at the predicted phase 0.4484 ± 0.0047 gives 0.27–0.39 ± 0.05 ppt. That is a broad, edge-of-scan trend, not an eclipse. The free secondary search's best candidate (0.28 ppt, 14 h, phase 0.429) is not repeatable: χ² for constant depth across events is 101/9, the only S/N > 3 event (s080) comes with a 10 mpix centroid shift, and 78 of 301 control phases reach |S/N| > 4.

**Measurements (QLP SAP_FLUX, QUALITY = 0, no trimming)**
- **Shape:** depth 13.97 ± 0.09 ppt, T14 2.82 h (1σ 2.76–2.82), T12 1.13 h (T12/T14 0.4, 0.56 h flat). A V shape (T12/T14 0.5) is worse by Δχ² 68; a box (T12/T14 0.1) is worse by 2020.
- **Events:** nine Q0 events, all with S/N 16–67. Two more sit in flagged-only cadences at the predicted times: s054 2792.29 (QUALITY 4096/6144) and s080 3488.09 (bit 30), with crude dips of 10.4 and 8.9 ppt. s014 has no cadences at its 1696.78 epoch.
- **Depth constancy:** χ² 29.6/8, driven by s054 (17.9 ± 1.1, the noisiest sector at 2.8 ppt/h) and s080 (12.8 ± 0.35). Odd 14.13 ± 0.16, even 13.89 ± 0.11.
- **Ephemeris:** P = 14.804287 ± 0.000006 d, T0 = 3043.96544 ± 0.00021 BTJD. χ²/dof 26.6/7 (errors ×1.95), O−C rms 1.1 min. Jackknife: every leave-one-event-out and leave-one-sector-out P is within 6 ppm-d.
- **e cos ω / e sin ω:** these cannot be derived from timing with only one eclipse kind. The single-eclipse geometry agrees with Gaia (e cos ω +0.077, e sin ω −0.321): r_A/r_B = 1.945 is what removes the second eclipse.
- **Systematics:** none of the events lies within 0.5 d of the listed sector-wide systematics; one window contains a bit-32 cadence. Background regression (unit-free) allows at most 1.24 ppt of fake depth per event, typically under 0.3. Centroid in−out: dX +0.3 ± 0.5, dY +0.35 ± 0.26 mpix. Control phases are all consistent with 0 (|depth| ≤ 0.22 ppt). The blind census found 17 dips at S/N ≥ 4: 9 on the ephemeris, 0 off-ephemeris deeper than 7 ppt.
- **Neighbours (fractional dip each would need):**

  | Neighbour | Needed dip |
  |---|---|
  | G 14.82 at 47″ | 93% |
  | G 15.38 at 33″ and 35″ | 155% |
  | G 16.48 at 5.8″ | 430% |

  None can host it.
- **Archives:** cats.py (VSX, ASAS-SN, Prša+2022, IJspeert+2024, Kostov t2/t3/t4) found nothing. SIMBAD has TYC 2136-2756-1 only as [SB*]. SB9, WDS and J/AJ/160/111 have nothing. Gaia vari_summary and vari_eclipsing_binary are empty. ExoFOP has no TOI/CTOI, imaging or spectroscopy. A web search on the TYC, TIC and Gaia ids found nothing. **New as an eclipsing binary.**

**Row fixes for the paper table**
- P: 14.80432 → **14.804287 ± 0.000006 d**; T0 **3043.96544 ± 0.00021 BTJD**.
- Depth: 12.7 → **14.0 ppt** (QLP SAP; PDCSAP 14.3).
- Duration: **2.82 h**, V-ish, grazing.
- Events: 9 Q0 (+2 in flagged cadences).
- dphi: report the conjunction offset at the Gaia epoch, **+0.003 (1.06 h, 2.4σ)**. The +0.019 figure is an extrapolation of Gaia's P error.
- Notes: eclipse at conjunction B only; the other conjunction is geometrically excluded; Gaia P is 4.3σ off.
- Diffimg: on target (TESS-SPOC s040/41/74).

**Next predicted times (BTJD)**
- Eclipse (conjunction B): **4346.7427, 4361.5470, 4376.3512** (± 0.0006 d).
- Conjunction A, no eclipse expected: **4353.381, 4368.185, 4382.990** (± 0.07 d).

**Would settle it further:** a joint light-curve and RV model with the Gaia SB2 constraint, giving i, the radii and the individual masses (a good benchmark: two F stars, grazing, e = 0.33). Ground-based photometry at a predicted conjunction-A time would confirm the absence of a second eclipse.
