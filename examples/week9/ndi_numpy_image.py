
''''
NDI Sender example using py5canvas and NDIlib
To run you need to install the NDI SDK (system wide) on your machine from:
https://ndi.video/for-developers/ndi-sdk/
And then the ndi-python package with
pip install ndi-python
'''

from py5canvas import *
import NDIlib as ndi

def setup_ndi(name="py5canvas NDI Sender"):
    """ This function initializes NDI for sending video frames once
    If you reload the script, it will not re-initialize NDI and keep the same sender.
    The sender will be exposed as a global `ndi_send` variable
    """
    print("Setting up NDI sender...")
    global ndi_send
    try:
        ndi_send
        return
    except NameError:        
        if not ndi.initialize():
            print("Cannot initialize NDI")

        send_settings = ndi.SendCreate()
        send_settings.ndi_name = name
        ndi_send = ndi.send_create(send_settings)

        
        if ndi_send is None:
            print("Could not initialize NDI sender")

def normalize_image(im):
    return (im - im.min())/(im.max() - im.min())
    
def setup():
    create_canvas(512, 512) #1024, 1024) #512, 512)
    setup_ndi()

def draw():
    background(0)
    
    t = frame_count/200
    # Get two grids one for x's and one for y's 
    x, y = np.meshgrid(np.linspace(-1, 1, width), np.linspace(-1, 1, height))
    # Convert to polar coordinates (angle, radius)
    angle = np.arctan2(y, x)
    r = sqrt(x**2 + y**2)
    # Comment/uncomment for different variants
    # Spiral
    # v = sin(10 * r + 5 * angle + t * TWO_PI * 2)

    # Expanding circles
    #v = sin(20 * r - t * TWO_PI * 4)

    # Pulsing rounded squares
    v = sin((cos(x * PI * 0.5) * sin(y * PI * 0.5) + t * TWO_PI) * 10)

    # Trifoil warp 
    # v = sin(8 * r + 6 * sin(3 * angle + t * TWO_PI) + t*TWO_PI*4)

    # Noisy pattern
    v = sin(noise(x*2)*5 + cos(y*4) + t*TWO_PI)

    # Ripple
    #v = sin((x**2 + y**2)*10 + t*TWO_PI*3)
    
    # Draw it
    image(normalize_image(v))


    # Send frame via NDI
    img = get_image().convert('RGBA')
    video_frame = ndi.VideoFrameV2()
    video_frame.data = img
    video_frame.FourCC = ndi.FOURCC_VIDEO_TYPE_RGBA
    ndi.send_send_video_v2(ndi_send, video_frame)



run()
