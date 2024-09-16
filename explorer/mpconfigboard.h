// Board and hardware specific configuration

#define MICROPY_HW_BOARD_NAME                   "Pimoroni Explorer"

// Reserve 2MB for MicroPython, leaving the rest for the user filesystem
#define MICROPY_HW_FLASH_STORAGE_BYTES          (PICO_FLASH_SIZE_BYTES - (2 * 1024 * 1024))
