
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


def setup():
    create_canvas(512, 512) #1024, 1024) #512, 512)
    setup_ndi()

def draw():
    background(0)
    translate(center)
    rect_mode(CENTER)
    n = 7 
    for i in range(n):
        w = remap(i, 0, n-1, width, 20)
        v = sin(frame_count*0.05 + i*0.8) * 0.5 + 0.5
        fill(v*255)
        square(0, 0, w)

    # Send frame via NDI
    img = get_image().convert('RGBA')
    video_frame = ndi.VideoFrameV2()
    video_frame.data = img
    video_frame.FourCC = ndi.FOURCC_VIDEO_TYPE_RGBA
    ndi.send_send_video_v2(ndi_send, video_frame)



run()
