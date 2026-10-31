> Historical report: superseded by the current reconciliation at ../../../reports/112232265/REPORT.md. Its original bytes are preserved in the source archive; this public copy is sanitized.

# TIC 112232265 (TYC 7108-2386-1): adversarial check

Gaia DR3 SB1, P 28.40535 ± 0.00789 d, e 0.4460 ± 0.0200, ω 211.22 ± 2.31°, K1 36.54 km/s; RUWE 3.51. G 11.44, Teff 6026 K, R 2.58 R☉ (TIC). Checked by an Opus checker for Fable 5.1, 2026-10-22 (chunk-3 wave 3, 18:50–19:01). Saved from the checker's final message by Fable 5.1; the file tool refused REPORT.md. Scripts and outputs are in this folder (plots in `w\`), the step-by-step record in `progress.md`; downloads in `[local path omitted] The earlier stopped checker's outputs (archives2.json, arch2/arch3.txt, gaia.json) were overwritten by reruns.

## Verdict: CONFIRMED

The eclipse is on the target star, not on a neighbour. It repeats at the period Gaia gives, and two eclipses that nobody had looked at turned up at the times the ephemeris predicted, within a minute.

## 1. Archives

**Gaia DR3** (TAP, `arch2.py`, `gaia_q.py`, `arch3.py`):
- The orbit row is an SB1 with P 28.40535 ± 0.00789 d, e 0.4460 ± 0.0200, ω 211.22 ± 2.31°, T_peri 2.3608 ± 0.1546 (BTJD 391.36) and K1 36.54 km/s. It has a 15-element corr_vec, which I used.
- RUWE is 3.51, ipd_frac_multi_peak is 2 and rv_amplitude_robust is 74.6 km/s.
- G 11.44, BP−RP 0.90, parallax 1.85 mas.
- The variability tables (vari_summary, vari_classifier_result, vari_eclipsing_binary, rotation, long-period) have nothing for this star.

**VizieR** (TAP worked tonight, plus the asu-tsv cone interface, 60″):
- VSX has no entry at the target. It has two neighbours:
  - Gaia DR3 5592591334052411648, type E, P 1.12255 d, G 18.14, at 29″.
  - Gaia DR3 5592591166557257984, type DSCT|GDOR|SXPHE, G 9.78, at 55″.
- Prša+2022, IJspeert+2024, Kostov+2025 (tables 2, 3 and 4), the ZTF, ATLAS, ASAS-SN, WISE and ASAS variable catalogues, SB9 and WDS all have 0 rows.
- The Gaia DR3 EB catalogue (Mowlavi+2023) has one source in the cone: G 16.17 at 40.7″. Not the target.

**Other sources:**
- SIMBAD lists the star as SB* with one reference, 2023A&A...674A..34G (the Gaia orbit paper).
- `cats.py`: VSX has only the two neighbours above, ASAS-SN has nothing, and SIMBAD has the SB* entry.
- The NASA Exoplanet Archive TOI table has no rows.
- **ExoFOP returned HTTP 503**, so CTOIs are unchecked.
- A web search on "TYC 7108-2386-1" and on the TIC and Gaia ids found nothing.

**Prior art:** none. The star is known only as a Gaia spectroscopic binary.

## 2. Every eclipse measured

**Light-curve noise.** The QLP light curve scatters by 8–9 ppt. Most of that is the G 9.8 δ Scuti star 55″ away (2.7 pixels) leaking into QLP's aperture. My own 3×3-pixel photometry on TESScut cutouts (`tcphot.py`) brings the scatter down to 1.6–2.8 ppt.

**Extra sectors.** MAST holds full-frame images for sectors 87, 108 and 109, which are not in the QLP set. They add two eclipses at times predicted in advance.

Eclipses at conjunction B, trapezoid plus quadratic baseline fitted to quality-0 data; errors from cyclic residual shifts (`tcfit.py`, `fitecl.py`):

| Sector | Mid-time, my TESScut photometry (BTJD) | Mid-time, QLP SAP | Depth (3×3 / QLP) | T14 (h) | Notes |
|---|---|---|---|---|---|
| 7 | 1501.2978 ± 0.0018 | 1501.2956 ± 0.0053 | 2.16% / 3.20% | 6.5 | V-shaped |
| 34 | 2239.8230 ± 0.0060 | 2239.8182 ± 0.0071 | 1.30% / 3.04% | 4.9 | noisy, short flat bottom |
| 61 | 2978.3641 ± 0.0014 | 2978.3567 ± 0.0056 | 1.89% / 3.66% | 6.6 | V-shaped |
| **87 (new)** | 3688.4935 ± 0.0023 | not in QLP | 1.73% | 6.4 | |
| 88 | 3716.9002 ± 0.0024 | 3716.9023 ± 0.0109 | 2.28% / 3.67% | 6.7 | QLP flags 53 of 125 cadences in the eclipse and it sits on a background ramp; clean in TESScut |
| **108 (new)** | 4313.4066 ± 0.0022 | not in QLP | 1.79% | 5.6 | |

- **Shape:** the ingress takes up most of the event and the flat bottom is under about 2 h. A grazing eclipse would look like this.
- **Depth:** it depends on how much of the δ Scuti star's light the aperture includes:
  - SPOC's crowding-corrected PDCSAP gives 3.0–3.6%, which I take as the best intrinsic value.
  - My 3×3 aperture gives about 1.9%.
  - The QLP depths are larger than either. That probably comes from QLP's background estimate.
- **Background:** in sectors 34, 61 and 88 the in-eclipse background excursion is −44 ± 17, +4 ± 5 and −66 ± 11 e⁻/s against out-of-eclipse scatter of 55–120 e⁻/s. In sector 88 that "excursion" is the steep ramp left over after a quadratic fit. Sector 7 has a background spike near 1501.2 but none inside the eclipse.
- **Centroids:** QLP's centroids shift by about +0.0036 px in x and −0.0037 px in y during eclipse (10–17σ). Section 4 settles where that comes from.
- **Blind dip census** (6-h box, every sector, dips above 0.5%; `step3.py`): only the six B eclipses turn up. Everything else is at a data gap or orbit edge (s61 at 2975.5 and 2976.4; s88 at 3696.9 and 3711.6) or is scattered light at the s87 orbit starts (3664–3666, 3676–3680). Sector 109 is clean.

## 3. Ephemeris and Gaia comparison

**Linear fit to the B eclipses** (six TESScut times, `step3.py`):
- P = **28.40515 ± 0.00003 d**
- T0 = **2978.3647 ± 0.0008 BTJD**
- χ² is 2.6 for 4 degrees of freedom.
- O−C in minutes: +1.1, −11.3, −0.9, +0.1, +2.4, −0.1. Sector 34 has the noisiest event.

**Forward tests:**
- An ephemeris built only from the four eclipses the classifier saw predicts sector 87 to within **+0.1 min**.
- One built from the first five predicts sector 108, twelve cycles beyond them, to within **−0.2 min** (predicted 4313.4067 ± 0.0017).

**Against Gaia's period:** the difference is −0.0002 d, which is −0.03σ. The eclipses are 26 cycles apart and Gaia's σ_P is 0.008 d, so a 25- or 27-cycle alias is ruled out.

**Against Gaia's predicted conjunctions** (`conjmc.py`, Monte Carlo over this star's own covariance):
- B eclipses: 1501 is +0.348 d (0.81σ), 2239 is +0.334 d (0.53σ), 2978 is +0.336 d (0.40σ), 3716 is +0.332 d (0.32σ). The offset of about +0.33 d is the same every time, so it is one small error in the Gaia orbit, not scatter.
- Conjunction A (Gaia, sd): 1493.65 ± 0.31, 2232.19 ± 0.48, 2970.73 ± 0.67, 3709.27 ± 0.87.

**e cos ω and e sin ω:** these cannot be measured from the light curve, because only one kind of eclipse is seen. Gaia gives e cos ω = −0.381 ± 0.019, e sin ω = −0.231 ± 0.019, and puts A 0.2572 ± 0.0114 in phase before B, i.e. 7.306 ± 0.324 d.

**Upper limit on conjunction A:**
- Six A windows were covered (1493.99, 2232.53, 2971.06, 3681.19, 3709.59 and 4306.10, each ±0.97 d), all 100% covered.
- The deepest 4–8 h box in five of them is 0.8–1.85 ppt in the 3×3 aperture, about 1/20 of the B depth there.
- In the sector 87 window the deepest box is 9.9 ppt, but that is the end of a scattered-light ramp.
- So there is no A eclipse deeper than about 2 ppt in the 3×3 aperture (roughly 0.3% intrinsic).

## 4. Independence

**Pixel test (`mypix.py`).** This is the centroid check the classifier asked for. I fitted each pixel of each cutout with a quadratic trend plus the eclipse template, then fitted the resulting map of lost flux with Gaussian point-spread functions placed at the Gaia positions.
- **In all four sectors I tested, the lost flux is centred on the target**, 1.6–5.6″ from it and 58–64″ from the δ Scuti star.
- Fitting the lost-flux map to the target alone versus the δ Scuti star alone gives χ² of:
  - s61: 1220 vs 11272
  - s88: 798 vs 3807
  - s34: 1523 vs 6850
  - s7: 979 vs 6803
- At the δ Scuti star's pixel the fractional depth is 0.07 ± 0.08%, 0.14 ± 0.16%, −0.05 ± 0.17% and 0.00 ± 0.20%. It would need to be 0.8% for that star to be the source.
- So the QLP centroid shift is the target dimming inside a blend, not a neighbour.

**Neighbour dilution table** (Gaia sources brighter than G 15 within 60″, plus the VSX and Gaia-EB stars). "Dip needed" is how deep that star's own eclipse would have to be to produce the observed one, taking a 3.6% observed depth.

| Star | G | Separation | Dip needed | Possible? |
|---|---|---|---|---|
| δ Scuti star | 9.80 | 55″ | 0.8% | Possible on brightness, but excluded by the pixel test |
| Gaia-EB candidate (Mowlavi+2023) | 16.17 | 41″ | ~280% | No |
| VSX E-type, P 1.12 d | 18.17 | 29″ | ~1800% | No |
| Faint neighbour | 17.58 | 2.9″ | ~1000% | No |

**Other pipelines** (`pipe2.py`): every one shows the eclipse at the same time with T14 of 6.2–6.5 h:
- TESS-SPOC s7: 1501.299 (SAP 2.45%, PDCSAP 3.60%)
- TESS-SPOC s34: 2239.831 (SAP 1.88%, PDCSAP 2.98%; CROWDSAP 0.68 and 0.62)
- GSFC-eleanor-lite s7: 1501.2996, 2.32%
- TGLC s7: 1501.2977 (aperture 3.18%) and 1501.3013 (PSF 2.63%)

I did not finish parsing the T16 file.

## 5. Physics (`myphys.py`)

- **Mass function:** f(m) = 0.1030 M☉.
- **Companion mass:** for a primary of 1.2 / 1.4 / 1.6 M☉ (TIC gives R1 2.58 R☉ and Teff 6026 K; Gaia M_G ≈ 2.6 says it is somewhat evolved), m2 at i = 90° is 0.73 / 0.79 / 0.85 M☉, a K dwarf, and a = 49–53 R☉.
- **Separations:** about 32 R☉ at B (0.651a) and about 53 R☉ at A (1.042a).
- **Durations:** a central eclipse would last 10.1–10.6 h at B and 16–17 h at A.
- **Geometry from the observed duration:**
  - The observed 6.5 h at B gives an impact parameter of about 0.78 (R1+R2), so i ≈ 85.5°.
  - At A the impact parameter is then about 1.24 (R1+R2), so **no eclipse at A is possible**. The missing A eclipse is what this geometry predicts.
- **Which star is in front:** in the RV convention for the primary's ω, the companion is in front at A, so at B the evolved primary passes in front of and grazes the companion. The eclipse we see would then be a grazing occultation of a companion giving about 5–8% of the light, which would yield a depth of about 2–4%. That is consistent with the crowding-corrected 3.0–3.6%, though a bit tight unless the companion sits near the top of the mass range. If the convention were the other way round, a grazing transit of a 0.75 R☉ star across a 2.6 R☉ star also gives about 3%. Either way, depth, duration, V shape and the absent A eclipse fit one geometry.
- **RUWE 3.5** could be the photocentre wobble of this orbit. A third body is not excluded.

## 6. Verdict: CONFIRMED

The deciding numbers:
- Six eclipses at one conjunction kind, two of them forward predictions that landed within 0.1 and 0.2 min.
- The eclipse period matches Gaia's to 0.03σ, and every eclipse falls 0.3–0.8σ from Gaia's B conjunction.
- The lost flux sits on the target, and the only neighbour bright enough to mimic it (the G 9.8 δ Scuti star) is excluded by a χ² ratio of 5–9.
- Four independent pipelines see it.
- Nothing is catalogued: this is a new eclipsing binary.

**Next predicted eclipses (BTJD):**
- **B:** 4341.812, 4370.217, 4398.622, 4427.027, 4455.432, 4483.838, 4512.243 (each ±0.002 d).
- **A:** none expected (impact parameter about 1.24). If it happened, it would be at B − 7.306 ± 0.32 d: 4334.51, 4362.91, 4391.32, 4419.72, …

**What would settle it further:**
- Spectra at B to confirm what the companion is, or an SB2 detection, so the light ratio and depth can be checked against each other.
- A limb-darkened two-sphere fit using a proper point-spread-function depth, for the inclination and radius ratio.
- A Gaia DR4 epoch-RV orbit to remove the +0.33 d offset.

**Services that could not be checked:** ExoFOP (503), so CTOIs remain unchecked.

Sources: [web search (no relevant results)](http[local path omitted]), [arXiv 2604.04004 (search result, unrelated)](http[local path omitted])
