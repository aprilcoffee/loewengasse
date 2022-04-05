import RPi.GPIO as GPIO
import time,os,signal,sys
import subprocess
import multiprocessing

GPIO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

while True:
    time.sleep(1)
    btn = GPIO.input(14)
    print(btn)
