import json,os
ids=['373138363','270181578','298645930','362610608','399501645']
p=os.path.join(os.environ['TEMP'],'hunt-sb1-scale','targets.json')
t=json.load(open(p)); o={k:t[k] for k in ids}; json.dump(o,open('targets-selected.json','w'),indent=2)
for k,v in o.items(): print(k, len(v.get('qlp',[])), 'gaia',v.get('gaia'), 'qlp', v.get('qlp',[])[:1])
