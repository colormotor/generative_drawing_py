''' Simulating a Galton board with python'''

from py5canvas import *

rows = 20
num_bins = rows*2+1
counts = [0]*num_bins # This creates an array with the number of bins

def setup():
    create_canvas(500, 400)
    frame_rate(0)

def random_process():
    # Starting from the middle we randomly move left or right 
    # as we go down each row
    index = rows 
    # Randomly make iterations even or odd, 
    # otherwise we will end up in only even or only odd bins
    n = rows 
    if random() < 0.5:
        n = n - 1
    # Run the simulation
    for i in range(n):
        if random() < 0.5: 
            index -= 1
        else:
            index += 1
    # Increase count for bin where we ended
    counts[index] += 1

def draw():
    fill(0)
    # Continue each frame until we reach max height
    if max(counts) < height:
        random_process()
    # Show it
    bin_w = width/num_bins
    for i in range(num_bins):
        x = remap(i, 0, num_bins, 0, width)
        h = counts[i]
        rect(x, height-h, bin_w, h)

run()