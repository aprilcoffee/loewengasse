import time
import os
import signal
import sys
import subprocess
import multiprocessing

from pythonosc import dispatcher
from pythonosc import osc_server
import argparse
import math

counter = 0

def playsound(unused_addr, args, signal):
    global counter
    if(counter == 0):
        time.sleep(5)
        proc1 = subprocess.Popen(args=['omxplayer', '-o', 'both', 'val1.mp3'])
        time.sleep(120)
        subprocess.call(['pkill', '-P', str(proc1.pid)])
        proc1.kill()

    elif(counter == 1):
        time.sleep(5)
        proc1 = subprocess.Popen(args=['omxplayer', '-o', 'both', 'val2.mp3'])
        time.sleep(120)
        subprocess.call(['pkill', '-P', str(proc1.pid)])
        proc1.kill()

    elif(counter == 2):
        time.sleep(5)
        proc1 = subprocess.Popen(args=['omxplayer', '-o', 'both', 'val2.mp3'])
        time.sleep(120)
        subprocess.call(['pkill', '-P', str(proc1.pid)])
        proc1.kill()

    counter += 1
    counter %= 3


while True:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip",default="127.0.0.1", help="The ip to listen on")
    parser.add_argument("--port",type=int, default=9527, help="The port to listen on")
    args = parser.parse_args()

    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/signal", playsound, "signal")

    server = osc_server.ThreadingOSCUDPServer((args.ip, args.port), dispatcher)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()
