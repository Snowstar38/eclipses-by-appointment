# TIC 307361219 (TYC 9193-870-1, Gaia DR3 5270203254792431744): adversarial check

**Verdict: CONFIRMED.** It is an eccentric detached eclipsing binary on target, with P = 23.828151 d. It shows a 22% primary eclipse (the Gaia RV primary, a K4-5 dwarf, is eclipsed at Gaia conjunction A) and a 0.43% grazing secondary at phase 0.7136 (conjunction B). The companion is an early-M dwarf of about 0.5 Msun.

## Deciding numbers
- **Period.** 23 primaries over s2-s98 (2018-2025) give a linear ephemeris with rms O-C of 0.36 min. The secondary period agrees with the primary period to +0.007 +- 0.028 min/cycle. P_Gaia - P_TESS = +0.0009 d (0.2 sigma Gaia).
- **Timing against Gaia.** Gaia conjunction A, predicted at the deep eclipse: obs - pred = +0.18 +- 0.39 d. Conjunction B at the secondary: -0.33 +- 0.46 d. Swapping the two assignments puts them 14-60 sigma off.
- **On target.** The TESScut difference images (s63, s64) put the deficit centroid 1.0-1.5" from the light centroid for the primary and 1.7-4.0" for the secondary (one pixel is 21"). There is no Gaia neighbour brighter than G 15.89 within 60". A neighbour would need a primary dip above 1000%, so it cannot host the primary.
- **Independent pipeline.** TESS-SPOC raised two TCEs from s56-s69 (dvr.xml):
  - TCE1 epoch 2994.77167 (ours 2994.77174), depth 22.8%, 3.62 h, SNR 932.
  - TCE2 epoch 3011.7748 (ours 3011.7752), depth 0.40%, 2.97 h, SNR 19.
  - Both had alias periods (38.125 d and 27.23 d) because of the gappy coverage, and neither became a TOI.
  - Our fits to TESS-SPOC SAP s62/65/69 match QLP to within 0.4 min.
- **Physics.** A two-sphere model, with e cos w locked by the phase and e sin w fixed at +0.25 (Gaia +0.243), fits both eclipse shapes with these parameters:
  - e 0.415, w 37.0 deg, i 88.54 deg
  - R1/a 0.0187, R2/a 0.0131, L2/L1 (TESS) 0.074
  - model secondary at phase 0.71359, depth 0.40%
  - With f(M) = 0.0812 Msun, M1 0.76 gives m2 = 0.51 Msun, a = 37.7 Rsun, R1 = 0.70 Rsun and R2 = 0.49 Rsun: a K dwarf with an early-M dwarf, consistent with the Gaia luminosity (M_G 6.08).
  - Impact parameters b_A 0.53 and b_B 0.89, which is why the secondary is grazing and V-shaped.

## Archives (step 1)
- **Catalogues.** VSX, ASAS-SN, SB9, WDS, Prsa+2022, IJspeert+2024 and Kostov+2025 have nothing within 60".
- **SIMBAD** lists the star as SB* only (from Gaia NSS). Gaia vari_summary and vari_eclipsing_binary have no rows.
- **ExoFOP** has no TOI or CTOI (rechecked 2026-10-21).
- **Web search** on the names (TYC, TIC, 2MASS J08210101-6909391) found nothing.
- **Prior detection.** The only prior detection is the unpromoted SPOC TCE pair above. **The star is not catalogued as an eclipsing binary.**
- **Gaia NSS SB1:** P 23.8291 +- 0.0046, e 0.4405 +- 0.0141, w 33.5 +- 2.8, K1 35.68 +- 0.78 km/s.

## Eclipse measurements (step 2; raw QLP SAP, quality==0, untrimmed trapezoid with quadratic baseline)
- **Primary.** 23 fitted.
  - Depth 19.6-23.1% in QLP; the variation is sector dilution (s98 17.6-18.2%; TESS-SPOC 21.5-21.8%).
  - T14 3.27-3.31 h in the 200-s sectors, T12 1.34 h, flat bottom 0.58 h.
  - t0 errors 0.1-0.3 min.
- **Secondary.** 20 fitted.
  - Depth 0.30-0.57% (typically 0.43%).
  - T14 2.3-3.0 h (mean 2.7 h), nearly V-shaped.
  - t0 errors 2-5 min.
- **Background and centroids.**
  - Background drops during the primary (the star's wings fall in the annulus) and never rises. It is flat at the secondaries.
  - Centroid shifts are 3-20 mpx in the primary and under 2 mpx in the secondary.
- **Blind census** (>0.2%, 1-h runs): nothing except sector-start and gap-edge features (s62 2989.0, s63 3014.4, s87 3665.4/3676.0, s98 4002.8-4003.2/4009.4). There is no third dip kind.

## Ephemerides (step 3)
- **Primary (A; K dwarf eclipsed):** BTJD 2089.30214 +- 0.00005 + E x 23.828151 +- 0.0000013 d (chi2 90/21; errors scaled).
- **Secondary (B):** BTJD 2106.30502 +- 0.00091 + E x 23.828156 +- 0.000020 d (chi2 47/17; rms 4.6 min).
- **Secondary phase:** 0.71356 +- 0.00004.
- **e cos w** from the phase is 0.33 at e ~0.42 (Gaia 0.367).
- **Tension with Gaia's w.** At Gaia's e, the phase needs w = 42.0 deg against Gaia's 33.5 +- 2.8 (3.0 sigma on w alone). With e also free, the LC solution e 0.415 / w 37.0 is about 1.8 sigma in e and 1.2 sigma in w. Gaia predicts B - A = 0.7352; the observed value is 0.7136.
- **e sin w.** The light curve alone is bimodal in e sin w:
  - The -0.20 branch has an SSR equal to +0.25 within dchi2 ~1, but needs R1 = 0.46 Rsun and L2/L1 = 0.005. That is unphysical for a 4730 K star with M_G 6.08 and a 0.5 Msun companion.
  - e sin w = 0 is worse by dchi2 ~33.
  - The +0.25 branch agrees with Gaia (e sin w +0.243).
  - The grid run was stopped early. Only -0.20, -0.10, 0.00 and +0.25 were completed (ebgrid.txt, ebgrid_+0.25.png).

## Independence (step 4)
TESS-SPOC SAP, the SPOC DV TCEs and the difference images are listed above. The previous checker's free ebfit.py result (e 0.573, L2/L1 2.6) is void: the optimizer lost the secondary and put it at phase 0.745.

## Next predicted eclipses (BTJD)
| Kind | Epoch | BTJD | Error | UTC |
|---|---|---|---|---|
| Primary | E95 | 4352.9765 | 0.2 min | 2026-11-08 11:26 |
| Primary | E96 | 4376.8046 | 0.2 min | |
| Primary | E97 | 4400.6328 | 0.2 min | |
| Primary | E98 | 4424.4609 | 0.2 min | |
| Secondary | E94 | 4346.1517 | 3.0 min | 2026-11-01 15:38 |
| Secondary | E95 | 4369.9798 | 3.0 min | |
| Secondary | E96 | 4393.8080 | 3.1 min | |
| Secondary | E97 | 4417.6362 | 3.1 min | |

## What would settle it further
- Two or three RV epochs (ground or archival spectra) to tie e and w down. The ~3-sigma tension in w between Gaia SB1 and the eclipse phase is the only loose end.
- A finished e sin w grid with a physically priored L2/L1 (rerun `ebgrid.py ... 0.1,0.15,0.2,0.3,0.35`).
- A spectrum to see whether the M companion is visible (SB2 at K2 ~ 53 km/s).
