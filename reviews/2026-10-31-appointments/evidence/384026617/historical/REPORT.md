> Historical report: superseded by the current reconciliation at ../../../reports/384026617/REPORT.md. Its original bytes are preserved in the source archive; this public copy is sanitized.

# TIC 384026617 (GSC 08594-00924 = TYC 8594-924-1, Gaia DR3 5303449467068766464): adversarial check

Opus checker for Fable 5.1, 2026-10-22 (chunk-3 wave 2). Saved from the checker's final message by Fable 5.1; the file tool refused REPORT.md. Everything else is in this folder, and `progress.md` lists which script produced each number. Downloads are in `[local path omitted]

## Verdict: **CONFIRMED.** A detached, eccentric eclipsing binary with both eclipses seen, on the Gaia SB1 star itself

What decides it:
1. **Both eclipse kinds repeat on one period.**
   - The deep eclipse (A) is seen 9 times in 6 sectors (s9 to s90).
   - A shallow secondary (S) is seen 8 times. The by-eye classifier missed it.
   - The two periods agree over 2,200 d: 30.05387(5) d and 30.05384(13) d.
2. **The pixels put the eclipses on the target and the pulsation on the neighbour.** I fitted every pixel separately in TESScut cutouts of s62 and s89.
   - The light lost in eclipse A centres 0.09 and 0.26 px from the target, and 1.03 and 1.17 px from the 19.6" neighbour.
   - The light lost in eclipse S centres 0.23 and 0.47 px from the target.
   - The δ Scuti pulsation centres 0.21 and 0.31 px from the **neighbour**. That neighbour is Gaia DR3 5303449501428506880 (G 12.24), the VSX "VAR" star. Its catalogued period, 0.1923277 d, equals the strongest frequency in the TESS data (f1 = 5.1995 cycles/day).
3. **Other pipelines agree.**
   - TGLC fits each star's image separately. On the target it removes the pulsation (1.3 ppt, against 16 ppt in QLP) but keeps both eclipses.
   - The SPOC s35 aperture is smaller than QLP's. It cuts the pulsation 2.4x (7.1 against 17.1 ppt), but the eclipse depth stays at 4.72%.
4. **The eclipse geometry fits the Gaia orbit.**
   - Eccentricity from the eclipses is 0.351, against Gaia's 0.368 ± 0.100.
   - e cos ω and e sin ω sit 2.1σ from Gaia's (p = 0.10), using this star's own Gaia covariance.
   - The deep eclipse falls at Gaia's conjunction A: +0.33 d (+0.47σ) when projected back to Gaia's reference epoch. At TESS epochs the offset grows to −1.0 to −1.2σ, entirely because Gaia's period is 1.37σ long.
5. **The physics is self-consistent.**
   - The mass function, f(m) = 0.055 M☉, gives a companion of about 0.75 M☉ for a 2.0 M☉ primary.
   - The fitted companion radius (0.71 R☉) and temperature (about 4900 K) describe a K dwarf of that mass.
   - The fitted primary radius (3.3 R☉) matches the TIC's 3.6 R☉.
   - Predicted durations for central eclipses are 12.45 h and 19.6 h; the observed ones are 12.4 h and 19.4 h.

## 1. Archives and web: what was queried and what came back
- **`cats.py --r 60`**
  - VSX (VizieR TAP): HTTP 503.
  - ASAS-SN: none.
  - SIMBAD: GSC 08594-00924 [SB*]; TYC 8594-924-1 and TYC 8594-924-2 (the second is the WDS component below).
- **VizieR cone searches of 60" (`arch3.py`, the asu-tsv interface, which did work):**
  - 0 rows in Prša+2022, IJspeert+2024, Kostov+2025 t2/t3/t4, Gaia DR3 variability (I/358), ZTF, ATLAS, ASAS-SN, WISE, ASAS-3, Justesen+2021 and Oelkers.
  - Mowlavi+2023 (Gaia eclipsing binaries): only other stars, at 26.8" and 55".
  - SB9: 0 rows.
  - **VSX:** one entry, at 19.57". It is the neighbour, not the target: type VAR, G 12.09–12.39, P 0.1923277 d, Sp F. So it is not prior art for the target, and no type revision is needed (the target has no VSX entry).
  - **WDS 09025-5821 = TDS 6264, at 0.13"** from the target: a 0.6" pair with mags 11.59 and 12.01 (Tycho Double Star catalogue, 1991).
    - Gaia DR3 sees a single source there: RUWE 0.87, ipd_frac_multi_peak 0, ipd_gof_harmonic_amplitude 0.02. The nearest other Gaia source is G 18.99 at 3.6".
    - A real pair with Δm ≈ 0.4 at 0.6" would almost certainly show in those image statistics, so I judge it spurious. That is common for faint TDS pairs.
    - If it were real, both stars sit in the target pixel, and the Gaia SB1 orbit would itself be a blend.
- **Gaia DR3 (`arch2.py`, `arch4.py`)**
  - Target: no entry in vari_summary, vari_eclipsing_binary or vari_classifier; phot_variable_flag NOT_AVAILABLE.
  - Target radial velocities: rv_amplitude_robust 61 km/s over 25 transits, consistent with twice K1 (56 km/s).
  - Neighbour: phot_variable_flag VARIABLE, G range 0.30 mag, Teff 6565 K, logg 3.5, parallax 0.61 mas against the target's 1.05. The two stars are unrelated.
- **SIMBAD references:** only the Gaia DR3 orbit papers (2023A&A...674A..34G, 2018A&A...615A..49C).
- **ExoFOP:** HTTP 503 on three tries, so TOI/CTOI status is **unverified**.
- **Web search** on every name ("TYC 8594-924-1", "GSC 08594-00924", "TIC 384026617", the Gaia ID, "TDS 6264", "J09025-5821"): nothing about this star.
- **MAST CAOM (`archives.py`):**
  - QLP: s9, 10, 35, 37, 62, 63, 64, 89, 90.
  - TGLC, eleanor-lite and T16: s9 and s10.
  - TESS-SPOC: s35.
- **Conclusion:** not catalogued as an eclipsing binary anywhere.

## 2. Eclipse measurements (raw QLP SAP_FLUX, pulsation model subtracted)
**Pulsation model (`freq.py`).** Each sector gets a 25-frequency fit with the eclipses masked. The main terms are:
- f1 = 5.1995 and f2 = 6.7908 cycles/day, about 17 ppt each in the blended light;
- further modes at 10.591, 9.314, 8.575 and 8.497 cycles/day;
- combination terms f1+f2 = 11.990, f2−f1 = 1.5925 and 2f1 = 10.398, which mean all of it comes from one pulsating star.

Subtracting the model cuts the scatter from 19–21 ppt to 3.3–4.7 ppt.

**A (deep) eclipses.** Free trapezoid fits (`ecl.py`) on the six complete events give:

| Quantity | Value |
|---|---|
| Depth | 4.59–4.92% (mean 4.80%) |
| Total duration | 11.5–12.1 h |
| Ingress | 2.0–2.4 h |
| Flat part | 7.2–7.9 h |

The two-sphere model gives a depth of 5.0%, a duration of 12.38 h, and a bottom rounded by limb darkening: the K dwarf transits the A star.

Timing with the eclipse shape held fixed (`eclfix.py`):

| Sector | Mid-time (BTJD) | Error | Depth | Note |
|---|---|---|---|---|
| s9 | 1550.8508 | 2.4 min | 4.58% | |
| s10 | 1580.9024 | 3.9 min | 4.83% | |
| s35 | 2272.1422 | 4.0 min | 5.30% | egress only in unflagged data; SPOC gives 2272.1413 and 4.72% |
| s37 | 2332.2414 | 3.7 min | 4.47% | at the sector end |
| s62 | 2993.4316 | 1.7 min | 4.83% | |
| s63 | 3023.4848 | 3.3 min | 4.83% | |
| s64 | 3053.5468 | 2.9 min | 4.90% | |
| s89 | 3744.7832 | 1.9 min | 4.72% | |
| s90 | 3774.8382 | 4.8 min | 4.30% | at the sector end |

Including the quality-flagged cadences moves the times by 1 min or less, except s35 (+12 min, from scatter in the flagged data) and s37 (+7 min).

Checks through the A events:
- Background is flat in the complete events (changes under 0.6σ).
- No flagged cadence falls inside any of the unflagged-data eclipse windows. The s35 ingress itself is flagged (scattered light).
- The QLP centroid columns shift by 1–8 millipixels in eclipse; the pixel test in section 4 resolves what that means.

**S (shallow) eclipses.** Free trapezoid fits give depth 0.83–1.06%, total duration 17.6–21 h and a flat bottom of about 13 h. The model gives 0.90% and 19.4 h: the K dwarf is completely hidden behind the A star.

Mid-times (BTJD, `eclfix.py`):

| Sector | Mid-time | Error |
|---|---|---|
| s9 | 1560.6170 | 12 min |
| s10 | 1590.6744 | 13 min |
| s37 | 2311.9854 | 14 min |
| s62 | 3003.2038 | 12 min |
| s63 | 3033.2662 | 15 min |
| s64 | 3063.3186 | 17 min |
| s89 | 3724.4940 | 21 min |
| s90 | 3754.5500 | 14 min |

Background is flat through every S event.

**Blind dip search (`census2.py`).** With the pulsation removed, every run of 1 h or more deeper than 0.4% is either an A or S eclipse or a short blip of 0.86% or less. None of the known sector-wide systematic times is involved, and the eclipses line up across six years of sectors.

## 3. Ephemerides and comparison with Gaia
| Kind | P (d) | T0 (BTJD) | Fit quality | Gap to Gaia's P (30.11298 ± 0.04306) |
|---|---|---|---|---|
| A, adopted (6 complete events) | 30.05387 ± 0.00005 | 2903.2730 ± 0.0014 (first event 1550.8489) | χ² 17/4, errors scaled ×2.07, observed-minus-computed scatter ≈ 5 min | 1.37σ |
| A, all 9 events | 30.05389 ± 0.00005 | 2873.2188 ± 0.0012 | χ² 27/7 | 1.37σ |
| S | 30.05384 ± 0.00013 | 2612.5076 ± 0.0035 (first event 1560.6231) | χ² 4.1/6 | 1.37σ |

- **Phase of S after A:** 0.32526 (model 0.32530). Gaia predicts 0.422 ± 0.062, so −1.55σ.
- **Offsets from Gaia's predicted conjunctions** (Monte Carlo with this star's own Gaia covariance; `gaiacmp.py`, `gaiaepoch.py`):
  - A at TESS epochs: −1.9 d (−0.97σ), −4.7 d (−1.19σ) and −6.2 d (−1.23σ).
  - S at TESS epochs: −1.8 to −2.0σ.
  - Projected back to Gaia's reference epoch: A +0.33 d (+0.47σ), S −2.5 d (−1.64σ).
- **e cos ω and e sin ω** from a limb-darkened two-sphere fit to both eclipse kinds in all sectors (`ebfit.py`):
  - e cos ω = −0.2710 ± 0.0005.
  - e sin ω = 0.224 ± 0.008. The range is 0.218–0.229 across third light 0 or 0.21 and two sets of limb-darkening coefficients.
  - e = 0.351, ω = 140.5°, inclination 89.4–90°.
  - Impact parameter 0.12 of the primary radius at A and 0.19 at B. Both eclipses are total or annular, so the flat bottoms are real totality, not an artefact of the trapezoid.
- **Gaia's values:**
  - e cos ω = −0.121 ± 0.092 (we are −1.63σ from it); e sin ω = 0.337 ± 0.096 (−1.18σ); their correlation is −0.11.
  - Combined distance 2.13σ; e agrees within 0.2σ; ω alone is off by +2.25σ.
- **The tension is mild.** Gaia's e sin ω would predict a duration ratio of about 2.0 between the two eclipses; the observed ratio is 1.56.

## 4. Independence, pixels and neighbours
- **Other pipelines (`secondpipe2.py`, `spoc35.py`).** All of these show both eclipses at the QLP times, within a few minutes for A:
  - TGLC (image-fit and aperture), s9 and s10;
  - eleanor-lite, s9 and s10;
  - T16, three apertures, s9 and s10;
  - TESS-SPOC s35 (A only).

  Depths range over 3.3–5.4% for A and 0.4–1.15% for S, depending on how much of the neighbour each aperture or fit takes in. Two patterns point to the target:
  - In T16, a bigger aperture around the target raises the pulsation amplitude and lowers the eclipse depth. That is dilution by the neighbour.
  - TGLC's separate fits put about 58% of the eclipse light on the target but only 10% of the pulsation in s9; in s10 the split is 82% against 49%.

  The known problem of QLP depths running low in s96–s103 does not apply: this star has no data in those sectors.
- **Difference images (`pixtest.py` on TESScut s62 and s89; `pix_s62.png`, `pix_s89.png`).** Each pixel is fitted with a trend, the pulsation pattern and the two eclipse shapes.
  - A deficit: 0.09 and 0.26 px from the target, 1.03 and 1.17 px from the neighbour.
  - S deficit: 0.23 and 0.47 px from the target.
  - Pulsation: 0.21 and 0.31 px from the neighbour.
  - A two-Gaussian split puts 100% and 107% of the A deficit on the target. Its absolute flux ratios are unreliable, because a Gaussian is a poor fit to the star images here.
- **Neighbour dilution (Gaia DR3 stars within 60" brighter than G 15):**

| Star | Separation | Δm | Depth it would need |
|---|---|---|---|
| G 12.24 (the pulsator) | 19.6" | 1.23 | 14.9% for A, 2.9% for S; ruled out by the pixels |
| G 15.18 | 34.2" | 4.17 | 220%, impossible |
| G 15.49 | 55.2" | 4.47 | 290%, impossible |

  Every other star within 60" is fainter than G 15.8. The only possibility the pixels cannot resolve is the doubtful 0.6" TDS companion.

## 5. Physics (`physics.py`)
- **Mass function:** f(m) = 0.055 ± 0.022 M☉ (K1 = 27.8 ± 3.6 km/s, e = 0.351).
- **Companion mass at inclination ≈ 89.5°:**

| Primary mass M1 | Companion mass m2 (range for K1 ±1σ) | Separation a | Primary radius R1 | Companion radius R2 |
|---|---|---|---|---|
| 1.8 M☉ | 0.70 M☉ (0.59–0.82) | 55.2 R☉ | 3.23 R☉ | 0.68 R☉ |
| 2.0 M☉ | 0.75 M☉ (0.63–0.87) | 57.0 R☉ | 3.33 R☉ | 0.71 R☉ |
| 2.2 M☉ | 0.79 M☉ (0.67–0.92) | 58.6 R☉ | 3.43 R☉ | 0.73 R☉ |

  With third light set to 0.21, the companion radius becomes 0.79 R☉. Either way the primary's surface gravity (log g ≈ 3.7) makes it an 8100 K A star that has evolved somewhat off the main sequence.
- **Companion temperature:** the fitted surface-brightness ratio of 0.215 in the TESS band means about 4900 K for an 8100 K primary (blackbody at 0.8 µm). The companion gives about 0.9% of the light. That is a K dwarf, as a 0.75 M☉ companion should be.
- **Which star is in front:**
  - At A (near periastron, separation 0.72a), the K dwarf passes in front of the A star. The depth is set by the radius ratio, 0.21, squared, adjusted for limb darkening.
  - At B (separation 1.13a), the K dwarf is hidden behind the A star. The depth equals its share of the light, 0.9%.
- **Predicted durations for central eclipses:** 12.45 h at A and 19.6 h at B, against measured 12.38 h and 19.38 h. Depths, durations and shapes all fit one geometry and the companion's light.
- **The pulsation:** the δ Scuti-like signal (f1/f2 = 0.766, with combination terms) belongs to the unrelated F-type neighbour, not to the binary.

## 6. Next predicted eclipses (BTJD; uncertainty about 5 min for A and 12 min for S)
| Kind | Times |
|---|---|
| A (deep: 4.8% in the QLP blend, 12.4 h long) | 4345.859, 4375.913, 4405.967, 4436.020 |
| S (shallow: 0.9–1.0%, 19.4 h long) | 4355.631, 4385.684, 4415.738, 4445.792 |

General formula: A = 2903.2730 + 30.05387 E; S = 2612.5076 + 30.05384 E.

## What would settle it further
- **A spectroscopic orbit**, ideally showing the K dwarf's lines in the red. It would pin K1 (Gaia's has a 13% error), the masses through K2, and ω. Gaia's ω is 2.25σ from the eclipse value; we expect ω ≈ 140° and e ≈ 0.35.
- **Speckle or adaptive-optics imaging** to settle whether the 0.6" pair TDS 6264 is real.
- **ExoFOP TOI/CTOI status** once the site is back up (it returned 503 today).
- **A difference image from the SPOC s35 target pixel file**, which exists. I used TESScut only, for s62 and s89.
- **A longer baseline for apsidal motion.** None is seen yet: P_S − P_A = −0.00003 ± 0.00014 d.

## Notes for Fable 5.1
- **Run scripts as `python -X utf8`, not `python -I`.** `-I` drops the user site-packages where astropy is installed. I ran scripts from my own folder instead; the downloaded files are FITS data only.
- **Two ephemeris files.** The live `eclfixA_ephem.json` is the 6-complete-event fit, which `ebfit.py` and the predictions use. Rerunning `ephem.py eclfixA.json` with no exclusions overwrites it with the 9-event fit; the two differ by 0.4σ.
- **Web sources checked** (none mention the star): arXiv 2302.00320, AAS Nova post 940, arXiv 2310.02695.
