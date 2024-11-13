from py5canvas import *

"""
TASK
- Change the code to add an array of thousands of particles starting in random positions.
- Add code to randomly reposition the particles when they go off canvas.
- Add code to change the colour of the particles based on the same or different noiseVals.
- Experiment with changing parameters such as noiseScale, octaves and falloff.
- Experiment with moving through the noise plane with incrementing values (in the flow function).
- Experiment with adding a third incrementing dimension to the noise plane (in the flow function).
"""

octaves = 8
falloff = 0.5
particle = None
noise_scale = 0.01

def setup():
    global particle
    size(512, 512)
    noise_detail(octaves, falloff)
    particle = Vector(width / 2, height / 2)
    background(0)

def flow(x, y):
    noise_val = noise(x * noise_scale + frame_count * 0.02, 
                      y * noise_scale, 
                      frame_count * 0.01)
    angle = remap(noise_val, 0, 1, 0, TWO_PI)
    return angle

def draw_flow_field():
    stroke_weight(1)
    background(0)
    stroke(255, 0, 255, 255)
    step = 10
    for y in range(0, height, step):
        for x in range(0, width, step):
            theta = flow(x, y)
            dx = cos(theta)
            dy = sin(theta)
            line(x, y, x + dx * 20, y + dy * 20)

def draw():
    global particle
    background(0, 5)

    # Uncomment to visualize flow field
    draw_flow_field()
    angle = flow(particle[0], particle[1])
    particle += direction(angle) #Vector(cos(angle), sin(angle))

    stroke(255)
    stroke_weight(4)
    point(particle)

run()
