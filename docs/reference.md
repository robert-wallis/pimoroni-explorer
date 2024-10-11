# Pimoroni Explorer- Library Reference <!-- omit in toc -->

This is the library reference for the [Pimoroni Explorer](https://shop.pimoroni.com/products/explorer), an electronics adventure playground, powered by the Raspberry Pi RP2350.


## Table of Content <!-- omit in toc -->
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


## Getting Started

To start coding your Pimoroni Explorer, you will need to add the following line to the start of your code file.

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
```python
NUM_GPIOS = 6
NUM_ADCS = 6
NUM_SERVOS = 4
NUM_SWITCHES = 6
```

### Colour Constants
```python
WHITE = 65535
BLACK = 0
CYAN = 65287
MAGENTA = 8184
YELLOW = 57599
GREEN = 57351
RED = 248
BLUE = 7936
```

### Pin Constants
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