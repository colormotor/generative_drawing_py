'''
 Modulo can be useful to do "infinite" animations
 Here we animate a series of concentric cirles and use
 the modulo operator to animate just the movement between a cirle and the distance to the next
 giving the illusion of a continuous movement.

 Ideas:
 - Try changing/varying shapes, stroke weights, adding colors
 - The animation is intentionally inside a funtion:
   - try superimposing multiple "ripples" at different positions
   - try varying the parameters for different ripples
 - Note that in Javascript the % operator will also work with non-integer values
'''

from py5canvas import *

t = 0

def setup():
    create_canvas(512, 512)
    stroke(0)
    no_fill()

def ripple(x, y, step):
    stroke_weight(step / 3)
    for i in range(0, int(width * 3), step):
        circle(x, y, i + t % step)

def draw():
    global t
    background(255)
    ripple(width / 2, height / 2, 20)
    t += 1

run()