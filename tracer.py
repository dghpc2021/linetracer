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
        """
        direction = input("dir: ")
        if direction.startswith("f"):
            motor.forward()
        elif direction.startswith("b"):
            motor.backward()
        elif direction.startswith("l"):
            motor.left()
        elif direction.startswith("r"):
            motor.right()
        ipt = int(input("speed: "))
        motor.set_speed(ipt)
        print(sensor.left_ipt, sensor.middle_ipt, sensor.right_ipt)
        time.sleep(5)
        """
        # 추천 속도: 50 ~ 100
        # - 붙이면 반대로 돌아감
        if sensor.is_centered():
            pass
        elif sensor.is_left():  # 트레이서가 왼쪽으로 기울어진 경우
            motor.set_individual_speed(..., ...)
        elif sensor.is_right():  # 트레이서가 오른쪽으로 기울어진 경우
            motor.set_individual_speed(..., ...)
        else:
            ...
except KeyboardInterrupt:
    pass
finally:
    motor.close()
    GPIO.cleanup()
