from py5canvas import *

"""
TASK
- Annoyingly the circle doesn't close properly. Can you explain why?
- There's a straightforward solution to this problem using 2D noise. Can you work out what it is?
- Have a go at implementing it.
- Use a for loop to create concentric circles (like a tree trunk).
- Can you change the parameters to make these varied as the circles move outwards?
"""

noise_step = 0.01

def setup():
    size(512, 512)
    no_fill()
    stroke(255)
    noise_detail(2)
    
def draw():
    background(0)
    translate(width / 2, height / 2)

    for i in range(5):  # Create multiple concentric circles
        begin_shape()
        for theta in range(360):
            noise_val = noise(theta * noise_step, i * 0.1)  # Use 2D noise for smooth closure
            r = remap(noise_val, 0, 1, 100 + i * 20, 200 + i * 30)  # Vary parameters outward
            
            x = sin(radians(theta)) * r
            y = cos(radians(theta)) * r
            
            vertex(x, y)
        end_shape(CLOSE)

run()
