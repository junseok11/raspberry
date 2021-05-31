import RPi.GPIO as GPIO
import I2C_driver as LCD
from time import *

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
LED = 12
Switch = 10

GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

mylcd = LCD.lcd()

while True:
    if GPIO.input(Switch) == GPIO.HIGH:
        mylcd.lcd_display_string("LED ON",1)
        GPIO.output(LED,GPIO.HIGH)
    else:
        mylcd.lcd_display_string("LED OFF",1)
        GPIO.output(LED,GPIO.LOW)
