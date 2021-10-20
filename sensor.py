try:
    import RPi.GPIO as GPIO
except ImportError:
    from RPiSim.GPIO import GPIO

GPIO.setmode(GPIO.BCM)  # noqa


class Sensor:
    LIR = 9
    MIR = 11
    RIR = 10

    def __init__(self):
        GPIO.setup(self.LIR, GPIO.IN)
        GPIO.setup(self.MIR, GPIO.IN)
        GPIO.setup(self.RIR, GPIO.IN)

    @property
    def left_ipt(self):
        return GPIO.input(self.LIR)

    @property
    def middle_ipt(self):
        return GPIO.input(self.MIR)

    @property
    def right_ipt(self):
        return GPIO.input(self.RIR)

    def is_centered(self):
        return self.left_ipt == self.right_ipt and self.left_ipt != self.middle_ipt
        # return self.middle_ipt == 0

    def is_left(self):
        return self.left_ipt == self.middle_ipt and self.left_ipt != self.right_ipt

    def is_right(self):
        return self.right_ipt == self.middle_ipt and self.left_ipt != self.right_ipt
