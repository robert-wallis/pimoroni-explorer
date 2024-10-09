import time
from lsm6ds3 import LSM6DS3, NORMAL_MODE_104HZ
from explorer import display, i2c, BLACK, WHITE

WIDTH, HEIGHT = display.get_bounds()

# Clear all layers first
display.set_layer(0)
display.set_pen(BLACK)
display.clear()
display.set_layer(1)
display.set_pen(BLACK)
display.clear()

# Define our own pen here
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


# Text size and Offset for the drop shadow. We'll use these later!
text_size = 9
offset = 3

while True:

    # Set the layer we're going to be drawing to.
    display.set_layer(0)

    tap = sensor.double_tap_detected()
    start_tick = time.ticks_ms()

    # Clear the screen
    display.set_pen(BG)
    display.clear()

    if tap == 1:
        while (time.ticks_ms() - start_tick < 1000):
            display.set_pen(BLACK)
            display.text("Who's there!?", 10 + offset, 10 + offset, WIDTH, text_size)
            display.set_pen(WHITE)
            display.text("Who's there!?", 10, 10, WIDTH, text_size)
            display.update()

    else:
        display.set_pen(BLACK)
        display.text("Knock Knock..", 10 + offset, 10 + offset, WIDTH, text_size)
        display.set_pen(WHITE)
        display.text("Knock Knock..", 10, 10, WIDTH, text_size)

    # Finally, we tell the screen to update so we can see our work!
    display.update()
