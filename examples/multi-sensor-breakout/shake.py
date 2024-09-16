import time
from machine import I2C, Pin
from lsm6ds3 import LSM6DS3, NORMAL_MODE_104HZ
from picographics import PicoGraphics, DISPLAY_EXPLORER, PEN_P8

display = PicoGraphics(display=DISPLAY_EXPLORER, pen_type=PEN_P8)
WIDTH, HEIGHT = display.get_bounds()

# Some colours we'll need later on
WHITE = display.create_pen(255, 255, 255)
BLACK = display.create_pen(0, 0, 0)
RED = display.create_pen(255, 0, 0)
GREEN = display.create_pen(0, 255, 0)
BLUE = display.create_pen(0, 0, 255)
BG = WHITE

# Create the I2C instance and pass that to LSM6DS3
i2c = I2C(0, scl=21, sda=20)
sensor = LSM6DS3(i2c, mode=NORMAL_MODE_104HZ)

# Setup the pins used by the Buttons
button_a = Pin(16, Pin.IN, Pin.PULL_UP)
button_b = Pin(15, Pin.IN, Pin.PULL_UP)
button_c = Pin(14, Pin.IN, Pin.PULL_UP)
button_x = Pin(17, Pin.IN, Pin.PULL_UP)
button_z = Pin(19, Pin.IN, Pin.PULL_UP)


class PALETTE(object):

    def __init__(self):

        self.selected_colour_1 = []
        self.selected_colour_2 = []
        self.mixed_colour = []
        self.mixed_pen = WHITE

    def add_colour(self, colour):

        if not self.selected_colour_1:
            self.selected_colour_1 = colour
        elif not self.selected_colour_2:
            self.selected_colour_2 = colour

    def clear_colours(self):

        self.selected_colour_1 = []
        self.selected_colour_2 = []
        self.mixed_colour = []
        self.mixed_pen = WHITE

    def mix_colours(self):

        if self.selected_colour_1 and self.selected_colour_2:
            self.mixed_colour = [min(a + b, 255) for a, b in zip(self.selected_colour_1, self.selected_colour_2)]
            self.mixed_pen = display.create_pen(self.mixed_colour[0], self.mixed_colour[1], self.mixed_colour[2])

    def process_input(self):

        if button_a.value() == 0:
            self.add_colour([255, 0, 0])
            time.sleep(0.1)

        if button_b.value() == 0:
            self.add_colour([0, 255, 0])
            time.sleep(0.1)

        if button_c.value() == 0:
            self.add_colour([0, 0, 255])
            time.sleep(0.1)

        if button_x.value() == 0:
            self.clear_colours()
            time.sleep(0.1)

        if button_z.value() == 0:
            self.mix_colours()
            time.sleep(0.1)

        if sensor.sig_motion_detected():
            self.mix_colours()
            time.sleep(0.1)

    def draw(self):
        # Clear the screen
        display.set_pen(BG)
        display.clear()

        display.set_pen(RED)
        display.rectangle(0, 25, 29, 29)
        display.circle(30, 39, 14)

        display.set_pen(GREEN)
        display.rectangle(0, 102, 29, 29)
        display.circle(30, 116, 14)

        display.set_pen(BLUE)
        display.rectangle(0, 178, 29, 29)
        display.circle(30, 192, 14)

        display.set_pen(BLUE)
        display.rectangle(0, 178, 29, 29)
        display.circle(30, 192, 14)

        display.set_pen(BLACK)
        display.rectangle(135 + 2, 75 + 2, 100, 100)
        display.set_pen(self.mixed_pen)
        display.rectangle(135, 75, 100, 100)

        if self.selected_colour_1 and self.selected_colour_2:
            display.set_pen(BLACK)
            display.text("SHAKE TO MIX!", 90 + 1, 20 + 1, WIDTH, 3)
            display.text("Press X to Reset", 105, 215, WIDTH, 2)
            display.set_pen(BLUE)
            display.text("SHAKE TO MIX!", 90, 20, WIDTH, 3)

        else:
            display.set_pen(BLACK)
            display.text("<< Select 2 colours", 80 + 1, 20 + 1, WIDTH, 2)
            display.set_pen(BLUE)
            display.text("<< Select 2 colours", 80, 20, WIDTH, 2)

        display.update()


p = PALETTE()

while True:

    p.process_input()
    p.draw()
