from py5canvas import *

w, h = 400, 400

vin = VideoInput(size=(w, h))

# For color images, format is height (num rows), width (num cols), num_channels 
img = np.zeros((h, w, 3))

def parameters():
    params = {'Amount': (0.1, {'min':0.01, 'max':1.0})}
    return params

def setup():
    create_canvas(w, h)

def draw():
    global img # we are modifying the image
    background(255)
    fill(0, 128)
    no_stroke()

    # Get a new image, convert to grayscale and then numpy
    new_img = vin.read() # PIL Image
    # new_img = new_img.convert('L')
    new_img = np.array(new_img)/255

    amt = params.amount
    # EMA stands for "Exponential moving average", 
    # it is a trick we have used a bunch of times already 
    img = lerp(img, new_img, amt)
    # Or
    # img = new_img*amt + img*(1.0 - amt)
    # Or
    # img = img + (new_img - img)*amt
    image(img)

run()