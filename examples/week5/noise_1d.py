from py5canvas import *

def setup():
    create_canvas(600, 400)
    noise_detail(3)

def draw():
    background(255)
    translate(0, height/2)
    no_fill()
    
    phase = 0

    n = 5
    
    amplitude = 100
    begin_shape()
    for input in linspace(0, n-1, 200):
        x = remap(input, 0, n-1, 0, width)
        y = remap(noise(input + phase), 0, 1, -amplitude, amplitude)
        vertex(x, y)
    end_shape()

    # Draw the zero 
    stroke(255, 0, 0, 128)
    line(0, 0, width, 0)
    for i in range(n):
        x = remap(i, 0, n-1, 0, width)
        circle(x, 0, 4)
    stroke(0)
    
run()
