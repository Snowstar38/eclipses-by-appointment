# TIC 258860596 — per-object vet (sb1-scale, pervet)

**Verdict: CONFIRMED** — an eclipsing SB1 with a grazing primary eclipse at Gaia conjunction A and a shallow secondary at phase 0.501. P = 4.959311 d.

TYC 2205-1326-1, Gaia DR3 1783049316382818816, G 11.50, Tmag 11.19, TIC Teff 6900 K, R 1.69 Rsun, M 1.5 Msun.
TESS data: QLP s056 and s083 (200 s). No other sectors, and no non-QLP light curves in MAST.

The work was done in two sessions (wave 4, 2026-10-20/21). The first was killed partway through. It left behind vet.py, sec.py, sec2.py, gaiaepoch.py, the archive queries, and their outputs, all in this folder. The second session checked the key numbers in those outputs, then added:
- the full MAST CAOM listing (`caomall-out.txt`);
- independent TESScut photometry and difference images (`cutphot-out.txt`, `cutdiff_s56/s83.png`, `cutfold_s56/s83.png`);
- the physics and dilution check (`physics-out.txt`).
(Saved by the parent session; the file-write tool refused REPORT.md for the subagent.)

## 1. Archives (own pass)
- `cats.py --r 60`: VSX none; ASAS-SN none; SIMBAD has TYC 2205-1326-1 as `SB*` (Gaia SB1) only.
- SB9, WDS and J/AJ/160/111 return nothing.
- ExoFOP has no TOIs, CTOIs, imaging, spectroscopy or stellar companions.
- Gaia DR3: vari_summary and vari_eclipsing_binary are empty; phot_variable_flag is NOT_AVAILABLE; RUWE 0.86.
- Batch receipts: c4-ebcats has no hit in any vetted or unvetted EB table. c4-vetsum gives "dphi −0.007/−0.486 ATTR".
- Web searches for "TYC 2205-1326-1" and "TIC 258860596" find no page that mentions the star.
- **Not previously catalogued as an eclipsing binary.**

## 2. Eclipse measurements (raw QLP SAP_FLUX, QUALITY==0, no trimming)

**Primary:**
- Trapezoid fit: depth 18.08 ppt, T14 2.82 h, T12 1.13 h. T12/T14 is 0.40, so the shape is close to a V. Flat bottom 0.56 h.
- Ten individual eclipses give 18.13 ± 0.13 ppt.
- The depth is constant (χ² 9.9/9): even events 18.15 ± 0.20, odd 18.11 ± 0.18; s056 17.89 ± 0.18, s083 18.43 ± 0.20.
- Every event has S/N 20–52.
- None has a bit-32 cadence (momentum-dump flag) in its window. None falls within 0.5 d of a listed sector-wide systematic.

**Controls:** phases 0.125–0.875 (excluding 0.5) are all within ±0.13 ppt of zero. No control event reaches S/N > 3.

**Background:**
- In-eclipse minus out-of-eclipse SAP_BKG is +0.46 ppt of the target's flux.
- A fake dip of 18 ppt would need +91 e⁻/s.
- A unit-free regression gives a possible fake of at most 0.3 ppt per event. The one exception is the event at 2837.94, which has 14 flagged cadences, and even there the fake is only −2.2 ppt against an 11-ppt dip.

**Centroids:** dX −0.18 ± 0.27 mpix, dY +1.10 ± 0.93 mpix.

**Blind dip census:**
- 14 dips at S/N ≥ 4.
- 11 are on the primary ephemeris. The other 3 are 1.7–2.0 ppt dips at phase 0.5, which is the secondary.
- There is no dip deeper than 9 ppt anywhere off the ephemeris.

**Secondary:** sec2 was used, not the shared sec.py. sec2 fixes the primary's shape at the predicted phase and compares against random phases.
- At phase 0.5000: 1.38 ± 0.13 ppt, S/N 10.8.
- 436 random phases with the same shape give a maximum S/N of 1.94 (rms 0.97). None reaches the secondary's S/N; it sits at 11.1× the control rms.
- Changing the detrending (2 or 6 harmonics, or leaving the window unmasked) moves the depth by at most 0.02 ppt.
- Per event (10 events): 1.48 ± 0.13 ppt, constant (χ² 5.2/9). In raw SAP: 1.25 ± 0.15 ppt.
- Clean subset (excluding the listed systematic at 3564.5): 1.47 ± 0.15 ppt.
- Duration ratio T14(sec)/T14(pri) = 0.90 (1σ range 0.85–0.95).

## 3. Ephemeris and orbit
**Primary ephemeris:**
- P = 4.959311 ± 0.000003 d.
- T0 = 3056.15218 ± 0.00022 BTJD.
- χ²/dof 18.1/8 (errors scaled ×1.51); O−C rms 0.9 min.
- Dropping any one event changes P by at most 2 ppm-d.

**Comparison with Gaia:**
- Gaia P = 4.959237 ± 0.000701 d, which differs from the TESS period by +0.11σ.
- The Monte Carlo used Gaia's correlation vector (the ω–Tp correlation is +1.00). At the Gaia epoch (BTJD 389) the primary lands on conjunction A at −0.64σ; at BTJD 3250 it lands at +0.03σ.
- The secondary lands on conjunction B at +0.17σ at both epochs.

**Secondary timing:** the per-event times put the secondary at phase 0.50139 ± 0.00067. A free secondary period gives 4.959290 ± 0.000029 d, −0.75σ from the primary period.

**Orbit shape compared with Gaia:**

| quantity | TESS | Gaia | difference |
|---|---|---|---|
| e cos ω | +0.0022 ± 0.0011 | −0.0097 ± 0.033 | +0.36σ |
| e sin ω (from the duration ratio) | −0.053 ± 0.028 | −0.002 ± 0.035 | −1.1σ |

Both agree with Gaia's e = 0.034 ± 0.037, which is consistent with a circular orbit.

## 4. Independence
**MAST:** CAOM searched within 10.8″ under all target names (so TGLC products filed under Gaia IDs would show up). There are only the QLP s56/s83 light curves, the SPOC and TICA full-frame images, and non-TESS imaging. No SPOC, TESS-SPOC, TGLC, TARS or eleanor light curve exists.

**Own photometry from the TESScut cubes** (SPOC-calibrated FFIs, own aperture and background, no QLP product). Depths in ppt:

| aperture | s56 primary | s83 primary | s56 secondary | s83 secondary |
|---|---|---|---|---|
| r ≤ 1.0 px | 18.14 ± 0.19 | 18.58 ± 0.23 | 1.30 ± 0.18 | 1.76 ± 0.25 |
| r ≤ 1.5 px | 18.12 ± 0.16 | 18.51 ± 0.20 | 1.25 ± 0.16 | 1.60 ± 0.20 |
| r ≤ 2.0 px | 18.49 ± 0.18 | 18.76 ± 0.22 | 1.03 ± 0.18 | 1.59 ± 0.21 |
| r ≤ 3.0 px | 18.61 ± 0.25 | 18.58 ± 0.33 | 0.68 ± 0.26 | 1.78 ± 0.28 |

- The primary depth does not change with aperture size. An off-target source would make it change.
- The control phases 0.25 and 0.75 are within ±0.6 ppt of zero.
- The s56 secondary falls as the aperture grows, but the two ends differ by only 2σ, and the s83 secondary is flat.

**Difference images:**
- The centroid of the lost light is 1.0″ (s56) and 4.1″ (s83) from the centroid of the out-of-eclipse light.
- The pixel with the most significant loss (S/N 21 in s56, 27 in s83) is the target pixel or the one next to it.
- A PSF fit at the target gives χ² 88 (s56) and 805 (s83). A fit at any neighbour gives χ² ≥ 1194 (s56) and ≥ 3895 (s83).
- This agrees with the batch diffimg result for s56: peak on target, loss 1.09″ from the light centroid.

**Dilution:**
- The brightest Gaia neighbour within 90″ is G 15.70 at 74.9″. It would need an 87% dip to produce the primary.
- Every other neighbour would need more than 100%.

## 5. Physics
**Companion mass and orbit size:**
- Mass function f(M) = 0.0245 ± 0.0031 Msun.
- For a primary mass M1 of 1.35–1.65 Msun, the companion's minimum mass m2 (at i = 90°) is 0.43–0.48 Msun.
- The separation is a ≈ 15.3 Rsun, or 9.1 primary radii.

**Grazing geometry:**
- A main-sequence companion of R2 ≈ 0.49 Rsun gives a radius ratio k ≈ 0.29, so a central eclipse would last 5.4 h.
- The observed 2.82 h implies an impact parameter b ≈ 1.10 primary radii (i ≈ 83°). That is grazing, since b < 1 + k.
- Grazing explains both the near-V shape and a depth (18 ppt) far below k² (85 ppt).

**Which star is in front:**
- At conjunction A (the primary eclipse), the M-dwarf companion passes in front of the F star.
- At conjunction B, the F star passes in front of the companion.

**Companion temperature:**
- The depth ratio gives a surface-brightness ratio J ≈ 0.076, so T2 ≈ 3500 K at 800 nm.
- That is the right temperature for a 0.45 Msun main-sequence M dwarf.
- The companion then supplies about 0.6% of the light in the TESS band.

The depths, both durations and the secondary depth all fit one grazing, circular F + early-M system. The eccentricity is low and the conjunction is not near periastron, so the heartbeat/tide confusion does not arise.

## Verdict: CONFIRMED
The deciding numbers:
- 10 of 10 primaries at S/N 20–52, with constant depth 18.13 ± 0.13 ppt.
- P 4.959311 d, +0.11σ from Gaia's period. The primary falls on Gaia conjunction A (−0.6σ at the Gaia epoch) and the secondary on conjunction B (+0.2σ).
- A secondary of 1.38 ± 0.13 ppt at phase 0.5014 with S/N 10.8, where no random phase gets above S/N 1.9.
- Own TESScut photometry reproduces both eclipses: primary 18.1–18.8 ppt with no aperture dependence, secondary 1.3–1.6 ppt.
- The difference image puts the loss on the target, and no neighbour can produce the dip.
- The physics fits one geometry: a grazing eclipse by a ~0.45 Msun M dwarf.

**Next predicted eclipses** (BTJD; linear TESS ephemeris; secondary at phase 0.50139):

| primary | secondary |
|---|---|
| 4400.1256 ± 1.3 min | 4402.6121 ± 5.0 min |
| 4405.0849 ± 1.3 min | 4407.5715 ± 5.0 min |
| 4410.0442 ± 1.3 min | 4412.5308 ± 5.0 min |

**What would settle it further:**
- Gaia DR4 epoch RVs, to check that the deep eclipse falls at the RV node Gaia predicts for conjunction A.
- A third TESS sector, to tighten e sin ω.
- Ground photometry: a 2.8-h, 18-ppt eclipse at Tmag 11.2 is easy to catch.
