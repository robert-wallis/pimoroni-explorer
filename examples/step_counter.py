import time
import pngdec
from lsm6ds3 import LSM6DS3, NORMAL_MODE_104HZ
from explorer import display, i2c, BLACK, WHITE

png = pngdec.PNG(display)

WIDTH, HEIGHT = display.get_bounds()

# Clear all layers first
display.set_layer(0)
display.set_pen(BLACK)
display.clear()
display.set_layer(1)
display.set_pen(BLACK)
display.clear()

# Some colours we'll need later on
BG = display.create_pen(255, 99, 71)

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

# Text size and Offset for the drop shadow. We'll use these later!
text_size = 12
offset = 3

while True:
    # Get the latest step count from the sensor
    steps = sensor.get_step_count()

    # Set the layer we're going to be drawing to.
    display.set_layer(0)

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
