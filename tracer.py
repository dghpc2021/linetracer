try:
    import RPi.GPIO as GPIO
except ImportError:
    from RPiSim.GPIO import GPIO
import time
from motor import Motor

GPIO.setmode(GPIO.BCM)  # noqa

motor = Motor()

IR_LEFT = 9
IR_MIDDLE = 11
IR_RIGHT = 10

ir_left = GPIO.setup(IR_LEFT, GPIO.IN)
ir_middle = GPIO.setup(IR_MIDDLE, GPIO.IN)
ir_right = GPIO.setup(IR_RIGHT, GPIO.IN)

try:
    motor.forward()
    while True:
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
        print(GPIO.input(IR_LEFT), GPIO.input(IR_MIDDLE), GPIO.input(IR_RIGHT))
        time.sleep(5)
except KeyboardInterrupt:
    pass
finally:
    motor.close()
    GPIO.cleanup()
