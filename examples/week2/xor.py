from py5canvas import *

"""
- Experiment with changing the modulo value
- How many different patterns can you make
- Try changing the formula further
- Can you make patterns which are less square like ?
"""

n = 14

def setup():
    create_canvas(300, 300)
    background(0, 128, 255)  # sky-blue background
    no_fill()
    for y in range(height):
        for x in range(width):
            # bitwise XOR on integers, then modulo and threshold
            v = abs(((x + y) ^ (x - y)) % n) > (n / 2)
            stroke(int(v) * 255)  # True -> 255, False -> 0
            point(x, y)

# More detailed explanation here ...
# https://blog.devgenius.io/p5-js-animation-in-131-characters-of-code-explained-37cd8e1bb996

run()
