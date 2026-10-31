> Historical report: superseded by the current reconciliation at ../../../reports/262653359/REPORT.md. Its original bytes are preserved in the source archive; this public copy is sanitized.

# TIC 262653359 (TYC 9033-1852-1, Gaia DR3 5824423773088370944): adversarial check

Opus checker for Fable 5.1, 2026-10-22 (chunk-3 wave 2). Saved from the checker's final message by Fable 5.1; the file tool refused REPORT.md.

**Verdict: CONFIRMED.** This is an eclipsing binary on the Gaia SB1 orbit. It shows one eclipse per orbit, at Gaia conjunction **B**. There is no eclipse at conjunction A deeper than 0.2%.

Deciding numbers:
- **Seven eclipses**, at E = −31, −16, −15, 0, 1, 22 and 23. That is two more than the classifier saw: s12 and s39 sit in QLP-flagged cadences (bit 4096) and their light curves are clean.
- **Period:** P = 46.12905 ± 0.00005 d. Gaia's P is 46.096 ± 0.126 d, so the difference is +0.26σ.
- **Conjunction B, not A:** this uses the star's own Gaia covariance.
  - Predicted B minus observed is +0.66 ± 1.48 d at the Gaia epoch (0.45σ), or +0.96 ± 1.17 d when conditioned on the TESS period.
  - Predicted A minus observed is +9.6 ± 0.9 d (10.4σ), or +9.55 ± 1.14 d (8.4σ).
  - The ω error cannot swap the two.
- **On target:** the flux deficit falls on the target pixel in four sectors (s38, s65, s100, s102). The deficit centroid is 0.08–0.25 px from the target. The only neighbour bright enough to matter (G 12.73, 46.7″) shows 0.1–0.3% at its own pixel, against 2.8–3.0% on the target pixel.
- **Independent photometry:** my own TESScut FFI photometry recovers every eclipse it covers. The depth is constant at 3.1%.

## 1. Archives and web
| Query | Result |
|---|---|
| `cats.py --r 60` | VSX 503 (retried below). ASAS-SN none. SIMBAD: TYC 9033-1852-1 [SB*] at 0.0″ |
| VizieR 60″ cones (`arch3.py`) | Prša+2022 0, IJspeert+2024 0, Kostov+2025 t3/t4 0. ZTF, ATLAS, ASAS-SN vars, WISE, ACVS, Justesen, Oelkers, SB9 and VSX: 0 |
| Kostov+2025 table2 (unvetted) | The target is **not** listed. **Three neighbours are**: TIC 262653358 (Tmag 14.51, 31.3″), TIC 262916695 (14.23, 38.9″) and TIC 262916727 (12.02, 46.8″). These are almost certainly this star's eclipses blended into their apertures, and the pixels below say so. Not prior art |
| VSX TAP 120″ (`arch4.py`) | Nothing within 60″. At 81″ there is a G 17.5, 0.372-d EB (Gaia DR3 5823672703564193664); the other entries are ROT stars at 65–119″ |
| Gaia DR3 vari_summary / vari_eclipsing_binary / classifier / rotation / LPV for the target | 0 rows. phot_variable_flag NOT_AVAILABLE |
| Gaia DR3 NSS within 120″ | Only the target's SB1 |
| SB9 | 0 |
| WDS | 503 on every attempt |
| ExoFOP target page and json | 503 throughout (Retry-After 3600) |
| NASA Exoplanet Archive TOI table, target and the 3 neighbours | No TOI |
| SIMBAD | IDs: TIC, Gaia DR1/2/3, GSC 09033-01852, TYC, 2MASS J15181811-6702103. Otypes: *, NIR, SB*. Only reference is 2023A&A...674A..34G (Gaia DR3 NSS) |
| Web search on all names | Nothing about this star |
| MAST CAOM 10″ | QLP s12, 38, 39, 65, 66, 99–102; GSFC-ELEANOR-LITE s12 only. **No SPOC, TESS-SPOC or TGLC** |

So no eclipse has been reported for this star. **WDS and ExoFOP could not be checked** (both returned 503) and should be re-queried before publication.

## 2. Eclipse measurements (raw SAP, trapezoid × quadratic baseline)
Fits are in `ecl.py` / `ecl_flag.py`, results in `ecl_all.json`. Errors are the larger of the red-noise-scaled profile error and the residual-bootstrap error.

| Sector | t0 (BTJD) | ± (min) | Depth (QLP) | T14 (h) | T12 (h) | Notes |
|---|---|---|---|---|---|---|
| s12 | 1644.11247 | 2.7 | 2.97% | 10.00 | 3.90 | 30-min cadence, mostly flag 4096. Clean, no background or centroid feature |
| s38 | 2336.04835 | 1.8 | 3.10% | 9.87 | 3.87 | Pre-ingress cadences flagged; all-quality fit gives the same t0 |
| s39 | 2382.18078 | 1.5 | 3.23% | 9.88 | 3.60 | Flag 4096. SAP_BKG ramps slowly through it, with no feature at the eclipse |
| s65 | 3074.11479 | 1.3 | 3.16% | 9.96 | 3.78 | Clean |
| s66 | 3120.24488 | 18.6 | (4.35%) | (12.2) | (5.2) | SAP_BKG drops at egress, making a +1.5% hump. Shape not usable; excluded from the ephemeris |
| s100 | 4088.95409 | 0.7 | 2.81% | 9.90 | 3.87 | Comes after a flagged scattered-light hump that ends at 4088.2; the eclipse itself is in q==0 data |
| s102 | 4135.08091 | 1.7 | 2.71% | 9.94 | 3.92 | Clean. Small SAP_BKG dips at 4134.2 and 4135.4 do not line up with the eclipse |

- **Total duration:** T14 = 9.9 ± 0.1 h. Ingress is about 3.9 h. The trapezoid "flat" is about 2.1 h.
- **No totality:** the limb-darkened two-sphere fits (`ldfit.py`) find every eclipse partial (grazing) in both geometries, with no T23. The 2-h flat is the rounded bottom of a grazing eclipse.
- **Centroids:** SAP_X/Y show no excursion at any clean eclipse.
- **Blind dip census** (`census.py`, 1-h bins, >0.3%, every sector): nothing except the seven eclipses and background-driven noise in s66 (3097.7–3098.0, 3104.6).
- **Phase scan** (`aside.py`): a fixed-shape eclipse at every offset 0.3–45.8 d, with templates of 6, 9.9 and 14 h. Nothing above S/N 5.3 anywhere. The highest point is the known s99 4067.5 step combined with s66 noise.

**Depths:** QLP gives 3.0–3.2% in s12–s65 and 2.7–2.8% in s100/s102. My TESScut 2×2 photometry gives 3.10, 3.08, 3.10 and 3.16% (s38, s65, s100, s102). So the shallower s100/s102 values are QLP dilution, not a real change. **Adopted depth: 3.1 ± 0.1%.**

## 3. Ephemeris and orbit comparison
`ephem_all.py` fits 6 eclipses (s66 excluded):
- **P = 46.129048 ± 0.000030 d** (χ² 8.6/4, errors scaled). With a 3-min inter-pipeline timing floor, **P = 46.12905 ± 0.00005 d**.
- **T0 = 3489.27618 ± 0.00053 BTJD** (an interpolated epoch). An observed reference is 4135.0809 ± 0.0012.
- O−C is −2.6, −2.3, +2.5, +0.1, (+1.6), +0.4 and −2.8 min.
- The TESScut-only period is 46.129175 ± 0.000033 d.
- Gaia: P 46.0957 ± 0.1259 d, so Δ = +0.0333 d = **+0.26σ**.

**Gaia conjunctions** (`conjmc.py`, `ab.py`; this star's own corr_vec in SB1 order P, γ, K1, e, ω, Tp, with ρ(ω, Tp) = 0.874 and ρ(P, Tp) = 0.806):
- A falls 8.59 ± 1.43 d after B. The A−B phase is 0.186 ± 0.031, or B−A = 0.812 ± 0.037.
- Unconditioned, extrapolated back to the Gaia epoch: B − observed = +0.66 ± 1.48 d (0.45σ); A − observed = +9.58 ± 0.92 d (10.4σ).
- Conditioned on P = 46.129: B = +0.96 ± 1.17 d (0.8σ); A = +9.55 ± 1.14 d (8.4σ).
- **The eclipses are at B.** The A−B separation is fixed mostly by e and ω, and swapping the two would need ω to move by roughly 180°, not 12°.
- The classifier's drifting offsets came from Gaia's P error (σ about 5–11 d at TESS epochs). They are not a disagreement.

**e cos ω and e sin ω:**
- Only one eclipse kind is seen, so TESS cannot measure a phase separation or a duration ratio.
- Gaia, conditioned on the TESS period: **e cos ω = 0.515 ± 0.056, e sin ω = −0.047 ± 0.090** (e 0.525, ω 355°). Unconditioned: 0.503 ± 0.068 and −0.060 ± 0.104.
- **Constraint from the missing A eclipse:** the A eclipse misses (or is a sub-0.2% graze) if e sin ω ≲ −0.07 to −0.08. That is within 0.3σ of Gaia's value; see section 5.

**Conjunction A searched directly** (`aside.py`, `coverage.py`): over B + 4.3…12.9 d (±3σ), the Gaussian-prior-weighted coverage is 0.95–0.99. The only uncovered offsets are 9.74–9.96 d. The 3σ upper limit on an A eclipse there is **0.21–0.23%** for 6–14 h durations, against 3.1% at B.

## 4. Independence
- **Second pipeline:** MAST has no SPOC, TESS-SPOC or TGLC product, and ELEANOR-LITE exists only for s12. So I built my own photometry from TESScut FFI cutouts (`tcphot.py`; background is the median of the faintest 40% of pixels).
  - It recovers every eclipse in s38, s65, s100 and s102.
  - 2×2 aperture: depths 3.08–3.16%, T14 9.87–9.95 h.
  - t0 agrees with QLP within −2.7 to +4.1 min.
- **Difference images** (`diffimg.py`, `diff_s038/065/100/102.png`, in-eclipse window ±0.1 d):
  - In all four sectors the peak deficit pixel is the target pixel.
  - The deficit centroid is 1.6–5″ from the target.
  - The 3×3 aperture holds 70–87% of the 7×7 deficit but only 48–51% of the light.
  - Fractional depth is 2.8–3.0% on the target pixel and 0.1–0.3% on the pixel of the G 12.73 star at 46.7″.
- **Neighbour dilution** (Gaia DR3, G < 15, depth 3.1%): the dip each neighbour would need on its own.

| Neighbour | Separation | G | Dip it would need |
|---|---|---|---|
| 5824423395131318656 | 31.3″ | 14.97 | 99% |
| 5824423708694144640 | 38.9″ | 14.64 | 73% |
| 5824423743053890048 | 46.7″ | 12.73 | 12.5% (ruled out by the pixels) |
| 5824423365096766336 | 61.6″ | 12.68 | 12% (ruled out by the pixels) |

  Nothing else brighter than G 15 lies within 60″. The nearest source is G 17.4 at 3.4″, which would need an impossible >100% dip. Gaia RUWE is 0.95 and ipd_frac_multi_peak is 0.

## 5. Physics (`phys.py`)
- **Primary:** TIC gives Teff 7539 K, R 4.39 R☉, d 1.30 kpc (Gaia GSP-Phot: 6899 K, logg 3.2), so L ≈ 56 L☉. That makes the primary an evolved A/F star of roughly 2–2.5 M☉ (TIC uses 1.74).
- **Mass function:** f(M) = 0.0989 M☉. At i = 90°, m2 = 0.88 / 0.95 / 1.03 / 1.11 M☉ for M1 = 1.74 / 2.0 / 2.3 / 2.6. The companion is probably a G/F dwarf with about 1.5–3% of the TESS light (blackbody estimate).
- **Separation:** a = 75–84 R☉ (0.35–0.39 AU). Separation is about 52–58 R☉ at B and about 58–65 R☉ at A (r_A/r_B = 1.13 for Gaia's e sin ω).
- **Durations:** sky speed is about 101–114 km/s at B and about 90–101 km/s at A. A central eclipse would last about 19–20 h at B and about 21–23 h at A.
- **Geometry from the observed duration:** T14 = 9.9 h means b/(R1+R2) ≈ 0.85–0.87 at B, so i ≈ 85°. This agrees with the grazing shape from the limb-darkened fits.
  - With Gaia's nominal e sin ω, b at A would be 0.96–0.98: a short (4–6 h), very grazing A eclipse.
  - A misses entirely if e sin ω < −0.07 to −0.08.
  - Monte Carlo over the P-conditioned Gaia draws: P(A misses | B shows 9.9 h) = 0.32–0.38. Most of the remaining draws give an A eclipse grazing enough to be shallow.
  - **So the single-eclipse pattern fits the Gaia orbit.** It puts e sin ω at or below about −0.07.
- **Which star is in front** (standard RV convention, ω of the RV primary):
  - At **A** (ν + ω = 90°) the companion is in front of the primary.
  - At **B** (ν + ω = 270°) the primary is in front, so the observed 3.1% eclipse is the primary **partially occulting the companion**. That needs the companion to give ≥4–6% of the TESS light; the limb-darkened occultation fits give L2 = 0.04–0.06.
  - A main-sequence companion of m2 ≈ 1.0–1.1 M☉ gives about 2.5–3.1%. **That is a mild tension (factor ≲2).** It goes away if M1 ≳ 2.6 M☉ or the companion is slightly evolved.
  - In the other reading (a transit), the fits give k = 0.21–0.35, i.e. R2 = 0.9–1.5 R☉, which is natural for the mass function. But that reading needs Gaia's ω to refer to the companion, which is not the DR3 convention.
  - Either way, depth, duration, grazing shape and period fit one geometry. Which star is eclipsed does not change the verdict.

## 6. Verdict and predictions
**CONFIRMED.**
- Seven eclipses fit one linear ephemeris to within 3 min, at 0.26σ from Gaia's period.
- They sit at Gaia's conjunction B (0.5–0.8σ); A is excluded at 8–10σ.
- Pixel-level and independent-photometry checks put the eclipse on the target.
- No catalogue prior art was found. The three Kostov+2025 table2 neighbour flags are this star's blended signal.

**Next eclipses at B** (`predict.txt`, ±3.2 min):

| BTJD | JD |
|---|---|
| 4365.7281 | 2461365.7281 |
| 4411.8572 | 2461411.8572 |
| 4457.9862 | 2461457.9862 |
| 4504.1152 | 2461504.1152 |
| 4550.2443 | 2461550.2443 |
| 4596.3733 | 2461596.3733 |
| 4642.5024 | 2461642.5024 |
| 4688.6314 | 2461688.6314 |

**Conjunction A**, if it shows at all, would be at B + 8.59 ± 1.43 d: 4374.3, 4420.5, 4466.6, 4512.7 … ± 1.4 d. TESS limits it to < 0.2%.

**What would settle it further:**
1. **SB2 spectroscopy** to see the companion's lines, giving the light ratio and the companion's Teff. Spectra at B (BTJD 4365.73) would show whether the companion's lines weaken (an occultation) or the primary's line profile is distorted (a Rossiter–McLaughlin signal, i.e. a transit).
2. **RV follow-up to pin down ω and e:** e sin ω ≲ −0.07 is predicted by the missing A eclipse.
3. **Two-colour photometry of a B eclipse:** occulting a cooler companion makes a deeper eclipse in red; a transit of the hot primary does the opposite.
4. **Re-query WDS and ExoFOP**, which returned 503 during this check.

## Files (all in this folder; data in `[local path omitted])
- **Queries:** `cats.txt`, `arch2.txt`/`archives2.json`, `arch3.txt/json`, `arch4.txt/json`, `toi_nea.txt`, `archives.txt/json`, `gaia_q.txt`/`gaia.json`
- **Conjunctions:** `conjmc.txt`, `ab.py`/`ab.txt`
- **Eclipse fits:** `look.py`/`look_*.png`, `ecl.py`/`ecl.json`/`ecl_fits*.png`, `ecl_flag.py`/`ecl_all.json`, `ldfit.py`/`ldfit.txt/json/png`
- **Ephemeris:** `ephem.py`/`ephem_all.py`/`ephem_all.json`, `ephem_pipes.txt`
- **Coverage and second-eclipse search:** `coverage.py`/`coverage.txt`, `aside.py`/`aside_*.txt/png`, `census.py`/`census*.txt`
- **Pixels and independent photometry:** `tesscut.py`, `diffimg.py`/`diffimg.txt`/`diff_s*.png`, `tcphot.py`/`tcphot.txt`
- **Physics and predictions:** `phys.py`/`phys.txt`, `predict.py`/`predict.txt`
- **Progress log:** `progress.md`

Web searches used (none mention this star): Wikipedia TYC 3801-1529-1; arXiv 2510.05852; arXiv 2510.27470; arXiv 2202.05790.
