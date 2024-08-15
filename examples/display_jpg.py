from explorer import Explorer2350
import jpegdec

board = Explorer2350()

display = board.display

# Create a new JPEG decoder for our PicoGraphics
j = jpegdec.JPEG(display)

# Open the JPEG file
j.open_file("backgroundforscreen.jpg")

# Decode the JPEG
j.decode(0, 0, jpegdec.JPEG_SCALE_FULL, dither=True)

# Display the result
display.update()
