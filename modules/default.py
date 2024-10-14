# Include the manifest.py from micropython/ports/rp2/boards/manifest.py
include("$(PORT_DIR)/boards/manifest.py")

# Include the manifest.py from micropython/<board>/manifest.py
include("$(BOARD_DIR)/manifest.py")

# Freeze modules/py_frozen
freeze("py_frozen/")

# Freeze pimoroni.py
freeze("../../pimoroni-pico/micropython/modules_py/", "pimoroni.py")