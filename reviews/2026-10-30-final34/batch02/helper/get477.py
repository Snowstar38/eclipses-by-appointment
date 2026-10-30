import urllib.request,urllib.parse,concurrent.futures,pathlib
p=pathlib.Path('.');tic='0000000047719859';parts='/'.join(tic[i:i+4] for i in range(0,16,4))
def task(s):
 uri=f'mast:HLSP/qlp/s{s:04d}/{parts}/hlsp_qlp_tess_ffi_s{s:04d}-{tic}_tess_v01_llc.fits'
 try:
  b=urllib.request.urlopen('https://mast.stsci.edu/api/v0.1/Download/file?'+urllib.parse.urlencode({'uri':uri}),timeout=25).read(); (p/f'47719859_s{s:03}.fits').write_bytes(b); return s,len(b)
 except Exception as e:return s,str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=12) as ex:
 for x in ex.map(task,[6,7,8,9,10,32,34,35,59,60,61,62,85,86,87,88]): print(x,flush=True)
