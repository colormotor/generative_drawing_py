from py5canvas import *

"""
TASK

- Input currently isn't used. Convert the noise into 2D noise using the changing value of input to create an animated effect.
- How is this animation different from the previous noise sketches? Can you describe this accurately?
- What else do you notice about this animation?
- Use a for loop to make multiple animated lines.
- How can you make the lines varied but not overlap (like Andrew Hoff)?
"""

noise_step = 0.01
input_val = 0

def setup():
    size(400, 400)
    no_fill()
    noise_detail(2)

def draw():
    global input_val
    background(0)
    stroke(255)
    
    begin_shape()
    for i in range(width):
        n = noise(i * noise_step) #, input_val)  # Use 2D noise for animation
        y = remap(n, 0, 1, height / 2 - 50, height / 2 + 50)
        vertex(i, y)
    end_shape()
    
    input_val += 0.01  # Increment input for animation

run()
