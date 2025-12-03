from py5canvas import *
''' Lab: 
    - Can you draw multiple cars with different colors, 
      starting positions and initial orientations?
    - Can you replace the keyboard input code with code that automatically 
    - varies the car's speed and orientation over time?
    - How could you modify this code to draw points 
      along the car's path instead of drawing the car?
'''

class Car:
    def __init__(self, x, y, color, max_speed=10):
        self.position = vector(x, y)
        self.color = color
        self.size = 40
        self.orientation = 0 # in degrees
        self.speed = 0.0
        self.max_speed = max_speed

    def accelerate(self, amount):
        self.speed += amount
        # Clamp speed to max_speed
        self.speed = max(-self.max_speed, min(self.speed, self.max_speed))

    def move(self):
        theta = radians(self.orientation)
        # Move along the vector that defines the car's orientation
        self.position += vector(cos(theta), sin(theta)) * self.speed
        # Keep the car within the canvas bounds (wrapping around)
        if self.position[0] > width:
            self.position[0] -= width
        if self.position[0] < 0:
            self.position[0] += width
        if self.position[1] > height:
            self.position[1] -= height
        if self.position[1] < 0:
            self.position[1] += height

    def turn(self, angle):
        self.orientation = self.orientation + angle

    def display(self):
        push()
        translate(self.position)
        rotate(radians(self.orientation))
        fill(self.color)
        rect_mode(CENTER)
        rect(0, 0, self.size, self.size * 0.5)
        pop()


def setup():
    global car
    create_canvas(400, 400)
    car = Car(width / 2, height / 2, color(255, 0, 0))

def draw():
    background(255)
    if key_is_down('UP'):
        car.accelerate(0.2)
    if key_is_down('DOWN'):
        car.accelerate(-0.2)
    if key_is_down('LEFT'):
        car.turn(-5)
    if key_is_down('RIGHT'):         
        car.turn(5)

    car.move()
    car.display()

run()