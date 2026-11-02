from pathlib import Path
import csv
from PIL import Image,ImageOps,ImageDraw
B=Path(__file__).parent
rows=list(csv.DictReader(open(B/'queue.csv')))
for kind,pat in [('raw','raw-events.png'),('pixel','fresh-pixels/diff_fresh.png')]:
 imgs=[]
 for r in rows:
  im=Image.open(B/r['tic']/pat).convert('RGB');im.thumbnail((1000,900));can=Image.new('RGB',(1000,930),'white');can.paste(im,(0,30));ImageDraw.Draw(can).text((10,8),r['tic'],fill='black');imgs.append(can)
 out=Image.new('RGB',(2000,930*5),'white')
 for i,im in enumerate(imgs):out.paste(im,((i%2)*1000,(i//2)*930))
 out.save(B/f'{kind}-contact.png')
