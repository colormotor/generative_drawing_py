'''
Warm up
 - What new patterns can you make ?
 - Try using s to change the x and y positions of the circles
 - Try adding extra ellipse calls with different uses of s to make a design
 - What might you do with colour ?
 - Could you apply the same techniques with different shapes
'''

from py5canvas import *

s = None
is_dark = True

def setup():
    global s
    create_canvas(400, 400)
    background(0)
    no_stroke()
    s = width
    is_dark = True

def draw():
    global s, is_dark

    if is_dark:
        fill(0)
    else:
        fill(255, 0, 0)

    ellipse(width / 2, height / 2, s, s)

    s -= 5
    is_dark = not is_dark

    if s < 0:
        no_loop()

run()
