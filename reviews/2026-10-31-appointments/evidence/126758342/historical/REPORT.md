> Historical report: superseded by the current reconciliation at ../../../reports/126758342/REPORT.md. Its original bytes are preserved in the source archive; this public copy is sanitized.

# TIC 126758342 (TYC 2185-768-1): adversarial check

Gaia DR3 SB1, P 22.91415 ± 0.04025 d, e 0.376 ± 0.195, ω 289.7 ± 18.1°, K1 33.68 ± 5.4 km/s. G 11.25, BP−RP 0.51, parallax 1.521 mas (about 660 pc), RUWE 1.35, Teff 7380 K (GSP-Phot), R 2.19 R☉ (TIC). Checked by an Opus checker for Fable 5.1, 2026-10-22 (chunk-3 wave 4, 19:11–19:17). Saved from the checker's final message by Fable 5.1; the file tool refused REPORT.md. Scripts, outputs and `progress.md` are in this folder; downloads in `[local path omitted]

## Verdict: CONFIRMED (one eclipse kind only, the B conjunction)

## 1. Archives: what was queried and what came back
- **ExoFOP** (`target.php?id=126758342&json`): HTTP 503, both by curl and in `arch2.py`. CTOIs were not checked.
- **NASA Exoplanet Archive TOI table** (`toi_nea.txt`): no TOI for this TIC.
- **Gaia DR3** (`gaia_q.py` → `gaia.json`; `arch2.py` → `arch2.json`):
  - The star: G 11.25, BP−RP 0.51, parallax 1.521 mas (about 660 pc), RUWE 1.35, Teff_gspphot 7380 K, logg 3.95.
  - Radial velocity: rv_amplitude_robust 70 km/s, rv_chisq_pvalue 0.
  - NSS orbit (SB1): P 22.91415 ± 0.04025 d, e 0.376 ± 0.195, ω 289.7 ± 18.1°, t_periastron −8.433 ± 1.308, K1 33.68 ± 5.4 km/s.
  - vari_summary and vari_eclipsing_binary both returned 0 rows.
- **VizieR TAP**: SB9 0, WDS 0. VSX returned 1 row: Gaia DR3 1852163827032966528, type ROT, P 6.1668 d, G 17.8, 25.0″ away. That is the neighbour, not the target.
- **VizieR asu-tsv 60″ sweep** (`viz.txt`):
  - VSX: only the same ROT neighbour.
  - Zero rows from Prša+2022, IJspeert+2024, Kostov tables 2/3/4, ASAS-SN II/366, SB9, WDS, ATLAS, Gaia vclassre and ASAS ACVS.
  - The "Mowlavi" query returned 443 rows; that is the synthetic-photometry table, not prior art.
- **cats.py**: VSX only the ROT neighbour; ASAS-SN none; SIMBAD lists TYC 2185-768-1 as [SB*], with no eclipse type.
- **MAST CAOM** (`archives.py`):
  - QLP s15 (1800 s), s41 and s55 (600 s); TESS-SPOC s15, s41, s55; TASOC s15.
  - No SPOC 2-min data, TARS or eleanor.
  - TESScut covers only sectors 15, 41 and 55.
- **Web search**: not done, for time.
- **Novelty**: no eclipsing-binary listing anywhere. The VSX ROT entry belongs to a G 17.85 star 25″ away; it is neither prior art nor a type revision of the target.

## 2. Eclipses (`look.py` → census.txt and overview.png; `ecl.py` → ecl.txt, ecl.json, ecl_fits.png)
**Blind census** (all three sectors, quality-0 cadences, 0.2-d box, threshold above 0.6%): the only dips are the three events below.

**The three events.** All are V-shaped and fall at the Gaia B conjunction (ν = 270° − ω), where the primary passes in front of the companion. Trapezoid fits on raw SAP:

| Event | Pipeline | t0 (BTJD) | Depth | T14 | T12 | Flat |
|---|---|---|---|---|---|---|
| s15 | QLP | 1729.5390 ± 4.1 min | 1.93% | 6.41 h | 2.36 h | 1.70 h |
| s15 | TESS-SPOC | 1729.5456 ± 4.3 min | 1.84% | 6.25 h | | |
| s15 | TASOC | 1729.5461 ± 8.8 min | 1.48% | 6.19 h | | |
| s41 | QLP | 2438.5079 ± 4.7 min | 1.90% | 5.88 h | 2.01 h | 1.87 h |
| s41 | TESS-SPOC | 2438.5083 | 1.67% | 6.19 h | | |
| s55 | QLP | 2804.4287 ± 3.4 min | 2.10% | 5.99 h | 2.60 h | 0.79 h |
| s55 | TESS-SPOC | 2804.4292 | 1.97% | 6.02 h | | |

- The deepest points reach about 2.2%. The trapezoid "flat" is not real totality; the shape is a partial eclipse.
- **Quality flags:** no flagged cadences inside any eclipse. QLP fits on all cadences agree with the quality-0 fits.
- **Centroids:** shifts of at most 0.0017 px (QLP SAP_X/Y, TESS-SPOC MOM_CENTR), within 1.3σ of the out-of-eclipse scatter.
- **Background (in its own units):**
  - s15 and s41: no excursion.
  - s55: the background is 1.6σ (QLP) and 1.8σ (TESS-SPOC) lower in eclipse. A lower background raises SAP flux, so it cannot make a dip.
- **Known systematics:** no event coincides with any time on the known list.

## 3. Ephemeris and Gaia comparison (`ephem.py` → ephem.txt; `conjmc.py` → conjmc.txt, reading this star's own corr_vec)
- **Linear ephemeris for B:** T0 = 1729.54161 ± 4.3 min, P = 22.86993 ± 0.00008 d, χ² 0.52 for 1 degree of freedom.
  - O−C at cycles 0, 31, 47: +1.3, −2.0, +0.7 min.
- **Against Gaia's period:** Δ = −0.044 d, which is −1.10σ.
- **Against each predicted B conjunction:**
  - 1732.09 ± 2.92 (−0.87σ)
  - 2442.47 ± 4.08 (−0.97σ)
  - 2809.12 ± 4.69 (−1.00σ)
  - The steady drift is fully explained by the 1.1σ period difference.
- **Against the A conjunctions:** the nearest predicted A times (1718.18, 2428.59, 2795.25) are 7–11 d from the events, so these are not A eclipses.
- **Aliases:** P/2, P/3 and P/4 are excluded. Their extra epochs are covered by data with no dip (|depth| ≤ 0.14%).
- **No A eclipse is seen:**
  - Each sector is longer than P, so every orbital phase is covered.
  - Gaia's Monte Carlo puts A at phase 0.414 ± 0.111 after B.
  - In phases 0.303–0.525: no dip above 0.105%. The 3σ upper limit has a median of 0.18% and is 0.28% at worst (3-h box); 0.14% and 0.20% with a 5-h box.
  - Over the whole orbit, the worst 3σ upper limit is 0.46% (3-h box) or 0.35% (5-h box).
  - The highest-significance bump is 0.19% (4.5σ) at phase 0.24. It lands at sector edges (1712.16, 2421.13, 2444.0) and is not eclipse-like.
- **e cos ω** cannot be measured, because there is no second eclipse kind. Gaia gives e cos ω = +0.13 ± 0.17 and e sin ω = −0.34 ± 0.13.

## 4. Independence tests
- **Other pipelines:** TESS-SPOC (all three sectors) and TASOC (s15) show every event at the same time and at 1.5–2.0% depth.
- **Pixel level** (`pixreg_trap.py` → pixreg.txt and pix_s15/s41/s55.png): per-pixel fit of each 11×11 TESScut cutout with a quadratic trend plus a unit trapezoid template. Three sectors, two cameras.

  | Sector | Deficit centroid to light centroid | Deficit centroid to target | Target-pixel depth |
  |---|---|---|---|
  | s15 | 2.2″ | 2.8″ | 1.97 ± 0.17% |
  | s41 | 1.3″ | 4.0″ | 1.90 ± 0.07% |
  | s55 | 2.9″ | 2.0″ | 1.87 ± 0.13% |

  The flux deficit peaks on the target pixel in every sector.
- **Neighbour dilution** (dip a neighbour would need = 2.0% × 10^(0.4 ΔG)):
  - G 15.87 at 13.8″: 141%. It shares the target's pixel, so the pixel fit cannot separate it, but it would need a 141% dip, which is impossible.
  - G 13.87 at 34.2″: 22%. Its pixel shows only 0.3–1.2%, which is the target's wings, and the deficit would sit 1.6 px off target. Neither is seen.
  - The ROT star, G 17.85 at 24″: about 870%, impossible.
  - G 15.45 at 55.8″: 95%, impossible.
- **The classifier's centroid concern is resolved:** the dip is on the target.

## 5. Physics (`physics.py` → physics.txt)
- **Mass function:** f(M) = 0.0721 M☉.
- **Companion:** m2 at i = 90° is 0.68, 0.73 or 0.78 M☉ for M1 = 1.4, 1.59 or 1.8. That suggests a K dwarf of about 4700–5000 K and 0.70–0.80 R☉, giving 2.5–4.3% of the light in the TESS band.
- **Orbit size:** a = 43–47 R☉.
- **Which conjunction is which:**
  - B is the primary (an A-type star, R 2.19 R☉) in front of the companion, so B is an occultation of the companion.
  - With e sin ω ≈ −0.34, B is the near conjunction; the separation at A is about 2.0 times the separation at B.
- **Monte Carlo** (Gaia covariance, M1 between 1.4 and 1.8, main-sequence companion):
  - Central T14 at B is 7.8 h [6.4, 9.3], longer than the observed 6.1 h. So b/(R1+R2) ≈ 0.65, i ≈ 86.5°, and the eclipse is partial in 82% of draws. That matches the V shape.
  - The A conjunction misses in 83% of draws.
  - The predicted B depth is 2.1% [1.1, 3.5], against 2.0–2.2% observed.
  - Where A would eclipse, it would be about 1.4% deep or more, which the 0.35–0.46% limit excludes.
  - For A to miss, e sin ω must be below about −0.15 to −0.2. Gaia's −0.34 ± 0.13 agrees, so the geometry predicts the missing eclipse.
- **Overall:** depth, duration, shape and the absent A eclipse fit one geometry. The 2.2% B depth is consistent with partly occulting the companion light expected from the mass function.

## 6. Verdict: CONFIRMED
**Deciding numbers:**
- Three eclipses on target, each at the Gaia B conjunction (−0.9 to −1.0σ).
- The linear ephemeris holds to 2 min over 47 cycles (χ² 0.5).
- P = 22.86993 d against Gaia's 22.914 ± 0.040 (−1.1σ).
- The pixel-level deficit sits on the target in three sectors and two cameras, and the events appear in three pipelines.
- No neighbour can produce the dip.
- Only one eclipse kind is seen, and the absence of an A eclipse (below 0.35–0.46%) is what Gaia's e sin ω predicts.

**Next predicted B eclipses (BTJD, ±9 min):** 4336.7137, 4359.5837, 4382.4536, 4405.3235 (then +22.86993 d each).

**A conjunction:** no eclipse is expected. If the geometry is wrong, an A event would fall near 4346.18, 4369.05, 4391.92 or 4414.79, each ±2.5 d.

**What would settle it further:**
- An RV orbit that sharpens e and ω, which would test whether A has to miss.
- A limb-darkened two-sphere fit of the B shape for the radius ratio and b (not done, for time).
- Any future TESS sector to extend the ephemeris.

**Not checked:** ExoFOP (HTTP 503, so CTOIs unchecked) and the web search on the star's names.
