# PyLights
Client side utilities for driving remote light displays, such as neo_goi.

Line.py is an implementation of the Bresenham's line algorithm to draw a line in integer space.
        It returns a list of points.    Good for drawing lines on neopixel displays.
        We could AntiLine.py (Wu's algorithm that does anti-aliasing) if someone wants something to do.

joystick.py    Some portion of the joystick interface so we can test a joystick as a source of data.
               This needs an upgrade so that it "moves-around"  just some simple random movements would be fine.

JoyLights.py   Uses joystick position (x,y) as a data source to draw lines on a remote neopixel display.
               Message packet format must be standardized with the neo_goi server command format.


Note:  JoyLights will require communication services that is easily provided by the UDPChannel found in the lib1076.   You'll want to use that.    After you have cloned this repository, you can clone that so that it is inside the directory with your code.   (some day we'll learn how to do git subtrees and have it all work nicely).   But for now, you can just pick up the lastest version to use in your project.
