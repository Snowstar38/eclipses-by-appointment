import json,pathlib
R=pathlib.Path(__file__).parent; raw=json.load(open(R/'raw-events.json'))
for tic,r in raw.items():
 data=[]
 for sec in sorted({e['sector'] for e in r['events'] if 'tc' in e}):
  t=tic.zfill(16); parts='/'.join(t[i:i+4] for i in range(0,16,4));uri=f'mast:HLSP/tess-spoc/s{sec:04}/target/{parts}/hlsp_tess-spoc_tess_phot_{t}-s{sec:04}_tess_v1_lc.fits';data.append(dict(provenance_name='TESS-SPOC',sequence_number=sec,dataURL=uri))
 (R/tic/'mast-products.json').write_text(json.dumps({'data':data,'note':'constructed direct TESS-SPOC URI; availability unverified'}))
