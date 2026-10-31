> Historical report: superseded by the current reconciliation at ../../../reports/277542587/REPORT.md. Its original bytes are preserved in the source archive; this public copy is sanitized.

# TIC 277542587 (TYC 1007-1061-1): adversarial check

Gaia DR3 4488407400334098432, SB1, P 24.326 d, e 0.346 ± 0.015, ω 214.6 ± 2.7°; TIC R 2.82 R☉. Checked by an Opus checker for Fable 5.1, 2026-10-22 (chunk-3 wave 6, 19:37–19:46, under a 15-minute cap). Saved from the checker's final message by Fable 5.1; the file tool refused REPORT.md. Scripts and outputs are in this folder, each step checkpointed in `progress.md`; the TESScut cutout is in `[local path omitted]

## Verdict: CONFIRMED

This is an eclipsing binary on the target and on Gaia's orbit. It has one sector of data (s080) with one eclipse of each kind.

## 1. Archives and web
- **ExoFOP:** HTTP 503 on the one try, so CTOIs are unchecked.
- **NASA Exoplanet Archive TOI table** (`tid=277542587`): 0 rows.
- **`viz.py`** (VizieR asu-tsv 60″ cones):
  - VSX, Prša+2022, IJspeert+2024, Kostov t3 and Kostov t4: 0 rows.
  - Kostov t2 (an unvetted ML list): one row, TIC 277542595 at 33.8″ (Tmag 14.79, the G 15.39 neighbour). It is not the target and is not prior art.
  - `viz.py` hung after the Kostov t4 cone. I re-queried the next cones by curl: SB9, WDS, the Gaia DR3 variability classifier (I/358/vclassre) and the ASAS-SN variables (II/366) each returned HTTP 200 with 0 rows.
  - Never checked: Mowlavi+2023, ATLAS and ASAS ACVS.
- **`cats.py`:** no VSX or ASAS-SN entry; SIMBAD lists TYC 1007-1061-1 as type [SB*].
- **Gaia DR3 (TAP):** no `vari_summary` row. The full NSS row with `corr_vec` is in `archives2.json` (`nssfull.py`).
- **MAST** (CAOM, 10″, `archives.py`): only HLSP QLP s080 at 200 s. There is no SPOC, TESS-SPOC, TGLC, TASOC or eleanor product.
- **Web search** for "TYC 1007-1061-1": nothing about this star.
- **Status:** no prior art found. The eclipses look new.

## 2. Eclipses (`ecl.py` → `ecl.json`, `ecl.png`; census in `look.py`)
Fits use raw SAP_FLUX, a trapezoid and a quadratic baseline over ±0.8 d.

| | A (ν = 90°−ω, companion in front) | B (ν = 270°−ω, primary in front) |
|---|---|---|
| Mid-time (BTJD) | 3488.8242 ± 0.0020 | 3496.7501 ± 0.0027 |
| Depth | 7.76% | 14.92% |
| T14 | 12.37 h | 9.98 h |
| Ingress (T12) | 4.85 h | 3.80 h |
| "Flat" bottom | 2.7 h | 2.4 h |
| Cadences used | all-quality fit, t > 3488.35 | q0 = all-quality |
| Flagged cadences in eclipse | 197 of 223 | 0 |
| Background (raw SAP_BKG, e⁻/s) | smooth, monotonic | flat |
| Centroids | x +0.02 sd, y −1.9 sd | SAP_Y −0.006 px (−1.7 sd) tracks the dip |

More on A:
- The flags are bits 2048 and 2^30, from the tail of a large scattered-light episode (peak 3.9×10⁵ e⁻/s at 3488.2).
- A fit to q0 cadences only can't be used: there is no q0 data before ingress.
- Through the eclipse the background falls smoothly from 2×10⁴ to 3×10³ e⁻/s, with no dip-shaped feature. The eclipse itself is symmetric and V/U-shaped, and the flux before it is flat at 1.0.

More on B: the background is −337 e⁻/s in eclipse against −262 ± 96 out of eclipse. The small centroid shift tracking the dip is what an on-target eclipse with slight contamination would give.

**Blind census** (1-h bins below −1%):
- In q0 cadences, only these two events.
- With all cadences, also 3485.24–3485.70 at −3.4%. That sits inside the flagged scattered-light mess, where background reaches 8×10⁶ in median-flux units.

## 3. Ephemeris and the Gaia comparison
Scripts: `conjmc.py` (this star's own `corr_vec`) → `conjmc.txt`; `ephem.py` → `ephem.txt`. With one eclipse of each kind there is no independent period.

- **A:** Gaia predicts 3488.317 ± 0.842. O−C is +0.507 d (+0.60σ).
- **B:** Gaia predicts 3496.052 ± 0.843. O−C is +0.698 d (+0.83σ).
- **B−A separation:** 7.9260 d, which is phase 0.3258 ± 0.0002. Gaia's Monte Carlo gives 0.3179 ± 0.0102, so the difference is +0.77σ. This is the test that does not depend on the period.
- **e cos ω** from the separation is −0.2718. Gaia gives −0.2845 ± 0.0165 (0.8σ).
- **Durations:** the trapezoid T14 ratio A/B is 1.24, which taken naively implies e sin ω = −0.107. That reading is invalid here because A is near-grazing. So I fitted a limb-darkened two-sphere model (`ebfit_s80.py`, model code from `ebfit3.py`; P fixed at Gaia's value).
- **Two-sphere fit, free:**
  - e cos ω = −0.2720, e sin ω = −0.186, e = 0.329, ω = 214.4°.
  - Gaia: e = 0.346 ± 0.015, ω = 214.6 ± 2.7°, e sin ω = −0.196 ± 0.015.
  - So e sin ω agrees within 0.7σ, and ω agrees almost exactly.
  - i = 87.15°, R1/a = 0.0560, R2/a = 0.0255, k = 0.455, J = 1.01.
  - L2 is 16.7% of the light. Impact parameters in units of R1: A 0.97, B 0.67. Residual rms 2.38 ppt.
- **Two-sphere fit with e sin ω fixed at Gaia's value:** Δχ² = +13 (formal, before red-noise inflation; β = 1.5–2.1).
- **Profile in e sin ω:** the minimum is near −0.18 to −0.19. The naive −0.10 is excluded at Δχ² = 723.

## 4. Independence
- **Other pipelines:** there are none on MAST, so this test was not possible.
- **TESScut pixel test** (`pixtrap.py`, which is `pixreg.py` with the trapezoid as template; output in `pix_B.txt`, `pix_A.txt`, `pix_s80*.png`). This is also an independent FFI photometry.
  - **B:** fractional depth is 15.03 ± 0.04% (1×1), 14.88% (3×3) and 14.77% (5×5), so it is constant across apertures. The deficit centroid is 0.4″ from the light centroid.
  - **A** (all cadences): 7.82 ± 0.05%, 7.81% and 7.79%. The deficit is 0.3″ from the light centroid.
  - **Neighbour pixels:** the pixel of the G 13.32 star at 84.5″ shows −0.11 ± 0.09% (B), and the G 14.77 star at 85.8″ shows −0.04%. The G 15.39 neighbour's pixel shows 14.4%, but that pixel is in the target's PSF wing.
  - One faint wing pixel at (11,7) has a noisy fractional depth of about 19%. It is not at any neighbour, and the deficit map is centred on the target.
- **Dilution table** (dip a neighbour would need = depth × 10^(0.4ΔG)):
  - Every Gaia source within 90″ brighter than G 16 would need more than 100% for B, except the G 13.32 star at 84.5″. That one would need 88%, and its own pixel is flat.
  - The G 18.23 source at 5.8″ would need 8000%.
  - So contamination is excluded.
- **The other conjunction:** both kinds were observed, so no null limit was needed.

## 5. Physics (`physics.py` → `physics.txt`)
- **Mass function:** f(m) = 0.1851 M☉. This gives m2(i = 90°) = 0.97, 1.07, 1.18 or 1.25 M☉ for M1 = 1.25, 1.5, 1.8 or 2.0, and a = 46–52 R☉.
- **Separation at conjunction:** 50–57 R☉ at A and 34–38 R☉ at B.
- **Central durations:** about 17–18 h at A and 11–12 h at B. The observed 12.4 h and 10.0 h fit a single inclination: A is near-grazing (larger separation) and B is more central (b_A/b_B ≈ 1.49).
- **Radii:** R1 = 0.056a = 2.6–2.9 R☉, matching the TIC value of 2.82. R2 = 1.2–1.3 R☉.
- **Why B is deeper** (the classifier's question): it is geometry.
  - J ≈ 1 means the two stars have about equal surface brightness, so depth follows overlap area.
  - Because e sin ω < 0, B happens at the smaller separation. The primary therefore covers most of the companion at B (16.7% of the light), while at A the companion only grazes the primary's limb.
- **Companion:** a star of about 1.2 M☉ and Teff near the primary's. That needs M1 ≈ 1.8–2.0 M☉, i.e. a slightly evolved F primary, rather than the TIC's 1.25. That is mild and plausible.
- **Why SB1:** a 17%-light companion of similar temperature could be blended in Gaia RVS. This is worth noting but is not in tension with anything.

## 6. Verdict: CONFIRMED
The deciding numbers:
- Both eclipses fall within 0.6σ and 0.8σ of Gaia's conjunctions.
- The B−A phase agrees within 0.77σ, and e cos ω within 0.8σ.
- The two-sphere e sin ω (−0.186) and ω (214.4°) match Gaia's (−0.196, 214.6°).
- Depth is constant across 1×1, 3×3 and 5×5 apertures, with the deficit centroid within 0.4″ of the light centroid.
- No neighbour can produce the depth.

Caveats:
- Single sector.
- A is mostly in flagged scattered-light cadences, though its pixel-level depth is identical.
- No second pipeline exists.

**Next predicted eclipses** (BTJD; anchored on the observed times with Gaia's P, error n × σP):

| A | B |
|---|---|
| 4340.243 ± 0.24 | 4348.169 ± 0.24 |
| 4364.569 | 4372.495 |
| 4388.895 | 4396.821 |
| 4413.222 | 4421.148 |
| 4437.548 ± 0.27 | 4445.474 ± 0.27 |

Gaia-only predictions are later by about 0.5–0.7 d, with σ about 1.08 (`conj_future.txt`).

**What would settle it further:**
- A second TESS sector or ground photometry at any of these times, which would give a real period.
- Spectra to look for the second set of lines (SB2), since the companion should carry about 17% of the light.

**Not done:** the CTOI check (ExoFOP down); three of `viz.py`'s VizieR cones (Mowlavi+2023, ATLAS, ASAS ACVS); and a common-mode check against unrelated s080 stars, which the checker judged unnecessary for a clean, 15%-deep, on-target event.
