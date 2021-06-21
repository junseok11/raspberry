import RPi.GPIO as GPIO 
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(10, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(12,GPIO.OUT)

while True:
    GPIO.output(12,GPIO.LOW)
    if GPIO.input(10) ==1:
        GPIO.output(12,GPIO.HIGH)
    else GPIO.input(10) ==0: //스위치가 눌리지 않았을 때
        GPIO.output(12,GPIO.LOW)
