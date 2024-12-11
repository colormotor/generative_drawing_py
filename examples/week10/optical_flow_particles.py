from py5canvas import *
from PIL import ImageFilter
import cv2


w, h = 400, 400
vin = VideoInput('fingers.mov', size=(w, h))
#vin = VideoInput(size=(w, h))

images = []
particles = []

def setup():
    create_canvas(w, h)

def draw():
    global particles

    img = vin.read().convert('L')
    #img = img.filter(ImageFilter.GaussianBlur(5))
    images.append(np.array(img))
    
    if len(images) > 2:
        images.pop(0)
    image(images[-1]/512)
    if len(images) < 2:
        return
    
    # Clean up dead particles
    # Get rid of "dead" particles:
    # Creates a new list, 
    # re-adding a particle only if the condition on the end is True
    particles = [p for p in particles if p.life >= 0]

    # Optical flow gives us     
    flow = cv2.calcOpticalFlowFarneback(images[0], images[1], None, 0.7, 3, 11, 5, 5, 1.1, 0)

    # This gives us a 3d array with two vector coordinates for each entry 
    # We can get the length of each entry using Pythagoras:
    lengths = np.sqrt(flow[:,:,0]**2 + flow[:,:,1]**2)
    # And then find the maximum length as we did in body glow (fast version)
    max_row, max_col = np.unravel_index(np.argmax(lengths), lengths.shape)
    max_len = lengths[max_row, max_col]
    # Add a particle if length is greater than a threshold
    if max_len > 5.0 and len(particles) < 300:
        particles.append(Particle([max_col, max_row], flow[max_row, max_col]*100))

    stroke(255, 0, 0)
    step = 20
    for i in range(0, h, step):
        for j in range(0, w, step):
            line(j, i, j+flow[i,j,0], i+flow[i,j,1])

    no_stroke()
    for p in particles:
        # Update force based on position
        x = int(p.pos[0])
        y = int(p.pos[1])
        force = np.zeros(2)
        if (x >= 0 and x < flow.shape[1] and
            y >= 0 and y < flow.shape[0]):
            force = flow[y, x]*100
        p.update(1/60, force)
        p.draw()

run()

class Particle:
    def __init__(self, pos, force, lifetime=3.0):
        self.lifetime = lifetime
        self.life = self.lifetime
        self.reset(pos, force)

    def reset(self, pos, force):
        self.pos = np.array(pos).astype(np.float64)
        self.vel = np.zeros(2)
        self.acc = np.array(force)
        self.life = self.lifetime
    
    def update(self, dt, force=np.zeros(2)):
        self.acc += force
        #self.acc += Vector(0, 9.8) # Gravity
        self.vel += self.acc*dt 
        self.pos += self.vel*dt
        self.life -= dt
        
    def draw(self):
        fill(255, 255*(self.life/self.lifetime))
        circle(self.pos, 5)

