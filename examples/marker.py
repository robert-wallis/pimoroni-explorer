import time

import explorer
from picovector import ANTIALIAS_NONE, HALIGN_CENTER, PicoVector

vector = PicoVector(explorer.display)

FONT_SIZE = 70

vector.set_antialiasing(ANTIALIAS_NONE)
vector.set_font("marker.af", FONT_SIZE)
vector.set_font_size(FONT_SIZE)
vector.set_font_line_height(70)
vector.set_font_align(HALIGN_CENTER)

BG = explorer.display.create_pen(0, 150, 190)
FG = explorer.display.create_pen(0, 100, 126)
BLACK = explorer.BLACK


text = """Permanent
marker"""

x, y, w, h = vector.measure_text(text)

x = int((320 - w) / 2)
y = int((240 - h) / 2) + (FONT_SIZE // 2)

explorer.display.set_layer(1)
explorer.display.set_pen(BG)
explorer.display.clear()

explorer.display.set_pen(FG)
vector.text(text, x, y + 4)
explorer.display.set_pen(BLACK)
vector.text(text, x, y)


explorer.display.set_layer(0)

GRADIENT_WIDTH = 320 * 4

rgb = [explorer.display.create_pen_hsv(x / GRADIENT_WIDTH, 1.0, 1.0) for x in range(GRADIENT_WIDTH)]

while True:
    o = time.ticks_ms() // 10
    for x in range(320):
        explorer.display.set_pen(rgb[(x + o) % GRADIENT_WIDTH])
        explorer.display.line(x, 0, x, 240)
    explorer.display.update()
