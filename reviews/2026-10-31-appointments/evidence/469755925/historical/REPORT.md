> Historical report: superseded by the current reconciliation at ../../../reports/469755925/REPORT.md. Its original bytes are preserved in the source archive; this public copy is sanitized.

# TIC 469755925 (TYC 7931-842-1): adversarial check

Gaia DR3 6739146911148825344, SB1, P 23.32374 ± 0.00949 d, e 0.046 ± 0.033, ω 154 ± 41°, K1 17.17 km/s. G 11.13, parallax 3.97 mas, RUWE 0.91. Checked by an Opus checker for Fable 5.1, 2026-10-22 (chunk-3 wave 3, 18:50–19:02). Saved from the checker's final message by Fable 5.1; the file tool refused REPORT.md. Scripts and outputs are in this folder, the step-by-step record in `progress.md`; downloads in `[local path omitted] From the earlier stopped checker's files only the code was reused (vetlib.py, conjmc.py, gaia_q.py, arch2.py, archives.py, fetch_lc2.py), and every script was rerun.

## Verdict: CONFIRMED

This is a detached eclipsing binary: an M dwarf companion transits a G star. Both eclipse kinds are real, both are on the target, and the timing matches the Gaia SB1 orbit to within 0.3σ. This is a new eclipsing binary in every catalogue I could reach. It is not entirely unseen, though: SPOC raised TCEs on it at the wrong periods, and it never became a TOI.

## 1. Archives and web
- **Gaia DR3** (`gaia_q.py`, `arch2.py`):
  - SB1 solution: P 23.32374 ± 0.00949 d, e 0.046 ± 0.033, ω 154 ± 41°, K1 17.17 km/s, significance 26.
  - G 11.13, parallax 3.97 mas, RUWE 0.91.
  - `rv_amplitude_robust` is 33.8 km/s, which matches 2K1.
  - vari_summary and vari_eclipsing_binary: no rows.
- **VizieR** (asu-tsv 60″ cones, `viz.py`): no rows in VSX, Prša+2022, IJspeert+2024, Kostov+2025 t3/t4, ASAS-SN II/366, SB9, WDS, ATLAS, ASAS ACVS or Gaia vclassre.
  - Kostov t2 (the unvetted list) contains only a neighbour, TIC 469755932 (T 14.16, 41.7″ away). Its flag is probably our star's eclipses leaking into its aperture.
- **cats.py**: no VSX or ASAS-SN entry; SIMBAD has TYC 7931-842-1 typed as SB*. `cats.py` printed only those three lines and nothing for its other catalogues; `viz.py` covered them instead.
- **arch3.py**: hung for more than 15 minutes, with four other checkers' copies running at the same time. I stopped my own copy (PID 2908) and replaced it with `viz.py`.
- **ExoFOP**: HTTP 503, tried once (`arch2.py`). CTOIs are therefore unchecked.
- **NASA Exoplanet Archive TOI table**: no TOI for TIC 469755925.
- **MAST** (`archives.py`): QLP s13/27/67/94; SPOC 2-min s27/67/94; TESS-SPOC s13/27/67; TARS s13/27/67/94; eleanor-lite s13; SPOC multi-sector DV runs s1–s69 and s1–s96.
- **SPOC DV reports** (`dvlist.py`): these are prior pipeline flags, not a catalogued EB. Each fit gives `suspectedEclipsingBinary=false`.
  - s67 TCE: P 17.107 d, epoch 3127.978, depth 40850 ppm, 7.76 h.
  - s1–s96 TCE-1: P 277.156 d, epoch 2036.459, depth 41960 ppm, MES 174. TCE-2: P 39.28 d, MES 23.
  - s1–s69 TCE: P 6.19 d, MES 108.
  - The SPOC 2-min light curves have no data dips at 2036.46 or 3127.98. These are fold epochs; the TCEs come from the A eclipse at 3145.08.
- **Web search** for "TYC 7931-842-1" / "TIC 469755925": nothing relevant. The results were unrelated papers, e.g. [arXiv 2302.00320](http[local path omitted]) and [arXiv 2510.27470](http[local path omitted]).

## 2. Eclipses measured
All fits are trapezoids with a quadratic baseline on raw SAP or raw flux (`ecl.py` → `ecl.txt`, `ecl_fits.png`). Timing errors are the profile-χ² error times a red-noise β.

**Eclipse A: the deep one, 4.0–4.2% deep, flat-bottomed (annular)**

| Event (sector) | Pipelines | Mid-time (BTJD) | Error | Depth | T14 | Ingress (T12) | Flat |
|---|---|---|---|---|---|---|---|
| s13 | QLP, TESS-SPOC, TARS, eleanor | 1675.7384 (spread 1675.7370–.7396) | 1.6 min | 3.98–4.15% | 7.49–7.66 h | 1.4–1.7 h | 4.2–4.7 h |
| s67 | QLP, SPOC 2-min, TESS-SPOC, TARS | 3145.0842 (spread .0839–.0848) | 0.8 min | 4.00–4.18% | 7.42–7.52 h | 1.5 h | 4.5 h |
| s94 | SPOC 2-min only | 3868.0984 | ~1.5 min | 4.01% | 7.27 h | 1.32 h | 4.63 h |

- The s94 eclipse sits in QUALITY-flagged pre-gap scattered-light cadences (157 flagged cadences in eclipse). The background rises there, but the shape and depth are identical to the other two A events. QLP is unusable at that time.
- The classifier missed this eclipse.

**Eclipse B: the shallow one, 0.25–0.40% deep, flat-bottomed (total)**

| Event (sector) | Pipelines | Mid-time (BTJD) | Error | Depth | T14 | Note |
|---|---|---|---|---|---|---|
| s13 | 4 | 1663.2814 | 4 min | 0.28–0.40% | 7.4–8.5 h | |
| s27 start | QLP, SPOC, TESS-SPOC | 2036.4538 | 4 min | 0.32–0.35% | ~7.6 h | Mostly egress; data starts at 2036.28 |
| s27 end | flagged cadences | 2059.769 | 7 min | 0.26–0.30% | | Marginal |
| s67 | 4 | 3132.628 | 2.5 min | 0.32–0.40% | 8.0–8.5 h | |
| s94 | QLP, SPOC, TARS | 3878.964 | 3 min | 0.25–0.28% | 7.9–8.1 h | |

- The classifier discounted the s94 B dip as a "background jump". I find no background excursion there: SPOC ΔBKG −0.6 (sd 3.8), QLP −3.9 (sd 23.5), each in its own units. It is real, it is in three pipelines, and it is on ephemeris.

**Background and centroids:** no unflagged event shows a background excursion beyond 1σ. The SPOC MOM_CENTR shift is ≤0.001 px for A and ≤0.002 px for B.

**Blind dip census** (QLP q==0, 0.25-d box, depth >0.15%, `lcview.py`): apart from the A and B events, it found only:
- s13 at 1657.7 and 1661.1: about 0.2%, broad, in the noisy orbit-start stretch, and not at any conjunction phase;
- s94: ramps at the sector and orbit edges, and the known s094 3875 systematic.

## 3. Ephemeris and Gaia comparison
From `ephem.py`; the conjunctions come from `conjmc.py`, which uses this star's own `corr_vec`.

**Linear fits**

| Fit | T0 (BTJD) | P (d) | O−C | χ² |
|---|---|---|---|---|
| A | 1675.73759 ± 1.5 min | 23.322972 ± 0.000016 | +1.1, −0.9, +2.0 min | 3.4 / 1 dof |
| B | 1663.28274 ± 2.8 min | 23.322955 ± 0.000031 | all within 5.5 min | 3.1 / 3 dof |
| Joint (common P) | A 1675.73779 ± 1.4 min; B 1663.28204 ± 1.9 min | 23.322969 ± 0.000014 | | 6.7 / 5 dof |

**Against Gaia**
- Period: the joint P is 0.00077 d shorter than Gaia's, which is −0.08σ.
- Gaia-predicted conjunctions:
  - A: observed minus predicted is +0.057, +0.034 and +0.021 d, all ≤0.10σ (Gaia σ = 0.56–1.42 d).
  - B: observed minus predicted is −0.19 to −0.22 d, all ≤0.28σ.

**Eccentricity components**
- e cos ω: the B−A phase separation is 0.46594, which gives e cos ω = −0.0535 to first order. Gaia's MC value is −0.035 ± 0.029 (phase separation 0.478 ± 0.018), so they differ by 0.66σ.
- e sin ω: T14 is 7.49 ± 0.03 h for A and 7.94 ± 0.13 h for B, which gives e sin ω ≈ +0.029 ± 0.009 to first order. Gaia's MC value is +0.013 ± 0.032.
- No limb-darkened model was needed: neither eclipse is grazing, since A is flat and annular and B is total. The B T14 is a trapezoid estimate on a 0.3% signal, so treat e sin ω as indicative.

## 4. Independence
- **Other pipelines:** A appears in five pipelines (QLP, SPOC 2-min, TESS-SPOC, TARS, eleanor-lite) and B in four. Depths agree to about 5% across very different apertures, and mid-times agree within about 2 min.
- **Neighbour dilution** (`dilution.txt`): no Gaia source within 60″ can produce A. The brightest, G 14.63 at 42″, would need a 103% intrinsic dip. Just outside 60″, a G 12.44 star at 74.8″ would need 13.7% for A and 1.0% for B. That is ruled out by:
  - the depth staying the same across five pipelines' apertures;
  - the null centroid shift;
  - the timing landing exactly on the Gaia SB1 conjunctions of this star.
- **Not done (time):** no difference image or TESScut per-pixel fit. No other-conjunction upper limit was needed, because both kinds are detected.

## 5. Physics (`physics.txt`)
- **Mass function:** f(M) = 0.01219 M☉.
- **Companion and orbit:** for M1 = 0.95–1.2 M☉, m2(i = 90°) = 0.26–0.30 M☉ and a = 37–39 R☉.
- **Durations:** the predicted central T14 for R1 = 1.3–1.53 R☉ is 7.3–8.7 h. The observed 7.5 h implies b ≈ 0–0.5, and eclipses need i > 87.3°.
- **Depths:**
  - A: k² for an R2 ≈ 0.27 R☉ M dwarf is 3–5%, consistent with the 4.0% depth and the T12/T14 ≈ 0.2 ingress ratio.
  - B: the 0.30% occultation implies a TESS-band surface-brightness ratio of about 0.09, which fits an M3–4 dwarf against a ~5300–5600 K primary. It also explains why Gaia sees only one set of lines.
- **Which star is in front:** at A (ν = 90° − ω) the companion transits the primary; at B the primary occults the companion. Depths, durations, shapes and the companion's light are consistent with one geometry.

## 6. Verdict
**CONFIRMED.** The deciding numbers:
- 3 A and 5 B eclipses across 4 sectors, seen in up to 5 independent pipelines;
- period agreement with Gaia at −0.08σ;
- every event within 0.3σ of its Gaia-predicted conjunction;
- e cos ω within 0.7σ of Gaia's value;
- an M-dwarf companion whose eclipse depths match the mass function.

**Prior art:** none in any catalogue. SPOC raised TCEs at the wrong periods (6.19, 17.11, 39.28 and 277.16 d), and it was never a TOI. ExoFOP was down (HTTP 503), so CTOIs are unchecked.

**Next eclipses** (BTJD, joint ephemeris, about ±2 min):

| A (primary, ~4.1%, 7.5 h) | B (secondary, ~0.3%, ~7.9 h) |
|---|---|
| 4357.8792 | 4345.4235 |
| 4381.2022 | 4368.7464 |
| 4404.5252 | 4392.0694 |
| 4427.8481 | 4415.3924 |

**What would settle it further:**
- an RV follow-up or Gaia DR4 epoch RVs, to get i ≈ 88–90° and absolute masses (this would make a good M-dwarf mass–radius benchmark);
- a TESScut pixel fit or difference image, which I did not do;
- an ExoFOP CTOI check once the service is back.
