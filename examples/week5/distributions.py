from py5canvas import *

"""
TASK

- experiment with using min and max to make different distributions
- experiment with using pow with different exponent values to make different distributions
- experiment with random_gaussian to make different distributions. Make sure you understand what the two arguments do.
"""

def setup():
    create_canvas(512, 512)

    num_bins = 20
    num_samples = 2000
    
    bins = []
    
    # create the bins initialized at zero
    for i in range(num_bins):
        bins.append(0)
    
    for i in range(num_samples):
        
        # generate a random number between 0 and 1
        r = random()
        
        # workout the correct bin to put it in
        index = floor(r * num_bins)
        
        bins[index] += 1
        
    background(0)
    fill(255, 0, 0)
    stroke(255)
    
    w = width/num_bins
    # draw the histogram
    for i in range(num_bins):
        rect(
            i * w,
            height - bins[i],
            w,
            bins[i]
        )

run()