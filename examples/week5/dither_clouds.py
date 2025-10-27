from py5canvas import *

"""
TASK
- experiment with biases to create density gradients changing from left to right and top to bottom
- experiment with different values for the pow function to create different shapes of distribution
- combine the distributions in the x and y planes to make shades in the corner
- using conditional statements and random see if you can build up more complex shapes and symmetries
- experiment with random gaussian to create further shapes
- try combining with other functions such as min, max, constrain, sin & cos to make many shapes
"""

def setup():
    create_canvas(512, 512)
    
    stroke_weight(2)

def draw():
    background(0)
    
    stroke(255)
    
    translate(width/2, height/2)
    
    for i in range(2000):
        x = random()
        y = random()
        
        x = remap(x, 0, 1, -100, 100)
        y = remap(y, 0, 1, -100, 100)
        point(x, y)  

run()
