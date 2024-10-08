#!/usr/bin/env python3
import importlib
import py5canvas
importlib.reload(py5canvas)
from py5canvas import *

def setup():
    global runners, num_runners, runner_size, runner_spacing, increment
    create_canvas(512, 512)

    runners = []
    num_runners = 300
    runner_size = 2
    runner_spacing = runner_size * 3 / 4

    increment = TWO_PI / 7200

    # create an array of runners
    for i in range(num_runners):
        x = 0
        y = (runner_spacing + runner_spacing * i) * -1
        runners.append([x, y])

def draw():
    background(255)

    # we make 0,0 the center of the canvas
    translate(width / 2, height / 2)

    # draw the runners and update their position
    stroke(0)
    no_fill()
    begin_shape()

    for i in range(len(runners)):
        x, y = runners[i]
        vertex(x, y)
        # rotate each runner's position
        runners[i] = rotate_vector(x, y, increment * (len(runners) - i))

    end_shape()


run()
