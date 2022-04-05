import RPi.GPIO as GPIO
import time,os,signal,sys
import subprocess
import multiprocessing 

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

while True:
    time.sleep(1)
    btn = GPIO.input(4)
    if(btn==1):
        proc = subprocess.Popen(args=['omxplayer','-o','both','VAL.wav'])
        time.sleep(30)
        subprocess.call(['pkill','-P',str(proc.pid)])
        proc.kill()
