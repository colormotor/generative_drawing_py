from py5canvas import *
from PIL import ImageOps

w, h = 400, 400
vin = VideoInput(size=(w, h))

palette = load_image('palette.jpg')

def setup():
    create_canvas(w, h)

def draw():
    background(255)
    fill(0)
    no_stroke()

    img = vin.read()

    img = img.resize((25,25)).convert('L')
    
    h = 0.5
    palette_y = int(remap(h, 0, 1, 0, palette.height-1))

    spacing = width/img.height
    for y in range(img.height):
        for x in range(img.width): #
            push()
            v = img.getpixel((x,y)) # In range 0 - 255
            radius = remap(v, (0, 255), (spacing*0.5, 0.0))
            palette_x = int(remap(v, 0, 255, 0, palette.width-1))
            fill(palette.getpixel((palette_x, palette_y)))
            translate(x*spacing+spacing/2, y*spacing+spacing/2)
            circle(0, 0, radius)
            pop()

    # Show palette
    # image(palette)
    # fill(0)
    # circle(palette_x, palette_y, 7)
run()