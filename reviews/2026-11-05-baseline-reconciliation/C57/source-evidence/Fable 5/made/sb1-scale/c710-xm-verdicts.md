# Chunks 7–10 deep x-match: verdicts (2026-11-02, 21:30 session)

The owed batch item, fourth session: 10″ x-match of all 229 c7–c10
candidates against VSX, Gaia DR3 vari classification, ZTF periodic
variables, ATLAS, and ASAS-SN variables. CDS and its XMatch API still
down (4th session); ran as per-candidate multi-catalogue cones on the
**vizier.idia.ac.za** mirror (VSX version 2026-10-18; ASAS-SN table is
`II/366/catv2021` there, not `catalog`). Control: RR Lyr through the
same code path matched VSX + Gaia vari before the run.

Receipts: `c710_xm.py` → `c710-xm-out.txt` (229 queried, 0 failed, 66
tics with ≥1 match, 548 s), raw rows `c710-xm.json`, triage
`c710_xmtriage.py` → `c710-xm-triage.txt` (8 period-locked flags).

## Strikes — previously catalogued eclipsers (same star)

| TIC | chunk | prior record | sep | period |
|---|---|---|---|---|
| 195865529 | 9 | ASAS-SN AP14046259, **EA P 3.8310 d** (+ ATLAS DBH at P/2) | 0.16″ | ours 3.83104 — ratio 1.0000 |
| 295771108 | 7 | ASAS-SN AP47351549, **EA P 3.5059 d** | 3.10″ | ours 1.75296 = P/2 |
| 377389892 | 7 | VSX ASASSN-V J104558.09+574951.0, **EA P 1.147 d** | 0.02″ | ours 4.58817 = 4.0001×P (VSX period likely a quarter alias) |
| 66072136 | 7 | VSX **V0693 Lac, EA P 1.08916 d** | 0.03″ | ours 4.5892 (ratio 4.21, not locked — VSX period suspect) |

195865529 is the one nobody had: not in VSX, not in the five vetted EB
tables (the chunk-9 join found only 300903537), outside Astra's reviewed
G range. It was only ever in ASAS-SN's own variable catalogue and ATLAS.
The other three match Astra's independent review exclusions exactly
(CATALOGUE.md campaign paragraphs, R217–R675): same three TICs, same
reading. Counts: chunk 7 126 → **123**, chunk 9 18 → **17**; chunks 8
and 10 unchanged.

## Annotations — star previously catalogued, eclipse claim unaffected

- **407207285 (c7)**: VSX+ASAS-SN **ROT P 6.4067 = ours/2 exactly**
  (12.81472/2 = 6.40736). The catalogued "rotation" is most plausibly
  the double-wave spot/ellipsoidal signal of the synchronized binary —
  type-revision prospect, the 448581731 pattern.
- **311398753 (c7)**: VSX ROT 14.75 d ≈ ours 15.044 (2%); Gaia RS.
  Near-synchronous spots; eclipse new.
- **402940895 (c9)**: ASAS-SN ROT 69.89 d — the already-measured 69.9-d
  spot rotation in the promotion row; Gaia RS. Consistent, nothing new.
- **462088261 (c10)**: VSX + Gaia RS (no period). Known active star;
  the 17.52-d eclipse is new — type-revision prospect.
- 14 further same-star VSX ROT / Gaia SOLAR_LIKE or RS matches (c7:
  29114881, 91614687, 169318948, 246857844, 305826287, 349452680,
  351610379, 392794270; c8: 58825156, 73248723, 150162108, 176048490,
  237092634, 287756198, 269506784; c9: 36083554, 92881948) — spotted
  rotators with no eclipse record, periods absent or unrelated.
- VSX "VAR" rows with P 0.015–0.086 d are Gaia short-timescale
  variability flags, not period claims; ATLAS "dubious"/NSINE/IRR rows
  carry no credible period. Harmless.
- 187202091 (c10): only ATLAS "dubious", no period. The promotion
  stands untouched.

## Instrument note

The mirror caps the *all-catalogue* cone (`asu-tsv`, no `-source`) at
exactly 90,112 bytes — deterministic across clients and retries, so a
catch-all null on idia is **not** a null (an RR Lyr control returned 1
flagged table where CDS-era vizall returned dozens). Named-table cones
are not affected. Anything needing the catch-all still waits for CDS.
