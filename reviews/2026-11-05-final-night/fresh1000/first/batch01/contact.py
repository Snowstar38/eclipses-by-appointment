import json
from pathlib import Path
from PIL import Image,ImageOps,ImageDraw
b=Path(__file__).resolve().parent
ims=[]
for f in b.glob('*/lead-raw-context.png'):
 im=Image.open(f); im.thumbnail((600,1000)); ims.append(im)
out=Image.new('RGB',(2400,2000),'white')
for i,im in enumerate(ims):out.paste(im,((i%4)*600,(i//4)*1000))
out.save(b/'contact.png')
