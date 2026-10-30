# TIC 348536911 (TYC 5995-1398-1, Gaia DR3 5721091468448223488): per-object vet

Opus subagent, 2026-10-21, following VET-BRIEF and BRIEF-ADAPT. The data is raw QLP SAP_FLUX, QUALITY==0, no trimming, unless stated otherwise. The parent saved this file because the write tool refused it for the subagent.

## Verdict: CONFIRMED. The target eclipses: a grazing, circular eclipsing SB1 (a G subgiant with an early M dwarf), with both eclipse kinds seen.

Deciding numbers:
- **Primary eclipses:** 36 events in 4 sectors (s007, s034, s061, s088).
  - QLP depth 28.2 ppt, T14 3.36 h, T12/T14 0.40.
  - Odd and even depths are equal: 28.24 ± 0.07 vs 28.15 ± 0.07 ppt.
- **Secondary eclipse:** 3.84 ± 0.07 ppt (S/N 58) at phase **0.49993 ± 0.00045**.
  - Twelve control phases give ≤ 0.57 ppt.
  - It is seen in every pipeline and every sector.
- **Period:** P = 2.553938 ± 0.000005 d. Gaia gives 2.554066 ± 0.000037 d, so TESS is −3.4σ shorter.
- **Timing against Gaia:** the primary falls on Gaia conjunction A, meaning the RV primary is the star eclipsed.
  - At the TESS sectors the offset is +0.1σ to +2.4σ; at the Gaia epoch it is −1.28 h (−3.9σ).
  - All of that offset comes from Gaia's e cos ω. Restricted to circular draws, A lands −0.30 h (−2.0σ) from the TESS primary and B lands −0.24 h (−1.6σ) from the TESS secondary.
  - TESS gives e cos ω = −0.0001 ± 0.0007, against Gaia's +0.051 ± 0.015 (3.5σ). This is a seventh small-e Gaia orbit failing in the circular direction.
- **On target, despite a G 11.44 star 9.6″ away.** That star is WDS ARA 52 and is not bound to the target.
  - Test: in the TESS-SPOC pixel data, the fractional flux loss per pixel was measured along the line from the target to the neighbour.
  - It falls toward the neighbour in all 3 sectors, for both eclipse kinds.
  - Primary: −2.9 ± 0.2, −5.9 ± 0.6 and −4.1 ± 0.7 ppt/px. Secondary: −0.6 ± 0.3, −1.4 ± 0.4 and −1.3 ± 0.5 ppt/px.
  - A target eclipse predicts about −4.3 ppt/px; a neighbour eclipse predicts about +12.
- **Physics:** a limb-darkened two-sphere fit gives R1 = 2.12 R☉ (TIC 2.07 ± 0.10), R2 ≈ 0.63 R☉, b ≈ 1.04, i ≈ 76°.
  - Gaia's f(M) = 0.0513 M☉ then gives m2 ≈ 0.51–0.53 M☉.
  - The predicted ellipsoidal amplitude is 6.9 ppt; the observed 3.8–6.3 ppt is contaminated by starspots.
  - The secondary depth fits an M dwarf at T2 ≈ 3400–3500 K.

**Row fixes:**

| | batch row | corrected |
|---|---|---|
| P (d) | 2.55395 | **2.553938 ± 0.000005** |
| depth (ppt) | 26.2 | **28.2**, fixed-shape fit; sector means 28.6 / 29.0 / 28.3 / 27.7 |
| events | 27 | **36**, adding s007 (30-min cadence), which the batch lacked |
| T14 (h) | 1.9 | **3.36** |
| dphi | | secondary at phase **0.49993 ± 0.00045**; Gaia A − TESS primary = −0.021 ± 0.006 phase at the Gaia epoch (−0.005 if circular) |
| diffimg | 2.75″ | stands: its deficit−light 2.62″ matches the 2.47″ a target eclipse predicts (a neighbour eclipse predicts 7.1″) |

## 1. Archives
- **cats.py --r 60** (`cats-out.txt`, with APPOINTMENTS_DATA set):
  - No hits in VSX, ASAS-SN, Prša+2022, IJspeert+2024, or Kostov t2/t3/t4. There is not even a Kostov table2 flag.
  - SIMBAD has TYC 5995-1398-1, typed [SB*].
- **Gaia DR3** (`gaiatap-out.txt`, `gaia.json`):
  - vari_summary and vari_eclipsing_binary are empty.
  - NSS solution: SB1, significance 46, flags 0. P 2.5540664 ± 0.0000374, e 0.054 ± 0.015, ω 15.4 ± 12.9°, Tp −1.146 ± 0.092, K1 57.88 ± 1.25 km/s.
  - RUWE 1.03.
- **SB9 and J/AJ/160/111:** no entry.
- **WDS** (`morecats-out.txt`): 08066−1645 is ARA 52, a 9.6–9.8″ pair first measured in 1903, PA 264° to 261°, mags 10.79 and 11.90.
  - The companion is Gaia 5721091365369010176 = TIC 348536909.
  - It is an optical pair (`pair-out.txt`): parallax 0.717 against 3.191 mas, different proper motion, RV +47 against −9 km/s, and Teff 7640 K.
- **ExoFOP:** returned HTTP 503 and was not checked. The batch sweep found no TOI or CTOI.
- **Extra VizieR cones at 30″** (`extracats-out.txt`; control cones returned rows):
  - The only hit is an ATLAS "dubious" variable at 23.5″ with G about 17. It would need a dip deeper than 100%, so it is irrelevant.
  - J/A+A/674/A16 is not an EB table.
- **Web search:** "TIC 348536911" and "TYC 5995-1398-1" returned nothing relevant.
- **Batch receipts:**
  - c3-vetsum: dphi −0.002/+0.465, ATTR.
  - c3-sapdepth: 27 events, median 26.19 ppt. Its box estimator underestimates the depth.
  - diffrun s088: peak on target, deficit−target 2.75″, deficit−light 2.62″.
- **No prior art as an eclipsing binary.** This is a new eclipsing binary in a known SB1.

## 2. Measurements (`vet-out.txt`, `sec2-out.txt`, `census-out.txt`)
- **Primary shape:** the fold of the 200-s sectors gives 27.9 ppt, T14 3.36 h, T12/T14 0.40.
  - Each event was fitted with that fixed shape on a quadratic baseline within ±0.4 d, supersampled for the 30-min sector.
  - Depth constancy χ² is 118/35. The ~1 ppt sector-to-sector steps come from QLP's reference flux, dilution and spots.
- **Background:** the unit-free regression gives ≤ 0.32 ppt per event.
- **Centroids:** in-eclipse shifts are 0–2 mpix.
- **Quality flags:** no event touches a bit-32 cadence, and none sits at a listed sector-wide systematic time.
  - Three events have no Q==0 points in eclipse (2242.55, 2247.66, 2975.53) and were skipped.
- **Out-of-eclipse light** (`timeseries.png`, `look.png`): a ±10 ppt modulation, combining the ellipsoidal effect with large spot humps.
  - The humps migrate in phase from sector to sector, like a synchronised active star of the RS CVn type.
  - A beaming tie is therefore not possible: the expected ~0.6 ppt is swamped.
  - `sec.py`'s global harmonic model fails on this light curve. `sec2.py` supersedes it.
- **Secondary:**
  - Local fixed-shape fits give 3.84 ± 0.07 ppt at phase 0.4990 (fold) and 0.49993 ± 0.00045 (sector-weighted).
  - Controls at phases 0.15–0.85 are ≤ 0.57 ppt; the largest, at 0.40 and 0.60, is leakage from the V-shaped minimum.
  - The fitted secondary T14 of 1.44 h is not physical. The shallow eclipse sits in a V-shaped ellipsoidal minimum, and the quadratic baseline absorbs its wings.
  - A grazing circular orbit has equal chords at both eclipses, so **no e sin ω is derived from durations**.
- **Eclipse timing variations (ETV):** sector-mean primary O−C is −6.5, +4.2, +1.3 and −1.3 min (χ²/dof 1549/34).
  - TESS-SPOC, TGLC and TARS reproduce it (−6.3, +4.0, +1.2, −1.2 min), so it is astrophysical, not a QLP artefact.
  - O−C correlates with the local baseline slope at r = −0.84. After correcting for slope the sector means are −0.4, +2.3, +2.3 and +1.8 min, so the shifts are spot-induced.
  - Secondary minus primary per sector is −3.7, −2.9, +4.7 and +1.0 min (± 2–3). That is not significantly anti-correlated, so there is no apsidal-motion or light-travel-time claim.
  - The period error is inflated to 5 × 10⁻⁶ d because of this.
- **Blind census:** every dip over 6 ppt is a primary or a secondary, except four of 6–10 ppt.
  - Those four sit at phase 0.89–0.93 or 0.11, about 0.27 d from a primary. They are artefacts of the fitting window's edge.
  - No unexplained dips remain.

## 3. Ephemeris and Gaia (`conj-out.txt`, `conjcirc-out.txt`)
The Monte Carlo uses this star's own corr_vec (ω–Tp correlation 0.999).
- **Primary ephemeris:** T0 = 2998.52091 ± 0.00035 BTJD, P = 2.5539380 ± 0.0000050 d (formal error 0.0000012).
- **Secondary phase:** 0.49993 ± 0.00045, against Gaia's (B−A)/P = 0.532 ± 0.009 (−3.5σ). That gives e cos ω = −0.0001 ± 0.0007.
- **Gaia A minus the TESS primary:**

  | epoch | Gaia A − TESS primary |
  |---|---|
  | Gaia epoch | −1.28 h (−3.9σ) |
  | s007 | +0.06 h |
  | s034 | +0.94 h |
  | s061 | +1.83 h |
  | s088 | +2.70 h (+2.4σ) |

  The drift across the sectors is Gaia's period running 3.4σ long.
- **Gaia B minus the TESS secondary:** +0.70 h at the Gaia epoch, and +2.1 to +4.7 h in the sectors.
- **Conditioned on e cos ω ≈ 0:** A is −0.30 h and B is −0.24 h from the TESS events at the Gaia epoch.
- **Attribution:** the primary is conjunction A, unambiguously; the other assignment would be off by P/2.

## 4. Independence (`indep-out.txt`, `tpf2-out.txt`)
- **Second pipelines (primary depth):**

  | pipeline | sectors | primary depth (ppt) |
  |---|---|---|
  | TESS-SPOC PDCSAP | s007 / s034 / s061 | 28.4 / 28.3 / 27.8 |
  | TESS-SPOC SAP (diluted; crowding correction ~0.72) | same | 20.2–20.4 |
  | TGLC PSF | s007 | 28.5 |
  | TARS | all four | 20.8–24.3 |
  | eleanor-lite | s007 | 18.2 |

  The secondary appears in all of them at 2.6–4.9 ppt.
- **The neighbour's own light curves** (TIC 348536909): QLP shows 81–83 ppt and TGLC PSF shows 64 ppt. This is **not** evidence against the target.
  - QLP measures flux on difference images and adds back each star's catalogue flux.
  - So a target eclipse seen in the overlapping neighbour aperture gets divided by a reference flux 0.347 times smaller.
  - The observed ratio 83/28 = 2.96 matches 1/0.347 = 2.88, and either hypothesis predicts that.
  - Likewise, TGLC's PSF fit cannot split a pair 0.46 px apart.
- **TESS-SPOC TPF difference images** (s007, s034, s061; both eclipse kinds):
  - The PSF-free sign test (D/O gradient along target→neighbour) is negative in all 6 cases, matching a target eclipse in sign and size.
  - Deficit-minus-light offset along target→neighbour, where the target predicts −0.12 px and the neighbour predicts +0.34 px:

    | eclipse | s007 | s034 | s061 |
    |---|---|---|---|
    | primary (px) | +0.13 | −0.02 | −0.04 |
    | secondary (px) | −0.14 | −0.10 | −0.21 |

    Five of six favour the target. s007 is ambiguous at 30-min cadence.
  - Two-Gaussian fits are degenerate at this separation (negative flux ratios) and are disregarded.
- **Dilution:** if the G 11.44 neighbour were the eclipser, it would need an ~81 ppt dip of its own. It would also have to share the target's Gaia SB1 period and conjunction phase by chance.
  - The next-brightest star within 60″ is G 14.36 at 54″. It would need about 1000 ppt.

## 5. Physics (`physics-out.txt`)
- **Mass function and orbit:** f(M) = 0.0513 M☉. With M1 = 1.09 M☉: m2(90°) = 0.51 M☉, q = 0.47, a = 9.20 R☉.
- **Primary eclipse fit:** quadratic limb darkening and no dilution, since QLP's reference flux leaves the depth essentially undiluted.
  - Result: R1/a = 0.23, k = 0.30, b = 1.04.
  - So R1 = 2.12 R☉, which matches TIC (2.07, log g 3.84, a subgiant).
  - R2 ≈ 0.63 R☉ and i ≈ 76°, giving m2 ≈ 0.53 M☉.
  - R2 runs about 20% large for that mass. The grazing geometry, the coarse grid and spots allow that; the grid was resolution-limited, so no formal ranges are given.
- **Eclipse geometry:** at A the M dwarf transits the G star. At B about 39% of the M dwarf is occulted.
- **Secondary:** 3.84 ppt means L2/L1 ≥ 9.8 ppt and a surface-brightness ratio of 0.108, i.e. T2 ≈ 3450 K. That is slightly cool for 0.53 M☉ but within the approximations.
- **Ellipsoidal:** 6.9 ppt predicted against 3.8–6.3 ppt observed. Consistent.
- **Not a heartbeat:** the orbit is circular, and both eclipses are sharp and at fixed phases.

## 6. Next predicted eclipse times (BTJD)
- **Primary** (M dwarf transits, conjunction A): **4336.7844, 4339.3384, 4341.8923**, then every 2.553938 d.
  - The ephemeris gives ±4 min; spot jitter adds up to ±6 min.
- **Secondary** (M dwarf occulted, conjunction B): **4338.0612, 4340.6152, 4343.1691** (± 5 min).

## What would settle it further
- **Radial velocities**, ideally red or infrared so the secondary's lines show. These would give the true K1 and e and resolve the two Gaia tensions (P at 3.4σ, e cos ω at 3.5σ).
- **A spot-aware timing fit** would turn the O−C into a real ETV test.
- **ExoFOP**, once the service is back.
- **Third light:** the 9.6″ pair is already resolved, so imaging would only help to bound unresolved light closer in.

## Files
- **Scripts:** vet.py, vetlib.py (copied from vet423927429), sec.py (superseded), sec2.py, look.py, conj.py, conjcirc.py, gaiatap.py, morecats.py, extracats.py, mastlc.py, indep.py, tpf2.py, physics.py, census.py.
- **Outputs:** vet-out.txt, vet-results.json, sec2-out.txt, sec2-results.json, conj-out.txt, conjcirc-out.txt, indep-out.txt, tpf2-out.txt, physics-out.txt, census-out.txt, cats-out.txt, gaiatap-out.txt, morecats-out.txt, extracats-out.txt, pair-out.txt, mastlc-*.txt.
- **Figures:** fold_oc.png, sec2.png, look.png, timeseries.png.
- **Data:** `C:\Home\sky\data\qlp-sb-p20-60\pervet348536911\`, with the neighbour's files in `nbr\`.
