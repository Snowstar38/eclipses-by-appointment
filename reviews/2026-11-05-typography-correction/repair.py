import pymupdf,json,re,hashlib
from pathlib import Path
from collections import defaultdict
b=Path('[workspace]/Astra/made/final-night-2026-11-05'); out=b/'typography-qa';r=json.loads((b/'typography-receipt.json').read_text(encoding='utf-8')); name=r['pdf']['file']; original=b/'typography-originals'/name; public=Path('[workspace]/tmp/eba-astra-20261030')/name; temp=out/'corrected-temp.pdf'; sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest(); old=sha(public); d=pymupdf.open(original); before=[p.get_text() for p in d]; groups=defaultdict(list)
for f in r['pdf']['replacements']:groups[f['page']].append(f)
font=pymupdf.Font(fontfile='C:/Windows/Fonts/georgia.ttf'); fixes=[]
for n,fs in groups.items():
 p=d[n-1]; spans=[s for b1 in p.get_text('dict')['blocks'] for l in b1.get('lines',[]) for s in l['spans']]
 for f in fs:
  rect=pymupdf.Rect(f['rect']); matches=[s for s in spans if pymupdf.Rect(s['bbox']).intersects(rect) and '+/-' in s['text']]; assert len(matches)==1,(n,len(matches)); s=matches[0]; assert s['font']=='Georgia'; size=s['size']; baseline=s['origin'][1]; color=s['color']; width=font.text_length('±',fontsize=size); x=(rect.x0+rect.x1-width)/2
  p.add_redact_annot(rect,fill=(1,1,1)); fixes.append({'page':n,'rect':list(rect),'origin':[x,baseline],'font':'Georgia','size':size,'color':color})
 p.apply_redactions(images=0,graphics=0)
 p.insert_font(fontname='qaGeorgia',fontfile='C:/Windows/Fonts/georgia.ttf')
 for f in [x for x in fixes if x['page']==n]:
  c=f['color']; p.insert_text(f['origin'],'±',fontname='qaGeorgia',fontsize=f['size'],color=((c>>16&255)/255,(c>>8&255)/255,(c&255)/255))
d.save(temp,garbage=4,deflate=True);d.close()
with pymupdf.open(temp) as a:
 assert len(a)==len(before)==762
 for i,p in enumerate(a):
  assert re.findall(r'\d+(?:\.\d+)?',before[i])==re.findall(r'\d+(?:\.\d+)?',p.get_text()),i+1
 for n,fs in groups.items():
  for f in fs: assert '±' in a[n-1].get_textbox(pymupdf.Rect(f['rect'])+(-3,-3,3,3)),n
new=sha(temp)
receipt={'source_backup_sha256':sha(original),'previous_public_sha256':old,'corrected_public_sha256':new,'pages':762,'numeric_tokens_unchanged_all_pages':True,'page_count_unchanged':True,'fixes':fixes,'visual_review':'pending'}
(out/'repair-receipt.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print('temp',temp,'sha',new,'fixes',len(fixes))


