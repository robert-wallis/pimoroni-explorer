import time
from lsm6ds3 import LSM6DS3, NORMAL_MODE_104HZ
from explorer import display, i2c, button_a, button_b, button_c, button_x, button_z, BLACK, WHITE, RED, GREEN, BLUE

WIDTH, HEIGHT = display.get_bounds()

# Clear all layers first
display.set_layer(0)
display.set_pen(BLACK)
display.clear()
display.set_layer(1)
display.set_pen(BLACK)
display.clear()

BG = display.create_pen(70, 130, 180)

try:
    # Create the I2C instance and pass that to LSM6DS3
    sensor = LSM6DS3(i2c, mode=NORMAL_MODE_104HZ)
except OSError:
    # Clear the screen
    display.set_pen(BG)
    display.clear()
    display.set_pen(WHITE)
    display.text("Multi-Sensor stick not detected! :(", 10, 95, WIDTH, 3)
    display.update()


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

        # Set the layer we're going to be drawing to.
        display.set_layer(0)

        # Clear the screen
        display.set_pen(WHITE)
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
