# TIC 55114385 — per-object vet (sb1-scale, pervet)

**Verdict: CONFIRMED** — an eclipsing SB1 with a grazing primary eclipse at Gaia conjunction A and a secondary at phase 0.5000. P = 4.268746 d.

TYC 1337-1803-1, Gaia DR3 3371848501900503296, G 10.59, Tmag 10.16, TIC Teff 5995 K, R 1.27 Rsun, M 1.105 Msun, d 201 pc.
TESS data: QLP s043, s044, s045 (600 s) and s071, s072 (200 s). TESS-SPOC and TARS light curves and SPOC target pixel files exist for all five sectors.

Wave 4, 2026-10-20/21. The killed session had already run the archive checks, vet, sec, sec2, gaiaepoch, mastlc (with downloads), indep (primary and secondary) and tpfdiff on the five target pixel files. The second session re-checked those numbers and added the physics and dilution check (`physics-out.txt`). It also overrode `sec-out.txt`; see the secondary section below. (Saved by the parent session; the file-write tool refused REPORT.md for the subagent.)

## 1. Archives (own pass)
- `cats.py --r 60`: VSX none; ASAS-SN none; SIMBAD has TYC 1337-1803-1 as `SB*` only.
- SB9, WDS and J/AJ/160/111 return nothing.
- ExoFOP has no TOIs, CTOIs, imaging, spectroscopy or companions.
- Gaia DR3: vari_summary and vari_eclipsing_binary are empty; phot_variable_flag is NOT_AVAILABLE; RUWE 1.17.
- Batch receipts: c3-ebcats2 has no hit in any EB table. c3-vetsum gives "dphi +0.020/−0.474 ATTR".
- Web searches for "TYC 1337-1803-1" and "TIC 55114385" find no page that mentions the star.
- **Not previously catalogued as an eclipsing binary.**

## 2. Eclipse measurements (raw QLP SAP_FLUX, QUALITY==0)

**Primary:**
- Trapezoid fit: depth 17.89 ppt, T14 1.86 h, T12 0.74 h. T12/T14 is 0.40, so the shape is close to a V. Flat bottom 0.37 h.
- 23 individual eclipses, all at S/N 27–70, give 17.81 ± 0.07 ppt.
- Even 17.80 ± 0.09, odd 17.81 ± 0.10.
- By sector: 17.37, 17.89, 17.55, 18.31, 17.81 (each ±0.13–0.17).
- The scatter is larger than the errors (χ² 69/22). The amplitudes are about 0.5 ppt from sector to sector. That fits spot activity on a G star likely tidally synchronised to the 4.27-d orbit: the c1 harmonic at the orbital period is −2.1 ppt.
- Three events have bit-32 cadences in their windows. Their depths (16.9, 18.4, 17.8 ppt) are normal.
- No event falls within 0.5 d of a listed systematic.

**Controls:** phases 0.125–0.875 (excluding 0.5) are within ±0.11 ppt of zero.

**Background:**
- In-eclipse minus out-of-eclipse SAP_BKG is −0.76 ppt of the target's flux.
- A fake dip of 17.8 ppt would need +231 e⁻/s.

**Centroids:** dX +0.32 ± 0.10 mpix, dY −0.05 ± 0.13 mpix.

**Blind dip census:**
- 50 dips at S/N ≥ 4.
- 22 are primaries. 25 of the off-ephemeris dips sit at phase ±0.50, which is the secondary.
- There is no off-ephemeris dip of 8.9 ppt or more.

**Secondary:**
- `sec-out.txt` is overridden. It was produced by the shared sec.py, which locked onto a 9.8-h feature at phase 0.47 with an inconsistent period (the known failure mode). sec2 was used instead.
- At phase 0.5000: 2.43 ± 0.21 ppt, S/N 11.7.
- 475 random phases give a maximum S/N of 2.70 (rms 0.73). The secondary's S/N is 16.0× the control rms.
- The best phase is 0.4998 (1σ range 0.4993–0.4998).
- Per event (25 events, all at S/N > 3): 2.46 ± 0.06 ppt. In raw SAP: 2.51 ± 0.07 ppt.
- No event could be faked by the background: |fake| ≤ 0.29 ppt for every event.
- The depth varies (χ² 116/24; 1.98 in s072, 2.94 in s071). That is again consistent with spots.
- Duration ratio T14(sec)/T14(pri) = 0.95 (1σ range 0.90–1.00).

## 3. Ephemeris and orbit
**Primary ephemeris:**
- P = 4.268746 ± 0.000001 d.
- T0 = 2870.92006 ± 0.00009 BTJD.
- χ²/dof 69/21 (errors scaled ×1.82); O−C rms 0.6 min.
- Dropping any one sector leaves P within 1 ppm-d.

**Comparison with Gaia:**
- Gaia P = 4.268512 ± 0.000105 d, +2.24σ from the TESS period.
- Projecting from the Gaia epoch into the TESS sectors therefore drifts, giving +1.9σ to +2.0σ at conjunction A.
- At the Gaia epoch itself, using Gaia's correlation vector (ω–Tp correlation +1.00):
  - the primary lands on conjunction A at −0.66 h (−1.33σ);
  - the secondary lands on conjunction B at −0.09 h (−0.32σ).
- Conjunction B is −27σ to −37σ from the primary, so B cannot be the primary.
- So this is the 403936502 pattern: Gaia's own period is slightly off, and the attribution holds when compared at the Gaia epoch.

**Secondary timing:** the per-event times put the secondary at phase 0.50003 ± 0.00015.

**Orbit shape compared with Gaia:**

| quantity | TESS | Gaia | difference |
|---|---|---|---|
| e cos ω | +0.00004 ± 0.00024 | −0.0079 ± 0.0098 | +0.81σ |
| e sin ω (from the duration ratio) | −0.026 ± 0.026 | +0.019 ± 0.009 | −1.6σ |

The −1.6σ e sin ω difference is mild and uses a crude duration-ratio estimator. Gaia's e = 0.023 ± 0.009 is small. Overall the orbit is consistent with near-circular.

## 4. Independence
**Other pipelines' light curves** (`indep-out.txt`, `indep-sec-out.txt`). Depths in ppt:

| pipeline | primary depth per sector | secondary depth per sector |
|---|---|---|
| TESS-SPOC PDCSAP | 17.2–17.5 | 2.2–2.7 |
| SPOC SAP | 16.2–16.6 | 2.0–2.6 |
| TARS | 16.5–17.4 | 2.2–3.2 |
| QLP SAP | 17.4–18.2 | 2.2–2.8 |

- Every pipeline sees both eclipses in every sector.
- SPOC SAP is about 1 ppt shallower than PDCSAP. That is the expected crowding correction (TIC contamination ratio 0.05).

**Difference images from the SPOC target pixel files** (s43, s44, s45, s71, s72; `tpfdiff-out.txt`, `tpfdiff_*.png`):
- In every sector the pixel with the most significant loss (S/N 34–49) is the target pixel.
- A PSF fit at the target gives χ² 766–1134, and implies the target's own dip is 12.9–14.1 ppt (with crude PSF normalisation).
- The best neighbour fit gives χ² 3730–6715.
- The G 14.51 neighbour at 19.5″ would need a dip of 141–204 ppt in this test.
- The batch diffimg result for s72 agrees: peak on target, loss 1.27″ from the light centroid.

**Dilution:**
- The neighbour at G 14.51, 19.5″ would need a 66% primary dip and a 9% secondary.
- The neighbour at G 14.76, 77″ would need 83%.
- All others would need more than 100%.
- Even the two that could in principle produce it are excluded by the difference images.

## 5. Physics
**Companion mass and orbit size:**
- Mass function f(M) = 0.0891 ± 0.0018 Msun.
- For a primary mass M1 of 0.99–1.22 Msun, the companion's minimum mass m2 (at i = 90°) is 0.61–0.69 Msun.
- The separation is a ≈ 13.4 Rsun, or 10.5 primary radii.

**Grazing geometry:**
- A main-sequence companion of R2 ≈ 0.68 Rsun gives k ≈ 0.53, so a central eclipse would last 4.8 h.
- The observed 1.86 h implies an impact parameter b ≈ 1.41 primary radii (i ≈ 82°). That is grazing, since b < 1 + k = 1.53.
- Grazing explains both the near-V shape and a depth (17.8 ppt) far below k² (≈ 290 ppt).

**Which star is in front:**
- At conjunction A (the primary eclipse), the K/M-dwarf companion passes in front of the G star.
- At conjunction B, the G star passes in front of the companion.

**Companion temperature:**
- The depth ratio gives a surface-brightness ratio J ≈ 0.136, so T2 ≈ 3600 K at 800 nm.
- A 0.65 Msun main-sequence star should be nearer 4000–4200 K.
- That gap is within what the J estimate can resolve for a grazing chord, where limb darkening differs between the two eclipses and spots are present.
- The companion supplies about 4% of the light in the TESS band.

Everything else fits one grazing, near-circular G + late-K/early-M system. The eccentricity is low and the conjunction is not near periastron, so the heartbeat/tide confusion does not arise.

## Verdict: CONFIRMED
The deciding numbers:
- 23 of 23 primaries at S/N 27–70, 17.81 ± 0.07 ppt, with even and odd depths equal.
- The primary falls on Gaia conjunction A at the Gaia epoch (−1.3σ) and the secondary on conjunction B (−0.3σ). The 2.2σ difference between Gaia's period and the TESS period accounts for the drift into the TESS sectors (the 403936502 pattern).
- A secondary of 2.43 ± 0.21 ppt at phase 0.5000 with S/N 11.7, where no random phase gets above S/N 2.7.
- Both eclipses appear in TESS-SPOC PDCSAP, SPOC SAP, TARS and QLP in all five sectors.
- The difference images from the SPOC target pixel files put the loss on the target in all five sectors, and the brightest neighbour would need a 66% dip.
- The physics fits one geometry: a grazing eclipse by a ~0.65 Msun companion.

**Next predicted eclipses** (BTJD; linear TESS ephemeris; secondary at phase 0.50003):

| primary | secondary |
|---|---|
| 4403.4000 ± 0.6 min | 4405.5345 ± 1.1 min |
| 4407.6688 ± 0.6 min | 4409.8033 ± 1.1 min |
| 4411.9375 ± 0.6 min | 4414.0720 ± 1.1 min |

**What would settle it further:**
- Gaia DR4 epoch RVs, to fix the conjunction-A attribution directly and resolve the 2.2σ period offset.
- Spot-aware modelling, to explain the scatter in both depths.
- Ground photometry of the 1.9-h, 18-ppt primary at Tmag 10.2 is easy.
