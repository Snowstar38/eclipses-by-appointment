import concurrent.futures
import io
import json
import requests
from pathlib import Path
from astropy.io.votable import parse
RA,DEC=257.0919764,86.8219122
P=f"{RA} {DEC}"
R=.05
cone=f"CONTAINS(POINT('ICRS',s_ra,s_dec),CIRCLE('ICRS',{RA},{DEC},{R}))=1"
tap=dict(REQUEST="doQuery",LANG="ADQL",FORMAT="votable")
sql=f"SELECT TOP 50 specObjID,ra,dec,plate,mjd,fiberID,class,survey FROM SpecObjAll WHERE dec BETWEEN {DEC-R} AND {DEC+R} AND ra BETWEEN {RA-1} AND {RA+1}"
jobs={
 'cadc':('https://ws.cadc-ccda.hia-iha.nrc-cnrc.gc.ca/argus/sync',dict(tap,QUERY=f"SELECT TOP 50 obs_collection,obs_id,dataproduct_type,s_ra,s_dec,target_name FROM ivoa.ObsCore WHERE dataproduct_type='spectrum' AND {cone}")),
 'eso_reduced':('https://archive.eso.org/tap_obs/sync',dict(tap,QUERY=f"SELECT TOP 50 obs_collection,obs_id,dataproduct_type,s_ra,s_dec,target_name FROM ivoa.ObsCore WHERE dataproduct_type='spectrum' AND {cone}")),
 'eso_raw':('https://archive.eso.org/tap_obs/sync',dict(tap,QUERY=f"SELECT TOP 50 dp_id,instrument,ra,dec,object,dp_type FROM dbo.raw WHERE CONTAINS(POINT('ICRS',ra,dec),CIRCLE('ICRS',{RA},{DEC},{R}))=1")),
 'lamost_lrs':('https://www.lamost.org/dr12/v2.0/voservice/conesearch',dict(RA=RA,DEC=DEC,SR=R)),
 'lamost_mrs':('https://www.lamost.org/dr12/v2.0/medvoservice/conesearch',dict(RA=RA,DEC=DEC,SR=R)),
 'sdss':('https://skyserver.sdss.org/dr19/SkyServerWS/SearchTools/SqlSearch',dict(cmd=sql,format="json")),
 'elodie':('https://atlas.obs-hp.fr/elodie/E.cgi',dict(a="t",c="ssa",n="ssa",REQUEST="queryData",POS=f"{RA},{DEC}",SIZE=R)),
 'sophie':('https://atlas.obs-hp.fr/sophie/',{}),
 'spectrapointer':('https://astro.gsu.edu/~way/spectra_pointer/',dict(q="1727862804856539264")),
}
def run(item):
 key,(url,params)=item
 try:
  r=requests.get(url,params=params,timeout=(7,15)); content=r.content
  summary=dict(url=r.url,status=r.status_code,bytes=len(content))
  if r.ok and b'<VOTABLE' in content.upper()[:2000]:
   table=parse(io.BytesIO(content))
   summary['info']=[str((i.name,i.value,i.content)) for resource in table.resources for i in resource.infos]+[str((i.name,i.value,i.content)) for i in table.infos]
   summary['tables']=[len(t.array) for t in table.iter_tables()]
  elif r.ok and key=='sdss':
   result=r.json()
   summary['result']=result
  else:
   summary['response_prefix']=r.text[:200]
  Path(f'{key}.response').write_bytes(content)
  return key,summary
 except Exception as exc:
  return key,dict(url=url,params=params,error=f'{type(exc).__name__}: {exc}')
with concurrent.futures.ThreadPoolExecutor(10) as pool:
 results=dict(pool.map(run,jobs.items()))
Path('optical-queries.json').write_text(json.dumps(results,indent=2))
print(json.dumps(results,indent=2))
