# Two published eclipse hosts in neighbouring TESS apertures

| Fable aperture | Proposed source | Offset from aperture | Period measured in aperture (d) | Earlier source and period (d) |
|---|---|---:|---:|---|
| TIC 99572538 | TIC 99572535 | 48.21″ | 2.39247350 | Gaia DR3 1111551490556587264, 2.39243823. VSX EA XOSS-V J071039.86+715302.3, 2.394740. |
| TIC 300987559 | TIC 300987437 | 40.68″ | 3.99492767 | Kostov et al. table 4, 3.994690. Gaia DR3 4321133168808401024, 3.99470832. VSX EA WISE J192013.4+163701, 3.9942971. |

The VizieR positions of the VSX systems are 0.04″ and 0.09″ from the proposed Gaia sources, respectively. Each source has a published eclipsing-binary identification and a matching period. Both proposed hosts therefore remain outside the additions count. [Electronic comparison records](position-and-id.json) · [Controlled catalogue queries](../ffi/catalogue-screen.json) · [Proposed neighbours](../ffi/reassignments.json)

Xingming Observatory credits Guoyou Sun, Kai Li, Difu Guo, Zhijian Xu and Xing Gao with discovering XOSS-V J071039.86+715302.3 on 20 February 2020. Its account records subsequent classification as an Algol-type eclipsing binary in VSX. For TIC 300987437, Kostov and colleagues give the TESS period in their table of previously known eclipsing binaries. [Xingming Observatory 2020 activity register, item 40](https://xjltp.china-vo.org/2020.html) · [Kostov et al. table 4, TIC 300987437](https://vizier.cds.unistra.fr/viz-bin/VizieR?-source=J/ApJS/279/50/table4&TIC=300987437)

We checked both proposed source positions, TICs and Gaia identifiers against 798 distinct stars in 19 of Théo Chopard-Vilhem's released and working tables. The nearest survey stars lie 18.40° and 7.55° away, respectively. The local comparisons additionally cover the project catalogue, both published IJspeert eclipse lists, Prša's TESS eclipse list, Tang's 514 TICs and a 280-system spectroscopic eclipse table. SIMBAD classifies both sources as eclipsing binaries and lists the Gaia DR3 eclipse paper. The ADS exact-name full-text searches and the Villanova TIC search returned no entries for the aliases tested. [TIC 99572535 bibliography](99572535-bibliography.json) · [TIC 300987437 bibliography](300987437-bibliography.json)

Run `python compare.py local` and `python compare.py literature` from this directory to rebuild the local comparisons and query the bibliography. Both use the periods measured in the original TESS apertures.
