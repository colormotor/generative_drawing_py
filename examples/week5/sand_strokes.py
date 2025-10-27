from py5canvas import *

# Sandstrokes - J.Tarbull study
# Simon Katan - Generative Drawing 2020
# Converted to py5canvas by Daniel Berio

"""
TASK 
    - add an extra for loop to implement multiple lines across the image
    - sample a random pixel from the image for each line and use this to set colour
    - experiment with with different numbers of lines, alpha blend and sand_densities
    - experiment with randomGaussian and distributions to change the quality of the sandstrokes
    - try a different colour sampling strategy eg. move linearly for each collection of sandstrokes
"""

img = None

def preload():
    global img
    img = load_image('sand.jpg')  # load our colour sample image

def setup():
    create_canvas(400, 400)

    background(255)
    
    sand_density = 100

    translate(0, height/2)

    stroke(0, 10)

    amp = 20

    for i in range(width):
        x = i
        amp += random(-5, 5)

        for j in range(sand_density):
            y = random_gaussian(0.5, 0.2)
            y = remap(y, 0, 1, -amp, amp)
            point(x, y)

run()