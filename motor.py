try:
    import RPi.GPIO as GPIO
except ImportError:
    from RPiSim.GPIO import GPIO

GPIO.setmode(GPIO.BCM)  # noqa


class Motor:
    ENA = 2
    IN1 = 3
    IN2 = 4
    IN3 = 17
    IN4 = 27
    ENB = 22

    def __init__(self):
        GPIO.setup(self.ENA, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.IN1, GPIO.OUT, initial=GPIO.LOW)

        GPIO.setup(self.IN2, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.IN3, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.IN4, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.ENB, GPIO.OUT, initial=GPIO.LOW)

        self.enap = GPIO.PWM(self.ENA, 200)  # noqa
        self.enbp = GPIO.PWM(self.ENB, 200)  # noqa
        self.enap.start(0)
        self.enbp.start(0)

        self.__speed = 100
        self.__speed_left = 100
        self.__speed_right = 100

    def close(self):
        GPIO.output(self.IN1, GPIO.LOW)  # noqa
        GPIO.output(self.IN2, GPIO.LOW)  # noqa
        GPIO.output(self.IN3, GPIO.LOW)  # noqa
        GPIO.output(self.IN4, GPIO.LOW)  # noqa

    def forward(self):
        GPIO.output(self.IN1, GPIO.LOW)  # noqa
        GPIO.output(self.IN2, GPIO.HIGH)  # noqa
        GPIO.output(self.IN3, GPIO.HIGH)  # noqa
        GPIO.output(self.IN4, GPIO.LOW)  # noqa

    def backward(self):
        GPIO.output(self.IN1, GPIO.HIGH)  # noqa
        GPIO.output(self.IN2, GPIO.LOW)  # noqa
        GPIO.output(self.IN3, GPIO.LOW)  # noqa
        GPIO.output(self.IN4, GPIO.HIGH)  # noqa

    def right(self):
        GPIO.output(self.IN1, GPIO.LOW)  # noqa
        GPIO.output(self.IN2, GPIO.HIGH)  # noqa
        GPIO.output(self.IN3, GPIO.LOW)  # noqa
        GPIO.output(self.IN4, GPIO.HIGH)  # noqa

    def left(self):
        GPIO.output(self.IN1, GPIO.HIGH)  # noqa
        GPIO.output(self.IN2, GPIO.LOW)  # noqa
        GPIO.output(self.IN3, GPIO.HIGH)  # noqa
        GPIO.output(self.IN4, GPIO.LOW)  # noqa

    def set_speed(self, speed: int):
        self.__speed_left = speed
        self.__speed_right = speed
        self.enap.ChangeDutyCycle(self.__speed_left)
        self.enbp.ChangeDutyCycle(self.__speed_right)

    def set_individual_speed(self, left_speed: int = None, right_speed: int = None):
        self.__speed_left = left_speed
        self.__speed_right = right_speed
        self.enap.ChangeDutyCycle(self.__speed_left)
        self.enbp.ChangeDutyCycle(self.__speed_right)
