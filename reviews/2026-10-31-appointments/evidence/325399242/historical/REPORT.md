> Historical report: superseded by the current reconciliation at ../../../reports/325399242/REPORT.md. Its original bytes are preserved in the source archive; this public copy is sanitized.

# TIC 325399242 (TYC 3969-3710-1, Gaia DR3 1981231859197084544): adversarial check, 2026-10-22

Opus checker for Fable 5.1 (chunk-3 wave 2). Saved from the checker's final message by Fable 5.1; the file tool refused REPORT.md.

**VERDICT: CONFIRMED.** This is a detached eclipsing binary with P = 28.03837 d: a K giant (4751 K, about 4.3 Rsun, about 1.2 Msun) and an M dwarf (about 0.30 Msun, 0.31 Rsun, about 3300 K), with i = 86°.

- **Eclipse A** is a full transit of the giant by the M dwarf: 0.50% deep, T14 15.7 h, b about 0.7. Its bottom is rounded by the giant's limb darkening. It is neither grazing nor a total eclipse of the companion.
- **Eclipse B** is a total occultation of the M dwarf: 0.09% deep and flat. The by-eye classifier did not see it. It was found here at 10σ at phase 0.381.
- **The deciding numbers:**
  - The eclipse period agrees with Gaia's to 0.3σ.
  - Every event sits within 1σ of its Gaia conjunction (A −0.3 to −0.5σ, B +0.6 to +0.8σ).
  - The depth, duration and surface-brightness ratio give one consistent geometry, and it reproduces Gaia's mass function with the TIC radius.
  - TARS reproduces A, and the A eclipse is on the target pixel.
- **Prior art:** no catalogue lists it as a variable or an eclipsing binary. Its only prior status is Gaia's SB1 orbit.

## 1. Archives (2026-10-22)

- **`cats.py --r 60`:** the VSX TAP query failed with HTTP 503. ASAS-SN has nothing. SIMBAD has TYC 3969-3710-1 as type SB* at 0".
- **VizieR 60" cones (`arch3.py`), 0 rows in:** Prša+2022, IJspeert+2024, Kostov+2025 t2/t3/t4, VSX (this cone worked), SB9, WDS, ZTF periodic, ASAS-SN II/366, WISE, ACVS, KELT, Justesen+2021 and the TESS OBA EBs.
  - ATLAS lists only two neighbours, at 38" and 56".
  - The J/A+A/674/A16 cone hit a Gaia source table of neighbours and is irrelevant.
- **Gaia DR3 variability tables:** vari_classifier_result, vari_summary, vari_eclipsing_binary, vari_rotation_modulation and vari_long_period_variable are all empty. phot_variable_flag is NOT_AVAILABLE.
- **Gaia NSS solution (SB1):**
  - P 28.03673 ± 0.00510 d, e 0.2310 ± 0.0196, ω 196.42 ± 4.07°, K1 16.31 ± 0.48 km/s.
  - t_periastron is 8.7476 ± 0.3657 d after J2016.0, i.e. BTJD 397.748.
  - Significance 33.7, RUWE 0.90.
- **SIMBAD identifiers:** TIC, Gaia DR1/DR2/DR3, TYC and 2MASS J22033500+5308531. Its only reference is the Gaia DR3 NSS paper (2023A&A...674A..34G).
- **ZTF (IRSA):** 0 rows; the star is probably saturated.
- **ExoFOP:** HTTP 503 on two tries, so TOI/CTOI status is unverified. The web searches found no TOI either.
- **MAST (CAOM, 10"):** only QLP and TARS light curves, for sectors 16, 17, 56, 57, 76, 77, 83 and 84. There is no SPOC, TESS-SPOC or TGLC light curve and no target pixel file.
- **Web searches** on "TYC 3969-3710-1", "TIC 325399242" and "2MASS J22033500+5308531": nothing about this star.

## 2. Eclipses (QLP SAP_FLUX, untrimmed; QUALITY==0 unless noted)

**A-kind eclipses** (`eclfix.py`: fixed trapezoid shape, prayer-bead errors; `ecl.py`: free trapezoid):

| sector | t0 (BTJD) | error | depth | free T14 / T12 | notes |
|---|---|---|---|---|---|
| s017 | 1764.9931 | 9 min | 0.45% | | 2019, 30-min cadence; all cadences flagged, egress only |
| s056 | 2830.4512 | 5 min | 0.50% | 16.8 / 4.3 h | |
| s057 | 2858.5020 | 5 min | 0.54% | 14.6 / 1.5 h | 15 flagged cadences on egress; the all-cadence fit is the same |
| s076 | 3391.2173 | 6 min | 0.50% | 16.7 / 3.4 h | |
| s077 | 3419.2612 | 7 min | 0.49% | 15.4 / 2.3 h | |
| s083 | 3559.4668 | 6 min | 0.52% | | egress only, at the sector start |
| s084 | 3587.4865 | 4 min | 0.50% | 15.6 / 2.4 h | |

- The weighted QLP depth is 0.496 ± 0.007%, with a scatter of 0.018%.
- The by-eye "12 h" was the FWHM. The total duration is about 15.7 h.
- **Background** (SAP_BKG, e-/s), in-eclipse minus out: −36 ± 8, +12 ± 5, +46 ± 28, −19 ± 12 and −11 ± 26. There is no common sign, and the scattered-light structure in these sectors is 10³ e-/s.
- **Centroids:** the QLP SAP_X/Y shifts are at most 0.9 mpx.
- **Systematics:** no A or B event falls on the known common-mode list.

**B-kind eclipses:**

- **Phase scan** (`bsearch.py`, fixed shape, all phases): the only significant feature in the orbit is at phase 0.380, 835 ± 81 ppm, S/N 10.3. Elsewhere the maximum is 226 ppm (S/N 3.3) and the robust scatter is 76 ppm.
- **Every event contributes:** s056 775 ± 163, s057 699 ± 234, s076 902 ± 208, s077 977 ± 180, s083 661 ± 174 and s084 1300 ± 322 ppm. The s084 event sits on a rising-background edge.
- **Free trapezoids:** 0.076–0.104% deep, T14 12–15 h, ingress under 1.2 h, flat bottom.
- **Background:** clean in s056 (−1 ± 6), s057 (+9 ± 6) and s083 (−10 ± 5). The s076, s077 and s084 events sit on scattered-light slopes.
- **Timing:** single-event B times are only good to 18–51 min, so B timing comes from the joint model in section 3.

**Census** (`census.py`, 12-h box, every sector):

- Above 0.2%: exactly the five complete A events (S/N 11–14).
- Above 0.06% with S/N of 4 or more, excluding A:
  - Four B events: s056, s057, s077 and s084.
  - Four other hits, all at gap edges or ramps: s017 1768.9 and 1786.1, s056 2838.9 and s083 3572.2.
  - The s017 B event at 1775.5 is on a scattered-light ramp.

## 3. Ephemerides and orbit

- **A** (7 events, χ² 23/5, errors scaled by 2.16): T0 = 2830.45608 ± 0.00394 BTJD, P = 28.038374 ± 0.000191 d.
  - The O−C rms is about 9 min, set by red noise from the giant.
  - The five complete events alone give P = 28.038086 ± 0.000217 d.
  - Against Gaia's 28.03673 ± 0.00510 d, the difference is +0.3σ.
- **B:** T0 = 2841.1381 ± 0.012 BTJD with the same P. The B−A offset of 10.682 d is phase 0.3810, from the joint model.
- **Against Gaia's conjunctions** (`conjmc.py`, using this star's own covariance):

  | kind | observed (BTJD) | Gaia predicted | offset | σ |
  |---|---|---|---|---|
  | A | 2830.451 | 2830.711 ± 0.493 | −0.26 d | −0.5 |
  | A | 2858.502 | 2858.747 ± 0.498 | −0.25 d | −0.5 |
  | A | 3391.217 | 3391.445 ± 0.587 | −0.23 d | −0.4 |
  | A | 3419.261 | 3419.482 ± 0.592 | −0.22 d | −0.4 |
  | A | 3559.467 | 3559.665 ± 0.616 | −0.20 d | −0.3 |
  | A | 3587.487 | 3587.702 ± 0.621 | −0.22 d | −0.3 |
  | A | 1764.993 (s017) | 1765.315 ± 0.328 | −0.32 d | −1.0 |
  | B | 2841.138 | 2840.812 ± 0.428 | +0.33 d | +0.8 |
  | B | 3401.88 | 3401.546 ± 0.525 | +0.33 d | +0.6 |
  | B | 3598.15 | 3597.803 ± 0.559 | +0.35 d | +0.6 |

  The B−A phase is 0.3810 observed against Gaia's 0.3602 ± 0.0107, a +1.9σ difference.

- **Two-sphere limb-darkened model** (`ebfit.py`, own code; P fixed; 6 A + 6 B events in 10-min bins):

  | U1 (giant) | e cos ω | e sin ω | i | R1/a | R2/a | k | J | L2/L1 |
  |---|---|---|---|---|---|---|---|---|
  | 0.60 | −0.1872 | +0.061 | 85.8° | 0.0963 | 0.00693 | 0.072 | 0.186 | 0.0010 |
  | 0.50 | −0.1878 | −0.010 | 86.3° | 0.0901 | | | | |
  | 0.70 | −0.1876 | −0.016 | 86.1° | 0.0938 | | | | |

  Model eclipses:

  | eclipse | T14 | T23 | depth | b/R1 | in front |
  |---|---|---|---|---|---|
  | A | 15.6–16.1 h | 11.8–12.0 h | 0.53–0.55% | 0.68–0.71 | companion |
  | B | 15.6–16.0 h | 11.1–12.1 h | 0.098–0.100% | | giant |

- **Convention:** the model's ω is Gaia's primary ω, because the two axis flips cancel. The `vet356308234/ebfit2.py` docstring says "w + 180", which is wrong, though their numerical comparison was done correctly. Other folders that copied that script carry the same misleading comment.
- **e cos ω** = −0.1876 ± 0.001 against Gaia's −0.2209 ± 0.0170: a 2.0σ difference, and the only mild tension.
- **e sin ω** is only weakly constrained by the eclipses, as the brief warns:
  - The free fits move between −0.016 and +0.061 depending on limb darkening.
  - A fixed-e sin ω profile is flat: the white-noise Δχ² is 3.4 or less from −0.09 to +0.13, and 9.7 at −0.15. The residuals are red, so the true range is wider.
  - Gaia's −0.065 ± 0.019 sits at Δχ² about 1.8, so it is consistent.
  - Reading the trapezoid flats as T23 would invent a constraint here. The A eclipse is a limb-darkened transit at b about 0.7, not a box.
- **Durations** predicted with Gaia's e and ω at the fitted b: A 16.1 h (model 15.7), B 15.7 h (model 16.0).

## 4. Independence

- **TARS, A eclipse:** depths 0.48–0.54%, weighted 0.507 ± 0.009%, against QLP 0.496 ± 0.007%. The five A times agree with QLP within 0–15 min, on errors of about 5 min each.
- **TARS, B eclipse:**
  - Depth at fixed phase is 0.059 ± 0.008%, against QLP 0.090 ± 0.006%. The clean-sector events agree (s056 0.080 vs 0.094%, s057 0.084 vs 0.079%); TARS is lower in the scattered-light sectors.
  - A TARS phase scan puts the global maximum at 0.382 (570 ± 85 ppm). A bump at phase 0.165 is nearly as high (S/N 4.4), so TARS supports B but does not establish it alone.
  - None of these sectors is among the known low-depth QLP sectors (s96–s103).
- **TESScut difference images** (s056, s057 and s084, at A):
  - The deficit peaks on the target pixel, with depths there of 0.6%, 0.5% and 0.4%.
  - The deficit's share inside the 3×3 box (0.73, 0.75, 0.83) matches the light's share (0.75, 0.72, 0.73).
  - The deficit-vs-light offsets are 3–6" and point away from the 13.2" neighbour.
- **Cutout centroids at A** (`centroid.py`):
  - The in-minus-out shifts are (−0.2, +0.3), (+0.5, +0.4) and (+1.3, +0.8) mpx, each ± 0.15–0.23.
  - If the eclipse were on the G 14.88 star at 13.2", the shifts would be (−3.9, −1.2), (−3.9, −0.1) and (−2.8, +0.1) mpx.
  - The target hypothesis itself misses by about 1 mpx, which sets a systematic floor. Even so, the neighbour is disfavoured at about 3–4σ in each of the three sectors.
- **Neighbours within 60" brighter than G 16** (depth each would need = our depth × 10^(0.4 Δm)):

  | neighbour | separation | needed at A | needed at B |
  |---|---|---|---|
  | G 14.88 | 13.2" | 16.3% | 2.9% |
  | G 15.13 | 44.7" | 20.5% | 3.7% |
  | G 15.44 | 57.8" | 27% | 4.9% |
  | G 15.91 | 51.7" | 42% | 7.6% |

  The G 14.28 star at 62.3" would need 9.4% / 1.7%, and its pixel shows no deficit.
- **Most decisive:** both eclipse kinds fall at the target's own Gaia SB1 conjunctions, with the target's period, and their durations match the giant's radius. A blended background eclipsing binary cannot reproduce that.

## 5. Physics

- **Mass function** f(m) = 0.0116 ± 0.0011 Msun. At i = 86°:

  | M1 (Msun) | m2 (Msun) | a (Rsun) |
  |---|---|---|
  | 1.0 | 0.27 | 42 |
  | 1.3 | 0.31 | 45.5 |
  | 1.6 | 0.36 | 48.6 |
  | 2.0 | 0.41 | 52 |

- **Masses and radii:** the TIC radius (4.29 Rsun) with the eclipse R1/a of 0.096 gives a = 44.5 Rsun and M1 + m2 = 1.51 Msun.
  - Solving with the mass function gives M1 = 1.21 Msun, m2 = 0.30 Msun, R2 = k·R1 = 0.31 Rsun and logg1 about 3.25.
  - A 0.30 Msun M dwarf has a radius of about 0.3 Rsun, so mass, radius and mass function agree with each other.
- **Companion temperature:** the surface-brightness ratio J = 0.186 gives T2 of about 3300 K (blackbody, TESS band; T1 from 4600 to 4900 K gives 3230–3380 K). That fits an M3–4 dwarf, and L2/L1 = 0.0010 equals the B depth.
- **Geometry:**
  - At A (ν = 254°) the M dwarf crosses the giant. The A depth matches k² × the limb-darkening factor: 0.0052 × 1.04.
  - At B (ν = 74°) the giant totally occults the M dwarf.
  - The stars are closer at B (r/a 0.89 vs 1.01), which gives the smaller b at B.
  - Depth, duration, shape and the companion's light all fit one geometry.

## 6. Next eclipses (BTJD)

- **A** (transit, 0.50%, 15.7 h): 4344.5150, 4372.5531, 4400.5911, 4428.6292, 4456.6673 (± 14 min).
- **B** (occultation, 0.09%, about 16 h): 4355.1970, 4383.2351, 4411.2731, 4439.3112, 4467.3493 (± 22 min).

## What would settle it further

- **Orbit:** an RV orbit, or a higher-S/N B eclipse from more sectors, to bound e sin ω and resolve the 2σ e cos ω offset from Gaia.
- **Spectroscopy:** SB2 or high-resolution spectra to detect the M dwarf (predicted K2 about 68 km/s) and give absolute masses for an evolved-star benchmark.
- **ExoFOP:** retry the TOI/CTOI query, which returned 503.
- **Pixel data:** a SPOC or TGLC light curve, or a PRF-fit difference image, would rule out the 13" neighbour completely. The timing argument already excludes it.
- **Asteroseismology:** red-giant oscillations in TESS (numax near 300 µHz for logg 3.25) would give an independent M1 and R1.

Everything is in `[local path omitted] 5.1\made\appointments\vet325399242\`; `progress.md` lists which script made which output. Downloads (TARS light curves and TESScut cutouts for s056, s057 and s084) are in `[local path omitted] Nothing was committed and nothing outside those two folders was edited.

Web searches on the star's names returned nothing about it (hits were arXiv 1801.00671 and var.astro.cz star 94236, both other stars).
