from py5canvas import *
import cv2

w, h = 400, 400

vin = VideoInput('fingers.mov', size=(w, h))
first_frame = None

def parameters():
    return {'tightness':(0.5, {'min':0.0, 'max':1.0})}

def find_contours(im, invert=False, thresh=127, eps=0.0):
    ''' Utility function to get contours compatible with py5canvas.
    Assumes a grayscale image as a result
    The eps parameter controls the amount of simplification (if > 0)
    '''
    _, thresh_img = cv2.threshold(im, thresh, 256, int(invert))
    contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    S = []
    for ctr in contours:
        if eps > 0:
            ctr = cv2.approxPolyDP(ctr, eps, True)
        if len(ctr) > 3:
            S.append(np.vstack([ctr[:,0,0], ctr[:,0,1]]).T)
    return S

def setup():
    create_canvas(w, h)

def draw():
    global first_frame
    background(0)
    img = vin.read().convert('L')
    img = np.array(img)
    if first_frame is None:
        first_frame = img
    curve_tightness(params.tightness)
    contours = find_contours(img, eps=10)
    no_fill()
    stroke(255)
    for ctr in contours:
        curve(ctr, close=True)
        # begin_shape()
        # for p in ctr:
        #     curve_vertex(p)
        # end_shape(CLOSE)
    # #image(img)
    # stroke(255, 0, 0)
    # fill(0, 128)
    # #shape(contours, False)
    # for pts in contours:
    #     curve(pts)

run()