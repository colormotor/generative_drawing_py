from py5canvas import *

t = 0

def setup():
    create_canvas(512, 512)

def grid():
    for x in range(0, width, 10):
        rect(x - width / 2, -height, 4, height * 2)

def draw():
    global t
    background(255)
    fill(0, 90)
    no_stroke()

    translate(width / 2, height / 2)
    for i in range(10):
        push_matrix()
        rotate(t * (i + 1) * 0.3)
        grid()
        pop_matrix()
    t += 0.01


# ------------------------------
# Alternate sketch (commented)
# ------------------------------
# s = 2
#
# def setup():
#     create_canvas(400, 400)
#     background(0)
#     stroke(0, 255, 0, 128)
#     no_fill()
#
# def draw():
#     global s
#     for i in range(3):
#         for j in range(width):
#             ellipse(width/2 - 100 + j*100, height/2, s*(i+1)*0.79, s*(i+1)*0.79)
#     s += 3

run()
