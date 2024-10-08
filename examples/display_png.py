# Display a PNG image on Pimoroni Explorer

from pimoroni_explorer import display, BLACK
import pngdec
import gc

# Clear all layers first
display.set_layer(0)
display.set_pen(BLACK)
display.clear()
display.set_layer(1)
display.set_pen(BLACK)
display.clear()

# Set the layer we're going to be drawing to.
display.set_layer(0)

# run garbage collection - displaying large PNGs is resource intensive
gc.collect()

# Create a new JPEG decoder for our PicoGraphics
p = pngdec.PNG(display)

# Open the PNG file
p.open_file("backgroundforscreen.png")

# Decode the PNG
p.decode(0, 0)

# Display the result
display.update()
