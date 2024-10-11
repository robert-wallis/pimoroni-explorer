# Pimoroni Explorer- Library Reference <!-- omit in toc -->

This is the library reference for the [Pimoroni Explorer](https://shop.pimoroni.com/products/explorer), an electronics adventure playground, powered by the Raspberry Pi RP2350.

It's split into three main sections for your convenience:

- [Explorer Library](#explorer-library)
  - [Getting Started](#getting-started)
  - [Reading the Switches](#reading-the-switches)
  - [`explorer` Reference](#explorer-reference)
    - [Index Constants](#index-constants)
    - [Count Constants](#count-constants)
    - [Colour Constants](#colour-constants)
    - [Pin Constants](#pin-constants)
    - [Audio Constants](#audio-constants)
    - [Variables](#variables)
    - [Functions](#functions)
- [PicoGraphics](#picographics)
  - [Basic Drawing Functions](#basic-drawing-functions)
  - [Changing The Display Mode](#changing-the-display-mode)
  - [JPEG Decoding](#jpeg-decoding)
  - [PNG Decoding](#png-decoding)
- [PicoVector](#picovector)
  - [Setup \& Anti-aliasing](#setup--anti-aliasing)
  - [Shapes \& Primitives](#shapes--primitives)
  - [Fonts \& Text](#fonts--text)

# Explorer Library

The [explorer library](examples/lib/explorer.py) is a wrapper around some of Explorer's particulars. It aims to get you set up with a PicoGraphics surface for drawing, and help you find the right pins for the many inputs and outputs.

## Getting Started

To start coding your Pimoroni Explorer, you will need to add the following line to the start of your code file:

```python
import explorer
```

...

## Reading the Switches

...


## `explorer` Reference

### Index Constants

```python
SERVO_1 = 0
SERVO_2 = 1
SERVO_3 = 2
SERVO_4 = 3
```

### Count Constants

These handy constants tell you how many of something Explorer has.

```python
NUM_GPIOS = 6
NUM_ADCS = 6
NUM_SERVOS = 4
NUM_SWITCHES = 6
```

### Colour Constants

These are RGB565 colours for Explorer's default PicoGraphics instance.

```python
WHITE = 65535   # 255, 255, 255
BLACK = 0       # 0,   0,   0
CYAN = 65287    # 0,   255, 255
MAGENTA = 8184  # 255, 0,   255
YELLOW = 57599  # 255, 255, 0
GREEN = 57351   # 0,   255, 0
RED = 248       # 255, 0,   0
BLUE = 7936     # 0,   0,   255
```

If you're wondering how these baffling numbers are arrived at, we start with three 8-bit values for Red, Green and Blue:

```
red = RRRRRRRR 
green = GGGGGGGG
blue = BBBBBBBB
```

Then we chop them down to 5, 6 and 5 bits respectively:

```
red = RRRRR
green = GGGGGG
blue = BBBBBB
```

And stick them together:

```
rgb565 = RRRRRGGGGGGBBBBB
```

And byteswap them (swap the lower 8 bits with the upper 8 bits, for reasons):

```
rgb565 = GGGBBBBBRRRRRGGG
```

And that's why 255 red, or `0b0000000011111000` equals 248.

### Pin Constants

Constants for all the pins you might need to access on Explorer:

```python
SWITCH_A_PIN = 16
SWITCH_B_PIN = 15
SWITCH_C_PIN = 14
SWITCH_X_PIN = 17
SWITCH_Y_PIN = 18
SWITCH_Z_PIN = 19
SWITCH_USER_PIN = 22

I2C_SDA_PIN = 20
I2C_SCL_PIN = 21

SERVO_1_PIN = 9
SERVO_2_PIN = 8
SERVO_3_PIN = 7
SERVO_4_PIN = 6

ADC_0_PIN = 40
ADC_1_PIN = 41
ADC_2_PIN = 42
ADC_3_PIN = 43
ADC_4_PIN = 44
ADC_5_PIN = 45

GPIO_0_PIN = 0
GPIO_1_PIN = 1
GPIO_2_PIN = 2
GPIO_3_PIN = 3
GPIO_4_PIN = 4
GPIO_5_PIN = 5

PWM_AUDIO_PIN = 12
AMP_EN_PIN = 13
```

### Audio Constants

```python
AMP_CORRECTION = 4
DEFAULT_VOLUME = 0.2
```

### Variables

Defines a few values that you'll probably use most:

* `i2c` - A `machine.I2C` compatible I2C instance for I2C devices connected to the Qw/St socket
* `audio_pwm` - A `machine.PWM` instance to drive the piezo for beeps and boops
* `servos` - A list containing four `Servo` instances for driving the four servo connectors
* `display` - A PicoGraphics instance, configured in RGB565 pen mode with two drawing layers
* `button_<BTN>` - A collection of six `machine.Pin` instances for reading the onboard button
* `button_user` - A `machine.Pin` instance for reading the user / boot button

```python
i2c: PimoroniI2C
audio_pwm: PWM

button_a: Pin
button_b: Pin
button_c: Pin
button_x: Pin
button_y: Pin
button_z: Pin
button_user: Pin

display: PicoGraphics

servos: list[Servo]
```

### Functions

```python
play_tone(frequency: float) -> None
play_silence() -> None
stop_playing() -> None
set_volume(volume: float=None) -> None
mute_audio(value: bool=True) -> None
```

# PicoGraphics

Explorer, like all of our display products, uses our in-house framebuffer graphics library - PicoGraphics.

PicoGraphics is a wrapper around a big ol' chunk of RAM, which corresponds to the pixels on an attached display. By default, Explorer is configured in RGB565 mode which corresponds to two bytes per pixel, or 5 bits of red, 6 bits of green and 5 bits of blue respectively. It's also known as 65k colour, and does a pretty good job of making pretty pictures at half (rather than 2/3rds) the RAM cost (for awkward technical reasons) of RGB888.

## Basic Drawing Functions

Since there are many, many things you can do with PicoGraphics that would be silly to repeat here, I'll send you over to our main MicroPython repository for [a full PicoGraphics function reference.][https://github.com/pimoroni/pimoroni-pico/blob/main/micropython/modules/picographics/README.md#function-reference]

## Changing The Display Mode

You can replace `explorer.display` by just creating a PicoGraphics instance as normal, for example switching into RGB332 mode (1 byte per pixel) to save RAM can be done by just replacing `explorer.display`:

```python
from picographics import PicoGraphics, DISPLAY_EXPLORER, PEN_RGB332
explorer.display = PicoGraphics(display=DISPLAY_EXPLORER, pen_type=PEN_RGB332, layers=2)
```

We use two layers by default, since that extra layer is handy for static backgrounds and other fun drawing tricks.

## JPEG Decoding

## PNG Decoding

# PicoVector

## Setup & Anti-aliasing

## Shapes & Primitives

## Fonts & Text
