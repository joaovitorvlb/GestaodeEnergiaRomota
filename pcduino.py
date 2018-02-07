import os.path
from os import listdir

path_gpio = os.path.normpath('/sys/devices/virtual/misc/gpio/')

HIGH = 1
LOW = 0
INPUT = 0
OUTPUT = 1
INPUT_PU = 8


class Gpio(object):
    def __init__(self, mode=0,pin=3 ):
        self.mode = mode
        self.pin = pin
        self.ending = 'gpio' + str(self.pin)

        with open(os.path.join(path_gpio, 'mode', self.ending), 'w+') as f:
            f.write("%d\n" % self.mode)


    def write(self, value):
        with open(os.path.join(path_gpio, 'pin', self.ending), 'w+') as f:
            f.write("%d\n" % value)


    def read(self):
        with open(os.path.join(path_gpio, 'pin', self.ending), 'r+') as f:
            value = f.read(16).strip()
        return int(value)


class Adc(object):
    def __init__(self, channel=0):
        self.channel = channel
        self.ADC_PATH= os.path.normpath('/proc/')
        self.ADC_FILENAME = "adc" 

    def read(self):
        with open(os.path.join(self.ADC_PATH, self.ADC_FILENAME + str(self.channel)), 'r+') as f:
            value = int(f.read(32).split(':')[1].strip())
        return value


MAX_PWM_LEVEL = 255
max_value = 0
path_pwm = '/sys/class/misc/pwmtimer/'

class Pwm(object):
    def __init__(self, pin=5, freq=50, value=0):
        self.pin = pin
        self.freq = freq
        self.value = value
        self.ending = 'pwm' + str(self.pin)

        pins = listdir(os.path.join(path_pwm, 'enable'))

        if not self.ending in pins:
            raise ValueError("Pin not found, PWM only possible on " + " ".join(str(p) for p in pins) + ".")

        with open(os.path.join(path_pwm, 'max_level',self.ending)) as f:
            max_value = int(f.read())

        if self.value < 0 or self.value > MAX_PWM_LEVEL:
            raise ValueError("value must be between 0 and %s" % MAX_PWM_LEVEL)

        map_level = ((max_value-1) * self.value) // MAX_PWM_LEVEL
        #-1 because if it puts max_value the duty cycle somehow becomes 0 (overflow)

        #disable -> change level -> enable , as requested by documentation
        with open(os.path.join(path_pwm, 'enable', self.ending), 'w+') as f:
            f.write("0\n")

        with open(os.path.join(path_pwm, 'level', self.ending), 'w+') as f:
            f.write("%d\n" % map_level)


    def write(self, value):
         level = ((max_value-1) * value) // MAX_PWM_LEVEL
         with open(os.path.join(path_pwm, 'level', self.ending), 'w+') as f:
            f.write("%d\n" % level)

    def stop(self):
        with open(os.path.join(path_pwm, 'enable', self.ending), 'w+') as f:
            f.write("0\n")

    def start(self):
        with open(os.path.join(path_pwm, 'enable', self.ending), 'w+') as f:
            f.write("1\n")


        