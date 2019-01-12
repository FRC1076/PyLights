import json
try:
    from frc1076lib.udp_channel import UDPChannel as udp
except:
    from lib1076.udp_channel import UDPChannel as udp
from Line import get_line

LOCALIP = "localhost"
LOCALPORT = 8877
REMOTEPORT = 8876
REMOTEIP = "localhost"


def cart_to_neo(location):
    x, y = location
    #check if even
    panel_offset = 255
    if y > 7:
        panel_offset = 0
        y = (y - 8)
    if (x % 2 == 0):
        #x is even
        val = (x * 8) + (7 - y)
    else:
        #x is odd
        val = (x * 8) + y

    return val + panel_offset


class JoyLights:
    def __init__(self, ard_addr, joystick):
        # create a socket to send to the arduion
        # initialize a counter to 0
        self.counter = 0

        self.sender = udp(
            local_ip=LOCALIP,
            local_port=LOCALPORT,
            remote_port=REMOTEPORT,
            remote_ip=REMOTEIP)

    def update_lights(self, position):
        # everth 10th that this is called. do this:
        # read joystick values
        # build json packet
        # send json packet to arduino.
        x, y = position

        if (self.counter == 10):
            self.counter = 0

            l = get_line(
                start=(8, 8), end=(round((x + 1) * 8), round((y + 1) * 8)))
            print(l)
            w = []
            for a in l:
                w.append(cart_to_neo(location=a))
            data = {
                'sender': 'joystick',
                'message': 'raw_display',
                'num_pixels': len(w),
                'pixel_values': w,
                'clear': 1
            }

            message = json.dumps(data)

            print(message)  #for debuging
            self.sender.reply_to(message, REMOTEIP, REMOTEPORT)
        else:
            self.counter += 1
