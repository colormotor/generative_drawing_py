from py5canvas import *
import cv2


w, h = 400, 400
vin = VideoInput('fingers.mov', (w, h))

images = []

def setup():
    create_canvas(w, h)

def draw():
    images.append(np.array(vin.read().convert('L')))
    
    if len(images) > 2:
        images.pop(0)
    image(images[-1])
    if len(images) < 2:
        return
    
    flow = cv2.calcOpticalFlowFarneback(images[0], images[1], None, 0.7, 3, 11, 5, 5, 1.1, 0)

    stroke(255, 0, 0)
    step = 10
    for i in range(0, h, step):
        for j in range(0, w, step):
            line(j, i, j+flow[i,j][0], i+flow[i,j][1])
run()