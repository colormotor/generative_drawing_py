from py5canvas import *

"""
TASK

- change the conditional statements to alter the distribution of triangles so that they are unevenly distributed
- now alter the code to make one type of triangle gradually dominate towards the south east corner of the grid
- experiment with introducing other independent random layers (Eg. fill colour)
- make these layers have biases tending towards different corners
"""

num_cols = 0
num_rows = 0

def setup():
    create_canvas(512, 512)

    global num_cols, num_rows
    num_cols = 20
    num_rows = 20
    
    fill(0)
    no_stroke()
    
    background(255)
    
    w = width/num_cols
    h = height/num_rows

    for i in range(num_cols):
        for j in range(num_rows):
            x = i * w
            y = j * h
            
            r = random()
            
            if r > 0.8:
                # EAST
                triangle(x, y, x + w, y + h/2, x, y + h)  
            elif r > 0.6:
                # WEST
                triangle(x, y + h/2, x + w, y, x + w, y + h)  
            elif r > 0.4:
                # NORTH
                triangle(x + w/2, y, x + w, y + h, x, y + h)  
            elif r > 0.2:
                # SOUTH
                triangle(x + w/2, y + h, x + w, y, x, y)   

run()
