"""Fetch G photometry by indexed IDs found in the Gaia cone receipt."""
from pathlib import Path
import requests
from astropy.io.votable import parse_single_table
H=Path(__file__).parent
ids=[str(x['datalinkID']) for x in parse_single_table(H/'gaia-neighbors-source.xml').to_table()]
assert len(ids)==len(set(ids)) and len(ids)<100
q='SELECT source_id,ra,dec,phot_g_mean_mag FROM gaiadr3.gaia_source WHERE source_id IN ('+','.join(ids)+')'
r=requests.get('https://gaia.aip.de/tap/sync',params={'REQUEST':'doQuery','LANG':'ADQL','QUERY':q},timeout=30)
r.raise_for_status()
(H/'gaia-photometry-source.xml').write_bytes(r.content)
print(len(ids),len(r.content),r.text[:100])
