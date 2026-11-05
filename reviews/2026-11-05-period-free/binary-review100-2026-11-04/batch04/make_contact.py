import csv
from pathlib import Path
from PIL import Image, ImageOps, ImageDraw

B=Path(__file__).resolve().parent
rows=list(csv.DictReader((B/'queue.csv').open(newline='',encoding='utf-8')))
for kind in ('raw-windows','orbit-context'):
 for start in (0,5):
  tile_w,tile_h=900,330
  sheet=Image.new('RGB',(tile_w*2,tile_h*5),'white')
  draw=ImageDraw.Draw(sheet)
  for j,q in enumerate(rows[start:start+5]):
   tic=q['tic'];n=start+j
   im=Image.open(B/tic/(kind+'.png')).convert('RGB')
   im.thumbnail((tile_w-8,tile_h-32))
   x=(j%2)*tile_w;y=(j//2)*tile_h
   sheet.paste(im,(x,y+25));draw.text((x+5,y+4),q['sample_id']+' TIC '+tic,fill='black')
  sheet.save(B/f'{kind}-contact-{start//5+1}.png')
