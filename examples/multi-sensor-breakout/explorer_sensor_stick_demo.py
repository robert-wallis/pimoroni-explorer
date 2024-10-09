# Display readings from the multi-sensor stick on the Explorer screen
from pimoroni_explorer import display, i2c, BLACK, WHITE, RED
from breakout_ltr559 import BreakoutLTR559
from lsm6ds3 import LSM6DS3
from breakout_bme280 import BreakoutBME280
import time

# Clear all layers first
display.set_layer(0)
display.set_pen(BLACK)
display.clear()
display.set_layer(1)
display.set_pen(BLACK)
display.clear()

try:
    ltr = BreakoutLTR559(i2c)
    lsm = LSM6DS3(i2c)
    bme = BreakoutBME280(i2c)
except OSError:
    # Clear the screen
    display.set_pen(RED)
    display.clear()
    display.set_pen(WHITE)
    display.text("Multi-Sensor stick not detected! :(", 10, 95, 320, 3)
    display.update()

while True:

    # Set the layer we're going to be drawing to.
    display.set_layer(0)

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
