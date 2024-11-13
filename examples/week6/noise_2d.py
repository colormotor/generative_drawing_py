from py5canvas import *

"""
TASK 
- Try adjusting pixelScale and noiseScale to understand what they do.
- Try animating the noise like you did with 1D noise.
- Try moving in different directions across the noise plane.
- Experiment with different ways for rendering the noise pattern.
"""

octaves = 4
falloff = 0.5
noise_scale = 0.05
pixel_scale = 8

def setup():
    size(512, 512)
    no_stroke()
    noise_detail(octaves, falloff)

def draw():
    background(0)

    num_cols = width // pixel_scale
    num_rows = height // pixel_scale
    w = width / num_cols
    h = height / num_rows

    for x in range(num_cols):
        for y in range(num_rows):
            noise_val = noise(x * noise_scale, y * noise_scale)
            fill(noise_val * 255)
            rect(x * w, y * h, w, h)

run()
