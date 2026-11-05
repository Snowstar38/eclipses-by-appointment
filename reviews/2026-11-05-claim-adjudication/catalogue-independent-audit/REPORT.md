# Independent cached literature audit - 49 exact identities

All 49 locked queue TIC and Gaia DR3 IDs were checked individually; `exact-results.csv` and `exact-results.json` retain all rows, source paths, hashes and matching output. No exact matches were found in these sources. This audit does not establish full catalogue clearance or exhaustive priority, and does not extend a result from one subset to another.

* Prsa 2022: complete cached MAST 4,584-row catalogue matched on tess_id. Receipt: `[local path omitted]`.
* IJspeert 2024: cached 69,057-row published identity table matched on TIC or Gaia DR3. Receipt: `[local path omitted]`.
* Tarrants & Mendes: cached primary HTML Table 2 exact Gaia scan plus previous same-parent crossmatch with both IDs checked. Primary HTML and crossmatch hashes are in `tarrants-mendes-overlaps.json`; crossmatch alone is not assumed exhaustive for new targets.
* Callahan 2025: cached arXiv source 112-row full table parsed for TIC; eight additional heartbeat papers scanned for exact TIC-number tokens. Their hashes and matching scope are in `heartbeat-overlaps.json`. OGLE/KIC-only identities remain untested by this token search.
* Chopard-Vilhem public v1.2.0: exact TIC/Gaia match against track3_detail and vetting/dossier, with scope and hashes in `chopard-overlaps.json`. Later releases and embargoed identities are not covered.

Matches use exact identity only; this audit did not independently perform positional neighbor searches, current VSX, ASAS-SN, Gaia, SIMBAD or Kostov gates. Source association and prior blends require separate evaluation. The catalogue lead owns final per-target coverage and disposition.
