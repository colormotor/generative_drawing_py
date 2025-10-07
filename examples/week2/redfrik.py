from py5canvas import *
import math

# Adapting Example 0009 from https://fredrikolofsson.com/f0blog/p5-tweets/
# Each block below is one of the tweet-length sketches,
# converted to Py5Canvas. Only the final "0002" is active.
# Uncomment others to try them out.

# ------------------------------
# 0009
# def setup():
#     create_canvas(1200, 900)
#
# def draw():
#     global i, j
#     for j in range(133):
#         rect(9 * j + 1,
#              math.sin((i + j) * 0.75 / math.cos(j / 99) / 5e3) * 99 + 450,
#              9, 9)
#     i += 1
#
# i = 0
# j = 0
# ------------------------------

# ------------------------------
# 0019
# s = 900
# i = 0
# j = 0
#
# def setup():
#     create_canvas(s, s)
#
# def draw():
#     global i, j
#     stroke(i)
#     line(i, j, s - j, i)
#     if j % 5 < 1:
#         i = (i + 1) % s
#     if i % 11 < 1:
#         j = (j + i) % s
# ------------------------------

# ------------------------------
# 0015
# s = 900
# i = 0
#
# def setup():
#     create_canvas(s, s)
#     frame_rate(10000)
#     stroke(255, 25)
#
# def draw():
#     global i
#     fill(i % 89, 0, 0, 127)
#     rect((i % 90) * 9,
#          (i % 91) * 9,
#          (i * i) % 92,
#          (i * i) % 93)
#     i += 1
# ------------------------------

# ------------------------------
# 0002 (first variant)
i = 0
j = 0

def setup():
    create_canvas(1200, 900)
    frame_rate(999)

def draw():
    global i, j
    j = 0
    while j < 99:
        x = i % (1199 - j)
        i += 1
        j += 1
        y = (i // 99) % (999 - j)
        rect(x, y, i % 12, j % 16)

# (0002 second variant)
# i = 0
# j = 0

# def setup():
#     create_canvas(1200, 900)
#     frame_rate(999)

# def draw():
#     global i, j
#     j = 0
#     while j < 99:
#         # In JS: rect(i++ % (1199 - j++), int(i/99) % (999 - j), i % 12, j % 16)
#         x = i % (1199 - j)
#         i += 1
#         j += 1
#         y = (i // 99) % (999 - j)
#         rect(x, y, i % 12, j % 16)

run()
