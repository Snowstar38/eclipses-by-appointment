> Historical report: superseded by the current reconciliation at ../../../reports/60583013/REPORT.md. Its original bytes are preserved in the source archive; this public copy is sanitized.

# TIC 60583013 (UCAC4 350-013805): adversarial check

Gaia DR3 SB1, P 26.65687 ± 0.00947 d, ω 16.5°, e cos ω 0.0736 ± 0.0238, e sin ω +0.0205 ± 0.0225; RUWE 0.94. TIC R 1.853 R☉, M ~1.14 M☉, an F/G star. Checked by an Opus checker for Fable 5.1, 2026-10-22 (chunk-3 wave 6, 19:37–19:43, under a 15-minute cap). Saved from the checker's final message by Fable 5.1; the file tool refused REPORT.md. Scripts and outputs are in this folder, each step's numbers and the script that made them in `progress.md`; downloads in `[local path omitted]

## Verdict: CONFIRMED

The primary and the secondary both come back in three pipelines, and the pixel test puts both on the target. The two secondaries, 28 cycles apart, give a period 0.6σ from Gaia's. The depths, durations and stellar density all fit one geometry: an M dwarf of about 0.36 M☉ orbiting a 1.85 R☉ F/G star.

### 1. Archives (what I queried and what came back)
- **Gaia DR3 TAP** (`arch2.py`): the full NSS row was retrieved (SB1, its own `corr_vec`). `vari_summary` and `vari_eclipsing_binary` have 0 rows. RUWE is 0.94 and `ipd_frac_multi_peak` is 0.
- **VizieR TAP** (`arch2.py`): VSX, SB9 and WDS each returned 0 rows, with no error.
- **VizieR asu-tsv** (`viz.py`): VSX, Prša+2022, IJspeert+2024 and Kostov+2025 tables 2, 3 and 4 each returned 0 rows. The rest of the sweep had not answered when I wrote this. That covers the Mowlavi synthetic-photometry table (which is not prior art anyway), the ASAS-SN II/366 catalogue, ATLAS, Gaia vari classifications and ASAS ACVS. The ASAS-SN lookup in `cats.py` came back clean (next item).
- **cats.py**: no VSX entry and no ASAS-SN entry. SIMBAD lists only "UCAC4 350-013805 [SB*]", which comes from the Gaia SB1 orbit.
- **ExoFOP**: HTTP 503, so CTOIs are unchecked. The NASA Exoplanet Archive TOI table has no TOI for TIC 60583013.
- **Web search** on "UCAC4 350-013805" and "TIC 60583013": nothing relevant.
- **MAST CAOM** (`archives.py`): QLP s6 and s33; TESS-SPOC s6 and s33; TARS s6 and s33; TGLC s6; ELEANOR-lite s6; TASOC s6; T16 s6. There is no SPOC 2-min data.
- **Prior art**: none found. As far as these archives show, this is a new eclipsing binary.

### 2. Eclipses (raw SAP_FLUX, trapezoid plus quadratic baseline; `ecl.py` → `ecl.txt`, `ecl_fits.png`)

| Event | Pipeline | Mid-time (BTJD) | Depth | T14 | T12 | Flat |
|---|---|---|---|---|---|---|
| A (primary), s033 | QLP | 2210.9657 ± 0.0003 | 4.12% | 9.77 h | 1.79 h | 6.19 h |
| A, s033 | TESS-SPOC | 2210.9660 | 4.08% | 9.78 h | | |
| A, s033 | TARS | 2210.9653 | 4.18% | 9.90 h | | |
| B (secondary), s033 | QLP | 2225.0600 ± 0.0010 | 0.257% | box ~8–10 h | | |
| B, s033 | TESS-SPOC | 2225.0545 | 0.293% | 10.4 h | | |
| B, s033 | TARS | 2225.0548 | 0.293% | | | |
| B, s006 | QLP | 1478.8272 ± 0.0015 | 0.229% | 9.4 h | | |
| B, s006 | TESS-SPOC | 1478.829 | 0.250% | | | |
| B, s006 | TARS | 1478.839 | 0.252% | | | |
| B, s006 | TGLC | 1478.849 | 0.39% | | | |
| B, s006 | ELEANOR | 1478.91 | | | | |

ELEANOR's fit of the s006 event is poor. I used the spread across pipelines as the timing error (s006: ±0.0059 d).

- **Primary shape**: the bottom is curved by limb darkening, so the eclipse is a full transit, not a grazing one. Background and centroids show nothing through it (centroid shift of 0.0003 px, 1σ), and no cadence inside it is flagged.
- **s033 secondary**: background is flat, centroids show nothing, and no cadence is flagged.
- **s006 event**: it starts about 0.6 d after the mid-sector gap. I checked it against the post-gap ramp (`zoom6.py` → `zoom6.png`):
  - The background ramp ends at about 1478.55, before ingress, and the background is flat through the dip in both QLP and TESS-SPOC.
  - The centroids show only the smooth post-gap relaxation, with no eclipse-shaped step. That relaxation is what produced the formal 10σ "centroid shift" in the QLP fit.
  - Egress at about 1479.02 is sharp and nothing happens in background or centroids there.
  - **Common-mode test** (`cm6.py` → `cm6.txt`): I ran the same box on 240 other QLP s006 stars. Their median depth is +0.003%. In camera 2 (138 stars) the median is +0.005%, and only 1 star exceeds 0.15%. The target is +0.239% at 19.7σ, so this is not a sector-wide systematic.
- **Blind census** (`census.py` → `census.txt`): only these three events show up. The other hits are two single-cadence QLP outliers (2207.72 and 2221.44, both background spikes and absent in TESS-SPOC) and wiggles of 0.09% or less.

### 3. Ephemeris and the Gaia comparison (`ephem.py` → `ephem.txt`; `conjmc.py` with this star's own `corr_vec` → `conjmc.txt`)
- **Period from the two secondaries** (28 cycles): **P = 26.65117 ± 0.00023 d**. Gaia gives 26.65687 ± 0.00947, so Δ = −0.6σ. Counting 27 or 29 cycles instead puts the period about 100σ from Gaia's, so the cycle count is unambiguous.
- **Limits of the ephemeris**: there is only one primary, so the primary ephemeris assumes the same period. With two points per kind, O−C is zero by construction.
- **Ephemeris**: primary at 2210.9657 + n × 26.65117; secondary at 2225.0600 + n × 26.65117.
- **Against Gaia's predicted conjunctions**:
  - A (k = 68) predicted 2210.955 ± 0.62; observed offset +0.01 d (0.0σ).
  - B (k = 68) predicted 2225.549 ± 0.70; offset −0.49 d (−0.7σ).
  - B (k = 40) predicted 1479.157 ± 0.46; offset −0.33 d (−0.7σ).
- **A windows in s006**: neither is covered. Refined times are 1464.733 and 1491.384; the sector runs 1468.29–1490.04.
- **e cos ω**: the secondary falls at phase 0.52884 ± 0.0001 after the primary; Gaia's Monte Carlo gives 0.5468 ± 0.0151 (−1.2σ). That makes e cos ω = 0.0453, against Gaia's 0.0736 ± 0.0238 (−1.2σ).
- **e sin ω**: I fitted the secondaries with the ingress time fixed to the primary's (T12 = 1.77 h). That gives T_B/T_A = 1.10 in s033 and 1.08 in s006, so e sin ω ≈ +0.04 to +0.05, against Gaia's +0.0205 ± 0.0225 (about +1.2σ). I did not run the limb-darkened two-sphere model. Neither eclipse is grazing (the primary has b ≈ 0.3 and a flat bottom; the secondary is a flat box), so the false-T23 trap the brief warns about does not apply. The trapezoid result is still crude.
- **Gaia's predicted durations**: Gaia's ω (16.5°) predicts B lasting 1.046 times as long as A; I measured 1.08–1.10, which is consistent.

### 4. Independence
- **Other pipelines**: TESS-SPOC and TARS reproduce both s033 events. TESS-SPOC, TARS and TGLC reproduce the s006 secondary.
- **Per-pixel regression** of TESScut 11×11 cutouts (`pixtrap.py` → `pixtrap.txt`, `pix_*.png`):
  - s033 primary: the flux-deficit centroid is 1.2″ from the target and 0.4″ from the light centroid. Depth is 4.08% on the target pixel (151σ), 4.15% in a 3×3 aperture and 4.13% in 5×5. The largest signal outside the 3×3 is 25σ, which is PSF wing: it is 4% of the target pixel's lost flux, at the same fractional depth.
  - s033 secondary: deficit 1.3″ from the target and 0.4″ from the light centroid. Depth is 0.27% on the target pixel (12σ), the same in all three apertures; nothing outside the 3×3 exceeds 2.9σ.
  - s006 secondary: inconclusive (3.8σ on the target pixel; 30-min cadence, 66 cadences).
- **Neighbour dilution**: I took the Gaia G magnitudes of the neighbours and worked out the dip each would need (depth × 10^(0.4Δm)) to produce the primary (4.1%) and the secondary (0.27%).

| Neighbour | Separation | Factor | Primary needs | Secondary needs |
|---|---|---|---|---|
| G 18.69 | 10.7″ | ×830 | 34× (impossible) | 2.2× (impossible) |
| G 17.68 | 36″ | ×327 | 13× (impossible) | 88% |
| G 16.52 | 50″ | ×113 | 4.6× (impossible) | 30% |

  No Gaia neighbour within 60″ is brighter than G 16.5. The G 16.52 star's pixel shows only 1.4σ at the secondary, consistent with PSF wing, and the deficit centroid sits on the target.
- **Other conjunction**: both kinds were detected, so no null test was needed.

### 5. Physics
- **Masses and orbit**: the mass function is 0.0205 M☉. For M1 = 1.14 M☉ (the range 1.0–1.3), m2 at i = 90° is 0.358 M☉ (0.33–0.39). The semi-major axis is 43.0 R☉, or 23.2 R1 with R1 = 1.853 R☉.
- **Durations**: for a central eclipse, T14 would be 10.2 h at A and 10.7 h at B. The observed 9.8 h at A fits an impact parameter b of about 0.3.
- **Primary shape** (a simple formula that ignores limb darkening): k ≈ 0.20, so R2 ≈ 0.37 R☉, which matches a 0.36 M☉ M dwarf. b ≈ 0.29 and a/R1 ≈ 24.3, against 23.2 predicted from TIC mass and radius. The stellar density agrees.
- **Which star is in front**: at A (ν = 90° − ω) the M dwarf transits the primary, which is the deep, limb-darkened eclipse. At B the M dwarf is occulted, which is the shallow, flat-bottomed box.
- **Secondary depth**: the secondary-to-primary depth ratio of 0.072 gives a TESS-band surface-brightness ratio of about 0.072. Blackbodies at 800 nm predict an occultation depth of 0.27% for a 3200 K companion and 0.38% for 3400 K; I measured 0.26–0.30%. Depths, durations, shapes and the companion's light all fit one geometry.

### 6. Verdict: CONFIRMED
**Deciding numbers:**
- The primary is detected at about 250σ in three pipelines, and the pixel test puts it on the target within 1.2″.
- The secondary is detected twice, in three pipelines each time. It is on the target in pixels in s033, and it is not common mode in s006.
- The secondaries give P = 26.6512 d, against Gaia's 26.6569 ± 0.0095 (−0.6σ).
- All conjunction offsets are within 0.7σ.
- e cos ω and e sin ω are each within about 1.2σ of Gaia's.
- The mass function, k and a/R1 agree with an M-dwarf companion of about 0.36 M☉.

**Next predicted eclipses (BTJD, ±0.02 d):**
- **Primary A**: 4343.059, 4369.710, 4396.362, 4423.013, 4449.664, 4476.315
- **Secondary B**: 4357.154, 4383.805, 4410.456, 4437.107, 4463.758, 4490.409

**What would settle it further:**
- A second primary eclipse, to fit an independent primary period and test the secondary's phase offset (e cos ω).
- A limb-darkened two-sphere fit, to firm up e sin ω and the inclination.
- ExoFOP CTOIs, once the service is back.
- RVs or a spectrum, to check the companion's mass.

**Not done or not checked:** ExoFOP (503, so CTOIs unchecked); the tail of the VizieR asu-tsv sweep listed above, which had not returned; the limb-darkened two-sphere fit; a TESS-SPOC difference image (I used the TESScut per-pixel regression instead).
