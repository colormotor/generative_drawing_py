from py5canvas import *
from py5canvas.turtle import Turtle 

def setup():
    create_canvas(600, 600)
    background(255)
    translate(width/2, height/2)
    t = Turtle()
    for i in range(36):
        t.right(10)
        t.circle(120, steps=11)
    stroke(0)
    stroke_weight(1)
    no_fill()
    shape(t.paths) # This draws all the paths created by the turtle

run()