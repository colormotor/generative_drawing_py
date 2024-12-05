from py5canvas import *

w, h = 400, 400

vin = VideoInput('fingers.mov', size=(w, h))

# Create a buffer of images
images = []
num_frames = 20 # Number of frames to average

# For color images, format is height (num rows), width (num cols), num_channels 
# Alternative syntax, "List comprehension":
images = [np.zeros((h, w, 3)) for i in range(num_frames)]
# Equivalent to:
# for i in range(num_frames):
#     images.append(np.zeros((h, w, 3)))

def setup():
    create_canvas(w, h)

def draw():
    background(255)
    fill(0, 128)
    no_stroke()

    # Get a new image, convert to grayscale and then numpy
    new_img = vin.read() # PIL Image
    # new_img = new_img.convert('L')
    new_img = np.array(new_img)/255
    # Append image to end of list and remove element from "front"
    images.append(new_img)
    images.pop(0)

    # Average images. Two ways to do this
    # 1. Use builtin `sum` function (it sums the arguments in a sequence provided as input)
    #    then divide by the number of frames 
    #average_img = sum(images)/num_frames #[-1] #np.mean(images, axis=-1)
    # 2. Use NumPy `mean` function (mean means average, no pun intended)
    average_img = np.mean(images, axis=0)

    image(average_img)

run()