# Reproduce the overview

From the repository root, with Python 3.14:

```sh
python -m pip install -r overview/requirements.txt
python overview/make_overview.py
```

The generator reads `paper.pdf`, `overview/systems.csv` and `overview/a98.json`, then writes `overview.png` (2400 by 1260 pixels). The first page is rendered directly from the current paper at 1785 pixels wide and cropped using the original overview geometry. The sky uses the original equatorial Mollweide projection, with right ascension increasing leftward and the Galactic plane shown for orientation. Each dot is one included system; probable systems remain explicitly identified in the subtitle and CSV.

`systems.csv` includes the original 199 active A systems and every current scientific review register row marked `count_addition=true`. Rows are joined by exact TIC identifier to the real TIC coordinate metadata; identifiers are unique and no coordinates are imputed. The generator validates IDs, tiers and coordinate ranges, and refuses to render if the paper first-page headline count differs from the CSV row count. `provenance.json` records source hashes and the complete inclusion count; source aliases avoid exposing local filesystem information.

`a98.json` is the unchanged real phase-binned A98 (BD+45 2574 A) light curve from the original overview, over its 3.5-day orbit. The inset and its explanatory annotations retain the original layout. The old caption's raw-measurement count is omitted because it cannot be independently reconstructed from the archived phase-bin arrays. The original broad novelty claim has been replaced with scoped wording. The title includes confirmed and probable systems, not a claim that every system is a newly discovered binary.

Exact pixels depend on the listed library versions and the DejaVu Sans font bundled with Matplotlib. The script fixes dimensions, DPI, fonts and plotting geometry and records no timestamp.
