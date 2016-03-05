#!/usr/bin/env python
import unicornhat as UH
from fonts import Bitmap, Font
import time
from datetime import datetime
import os,sys
os.chdir(os.path.dirname(sys.argv[0]))

fnt = Font('ttf/pixel4x4f.ttf', 6)
#fnt = Font('3x3_font_for_nerds.ttf', 4)
rgb = [100,100,255]

def flip(bit):
    out=Bitmap(8,8)
    for y in range(out.width):
      for x in range(out.height):
        out.pixels[56-(y*out.height) +(out.width-1-x)] = bit.pixels[y*out.width + x]
    return out

def show_time():
    t=str(datetime.now().time())[:5].replace(':','')

    out=Bitmap(8,8)
    for i,c in enumerate(t):
        ch = fnt.render_character(c)
        #print(i, i%2 *4, i//2 *4)
        out.bitblt(ch, i%2 *4, i//2 *4)

    out=flip(out)
    for y in range(out.width):
      for x in range(out.height):
        if out.pixels[y * out.width + x]:
            UH.set_pixel(x,y,*rgb)
        else:
            UH.set_pixel(x,y,0,0,0)

    if int(time.time()) % 2:
        #out.pixels[63] = 1
        UH.set_pixel(0,0,50,50,170)
    
    UH.show()
#    print(repr(out))

if __name__ == '__main__':
    while time.sleep(1) or True:
        show_time()

