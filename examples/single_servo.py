import time
import math
from pimoroni_explorer import display, servos, SERVO_1, BLACK, WHITE

"""
Demonstrates how to control a single servo on Explorer.
"""

display.set_pen(BLACK)
display.clear()
display.set_pen(WHITE)
display.update()

display.text("Attach a servo to slot 1!", 0, 0, 320, 3)
display.update()
time.sleep(2)

# Access the servo from Explorer and enable it (this puts it at the middle)

s = servos[SERVO_1]

display.text("Enable servo", 0, 50, 320, 3)
display.update()
s.enable()
time.sleep(2)

# Go to min
display.text("Go to min", 0, 70, 320, 3)
display.update()
s.to_min()
time.sleep(2)

# Go to max
display.text("Go to max", 0, 90, 320, 3)
display.update()
s.to_max()
time.sleep(2)

# Go back to mid
display.text("Back to middle", 0, 110, 320, 3)
display.update()
s.to_mid()
time.sleep(2)


SWEEPS = 3              # How many sweeps of the servo to perform
STEPS = 10              # The number of discrete sweep steps
STEPS_INTERVAL = 0.5    # The time in seconds between each step of the sequence
SWEEP_EXTENT = 90.0     # How far from zero to move the servo when sweeping


# Do a sine sweep
display.text(f"Do {SWEEPS} sine sweeps", 0, 130, 320, 3)
display.update()
for j in range(SWEEPS):
    for i in range(360):
        s.value(math.sin(math.radians(i)) * SWEEP_EXTENT)
        time.sleep(0.02)

# Do a stepped sweep
display.text(f"Do {SWEEPS} stepped sweeps", 0, 150, 320, 3)
display.update()
for j in range(SWEEPS):
    for i in range(0, STEPS):
        s.to_percent(i, 0, STEPS, 0.0 - SWEEP_EXTENT, SWEEP_EXTENT)
        time.sleep(STEPS_INTERVAL)
    for i in range(0, STEPS):
        s.to_percent(i, STEPS, 0, 0.0 - SWEEP_EXTENT, SWEEP_EXTENT)
        time.sleep(STEPS_INTERVAL)

# Disable the servo
display.text("Disable servo", 0, 170, 320, 3)
display.update()
s.disable()
