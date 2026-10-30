TIC 356308234 (TYC 3519-1236-1, Gaia DR3 1364083026255543936) - adversarial check, 2026-10-21

VERDICT: CONFIRMED. A detached, slightly eccentric EB, P = 42.86016 d: G subgiant (~1.0 Msun, 1.47 Rsun) + K dwarf
(~0.73 Msun, 0.78 Rsun) at i ~ 90 deg. The eclipses are on the target, and the orbit agrees with the Gaia SB1 orbit to
<=1.1 sigma in every element. Not catalogued as an EB, but not quite unknown: it is WASP0-TR-06 in Kane et al. 2005
(MNRAS 364, 1091). There it is a single partial "transit" from the 2000 Draco-field run: depth 13.2%, egress and bottom
missed, spurious P = 6.03 d, rejected as a planet (companion 3.9 R_J). Nothing since identifies it as an EB or gives
the real period.

1 ARCHIVES (2026-10-21)
- cats.py (60"): nothing in VSX, ASAS-SN, Prsa22, IJspeert24 or Kostov25 t2/t3/t4. SIMBAD has SB* only.
- VizieR cones (60"): 0 rows in ZTF-periodic, ATLAS, ASAS-SN II/366, WISE vars, VSX, SB9, WDS, ACVS, KELT,
  Justesen21 and the TESS OBA EBs. The J/A+A/674/A16 cone hit an unrelated table; the direct Gaia query below is
  the one that counts.
- Gaia DR3 vari_classifier/summary/eclipsing_binary/rotation/LPV: all empty. The NSS solution is SB1: P 42.874 +- 0.013,
  e 0.091 +- 0.012, w 23.2 +- 9.6, K1 30.94 +- 0.40 km/s.
- ExoFOP: no TOI or CTOI. ZTF light curve: 0 rows.
- SIMBAD ids include WASP0-TR 06; refs are 2005MNRAS.364.1091K and Gaia DR3. No epoch was published for the WASP0
  event, so it cannot be phased.
- Web search on the TYC and TIC names: nothing.

2 ECLIPSES (QLP SAP_FLUX, q==0, untrimmed)
14 events. Trapezoid (ecl.py) and mirror-symmetry (ecl2.py) mid-times agree to <=0.1 min (1 min in s14).
 sec kind  t0 BTJD      +-min depth  T14trap  W50
 14  P  1689.14172  0.4  25.8%  10.14h  6.54h
 26  S  2012.72988  0.3  15.3%  11.26   7.76
 26  P  2032.02385  0.3  26.5%  10.14   6.53
 40  S  2398.47104  0.3  15.2%  11.39   7.79
 40  P  2417.76502  0.2  26.5%  10.21   6.51
 51  S  2698.49240  0.3  15.3%  11.33   7.82   (21/72 flagged within 6 h; the allq fit is the same)
 53  P  2760.64591  0.2  26.6%  10.15   6.54
 54  S  2784.21249  0.3  15.2%  11.27   7.74
 74  P  3317.82795  0.3  26.9%  10.16   6.50
 78  P  3446.40862  0.3  26.4%  10.16   6.48
 79  S  3469.97518  0.4  15.1%  11.34   7.84
 80  P  3489.27065  0.3  26.9%  10.15   6.54   (background bump on ingress; +2.3 min O-C)
 81  S  3512.83488  0.4  15.2%  11.32   7.69
 81  P  3532.12854  0.3  26.7%  10.16   6.48
- Shapes: P has a rounded (limb-darkened) bottom, an annular transit. S is flat-bottomed (~4.3 h), a total
  occultation. Ingress is 3.5 h in both.
- Background: within +-2 sigma everywhere except s40 S, where it is 5 sigma lower (a trend; would brighten, not dim).
  Centroid shifts are 5-30 mpx with no consistent direction.
- Census: unmasked at 3%, it finds exactly these 14 events. Masked at 0.3%, only orbit-edge features remain (s14 1695.9
  and the end of the sector).

3 EPHEMERIDES AND ORBIT
- P: T0 = 1689.14215 +- 0.00057, P = 42.860164 +- 0.000019 d. chi2 90/6, errors scaled. O-C rms 1.0 min, driven by s80.
- S: T0 = 1712.70878 +- 0.00020, P = 42.860150 +- 0.000008 d, chi2 2.6/4.
- Against Gaia: 42.87429 +- 0.01282 (-1.1 sigma). P falls at Gaia conjunction A (companion in front) and S at B. With
  the full covariance every event is -0.7 to -1.1 sigma early (the period mismatch accumulating). S phase is 0.54985
  against Gaia's 0.5524 +- 0.0079.
- EB model (ebfit2; the 200-s and 600/1800-s data give the same answer):
  ecosw 0.0783, esinw 0.048 (+-~0.005 syst), e 0.092, w 31.5 deg, i 89.9-90, R1/a 0.0237, R2/a 0.0126, J 0.63, L2/L1 0.18.
- Against Gaia: ecosw 0.082 +- 0.012 (0.3 sig), esinw 0.035 +- 0.015 (0.9 sig), w 23.2 +- 9.6 (0.9 sig).

4 INDEPENDENCE
- TESS-SPOC SAP/PDCSAP (s14, s26, s40, s81) and TASOC (s14, s26): same times within 0.3 min (1-2 min in s14) and same
  depths. The SPOC s81 primary is flagged from 3532.3 on (end of sector), but the raw minimum is 0.743.
- TESScut difference images (s40, s81, both kinds): deficit centroid within 0.1-0.2 px of the target. Depth 26%/15% on
  the target pixel, <=0.7% at the G 12.5 neighbour (82").
- No Gaia star within 60" is brighter than G 16.2; a neighbour would need a depth of >2700%.
- Conclusion: contamination is excluded.

5 PHYSICS
- f(m) = 0.130 +- 0.005 Msun. M1 = 1.0 gives m2 = 0.73, a = 61.9 Rsun, R1 = 1.47, R2 = 0.78, K2 = 42 km/s. M1 = 1.2
  gives m2 = 0.81.
- J = 0.63 means T2 ~ 4700 K, a K dwarf.
- At A the K dwarf transits the G star (27%, annular). At B the G star occults the K dwarf (flat; depth = L2 fraction
  0.152, which matches the measured 15.2%).
- Predicted central T14 with Gaia e, w: A 11.4 h, B 12.3 h. The model gives 11.3 and 12.4 h.
- Everything fits one geometry.

6 NEXT ECLIPSES (BTJD)
- P (A, 27%): 4346.4723, 4389.3325, 4432.1926, 4475.0528 (+-1.9 min)
- S (B, 15%): 4370.0381, 4412.8982, 4455.7584, 4498.6185 (+-0.8 min)

FURTHER
- Settled as an EB on the target. What would add most: SB2 spectroscopy for absolute masses (a totally eclipsing
  G+K benchmark), fits with free limb darkening and third light, a check of the s80 timing and any ETVs, and the
  WASP0/SuperWASP archive epochs to extend the baseline.
