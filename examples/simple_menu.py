import time
from explorer import display, button_a, button_x, button_y, RED, GREEN, BLUE, MAGENTA, BLACK, WHITE

WIDTH, HEIGHT = display.get_bounds()

display.set_backlight(0.8)

# Clear all layers first
display.set_layer(0)
display.set_pen(BLACK)
display.clear()
display.set_layer(1)
display.set_pen(BLACK)
display.clear()


class Menu(object):
    def __init__(self):
        self.items = ["Red", "Green", "Blue", "Magenta"]
        self.selected = 0
        self.shadow_offset = 2
        self.cursor = "<-"
        self.colour = BLACK
        self.title = "Simple Menu"

    # A function to draw only the menu elements.
    def draw_menu(self):
        display.set_layer(0)
        display.set_pen(WHITE)
        display.clear()
        display.set_pen(BLACK)
        length = display.measure_text(self.title, 4)
        display.text(self.title, WIDTH // 2 - length // 2 + self.shadow_offset, 10 + self.shadow_offset, WIDTH, 4)
        display.set_pen(self.colour)
        display.text(self.title, WIDTH // 2 - length // 2, 10, WIDTH, 4)

        display.set_pen(BLACK)
        for item in range(len(self.items)):
            length = display.measure_text(self.items[item], 3)
            if self.selected == item:
                display.set_pen(self.colour)
                display.text(self.cursor, length + 40, HEIGHT // 2 + item * 20, WIDTH, 3)

            display.text(self.items[item], 30, HEIGHT // 2 + item * 20, WIDTH, 3)

            display.set_pen(self.colour)
            display.rectangle(0, HEIGHT - 10, WIDTH, 10)
            display.set_pen(BLACK)

    # Do a thing based on the currently selected menu item
    # For our example we'll be changing the text
    def process_selected(self):
        if self.selected == 0:
            self.colour = RED

        if self.selected == 1:
            self.colour = GREEN

        if self.selected == 2:
            self.colour = BLUE

        if self.selected == 3:
            self.colour = MAGENTA

    def user_input(self):
        # Process the user input and update the currently selected item
        if button_y.value() == 0:
            if self.selected + 1 < len(self.items):
                self.selected += 1
            else:
                self.selected = 0
            time.sleep(0.2)  # debounce

        if button_x.value() == 0:
            if self.selected > 0:
                self.selected -= 1
            else:
                self.selected = len(self.items) - 1
            time.sleep(0.2)  # debounce

        if button_a.value() == 0:
            self.process_selected()
            time.sleep(0.2)  # debounce


menu = Menu()

while True:

    menu.draw_menu()
    menu.user_input()

    display.update()

    time.sleep(1.0 / 20)
