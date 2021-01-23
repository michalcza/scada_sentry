#RELAY TEST
import RPi.GPIO as GPIO
import time

in1 = 16
in2 = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)

GPIO.output(in1, False)
GPIO.output(in2, False)

try:
      for x in range(5):
            GPIO.output(in1, True)
            time.sleep(0.5)
            GPIO.output(in1, False)
            GPIO.output(in2, True)
            time.sleep(0.5)
            GPIO.output(in2, False)
      
      GPIO.output(in1,True)
      GPIO.output(in2,True)



except KeyboardInterrupt:
    GPIO.cleanup()