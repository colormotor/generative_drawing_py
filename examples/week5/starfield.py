from py5canvas import *

"""
TASK
- use random_seed to stop the stars flickering
- use random_seed a second time in the code with no parameters to make the space craft shudder again.
"""

scroll_x = 0

def setup():
    create_canvas(512, 512)

def draw():
    global scroll_x
    background(0)
    # draw the starfield
    
    stroke_weight(2)
    stroke(255)
    
    for i in range(1000):
        point(scroll_x + random(0, width * 5), random(0, height))
    
    scroll_x -= 1

    translate(0, random(-2, 2))
    no_stroke()
    fill(100)
    arc(width/2, height/2, 100, 50, PI, TWO_PI)
    fill(0, 180, 180)
    arc(width/2, height/2 - 20, 45, 20, PI, TWO_PI)

run()