from py5canvas import *

"""
TASK

- Add some random displacement to the corner of each quad to make them overlap by different amounts
- Experiment with different size ranges of displacement for each corner
"""

num_cols = 0
num_rows = 0

def setup():
    create_canvas(512, 512)

    global num_cols, num_rows
    num_cols = 20
    num_rows = 20
    
    fill(80, 0, 130, 100)
    no_stroke()
    
    background(255)
    
    w = width/num_cols
    h = height/num_rows

    for i in range(num_cols):
        for j in range(num_rows):
            x = i * w
            y = j * h
            
            quad(
            x, y,
            x + w, y,
            x + w, y + h,
            x, y + h
            )

run()
