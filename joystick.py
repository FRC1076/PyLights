from JoyLights import JoyLights
import random

RIGHT = 0
LEFT = 1


class joystick():
    def __init__(self):
        self.x = 0
        self.y = 1

    def getX(self, ignore):
        #self.x += 1
        self.x = 1
        return self.x

    def getY(self, ignore_this_to):
        #self.y += 1

        self.y = 1
        return self.y


js = joystick()
jl = JoyLights('localhost', js)

for i in range(100):
    jl.update_lights([js.getX(1), js.getY(1)])
