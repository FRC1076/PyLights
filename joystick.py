from JoyLights import JoyLights
import random, time

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
jl = JoyLights('10.10.76.7', js)

movements = [(1,1), (.1,.1), (.5,1,), (.3,-.4), (-1,.5), (-.5,.6), (0,-.7), (-.9,.9), (.4,.9), (-.7,-.3), (.6,-.6)]
for m in movements:
    jl.update_lights((m[0], m[1]))
    time.sleep(1)
