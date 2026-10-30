# TIC 146111348 (TYC 8201-1042-1; Gaia DR3 5365525935061421952) -- adversarial check

Checkers: Opus 5.5 (steps 1-3 and the difference images, 2026-10-20; killed by a usage limit) and a second Opus 5.5 session that resumed on 2026-10-21. The second session re-checked steps 1-3 and did steps 4-6.
Gaia SB1: P 49.23438 +- 0.01378 d, e 0.1854 +- 0.0119, w 136.30 +- 4.11 deg, K1 35.53 km/s, gamma 41.18 km/s. TIC: Tmag 10.54, Teff 4716, R 5.56 (giant), d 590 pc.

## Verdict: CONFIRMED
This is a long-period eclipsing binary made of a K giant and a smaller, hotter companion of about 6000 K. The deeper eclipse (B) is a partial (grazing) occultation of the companion behind the giant. The shallower eclipse (A) is a full transit of the companion across the giant.

## 1. Archives (what was queried, what came back)
- cats.py --r 60: VSX none; ASAS-SN none; Prsa+2022, IJspeert+2024 and Kostov+2025 t2/t3/t4 none within 5"; SIMBAD has TYC 8201-1042-1 as [SB*] with 5 references (RAVE DR4/5/6, APASS-RAVE, Gaia DR3 multiplicity).
- Gaia DR3 vari_summary 0 rows, vari_eclipsing_binary 0 rows, phot_variable_flag NOT_AVAILABLE. SB9 0; WDS 0; ExoFOP has no TOI or CTOI. VizieR: ZTF 0 (the star is too far south), ATLAS 0, GCVS 0, WISE var 0, Gaia veb 0, Prsa 0.
- RAVE DR6 has one RV: 49.89 +- 0.63 km/s on 2007-03-28.
- Web search on the TYC, TIC and Gaia DR3 ids: no page mentions the star.
- MAST CAOM (10"): QLP s9, 10, 36, 63, 90, 99, 100; ELEANOR-LITE s9, 10; T16 s9, 10; TGLC s9, 10; TESS-SPOC s63 (TPF).
- Gaia: RUWE 1.15, ipd_frac_multi_peak 0, GSP-Phot Teff 4900 and logg 3.12.
- No prior art. The eclipses are new.

## 2. Eclipses (raw QLP SAP_FLUX, QUALITY==0, no trimming)
- B s9: 1565.73168 +- 1.4 min, depth 12.8%.
- B s36: 2304.34708 +- 0.9 min, depth 14.2%.
- B s100: 4077.01554 +- 0.8 min, depth 12.4%.
- A s9: 1545.049, depth 7.7%. Pre-ingress cadences flagged; one-sided, not used in the fit.
- A s10: 1594.29073 +- 0.9 min, depth 8.1%.
- A s36: 2283.66246 +- 0.7 min, depth 8.2%.
- A s63: 3022.27478 +- 0.7 min, depth 8.4%.
- A s90: 3760.895 +- 3.9 min. Egress only, on cadences flagged after the orbit gap.
- A s99: falls in the data gap.
- Shapes: B is rounded/V-like with T14 25.3 h. A has T14 21.8 h, ingress 7.8 h and a short, nearly flat bottom.
- Re-timing with my own code (mirror symmetry): B 1565.73400, 2304.34700, 4077.01525; A 1545.0505, 1594.29050, 2283.66300, 3022.27425. All agree with the list above to within 0.1-3.3 min.
- Census: nothing deeper than 0.5% outside the eclipses, apart from an orbit-start scattered-light ramp in s10 at 1585.1-1585.3. In-eclipse background dips of 1-3% of the star's flux are the star's own wings in the background annulus.
- Coverage: every predicted eclipse that falls inside the data is present, with the expected depth. None is missing.

## 3. Ephemeris
- Joint linear fit (common P; errors scaled x2.0): P = 49.24084 +- 0.00003 d; T0_B = BTJD 1565.73335 +- 1.7 min; T0_A = BTJD 1594.29078 +- 1.1 min. O-C: B -2.4, +1.7, -0.6 min; A -0.1, -0.0, -0.3, +11.4 min (s90 is egress-only on flagged cadences).
- Against Gaia: P differs by +0.0065 d, which is +0.47 sigma. The observed B time is 0.06-0.22 d later than Gaia's predicted conjunction (at most +0.54 sigma), and A is 0.05-0.21 d earlier (at most -1.0 sigma).
- The A-B separation is 28.557 d (phase 0.57995), against Gaia's prediction of 28.83 +- 0.39 d (-0.68 sigma).
- Physical model (step 5): e 0.1726, w 136.35 deg, so e cos w -0.125 and e sin w +0.119. Gaia has e cos w -0.134 and e sin w +0.128. e is -1.1 sigma from Gaia, and w agrees to 0.0 sigma.

## 4. Independence
- Three other pipelines show both eclipse kinds at the QLP times (s9/s10, timed with my mirror method):
  - B 1565.73: ELEANOR-LITE raw 1565.73425 (12.8%); TGLC aperture 1565.73525 (16.0%); TGLC PSF 1565.73450 (14.9%); T16 1565.73400 (12.4%).
  - A 1594.29: ELEANOR-LITE 1594.28975 (8.3%); TGLC 1594.29075 (aperture 9.7%, PSF 8.7%); T16 1594.29075 (7.2%).
  - A 1545.05: ELEANOR-LITE 1545.05175; T16 1545.05000.
  - All are within 0-5 min of QLP. TGLC's PSF photometry, which fits Gaia-positioned PSFs, puts the whole dip on the target.
- Difference images from TESScut (s9 B, s36 A, s36 B, s63 A, s100 B; I re-ran s36 B and s63 A and reproduced the earlier numbers exactly):
  - The centroid of the flux deficit lies 1.4-5.6" from the target. The out-of-eclipse light centroid is 6-21" off, pulled by neighbours.
  - 72-81% of the deficit falls in the 3x3 box on the target, compared with 23-37% of the light.
- Neighbours:
  - Within 60", only the G 12.79 star at 55.5" is bright enough to host the dips in flux terms; it would need a 60% dip for B and 37% for A. Its pixel loses 1.8% (s36 B) and 0.4% (s63 A), against 14.0% and 8.2% in the target pixel.
  - The G 13.32 star at 66" would need 98% and 60%; its pixel shows 0.7%.
  - All other neighbours would need dips of more than 100%. Ruled out.

## 5. Physics (deeper-B question)
- Mass function f(m) = 0.217 Msun; a1 sin i = 34.0 Rsun.
- Which star is in front: the SB1 w is the giant's. A falls at nu = 90 - w = 313.7 deg, where the companion is in front, near periastron (r/a 0.856). B falls at nu = 133.7 deg, where the giant is in front, near apastron (r/a 1.107).
- One geometry fits both s36 eclipses. I fitted a two-sphere eccentric model with the giant's quadratic limb darkening fixed at 0.45/0.20:
  - k = 0.312; L2 = 0.175; R1/a = 0.0615; i = 87.38 deg.
  - Residuals are white, with rms 0.90 and 0.92 ppt.
  - Impact parameter b_A = 0.64, which is below 1 - k = 0.69, so A is a full transit with a short, flattish, limb-darkened bottom.
  - Impact parameter b_B = 0.82, which is above 1 - k, so B is a PARTIAL occultation. That gives the rounded, V-like shape, as observed. The larger separation at apastron is exactly what raises b at B.
- Why B is deeper: the giant covers part of a companion that supplies 17.5% of the TESS light, removing 13-14%. At A, the companion's disk (k^2 = 0.097) blocks about 8% of the cooler giant's light. Per unit area the companion is 2.18x brighter in TESS than the giant, which as blackbodies gives T2 about 5900-6150 K for T1 = 4716-4900 K.
- Sizes and masses: for M1 = 1.5 / 2.0 / 2.5 Msun, m2 = 1.16 / 1.35 / 1.53 Msun, R1 = 4.8 / 5.2 / 5.5 Rsun and R2 = 1.50 / 1.62 / 1.72 Rsun (logg1 3.25 / 3.31 / 3.35; TIC R1 5.56, Gaia logg 3.12). The companion would be a slightly evolved F/G star of about 1.35 Msun around a giant of about 2 Msun. That is self-consistent.
- The single RAVE RV (49.89 km/s in 2007) matches the orbit's predicted 51.0-52.5 km/s (the orbit spans 0.9-71.9) to within 1-3 km/s.
- Depths, shapes, durations, both timings and the companion's light all fit one geometry.

## 6. Next predicted eclipses (BTJD; linear ephemeris; formal errors about 2 min, allow +-10 min)
- A (full transit, ~8.2%, 21.8 h): 4351.778, 4401.018, 4450.259, 4499.500, 4548.741, 4597.982
- B (partial occultation, ~13-14%, 25.3 h): 4372.461, 4421.702, 4470.943, 4520.183, 4569.424, 4618.665

## What would settle it further
- Spectroscopy for an SB2: K2 should be about 32-40 km/s, with lines from a ~6000 K star. That would give dynamical masses.
- Multi-band photometry of a B eclipse: because B is a partial occultation, its depth should rise toward the blue, since the companion is hotter.
- Further TESS sectors to tighten e and w (the e of 0.173 vs Gaia's 0.185 is a 1.1 sigma difference).

Files: progress.md, verify.py/txt, zoom.py/zoom_all.png, pipe2.py/txt, diffimg_s36B.txt, diffimg_s63A.txt, diff_*.png/json, neighbours.txt, physics.py/txt, ebfit.py, ebfit_s36.json and ebfit_s36_fit.json/png, rave_check.py/txt, coverage.py/txt, ephem_final.py/json/_out.json/txt. Downloads are in C:\Home\sky\data\qlp-sb-p20-60\vet146111348\.