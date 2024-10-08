"""
This example shows you a simple, non-interrupt way of reading Pico Explorer's buttons with a loop that checks to see if buttons are pressed.
"""
import time
from pimoroni_explorer import button_a, button_b, button_c, button_x, button_y, button_z, display, WHITE, CYAN, MAGENTA, YELLOW, GREEN, BLACK, BLUE, RED


# A little function to save ourselves some time doing the drop shadows :)
def drop_shadow_text(text, x, y, offset, wrap, size, main_colour):

    # Draw the drop shadow
    display.set_pen(BLACK)
    display.text(text, x + offset, y + offset, wrap, size)

    # Draw the main text
    display.set_pen(main_colour)
    display.text(text, x, y, wrap, size)


# sets up a handy function we can call to clear the screen
def clear():
    display.set_pen(WHITE)
    display.clear()
    display.update()


# set up
clear()
display.set_font("bitmap8")
display.set_layer(0)

while True:
    if button_a.value() == 0:
        clear()
        drop_shadow_text("Button A pressed", 65, 75, 2, 240, 4, CYAN)
        display.update()
        time.sleep(1)
        clear()
    elif button_b.value() == 0:
        clear()
        drop_shadow_text("Button B pressed", 65, 75, 2, 240, 4, MAGENTA)
        display.update()
        time.sleep(1)
        clear()
    elif button_c.value() == 0:
        clear()
        drop_shadow_text("Button C pressed", 65, 75, 2, 240, 4, YELLOW)
        display.update()
        time.sleep(1)
        clear()
    elif button_x.value() == 0:
        clear()
        drop_shadow_text("Button X pressed", 65, 75, 2, 240, 4, GREEN)
        display.update()
        time.sleep(1)
        clear()
    elif button_y.value() == 0:
        clear()
        drop_shadow_text("Button Y pressed", 65, 75, 2, 240, 4, RED)
        display.update()
        time.sleep(1)
        clear()
    elif button_z.value() == 0:
        clear()
        drop_shadow_text("Button Z pressed", 65, 75, 2, 240, 4, BLUE)
        display.update()
        time.sleep(1)
        clear()
    else:
        display.set_pen(BLACK)
        drop_shadow_text("Press any button! :)", 65, 75, 2, 240, 4, CYAN)
        display.update()
    time.sleep(0.1)  # this number is how frequently the Pico checks for button presses
