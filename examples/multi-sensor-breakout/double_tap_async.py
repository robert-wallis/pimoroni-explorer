from machine import I2C
from lsm6ds3 import LSM6DS3, NORMAL_MODE_104HZ
from picographics import PicoGraphics, DISPLAY_EXPLORER, PEN_P8
import asyncio

display = PicoGraphics(display=DISPLAY_EXPLORER, pen_type=PEN_P8)

WIDTH, HEIGHT = display.get_bounds()

# Some colours we'll need later on
BG = display.create_pen(70, 130, 180)
WHITE = display.create_pen(255, 255, 255)
BLACK = display.create_pen(0, 0, 0)

# Create the I2C instance and pass that to LSM6DS3
i2c = I2C(0, scl=21, sda=20)
sensor = LSM6DS3(i2c, mode=NORMAL_MODE_104HZ)

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
