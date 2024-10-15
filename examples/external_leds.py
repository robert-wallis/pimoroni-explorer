"""
Connect (up to) 3 LEDs to Explorer and turn them on and off with buttons A, B and C.

Wire the long leg of your LEDs up to GP0, GP1 and GP2. The other leg should be wired to ground.
(Note that you don't need to include a resistor in your circuit to current-limit the LEDs with Explorer, as there are resistors on the board).
"""

from machine import Pin
import time
from explorer import display, button_a, button_b, button_c, BLACK, WHITE

# Set up the LEDs
led_0 = Pin(0, Pin.OUT)
led_1 = Pin(1, Pin.OUT)
led_2 = Pin(2, Pin.OUT)

# Clear all layers first
display.set_layer(0)
display.set_pen(BLACK)
display.clear()
display.set_layer(1)
display.set_pen(BLACK)
display.clear()

# Set the layer we're going to be drawing to.
display.set_layer(0)

# Draw some text to the screen
display.set_pen(WHITE)
display.text("Wire up some LEDs to GP0, GP1 and GP2, and then push buttons A, B and C", 0, 0, 320, 4)
display.update()

while True:
    # Start the loop with all LEDs off
    led_0.off()
    led_1.off()
    led_2.off()
    # Because we're using Pin.PULL_UP the logic is reversed - '0' is pushed and '1' is unpushed
    if button_a.value() == 0:
        led_0.on()
    if button_b.value() == 0:
        led_1.on()
    if button_c.value() == 0:
        led_2.on()
    # Short pause to stop Thonny from falling over
    time.sleep(0.01)
