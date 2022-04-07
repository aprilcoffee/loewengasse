import RPi.GPIO as GPIO
import time
import os
import signal
import sys
import subprocess
import multiprocessing
import argparse
from pythonosc import udp_client


parser = argparse.ArgumentParser()
parser.add_argument("--ip", default="127.0.0.1",
                    help="The ip of the OSC server")
parser.add_argument("--port", type=int, default=9527,
                    help="The port the OSC server is listening on")
args = parser.parse_args()

client = udp_client.SimpleUDPClient(args.ip, args.port)

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)

while True:
    time.sleep(1)
    btn = GPIO.input(4)
    if(btn == 1):
        client.send_message("/signal", 1)
