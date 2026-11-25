# Reproduce the overview

From the repository root, with Python 3.14:

```sh
python -m pip install -r overview/requirements.txt
python overview/make_overview.py
```

The generator reads `paper.pdf`, `overview/systems.csv` and `overview/a98.json`, then writes `overview.png` (2400 by 1260 pixels). The first page is rendered directly from the current paper at 1785 pixels wide and cropped using the original overview geometry. The sky uses the original equatorial Mollweide projection, with right ascension increasing leftward and a coordinate-aligned NASA sky background. Each dot is one included system; probable systems remain explicitly identified in the subtitle and CSV.

`systems.csv` contains 2,029 unique TICs (1,487 confirmed and 542 probable). The review of Fable’s lower-tier shortlist adds 3 hosts (R1855–R1857). Kounkel et al. (2021) had already classified ten previously counted systems as detached eclipsing binaries. They remain available as physical measurements with their earlier identifications credited. [Current host positions](systems.csv) · [Shortlist review](../reviews/2026-11-24-fable-shortlist/README.md)

The map represents sky position and inclusion only: all dots have the same nominal size and color. It does not represent magnitude, distance, eclipse depth or the strength of evidence, and these quantities are not imputed. Overlapping dots can obscure individual systems. Confirmed and probable describe the physical review tiers; they do not imply a newly discovered binary or uniquely resolved source in every case.

`a98.json` is the unchanged real phase-binned A98 (BD+45 2574 A) light curve from the original overview, over its 3.5-day orbit. The inset and its explanatory annotations retain the original layout. The old caption's raw-measurement count is omitted because it cannot be independently reconstructed from the archived phase-bin arrays. The original broad novelty claim has been replaced with scoped wording. The title includes confirmed and probable systems, not a claim that every system is a newly discovered binary.

Exact pixels depend on the listed library versions and the DejaVu Sans font bundled with Matplotlib. The script fixes dimensions, DPI, fonts and plotting geometry and records no timestamp.

## Sky background and reuse

Bundled unmodified asset: [`milkyway_2020_4k_print.jpg`](milkyway_2020_4k_print.jpg), 1024 x 512 pixels, from [NASA SVS Deep Star Maps 2020, item 4851](https://svs.gsfc.nasa.gov/4851/), [direct download](https://svs.gsfc.nasa.gov/vis/a000000/a004800/a004851/milkyway_2020_4k_print.jpg).

Credit: NASA/Goddard Space Flight Center Scientific Visualization Studio; Gaia DR2: ESA/Gaia/DPAC. This is a real catalogue-derived optical sky visualization, rather than an exposure from one camera. The Milky Way component omits the bright Hipparcos/Tycho foreground stars. Reuse follows [NASA images and media guidelines](https://www.nasa.gov/nasa-brand-center/images-and-media/), which permit educational/informational use of NASA material; the asset has no separate third-party copyright notice. No endorsement is implied.

The source is ICRF/J2000 plate carree, north up, centred on RA 0h, with RA increasing leftward. Each pixel cell is transformed by the same Matplotlib Mollweide projection as the system dots. Rows are reversed to make declination increase upward; no horizontal flip or Galactic-coordinate approximation is used. The displayed RGB is `0.57 * source + 0.43 * original_navy`. Source pixels, star positions and photometry are otherwise unchanged. At the Galactic centre (RA 266.4051 deg, Dec -28.936175 deg), the source location is x=778.9366, y=338.3073 pixels and map longitude is +93.5949 deg; the bright bulge therefore appears in the lower-right, consistent with the transformed Galactic plane. The source resolution is adequate for this subdued 1272-pixel-wide panel.

Source SHA-256 (checked by the generator): `1ebe95804f5f0e6e23f77488aaa33fdb4aaef3fd336821fb41b261ddeaee2df0`.
