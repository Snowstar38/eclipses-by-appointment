# Shared catalogue audit: fixed T001–T100 queue

The queue SHA256 is `10b79b38ba30b0718fe1b2a4833060e2257836baf2d730bae98ab598870f64ff`. `TARGET-STATUS.csv` and `target-evidence.json` cover every fixed identity in order. No row is a novelty clearance or a physical verdict. The four VizieR gates (VSX, ASAS-SN II/366, Kostov table 3, Kostov table 4) are **UNKNOWN for all 100**: one known-source VSX positive control timed out at CFA Harvard and one bounded alternate timed out at CDS Strasbourg. Neither failure is a nonmatch. No 400-cone query storm followed.

The complete cached Prša table (4,584 rows) and IJspeert identity table (69,057 rows) were checked by exact TIC/Gaia ID and spherical 5-arcsecond cones. Neither has a match for this queue. IJspeert's local identity table omits its science columns. Six prior review result files, the accepted ledger, pending list, and `sky/CATALOGUE.md` were checked by exact TIC token; these are historical alerts, not current physical classifications. Verified target-specific successful old VizieR receipts: zero. Cached Callahan and eight other heartbeat sources were checked by exact TIC token (OGLE/KIC-only aliases remain outside that scope). Public Chopard v1.2.0 was checked by Gaia/TIC in two tables (later or embargoed identities remain unknown). Tarrants–Mendes was checked using the same-parent crossmatch and exact Gaia ID in the primary HTML table.

Five rows need prior-source interpretation:

| Sample | TIC | Alert and scope |
|---|---:|---|
| T074 | 435855781 | `sky/CATALOGUE.md` records an earlier SuperWASP EA/EB and local period revision. |
| T083 | 271053559 | `sky/CATALOGUE.md` records a prior local plausible target eclipse/precession investigation. |
| T085 | 122980411 | `sky/CATALOGUE.md` says the 4.24-day EB belongs to the 17-arcsecond neighbor HJ 68 B, not the queued target. |
| T086 | 398402989 | Public Chopard v1.2.0 dossier explicitly records eclipses in 4/7 conjunction windows; exact Gaia ID. |
| T091 | 420645189 | Tarrants–Mendes primary table exact Gaia row says EB; `sky/CATALOGUE.md` identifies TOI-1897 as an already retired EB. |

One bounded exact-Gaia bulk query per Gaia DR3 `vari_eclipsing_binary`, `vari_summary`, `nss_two_body_orbit`, and SIMBAD succeeded. Gaia EB returned zero rows; variability summary 17; NSS 103 orbit rows (orbits are not prior eclipse IDs); SIMBAD 100 exact identifier rows. Raw CSVs and request/response hashes are retained in `bulk-remote-receipts.json`. Two bounded Gaia DR3 `gaia_source` cone queries supply 120-arcsecond neighbors, G, coordinates and angular separations for all 100 targets in `gaia-neighbors.json`. G flux ratio is approximate and bandpass dependent; those rows alone cannot attribute an eclipse or rule out a brightening.

`verify.py` checks queue identity/order, all 100 statuses, source hashes, remote response hashes, the neighbor receipt scope and the four unknown gates. `verification.json` records the pass. The audit leaves the sample unchanged and makes no manuscript or claim-count change.
