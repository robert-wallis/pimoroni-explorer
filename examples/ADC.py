"""
Reads an analog input connected to ADC0.

Connect the middle pin of your potentiometer to ADC0, and the other two pins to 3.3V and GND.
"""

from explorer import Explorer2350
from machine import ADC
import time

board = Explorer2350()

display = board.display

# lets set up some pen colours to make drawing easier
WHITE = display.create_pen(255, 255, 255)
BLACK = display.create_pen(0, 0, 0)

pot = ADC(0)

# alternatively, you could specify the pin number like this:
# pot = ADC(40)

while True:
    display.set_pen(BLACK)
    display.clear()
    display.set_pen(WHITE)
    # read the potentiometer value, it's a number between 0 and 65535 which represents a voltage between 0v and 3.3v
    pot_value = pot.read_u16()
    display.text(f"{pot_value}", 0, 0, 320, 4)
    display.update()
    time.sleep(0.1)
