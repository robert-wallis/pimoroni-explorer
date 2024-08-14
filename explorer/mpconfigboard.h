// Board and hardware specific configuration

// Board and hardware specific configuration
#ifndef MICROPY_HW_BOARD_NAME
// Might be defined by mpconfigvariant_VARIANT.cmake
#define MICROPY_HW_BOARD_NAME                   "Pimoroni Explorer"
#endif

// Portion of onboard flash to reserve for the user filesystem
// PGA2350 has 16MB flash, so reserve 2MiB for the firmware and leave 14MiB
#define MICROPY_HW_FLASH_STORAGE_BYTES          (14 * 1024 * 1024)
