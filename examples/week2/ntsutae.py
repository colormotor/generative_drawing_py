"""
- Experiment with changing the modulo value
- How many different patterns can you make
- Try changing the formula further
- Can you make patterns that are less square-like?
See: https://twitter.com/ntsutae/status/1268820823952916486?s=20&t=F8ydakRFTRmTlvl1bU8fKA
"""

from py5canvas import *

def setup():
    create_canvas(600, 600)
    background(0)

def draw():
    t = frame_count
    copy(0, 0, width, height, 0, 1, width, height)  # scroll down
    stroke(255)
    for x in range(width, -1, -1):
        v = int(abs(t+((x-t)^(x+t)+3)**9))%997 > 97;
        #v = ((x + t) ^ (x - t)) % 9  # simplified version
        if not v:  # when v is 0, stroke white
            stroke(255)
        else:
            stroke(0)
        point(x, 0)

run()
