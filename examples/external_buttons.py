"""
Connect (up to) 3 external buttons to Explorer.

We're connecting our yellow button to GPIO 0, a red button to GPIO 1 and a blue button to GPIO 3. The other side of each button should be wired to ground.

Note that if you're using our square buttons, you should connect wires to two pins that are diagonally opposite each other.
"""

from machine import Pin
import time
from explorer import Explorer2350

board = Explorer2350()

display = board.display

yellow_button = Pin(0, Pin.IN, Pin.PULL_UP)
blue_button = Pin(1, Pin.IN, Pin.PULL_UP)
red_button = Pin(2, Pin.IN, Pin.PULL_UP)

# lets set up some pen colours to make drawing easier
WHITE = display.create_pen(255, 255, 255)
BLACK = display.create_pen(0, 0, 0)
YELLOW = display.create_pen(0, 255, 255)
BLUE = display.create_pen(0, 0, 255)
RED = display.create_pen(255, 0, 0)


while True:
    display.set_pen(BLACK)
    display.clear()
    display.set_pen(WHITE)
    display.text("Wire up some buttons to GP0, GP1 and GP2, and push 'em!", 0, 0, 320, 4)
    # because we're using Pin.PULL_UP the logic is reversed - '0' is pushed and '1' is unpushed
    if yellow_button.value() == 0:
        display.set_pen(BLACK)
        display.clear()
        display.set_pen(YELLOW)
        display.text("Yellow button pushed", 0, 0, 320, 4)
    if blue_button.value() == 0:
        display.set_pen(BLACK)
        display.clear()
        display.set_pen(BLUE)
        display.text("Blue button pushed", 0, 0, 320, 4)
    if red_button.value() == 0:
        display.set_pen(BLACK)
        display.clear()
        display.set_pen(RED)
        display.text("Red button pushed", 0, 0, 320, 4)
    display.update()
    time.sleep(0.01)
