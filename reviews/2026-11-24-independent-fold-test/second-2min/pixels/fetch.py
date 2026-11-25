import requests,pathlib
p=pathlib.Path(__file__).resolve().parent; root='https://stpubdata.s3.us-east-1.amazonaws.com/tess/public/tid/s0059/0000/0001/8726/1476/'
for suffix in ['tp','lc']:
 url=root+f'tess2022330142927-s0059-0000000187261476-0248-s_{suffix}.fits'; r=requests.get(url,timeout=90);r.raise_for_status(); (p/f'{suffix}.fits').write_bytes(r.content);print(suffix,len(r.content),url)
