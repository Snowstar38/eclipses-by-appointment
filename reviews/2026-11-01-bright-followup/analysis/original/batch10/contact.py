from pathlib import Path
from PIL import Image,ImageOps,ImageDraw
import csv,glob
B=Path(__file__).parent
for kind in ('raw','diff'):
 rows=[]
 for q in csv.DictReader((B/'queue.csv').open()):
  tic=q['tic'];p=B/tic/'raw-events.png' if kind=='raw' else Path(glob.glob(str(Path('[local path omitted] 5/made/sb1-scale/diffimg')/tic/'diff_s*.png'))[0]);im=Image.open(p).convert('RGB');im.thumbnail((550,350));canvas=Image.new('RGB',(570,390),'white');ImageDraw.Draw(canvas).text((8,4),tic,fill='black');canvas.paste(im,((570-im.width)//2,30));rows.append(canvas)
 out=Image.new('RGB',(570*2,390*5),'white')
 for i,im in enumerate(rows):out.paste(im,((i%2)*570,(i//2)*390))
 out.save(B/(kind+'-contact.png'))
