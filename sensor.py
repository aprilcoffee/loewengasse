import RPi.GPIO as GPIO
import time
import os
import signal
import sys
import subprocess
import multiprocessing
from OSC import OSCServer,OSCClient, OSCMessage

client = OSCClient()
client.connect(('172.20.10.2', 9527))


GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN)

while True:
    time.sleep(1)
    btn = GPIO.input(26)
    if(btn == 1):
        oscmsg = OSCMessage()
        oscmsg.setAddress("/msg")
        oscmsg.append(1)
        client.send(oscmsg)

    print(btn)
