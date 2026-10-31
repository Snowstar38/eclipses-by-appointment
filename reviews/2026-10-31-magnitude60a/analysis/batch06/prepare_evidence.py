import csv,json,shutil
from pathlib import Path
from PIL import Image,ImageOps,ImageDraw
B=Path('[local path omitted]');S=Path('[local path omitted] 5/made/sb1-scale/diffimg');imgs=[];raw=[]
for r in csv.DictReader(open(B/'queue.csv')):
 t=r['tic'];D=B/t/'historical';D.mkdir(exist_ok=True)
 for p in (S/t).glob('*'):
  if p.name.startswith('diff_s') or p.name=='gaia.json':shutil.copy2(p,D/p.name)
 for dest,fp in [(imgs,next(D.glob('diff_s*.png'))),(raw,B/t/'raw-events.png')]:
  im=Image.open(fp).convert('RGB');im.thumbnail((1000,600));canvas=Image.new('RGB',(1000,630),'white');canvas.paste(im,(0,30));ImageDraw.Draw(canvas).text((10,5),t,fill='black');dest.append(canvas)
for name,arr in [('diff-contact.png',imgs),('raw-contact.png',raw)]:
 sheet=Image.new('RGB',(2000,630*5),'white')
 for i,im in enumerate(arr):sheet.paste(im,(1000*(i%2),630*(i//2)))
 sheet.save(B/name)
