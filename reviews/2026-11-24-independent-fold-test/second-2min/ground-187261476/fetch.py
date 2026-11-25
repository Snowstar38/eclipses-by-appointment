import requests,pathlib
p=pathlib.Path(__file__).resolve().parent
url='https://irsa.ipac.caltech.edu/cgi-bin/ZTF/nph_light_curves';par={'POS':'CIRCLE 72.6639595885975 40.85798381916 0.0006','BANDNAME':'g,r','FORMAT':'csv','BAD_CATFLAGS_MASK':'32768'}
r=requests.get(url,params=par,timeout=50);print(r.status_code,r.url,len(r.content),r.text[:500]);(p/'ztf_response.txt').write_bytes(r.content)
try:
 from pyasassn.client import SkyPatrolClient
 a=SkyPatrolClient(verbose=False);o=a.cone_search(ra_deg=72.6639595885975,dec_deg=40.85798381916,radius=4,units='arcsec',catalog='master_list',download=True,threads=1)
 print('ASASSN',len(o.data));o.data.to_csv(p/'asassn.csv',index=False)
except Exception as e:print('ASASSN error',repr(e))
