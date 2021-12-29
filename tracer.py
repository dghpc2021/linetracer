try:
    import RPi.GPIO as GPIO
except ImportError:
    from RPiSim.GPIO import GPIO
import time
from motor import Motor
from sensor import Sensor

GPIO.setmode(GPIO.BCM)  # noqa

motor = Motor()
sensor = Sensor()

try:
    motor.forward()
    while True:
        # 추천 속도: 50 ~ 100
        # - 붙이면 반대로 돌아감
        if sensor.is_centered():
            motor.set_individual_speed(60, 60)
            #pass
        elif sensor.is_left():  # 트레이서가 왼쪽으로 기울어진 경우
            motor.set_individual_speed(60, 0)
        elif sensor.is_right():  # 트레이서가 오른쪽으로 기울어진 경우
            motor.set_individual_speed(0, 60)
        else:
            motor.set_individual_speed(0, 0)
except KeyboardInterrupt:
    pass
finally:
    motor.close()
    GPIO.cleanup()
