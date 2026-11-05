import csv
from pathlib import Path
from PIL import Image, ImageOps, ImageDraw

b=Path(__file__).resolve().parent
rows=list(csv.DictReader((b/'queue.csv').open(encoding='utf-8',newline='')))
canvas=Image.new('RGB',(2400,1600),'white')
for i,row in enumerate(rows):
    src=b.parent/'source-packets'/row['tic']/'raw-preview.png'
    im=Image.open(src).convert('RGB')
    im.thumbnail((790,750))
    x=(i%3)*800;y=(i//3)*400
    # Show first half of each packet preview at legible scale.
    crop=im.crop((0,0,im.width,min(im.height,370)))
    canvas.paste(crop,(x,y+20))
    ImageDraw.Draw(canvas).text((x+5,y+4),row['sample_id']+' TIC '+row['tic'],fill='black')
canvas.save(b/'preview-montage.png')
