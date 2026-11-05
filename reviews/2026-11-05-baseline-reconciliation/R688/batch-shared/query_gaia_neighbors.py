import json,math
from pathlib import Path
from astropy.io.votable import parse_single_table
H=Path(__file__).parent
ra,dec=329.7472812178442,61.66216426711785
source=H/'gaia-photometry-source.xml'
rows=parse_single_table(source).to_table()
assert len(rows)==88
out=[]
for x in rows:
    sep=math.hypot((float(x['ra'])-ra)*math.cos(math.radians(dec)),float(x['dec'])-dec)*3600
    if x['phot_g_mean_mag'] is None or str(x['phot_g_mean_mag'])=='--':continue
    G=float(x['phot_g_mean_mag'])
    fr=10**(-.4*(G-7.008101));req=0.0003*(1+fr)/fr
    out.append(dict(source_id=str(x['datalinkID']),sep_arcsec=sep,G=G,required_intrinsic_fraction_for_300ppm_blended_loss=req,capable=req<=1))
out.sort(key=lambda z:z['sep_arcsec'])
target=[x for x in out if x['source_id']=='2204160934098817280']
assert len(target)==1
neighbors=[x for x in out if x['source_id']!='2204160934098817280']
info=dict(query_url='https://gaia.aip.de/conesearch/api/gaiadr3.gaia_source/?RA=329.7472812178442&DEC=61.66216426711785&SR=0.0166666667',target_source_id='2204160934098817280',target_G=7.008101,assumed_blended_depth_ppm=300,cone_radius_arcsec=60,raw_row_count=len(out),capable_neighbor_count=sum(x['capable'] for x in neighbors),neighbor_capability_note='Gaia G proxy for TESS flux, full throughput assumed; required intrinsic fraction is optimistic lower bound. No target or neighbor loss is demonstrated by this test.',target=target[0],neighbours=neighbors)
(H/'gaia-neighbors.json').write_text(json.dumps(info,indent=2)+'\n')
print(json.dumps(info,indent=2)[:4000])
