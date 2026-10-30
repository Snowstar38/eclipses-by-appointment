import pathlib,json,hashlib,csv
from astropy.io import fits
B=pathlib.Path('.');raw=json.load(open(B/'raw-evidence/raw-events.json'));q=json.load(open(B/'raw-evidence/qlp-results.json'));T=json.load(open(B.parent/'targets-selected.json'));out={}
for tic,r in raw.items():
 with fits.open(r['source_cutout']) as h: hdr=h[0].header; ext=h[1].header; sec=hdr.get('SECTOR',ext.get('SECTOR')); ra=hdr.get('RA_OBJ',ext.get('RA_OBJ')); dec=hdr.get('DEC_OBJ',ext.get('DEC_OBJ'))
 out[tic]={'cutout_sector_header':sec,'cutout_ra_header':ra,'cutout_dec_header':dec,'target':T[tic],'qlp_tic_matches':int(q[tic]['header_TICID'])==int(tic),'qlp_sector_matches':q[tic]['header_SECTOR']==r['sector'],'cutout_sha_matches':hashlib.sha256(pathlib.Path(r['source_cutout']).read_bytes()).hexdigest()==r['source_sha256'],'seed_sha_matches':hashlib.sha256(pathlib.Path(r['seed_receipt']).read_bytes()).hexdigest()==r['seed_sha256']}
(B/'identity-validation.json').write_text(json.dumps(out,indent=2))
print({t:{k:v for k,v in x.items() if k.endswith('matches')} for t,x in out.items()})
