from py5canvas import *

'''
TASK

- experiment with different alpha blends and shapes
- experiment with manipulating the colours (eg. flipping them)
- experiment with making the size of the shape dependent on the brightness https://p5js.org/reference/#/p5/brightness

'''


img = load_image('tornado.jpg')

def setup():
    create_canvas(img.width, img.height)
    no_stroke()

def draw():
    #random_seed(10)
    background(255)

    for i in range(1500):
        px = floor(random()*width)
        py = floor(random()*height)
        # https://www.geeksforgeeks.org/python/python-pil-getpixel-method/
        c = img.getpixel((px, py)) # 
        fill(c)
        rect(px, py, 50, 50)

run()