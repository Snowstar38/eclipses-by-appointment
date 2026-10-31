> Historical report: superseded by the current reconciliation at ../../../reports/23999420/REPORT.md. Its original bytes are preserved in the source archive; this public copy is sanitized.

# TIC 23999420 (TYC 6790-120-1): adversarial check

Gaia DR3 SB1, P = 22.13213 ± 0.00771 d, e = 0.186 ± 0.023, ω = 163.7 ± 7.4°, K1 = 16.48 ± 0.36 km/s. G 11.49, Teff 5195 K (GSP-Phot), R 1.99 R☉ (TIC). Checked by an Opus checker for Fable 5.1, 2026-10-22 (chunk-3 wave 3, 18:50–18:58). Saved from the checker's final message by Fable 5.1; the file tool refused REPORT.md. The checker's scripts and outputs are in `my\`, checkpoints in `progress.md`; downloads in `[local path omitted]

## Verdict: CONFIRMED (eclipsing binary, P = 22.12765 d; both eclipses on target)

I couldn't break this one: TIC 23999420 is CONFIRMED as an eclipsing binary with P = 22.12765 d. The secondary eclipse the classifier asked about appears in two independent light curves, sits on the target in the pixels, and lines up with no dip in the other stars of the same sectors.

## 1. Archives: what was queried and what came back
- **Gaia DR3** (TAP, `arch2.py` rerun → `arch2_rerun.txt`/`.json`):
  - The NSS solution is SB1: P = 22.13213 ± 0.00771 d, e = 0.186 ± 0.023, ω = 163.7 ± 7.4°, t_peri = −5.087 ± 0.418, K1 = 16.48 ± 0.36 km/s, significance 45.7.
  - `vari_summary` and `vari_eclipsing_binary` have no rows.
  - Other values: RUWE 1.13, rv_amplitude_robust 33.8 km/s (≈ 2K1), Teff_gspphot 5195 K, logg 4.08. The TIC lists the star as a giant with R = 1.99 R☉.
- **VSX** (60″): the only entry is Gaia DR3 6041428133889590656, 59″ away, type S, G ≈ 18. There is nothing at the target.
- **SIMBAD:** TYC 6790-120-1, type SB* only.
- **ASAS-SN:** none.
- **SB9 and WDS:** none.
- **Eclipsing-binary catalogues on VizieR** (asu-tsv, `arch3.py` → `arch3_b.txt`): Prša+2022, IJspeert+2024, and Kostov+2025 tables 2, 3 and 4 all returned 0 rows. The later parts of `arch3.py` (Gaia EB/Mowlavi, ZTF/ATLAS/WISE variable catalogues, Gaia vari classifier, SIMBAD bibcodes) had not finished when I wrote this, so they are unchecked.
- **ExoFOP:** HTTP 503 at about 18:51 and again at about 19:05, so **CTOIs are unchecked**.
- **NASA Exoplanet Archive TOI table:** no TOI for TIC 23999420.
- **Web search** for "TYC 6790-120-1" / "TIC 23999420": nothing about this star. The hits were unrelated TYC/TIC eclipsing binaries, e.g. [arXiv 2109.08713](http[local path omitted]) and [arXiv 2204.10680](http[local path omitted]).
- **Prior art:** none found.

## 2. Every eclipse measured
Fits are trapezoid × quadratic baseline on raw QLP SAP_FLUX, QUALITY==0, no trimming (`my\ecl.py` → `my\ecl.json`). The A conjunction gives the primary eclipse, P; the B conjunction gives the secondary, S.

| Sector | Kind | Mid-time BTJD | Error (min) | Depth | T14 (h) | T12 (h) | Flat (h) | Flagged cadences in eclipse |
|---|---|---|---|---|---|---|---|---|
| s12 | P | 1641.64 (all cadences) | ±14 | 3.3% | 10.6 | – | – | 20/20, on a background spike |
| s12 | S | 1650.5387 | 4.5 | 0.22% | 9.6 | 0.8 | 7.9 | 0/20 |
| s38 | S | 2336.4775 | 9.6 | 0.23% | 11.2 | 2.0 | 7.2 | 4/61 |
| s38 | **P** | **2349.7517** | 1.4 | **2.16%** | 9.78 | 1.63 | 6.5 | 1/60 |
| s38 | S | 2358.6237 | 6.6 | 0.17% | 10.5 | 1.2 | 8.2 | 5/61 |
| s65 | **P** | **3079.9643** | 1.6 | **2.13%** | 9.67 | 1.56 | 6.5 | 0/181 |
| s65 | S | 3088.8259 | 4.8 | 0.19% | 9.7 | 0.5 | 8.6 | 3/182 |
| s91 | S | 3796.9168 | 4.6 | 0.19% | 10.4 | 0.9 | 8.7 | 0/181 |

- **Not covered by QLP q==0 data:** S at 1628.4 (s12, flagged) and 3774.8 (s91, before the data start), and P at 3788.04 (s91, all flagged at a gap with scattered light). TARS does not cover 3788 either.
- **Centroids:** SAP_X/Y shifts in eclipse are ≤ 2 millipixels at every event except s91 S (+5.6 mpx in y).
- **Background:** SAP_BKG in-eclipse changes are small against its own large relative scatter (the background sits near zero). The background spikes only at s12 P, which I excluded from the ephemeris.
- **Blind dip census** (`my\census.py`, 1-h bins, threshold 0.10%): outside the predicted eclipses, nothing deeper than 0.15% lasts an hour or more, except s65 3082.5–3082.65 (0.19%) and 3089.96–3090.11 (0.22%). Those are the listed s065 3082.8 and 3089.8 common-mode dips.
- **The s65 secondary is not the 3089.8 artefact:** it ends at about 3089.05, and the neighbour test below shows the other stars are clean at 3088.83.

## 3. Ephemeris and the Gaia comparison
Scripts: `my\ephem.py`, `my\ebfit.py` (the limb-darkened two-sphere `ebfit3.py` adapted to this star; output in `my\ebfit_q0.txt`), and `conjmc.py`, which reads this star's own `corr_vec` (output in `conj.json`).

**Primary:**
- From the two clean events, 33 cycles apart: P = 22.127652 ± 0.000044 d, T0 = 2349.7517.
- The 33-cycle count is secure: the next aliases (22.82 d and 21.48 d) are more than 80σ from Gaia's period.

**Secondary:**
- From 5 events: P = 22.12760 ± 0.00008 d, T0 = 2358.61965 ± 0.0031. χ² = 8.9 for 3 degrees of freedom, so I inflated the errors ×1.72.
- O−C = +3, −21, +6, −7, +5 min.
- The secondary period agrees with the primary's (Δ = 0.6σ).

**Joint two-sphere fit** (q==0, all 7 events; reduced χ² 0.93):

| Parameter | Value |
|---|---|
| tP | 2349.75121 ± 0.00013 |
| P | 22.127650 ± 0.000015 d |
| e cos ω | −0.1565 |
| e sin ω | +0.0485 ± 0.0050 |
| e | 0.164 |
| ω | 162.8° |
| i | 89.19° |
| r1 = R1/a | 0.0552 |
| r2 = R2/a | 0.0077 |
| k = R2/R1 | 0.1395 |
| J (surface brightness ratio) | 0.109 |
| L2/L1 (TESS band) | 0.0020 |
| Impact parameter, A / B | 0.24 / 0.26 |

- **Not grazing:** the impact parameters are 0.24 and 0.26, so the secondary is a total occultation with about 8 h of flat bottom. The model secondary sits at phase 0.40063, lasts 10.7 h and is 0.203% deep.

**Against Gaia:**
- **Period:** ΔP = −0.0045 d, which is −0.59σ.
- **Each event against Gaia's predicted conjunction** (full covariance): P events are −0.73σ and −0.70σ; S events are −0.32σ to −0.50σ.
- **Phase separation:** B − A measures 0.4008; Gaia gives 0.388 ± 0.013 (+1.0σ).
- **e cos ω:** fit −0.1565 against Gaia −0.176 ± 0.021 (+0.9σ).
- **e sin ω:** fit +0.049 ± 0.005 against Gaia +0.051 ± 0.025 (−0.1σ).
- **e:** fit 0.164 against Gaia 0.186 ± 0.023 (−0.9σ).
- **ω:** fit 162.8° against Gaia 163.7 ± 7.4° (−0.1σ).

## 4. Independence tests
**Common mode against unrelated stars** (`my\neigh.py`): same box statistic (|dt| < 0.17 d against a linear baseline), raw SAP, q==0, on every other star in the shared folder observed in that sector.

| Event | Target depth | All other stars: median, MAD | Same-CCD stars as deep as the target |
|---|---|---|---|
| S 1650.54 | 2.08 ppt | +0.04, 0.23 ppt (479 stars) | 0 of 19 |
| S 2336.48 | 2.35 ppt | +0.02, 0.34 (324) | 0 of 8 |
| S 2358.62 | 1.78 ppt | +0.08, 0.25 (370) | 0 of 8 |
| S 3088.83 | 1.89 ppt | −0.09, 0.27 (391) | 0 of 17 |
| S 3796.92 | 2.03 ppt | −0.05, 0.25 (165) | 0 of 19 |
| P events | 20.3 ppt | about 0 | 0 |

- About 2–3% of all stars reach the target's depth at any single time. That is the ordinary rate of variable stars, and nothing on the target's CCD does.

**Second pipelines** (`my\pipe2.py`): TARS and GSFC-ELEANOR-LITE, downloaded with `fetch_lc2.py`.

| Pipeline | Event | Mid-time | O−C against my ephemeris (min) | Depth |
|---|---|---|---|---|
| TARS | s12 S | 1650.5373 | +3 | 0.24% |
| TARS | s38 P | 2349.7515 | −0.3 | 2.27% |
| TARS | s38 S | 2336.4746 | −25 | 0.23% |
| TARS | s38 S | 2358.6211 | +2 | 0.12% |
| TARS | s65 P | 3079.9625 | −2 | 2.16% |
| TARS | s65 S | 3088.8365 | +6 | 0.20% |
| TARS | s91 S | 3796.9054 | −17 | 0.25% |
| eleanor-lite | s12 S | 1650.54–1650.55 | | 0.22–0.24% |
| eleanor-lite CORR_FLUX | s12 P | 1641.689 | +32 | 3.1%, scattered light |

**Pixels** (`my\pix.py`): TESScut 15×15 cutouts for s38 and s65; each pixel is fitted with a quadratic trend plus a trapezoid template.

| Event | 3×3 depth | Deficit centroid against light centroid | Notes |
|---|---|---|---|
| P s65 | 2.095 ± 0.020% | 0.3″ | Uniform ~2% across the PSF, so on target |
| P s38 | 2.065 ± 0.018% | 0.1″ | Uniform ~2% across the PSF, so on target |
| S s38 2336.48 | 0.204 ± 0.016% | 3.5″ | Peak deficit on the target pixel at S/N 9.7; uniform ~0.2% across the PSF |
| S s65 3088.83 | 0.158 ± 0.034% | 6.7″ (0.3 px) | Low S/N |
| S s38 2358.62 | 0.161 ± 0.031% | 6.6″ (0.3 px) | Low S/N |

- No pixel of a G < 16 neighbour shows excess depth in any event.

**Dilution:** Gaia DR3 neighbours within 60″ with G < 16.5, against the target's G = 11.49. The fractional dip a neighbour would need is depth × 10^(0.4 Δm).

| Neighbour G | Separation | Needed for P (2.2%) | Needed for S (0.20%) |
|---|---|---|---|
| 16.36 | 21.3″ | 190%, impossible | 18% |
| 15.30 | 41.6″ | 73% | 6.6% |
| 15.19 | 52.0″ | 66% | 6.0% |
| 16.12 | 53.6″ | 142%, impossible | 14% |
| 15.79 | 59.1″ | 115%, impossible | 10% |

- None of these would put the deficit on the target pixel. The primary is impossible from any neighbour.

## 5. Physics
- **Mass function:** f(M) = 0.0097 M☉.
- **Companion mass at i = 89.2°:** 0.25 M☉ for M1 = 1.0, and 0.29 M☉ for M1 = 1.3.
- **Separation:** with the TIC radius R1 = 2.0 R☉, a = R1/r1 ≈ 36 R☉, giving M1 + M2 ≈ 1.3 M☉, which fits M1 ≈ 1.0 plus M2 ≈ 0.28.
- **Companion size and temperature:** R2 = k R1 ≈ 0.28 R☉, which is right for a 0.25–0.3 M☉ M dwarf. J = 0.109 in the TESS band implies Teff2 ≈ 3200 K, against 5160 K for the primary.
- **Which star is in front:**
  - At conjunction A the M dwarf passes in front of the larger star. That is a 2.2% transit with limb darkening.
  - At conjunction B the larger star occults the M dwarf completely. That is the flat 0.20% secondary, whose depth equals L2/(L1 + L2).
- **Durations:**
  - The B/A duration ratio predicted from Gaia's e sin ω is about 1.11. The fit gives 10.7/9.8 h ≈ 1.10, and the trapezoids give about 1.05 ± 0.05.
  - The primary and secondary have the same ingress scale and impact parameter, so both eclipses follow one geometry.
- **Consistency:** depths, durations, shapes, the phase offset, the companion's light, the period and e and ω all agree with the Gaia SB1 orbit within 1σ.

## 6. Verdict: CONFIRMED
- **Primary:** two clean 2.1–2.2% eclipses, 33 cycles apart, matched in TARS. In the pixels they sit on the target and cannot come from any neighbour.
- **Secondary:** a 0.20% total occultation, seen five times in four sectors at a constant phase of 0.4006 with O−C ≤ 21 min. It is reproduced in TARS and eleanor and has no common mode in any of 165–479 comparison stars, so it is not a sector systematic and not the s065 3089.8 dip.
- **Location:** one secondary event is located on the target in the pixels at S/N 9.7.
- **Physics:** the joint fit gives e and ω within 1σ of Gaia, and a companion whose radius, mass and temperature agree with each other as an M dwarf of about 0.28 M☉ and 3200 K.

**Next predicted eclipses (BTJD):**

| Kind | Times | Uncertainty |
|---|---|---|
| Primary (A) | 4341.240, 4363.367, 4385.495 | ±0.004 d |
| Secondary (B) | 4350.105, 4372.232, 4394.360 | ±0.006 d |

These come from tP = 2349.75121, P = 22.12765 and secondary phase 0.40063.

**What would settle it further:**
- Recovering the s91 primary at 3788.04, which is flagged in QLP and missing from TARS, from a TESScut cutout of sector 91.
- RVs to measure K2. A double-lined detection is unlikely because L2/L1 = 0.002.
- An ExoFOP CTOI check once the site is back up.
- The unfinished part of `arch3.py`: the Gaia EB/Mowlavi table and SIMBAD bibcodes.

**Caveats:**
- R1 = 2.0 R☉ is the TIC value, so the absolute masses and radii scale with it.
- The e cos ω error in the joint fit is the formal Hessian value and is surely too small.
