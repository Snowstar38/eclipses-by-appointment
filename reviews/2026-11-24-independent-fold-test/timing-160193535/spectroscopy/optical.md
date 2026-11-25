# Optical spectroscopy scout for TIC 160193535

Public optical archives queried around the Gaia counterpart at ICRS 257.0919764°, +86.8219122° yielded no verified matching optical spectrum. MAST's TIC lookup identifies Gaia 1727862804856539264, 2MASS J17082229+8649188, TYC 4655-00003-1, UCAC 885-003206 and AllWISE J170822.14+864918.9. The TIC row contains no SDSS name. [MAST TIC service](https://mast.stsci.edu/)

| Archive | Programmatic result |
| --- | --- |
| LAMOST DR12 v2.0 LRS and MRS | Both 3 arcmin cones returned HTTP 200, a valid VOTable with QUERY_STATUS OK, and zero rows. |
| ESO public raw and reduced archives | The coordinate box RA 256.0919764°–258.0919764°, Dec +86.7719122°–+86.8719122° returned zero raw observations and zero reduced spectra. Both results have QUERY_STATUS OK. This is a search of recorded centers. |
| OHP ELODIE | Registered HTTP SSAP 3 arcmin cone returned Successful Search and zero rows. |
| OHP SOPHIE | Native HTTP searches at 17 08 22.074 +86 49 18.884 returned only the query header for both the spectra and CCF tables. The service describes the search as a 3 arcmin box. |
| CADC | Three TAP queries, including a CAOM2 spectral footprint query, timed out. Coverage remains unverified. |
| SDSS optical SkyServer DR19 | Production and preproduction SpecObjAll SQL endpoints timed out. Optical coverage remains unverified by this check. |
| MAST mission observation cone | The request timed out. Archival HST optical spectroscopy remains unverified. |

Instrument and survey archives were searched by sky position to avoid relying on target names. Positions, queries and response summaries are in optical-queries.json and optical-retries.json. Successful LAMOST, ESO and OHP responses are retained alongside the report. These searches cover public metadata and the stated search regions. SDSS-V/APOGEE is being checked separately.

- [LAMOST DR12 v2.0](https://www.lamost.org/dr12/v2.0)
- [ESO archive programmatic access](https://archive.eso.org/programmatic/)
- [ELODIE registered search](https://dc.g-vo.org/rr/q/lp/custom/obs-hp.fr/elodie/ssa)
- [SOPHIE archive](http://atlas.obs-hp.fr/sophie/)
- [CADC TAP](https://www1.cadc.hia.nrc-cnrc.gc.ca/en/doc/tap/)
