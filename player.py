from OSC import OSCServer,OSCClient, OSCMessage
from playsound import playsound
import time
import os
import signal
import sys

server = OSCServer(("0.0.0.0",9527))
counter = 0

def msg_callback(path, tags, args, source):
    global counter
    print(int(args[0]))
    if(counter == 0):
        time.sleep(5)
        playsound('val1.mp3')
        time.sleep(120)

    elif(counter==1):
        time.sleep(5)
        playsound('val2.mp3')
        time.sleep(120)

    elif(counter==2):
        time.sleep(5)
        playsound('val3.mp3')
        time.sleep(120)

    counter+=1
    counter%=3

server.addMsgHandler("/msg",msg_callback)
while True:
    server.handle_request()
