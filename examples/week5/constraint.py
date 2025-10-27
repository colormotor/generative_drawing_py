from py5canvas import *

"""
TASK

- For each grid cell choose a random number
- if the number is greater than 0.5 draw a diagonal from bottom left to top right
- otherwise draw the other diagonal from top left to bottom right
- now comment out the rectangle to see the full effect
- experiment with changing the strokeWeight and strokeCap
- can you think of a third drawing option ? adapt your sketch to include these
- add another layer of stochastically controlled features on to the grid. This might involve colour or perhaps another shape
"""

num_cols = 0
num_rows = 0

def setup():
    create_canvas(512, 512)

    global num_cols, num_rows
    num_cols = 20
    num_rows = 20
    
    no_fill()
    
    background(255)
    
    w = width/num_cols
    h = height/num_rows

    for i in range(num_cols):
        for j in range(num_rows):
            x = i * w
            y = j * h
            
            rect(x, y, w, h)

run()