import time
import pngdec
from machine import I2C
from lsm6ds3 import LSM6DS3, NORMAL_MODE_104HZ
from picographics import PicoGraphics, DISPLAY_EXPLORER, PEN_P8

display = PicoGraphics(display=DISPLAY_EXPLORER, pen_type=PEN_P8)
png = pngdec.PNG(display)

WIDTH, HEIGHT = display.get_bounds()

# Some colours we'll need later on
BG = display.create_pen(255, 99, 71)
WHITE = display.create_pen(255, 255, 255)
BLACK = display.create_pen(0, 0, 0)

# Create the I2C instance and pass that to LSM6DS3
i2c = I2C(0, scl=21, sda=20)
sensor = LSM6DS3(i2c, mode=NORMAL_MODE_104HZ)

# Text size and Offset for the drop shadow. We'll use these later!
text_size = 12
offset = 3

while True:
    # Get the latest step count from the sensor
    steps = sensor.get_step_count()

    # Clear the screen
    display.set_pen(BG)
    display.clear()

    # Open the png and decode it
    try:
        png.open_file("walking.png")
        png.decode(170, 20, scale=1)
    except OSError:
        print("Error: PNG File missing. Copy the PNG file from the example folder to your Pico using Thonny and run the example again.")

    # First we draw the drop shadow, we want this to appear behind our text and offset slightly.
    display.set_pen(BLACK)
    display.text(str(steps), 10 + offset, HEIGHT - 220 + offset, WIDTH, text_size)
    display.text("Steps", 10 + offset, HEIGHT - 80 + offset, WIDTH, 5)

    # Now we draw the main text on top.
    display.set_pen(WHITE)
    length = display.measure_text(str(steps), text_size)
    display.text("Steps", 10, HEIGHT - 80, WIDTH, 5)
    display.text(str(steps), 10, HEIGHT - 220, WIDTH, text_size)

    # Finally, we tell the screen to update so we can see our work!
    display.update()
    time.sleep(0.01)
