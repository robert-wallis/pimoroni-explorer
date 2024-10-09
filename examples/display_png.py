# Display a PNG image on Pimoroni Explorer

from pimoroni_explorer import display
import pngdec
import gc

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
