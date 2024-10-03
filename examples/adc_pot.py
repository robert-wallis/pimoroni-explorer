"""
Reads an analog input connected to ADC0.

Connect the middle pin of your potentiometer to ADC0, and the other two pins to 3.3V and GND.
"""

from pimoroni_explorer import display, ADC_0_PIN, BLACK, WHITE
from machine import ADC
import time
import math

# Some constants
WIDTH, HEIGHT = display.get_bounds()
FULL_ANGLE = 300
ADC_REF = 3.3
LENGTH = 50
BG = display.create_pen(70, 130, 180)

# X and Y values for the circle we're going to draw later
x = 250
y = 170

# Setup the ADC for the pot.
pot = ADC(ADC_0_PIN)

while True:
    display.set_pen(BG)
    display.clear()

    # Draw the Title and drop shadow
    display.set_pen(BLACK)
    display.text("ADC: Potentiometer", 19, 8, 320, 3)
    display.set_pen(WHITE)
    display.text("ADC: Potentiometer", 16, 5, 320, 3)

    # read the potentiometer value, it's a number between 0 and 65535 which represents a voltage between 0v and 3.3v
    pot_value = pot.read_u16()
    voltage = round(pot_value * ADC_REF / 65536, 1)
    degrees = (voltage * FULL_ANGLE) / ADC_REF
    rad = math.radians(degrees)

    # Draw the circle outline
    display.set_pen(BLACK)
    display.circle(x, y, LENGTH + 2)

    # Draw the main circle
    display.set_pen(WHITE)
    display.circle(x, y, LENGTH)

    # Draw the line
    display.set_pen(BLACK)
    display.line(x, y, x + int((LENGTH * math.cos(rad))), int(y + (LENGTH * math.sin(rad))))

    # Draw text for the raw values
    display.set_pen(WHITE)
    display.text(f"ADC Value: {pot_value}", 10, 80, 320, 2)
    display.text(f"Voltage Value: {voltage}v", 10, 95, 320, 2)
    display.text(f"Degrees: {degrees}", 10, 110, 320, 2)

    display.update()
    time.sleep(0.1)
