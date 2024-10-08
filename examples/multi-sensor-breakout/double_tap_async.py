from pimoroni_explorer import display, i2c, BLACK, WHITE
from lsm6ds3 import LSM6DS3, NORMAL_MODE_104HZ
import asyncio
import sys


WIDTH, HEIGHT = display.get_bounds()

# Define our own pen for the background
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
    sys.exit()

# Text size and Offset for the drop shadow. We'll use these later!
text_size = 10
offset = 3

tap = 0


async def tapped():

    global tap

    while True:

        tap = sensor.double_tap_detected()

        if tap:
            await asyncio.sleep_ms(1000)
        else:
            await asyncio.sleep_ms(10)


async def main():

    global tap
    asyncio.create_task(tapped())
    await asyncio.sleep(0)

    while True:

        # Set the layer we're going to be drawing to.
        display.set_layer(0)

        # Clear the screen
        display.set_pen(BG)
        display.clear()

        if tap == 1:

            display.set_pen(BLACK)
            display.text("Who's there!?", 10 + offset, 10 + offset, WIDTH, text_size)
            display.set_pen(WHITE)
            display.text("Who's there!?", 10, 10, WIDTH, text_size)
        else:
            display.set_pen(BLACK)
            display.text("Knock Knock..", 10 + offset, 10 + offset, WIDTH, text_size)
            display.set_pen(WHITE)
            display.text("Knock Knock..", 10, 10, WIDTH, text_size)

        # Finally, we tell the screen to update so we can see our work!
        display.update()
        await asyncio.sleep_ms(250)

asyncio.run(main())
