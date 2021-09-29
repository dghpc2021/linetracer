try:
    import RPi.GPIO as GPIO
except ImportError:
    from RPiSim.GPIO import GPIO
import time
from motor import Motor

GPIO.setmode(GPIO.BCM)  # noqa

motor = Motor()

try:
    motor.forward()
    while True:
        ipt = int(input("speed: "))
        motor.set_speed(ipt)
        time.sleep(5)
except KeyboardInterrupt:
    pass
finally:
        
    GPIO.output(IN1, GPIO.LOW)  # noqa
    GPIO.output(IN2, GPIO.LOW)  # noqa
    GPIO.output(IN3, GPIO.LOW)  # noqa
    GPIO.output(IN4, GPIO.LOW)  # noqa
    GPIO.cleanup()
