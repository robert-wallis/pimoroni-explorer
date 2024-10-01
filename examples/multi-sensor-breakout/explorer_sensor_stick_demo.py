# Display readings from the multi-sensor stick on the Explorer screen
from pimoroni_explorer import PimoroniExplorer
from breakout_ltr559 import BreakoutLTR559
from lsm6ds3 import LSM6DS3
from breakout_bme280 import BreakoutBME280
import time

board = PimoroniExplorer()

ltr = BreakoutLTR559(board.i2c)
lsm = LSM6DS3(board.i2c)
bme = BreakoutBME280(board.i2c)

display = board.display

# lets set up some pen colours to make drawing easier
WHITE = display.create_pen(255, 255, 255)
BLACK = display.create_pen(0, 0, 0)
RED = display.create_pen(255, 0, 0)
GREY = display.create_pen(125, 125, 125)

while True:
    lux, _, _, _, _, _, prox = ltr.get_reading()
    ax, ay, az, gx, gy, gz = lsm.get_readings()
    temperature, pressure, humidity = bme.read()
    display.set_pen(BLACK)
    display.clear()
    display.set_pen(WHITE)
    if lux is not None:
        display.text(f"Lux: {lux:.0f}\nProx: {prox:.0f}", 0, 0, 320, 3)
    if ax is not None:
        display.text(f"Accelerometer:\nX: {ax:.0f}, Y: {ay:.0f}, \nZ: {az:.0f}\nGyro:\nX: {gx:.0f}, Y: {gy:.0f}, \nZ: {gz:.0f}", 0, 45, 320, 3)
    if temperature is not None:
        display.text(f"Temperature: {temperature:.2f}°C,\nHumidity: {humidity:.0f}%,\nPressure: {pressure / 100:.0f}hPa", 0, 180, 320, 3)
    display.update()
    time.sleep(0.1)
