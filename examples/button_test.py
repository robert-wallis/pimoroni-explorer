"""
This example shows you a simple, non-interrupt way of reading Pico Explorer's buttons with a loop that checks to see if buttons are pressed.
"""
import time
from pimoroni_explorer import button_a, button_b, button_c, button_x, button_y, button_z, display, WHITE, CYAN, MAGENTA, YELLOW, GREEN, BLACK


# sets up a handy function we can call to clear the screen
def clear():
    display.set_pen(BLACK)
    display.clear()
    display.update()


# set up
clear()
display.set_font("bitmap8")

while True:
    if button_a.value() == 0:                             # if a button press is detected then...
        clear()                                           # clear to black
        display.set_pen(WHITE)                            # change the pen colour
        display.text("Button A pressed", 10, 10, 240, 4)  # display some text on the screen
        display.update()                                  # update the display
        time.sleep(1)                                     # pause for a sec
        clear()                                           # clear to black again
    elif button_b.value() == 0:
        clear()
        display.set_pen(CYAN)
        display.text("Button B pressed", 10, 10, 240, 4)
        display.update()
        time.sleep(1)
        clear()
    elif button_c.value() == 0:
        clear()
        display.set_pen(CYAN)
        display.text("Button C pressed", 10, 10, 240, 4)
        display.update()
        time.sleep(1)
        clear()
    elif button_x.value() == 0:
        clear()
        display.set_pen(MAGENTA)
        display.text("Button X pressed", 10, 10, 240, 4)
        display.update()
        time.sleep(1)
        clear()
    elif button_y.value() == 0:
        clear()
        display.set_pen(YELLOW)
        display.text("Button Y pressed", 10, 10, 240, 4)
        display.update()
        time.sleep(1)
        clear()
    elif button_z.value() == 0:
        clear()
        display.set_pen(YELLOW)
        display.text("Button Z pressed", 10, 10, 240, 4)
        display.update()
        time.sleep(1)
        clear()
    else:
        display.set_pen(GREEN)
        display.text("Press any button!", 10, 10, 240, 4)
        display.update()
    time.sleep(0.1)  # this number is how frequently the Pico checks for button presses
