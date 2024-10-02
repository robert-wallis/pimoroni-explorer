import time
from lsm6ds3 import LSM6DS3, NORMAL_MODE_104HZ
from pimoroni_explorer import display, i2c, BLACK, WHITE

WIDTH, HEIGHT = display.get_bounds()

# Define our own pen here
BG = display.create_pen(70, 130, 180)

# Create the I2C instance and pass that to LSM6DS3
sensor = LSM6DS3(i2c, mode=NORMAL_MODE_104HZ)

# Text size and Offset for the drop shadow. We'll use these later!
text_size = 9
offset = 3

while True:

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
