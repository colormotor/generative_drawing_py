from py5canvas import *
from PIL import ImageOps

w, h = 400, 400
vin = VideoInput(size=(w, h))

def setup():
    create_canvas(w, h)

def draw():
    background(255)
    fill(0)
    no_stroke()

    img = vin.read()

    img = img.resize((30,30)).convert('L')
    
    spacing = width/img.height
    for y in range(img.height):
        for x in range(img.width): #
            push()
            v = img.getpixel((x,y)) # In range 0 - 255
            radius = remap(v, (0, 255), (spacing*0.5, 0.0))
            translate(x*spacing+spacing/2, y*spacing+spacing/2)
            circle(0, 0, radius)
            pop()

run()