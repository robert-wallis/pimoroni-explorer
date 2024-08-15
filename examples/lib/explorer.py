import gc
from machine import Pin, PWM
from pimoroni_i2c import PimoroniI2C
from servo import Servo
from picographics import PicoGraphics, DISPLAY_EXPLORER

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


class Explorer2350():
    SWITCH_A_PIN = 16
    SWITCH_B_PIN = 15
    SWITCH_C_PIN = 14
    SWITCH_X_PIN = 17
    SWITCH_Y_PIN = 18
    SWITCH_Z_PIN = 19

    I2C_SDA_PIN = 20
    I2C_SCL_PIN = 21

    USER_SW_PIN = 22

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

    AMP_CORRECTION = 4
    DEFAULT_VOLUME = 0.2

    def __init__(self, init_servos=True):
        # Free up hardware resources
        gc.collect()

        self.display = PicoGraphics(display=DISPLAY_EXPLORER)

        # Set up the servos, if the user wants them
        self.servos = None
        if init_servos:
            self.servos = [Servo(self.SERVO_1_PIN - i) for i in range(4)]

        # Set up the i2c for Qw/st and Breakout Garden
        self.i2c = PimoroniI2C(self.I2C_SDA_PIN, self.I2C_SCL_PIN, 100000)

        # Set up the amp enable
        self.__amp_en = Pin(self.AMP_EN_PIN, Pin.OUT)
        self.__amp_en.off()

        self.audio_pwm = PWM(Pin(self.PWM_AUDIO_PIN))
        self.__volume = self.DEFAULT_VOLUME

    def play_tone(self, frequency):
        try:
            self.audio_pwm.freq(frequency)
        except ValueError:
            self.play_silence()
            raise ValueError("frequency of range. Expected greater than 0")

        corrected_volume = (self.__volume ** 4)  # Correct for RC Filter curve
        self.audio_pwm.duty_u16(int(32768 * corrected_volume))
        self.unmute_audio()

    def play_silence(self):
        self.audio_pwm.freq(44100)

        corrected_volume = (self.__volume ** 4)  # Correct for RC Filter curve
        self.audio_pwm.duty_u16(int(32768 * corrected_volume))
        self.unmute_audio()

    def stop_playing(self):
        self.audio_pwm.duty_u16(0)
        self.mute_audio()

    def volume(self, volume=None):
        if volume is None:
            return self.__volume

        if volume < 0.01 or volume > 1.0:
            raise ValueError("volume out of range. Expected 0.0 to 1.0")

        self.__volume = volume

    def mute_audio(self):
        self.__amp_en.off()

    def unmute_audio(self):
        self.__amp_en.on()
