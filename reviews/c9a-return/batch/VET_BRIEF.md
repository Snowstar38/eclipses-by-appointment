# Vet brief: adversarial check of chunk-9 (c9a) eclipse candidates

You are an independent checker. Your job is to try to break the claim that the star is an
eclipsing binary at the Gaia spectroscopic period, using your own code, from raw flux. The
discovery pipeline (a BLS fold of flattened QLP data around the Gaia period) is NOT evidence
here; you re-derive everything. The standard is the paper's Section 2.5 protocol. Confirmed
means every check the data allow passed:

1. repeated events re-measured from raw (SAP, QUALITY==0) flux, individually, not just in a fold;
2. a period from the eclipses themselves, compared with Gaia's period and error;
3. a difference image (in-eclipse minus out-of-eclipse) placing the deficit on the target
   against every neighbour bright enough to produce it (dilution arithmetic);
4. at least one independent pipeline agreeing on depth (QLP vs TESS-SPOC vs your own TESScut
   aperture photometry; 2-min SPOC where it exists);
5. a geometry consistent with Gaia's orbit (eclipse phase vs predicted conjunctions; secondary
   phase vs e cos omega).

Probable = eclipses real and repeating but one check missing or failed. Plausible = a single
event, or two with the period untested. Refuted = signal is on a neighbour, or is not an eclipse.
Open = you could not decide; say what would decide it. Say which tier and which checks, exactly.

## Working rules
- Write your own code. Save every script and every numeric output in your vet folder
  (`[local path omitted]`). Every number in REPORT.md must be
  pasted from a named output file in that folder. Plots are welcome but keep them small (PNG,
  <= 150 dpi); do NOT open more than ~6 images yourself, and never a montage of many panels.
- Downloads go under the scratchpad data directory given in your prompt, one subfolder per TIC.
  Delete TESScut cubes when you are done with them (they are tens of MB each). Do not download
  2-min target pixel files unless the star has 2-min data and you need it.
- Do not edit anything in the repository outside your vet folder. Do not commit.
- Numeric prior scores from the roster are context only. Trust nothing you did not measure.
- If a check is impossible with the data, say so rather than skipping silently.

## Data access that works from this machine (tested)
- Light curves: `lightkurve` imports fine.
  `lk.search_lightcurve('TIC <id>', author=['QLP','TESS-SPOC']).download_all(download_dir=...)`.
  QLP columns: sap_flux, kspsap_flux (detrended; avoid for depths), quality. TESS-SPOC: sap_flux,
  pdcsap_flux. Use SAP with QUALITY==0 for measurements; detrended columns suppress long eclipses.
  2-min SPOC (`author='SPOC'`) exists only for some stars (see targets.csv spoc2min_sectors).
- Pixels: `lk.search_tesscut(SkyCoord(ra, dec, unit='deg')).download(cutout_size=11, download_dir=...)`.
  Pass COORDINATES, not a name: the name resolver lightkurve uses runs over plain http, which
  this machine cannot reach. `astroquery.mast.Tesscut.get_cutouts(coordinates=..., size=11)` also works.
- Gaia DR3 (gaia_source, nss_two_body_orbit): the ESA TAP times out; use the Heidelberg mirror,
  POST to https://gaia.ari.uni-heidelberg.de/tap/sync with REQUEST=doQuery, LANG=ADQL,
  FORMAT=csv, QUERY=<ADQL>. nss_two_body_orbit.t_periastron is days from J2016.0, so
  BTJD = t_periastron + 389.0. Conjunction A is at true anomaly nu = 90 - omega, conjunction B at
  nu = 270 - omega (omega = arg_periastron of the primary, degrees). Propagate P, T_p, e, omega
  errors by Monte Carlo (e.g. 20000 draws) when comparing predicted and observed eclipse phases.
  The orbit row for your stars is already in targets.csv (gaia_* columns); re-query only if you
  need more columns.
- VizieR: the CDS hosts reset connections. Use the mirror https://vizier.idia.ac.za, e.g.
  `https://vizier.idia.ac.za/viz-bin/asu-tsv?-source=B/vsx/vsx&-c=<ra>%20<dec>&-c.rs=60&-out.all`
  (plain GET with requests or curl; astroquery's Vizier class failed against this mirror).
  Catalogues to cone: B/vsx/vsx (VSX, 60"), J/ApJS/258/16 (Prsa+2022 TESS EBs), J/A+A/652/A120
  (IJspeert+2021 OBAF EBs), I/358/veb (Gaia DR3 eclipsing binaries), I/357/varisum (Gaia
  variability summary), B/sb9/main (SB9). Also try the all-catalogue query (`-source=` omitted,
  `-c.rs=5`) to list any table with a row within 5"; verify it returns rows for a known object
  before trusting an empty result.
- SIMBAD: use the mirror simbad.harvard.edu (e.g.
  `https://simbad.harvard.edu/simbad/sim-id?Ident=TIC%20<id>&output.format=ASCII` or sim-coo
  with Coord=<ra>%20<dec>&Radius=10&Radius.unit=arcsec). Record object type and bibcode count.
- ExoFOP: `https://exofop.ipac.caltech.edu/tess/target.php?id=<tic>` (HTML; look for TOI/CTOI).
- ZTF (resolves neighbours at 1-2"): IRSA light-curve API,
  `https://irsa.ipac.caltech.edu/cgi-bin/ZTF/nph_light_curves?POS=CIRCLE%20<ra>%20<dec>%200.0014&BANDNAME=g,r&FORMAT=csv`.
  Use it when a neighbour within ~30" could supply the signal (these targets are T ~ 12, so ZTF
  should have them if Dec > -30).
- AAVSO VSX web API is behind Cloudflare (403); use the VizieR copy of VSX instead.
- ADS: no API token. Use WebSearch on the star's names for a brief literature check only.

## What to measure, per star
1. Archives: VSX / Gaia-EB / Prsa / IJspeert / SB9 cones, SIMBAD type, ExoFOP. State plainly
   whether the star is already a catalogued ECLIPSING binary (a known spectroscopic binary is
   expected: the sample is Gaia SB1 orbits). Give separations.
2. Raw light curves: download all QLP and TESS-SPOC sectors. With SAP QUALITY==0, find every
   individual eclipse event: mid-time, depth (fraction, local linear or quadratic baseline),
   duration T14 (and T23 if resolved), which pipeline(s) see it. Tabulate. Note events lost to
   gaps or flagged data.
3. Period from the eclipses alone (linear fit to primary mid-times; secondaries too), with
   error; compare to Gaia's P and error in sigma. Odd/even depth comparison at the eclipse
   period and at twice it (a P2 candidate's "primary" may be two eclipse kinds stacked).
4. Pixels: for at least two events in at least two sectors (different orientations if
   available), build the difference image from the TESScut cube (median in-eclipse minus median
   out-of-eclipse), find the deficit centroid and its offset from the target in arcsec
   (21"/pixel), and for every Gaia neighbour within 90" with G < 18 (neighbours_90as.csv)
   compute the intrinsic depth it would need given its flux fraction in your aperture. Say which
   neighbours are arithmetically excluded and which are not.
5. Independence: depths per sector from QLP SAP, TESS-SPOC SAP and your own TESScut aperture
   photometry; agreement within errors? Include 2-min SPOC if it exists.
6. Geometry: measured secondary phase vs the value Gaia's e and omega predict; absolute phase of
   the primary vs Gaia conjunctions A and B at the TESS epoch, with Monte-Carlo errors. Say which
   conjunction the primary is if the data decide it. Rough physical sanity check of depths and
   durations against TIC radius/Teff and Gaia K1.
7. Ephemeris: P, T0 (BJD_TDB and BTJD) with errors, and the next three primary eclipses in UTC
   (say whether you applied the barycentric light-time correction).
8. Common mode (if time allows): a few other QLP stars in the same sector/camera at the event
   times, to show the dip is not a sector-wide systematic.

## REPORT.md shape (house style; an excerpt of an existing report is in your prompt)
- Title: `# vetNN: adversarial check of TIC <id> (<name>) [and TIC <id2> (<name2>)]`
- One paragraph: who/when/for whom, where files are.
- **Verdict** per star in bold: CONFIRMED / PROBABLE / PLAUSIBLE / REFUTED / OPEN, then the
  checks passed and failed, one sentence each. If the by-eye screen got something wrong (depth,
  period, which eclipse is primary, a missed event), say so explicitly.
- `## 1. Archives and web`, `## 2. Independence, systematics, pixels`, `## 3. TIC <id>`
  (table: Event | Mid BTJD | Depth | T14/T23 | pipelines), `## 4. TIC <id2>`,
  `## Geometry vs Gaia`, `## Ephemerides and next eclipses`, `## Caveats`, `## Files`.
- Units: depths in % or ppt (say which), times as BTJD = BJD_TDB - 2457000, durations in hours.
- Concrete and quantitative. No padding. No novelty claims beyond what your cones show ("not in
  VSX/Gaia-EB/Prsa/IJspeert within X arcsec" is the right phrasing).

Final message: the full REPORT.md text (also saved in your folder), then one line per star:
`TIC <id>: <TIER>; P_ecl=<...> d; depth1=<...>; depth2=<...> at phase <...>; pixel: <on target /
neighbour / untested>; pipelines: <n>; Gaia geometry: <pass/fail/untestable>`.
