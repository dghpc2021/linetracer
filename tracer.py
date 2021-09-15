try:
    import RPi.GPIO as GPIO
except ImportError:
    from RPiSim.GPIO import GPIO
import time

GPIO.setmode(GPIO.BCM)  # noqa

ENA = 2
IN1 = 3
IN2 = 4
IN3 = 17
IN4 = 27
ENB = 22

GPIO.setup(ENA, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN1, GPIO.OUT, initial=GPIO.LOW)

GPIO.setup(IN2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN3, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN4, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ENB, GPIO.OUT, initial=GPIO.LOW)

enap = GPIO.PWM(ENA, 200)  # noqa
enbp = GPIO.PWM(ENB, 200)  # noqa
enap.start(0)
enbp.start(0)

try:
    while True:
        ipt = int(input("speed: "))
        enap.ChangeDutyCycle(ipt)
        enbp.ChangeDutyCycle(ipt)
        # GPIO.output(ENA, GPIO.HIGH)  # noqa
        # GPIO.output(ENB, GPIO.HIGH)  # noqa
        
        GPIO.output(IN1, GPIO.LOW)  # noqa
        GPIO.output(IN2, GPIO.HIGH)  # noqa
        GPIO.output(IN3, GPIO.LOW)  # noqa
        GPIO.output(IN4, GPIO.HIGH)  # noqa
        time.sleep(5)
except KeyboardInterrupt:
    pass
finally:
        
    GPIO.output(IN1, GPIO.LOW)  # noqa
    GPIO.output(IN2, GPIO.LOW)  # noqa
    GPIO.output(IN3, GPIO.LOW)  # noqa
    GPIO.output(IN4, GPIO.LOW)  # noqa
    GPIO.cleanup()
