import csv,json,hashlib,math,pathlib
w=pathlib.Path(__file__).parent;t=json.load(open(w/'targets.json'));root=pathlib.Path('Astra/made/binary-extension-2026-11-04/catalogue-archives')
a=root/'mast-prsa.csv';b=root/'ijspeert-identities.csv';assert hashlib.sha256(a.read_bytes()).hexdigest()=='97e81f6c01716a431379ab6bd37d1182b611a485107110e0eba830f817ba7a8f';assert hashlib.sha256(b.read_bytes()).hexdigest()=='8cc6a6b97bc21195d0564659d637f6928aec4364baa7bfa86f82e015742ef75e'
p=list(csv.DictReader(open(a,encoding='utf8')));i=list(csv.DictReader(open(b,encoding='utf8')))
def sep(a,b,c,d):
 a,b,c,d=map(math.radians,(float(a),float(b),float(c),float(d)));h=math.sin((b-d)/2)**2+math.cos(b)*math.cos(d)*math.sin((a-c)/2)**2;return math.degrees(2*math.asin(min(1,math.sqrt(h))))*3600
result=[]
for x in t:
 hitp=[r for r in p if r['tess_id']==x['tic'] or sep(r['ra'],r['dec'],x['ra'],x['dec'])<=60];hiti=[r for r in i if r['TIC']==x['tic'] or r['GaiaDR3']==x['gaia'] or sep(r['RAJ2000'],r['DEJ2000'],x['ra'],x['dec'])<=60];result.append({'tic':x['tic'],'scope':x['scope'],'label':x['label'],'prsa':hitp,'ijspeert':hiti})
(w/'local-table-matches-60arcsec.json').write_text(json.dumps(result,indent=2));print('hits',[(x['label'],len(x['prsa']),len(x['ijspeert'])) for x in result if x['prsa'] or x['ijspeert']])

