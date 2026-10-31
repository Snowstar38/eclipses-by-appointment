from pathlib import Path
import csv
from PIL import Image,ImageOps,ImageDraw
b=Path(__file__).parent;rs=list(csv.DictReader(open(b/'queue.csv')))
for kind in ['raw','diff']:
 canvas=Image.new('RGB',(2000,600*5),'white')
 for i,r in enumerate(rs):
  t=r['tic'];p=b/t/'raw-events.png' if kind=='raw' else next((Path('[local path omitted] 5/made/sb1-scale/diffimg')/t).glob('diff_s*.png'))
  im=Image.open(p);im.thumbnail((1000,570));x=(i%2)*1000;y=(i//2)*600;canvas.paste(im,(x,y+25));ImageDraw.Draw(canvas).text((x+10,y+5),t,fill='black')
 canvas.save(b/f'{kind}-contact.jpg')
