import gc
from machine import Pin, PWM
from pimoroni_i2c import PimoroniI2C
from servo import Servo
from picographics import PicoGraphics, DISPLAY_EXPLORER
from micropython import const

display = PicoGraphics(display=DISPLAY_EXPLORER)

# IO Pin Constants
GP0 = 0
GP1 = 1
GP2 = 2
GP3 = 3
GP4 = 4
GP5 = 5

A0 = 40
A1 = 41
A2 = 42
A3 = 43
A4 = 44
A5 = 45

GPIOS = (GP0, GP1, GP2, GP3, GP4, GP5, A0, A1, A2, A3, A4, A5)
ADCS = (A0, A1, A2, A3, A4, A5)

# Index Constants
SERVO_1 = 0
SERVO_2 = 1
SERVO_3 = 2
SERVO_4 = 3

SWITCH_A = 0
SWITCH_B = 1
SWITCH_C = 2
SWITCH_X = 3
SWITCH_Y = 4
SWITCH_Z = 5

# Count Constants
NUM_GPIOS = 6
NUM_ADCS = 6
NUM_SERVOS = 4
NUM_SWITCHES = 6

# Colours!
WHITE = display.create_pen(255, 255, 255)
BLACK = display.create_pen(0, 0, 0)
CYAN = display.create_pen(0, 255, 255)
MAGENTA = display.create_pen(255, 0, 255)
YELLOW = display.create_pen(255, 255, 0)
GREEN = display.create_pen(0, 255, 0)

SWITCH_A_PIN = const(16)
SWITCH_B_PIN = const(15)
SWITCH_C_PIN = const(14)
SWITCH_X_PIN = const(17)
SWITCH_Y_PIN = const(18)
SWITCH_Z_PIN = const(19)

I2C_SDA_PIN = const(20)
I2C_SCL_PIN = const(21)

USER_SW_PIN = const(22)

SERVO_1_PIN = const(9)
SERVO_2_PIN = const(8)
SERVO_3_PIN = const(7)
SERVO_4_PIN = const(6)

ADC_0_PIN = const(40)
ADC_1_PIN = const(41)
ADC_2_PIN = const(42)
ADC_3_PIN = const(43)
ADC_4_PIN = const(44)
ADC_5_PIN = const(45)

GPIO_0_PIN = const(0)
GPIO_1_PIN = const(1)
GPIO_2_PIN = const(2)
GPIO_3_PIN = const(3)
GPIO_4_PIN = const(4)
GPIO_5_PIN = const(5)

PWM_AUDIO_PIN = const(12)
AMP_EN_PIN = const(13)

AMP_CORRECTION = const(4)
DEFAULT_VOLUME = const(0.2)


class PimoroniExplorer():
    
    def __init__(self, init_servos=True):
        # Free up hardware resources
        gc.collect()

        self.display = display

        # Set up the servos, if the user wants them
        self.servos = None
        if init_servos:
            self.servos = [Servo(SERVO_1_PIN - i) for i in range(4)]

        # Set up the i2c for Qw/st and Breakout Garden
        self.i2c = PimoroniI2C(I2C_SDA_PIN, I2C_SCL_PIN, 100000)

        # Set up the amp enable
        self._amp_en = Pin(AMP_EN_PIN, Pin.OUT)
        self._amp_en.off()

        self.audio_pwm = PWM(Pin(PWM_AUDIO_PIN))
        self._volume = DEFAULT_VOLUME

        # Setup the pins for the buttons
        self.button_a = Pin(SWITCH_A_PIN, Pin.IN, Pin.PULL_UP)
        self.button_b = Pin(SWITCH_B_PIN, Pin.IN, Pin.PULL_UP)
        self.button_c = Pin(SWITCH_C_PIN, Pin.IN, Pin.PULL_UP)
        self.button_x = Pin(SWITCH_X_PIN, Pin.IN, Pin.PULL_UP)
        self.button_y = Pin(SWITCH_Y_PIN, Pin.IN, Pin.PULL_UP)
        self.button_z = Pin(SWITCH_Z_PIN, Pin.IN, Pin.PULL_UP)

    def play_tone(self, frequency):
        try:
            self.audio_pwm.freq(frequency)
        except ValueError:
            self.play_silence()
            raise ValueError("frequency of range. Expected greater than 0")

        corrected_volume = (self._volume ** 4)  # Correct for RC Filter curve
        self.audio_pwm.duty_u16(int(32768 * corrected_volume))
        self.mute_audio(False)

    def play_silence(self):
        self.audio_pwm.freq(44100)

        corrected_volume = (self._volume ** 4)  # Correct for RC Filter curve
        self.audio_pwm.duty_u16(int(32768 * corrected_volume))
        self.mute_audio(False)

    def stop_playing(self):
        self.audio_pwm.duty_u16(0)
        self.mute_audio(True)

    def set_volume(self, volume=None):
        if volume is None:
            return self._volume

        if volume < 0.01 or volume > 1.0:
            raise ValueError("volume out of range. Expected 0.0 to 1.0")

        self._volume = volume

    def mute_audio(self, value=True):
        self._amp_en.off() if value else self._amp_en.on()
